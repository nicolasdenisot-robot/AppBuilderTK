# Recipe: end-of-line pass/fail test

**Goal:** measure a unit, judge it against limits, show PASS/FAIL, export results.
**Layer:** live control. **Archetype:** 2.

> Reliability first (CLAUDE.md §3): the verdict is **deterministic code**, never an
> AI guess. Limits live in the app, fixed and testable.

```python
from oros_helpers import connect, run_measurement, get_scalar_result
from oros_helpers.export import results_to_excel, timestamped_name

# Fixed test limits — the heart of a pass/fail station. Tune per product.
LIMIT_DB = 95.0

def run_unit(serial):
    with connect() as client:
        run_measurement(duration_s=5, client=client)
        level = get_scalar_result(module=2, process=10, channel=1, client=client)

    verdict = "PASS" if level <= LIMIT_DB else "FAIL"
    return [serial, round(level, 2), LIMIT_DB, verdict]

if __name__ == "__main__":
    row = run_unit(serial="SN-0001")
    print(row)
    results_to_excel(
        rows=[row],
        headers=["Serial", "Level dB", "Limit dB", "Verdict"],
        path=timestamped_name("eol_result"),
    )
```

## Build checklist
- [ ] Limits and channels confirmed with the user → `DIRECTIVE.md` §3 / §7.
- [ ] Operator entry (serial number) — keyboard, barcode, or fixed.
- [ ] Where the verdict shows: NVGate window vs custom UI (CLAUDE.md stop #4).
- [ ] Export path agreed (network share? local folder?).
- [ ] Edge cases: NVGate down, no signal, out-of-range → clear operator message.
- [ ] Export form: `.exe` for the operator (confirm first, CLAUDE.md stop #6).
- [ ] Optional report: see `generate-report.md`.
