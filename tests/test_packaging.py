"""Regression checks for upload safety, determinism, and legacy compatibility."""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_openai_plugin import build
from validate_plugin import runtime_files, validate


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="gsat-package-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        self.root.mkdir()
        # Copy mutable text/branding; hard-link large read-only PDF fixtures.
        for source in runtime_files(ROOT):
            dest = self.root / source.relative_to(ROOT)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if source.suffix == ".pdf":
                try:
                    os.link(source, dest)
                except OSError:
                    shutil.copyfile(source, dest)
            else:
                shutil.copyfile(source, dest)
        shutil.copytree(ROOT / ".claude-plugin", self.root / ".claude-plugin")

    def change_manifest(self, mutate):
        path = self.root / "plugin.json"
        manifest = json.loads(path.read_text())
        mutate(manifest)
        path.write_text(json.dumps(manifest, ensure_ascii=False))

    def assert_rejected(self, message):
        report = validate(self.root)
        self.assertTrue(any(message in error for error in report.errors), report.errors)

    def test_repository_and_yaml_descriptions(self):
        self.assertEqual(validate(self.root).errors, [])

    def test_official_schema_rejects_invented_fields(self):
        self.change_manifest(lambda m: m.update(skills="./skills/"))
        self.assert_rejected("Additional properties")

    def test_version_drift_and_invalid_semver(self):
        self.change_manifest(lambda m: m.update(version="1.2.1"))
        self.assert_rejected("metadata mismatch: version")
        self.change_manifest(lambda m: m.update(version="01.2.0"))
        self.assert_rejected("invalid semantic version")

    def test_invalid_json_exits_nonzero(self):
        (self.root / "plugin.json").write_text('{"name":')
        run = subprocess.run([sys.executable, str(ROOT / "scripts/validate_plugin.py"), "--root", str(self.root)], capture_output=True, text=True)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("ERROR", run.stdout)

    def test_frontmatter_failures(self):
        path = self.root / "skills/gsat-math-a/SKILL.md"
        path.write_text("---\nname: gsat-math-a\ndescription: invalid: colon\n---\nBody\n")
        self.assert_rejected("mapping values")
        path.write_text("---\nname: gsat-math-a\nname: duplicate\ndescription: text\n---\nBody\n")
        self.assert_rejected("duplicate YAML")
        path.write_text("---\nname: wrong\ndescription: text\n---\nBody\n")
        self.assert_rejected("name/folder mismatch")

    def test_missing_subject_or_skill_instructions(self):
        path = self.root / "skills/gsat-chinese/SKILL.md"
        path.unlink()
        self.assert_rejected("gsat-chinese")
        shutil.rmtree(self.root / "skills/gsat-chinese")
        self.assert_rejected("all five")

    def test_missing_and_escaping_references(self):
        path = self.root / "skills/gsat-science/SKILL.md"
        original = path.read_text()
        path.write_text(original + "\nRead `references/missing.md`.\n")
        self.assert_rejected("missing.md")
        path.write_text(original + "\nRead [outside](../../README.md).\n")
        self.assert_rejected("escaping reference")
        (self.root / "skills/gsat-science/assets/papers/gsat-111.pdf").unlink()
        self.assert_rejected("gsat-111.pdf")

    def test_listing_final_limits_and_duplicate_prompts(self):
        self.change_manifest(lambda m: m["extensions"]["com.openai"]["interface"].update(shortDescription="x" * 31, defaultPrompt=["test", " test  "]))
        self.assert_rejected("shortDescription")
        self.assert_rejected("duplicate prompts")

    def test_invalid_category_and_prompt_mention(self):
        self.change_manifest(lambda m: m["extensions"]["com.openai"]["interface"].update(category="Education", defaultPrompt="@gsat-tutor hello"))
        self.assert_rejected("unsupported category")
        self.assert_rejected("@mentions")

    def test_credential_url_and_unsafe_icon(self):
        self.change_manifest(lambda m: m["extensions"]["com.openai"]["interface"].update(supportURL="https://user:password@example.com", logo="./../outside.png"))
        self.assert_rejected("supportURL")
        self.assert_rejected("unsafe asset")

    def test_missing_or_corrupt_icon(self):
        icon = self.root / "assets/icon.png"
        icon.write_bytes(b"not an image")
        self.assert_rejected("cannot identify image")
        icon.unlink()
        self.assert_rejected("asset file is missing")

    def test_secret_and_machine_path_are_rejected_without_leaking_value(self):
        path = self.root / "skills/gsat-science/references/private.md"
        fake = "sk-" + "x" * 30
        path.write_text("token=" + fake + "\n/Users/developer/private.txt")
        report = validate(self.root)
        self.assertTrue(any("possible secret" in e for e in report.errors))
        self.assertTrue(any("absolute path" in e for e in report.errors))
        self.assertNotIn(fake, "\n".join(report.errors))

    def test_symlink_is_rejected(self):
        path = self.root / "skills/gsat-science/references/outside.md"
        try:
            path.symlink_to(ROOT / "README.md")
        except (OSError, NotImplementedError):
            self.skipTest("environment does not permit symlinks")
        self.assert_rejected("symlink not allowed")

    def test_marketplace_source_and_duplicate_entry_are_rejected(self):
        path = self.root / ".claude-plugin/marketplace.json"
        catalog = json.loads(path.read_text())
        catalog["plugins"][0]["source"] = "./skills/"
        path.write_text(json.dumps(catalog))
        self.assert_rejected("source ./")
        catalog["plugins"][0]["source"] = "./"
        catalog["plugins"].append(catalog["plugins"][0])
        path.write_text(json.dumps(catalog))
        self.assert_rejected("one gsat-tutor entry")

    def test_app_bindings_and_mcp_are_rejected(self):
        self.change_manifest(lambda m: m["extensions"]["com.openai"].update(apps="./.app.json"))
        self.assert_rejected("must not declare")
        (self.root / "mcp.json").write_text("{}")
        self.assert_rejected("unexpected component")

    def test_deterministic_zip_and_clean_inventory(self):
        clutter = self.root / "skills/gsat-science/__pycache__/sample.pyc"
        clutter.parent.mkdir()
        clutter.write_bytes(b"cache")
        (self.root / "skills/gsat-science/.env").write_text("PRIVATE=do-not-package")
        (self.root / "skills/gsat-science/.DS_Store").write_bytes(b"finder")
        dev = self.root / "evals/run-output.md"
        dev.parent.mkdir()
        dev.write_text("development output")
        with contextlib.redirect_stdout(io.StringIO()):
            archive = build(self.root)
            first = hashlib.sha256(archive.read_bytes()).digest()
            # Source mtimes must not affect archive bytes.
            (self.root / "plugin.json").touch()
            build(self.root)
        self.assertEqual(first, hashlib.sha256(archive.read_bytes()).digest())
        with zipfile.ZipFile(archive) as zipped:
            names = zipped.namelist()
            self.assertIn("gsat-tutor/plugin.json", names)
            self.assertIn("gsat-tutor/assets/icon.png", names)
            self.assertEqual(sum(n.endswith("/SKILL.md") for n in names), 5)
            self.assertEqual(sum(n.endswith(".pdf") for n in names), 41)
            for forbidden in (".claude-plugin", ".codex-plugin", ".git/", "__pycache__", ".env", ".DS_Store", "evals/", "scripts/build", "requirements-dev"):
                self.assertFalse(any(forbidden in n for n in names), forbidden)
            self.assertIsNone(zipped.testzip())


class ExistingVocabularyTests(unittest.TestCase):
    def test_bundled_vocabulary_helper_without_working_directory_dependency(self):
        path = ROOT / "skills/gsat-english/scripts/vocab_level.py"
        spec = importlib.util.spec_from_file_location("vocab_level", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        table = module.load()
        self.assertEqual(module.level_of("abandon", table), (4, "abandon"))
        self.assertEqual(module.level_of("went", table)[0], table["go"])
        self.assertEqual(module.level_of("zzunlistedwordzz", table), (None, None))
        run = subprocess.run([sys.executable, str(path), "abandon", "zzunlistedwordzz"], cwd=tempfile.gettempdir(), capture_output=True, text=True, check=True)
        self.assertIn("abandon: L4", run.stdout)
        self.assertIn("not in 參考詞彙表", run.stdout)


if __name__ == "__main__":
    unittest.main()
