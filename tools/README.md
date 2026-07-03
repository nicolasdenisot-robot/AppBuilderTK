# tools

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
