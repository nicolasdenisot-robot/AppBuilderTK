# Where to get calculations (algorithms)

**Rule of order — always check Tier 1 first.**

## Tier 1 — Let NVGate compute it (preferred)

If NVGate already produces the result, **drive NVGate and fetch it** — do not
re-implement it in Python. NVGate natively does:

- FFT spectra, averaging, overall / RMS levels
- 1/n-octave (1/1, 1/3, 1/12, 1/24…)
- **Order tracking, order spectra, waterfalls, Campbell diagrams** (core for rotating machinery)
- FRF (frequency response functions), coherence
- Filtering, weighting, integration/derivation

Fetch with `oros_helpers.results` (`get_result`, `get_scalar_result`, `list_results`).
Reimplementing an FFT the analyzer already made is the #1 mistake — avoid it.

## Tier 2 — General scientific Python (PyPI)

For math NVGate doesn't do, or post-processing of fetched data:

| Package | Use |
|---------|-----|
| **numpy** | arrays, FFT (`numpy.fft`), math |
| **scipy** | `scipy.signal` (filtering, Welch PSD, spectrogram, peak-finding, Hilbert/envelope, resampling), `scipy.fft`, `scipy.stats` |
| **pandas** | tables, time series, CSV/Excel |
| **openpyxl / xlsxwriter** | write Excel files |
| **matplotlib / plotly** | plots for a custom UI |
| **python-docx / reportlab / Jinja2 + WeasyPrint** | generated reports / PDF |

## Tier 3 — Domain libraries (PyPI + GitHub)

### Rotating machinery / turbomachinery
> NVGate already does order tracking, waterfall/Campbell, FFT (Tier 1). Use these
> only for what it doesn't do.

| Package | Use |
|---------|-----|
| **ross-rotordynamics** (`ross`) | Rotordynamics: Campbell diagrams, critical speeds, mode shapes, unbalance/whirl response — turbomachinery rotor modeling |
| **scipy.signal + PyWavelets** (`pywt`) | Envelope analysis / demodulation for bearing & gear-mesh fault detection, transient capture |
| **tsfresh + scikit-learn** | Feature extraction & ML for condition monitoring / diagnostics (trend, anomaly, fault classification) |

### Sound quality (psychoacoustics)
| Package | Use |
|---------|-----|
| **mosqito** | **The** sound-quality toolbox: loudness (ISO 532-1 Zwicker), sharpness, roughness, fluctuation strength, tonality |
| **python-acoustics** | A/C/Z weighting, octave/third-octave bands, general acoustics |
| **librosa / waveform_analysis** | audio feature extraction, THD, A-weighting |

## How Claude uses this
1. Confirm the calculation isn't already a Tier-1 NVGate result.
2. If it needs Python, pick the smallest capable package, add it to the app's
   `requirements.txt`, and `pip install` it.
3. Record the choice (and why NVGate couldn't do it) in the app's `DIRECTIVE.md` §5.

> **PyPI** = the Python Package Index (pypi.org), the central store `pip install`
> downloads from. "On PyPI" means one-command install.
