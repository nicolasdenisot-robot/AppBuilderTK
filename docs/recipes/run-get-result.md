# Recipe: run a measurement and get a result

**Goal:** start the analyzer, let it acquire, stop, and read a result value.
**Layer:** live control (NVGate running). **Prereq:** inputs connected, a result
visible/available in NVGate.

```python
from oros_helpers import connect, run_measurement, list_results, get_scalar_result

with connect() as client:
    # 1. discover what results are available (optional, for finding addresses)
    for r in list_results(client=client):
        print(r.module_id, r.process_id, r.channel_number)

    # 2. run for 10 seconds then stop
    run_measurement(duration_s=10, client=client)

    # 3. read a scalar (e.g. an overall level). Replace with your address.
    level = get_scalar_result(module=2, process=10, channel=1, client=client)
    print("Level:", level)
```

## Notes
- A result address is `(module, process, channel, reference_channel_number)`.
  Get real addresses from `list_results()` or `GetWindowTraces` on a displayed window.
- For spectra/vectors use `get_result(...)` and inspect `result.to_dict()`.
- For waterfalls pass `waterfall=True` to `get_result`.
- Record the addresses you used in the app's `DIRECTIVE.md` §3.
