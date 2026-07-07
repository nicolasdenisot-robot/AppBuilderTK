# NVGate App-Building Workspace — Feature Overview

*A plain-language introduction for colleagues. No programming knowledge needed.*

> **📊 Slide deck version:** present or share this as a web page —
> <https://claude.ai/code/artifact/f8b584cd-cad5-4703-881b-cc23cdcbb470>
> (source: [workspace-overview-deck.html](workspace-overview-deck.html))

---

## What this workspace is — in one sentence

**You describe the outcome you want ("a pass/fail test that exports to Excel"), and
the workspace turns it into a finished, shippable application — without you writing
any code.**

The key idea: **the AI does the building and the decisions; plain, tested code does
the actual work in the delivered app.** That means a delivered app behaves
*identically every time* — a pass/fail result is never a guess — and it has **zero AI
inside it** once shipped.

---

## The main features

### 1. It interviews you before building
Instead of guessing, it walks you through a short **6-question interview** and lets
you pick at each real decision:
- **What's the goal**, and who runs the finished app — you, or an operator who just
  clicks an icon?
- **Live analyzer** (NVGate running, real-time) or **saved files** (offline)?
- **Where results appear** — inside NVGate, or on a custom branded screen?
- **How it's delivered** — a standalone `.exe`, or the source with a click-to-run file.
- **Where the operator launches it** — desktop icon, NVGate's Automation menu, a
  scheduled task.

It always explains the trade-offs and lets *you* choose — it never silently assumes.

### 2. Build from scratch **or** from an app you already have
- **From scratch** — the interview above.
- **From an existing app** — point it at code you already have (even code from
  elsewhere) and it reads it, reverse-engineers what it does, and writes up a
  plain-language overview. Same for scoping a change to an app that already exists.

### 3. Every app gets a written spec — `DIRECTIVE.md`
The interview answers are captured in a single **spec document per app** that becomes
the "source of truth" for how that app should behave. It's a *living* document — as
the app is built and lessons are learned, they get recorded there, so the next work
session (or the next app) benefits.

### 4. Big builds are split into milestones — and progress is saved
Complex apps are **sliced into small, tested steps** rather than built in one risky
go. The build progress (what's done, what's next) is **saved into the app's spec**, so
if you **run out of time you can open a new session and pick up exactly where you left
off.** You can also save a checkpoint or roll back to an earlier one at any time.

### 5. It reuses proven building blocks
There's a shared library of tested code for the common jobs — **connecting to NVGate,
reading settings and results, exporting to Excel, generating reports** — plus a set of
**"recipes"** for typical tasks (pass/fail tests, run-and-get-a-result, export to
Excel, auto-report, notifications). New apps reuse these instead of reinventing them,
which makes them faster to build and more reliable.

### 6. Custom screens, prototyped cheaply first
If an app needs its own screen (not just NVGate's windows), it can build one — and for
anything non-trivial it shows you a **clickable prototype with dummy data for sign-off
first**, so you catch design issues early, before the real work goes in. Your company
logo/branding is applied automatically.

### 7. It writes the user-facing documents for you
When an app works end-to-end, it **automatically creates a plain-language `README`**
(how to use it, written for whoever will run it) and keeps a **`CHANGELOG`** that ships
with every delivery as a **"What's New"** file — so the operator always sees what
changed.

### 8. One-command delivery
When an app is ready, it's **packaged into a self-contained folder you can zip and
send** — either a standalone `.exe` (nothing to install) or the source plus a
click-to-run file. Whichever you chose in the interview.

### 9. A consistent, tidy structure
Every app lives in its **own self-contained folder** started from a **template**, with
a fixed layout (the runtime code, the spec, the docs, the delivery). This keeps every
project organized the same way and lets each one be shipped on its own.

### 10. Your original data is protected
A standing rule across everything: **your measurements, signals, NVGate projects and
settings are never deleted, overwritten, or edited in place.** When a task needs to
change such a file, it writes a **new, dated copy** and leaves the original untouched.

### 11. It speaks plain language
It's built on the assumption that the user knows **sound & vibration and NVGate — but
not programming, terminals, or packaging.** It explains everything without jargon, does
the technical work silently, and confirms before running or building anything on your
machine.

---

## Two ways it talks to NVGate

- **Live control** — drives a running analyzer in real time (run/stop, change
  settings, fetch live results).
- **File access** — reads and processes saved signals and results on disk, with
  NVGate closed.
