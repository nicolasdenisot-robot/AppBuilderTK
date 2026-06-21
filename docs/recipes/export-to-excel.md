# Recipe: export results to Excel

**Goal:** write measured values to an `.xlsx` file. **Needs:** `openpyxl` in the
app's `requirements.txt` (add `pandas` for the DataFrame variant).

```python
from oros_helpers.export import results_to_excel, timestamped_name

rows = [
    ["Ch1", 92.3, "PASS"],
    ["Ch2", 97.1, "FAIL"],
]
results_to_excel(
    rows=rows,
    headers=["Channel", "Level dB", "Verdict"],
    path=timestamped_name("measurement"),   # e.g. measurement_2026-06-17_14-32-05.xlsx
)
```

## With pandas (bigger tables / spectra)
```python
import pandas as pd
from oros_helpers.export import dataframe_to_excel

df = pd.DataFrame({"Frequency_Hz": freqs, "Level_dB": levels})
dataframe_to_excel(df, "spectrum.xlsx")
```

## Notes
- Use `timestamped_name(prefix)` to avoid overwriting previous runs.
- Append-to-existing-workbook or multi-sheet? Extend `oros_helpers/export.py` and
  reuse it across apps rather than copying code into each app.
