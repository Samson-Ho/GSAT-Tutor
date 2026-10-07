#!/usr/bin/env python3
"""Offline package checks; OpenAI's portal still performs its own review/scans."""
import argparse
import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

try:
    import yaml
    from jsonschema import Draft202012Validator
    from PIL import Image
except ImportError as exc:
    raise SystemExit("Install maintainer dependencies: python3 -m pip install -r requirements-dev.txt") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "scripts/schemas/plugin.schema.json"
SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
IDENTITY_FIELDS = ("name", "version", "description", "author", "homepage", "repository", "license", "keywords")
SEMVER = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)(?:\.(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?", re.ASCII)
CATEGORIES = {"Productivity", "Creativity", "Developer Tools", "Business & Operations", "Data & Analytics", "Communication", "Education & Research", "Security", "Finance", "Healthcare", "Travel", "Entertainment", "Other"}
SKILLS = {"gsat-math-a", "gsat-science", "gsat-english", "gsat-chinese", "gsat-chinese-writing"}
IGNORED = {".DS_Store", "__pycache__", ".pytest_cache", ".venv", "node_modules"}
LOCAL_PATH = re.compile(r"(?:/Users/|/home/|/private/|/opt/homebrew/|/usr/local/|[A-Za-z]:[\\/](?:Users|home)[\\/])")
SECRETS = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-(?:proj-)?[A-Za-z0-9_-]{24,}|AKIA[0-9A-Z]{16})\b|(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)\s*[:=]\s*[\"'][A-Za-z0-9+/=_-]{16,}[\"']", re.I)
FILE_REF = re.compile(r"(?<![\w:/])((?:\.{1,2}/)?(?:[\w.-]+/)*[\w.-]+\.(?:md|pdf|py|json|ya?ml|png|svg|webp|jpe?g))\b")


@dataclass
class Report:
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)

    def check(self, condition, message):
        if not condition:
            self.errors.append(message)


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path, report):
    try:
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_pairs)
        if not isinstance(value, dict):
            raise ValueError("expected a JSON object")
        return value
    except (OSError, ValueError) as exc:
        report.errors.append(f"{path.name}: {exc}")
        return {}


class UniqueYamlLoader(yaml.SafeLoader):
    """Reject duplicate fields rather than accepting the last declaration."""


def yaml_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str) or key in result:
            raise ValueError("non-string or duplicate YAML field")
        result[key] = loader.construct_object(value_node)
    return result


UniqueYamlLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, yaml_mapping)


def valid_text(value, limit, multiline=False):
    return (isinstance(value, str) and bool(value.strip()) and len(value) <= limit
            and all((multiline and c in "\n\r\t") or unicodedata.category(c) not in {"Cc", "Cf", "Zl", "Zp"} for c in value))


def valid_https(value, limit=1024):
    if not valid_text(value, limit) or any(c.isspace() for c in value):
        return False
    try:
        parsed = urlsplit(value)
        return parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password
    except ValueError:
        return False


def asset_path(root, value):
    if not isinstance(value, str) or not value.startswith("./") or "\\" in value:
        raise ValueError("asset path must start with ./ and use forward slashes")
    parts = PurePosixPath(value).parts
    if ".." in parts or ":" in value or value != value.strip() or any(ord(c) < 32 for c in value):
        raise ValueError("unsafe asset path")
    path = root / value
    if any(p.is_symlink() for p in [path, *path.parents]) or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("asset must be contained in the package without symlinks")
    if not path.is_file():
        raise ValueError("referenced asset file is missing")
    return path


def check_interface(root, interface, report):
    if not isinstance(interface, dict):
        report.errors.append("extensions.com.openai.interface must be an object")
        return
    for key, limit in {"displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80}.items():
        report.check(valid_text(interface.get(key), limit, key == "longDescription"), f"interface.{key}: required supported text, maximum {limit} characters")
    report.check(isinstance(interface.get("category"), str) and interface["category"] in CATEGORIES, "interface.category: unsupported category")
    caps = interface.get("capabilities", [])
    report.check(isinstance(caps, list) and len(caps) <= 20 and all(valid_text(c, 120) for c in caps), "interface.capabilities: at most 20 single-line labels, 120 characters each")
    prompts = interface.get("defaultPrompt", [])
    prompts = [prompts] if isinstance(prompts, str) else prompts
    if not isinstance(prompts, list):
        report.errors.append("interface.defaultPrompt must be a string or array")
    else:
        report.check(len(prompts) <= 3 and all(valid_text(p, 128) and "@" not in p for p in prompts), "interface.defaultPrompt: at most three single-line prompts, 128 characters, no @mentions")
        normalized = [" ".join(unicodedata.normalize("NFKC", p).split()) for p in prompts if isinstance(p, str)]
        report.check(len(normalized) == len(set(normalized)), "interface.defaultPrompt: duplicate prompts")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if key in interface:
            report.check(valid_https(interface[key]), f"interface.{key}: requires HTTPS without credentials, at most 1024 characters")
    for key in ("logo", "composerIcon", "logoDark", "composerIconDark"):
        if key not in interface:
            if key in {"logo", "composerIcon"}:
                report.errors.append(f"interface.{key}: include the distribution icon")
            continue
        try:
            path = asset_path(root, interface[key])
            report.check(path.stat().st_size <= 5 * 1024 * 1024, f"{key}: image exceeds 5 MiB")
            with Image.open(path) as image:
                report.check(image.format in {"PNG", "JPEG", "WEBP"}, f"{key}: unsupported raster format")
                suffixes = {"PNG": {".png"}, "JPEG": {".jpg", ".jpeg"}, "WEBP": {".webp"}}
                report.check(path.suffix.lower() in suffixes.get(image.format, set()), f"{key}: image extension does not match content")
                w, h = image.size
                report.check(w == h and 48 <= w <= 4096, f"{key}: icon must be square, 48–4096 pixels")
                image.verify()
        except (OSError, ValueError) as exc:
            report.errors.append(f"interface.{key}: {exc}")
    report.check(not interface.get("screenshots"), "skills-only package has no custom MCP UI: omit screenshots")


def runtime_files(root):
    """Explicit upload allowlist; never copy the repository wholesale."""
    files = [root / name for name in ("plugin.json", "README.md", "LICENSE", "PRIVACY.md", "SUPPORT.md")]
    for directory in ("skills", "assets"):
        if (root / directory).is_symlink():
            raise ValueError(f"symlink not allowed: {directory}")
        for path in sorted((root / directory).rglob("*")):
            if path.is_symlink():
                raise ValueError(f"symlink not allowed: {path.relative_to(root)}")
            if any(part in IGNORED or part.startswith(".") or part.endswith((".pyc", ".pyo", ".swp", "~")) for part in path.relative_to(root).parts):
                continue
            if path.is_file():
                files.append(path)
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def check_references(path, skill, report):
    text = path.read_text(encoding="utf-8")
    refs = set()
    for code in re.findall(r"(?<!`)`([^`\n]+)`(?!`)", text):
        refs.update(FILE_REF.findall(code))
    for target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
        target = target.split()[0].strip("<>")
        if urlsplit(target).scheme or target.startswith("#"):
            continue
        refs.add(unquote(target.split("#", 1)[0]))
    for ref in refs:
        candidates = [path.parent / ref, skill / ref]
        if "/" not in ref:
            candidates.append(skill / "references" / ref)
        report.check(any(p.exists() and p.resolve().is_relative_to(skill.resolve()) for p in candidates), f"{path.relative_to(skill)}: missing or escaping reference {ref}")


def validate(root=ROOT, compatibility=True):
    root = Path(root).resolve()
    report = Report()
    manifest = read_json(root / "plugin.json", report)
    schema = read_json(SCHEMA, report)
    for error in Draft202012Validator(schema).iter_errors(manifest):
        report.errors.append(f"plugin.json {'/'.join(map(str, error.path))}: {error.message}")
    if report.errors:
        return report
    report.check(manifest.get("$schema") == SCHEMA_URL, "plugin.json: use the verified Agent Plugins 1.0.0 schema")
    report.check(manifest.get("name") == "gsat-tutor", "package identifier must remain gsat-tutor")
    version = manifest.get("version")
    report.check(isinstance(version, str) and len(version) <= 64 and bool(SEMVER.fullmatch(version)), "plugin.json: invalid semantic version")
    report.check(valid_text(manifest.get("description"), 4000, True), "plugin.json: missing/invalid description")
    author = manifest.get("author", {})
    report.check(isinstance(author, dict) and valid_text(author.get("name"), 120), "plugin.json: missing/invalid author.name")
    extension = manifest.get("extensions", {}).get("com.openai", {})
    if not isinstance(extension, dict):
        report.errors.append("extensions.com.openai must be an object")
        extension = {}
    report.check(not any(extension.get(key) is not None for key in ("apps", "hooks", "mcpServers", "skills")), "skills-only portable extension must not declare apps, hooks, MCP or alternative skill directories")
    check_interface(root, extension.get("interface"), report)
    if compatibility:
        claude = read_json(root / ".claude-plugin/plugin.json", report)
        for key in IDENTITY_FIELDS:
            report.check(manifest.get(key) == claude.get(key), f"Claude/root metadata mismatch: {key}")
        report.check(claude.get("displayName") == extension.get("interface", {}).get("displayName"), "Claude/root displayName mismatch")
        marketplace = read_json(root / ".claude-plugin/marketplace.json", report)
        report.check(marketplace.get("name") == "gsat-tutor-marketplace", "legacy marketplace name changed")
        entries = marketplace.get("plugins", [])
        report.check(isinstance(entries, list) and len(entries) == 1 and isinstance(entries[0], dict) and entries[0].get("name") == "gsat-tutor" and entries[0].get("source") == "./", "legacy marketplace must retain one gsat-tutor entry with source ./ (repository root)")
        overlay = root / ".codex-plugin/plugin.json"
        if overlay.exists():
            codex = read_json(overlay, report)
            for key in IDENTITY_FIELDS:
                report.check(codex.get(key) == manifest.get(key), f"Codex/root metadata mismatch: {key}")
            report.check(codex.get("interface") == extension.get("interface"), "Codex/root interface mismatch")
            report.check(codex.get("skills") == "./skills/", "Codex fallback must resolve skills from the plugin root")
        report.check(not (root / ".agents/plugins/marketplace.json").exists(), "do not introduce a duplicate native marketplace")
    dirs = [p for p in (root / "skills").iterdir() if p.is_dir()] if (root / "skills").is_dir() else []
    report.check({p.name for p in dirs} == SKILLS, "package must preserve all five subject skill directories")
    for skill in dirs:
        try:
            text = (skill / "SKILL.md").read_text(encoding="utf-8")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", text, re.S)
            if not match:
                raise ValueError("missing YAML frontmatter delimiters")
            header = yaml.load(match[1], Loader=UniqueYamlLoader)
            if not isinstance(header, dict):
                raise ValueError("frontmatter must be a mapping")
            report.check(header.get("name") == skill.name and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name)), f"{skill.name}: skill name/folder mismatch")
            report.check(len(f"gsat-tutor:{skill.name}") <= 64, f"{skill.name}: combined skill identity exceeds 64 characters")
            report.check(valid_text(header.get("description"), 1024, True), f"{skill.name}: invalid description (maximum 1024 characters)")
            report.check(bool(match[2].strip()), f"{skill.name}: empty instructions")
            for path in skill.rglob("*.md"):
                check_references(path, skill, report)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            report.errors.append(f"{skill.name}: {exc}")
    try:
        paths = runtime_files(root)
        normalized = set()
        for path in paths:
            rel = path.relative_to(root).as_posix()
            key = unicodedata.normalize("NFC", rel).casefold()
            report.check(key not in normalized, f"archive path collision: {rel}")
            normalized.add(key)
            report.check(path.is_file() and not path.is_symlink(), f"missing/nonregular package file: {rel}")
            report.check(not any(p.lower() in {".env", ".aws", "credentials", "secrets", "id_rsa", "id_ed25519"} or p.lower().endswith((".pem", ".key")) for p in path.parts), f"credential file in package: {rel}")
            if not path.is_file():
                continue
            if path.suffix == ".pdf":
                with path.open("rb") as source:
                    report.check(source.read(5) == b"%PDF-", f"invalid PDF asset: {rel}")
            elif path.suffix in {".md", ".py", ".json", ".yaml", ".yml", ".txt"}:
                content = path.read_text(encoding="utf-8")
                report.check(not LOCAL_PATH.search(content), f"developer-machine absolute path in {rel}")
                report.check(not SECRETS.search(content), f"possible secret in {rel} (value withheld)")
                if path.suffix == ".json":
                    read_json(path, report)
        for name in ("mcp.json", ".mcp.json", ".app.json", "hooks/hooks.json"):
            report.check(not (root / name).exists(), f"unexpected component in skills-only package: {name}")
    except (OSError, ValueError) as exc:
        report.errors.append(str(exc))
    report.warnings.append("Portal identity verification, safety/security scans, policy attestations, approval and publication remain required.")
    report.warnings.append("PRIVACY.md is bundled; publish it to a public HTTPS page before final review and set privacyPolicyURL after verifying the page.")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--package-only", action="store_true", help="validate a staged/extracted public package without legacy manifests")
    args = parser.parse_args()
    report = validate(args.root, compatibility=not args.package_only)
    for error in report.errors:
        print(f"ERROR: {error}")
    for warning in report.warnings:
        print(f"NOTE: {warning}")
    print(f"{'FAILED' if report.errors else 'PASS'}: package checks ({len(report.errors)} errors)")
    return bool(report.errors)


if __name__ == "__main__":
    raise SystemExit(main())
