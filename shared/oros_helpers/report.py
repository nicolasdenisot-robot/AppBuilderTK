"""
Report helpers — generate a simple HTML report from results.

`render_html_report` has no dependencies: it writes an .html file you can open
or print to PDF from a browser. For automated PDF output, add a
`render_pdf_report(...)` here using `reportlab` or WeasyPrint (see
docs/recipes/generate-report.md). Keep reports deterministic and template-driven.
"""

import datetime as _dt


def render_html_report(title, sections, path):
    """
    Write a basic HTML report.

    `sections`: list of (heading, body_text) tuples. `body_text` may contain
    simple HTML (e.g. a <table>). Returns the written path.
    """
    stamp = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    parts = [
        "<!doctype html><html><head><meta charset='utf-8'>",
        f"<title>{_esc(title)}</title>",
        "<style>body{font-family:Segoe UI,Arial,sans-serif;margin:2em;}"
        "h1{color:#003a5d;} h2{color:#005b8f;border-bottom:1px solid #ccc;}"
        "table{border-collapse:collapse;} td,th{border:1px solid #aaa;padding:4px 8px;}"
        ".pass{color:#1a7f37;font-weight:bold;} .fail{color:#cf222e;font-weight:bold;}"
        "</style></head><body>",
        f"<h1>{_esc(title)}</h1><p><i>Generated {stamp}</i></p>",
    ]
    for heading, body in sections:
        parts.append(f"<h2>{_esc(heading)}</h2>")
        parts.append(f"<div>{body}</div>")
    parts.append("</body></html>")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    return path


def _esc(text):
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
