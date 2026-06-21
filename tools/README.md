# tools

## export_app.py
Bundles an app into a self-contained deliverable.

```bash
python tools/export_app.py <app-name> [--target exe|source]
```

- Reads the app's `DIRECTIVE.md` frontmatter (`export_target`, `entry_point`).
- Vendors `pynvdrive` + the `oros_helpers` package into `apps/<app-name>/dist/`.
- `--target source` → zipped folder (recipient runs with Python).
- `--target exe` → standalone `.exe` via PyInstaller (recipient just double-clicks;
  requires `pyinstaller` installed in the build environment).

> Always confirm the export form with the user before building (CLAUDE.md rule #6).
