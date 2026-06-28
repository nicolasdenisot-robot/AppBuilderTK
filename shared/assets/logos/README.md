# Logo convention — full reference

## Which variant to use

| File | When to use |
|------|-------------|
| `logo_color.png` | Light-theme UI — **default for all apps unless told otherwise** |
| `logo_white.png` | Dark-theme UI only |

### Asset quality standard

Supply each variant as a PNG with transparency, **at least ~500 px wide** so it
stays crisp when a UI scales it up. Both variants of a brand should be the same
resolution.

> **Known gap (oros):** the current `oros/logo_color.png` is only 135×37 px, while
> `oros/logo_white.png` is 500×135 px. The colour mark is the *default* (light
> themes) yet is the lower-resolution file, so it can look soft when enlarged. It
> is a multi-colour mark, so it can't be regenerated from the white silhouette —
> replace it with a high-resolution colour PNG from OROS's brand assets when one is
> available. (At small header sizes the current file is acceptable.)

---

## Adding a logo to an app

**Step 1 — DIRECTIVE.md**

Set the `logo:` field to the brand folder name:

```yaml
logo: oros          # → shared/assets/logos/oros/
```

The export tool reads this field and copies both `logo_color.png` and
`logo_white.png` into the staging area automatically. Nothing else to do
for delivery.

**Step 2 — main.py**

Copy-paste this pattern (change `_LOGO_BRAND` and `_LOGO_VARIANT` as needed):

```python
_LOGO_BRAND   = "oros"   # must match a folder under shared/assets/logos/
_LOGO_VARIANT = "color"  # "color" for light themes · "white" for dark themes

def _logo_path() -> str:
    fname = f"logo_{_LOGO_VARIANT}.png"
    if hasattr(sys, '_MEIPASS'):           # running as a PyInstaller exe
        return os.path.join(sys._MEIPASS, fname)
    _here = Path(__file__).resolve()
    for candidate in (
        _here.parents[3] / "shared" / "assets" / "logos" / _LOGO_BRAND,
        _here.parent,                      # local override next to main.py
    ):
        p = candidate / fname
        if p.exists():
            return str(p)
    return ""
```

This works in development (finds the logo in `shared/assets/logos/<brand>/`) and
in a bundled exe (`sys._MEIPASS` — the export tool puts it there via `--add-data`).

---

## Loading other runtime assets (templates, images)

Any file the app loads at runtime (an Excel/report template, a config, an image)
uses the same bundle-aware pattern as `_logo_path()`. Keep the file **top-level in
`app/`** — the exe bundler does not recurse into sub-folders — and read it with:

```python
def _asset_path(fname):
    if hasattr(sys, "_MEIPASS"):               # running as the .exe
        return os.path.join(sys._MEIPASS, fname)
    return str(Path(__file__).parent / fname)  # running from source
```

---

## Adding a customer-branded app

1. Create `shared/assets/logos/<customer-name>/` and place `logo_color.png` and
   `logo_white.png` inside it.
2. Set `logo: <customer-name>` in the app's `DIRECTIVE.md`.
3. Set `_LOGO_BRAND = "<customer-name>"` in `main.py`.

No other changes needed — the export tool handles everything else.
