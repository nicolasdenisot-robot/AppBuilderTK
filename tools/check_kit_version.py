"""
Check the AI reference kit against the installed OROS Framework.

The kit in `resources/AI/` is generated from one specific Framework version and
stamped with it. The SDK in `resources/Framework/` is whatever the user downloaded.
When the SDK is newer, the kit is still correct about what it documents but will not
know about anything added since -- and CLAUDE.md tells Claude to trust the kit, so a
silent mismatch is the failure worth catching.

Run:  python tools/check_kit_version.py

Exit codes:  0 = versions match   1 = kit is older than the SDK   2 = cannot tell
"""

import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
MANIFEST = WORKSPACE / "resources" / "AI" / "MANIFEST.txt"
SDK_VERSION = WORKSPACE / "resources" / "Framework" / "version.txt"


def _read(path, pattern):
    """Return the first capture of `pattern` in `path`, or None."""
    if not path.exists():
        return None
    m = re.search(pattern, path.read_text(encoding="utf-8", errors="replace"))
    return m.group(1).strip() if m else None


def _as_tuple(version):
    """'18.00.001' -> (18, 0, 1) for comparison; None if unparseable."""
    parts = re.findall(r"\d+", version or "")
    return tuple(int(p) for p in parts[:3]) if parts else None


def main():
    kit = _read(MANIFEST, r"Framework version\s*:\s*(\S+)")
    sdk = _read(SDK_VERSION, r'NVGate version:\s*"([^"]+)"')

    if kit is None:
        print("Cannot check: the AI kit is not in resources/AI/ (no MANIFEST.txt).")
        return 2
    if sdk is None:
        print("Cannot check: the OROS Framework is not in resources/Framework/ yet.")
        print(f"The AI reference kit was built from Framework {kit}.")
        print("Add the SDK (see resources/README.md), then run this again.")
        return 2

    print(f"  AI reference kit : built from Framework {kit}")
    print(f"  Framework installed here : {sdk}")

    kv, sv = _as_tuple(kit), _as_tuple(sdk)
    if kit == sdk or (kv and sv and kv == sv):
        print("\nMatch. The reference kit describes the SDK you have.")
        return 0
    if kv and sv and kv < sv:
        print(
            "\nThe reference kit is OLDER than your Framework.\n"
            "\nWhat this means in practice: everything the kit documents is still\n"
            "accurate, but it will not know about commands or settings added since\n"
            f"{kit}. If you look for something and the kit says it does not exist,\n"
            "check the SDK itself before believing it -- the Python command classes\n"
            "in resources/Framework/Python/pynvdrive/pynvdrive/commands/ are the\n"
            "ground truth, and the PDFs in resources/Framework/ are the reference.\n"
            "\nTo fix it properly, ask OROS for a reference kit built from "
            f"Framework {sdk}."
        )
        return 1
    print(
        "\nThe kit and the Framework are stamped with different versions.\n"
        "Trust the SDK and the PDFs in resources/Framework/ where they disagree."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
