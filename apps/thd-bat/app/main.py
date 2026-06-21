"""
thd-bat — Total Harmonic Distortion calculator.

Connects to a running NVGate session, reads the spectrum from Window2,
finds the fundamental frequency (peak amplitude), places a Harmonic marker
in Window2, computes THD from harmonics 2–5, and displays the result in a
new scalar window inside NVGate.

Run:  python app/main.py          (development)
      launch_thd.bat              (operator)
"""

import sys
import math
import datetime
from pathlib import Path

# ── Path setup: works both inside this workspace and in an exported bundle ──
_HERE = Path(__file__).resolve()
for _candidate in (_HERE.parents[3] / "shared", _HERE.parents[1]):
    if (_candidate / "oros_helpers").is_dir() and str(_candidate) not in sys.path:
        sys.path.insert(0, str(_candidate))

import oros_helpers  # noqa: F401  — side-effect: calls ensure_pynvdrive()
from oros_helpers import connect, is_nvgate_available

import pynvdrive
from pynvdrive.command import CommandAction
from pynvdrive.commands.marker import GetWindowTraces, GetWindowDisplayZone
from pynvdrive.commands.signalresult import (
    CreateResultEx, GetResultEx, DeleteAllResultEx, CreateTCPResultChannel,
)
from pynvdrive.commands.graphics import AddWindowResult
from pynvdrive.commands.graphics.getcurrentlayout import GetCurrentLayout
from pynvdrive.formats.result import Result
from pynvdrive.formats.blocks import HEAD, SCAL, INFO, TCPRESULT


# ── Custom NVDrive commands (not yet wrapped in pynvdrive Python library) ───
# The class name must match the NVDrive command name exactly.

class AddHarmonicMarker(CommandAction):
    """Add a harmonic marker to a display zone (NVDrive manual §3.2.9)."""
    def __init__(self, window_name, start_position, num_harmonics=5, display_zone=''):
        super().__init__(
            name=None,
            parameters=[window_name, str(start_position), str(num_harmonics), str(display_zone)],
        )


# ── Configuration ───────────────────────────────────────────────────────────

WINDOW_SPECTRUM = "Window2"   # NVGate window that shows the spectrum
NUM_HARMONICS   = 5           # H1 (fundamental) + H2..H5
THD_WINDOW_NAME = "THD"       # name for the new NVGate scalar window


# ── Spectrum helpers ────────────────────────────────────────────────────────

def get_amplitudes(result):
    """
    Return a flat list of linear amplitude values from a spectrum result.
    Handles both RVEC (real/amplitude spectrum) and CVEC (complex spectrum).
    """
    if result.rvec is not None:
        return list(result.rvec.data)
    if result.cvec is not None:
        # CVEC.data is a list of (real, imag) tuples
        return [math.sqrt(d[0] ** 2 + d[1] ** 2) for d in result.cvec.data]
    return None


def find_fundamental(amplitudes, freq_start, freq_stop):
    """Return (index, frequency_Hz, amplitude) for the highest-amplitude bin."""
    idx = max(range(len(amplitudes)), key=lambda i: amplitudes[i])
    n   = len(amplitudes)
    freq = freq_start + idx * (freq_stop - freq_start) / max(n - 1, 1)
    return idx, freq, amplitudes[idx]


def amplitude_at(amplitudes, freq_start, freq_stop, target_hz):
    """Amplitude at the spectrum bin nearest to target_hz."""
    n  = len(amplitudes)
    df = (freq_stop - freq_start) / max(n - 1, 1)
    idx = int(round((target_hz - freq_start) / df))
    idx = max(0, min(idx, n - 1))
    return amplitudes[idx]


# ── THD formula ─────────────────────────────────────────────────────────────

def compute_thd(h1, h2, h3, h4, h5):
    """Standard THD (%) = √(H2²+H3²+H4²+H5²) / |H1| × 100."""
    if abs(h1) == 0:
        raise ValueError("Fundamental amplitude is zero — cannot divide.")
    return math.sqrt(h2**2 + h3**2 + h4**2 + h5**2) / abs(h1) * 100.0


# ── NVGate scalar injection ─────────────────────────────────────────────────

def inject_scalar_percent(client, value_pct, name="THD"):
    """
    Push a percentage scalar into NVGate via a TCP result channel.
    Returns the channel id assigned by NVGate.
    """
    head = HEAD(
        version=5,
        result_type=1,           # 1 = scalar
        size=1,
        dimension=1,
        is_complex=0,
        measure_status=2,        # 2 = measurement finished / ready
        physical_quantity="",    # must be empty so get_unit uses magnitude_key only
        unit_name=None,          # let pynvdrive pick the SI unit automatically
        unit_label=None,
        name=name,
        overall_level_status=0,
        weighted_ol_status=0,
        weighting_window=0,
        magnitude_key="Percentage",
    )
    # value_pct is in %; pynvdrive converts it to SI (ratio) before sending to NVGate.
    # NVGate receives the ratio and redisplays it in % using its Percent display unit.
    scal = SCAL(
        version=2,
        min=value_pct,
        max=value_pct,
        value=value_pct,
        rel_precision=0.001,
        abs_precision=1e-30,
        imag=0.0,
    )
    info = INFO(
        version=1,
        info_mask=0,
        date=datetime.datetime.now(),
        global_level=0,
        weighted_global_level=0,
        tacho=0,
    )
    result  = Result(head=head, scal=scal, info=info)
    tcp_res = TCPRESULT(
        module=498,
        process=182,             # NVC SCALAR
        channel=1,
        ref_channel=0,
        input_name="THD_Result",
        result=result,
    )
    cmd = CreateTCPResultChannel(tcp_result=tcp_res)
    client.send_command(cmd)
    return cmd.value            # channel id assigned by NVGate


# ── Main flow ───────────────────────────────────────────────────────────────

def main():
    print("=" * 55)
    print("  THD Calculator — thd-bat")
    print("=" * 55)

    # Guard: NVGate must be reachable
    if not is_nvgate_available():
        print("\nERROR: Cannot reach NVGate.")
        print("  Make sure NVGate is running and in connected mode, then try again.")
        return 1

    print("\nConnecting to NVGate...")

    with connect() as client:

        # ── 1. Identify the trace in Window2 ─────────────────────────────────
        print(f"\n[1] Reading trace info from '{WINDOW_SPECTRUM}'...")
        try:
            cmd = GetWindowTraces(window_name=WINDOW_SPECTRUM)
            client.send_command(cmd)
        except pynvdrive.NVDriveCommandError as e:
            print(f"\nERROR: Could not read '{WINDOW_SPECTRUM}': {e.error}")
            print(f"  Is '{WINDOW_SPECTRUM}' open and showing a spectrum?")
            return 1

        if not cmd.list_result_format_and_description:
            print(f"\nERROR: '{WINDOW_SPECTRUM}' is empty — no trace found.")
            return 1

        trace   = cmd.list_result_format_and_description[0]
        module  = trace.module_id
        process = trace.process_id
        channel = trace.channel_number
        ref_ch  = trace.reference_channel_number or 0
        print(f"  module={module}  process={process}  channel={channel}")

        # ── 2. Download the spectrum data ─────────────────────────────────────
        print("\n[2] Downloading spectrum data...")
        try:
            client.send_command(DeleteAllResultEx())
        except pynvdrive.NVDriveCommandError:
            pass  # nothing registered yet — fine

        try:
            client.send_command(
                CreateResultEx(module=module, process=process,
                               channel=channel, reference_channel_number=ref_ch)
            )
            cmd_r = GetResultEx(module=module, process=process,
                                channel=channel, reference_channel_number=ref_ch)
            client.send_command(cmd_r)
            result = cmd_r.result
        except pynvdrive.NVDriveCommandError as e:
            print(f"\nERROR: Could not fetch spectrum data: {e.error}")
            return 1

        # ── 3. Extract amplitudes and frequency axis ──────────────────────────
        amplitudes = get_amplitudes(result)
        if amplitudes is None:
            print("\nERROR: The result in Window2 is not a spectrum (no RVEC or CVEC block).")
            print("  Please make sure Window2 shows an FFT spectrum.")
            return 1

        if result.xreg is None:
            print("\nERROR: No frequency axis found in the spectrum result.")
            print("  Only regular (linear-frequency) FFT spectra are supported.")
            return 1

        freq_start = result.xreg.start
        freq_stop  = result.xreg.stop
        n_bins     = len(amplitudes)
        print(f"  {n_bins} bins,  {freq_start:.2f} – {freq_stop:.2f} Hz")

        # ── 4. Find fundamental frequency ─────────────────────────────────────
        print("\n[3] Finding fundamental frequency...")
        _, f0, h1 = find_fundamental(amplitudes, freq_start, freq_stop)
        print(f"  f0 = {f0:.4f} Hz   H1 = {h1:.6g}")

        if 5 * f0 > freq_stop:
            print(f"\n  WARNING: 5th harmonic ({5*f0:.1f} Hz) exceeds the spectrum range ({freq_stop:.1f} Hz).")
            print("  Harmonics outside the range will read the edge bin value.")

        # ── 5. Get display-zone type of Window2 ───────────────────────────────
        display_zone = ''
        try:
            cmd_dz = GetWindowDisplayZone(window_name=WINDOW_SPECTRUM)
            client.send_command(cmd_dz)
            if cmd_dz.list_display_zone_type:
                display_zone = cmd_dz.list_display_zone_type[0]
        except pynvdrive.NVDriveCommandError:
            pass  # leave display_zone empty; NVGate will use its default

        # ── 6. Add Harmonic marker in Window2 (for visual display) ────────────
        print(f"\n[4] Adding Harmonic marker at {f0:.4f} Hz ({NUM_HARMONICS} harmonics)...")
        try:
            client.send_command(
                AddHarmonicMarker(
                    window_name=WINDOW_SPECTRUM,
                    start_position=f0,
                    num_harmonics=NUM_HARMONICS,
                    display_zone=display_zone,
                )
            )
            print("  Marker added.")
        except pynvdrive.NVDriveCommandError as e:
            print(f"  WARNING: Could not add Harmonic marker: {e.error}")
            print("  Continuing — THD will still be calculated.")

        # ── 7. Read harmonic amplitudes from the spectrum data ─────────────────
        print("\n[5] Extracting harmonic amplitudes...")
        h2 = amplitude_at(amplitudes, freq_start, freq_stop, 2 * f0)
        h3 = amplitude_at(amplitudes, freq_start, freq_stop, 3 * f0)
        h4 = amplitude_at(amplitudes, freq_start, freq_stop, 4 * f0)
        h5 = amplitude_at(amplitudes, freq_start, freq_stop, 5 * f0)
        print(f"  H1 = {h1:.6g}")
        print(f"  H2 = {h2:.6g}  ({2*f0:.2f} Hz)")
        print(f"  H3 = {h3:.6g}  ({3*f0:.2f} Hz)")
        print(f"  H4 = {h4:.6g}  ({4*f0:.2f} Hz)")
        print(f"  H5 = {h5:.6g}  ({5*f0:.2f} Hz)")

        # ── 8. Calculate THD ───────────────────────────────────────────────────
        print("\n[6] Computing THD...")
        try:
            thd = compute_thd(h1, h2, h3, h4, h5)
        except ValueError as exc:
            print(f"\nERROR: {exc}")
            return 1

        print(f"\n  ★  THD = {thd:.2f} %\n")

        # ── 9. Inject scalar result into NVGate ────────────────────────────────
        print("[7] Sending THD result to NVGate...")
        try:
            channel_id = inject_scalar_percent(client, thd, name="THD")
        except pynvdrive.NVDriveCommandError as e:
            print(f"\nERROR: Could not create scalar channel in NVGate: {e.error}")
            return 1

        # ── 10. Open new window to display the scalar ──────────────────────────
        try:
            cmd_lay = GetCurrentLayout()
            client.send_command(cmd_lay)
            layout = cmd_lay.value or "Layout1"
        except pynvdrive.NVDriveCommandError:
            layout = "Layout1"

        try:
            client.send_command(
                AddWindowResult(
                    layout=layout,
                    window=THD_WINDOW_NAME,
                    module=498,
                    process=182,
                    channel=channel_id,
                    existing_result_is_an_error='0',
                )
            )
            print(f"  Window '{THD_WINDOW_NAME}' opened in layout '{layout}'.")
        except pynvdrive.NVDriveCommandError as e:
            print(f"  WARNING: Could not open the THD window: {e.error}")
            print(f"  The result channel was created (id={channel_id}).")
            print("  You can open it manually in NVGate.")

    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
