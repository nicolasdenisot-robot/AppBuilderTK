# tools

## export_app.py
Bundles an app into a self-contained deliverable.

```bash
python tools/export_app.py <app-name> [--target exe|source]
```

- Reads the app's `DIRECTIVE.md` frontmatter (`version`, `display_name`,
  `export_target`, `entry_point`).
- Vendors `pynvdrive` + the `oros_helpers` package into the delivery folder.
- Produces a versioned folder at `apps/<app-name>/dist/<app-name>-v<version>-<target>/`.
  The tool stops there — the user inspects the folder, then zips and sends it.
- `--target source` → folder with Python source + launcher + `setup.bat` +
  `install_to_nvgate.bat` + `README.txt` (recipient needs Python installed).
- `--target exe` → folder with standalone `.exe` + `install_to_nvgate.bat` +
  `README.txt` (recipient needs nothing pre-installed; requires `pyinstaller`
  in the build environment).

> Always confirm the export form with the user before building (CLAUDE.md rule #6).
