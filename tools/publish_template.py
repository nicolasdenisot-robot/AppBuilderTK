"""
publish_template.py — publish the CLEAN customer template from this workspace.

This workspace is your PRIVATE working copy: you build and test real apps in
apps/, and back the whole thing up with /sync-github. Customers must NOT receive
any of that. This tool copies ONLY an explicit allowlist of kit files into the
separate template repo and pushes it.

Because it is an allowlist (not a denylist), anything you add to the workspace
later — new apps, notes, .env, personal files — is NEVER published unless you
add it here on purpose.

Usage:
    python tools/publish_template.py [--repo OWNER/NAME] [--message "..."] [--dry-run]

Default repo: chaorandu-ai/oros-nvgate-app-builder (the template; override with --repo).
The template repo must already exist (create it once with:
    gh repo create OWNER/oros-nvgate-app-builder --private ).
"""

import argparse
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
DEFAULT_REPO = "chaorandu-ai/oros-nvgate-app-builder"   # the customer template repo

# --- WHAT CUSTOMERS GET (allowlist of paths, relative to workspace root) -----
INCLUDE = [
    "CLAUDE.md",
    "README.md",
    "LICENSE",
    ".gitignore",
    ".claude/settings.json",
    # Customer-facing skills only. publish-template and audit-workspace are
    # maintainer-only and NOT shipped.
    ".claude/skills/sync-github",
    ".claude/skills/explore-codebase",
    ".claude/skills/scope-feature",
    ".claude/skills/frontend-design",
    ".claude/skills/checkpoint",
    ".claude/skills/restore",
    "docs",
    "shared",
    "apps/_template",            # ONLY the template app, never real apps
    "resources/README.md",
    "resources/AI",              # OROS machine-readable reference kit (v1.7)
    "resources/llms.txt",        # map of that kit
    "tools/export_app.py",
    "tools/README.md",
    # NOTE: tools/publish_template.py is intentionally NOT shipped — it's yours.
    # NOTE: workspace-overview-deck.html is intentionally NOT shipped as a file.
    #       It is hosted as a public web page (see the "Workspace overview" link in
    #       README.md) so recipients see the rendered deck, not GitHub's code view.
]

# Names skipped anywhere during copy (defensive; INCLUDE already scopes things).
EXCLUDE_NAMES = {"__pycache__", ".tmp", "dist", "build", ".env", ".git"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}


def _on_rm_error(func, path, _exc):
    os.chmod(path, stat.S_IWRITE)
    func(path)


def _ignore(_dir, names):
    skip = set()
    for n in names:
        if n in EXCLUDE_NAMES or Path(n).suffix in EXCLUDE_SUFFIXES:
            skip.add(n)
    return skip


def copy_allowlist(dest_root):
    copied = []
    for rel in INCLUDE:
        src = WORKSPACE / rel
        dst = dest_root / rel
        if not src.exists():
            print(f"  ! skip (missing): {rel}")
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            shutil.copytree(src, dst, ignore=_ignore, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)
        copied.append(rel)
    return copied


def clear_except_git(root):
    for child in root.iterdir():
        if child.name == ".git":
            continue
        if child.is_dir():
            shutil.rmtree(child, onerror=_on_rm_error)
        else:
            child.unlink()


def run(cmd, cwd):
    print("  $", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(cwd))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=DEFAULT_REPO, help="OWNER/NAME of the template repo")
    ap.add_argument("--message", default="Update template from workspace")
    ap.add_argument("--dry-run", action="store_true",
                    help="stage the clean copy locally but do not clone/commit/push")
    args = ap.parse_args()

    staging = WORKSPACE / ".tmp" / "template-publish"
    staging.parent.mkdir(parents=True, exist_ok=True)
    if staging.exists():
        shutil.rmtree(staging, onerror=_on_rm_error)

    if args.dry_run:
        staging.mkdir(parents=True)
        print("Dry run — staging clean template at:", staging)
        copied = copy_allowlist(staging)
        print("\nWould publish these top-level items:")
        for rel in copied:
            print("  -", rel)
        print(f"\n(no git actions; inspect {staging})")
        return

    repo_url = f"https://github.com/{args.repo}.git"
    print(f"Cloning template repo {args.repo} ...")
    run(["git", "clone", repo_url, str(staging)], cwd=WORKSPACE)

    print("Clearing old content (keeping .git) ...")
    clear_except_git(staging)

    print("Copying clean kit (allowlist) ...")
    copied = copy_allowlist(staging)
    for rel in copied:
        print("  +", rel)

    print("Committing and pushing ...")
    run(["git", "add", "-A"], cwd=staging)
    # commit may be a no-op if nothing changed; tolerate that
    res = subprocess.run(["git", "commit", "-m", args.message], cwd=str(staging))
    if res.returncode != 0:
        print("  (nothing to commit — template already up to date)")
    else:
        run(["git", "branch", "-M", "main"], cwd=staging)
        run(["git", "push", "-u", "origin", "main"], cwd=staging)

    print(f"\nDone. Customer template published to {args.repo}.")


if __name__ == "__main__":
    main()
