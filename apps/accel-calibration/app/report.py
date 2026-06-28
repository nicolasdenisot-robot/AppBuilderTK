"""
Word calibration certificate.

Builds a deterministic .docx from a CalibrationResult: header + logo, the test
details, a per-frequency results table, an embedded sensitivity-vs-frequency
curve, the overall verdict, and signature lines. Same inputs -> same document.

The file is always written to a NEW dated name; nothing existing is overwritten
(CLAUDE.md rule #5).
"""

import io
from pathlib import Path

from .config import G_TO_MS2
from .resources import logo_path, external_dir

# unicode used only inside the document (not in console output)
_MS2 = "m/s²"          # m/s^2
_UNIT_MS2 = "mV/(m/s²)"
_DEG = "°"


def default_output_dir():
    docs = Path.home() / "Documents"
    return docs if docs.is_dir() else Path.home()


def report_filename(result):
    date = result.timestamp.strftime("%Y-%m-%d")
    return f"Calibration_{_safe(result.model.name)}_{_safe(result.serial)}_{date}.docx"


def build_certificate(result, out_dir=None):
    """Write the certificate and return its path."""
    out_dir = Path(out_dir) if out_dir else default_output_dir()
    out_dir = _writable_or_fallback(out_dir)
    path = out_dir / report_filename(result)
    _write_docx(result, path)
    return path


# ── document body ─────────────────────────────────────────────────────────────

def _write_docx(result, path):
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    model = result.model
    doc = Document()

    # logo (top-right)
    lp = logo_path("color")
    if lp:
        try:
            doc.add_picture(lp, width=Inches(1.8))
            doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        except Exception:
            pass

    doc.add_heading("Accelerometer Calibration Certificate", level=0)

    if result.simulated:
        warn = doc.add_paragraph()
        run = warn.add_run(
            "SIMULATION RUN — demonstration only. Not a valid calibration.")
        run.bold = True
        run.font.color.rgb = RGBColor(0xCF, 0x22, 0x2E)

    # --- details table -----------------------------------------------------
    details = [
        ("Date", result.timestamp.strftime("%Y-%m-%d %H:%M")),
        ("Operator", result.operator or "-"),
        ("Method", result.method_label),
        ("Accelerometer model", model.name),
        ("Manufacturer", model.manufacturer or "-"),
        ("Serial number", result.serial or "-"),
        ("Input type", model.input_type),
        ("Nominal sensitivity",
         f"{model.nominal_mv_per_g:.4g} mV/g  ({model.nominal_mv_per_ms2:.4g} {_UNIT_MS2})"),
        ("Tolerance", f"±{model.tolerance_pct:g} %"),
        ("Reference standard",
         f"{result.reference_sensitivity_mv_per_ms2:.4g} {_UNIT_MS2} (IEPE)"),
        ("Target level", f"{result.target_level_ms2:g} {_MS2}"),
    ]
    t = doc.add_table(rows=len(details), cols=2)
    t.style = "Light Grid Accent 1"
    for i, (k, v) in enumerate(details):
        t.rows[i].cells[0].paragraphs[0].add_run(k).bold = True
        t.rows[i].cells[1].text = str(v)

    # --- overall verdict ---------------------------------------------------
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.add_run("Overall result:  ").bold = True
    vr = p.add_run(result.overall_verdict)
    vr.bold = True
    vr.font.size = Pt(14)
    vr.font.color.rgb = _verdict_color(result.overall_verdict, RGBColor)

    # --- results table -----------------------------------------------------
    doc.add_heading("Results by frequency", level=1)
    headers = ["Frequency (Hz)", "Sensitivity (mV/g)", f"Sensitivity ({_UNIT_MS2})",
               f"Phase ({_DEG})", "Deviation (%)", "Verdict"]
    rt = doc.add_table(rows=1, cols=len(headers))
    rt.style = "Light Grid Accent 1"
    for c, h in enumerate(headers):
        rt.rows[0].cells[c].paragraphs[0].add_run(h).bold = True

    for pt in result.points:
        cells = rt.add_row().cells
        cells[0].text = _fmt_freq(pt.freq_hz)
        cells[1].text = f"{pt.sensitivity_mv_per_g:.4g}"
        cells[2].text = f"{pt.sensitivity_mv_per_ms2:.4g}"
        cells[3].text = f"{pt.phase_deg:+.1f}"
        cells[4].text = f"{pt.deviation_pct:+.2f}"
        vcell = cells[5]
        vrun = vcell.paragraphs[0].add_run(pt.verdict)
        vrun.bold = True
        vrun.font.color.rgb = _verdict_color(pt.verdict, RGBColor)
        if pt.note:
            cells[5].add_paragraph(pt.note)

    # --- curve -------------------------------------------------------------
    doc.add_heading("Sensitivity vs frequency", level=1)
    png = _sensitivity_plot_png(result)
    if png is not None:
        doc.add_picture(png, width=Inches(6.2))

    # --- signatures --------------------------------------------------------
    doc.add_paragraph()
    doc.add_paragraph()
    sig = doc.add_table(rows=1, cols=2)
    sig.rows[0].cells[0].text = "Calibrated by: ______________________"
    sig.rows[0].cells[1].text = "Approved by: ______________________"

    doc.save(str(path))


def _sensitivity_plot_png(result):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception:
        return None

    pts = result.points
    if not pts:
        return None
    freqs = [p.freq_hz for p in pts]
    sens_g = [p.sensitivity_mv_per_g for p in pts]
    nominal_g = result.model.nominal_mv_per_g
    tol = result.model.tolerance_pct

    fig, ax = plt.subplots(figsize=(6.4, 3.4), dpi=150)
    ax.semilogx(freqs, sens_g, "o-", color="#005b8f", label="Measured")
    ax.axhline(nominal_g, color="#1a7f37", ls="--", lw=1, label="Nominal")
    ax.axhline(nominal_g * (1 + tol / 100), color="#cf222e", ls=":", lw=1,
               label=f"±{tol:g}%")
    ax.axhline(nominal_g * (1 - tol / 100), color="#cf222e", ls=":", lw=1)

    fx = [p.freq_hz for p in pts if p.verdict != "PASS"]
    fy = [p.sensitivity_mv_per_g for p in pts if p.verdict != "PASS"]
    if fx:
        ax.scatter(fx, fy, color="#cf222e", zorder=5, label="Out of tolerance")

    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Sensitivity (mV/g)")
    ax.grid(True, which="both", ls=":", alpha=0.5)
    ax.legend(fontsize=8)
    fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)
    return buf


# ── small helpers ─────────────────────────────────────────────────────────────

def _verdict_color(verdict, RGBColor):
    return {
        "PASS": RGBColor(0x1A, 0x7F, 0x37),
        "FAIL": RGBColor(0xCF, 0x22, 0x2E),
        "CHECK": RGBColor(0xB5, 0x6A, 0x00),
    }.get(verdict, RGBColor(0x00, 0x00, 0x00))


def _fmt_freq(f):
    return f"{f:g}"


def _safe(s):
    keep = "-_."
    cleaned = "".join(ch if (ch.isalnum() or ch in keep) else "_" for ch in str(s))
    return cleaned.strip("_") or "x"


def _writable_or_fallback(out_dir):
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        probe = out_dir / ".write_test"
        probe.write_text("x", encoding="utf-8")
        probe.unlink()
        return out_dir
    except OSError:
        fallback = external_dir() / "reports"
        fallback.mkdir(parents=True, exist_ok=True)
        return fallback
