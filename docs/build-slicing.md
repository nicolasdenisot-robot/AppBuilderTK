# Build-slicing — how to split an app into milestones (and prototype the UI cheaply)

Rule #10 says: split every app into **the smallest slices that each end in tested,
working code**, propose that list, get a go-ahead, then build slice by slice. This
doc is the *how*: how to decide where the slice boundaries go, and — for any app with
a custom screen — how to get the interaction in front of the user early **without**
paying for it twice.

---

## Part A — Choosing the milestone boundaries

### The yardstick

Every candidate slice is judged by one question: **can I run it and verify it when
it's done?** A milestone is only ticked once it is *built, tested, and committed*
(rule #10). A slicing plan that produces a step you can't actually exercise is the
wrong plan, however tidy it looks.

Second reality for NVGate apps: **the riskiest, least-predictable part is almost
always the live-analyzer integration** — getting a real result out of NVGate over
pynvdrive with the right IDNs, settings whose effect isn't visible until you look,
timing quirks. The
deterministic parts (judging a threshold, formatting an Excel sheet) are the *easy,
reliable* parts. Good slicing front-loads the uncertainty, not the comfort.

### The strategies (and when each fits)

| Strategy | Slice by… | Good when | Watch out for |
|----------|-----------|-----------|---------------|
| **Walking skeleton** *(default)* | thinnest end-to-end pipeline first, then thicken each stage | almost always | keep slice 1 genuinely thin — resist polishing |
| **Risk-first** | hardest unknown first | integration or feasibility is uncertain | a pure spike can produce throwaway code — fold it into a real slice |
| **By functionality** | one capability per slice | the flow is well understood | integration risk can hide at the end; order matters |
| **By pipeline stage** | input → process → output | offline batch/file apps | risky stage may sit last |
| **By layer (UI-first / back-end-first)** | screen vs engine | *see Part B* | a UI on stubs isn't "tested, working code" — the trap Part B fixes |

### The recommended default

For a typical NVGate app, combine the top three:

1. **Walking skeleton first**, routed through the riskiest integration (risk-first
   *ordering*). Slice 1 = *connect → get one real number out of NVGate → trivial
   judge → trivial output*. If NVGate is going to fight you, you learn it on day one,
   and you have a runnable app from the first checkpoint.
2. **Then thicken in vertical functionality slices** — real thresholds, full export,
   edge cases — each independently testable because the skeleton already runs.
3. **UI is handled by Part B**, not bolted on at the end.

Also front-load slices that need a **live analyzer and the user in the room** to
verify; defer the pure-deterministic slices (pass/fail math, Excel formatting) you
can test alone. That batches the user's involvement at the start instead of
scattering it.

---

## Part B — The UI: an interactive prototype on a fake engine

The user judges the app by what they **see and click**. A static mockup proves the
*look*; only a *clickable* prototype proves **all the functionality they need is
there** — that there's a place to enter the serial number, a way to retest after a
fail, an error message when NVGate is down. Discovering a missing interaction at
delivery is the most expensive discovery there is. So for **any non-trivial app with
a custom UI, the default is to build an interactive prototype driven by dummy data,
and get sign-off on it, before building the real engine.**

The trick is to make that prototype **become the shipped UI** instead of throwaway.

### The move: put the fake behind a seam (the "engine contract")

Separate the screen from the engine with a thin, fixed set of calls the UI makes —
the *contract*. Everything the UI needs from the outside world goes through it:

```
connect()            start_measurement()      get_result()
judge(result)        export(result, path)     cancel()
```

The screen only ever talks to those. Then write **two** implementations behind them:

- **`FakeEngine`** — returns simulated data, fakes a few-second "measuring," and can
  be told to force a pass or a fail. Built in minutes.
- **`RealEngine`** — talks to NVGate. Built later.

The UI cannot tell them apart, so shipping is just swapping which engine is plugged
in (dependency injection). **The interaction is built once.** The prototype *is* the
real front-end, running on the fake.

This meets the walking skeleton from Part A in the middle: the skeleton runs the
*real* engine end-to-end-thin; the prototype runs the *real UI* on the *fake* engine;
they join **at the contract**.

### The interactions worth faking

Cheap and high-value:
- **Run → progress → result appears** (a timer + canned data).
- **A switch to force a fail**, so the user sees the PASS/FAIL states and confirms
  they read correctly.
- **Navigation** between screens/tabs, so they confirm the flow matches how they work.

The under-rated ones that justify the whole exercise — exactly what users find missing:
- **Error states**: NVGate not connected, no signal, out of range. Give `FakeEngine`
  a switch to *inject* each, so the error UX gets approved cheaply, not met on a bad
  day in production.
- **Cancel mid-run / retest without restarting** — workflow gaps a static screen hides.
- **Operator input + validation** — empty serial number, wrong channel: does the
  screen push back the way they want?

### The discipline: simulate the *constraints*, not the happy path

The failure mode of this technique: a fake that makes everything smooth and instant
earns enthusiastic sign-off — then `RealEngine` reveals the result is only available
*after Save*, takes 30 seconds, and *can't* be cancelled mid-run, and the approved
interaction is unbuildable. **Bake the constraints you already know into `FakeEngine`**
— known latencies, known ordering (a result only exists after Save), known
"can't cancel." Pull them from `DIRECTIVE.md` §9 "Lessons learned." The simulator's
job is an *honest rehearsal*, not a good demo.

### A bonus: the fake also extracts the spec

To write `get_result()` for the fake you must decide *what it returns* — one number? a
spectrum? a value plus timestamp plus channel? That decision **is** the requirement,
surfaced early. The finished prototype is an **executable spec**: a non-programmer
confirms scope by *doing* ("yes, everything I need is here") rather than reading a
document — far stronger sign-off.

### When it is NOT worth it

Be honest about the cost:
- **Small apps.** If the engine is one result against one threshold, faking it costs
  about as much as building it real — and the real walking skeleton is *already*
  interactive. Skip the fake; just build the skeleton.
- **Wrong stack.** Don't prototype in a design tool you'll throw away. Build the
  prototype in the **shipping stack** (PySide6 / Streamlit / Tkinter) on the fake
  engine, so it becomes the app. Fake the async with a `QTimer` (Qt) or
  `time.sleep` + spinner (Streamlit) in a few lines.

A quiet, large win for this workspace: the fake engine lets you and the user iterate
on the whole interaction **without NVGate or a real signal in the room** — on any
laptop, anytime. The expensive, location-bound part (a live analyzer with a real part
on it) is deferred to the very end, when the screen and flow are already locked.

### How it reshapes the milestones

For an app with a custom UI, the default slice order becomes:

1. **Define the engine contract + `FakeEngine`** (constraints baked in) — small, and
   it pins down the spec.
2. **Build the full interactive UI on the fake** — tested, working code, and the
   *real* screen.
3. **— sign-off gate —** the user clicks through and confirms every needed
   interaction is present; comments land while they're cheap.
4. **Build `RealEngine` piece by piece** (the walking skeleton) and swap it in behind
   the unchanged contract.

The expensive engine is built once, against requirements the user has *exercised* —
not just read — and the screen they approved is the screen that ships.

---

## In practice

- Propose the slice list (Part A order, or the Part-B order for a UI app) and get the
  go-ahead **before building** — rule #10, no app too small to plan.
- `/frontend-design <app>` builds the interactive prototype on the fake and runs the
  sign-off gate; it reaches for this pattern by default.
- Record the chosen slices in `DIRECTIVE.md` §10 "Build state"; tick each as it's
  built, tested, and committed. `/checkpoint` saves progress between slices.
