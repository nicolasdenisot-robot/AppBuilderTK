"""
Accelerometer model list — load and save the editable models file.

Each model carries the data the calibration needs: its nominal sensitivity (in
its own unit), the allowed pass/fail tolerance, and the input type. The list is
read from an editable JSON file that lives beside the deliverable so the operator
can add models without touching the program.
"""

import json
import shutil
from dataclasses import dataclass

from .config import G_TO_MS2, CONFIG
from .resources import bundled_path, external_dir

MODELS_FILENAME = "accelerometer_models.json"


@dataclass
class AccelModel:
    name: str
    manufacturer: str
    nominal_sensitivity: float   # in `unit`
    unit: str                    # "mV/g" or "mV/(m/s^2)"
    tolerance_pct: float
    input_type: str              # "IEPE" or "charge"

    @property
    def nominal_mv_per_ms2(self):
        """Nominal sensitivity expressed in mV/(m/s^2)."""
        if self.unit == "mV/g":
            return self.nominal_sensitivity / G_TO_MS2
        return self.nominal_sensitivity

    @property
    def nominal_mv_per_g(self):
        """Nominal sensitivity expressed in mV/g."""
        if self.unit == "mV/g":
            return self.nominal_sensitivity
        return self.nominal_sensitivity * G_TO_MS2

    @classmethod
    def from_dict(cls, d):
        return cls(
            name=str(d["name"]),
            manufacturer=str(d.get("manufacturer", "")),
            nominal_sensitivity=float(d["nominal_sensitivity"]),
            unit=str(d.get("unit", "mV/g")),
            tolerance_pct=float(d.get("tolerance_pct", CONFIG.default_tolerance_pct)),
            input_type=str(d.get("input_type", "IEPE")),
        )


def models_file_path():
    """
    Return the path to the editable models file.

    In a packaged delivery this is a writable copy beside the executable; the
    first time the app runs it is seeded from the version shipped inside the app
    so the operator has something to start from and can then edit it.
    """
    external = external_dir() / MODELS_FILENAME
    if external.exists():
        return external

    default = bundled_path(MODELS_FILENAME)
    if default.resolve() == external.resolve():
        return default  # development: the file already lives in the app folder

    try:
        if default.exists():
            shutil.copy2(default, external)
            return external
    except OSError:
        pass
    return default


def load_models():
    """Return the list of AccelModel, sorted by name. Raises on a broken file."""
    path = models_file_path()
    data = json.loads(path.read_text(encoding="utf-8"))
    models = [AccelModel.from_dict(m) for m in data.get("models", [])]
    models.sort(key=lambda m: m.name.lower())
    return models
