# tools

## verify_kit.py
Verifies the AI reference kit in `resources/AI/` against the installed OROS SDK.

```bash
python tools/verify_kit.py
```

Deliberately does **no** version comparison: the Framework and NVGate carry separate
version numbers (`resources/Framework/version.txt` reports the *NVGate* version, the
kit is stamped with the *Framework* version), so comparing them proves nothing. It
checks what matters instead:

- every command the kit says has a Python class — does that file and class exist?
- which commands `pynvdrive` exposes that the NVDrive manual never documented. The kit
  is generated from the manual, so it cannot describe those ~20 — but they work, and
  knowing they exist saves reinventing them.

Exit codes: `0` all claims verified · `1` mismatches found · `2` kit or SDK missing.
Run it before relying on the kit (CLAUDE.md §4), and after updating either.

## export_app.py
Bundles an app into a self-contained deliverable.

```bash
python tools/export_app.py <app-name> [--target exe|source]
```

- Reads the app's `DIRECTIVE.md` frontmatter (`version`, `display_name`,
  `export_target`, `entry_point`, `logo`).
- Vendors `pynvdrive` + the `oros_helpers` package into the delivery folder.
- Produces a versioned folder at `apps/<app-name>/dist/<app-name>-v<version>-<target>/`.
  The tool stops there — the user inspects the folder, then zips and sends it.
- `--target source` → folder with Python source + launcher + `setup.bat` +
  `install_to_nvgate.bat` + `README.txt` + `WHATS-NEW.txt` (recipient needs Python
  installed).
- `--target exe` → folder with standalone `.exe` + `install_to_nvgate.bat` +
  `README.txt` + `WHATS-NEW.txt` (recipient needs nothing pre-installed; requires
  `pyinstaller` in the build environment).
- Every package also includes `WHATS-NEW.txt`, copied from the app's `CHANGELOG.md`
  (rule #9). If the app has no `CHANGELOG.md`, the tool warns and ships without it.

> Always confirm the export form with the user before building (CLAUDE.md rule #6).
