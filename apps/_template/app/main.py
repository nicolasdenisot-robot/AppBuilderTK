"""
<app name> — entry point.

This is a STARTER. Replace the body with the steps from DIRECTIVE.md §4.
Keep all real work deterministic (CLAUDE.md §3): no AI at runtime.

Run during development:
    python app/main.py
"""

import sys
from pathlib import Path

# --- make `oros_helpers` importable, in dev AND in an exported bundle ------
# Dev (workspace):  shared/ is at <root>/shared  (3 levels up from app/).
# Export (bundle):  oros_helpers sits next to app/  (1 level up).
_HERE = Path(__file__).resolve()
for _candidate in (_HERE.parents[3] / "shared", _HERE.parents[1]):
    if (_candidate / "oros_helpers").is_dir() and str(_candidate) not in sys.path:
        sys.path.insert(0, str(_candidate))

from oros_helpers import connect, is_nvgate_available  # noqa: E402


def main():
    # 1. Make sure NVGate is reachable (for live-control apps).
    if not is_nvgate_available():
        print("NVGate is not reachable. Launch NVGate (connected mode) and retry.")
        return 1

    # 2. Do the work. Replace this with DIRECTIVE.md §4 steps.
    with connect() as client:
        print("Connected to NVGate. Add your steps here.")
        # e.g.
        # from oros_helpers import run_measurement, get_scalar_result
        # run_measurement(duration_s=10, client=client)
        # level = get_scalar_result(module=2, process=10, channel=1, client=client)
        # print("Level:", level)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
