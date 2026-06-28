---
name: explore-codebase
description: "Understand or onboard ONE existing NVGate app under apps/. Produces a plain-language overview and, when the app has none, reverse-engineers its DIRECTIVE.md from the code. Use when the user says '/explore-codebase', 'understand my app', 'onboard an existing app', or wants to improve an app already in apps/. Takes an app name."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
  - Agent
  - AskUserQuestion
disable-model-invocation: true
---

You help the user **understand one existing app** so they can improve it, and — when
the app was just pasted in and has no spec yet — you **reverse-engineer its
`DIRECTIVE.md`** from the code. This is the first stop in the "improve an existing
app" workflow (`/explore-codebase` → `/scope-feature` → `/frontend-design`).

Remember who you are helping (CLAUDE.md §1): a sound-&-vibration engineer who is
**not a programmer**. Everything you write back must be in **plain language, no
jargon**. You do the technical reading silently.

## Input

The app name — everything after `/explore-codebase`, e.g. `/explore-codebase my-pass-fail-test`.
It maps to the folder `apps/<app-name>/`.

- If the user gave no name, list the folders under `apps/` (skip `_template`) and ask
  which one to explore (AskUserQuestion).
- If `apps/<app-name>/` does not exist, tell them plainly and point to the onboarding
  steps below.

### Onboarding an existing app (no folder yet)

If the user has app code from elsewhere and nothing under `apps/` yet, explain the
convention in plain words and offer to set it up for them (confirm first — rule #5):

- Copy `apps/_template/` to `apps/<name>/`, paste their **code** into `apps/<name>/app/`.
- **Runtime templates** the app loads (e.g. an Excel template it fills, a report
  template, a config file, an image) → `apps/<name>/app/` as **top-level files** (the
  export tool bundles those; load them with a bundle-aware helper — CLAUDE.md §6).
- **Source documents that only inform the build** (initial spec, example output,
  customer email — the app never opens them) → `apps/<name>/reference/`, which is
  never shipped. Distil their requirements into `DIRECTIVE.md`.

Then continue below; the app will have a template `DIRECTIVE.md` you will fill in.

## Process

**Step 1 — Launch up to three sub-agents in parallel** (Agent tool), each with its own
fresh context. Scope every agent to `apps/<app-name>/` only; they may also note which
**`shared/oros_helpers/`** and **`docs/recipes/`** the app reuses, but should not map
the whole workspace (that's already documented in CLAUDE.md and `docs/`).

**Agent 1 — App-flow mapper:**
- Find the entry point (`DIRECTIVE.md` `entry_point`, usually `app/main.py`) and the
  modules under `app/`.
- Trace the deterministic step sequence the app performs: set params → run → wait →
  fetch result → judge → export (whatever applies).
- Identify the capability layer: **live control** (`pynvdrive`, NVGate must be running)
  vs **file access** (`orostk`/DLLs, offline). Note any NVGate result/setting IDNs used.

**Agent 2 — Dependencies & reuse:**
- Read `requirements.txt` and list the PyPI packages with their purpose.
- Identify which `shared/oros_helpers/` modules and which `docs/recipes/` patterns the
  app already uses (this serves rule #6 — "reuse before you write" — for the next change).
- Note pynvdrive / orostk usage and any external files the app reads or writes.

**Agent 3 — UI & outputs:**
- Identify the UI stack in use: none/console, Tkinter, PySide6/Qt, or Streamlit.
- Where do results appear: inside NVGate (drive windows/layouts/markers) or a custom UI?
- What is the export form / output: Excel, CSV, report, data injected back into NVGate.

**Step 2 — Synthesize** the three results into a plain-language overview with these parts:

```markdown
## What this app does
[1–3 plain sentences: the outcome it produces, and for whom.]

## How it runs
[Live or offline; NVGate required or not; who launches it and from where.]

## The steps it performs
[The deterministic sequence, in plain numbered steps.]

## What it's built from
[UI stack; key packages; which shared helpers and recipes it reuses; NVGate IDNs.]

## Where results go
[In NVGate vs custom UI; export format and path.]

## Things to watch when changing it
[Quirks, edge cases, anything fragile found in the code.]
```

**Step 3 — Write it into the app's `DIRECTIVE.md`** (the per-app living spec — the one
source of truth; do not create a separate doc, and never write to the root `docs/`):

- **App already has a filled-in `DIRECTIVE.md`:** do **not** overwrite it (rule #5).
  Show the user what you found, point out anything that contradicts the existing spec,
  and append a dated **"Current state (from /explore-codebase, YYYY-MM-DD)"** note to
  the "Lessons learned" section. Ask before changing existing sections.
- **App has only the empty `_template` `DIRECTIVE.md` (newly onboarded):** fill in
  sections §1–§6 from what you found — this is the reverse-engineering step. Leave a note
  where you inferred vs confirmed something, and confirm the inferred parts with the user.

**Step 4 — Present a short summary** to the user in plain language: what the app does,
what it's built from, and 2–3 things worth knowing before changing it. Keep it brief —
the detail is now in `DIRECTIVE.md`. Suggest `/scope-feature <app-name>` as the next step.

## Guidelines

- Plain language always. If a technical word is unavoidable, define it in one short sentence.
- Be specific — name real files (`app/main.py`), helpers, and recipes you found.
- Each sub-agent explores independently; the value is separate perspectives, not one long search.
- Protect the user's data and spec (rule #5): never overwrite a filled-in `DIRECTIVE.md`
  without asking.
