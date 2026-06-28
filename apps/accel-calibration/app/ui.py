"""
Operator screen (PySide6).

A clean, guided window: pick the accelerometer model, enter the serial and
operator, tick the frequencies, press Start. The calibration runs in a background
thread so the screen stays responsive; results fill in live; a Word certificate
is written automatically at the end.
"""

import os
import sys
from pathlib import Path

from PySide6.QtCore import Qt, QThread, QObject, Signal
from PySide6.QtGui import QPixmap, QColor, QFont
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QFormLayout, QLabel, QComboBox, QLineEdit, QPushButton, QCheckBox, QGroupBox,
    QTableWidget, QTableWidgetItem, QProgressBar, QFileDialog, QMessageBox,
    QHeaderView,
)

from .config import CONFIG, STANDARD_FREQUENCIES_HZ
from .models import load_models, models_file_path
from .backends import SimulationBackend, NVGateBackend
from .calibration import CalibrationRunner, CalibrationCancelled
from .report import build_certificate, default_output_dir
from .resources import logo_path

OROS_BLUE = "#003a5d"
VERDICT_COLORS = {"PASS": "#1a7f37", "FAIL": "#cf222e", "CHECK": "#b56a00"}


def nvgate_available():
    """True if NVGate is reachable right now (never raises)."""
    try:
        from oros_helpers import is_nvgate_available
        return bool(is_nvgate_available())
    except Exception:
        return False


# ── background worker ─────────────────────────────────────────────────────────

class CalibrationWorker(QObject):
    progress = Signal(dict)
    finished = Signal(object)
    failed = Signal(str)

    def __init__(self, backend, model, serial, operator, freqs):
        super().__init__()
        self._backend = backend
        self._model = model
        self._serial = serial
        self._operator = operator
        self._freqs = freqs
        self._cancel = False

    def cancel(self):
        self._cancel = True

    def run(self):
        try:
            runner = CalibrationRunner(self._backend)
            result = runner.run(
                self._model, self._serial, self._operator, self._freqs,
                progress_cb=lambda **kw: self.progress.emit(kw),
                is_cancelled=lambda: self._cancel,
            )
            self.finished.emit(result)
        except CalibrationCancelled:
            self.failed.emit("__cancelled__")
        except Exception as e:  # connection errors, backend errors, etc.
            self.failed.emit(str(e))


# ── main window ───────────────────────────────────────────────────────────────

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accelerometer Calibration")
        self.resize(900, 720)

        self._models = []
        self._freq_checks = []
        self._thread = None
        self._worker = None
        self._last_report = None

        self._build_ui()
        self._load_models_into_combo()
        self._refresh_mode_banner()

    # --- construction --------------------------------------------------------

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(16, 12, 16, 12)
        root.setSpacing(10)

        root.addLayout(self._build_header())
        root.addWidget(self._build_mode_banner())
        root.addWidget(self._build_setup_group())
        root.addWidget(self._build_freq_group())
        root.addLayout(self._build_action_row())
        root.addWidget(self._build_results_group(), stretch=1)

    def _build_header(self):
        row = QHBoxLayout()
        title = QLabel("Accelerometer Calibration")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet(f"color: {OROS_BLUE};")
        row.addWidget(title)
        row.addStretch(1)
        lp = logo_path("color")
        if lp:
            logo = QLabel()
            pm = QPixmap(lp)
            if not pm.isNull():
                logo.setPixmap(pm.scaledToHeight(40, Qt.SmoothTransformation))
            row.addWidget(logo)
        return row

    def _build_mode_banner(self):
        self.mode_label = QLabel()
        self.mode_label.setAlignment(Qt.AlignCenter)
        self.mode_label.setStyleSheet(
            "padding:6px; border-radius:4px; font-weight:bold;")
        return self.mode_label

    def _build_setup_group(self):
        box = QGroupBox("Unit under test")
        form = QFormLayout(box)
        form.setLabelAlignment(Qt.AlignRight)

        # model row with edit/reload buttons
        self.model_combo = QComboBox()
        self.model_combo.currentIndexChanged.connect(self._on_model_changed)
        model_row = QHBoxLayout()
        model_row.addWidget(self.model_combo, stretch=1)
        edit_btn = QPushButton("Edit list…")
        edit_btn.setToolTip("Open the editable model list in your text editor")
        edit_btn.clicked.connect(self._edit_models)
        reload_btn = QPushButton("Reload")
        reload_btn.setToolTip("Reload the model list after editing it")
        reload_btn.clicked.connect(self._load_models_into_combo)
        model_row.addWidget(edit_btn)
        model_row.addWidget(reload_btn)
        model_row_w = QWidget()
        model_row_w.setLayout(model_row)
        form.addRow("Model:", model_row_w)

        self.model_info = QLabel("-")
        self.model_info.setStyleSheet("color:#444;")
        form.addRow("", self.model_info)

        self.serial_edit = QLineEdit()
        self.serial_edit.setPlaceholderText("e.g. SN-00123")
        form.addRow("Serial number:", self.serial_edit)

        self.operator_edit = QLineEdit()
        self.operator_edit.setPlaceholderText("your name")
        form.addRow("Operator:", self.operator_edit)

        # output folder
        self.out_edit = QLineEdit(str(default_output_dir()))
        browse = QPushButton("Browse…")
        browse.clicked.connect(self._browse_output)
        out_row = QHBoxLayout()
        out_row.addWidget(self.out_edit, stretch=1)
        out_row.addWidget(browse)
        out_row_w = QWidget()
        out_row_w.setLayout(out_row)
        form.addRow("Save report to:", out_row_w)

        return box

    def _build_freq_group(self):
        box = QGroupBox("Calibration frequencies (Hz)")
        outer = QVBoxLayout(box)

        grid = QGridLayout()
        per_row = 6
        for i, f in enumerate(STANDARD_FREQUENCIES_HZ):
            cb = QCheckBox(f"{f:g}")
            cb.setChecked(True)
            self._freq_checks.append((f, cb))
            grid.addWidget(cb, i // per_row, i % per_row)
        outer.addLayout(grid)

        btns = QHBoxLayout()
        all_btn = QPushButton("Select all")
        all_btn.clicked.connect(lambda: self._set_all_freqs(True))
        none_btn = QPushButton("Clear")
        none_btn.clicked.connect(lambda: self._set_all_freqs(False))
        btns.addWidget(all_btn)
        btns.addWidget(none_btn)
        btns.addStretch(1)
        self.sim_check = QCheckBox("Force simulation (no shaker / no NVGate)")
        self.sim_check.stateChanged.connect(self._refresh_mode_banner)
        btns.addWidget(self.sim_check)
        outer.addLayout(btns)
        return box

    def _build_action_row(self):
        row = QHBoxLayout()
        self.start_btn = QPushButton("Start calibration")
        self.start_btn.setStyleSheet(
            f"background:{OROS_BLUE}; color:white; font-weight:bold; padding:8px 18px;")
        self.start_btn.clicked.connect(self._start)
        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setEnabled(False)
        self.cancel_btn.clicked.connect(self._cancel)
        self.open_btn = QPushButton("Open report")
        self.open_btn.setEnabled(False)
        self.open_btn.clicked.connect(self._open_report)

        row.addWidget(self.start_btn)
        row.addWidget(self.cancel_btn)
        row.addStretch(1)
        row.addWidget(self.open_btn)
        return row

    def _build_results_group(self):
        box = QGroupBox("Results")
        v = QVBoxLayout(box)

        self.progress = QProgressBar()
        self.progress.setValue(0)
        v.addWidget(self.progress)

        self.status = QLabel("Ready.")
        v.addWidget(self.status)

        self.overall = QLabel("")
        self.overall.setFont(QFont("Segoe UI", 14, QFont.Bold))
        v.addWidget(self.overall)

        headers = ["Frequency (Hz)", "mV/g", "mV/(m/s²)", "Phase (°)",
                   "Deviation (%)", "Verdict"]
        self.table = QTableWidget(0, len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        v.addWidget(self.table)
        return box

    # --- model handling ------------------------------------------------------

    def _load_models_into_combo(self):
        try:
            self._models = load_models()
        except Exception as e:
            QMessageBox.critical(self, "Model list error",
                                 f"Could not read the model list:\n{e}")
            self._models = []
        self.model_combo.blockSignals(True)
        self.model_combo.clear()
        for m in self._models:
            self.model_combo.addItem(m.name)
        self.model_combo.blockSignals(False)
        if self._models:
            self.model_combo.setCurrentIndex(0)
            self._on_model_changed(0)

    def _current_model(self):
        idx = self.model_combo.currentIndex()
        if 0 <= idx < len(self._models):
            return self._models[idx]
        return None

    def _on_model_changed(self, _idx):
        m = self._current_model()
        if m:
            self.model_info.setText(
                f"Nominal {m.nominal_mv_per_g:.4g} mV/g "
                f"({m.nominal_mv_per_ms2:.4g} mV/(m/s²))  ·  "
                f"tolerance ±{m.tolerance_pct:g}%  ·  {m.input_type}")

    def _edit_models(self):
        try:
            os.startfile(str(models_file_path()))  # Windows
        except Exception as e:
            QMessageBox.information(self, "Edit model list",
                                    f"Model list file:\n{models_file_path()}\n\n({e})")

    # --- frequency helpers ---------------------------------------------------

    def _set_all_freqs(self, checked):
        for _f, cb in self._freq_checks:
            cb.setChecked(checked)

    def _selected_freqs(self):
        return [f for f, cb in self._freq_checks if cb.isChecked()]

    # --- mode banner ---------------------------------------------------------

    def _refresh_mode_banner(self):
        if self.sim_check.isChecked():
            self._set_banner("SIMULATION — no hardware will be driven", "#b56a00")
        elif nvgate_available():
            self._set_banner("LIVE — NVGate connected", "#1a7f37")
        else:
            self._set_banner("NVGate not detected — will offer simulation", "#cf222e")

    def _set_banner(self, text, color):
        self.mode_label.setText(text)
        self.mode_label.setStyleSheet(
            f"padding:6px; border-radius:4px; font-weight:bold; "
            f"color:white; background:{color};")

    # --- output folder -------------------------------------------------------

    def _browse_output(self):
        d = QFileDialog.getExistingDirectory(self, "Choose report folder",
                                             self.out_edit.text())
        if d:
            self.out_edit.setText(d)

    # --- run -----------------------------------------------------------------

    def _start(self):
        model = self._current_model()
        if not model:
            QMessageBox.warning(self, "No model", "Please select an accelerometer model.")
            return
        serial = self.serial_edit.text().strip()
        if not serial:
            QMessageBox.warning(self, "Serial required",
                                "Please enter the serial number of the unit under test.")
            return
        freqs = self._selected_freqs()
        if not freqs:
            QMessageBox.warning(self, "No frequencies",
                                "Please tick at least one frequency.")
            return

        # choose the backend
        if self.sim_check.isChecked():
            backend = SimulationBackend(serial=serial)
        elif nvgate_available():
            backend = NVGateBackend()
        else:
            ans = QMessageBox.question(
                self, "NVGate not detected",
                "NVGate is not reachable. Run in SIMULATION instead?\n\n"
                "(Choose No to cancel and launch NVGate first.)")
            if ans != QMessageBox.Yes:
                return
            backend = SimulationBackend(serial=serial)

        operator = self.operator_edit.text().strip()

        # reset UI for a run
        self.table.setRowCount(0)
        self.overall.setText("")
        self.progress.setValue(0)
        self.open_btn.setEnabled(False)
        self._last_report = None
        self._set_running(True)
        self.status.setText("Starting…")

        # launch worker thread
        self._thread = QThread()
        self._worker = CalibrationWorker(backend, model, serial, operator, freqs)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.progress.connect(self._on_progress)
        self._worker.finished.connect(self._on_finished)
        self._worker.failed.connect(self._on_failed)
        self._thread.start()

    def _cancel(self):
        if self._worker:
            self._worker.cancel()
            self.status.setText("Cancelling…")
            self.cancel_btn.setEnabled(False)

    def _on_progress(self, kw):
        stage = kw.get("stage")
        index, total = kw.get("index", 0), kw.get("total", 0)
        freq = kw.get("freq_hz")
        if stage == "measuring":
            self.status.setText(f"Measuring {freq:g} Hz …  ({index}/{total})")
        elif stage == "point_done":
            self._append_point(kw.get("point"))
            if total:
                self.progress.setValue(int(index / total * 100))

    def _append_point(self, point):
        if point is None:
            return
        r = self.table.rowCount()
        self.table.insertRow(r)
        values = [
            f"{point.freq_hz:g}",
            f"{point.sensitivity_mv_per_g:.4g}",
            f"{point.sensitivity_mv_per_ms2:.4g}",
            f"{point.phase_deg:+.1f}",
            f"{point.deviation_pct:+.2f}",
            point.verdict + (f"  ({point.note})" if point.note else ""),
        ]
        for c, text in enumerate(values):
            item = QTableWidgetItem(text)
            if c == 5:
                item.setForeground(QColor(VERDICT_COLORS.get(point.verdict, "#000")))
                f = item.font(); f.setBold(True); item.setFont(f)
            self.table.setItem(r, c, item)

    def _on_finished(self, result):
        self._teardown_thread()
        self.progress.setValue(100)
        verdict = result.overall_verdict
        self.overall.setText(f"Overall: {verdict}")
        self.overall.setStyleSheet(f"color:{VERDICT_COLORS.get(verdict, '#000')};")

        # write the certificate
        self.status.setText("Writing certificate…")
        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            path = build_certificate(result, out_dir=self.out_edit.text().strip() or None)
            self._last_report = path
            self.status.setText(f"Done. Report saved: {path}")
            self.open_btn.setEnabled(True)
        except Exception as e:
            self.status.setText("Calibration finished, but the report failed.")
            QMessageBox.critical(self, "Report error",
                                 f"The calibration finished but the report could "
                                 f"not be written:\n{e}")
        finally:
            QApplication.restoreOverrideCursor()
        self._set_running(False)

    def _on_failed(self, msg):
        self._teardown_thread()
        self._set_running(False)
        if msg == "__cancelled__":
            self.status.setText("Cancelled.")
            return
        self.status.setText("Failed.")
        QMessageBox.critical(self, "Calibration error", msg)

    def _teardown_thread(self):
        if self._thread:
            self._thread.quit()
            self._thread.wait()
        self._thread = None
        self._worker = None

    def _set_running(self, running):
        self.start_btn.setEnabled(not running)
        self.cancel_btn.setEnabled(running)
        self.model_combo.setEnabled(not running)
        self.serial_edit.setEnabled(not running)
        self.operator_edit.setEnabled(not running)
        self.sim_check.setEnabled(not running)

    def _open_report(self):
        if self._last_report and Path(self._last_report).exists():
            try:
                os.startfile(str(self._last_report))  # Windows
            except Exception as e:
                QMessageBox.information(self, "Open report",
                                       f"Report is here:\n{self._last_report}\n\n({e})")

    def closeEvent(self, event):
        if self._worker:
            self._worker.cancel()
            self._teardown_thread()
        event.accept()


def run():
    app = QApplication.instance() or QApplication(sys.argv)
    win = MainWindow()
    win.show()
    return app.exec()
