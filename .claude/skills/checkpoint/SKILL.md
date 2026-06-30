---
name: checkpoint
description: "Save the build progress of ONE app under apps/ so a brand-new session can resume it exactly. Updates the app's DIRECTIVE.md 'Build state' (and 'Lessons learned'), then commits the working code as a recoverable checkpoint. Use when the user says '/checkpoint', 'checkpoint now', 'save my progress', or before context runs low on a multi-session build. Takes an app name."
allowed-tools:
  - Read
  - Edit
  - Write
  - Glob
  - Grep
  - Bash
  - AskUserQuestion
disable-model-invocation: true
---

You save the **build progress of one app** so a brand-new session can pick up exactly
where this one stopped — without losing the details that matter (setting/result IDNs,
the precise pass/fail numbers, the quirk you just found). This is the **manual half**
of the checkpoint discipline (CLAUDE.md rule #10); the **automatic half** is the
checkpoint you make on your own when about **30% of context remains**. Both do the
same thing — the steps below.

Who you're helping (CLAUDE.md §1): a sound-&-vibration engineer who is **not a
programmer**. Speak plain language. You do the file and git work silently.

## Input

The app name — everything after `/checkpoint`, e.g. `/checkpoint my-pass-fail-test`,
mapping to `apps/<app-name>/`.

- **No name given:** if it's obvious which app this session is building, use that and
  say which one. Otherwise list the folders under `apps/` (skip `_template`) and ask
  which one (AskUserQuestion).
- If `apps/<app-name>/` does not exist, say so plainly and stop.

## Steps

**1 — Update `DIRECTIVE.md` §10 "Build state".** (Edit only the living sections — never
rewrite the §1–§8 spec; rule #5.)
- Tick every milestone that is now built **and tested**. Leave half-done ones unticked.
- Rewrite the **"Last session left off"** line with: today's date · what is done and
  tested · what is half-built right now · the **single next concrete step**. Be specific
  enough that a fresh session needs nothing else — name the file and function to touch
  next, the IDN to use, the value to set.
- If §10 doesn't exist yet (an older app), add it from `apps/_template/DIRECTIVE.md`.

**2 — Capture discoveries in §9 "Lessons learned".** Add anything learned this session
that isn't already recorded: setting/result IDNs, a quirk ("setting X only applies after
Run"), timing, the fix for an error you hit. **These are exactly what auto-summary
loses** — write them down so the next session doesn't rediscover them.

**3 — Save a recoverable copy of the code.** The written Build state above is what lets
a fresh session resume; this step adds an **undo safety net** so a slice that breaks
something can be rolled back. First check whether the workspace uses git:
`git rev-parse --is-inside-work-tree` (quiet failure = no git).

**If it's a git repo** (the sturdiest option): commit to the **current branch**; do
**not** push (backup is the separate, user-initiated `/sync-github` step).
- Stage the app: `git add apps/<app-name>` (includes its updated `DIRECTIVE.md`).
- Commit with a clear subject: `checkpoint(<app-name>): <one line on what works now>`.

**If there's no git:**
- **Offer git once** (at most once per session): explain in one plain sentence that it
  lets them roll back a change that breaks something, and that `/sync-github` sets it up
  in a single step. If they say yes, set it up and commit as above.
- **If they decline (or "not now"):** fall back to a **dated snapshot of the code only** —
  copy `app/` and `DIRECTIVE.md` (never `reference/`, `dist/`, or `.tmp/`) into
  `apps/<app-name>/.tmp/checkpoints/<YYYY-MM-DD_HHMM>/`, and write a one-line `label.txt`
  in that folder (the same `<what works now>` summary) so **`/restore`** can show a
  friendly list instead of bare timestamps. That's just source files (kilobytes), and
  `.tmp/` is never shipped. **Keep only the 5 most recent** snapshots and delete older
  ones. Don't re-ask about git for the rest of the session.

Either way: if the code currently has an error that stops it running, save it anyway as
a clearly labelled work-in-progress checkpoint, and note in §10 that it's mid-fix and
how far the fix got — a recoverable broken state beats a lost one.

**4 — Tell the user plainly** (keep it short):
- "Progress saved." One line on what's done and what the next step is.
- **How to resume:** open a new session and say *"continue building `<app-name>`"* — you
  will read its Build state and pick up exactly there. (Starting fresh keeps full
  quality; that's the point of checkpointing instead of letting context fill.)
- If **you** triggered this at the ~30% mark (not the user), add: recommend starting a
  fresh session now, because quality drops as the remaining context shrinks.

## Guidelines

- Plain language; define any technical word in one short sentence.
- Protect the spec (rule #5): edit only §9 and §10 of `DIRECTIVE.md`; don't touch the
  §1–§8 spec without asking.
- A checkpoint must be **recoverable** = tested (or clearly-labelled WIP) code **plus** a
  written "where we left off." If either is missing, fix that before you call it done.
- Don't push and don't export here — those are `/sync-github` and `tools/export_app.py`.
  A checkpoint is a local save point, nothing more.
