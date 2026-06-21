# Recipe: auto-generate a report

**Goal:** produce a shareable report (HTML now, PDF if needed) from results.
**HTML needs nothing extra**; PDF via `reportlab` (add to `requirements.txt`).

```python
from oros_helpers.report import render_html_report

sections = [
    ("Summary", "Unit <b>SN-0001</b>: overall level 92.3 dB "
                "&rarr; <span class='pass'>PASS</span>"),
    ("Measurements", """
        <table>
          <tr><th>Channel</th><th>Level dB</th><th>Verdict</th></tr>
          <tr><td>Ch1</td><td>92.3</td><td class='pass'>PASS</td></tr>
          <tr><td>Ch2</td><td>97.1</td><td class='fail'>FAIL</td></tr>
        </table>"""),
]
render_html_report(title="End-of-line test report", sections=sections,
                   path="report.html")
```

## To PDF
- Simplest: open the HTML and "Print → Save as PDF".
- Automated: render the HTML with **WeasyPrint**, or build directly with
  **reportlab**. Add the chosen package to the app's `requirements.txt` and put a
  reusable `render_pdf_report(...)` in `oros_helpers/report.py`.

## Notes
- Keep reports template-driven and deterministic — same inputs, same output.
- Embed plots by saving a matplotlib PNG and referencing it with `<img>`.
