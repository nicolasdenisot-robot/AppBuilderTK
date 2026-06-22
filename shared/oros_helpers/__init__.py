"""
oros_helpers — reusable building blocks for NVGate / OROS apps.

Importing this package makes the vendored `pynvdrive` library importable, whether
you are running inside this workspace (it finds pynvdrive in resources/Framework)
or from an exported app bundle (where pynvdrive has been vendored next to it).

Typical use:

    from oros_helpers import connect, run_measurement, get_scalar_result
    from oros_helpers import get_setting, set_setting
    from oros_helpers.export import results_to_excel

See each module for details. Prefer these helpers over re-writing connection /
result / export code in every app (CLAUDE.md rule #6).
"""

from ._bootstrap import ensure_pynvdrive

ensure_pynvdrive()

from .connection import connect, is_nvgate_available
from .settings import get_setting, set_setting, list_setting_choices
from .results import (
    run_measurement,
    stop_measurement,
    list_results,
    get_scalar_result,
    get_result,
    clear_results,
)

__all__ = [
    "ensure_pynvdrive",
    "connect",
    "is_nvgate_available",
    "get_setting",
    "set_setting",
    "list_setting_choices",
    "run_measurement",
    "stop_measurement",
    "list_results",
    "get_scalar_result",
    "get_result",
    "clear_results",
]
