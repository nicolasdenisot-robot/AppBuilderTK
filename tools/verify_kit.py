"""
Verify the AI reference kit in `resources/AI/` against the installed OROS SDK.

There is deliberately NO version comparison here. The Framework and NVGate carry
separate version numbers -- `resources/Framework/version.txt` reports the NVGate
application version, while the kit is stamped with the Framework version -- so
comparing the two says nothing useful. This checks what actually matters: do the
kit's claims hold against the pynvdrive you have?

Two questions are answered:

  1. Every command the kit says has a Python class -- do that file and class
     really exist? A wrong class name sends an app to a runtime failure.
  2. Which commands does pynvdrive expose that the manual never documented? The
     kit is generated from the manual, so it cannot describe these -- but they
     work, and knowing they exist saves reinventing them.

Run:  python tools/verify_kit.py

Exit codes:  0 = every claim verified   1 = mismatches found   2 = kit or SDK missing
"""

import json
import re
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[1]
KIT = WORKSPACE / "resources" / "AI" / "nvdrive_commands.json"
COMMANDS = (WORKSPACE / "resources" / "Framework" / "Python" / "pynvdrive"
            / "pynvdrive" / "commands")


def sdk_classes():
    """Map class name -> [(file, base class), ...] for everything pynvdrive defines."""
    found = {}
    for path in COMMANDS.rglob("*.py"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"^class (\w+)\(([\w., ]*)\)", text, re.M):
            found.setdefault(m.group(1), []).append((path, m.group(2).strip()))
    return found


def main():
    if not KIT.exists():
        print("Cannot verify: the AI kit is not in resources/AI/.")
        return 2
    if not COMMANDS.is_dir():
        print("Cannot verify: the OROS Framework is not in resources/Framework/ yet.")
        print("Add the SDK (see resources/README.md), then run this again.")
        return 2

    catalogue = json.load(KIT.open(encoding="utf-8"))["commands"]
    classes = sdk_classes()

    # 1. Do the kit's Python-wrapper claims hold?
    claimed = [c for c in catalogue if c.get("pynvdrive")]
    bad = []
    for cmd in claimed:
        rel = cmd["pynvdrive_wrapper"]
        name = cmd["pynvdrive"]["class"]
        path = COMMANDS / rel
        if not path.exists():
            bad.append(f"{cmd['name']}: file not found -> {rel}")
        elif f"class {name}" not in path.read_text(encoding="utf-8", errors="replace"):
            bad.append(f"{cmd['name']}: class {name} not defined in {rel}")

    print(f"Kit claims {len(claimed)} of {len(catalogue)} commands have a Python class.")
    if bad:
        print(f"\n{len(bad)} CLAIM(S) DO NOT HOLD against your installed SDK:")
        for b in bad:
            print("  -", b)
        print("\nTrust the SDK, not the kit, for these. Worth reporting to OROS.")
    else:
        print("All verified: every wrapper file and class name exists in your SDK.")

    # 2. What does pynvdrive expose that the manual never documented?
    documented = {c["name"] for c in catalogue}
    undocumented = sorted(
        n for n, defs in classes.items()
        if n not in documented and any("Command" in base for _, base in defs)
    )
    if undocumented:
        print(
            f"\n{len(undocumented)} command(s) exist in pynvdrive but are NOT in the "
            "NVDrive manual,\nso the kit cannot describe them. They still work -- read "
            "the class to use one:"
        )
        for n in undocumented:
            rel = classes[n][0][0].relative_to(COMMANDS).as_posix()
            print(f"  {n:32} {rel}")

    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
