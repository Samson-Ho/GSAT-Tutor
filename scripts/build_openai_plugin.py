#!/usr/bin/env python3
"""Build a deterministic skills-only ZIP from an explicit runtime allowlist."""
import argparse
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path

from validate_plugin import ROOT, runtime_files, validate


def build(root=ROOT, output_dir=None):
    root = Path(root).resolve()
    report = validate(root)
    if report.errors:
        raise ValueError("Package validation failed:\n" + "\n".join(report.errors))
    for note in report.warnings:
        print(f"NOTE: {note}")
    import json
    manifest = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    dest = Path(output_dir).resolve() if output_dir else root / "dist"
    # Never stage into or overwrite runtime source files.
    if dest == root or dest.is_relative_to(root / "skills") or dest.is_relative_to(root / "assets"):
        raise ValueError("output directory must be separate from runtime source files")
    dest.mkdir(parents=True, exist_ok=True)
    target = dest / f"{name}-openai-{version}.zip"
    with tempfile.TemporaryDirectory(prefix="gsat-openai-") as tmp:
        stage = Path(tmp) / name
        stage.mkdir()
        for source in runtime_files(root):
            staged = stage / source.relative_to(root)
            staged.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, staged)
        staged_report = validate(stage, compatibility=False)
        if staged_report.errors:
            raise ValueError("Staged package failed validation:\n" + "\n".join(staged_report.errors))
        archive_path = Path(tmp) / target.name
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for source in runtime_files(stage):
                info = zipfile.ZipInfo(f"{name}/{source.relative_to(stage).as_posix()}", date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, source.read_bytes(), compresslevel=9)
        if archive_path.stat().st_size > 100_000_000:
            raise ValueError("ZIP exceeds the portal's 100 MB compressed limit")
        with zipfile.ZipFile(archive_path) as archive:
            if archive.testzip() is not None:
                raise ValueError("ZIP integrity check failed")
            expected = {f"{name}/{p.relative_to(stage).as_posix()}" for p in runtime_files(stage)}
            if set(archive.namelist()) != expected:
                raise ValueError("ZIP inventory differs from validated staging files")
            extracted = Path(tmp) / "extracted"
            archive.extractall(extracted)
        final_report = validate(extracted / name, compatibility=False)
        if final_report.errors:
            raise ValueError("Extracted ZIP failed validation:\n" + "\n".join(final_report.errors))
        shutil.copyfile(archive_path, target)
    print(f"Built: {target}")
    print(f"SHA256: {hashlib.sha256(target.read_bytes()).hexdigest()}")
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    try:
        build(args.root, args.output_dir)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
