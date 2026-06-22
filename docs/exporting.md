# Exporting — full delivery reference

Use `tools/export_app.py`. Run it once when the app is ready to ship:

```
python tools/export_app.py <app-name>
```

Output folder:

```
apps/<name>/dist/<name>-v<version>-<target>/
```

Both delivery forms can exist side by side in `dist/` without overwriting each other.
After the tool runs, show the user the folder path — they inspect it, zip it, and send
it. The tool does not zip automatically.

---

## Delivery folder contents

| Exe delivery | Source / bat delivery |
|---|---|
| `<name>.exe` | `app/` + `pynvdrive/` + `oros_helpers/` |
| `install_to_nvgate.bat` | `launch_<name>.bat` |
| `README.txt` | `setup.bat` (pip install, run once) |
| | `install_to_nvgate.bat` |
| | `requirements.txt` · `README.txt` |

---

## README handling

The app's `README.md` (Markdown, for development) is copied into the delivery
package as **`README.txt`** so any operator can open it with a double-click.

When the two forms need different instructions, create form-specific READMEs:

```
apps/<app-name>/
    README.md           ← development reference
    README-exe.md       ← delivery README for exe form (if different)
    README-source.md    ← delivery README for source form (if different)
```

The export tool picks `README-<target>.md` first if it exists, and falls back to
`README.md`. Write form-specific READMEs whenever the two forms would otherwise
reference files that don't exist in that package (e.g. `launch_*.bat` only exists
in the source package; `setup.bat` only in source).

---

## Generated files

Both delivery forms include a generated **`install_to_nvgate.bat`** that registers
the app in NVGate's Automation → Execute menu. It captures the exe / launcher bat's
absolute path at package time from wherever the operator unzips.

---

## Required DIRECTIVE.md frontmatter fields

```yaml
version: 1.0                # becomes part of the folder name
display_name: My App Name   # shown in NVGate Automation (derived from app_name if absent)
export_target: exe|source
entry_point: app/main.py
logo: oros                  # brand folder under shared/assets/logos/ (default: oros)
```

---

## Updating an existing app

1. Modify the app in `apps/<name>/`.
2. Bump `version` in `DIRECTIVE.md`.
3. Run `python tools/export_app.py <app-name>` again.
4. The user zips the new folder and sends it to the operator.
5. Operator unzips and re-runs `install_to_nvgate.bat` only if the install
   location has changed.
