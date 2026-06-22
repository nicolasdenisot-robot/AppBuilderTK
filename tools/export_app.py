"""
export_app.py — package an app into a ready-to-ship operator deliverable.

Reads the app's DIRECTIVE.md frontmatter, vendors pynvdrive + oros_helpers,
then builds a versioned folder at:

    apps/<name>/dist/<name>-v<version>-<target>/

The tool does not zip — it leaves the folder ready for you to inspect, zip,
and send.

── Exe delivery (operator needs nothing pre-installed) ──────────────────────
    <name>-v<version>-exe/
        <name>.exe                   standalone — Python not required
        install_to_nvgate.bat        run once: adds to NVGate Automation
        README.txt

── Source / bat delivery (operator needs Python installed) ──────────────────
    <name>-v<version>-source/
        app/                         Python source
        pynvdrive/  oros_helpers/    bundled SDK — workspace not required
        launch_<name>.bat            double-click to run
        setup.bat                    run once: pip install -r requirements.txt
        install_to_nvgate.bat        run once: adds to NVGate Automation
        requirements.txt
        README.txt

── DIRECTIVE.md frontmatter fields used by this tool ────────────────────────
    version: 1.0           → folder / zip name  (default: 1.0)
    display_name: My App   → NVGate Automation label + exe/bat name
                             (optional; derived from app_name if absent)
    export_target: exe|source
    entry_point: app/main.py

Usage:
    python tools/export_app.py <app-name> [--target exe|source]

NOTE for Claude: always CONFIRM the export form with the user before running
(CLAUDE.md rule #6 / stop #6).
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
APPS      = WORKSPACE / "apps"
SHARED    = WORKSPACE / "shared" / "oros_helpers"
LOGOS     = WORKSPACE / "shared" / "assets" / "logos"
PYNVDRIVE = (WORKSPACE / "resources" / "Framework"
             / "Python" / "pynvdrive" / "pynvdrive")
LINKS_DIR = r"C:\OROS\NVGate data\Links"


# ── DIRECTIVE.md reader ───────────────────────────────────────────────────────

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


# ── helpers ───────────────────────────────────────────────────────────────────

def make_display_name(app_name, meta):
    """Return display_name from meta, or derive one.  thd-ui → THD UI."""
    if meta.get("display_name"):
        return meta["display_name"]
    return " ".join(s.upper() for s in app_name.replace("_", "-").split("-"))


def find_launcher_bat(app_dir):
    """Return the launch_*.bat in the app folder (first alphabetically), or None."""
    candidates = sorted(app_dir.glob("launch_*.bat"))
    return candidates[0] if candidates else None


def find_readme(app_dir, target):
    """Return README-<target>.md if it exists, else README.md, else None."""
    specific = app_dir / f"README-{target}.md"
    if specific.exists():
        return specific
    generic = app_dir / "README.md"
    return generic if generic.exists() else None


def _bat(path, lines):
    """Write lines as a batch file. LF-only is fine on modern Windows cmd."""
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── staging (common to both targets) ─────────────────────────────────────────

def build_staging(app_dir, dist, logo_brand="oros"):
    """Copy app source + vendors into dist/_staging/. Returns the staging path."""
    staging = dist / "_staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    shutil.copytree(app_dir / "app", staging / "app")
    _no_cache = shutil.ignore_patterns("__pycache__", "*.pyc")
    shutil.copytree(PYNVDRIVE, staging / "pynvdrive", ignore=_no_cache)
    shutil.copytree(SHARED, staging / "oros_helpers", ignore=_no_cache)

    # Copy brand logos into staging/app/ so they are available at runtime
    # (source delivery) and picked up by the asset-bundling loop (exe delivery).
    logo_dir = LOGOS / logo_brand
    for variant in ("logo_color.png", "logo_white.png"):
        src = logo_dir / variant
        if src.exists():
            shutil.copy2(src, staging / "app" / variant)
            print(f"  Logo         : {logo_brand}/{variant}")
        else:
            print(f"  WARNING: logo not found: {src}")
    return staging


# ── generated bat files ───────────────────────────────────────────────────────

def _install_bat_exe(pkg_dir, app_name, display_name):
    """Write install_to_nvgate.bat for exe delivery."""
    exe_name  = f"{app_name}.exe"
    link_bat  = f"{display_name}.bat"
    _bat(pkg_dir / "install_to_nvgate.bat", [
        "@echo off",
        f"REM -- {display_name} -- NVGate Automation installer",
        "REM Run this script ONCE after unzipping.",
        f'REM Adds "{display_name}" to NVGate Automation / Execute.',
        f"REM To uninstall: delete  {LINKS_DIR}\\{link_bat}",
        "",
        f'set "APP_EXE=%~dp0{exe_name}"',
        f'set "LINKS_DIR={LINKS_DIR}"',
        f'set "LINK_FILE=%LINKS_DIR%\\{link_bat}"',
        "",
        "echo.",
        f"echo Installing: {display_name}",
        "echo   App          : %APP_EXE%",
        "echo   NVGate Links : %LINK_FILE%",
        "echo.",
        "",
        'if not exist "%APP_EXE%" (',
        f'    echo ERROR: {exe_name} not found.',
        "    echo Run install_to_nvgate.bat from the same folder as the .exe.",
        "    echo.",
        "    pause",
        "    exit /b 1",
        ")",
        "",
        'if not exist "%LINKS_DIR%\\" (',
        "    echo ERROR: NVGate Links folder not found:",
        "    echo   %LINKS_DIR%",
        "    echo Check that NVGate is installed on this PC.",
        "    echo.",
        "    pause",
        "    exit /b 1",
        ")",
        "",
        "(",
        "    echo @echo off",
        '    echo "%APP_EXE%"',
        ') > "%LINK_FILE%"',
        "",
        "if errorlevel 1 (",
        "    echo ERROR: Could not write to the Links folder.",
        "    echo Try running this script as Administrator.",
        "    echo.",
        "    pause",
        "    exit /b 1",
        ")",
        "",
        "echo.",
        "echo Done.",
        f'echo "{display_name}" now appears in NVGate under Automation / Execute.',
        "echo.",
        "pause",
    ])


def _install_bat_source(pkg_dir, launcher_name, display_name):
    """Write install_to_nvgate.bat for source delivery."""
    link_bat = f"{display_name}.bat"
    _bat(pkg_dir / "install_to_nvgate.bat", [
        "@echo off",
        f"REM -- {display_name} -- NVGate Automation installer",
        "REM Run this script ONCE (after setup.bat) to register the app in NVGate.",
        f'REM Adds "{display_name}" to NVGate Automation / Execute.',
        f"REM To uninstall: delete  {LINKS_DIR}\\{link_bat}",
        "",
        f'set "APP_BAT=%~dp0{launcher_name}"',
        f'set "LINKS_DIR={LINKS_DIR}"',
        f'set "LINK_FILE=%LINKS_DIR%\\{link_bat}"',
        "",
        "echo.",
        f"echo Installing: {display_name}",
        "echo   App launcher : %APP_BAT%",
        "echo   NVGate Links : %LINK_FILE%",
        "echo.",
        "",
        'if not exist "%APP_BAT%" (',
        f'    echo ERROR: {launcher_name} not found.',
        "    echo Run install_to_nvgate.bat from the same folder as the launcher.",
        "    echo.",
        "    pause",
        "    exit /b 1",
        ")",
        "",
        'if not exist "%LINKS_DIR%\\" (',
        "    echo ERROR: NVGate Links folder not found:",
        "    echo   %LINKS_DIR%",
        "    echo Check that NVGate is installed on this PC.",
        "    echo.",
        "    pause",
        "    exit /b 1",
        ")",
        "",
        "(",
        "    echo @echo off",
        '    echo call "%APP_BAT%"',
        ') > "%LINK_FILE%"',
        "",
        "if errorlevel 1 (",
        "    echo ERROR: Could not write to the Links folder.",
        "    echo Try running this script as Administrator.",
        "    echo.",
        "    pause",
        "    exit /b 1",
        ")",
        "",
        "echo.",
        "echo Done.",
        f'echo "{display_name}" now appears in NVGate under Automation / Execute.',
        "echo.",
        "pause",
    ])


def _setup_bat(pkg_dir, display_name):
    """Write setup.bat for source delivery (installs Python packages)."""
    _bat(pkg_dir / "setup.bat", [
        "@echo off",
        f"REM -- {display_name} -- first-time Python package installation",
        "REM Run this script ONCE before first use.",
        "REM Python must be installed on this PC.  Download: https://python.org",
        "",
        "echo.",
        f"echo Setting up {display_name}...",
        'pip install -r "%~dp0requirements.txt"',
        "if errorlevel 1 (",
        "    echo.",
        "    echo ERROR: installation failed.",
        "    echo Make sure Python is installed and accessible.",
        "    pause",
        "    exit /b 1",
        ")",
        "echo.",
        "echo Done. You can now run the application.",
        "pause",
    ])


# ── per-target packaging ──────────────────────────────────────────────────────

def package_source(app_dir, dist, pkg_dir, display_name, target="source"):
    """Assemble the source operator package in pkg_dir."""
    staging = dist / "_staging"

    shutil.copytree(staging / "app",          pkg_dir / "app")
    shutil.copytree(staging / "pynvdrive",    pkg_dir / "pynvdrive")
    shutil.copytree(staging / "oros_helpers", pkg_dir / "oros_helpers")

    launcher = find_launcher_bat(app_dir)
    if launcher:
        shutil.copy2(launcher, pkg_dir / launcher.name)
        launcher_name = launcher.name
        print(f"  Launcher     : {launcher.name}")
    else:
        print("  WARNING: no launch_*.bat found — operator will have no launcher.")
        launcher_name = "launch.bat"

    for fname in ("requirements.txt",):
        src = app_dir / fname
        if src.exists():
            shutil.copy2(src, pkg_dir / fname)
    readme = find_readme(app_dir, target)
    if readme:
        shutil.copy2(readme, pkg_dir / "README.txt")
        print(f"  README       : {readme.name} -> README.txt")

    _setup_bat(pkg_dir, display_name)
    _install_bat_source(pkg_dir, launcher_name, display_name)


def package_exe(app_dir, dist, staging, pkg_dir, meta, app_name, display_name):
    """Run PyInstaller, then assemble the clean 3-file exe operator package."""
    entry      = meta.get("entry_point", "app/main.py")
    entry_path = staging / entry
    sep        = ";" if sys.platform.startswith("win") else ":"

    exe_out  = dist / "_exe_out"
    exe_work = dist / "_build"

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--noconfirm", "--clean",
        "--name", app_name,
        "--paths", str(staging),
        "--add-data", f"{staging / 'pynvdrive'}{sep}pynvdrive",
        "--add-data", f"{staging / 'oros_helpers'}{sep}oros_helpers",
        "--distpath", str(exe_out),
        "--workpath", str(exe_work),
        "--specpath", str(exe_work),
        str(entry_path),
    ]
    # Bundle any non-Python asset files from app/ (logos, icons, config, etc.)
    for asset in sorted((staging / "app").glob("*")):
        if asset.is_file() and asset.suffix not in (".py", ".pyc", ".spec"):
            cmd += ["--add-data", f"{asset}{sep}."]
            print(f"  Asset        : {asset.name}")
    print(f"  Running PyInstaller...")
    subprocess.check_call(cmd)

    exe_src = exe_out / f"{app_name}.exe"
    if not exe_src.exists():
        sys.exit(f"PyInstaller did not produce: {exe_src}")

    shutil.copy2(exe_src, pkg_dir / f"{app_name}.exe")
    print(f"  Exe built    : {pkg_dir / f'{app_name}.exe'}")

    readme = find_readme(app_dir, "exe")
    if readme:
        shutil.copy2(readme, pkg_dir / "README.txt")
        print(f"  README       : {readme.name} -> README.txt")

    _install_bat_exe(pkg_dir, app_name, display_name)

    shutil.rmtree(exe_out,  ignore_errors=True)
    shutil.rmtree(exe_work, ignore_errors=True)


# ── entry point ───────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description="Package an NVGate app into an operator-ready deliverable.")
    ap.add_argument("app_name", help="App folder name under apps/")
    ap.add_argument("--target", choices=["exe", "source"], default=None,
                    help="Override export_target from DIRECTIVE.md")
    args = ap.parse_args()

    app_name = args.app_name
    app_dir  = APPS / app_name
    if not app_dir.is_dir():
        sys.exit(f"App not found: {app_dir}")

    meta    = parse_frontmatter(app_dir / "DIRECTIVE.md")
    version = meta.get("version", "1.0")
    display = make_display_name(app_name, meta)
    target  = args.target or meta.get("export_target", "source")
    logo    = meta.get("logo", "oros")

    dist    = app_dir / "dist"
    dist.mkdir(exist_ok=True)

    pkg_name = f"{app_name}-v{version}-{target}"
    pkg_dir  = dist / pkg_name
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)
    pkg_dir.mkdir()

    print(f"\nPackaging  '{app_name}'")
    print(f"  Version      : {version}")
    print(f"  Display name : {display}")
    print(f"  Target       : {target}")
    print(f"  Logo brand   : {logo}")
    print(f"  Output       : {pkg_dir}\n")

    staging = build_staging(app_dir, dist, logo)

    if target == "exe":
        package_exe(app_dir, dist, staging, pkg_dir, meta, app_name, display)
    else:
        package_source(app_dir, dist, pkg_dir, display, target)

    shutil.rmtree(staging, ignore_errors=True)

    SEP = "=" * 60
    print(f"\n{SEP}")
    print(f"Delivery folder ready — check the contents, then zip and send.")
    print(f"  {pkg_dir}")
    print(f"\nOperator steps after unzipping:")
    if target == "source":
        print(f"  1. Run setup.bat              (installs Python packages, once)")
        print(f"  2. Run install_to_nvgate.bat  (registers in NVGate, once)")
        print(f"  3. Launch via NVGate Automation, or double-click the launcher.")
    else:
        print(f"  1. Run install_to_nvgate.bat  (registers in NVGate, once)")
        print(f"  2. Launch via NVGate Automation, or double-click {app_name}.exe.")
    print(SEP + "\n")


if __name__ == "__main__":
    main()
