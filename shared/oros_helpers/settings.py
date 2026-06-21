"""
Read and write NVGate settings by their identification number (IDN).

A setting IDN looks like ``'001.001.201'`` or a named form like
``'frontEnd.inputSettings.inputSampling'``. In NVGate you can reveal a setting's
IDN with SHIFT + right-click on it (see NVDrive manual 3.6.1).
"""

from ._bootstrap import ensure_pynvdrive

ensure_pynvdrive()

import pynvdrive
from pynvdrive.commands.settingsstates import (
    GetSettingValue,
    SetSettingValue,
    GetSettingValues,
)


def get_setting(idn, client=None):
    """
    Return the current value of the setting `idn`.

    Pass an existing `client` to reuse a connection, or leave it None to open a
    short-lived one.
    """
    return _with_client(client, lambda c: _get_setting(c, idn))


def set_setting(idn, value, client=None):
    """Set the setting `idn` to `value`."""
    return _with_client(client, lambda c: _set_setting(c, idn, value))


def list_setting_choices(idn, client=None):
    """
    For an enumerated setting, return its list of possible values
    (e.g. the available sensors, ranges, units...).
    """
    return _with_client(client, lambda c: _get_setting_values(c, idn))


# --- internals -------------------------------------------------------------

def _get_setting(client, idn):
    cmd = GetSettingValue(idn=idn)
    client.send_command(cmd)
    return cmd.value


def _set_setting(client, idn, value):
    cmd = SetSettingValue(idn=idn, value=value)
    client.send_command(cmd)
    return True


def _get_setting_values(client, idn):
    cmd = GetSettingValues(idn=idn)
    client.send_command(cmd)
    return cmd.value


def _with_client(client, fn):
    if client is not None:
        return fn(client)
    from .connection import connect
    with connect() as c:
        return fn(c)
