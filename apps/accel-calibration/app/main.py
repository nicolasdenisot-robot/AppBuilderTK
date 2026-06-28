"""
Accelerometer Calibration — entry point.

Launches the operator screen. All real work is deterministic Python (no AI at
runtime, CLAUDE.md section 3). Runs the same in development, as a source delivery,
and as a packaged .exe.

Run during development:
    python app/main.py
"""

import sys
from pathlib import Path

# --- make the `app` package and `oros_helpers` importable in every form -------
# Dev (workspace):  parent of app/  +  <root>/shared
# Source/exe bundle: parent of app/ (oros_helpers is vendored next to app/)
_HERE = Path(__file__).resolve()
for _candidate in (_HERE.parents[1], _HERE.parents[3] / "shared", _HERE.parents[1]):
    _cand = Path(_candidate)
    if _cand.exists() and str(_cand) not in sys.path:
        sys.path.insert(0, str(_cand))

from app.ui import run  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(run())
