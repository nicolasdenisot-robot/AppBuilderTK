# oros_helpers — reusable building blocks

Tested helpers so every app doesn't re-write connection / result / export code.
Import the package and the vendored `pynvdrive` is wired up automatically.

| Module | What it gives you |
|--------|-------------------|
| `connection` | `connect()`, `is_nvgate_available()` — open/verify the NVGate live link (127.0.0.1:3000) |
| `settings` | `get_setting(idn)`, `set_setting(idn, value)`, `list_setting_choices(idn)` |
| `results` | `run_measurement(duration_s)`, `stop_measurement()`, `list_results()`, `get_result(...)`, `get_scalar_result(...)` |
| `nvgate_display` | `show_result_window(...)`, `set_layout(...)`, `autoscale_layout(...)` — present results inside NVGate |
| `export` | `results_to_excel(rows, path, headers)`, `dataframe_to_excel(...)`, `timestamped_name(...)` |
| `report` | `render_html_report(title, sections, path)` |

```python
from oros_helpers import connect, run_measurement, get_scalar_result
from oros_helpers.export import results_to_excel

with connect() as client:
    run_measurement(duration_s=10, client=client)
    level = get_scalar_result(module=2, process=10, channel=1, client=client)

results_to_excel([["Ch1", level, "PASS" if level < 95 else "FAIL"]],
                 headers=["Channel", "Level dB", "Verdict"], path="result.xlsx")
```

## Notes for Claude
- Result addresses are `(module, process, channel, reference_channel_number)`.
  Discover live ones with `list_results()` (items expose `.module_id`,
  `.process_id`, `.channel_number`).
- `nvgate_display` wraps a few NVDrive section-3.3 graphics commands. Add more
  wrappers here as apps need them — keep verifying signatures against the real
  command modules in `resources/Framework/Python/pynvdrive/pynvdrive/commands/`.
- These helpers are vendored into each app at export time (see `tools/export_app.py`).
