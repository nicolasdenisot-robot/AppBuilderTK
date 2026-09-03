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

**Only `app/` plus a few named files are packaged** (README, CHANGELOG → WHATS-NEW,
requirements, bundled SDK). Other folders in the app — notably `reference/` (source
docs that inform the build) and `.tmp/` — are **never shipped**. Documents the app
loads at runtime (templates, images) must therefore live as top-level files in `app/`,
not in `reference/`. See CLAUDE.md §6.

---

## Delivery folder contents

| Exe delivery | Source / bat delivery |
|---|---|
| `<name>.exe` | `app/` + `pynvdrive/` + `oros_helpers/` |
| `install_to_nvgate.bat` | `launch_<name>.bat` |
| `README.txt` | `setup.bat` (pip install, run once) |
| `WHATS-NEW.txt` | `install_to_nvgate.bat` |
| | `requirements.txt` · `README.txt` · `WHATS-NEW.txt` |

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

## Release notes (`WHATS-NEW.txt`)

Every delivery automatically includes a plain-text **`WHATS-NEW.txt`** so the
operator can see what changed in this version. It is a straight copy of the app's
**`CHANGELOG.md`** (single source of truth, newest entry first) — the same way
`README.md` is shipped as `README.txt`.

- Keep `apps/<name>/CHANGELOG.md` current: add an entry whenever you bump `version`
  (CLAUDE.md rule #9). New apps start from `apps/_template/CHANGELOG.md`.
- If an app has **no** `CHANGELOG.md`, the tool prints a warning and ships the
  package without `WHATS-NEW.txt` — it does not fail. Add one so updates carry
  release notes.

## Generated files

Both delivery forms include a generated **`install_to_nvgate.bat`** that registers
the app in NVGate's Automation → Execute menu. It captures the exe / launcher bat's
absolute path at package time from wherever the operator unzips.

The app's own launcher uses **relative** paths and must stay in its folder. NVGate's
Execute-menu registration, by contrast, lives in `C:\OROS\NVGate data\Links\` and needs
the **full absolute path** — which is exactly what `install_to_nvgate.bat` writes. So
always confirm *where and how* the operator will invoke the app (double-click, Automation
→ Execute, scheduled task) before treating delivery as complete.

---

## Required DIRECTIVE.md frontmatter fields

```yaml
version: 1.0                # becomes part of the folder name
display_name: My App Name   # shown in NVGate Automation (derived from the folder name if absent)
export_target: exe|source
entry_point: app/main.py
logo: oros                  # brand folder under shared/assets/logos/ (default: oros)
```

Those five are the only fields the tool reads. `apps/_template/DIRECTIVE.md` also
carries `app_name` and `helpers_used` — both **informational**: the app's name comes
from its folder, and the whole `oros_helpers` package is vendored regardless of what
`helpers_used` lists. A value containing `#` must be quoted
(`display_name: "Rig #3"`) — unquoted, `#` starts a comment, as in YAML.

---

## Updating an existing app

1. Modify the app in `apps/<name>/`.
2. Bump `version` in `DIRECTIVE.md`.
3. **Add a `CHANGELOG.md` entry** for the new version (plain language, newest
   first) — this is what ships as `WHATS-NEW.txt` (rule #9).
4. Run `python tools/export_app.py <app-name>` again.
5. The user zips the new folder and sends it to the operator.
6. Operator unzips and re-runs `install_to_nvgate.bat` only if the install
   location has changed.
