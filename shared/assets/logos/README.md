# Logo convention — full reference

## Which variant to use

| File | When to use |
|------|-------------|
| `logo_color.png` | Light-theme UI — **default for all apps unless told otherwise** (logo + "OROS") |
| `logo_white.png` | Dark-theme UI (logo + "OROS") |
| `logo_color_tagline.png` | Light-theme UI, with the "MEASURING NOISE & VIBRATION" tagline under the mark |
| `logo_white_tagline.png` | Dark-theme UI, with the tagline |

The plain `logo_color` / `logo_white` (no tagline) are the **defaults** — they are
what the export tool and `_logo_path()` look up by name, and the compact mark reads
best in a small UI header. The `_tagline` variants are **opt-in**: load one by its
filename with the `_asset_path()` helper below (or just point `_logo_path()` at the
tagline filename). Use the tagline version when the logo is shown large, e.g. a
splash or an about screen.

### Asset quality standard

Supply each variant as a transparent PNG, **at least ~1000 px wide** so it stays
crisp when a UI scales it. Keep the four files of a brand consistent: the same
artwork in colour and white, the tagline pair sharing the OROS-only pair's mark at
the same size/position.

> The `oros` brand ships all four at high resolution (logo + "OROS" ≈ 1230×349;
> with tagline ≈ 1233×406; transparent). When adding a new brand, match this set.

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
