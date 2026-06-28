"""
Locate files the app ships with (logo, default models list) and a writable place
for files the user edits — working the same way in development, in a source
delivery, and inside a packaged .exe.

- Bundled (read-only) resources: next to this package in dev/source, or at the
  PyInstaller extraction root (`sys._MEIPASS`) in an exe.
- External (writable) folder: the app folder in dev/source, or the folder that
  holds the .exe in a packaged delivery — so the operator can edit the models
  list without touching anything inside the program.
"""

import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent


def _meipass():
    return getattr(sys, "_MEIPASS", None)


def bundled_path(filename):
    """Return the path to a read-only resource shipped with the app."""
    mp = _meipass()
    if mp:
        p = Path(mp) / filename
        if p.exists():
            return p
    return APP_DIR / filename


def external_dir():
    """Return a writable folder beside the deliverable for user-editable files."""
    if _meipass():
        # one-file exe: the folder containing the executable
        return Path(sys.executable).resolve().parent
    return APP_DIR


def logo_path(variant="color", brand="oros"):
    """Return a path to the brand logo, or '' if none is found."""
    fname = f"logo_{variant}.png"
    mp = _meipass()
    if mp:
        p = Path(mp) / fname
        if p.exists():
            return str(p)
    here = Path(__file__).resolve()
    for candidate in (
        here.parents[3] / "shared" / "assets" / "logos" / brand,  # dev workspace
        here.parent,                                               # local override
    ):
        p = candidate / fname
        if p.exists():
            return str(p)
    return ""
