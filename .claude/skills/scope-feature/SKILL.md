---
name: scope-feature
description: "Scope a change or improvement to ONE existing NVGate app under apps/. Maps what you'd need to build, what already exists to reuse, dependencies and unknowns, and where the difficulty is — then runs a short improvement interview. Use when the user says '/scope-feature', 'scope a change', or 'what would it take to add X' to an existing app. Assumes /explore-codebase has run. Takes an app name and the change."
allowed-tools:
  - Read
  - Write
  - Glob
  - Grep
  - Bash
  - AskUserQuestion
disable-model-invocation: true
---

You scope a **change to an existing app** — what it would take to build, what's already
there to reuse, what's risky. This is the middle stop in the "improve an existing app"
workflow (`/explore-codebase` → `/scope-feature` → `/frontend-design`).

Remember who you are helping (CLAUDE.md §1): a sound-&-vibration engineer who is **not a
programmer**. Write everything back in **plain language, no jargon**. Do the technical
analysis silently and report the conclusions.

## Input

- The **app name** and the **change** the user wants — everything after `/scope-feature`,
  e.g. `/scope-feature my-pass-fail-test add a second microphone channel`. Rough notes are
  fine; work with whatever you get.
- If no app name is given, list the folders under `apps/` (skip `_template`) and ask which
  one (AskUserQuestion).

## Context

This skill assumes `/explore-codebase <app>` has already run, so the app's
**`DIRECTIVE.md`** describes what it does and is built from. Read that first. If it is
empty or missing, tell the user plainly and suggest running `/explore-codebase <app>`
first. Then read only the specific files under `apps/<app>/app/` you need to answer the
questions below — do not re-scan the whole app.

## Process

**Step 1 — Read context.** Read `apps/<app>/DIRECTIVE.md` and the few `app/` files relevant
to the change.

**Step 2 — Parse the change.** Extract what the user wants, even if rough.

**Step 3 — Build the scoping note:**

```markdown
## Scoping note: {change} — YYYY-MM-DD

### What you'd need to build
{The pieces that change — which app/ modules, new steps, new NVGate settings/IDNs to
read or set, new exports. For each, one plain sentence on what it does and why it's needed.}

### What already exists to reuse
{Existing app code, shared/oros_helpers/ modules, docs/recipes/ patterns, and NVGate-native
features this change should build on instead of writing from scratch (rule #6). Name them.}

### Dependencies & unknowns
{Things that depend on other things. Anything that needs checking against NVGate or the
analyzer before committing — e.g. whether NVGate computes it natively, whether a setting
takes effect as expected, hardware/channel availability.}

### Where the difficulty is
{Which parts are straightforward and which are hard, and WHY — in plain language. Ground it
in the actual code and in what NVGate can/can't do, not general guesses.}
```

**Step 4 — Run the short improvement interview** (use AskUserQuestion, a few questions, to
pin down the parts that decide whether the change is "done"):
- **Boundaries:** what should this change deliberately NOT do?
- **Edge cases:** how should it behave when things go wrong — NVGate not running, no signal,
  a value out of range, the operator cancels? (These map to `DIRECTIVE.md` §8.)
- **Acceptance / pass criteria:** what must be true for you to call it working? If it's a
  pass/fail change, the exact deterministic rule (maps to `DIRECTIVE.md` §7). See
  `docs/recipes/pass-fail.md`.

Keep it short — a handful of questions, not an interrogation. This replaces the old separate
spec interview; the answers live in `DIRECTIVE.md`, the one source of truth.

**Step 5 — Save into the app's `DIRECTIVE.md`** (never the root `docs/`): append the scoping
note to the "Lessons learned" / improvement-log section, and fold the interview answers into
§7 (pass/fail) and §8 (edge cases). **Ask before changing existing sections** (rule #5).

**Step 6 — Present a short summary**, leading with what's hard and why, then what's reusable.
Suggest the next step: build it, or `/frontend-design <app>` if the change is UI work.

## Guidelines

- Plain language always. Define any unavoidable technical word in one short sentence.
- Be specific — name real files, helpers, recipes, and NVGate features.
- Do NOT estimate hours, story points, or timelines.
- Tier-1 rule (CLAUDE.md §5): if NVGate already computes it, plan to drive NVGate and fetch
  the result — don't plan to reimplement it in Python.
- Keep it concise — the user should grasp the scope and the risks in about two minutes.
