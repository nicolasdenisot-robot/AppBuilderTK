# Export form trade-offs — full script

Use this when explaining the two delivery options to the user at stop #6 of the
6-stop interview. Read both options, then let them choose.

Both forms work equally well with NVGate's Automation → Execute menu — that is
*not* the differentiator.

---

## Option A — Standalone `.exe`

PyInstaller bundles Python, all libraries, and the app into a single file. The
operator needs **nothing pre-installed** — no Python, no pip, no setup.

- **Pros:** truly zero-dependency; one file to hand over; no IT involvement needed.
- **Cons:** the `.exe` is large (50–150 MB); Windows Defender or company antivirus
  sometimes flags unknown executables (even clean ones); every bug fix requires a
  full rebuild and re-delivery.
- **Best when:** the operator is a production-line worker or someone outside your
  company; you have no control over their PC; or IT policy forbids installing Python.

## Option B — `.bat` + Python source

The operator runs the Python code directly. They need **Python installed once**
(done via `setup.bat`); after that, launches are instant.

- **Pros:** tiny package (a few KB of text files); no antivirus issues; a bug fix is
  just editing a `.py` file and sending it — no rebuild; easier to diagnose when
  something breaks (the terminal shows the exact error).
- **Cons:** Python must be installed on the operator's PC; if it is not (or is the
  wrong version), IT help is needed before the app runs.
- **Best when:** the operator is an engineer in the same organisation; IT can install
  Python once; you expect to update the app regularly; or you are still iterating.
