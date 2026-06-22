# Logo convention — full reference

## Which variant to use

| File | When to use |
|------|-------------|
| `logo_color.png` | Light-theme UI — **default for all apps unless told otherwise** |
| `logo_white.png` | Dark-theme UI only |

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

## Adding a customer-branded app

1. Create `shared/assets/logos/<customer-name>/` and place `logo_color.png` and
   `logo_white.png` inside it.
2. Set `logo: <customer-name>` in the app's `DIRECTIVE.md`.
3. Set `_LOGO_BRAND = "<customer-name>"` in `main.py`.

No other changes needed — the export tool handles everything else.
