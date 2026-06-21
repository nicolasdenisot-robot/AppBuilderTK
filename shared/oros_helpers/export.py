"""
Export helpers — write results to Excel and other office formats.

Requires `openpyxl` (and optionally `pandas`). Add them to the app's
requirements.txt. These are intentionally simple, deterministic helpers.
"""

import datetime as _dt


def results_to_excel(rows, path, headers=None, sheet_name="Results"):
    """
    Write a table of `rows` to an .xlsx file at `path`.

    `rows`   : list of lists/tuples, one per line.
    `headers`: optional list of column titles written as the first row.

    Example:
        results_to_excel(
            rows=[["Ch1", 92.3, "PASS"], ["Ch2", 97.1, "FAIL"]],
            headers=["Channel", "Level dB", "Verdict"],
            path="report.xlsx",
        )
    """
    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name

    if headers:
        ws.append(list(headers))
    for row in rows:
        ws.append(list(row))

    wb.save(path)
    return path


def dataframe_to_excel(df, path, sheet_name="Results"):
    """Write a pandas DataFrame to .xlsx. Requires pandas + openpyxl."""
    df.to_excel(path, sheet_name=sheet_name, index=False)
    return path


def timestamped_name(prefix, ext=".xlsx"):
    """Return e.g. 'eol_2026-06-17_14-32-05.xlsx' for unique output files."""
    stamp = _dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{prefix}_{stamp}{ext}"
