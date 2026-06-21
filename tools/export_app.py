"""
export_app.py — bundle an app in apps/<name>/ into a self-contained deliverable.

It reads the app's DIRECTIVE.md frontmatter, vendors `pynvdrive` and the
`oros_helpers` modules the app uses, then either zips the source or builds a
standalone .exe with PyInstaller.

Usage:
    python tools/export_app.py <app-name> [--target exe|source]

If --target is omitted, the export_target from DIRECTIVE.md is used.

NOTE for Claude: always CONFIRM the export form with the user before running this
(CLAUDE.md rule #6), even though a default exists.
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
APPS = WORKSPACE / "apps"
SHARED = WORKSPACE / "shared" / "oros_helpers"
PYNVDRIVE = WORKSPACE / "resources" / "Framework" / "Python" / "pynvdrive" / "pynvdrive"


def parse_frontmatter(directive_path):
    """Minimal YAML-frontmatter reader (no external deps)."""
    text = directive_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    block = text[3:end]
    data, key = {}, None
    for raw in block.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("- ") and key:
            data.setdefault(key, []).append(line.lstrip()[2:].strip())
        elif ":" in line:
            k, v = line.split(":", 1)
            key = k.strip()
            v = v.strip()
            data[key] = v if v else []
    return data


def build_bundle(app_name):
    app_dir = APPS / app_name
    if not app_dir.is_dir():
        sys.exit(f"App not found: {app_dir}")

    meta = parse_frontmatter(app_dir / "DIRECTIVE.md")
    dist = app_dir / "dist"
    staging = dist / app_name
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    # 1. copy the app code
    shutil.copytree(app_dir / "app", staging / "app")
    for fname in ("DIRECTIVE.md", "requirements.txt", "README.md"):
        src = app_dir / fname
        if src.exists():
            shutil.copy2(src, staging / fname)

    # 2. vendor pynvdrive
    shutil.copytree(PYNVDRIVE, staging / "pynvdrive")

    # 3. vendor the oros_helpers package (whole — it is small and its __init__
    #    imports its submodules, so partial copies would break the import).
    #    `helpers_used` in DIRECTIVE.md stays as documentation of intent.
    helper_pkg = staging / "oros_helpers"
    shutil.copytree(SHARED, helper_pkg, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    print(f"Staged self-contained bundle at: {staging}")
    return meta, app_dir, dist, staging


def export_source(app_name, dist, staging):
    zip_base = dist / app_name
    archive = shutil.make_archive(str(zip_base), "zip", root_dir=staging.parent,
                                  base_dir=staging.name)
    print(f"Source bundle created: {archive}")


def export_exe(meta, staging, dist, app_name):
    entry = meta.get("entry_point", "app/main.py")
    entry_path = staging / entry
    sep = ";" if sys.platform.startswith("win") else ":"
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--noconfirm", "--clean",
        "--name", app_name,
        "--paths", str(staging),
        "--add-data", f"{staging / 'pynvdrive'}{sep}pynvdrive",
        "--add-data", f"{staging / 'oros_helpers'}{sep}oros_helpers",
        "--distpath", str(dist),
        "--workpath", str(dist / "_build"),
        "--specpath", str(dist / "_build"),
        str(entry_path),
    ]
    print("Running PyInstaller:\n  " + " ".join(cmd))
    subprocess.check_call(cmd)
    print(f"Executable created in: {dist}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("app_name")
    ap.add_argument("--target", choices=["exe", "source"], default=None)
    args = ap.parse_args()

    meta, app_dir, dist, staging = build_bundle(args.app_name)
    target = args.target or meta.get("export_target", "source")

    if target == "exe":
        export_exe(meta, staging, dist, args.app_name)
    else:
        export_source(args.app_name, dist, staging)


if __name__ == "__main__":
    main()
