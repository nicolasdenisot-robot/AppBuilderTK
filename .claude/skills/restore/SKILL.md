---
name: restore
description: "Roll ONE app under apps/ back to an earlier save point. Lists the saved points in plain language (from git history, or dated snapshots when there's no git), lets the user pick one, and restores it safely — saving the current version first so the rollback is itself undoable. Use when the user says '/restore', 'go back to a previous version', 'roll back', or 'undo my changes'. Takes an app name."
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

You let the user **go back to an earlier save point** of one app, safely. This is the
companion to `/checkpoint`: that one *creates* save points, this one *returns* to one.

Who you're helping (CLAUDE.md §1): a sound-&-vibration engineer who is **not a
programmer**. Speak plain language; do the git and file work silently. **Never destroy
their current state** (rule #5) — you always save the current version *before* rolling
back, so going back is itself reversible.

## Input

The app name after `/restore`, e.g. `/restore my-pass-fail-test` → `apps/<app-name>/`.

- **No name given:** if it's obvious which app is in play, use it and say which.
  Otherwise list the folders under `apps/` (skip `_template`) and ask (AskUserQuestion).
- If `apps/<app-name>/` does not exist, say so plainly and stop.

## Steps

**1 — Find the save points.** Check whether the workspace uses git
(`git rev-parse --is-inside-work-tree`).
- **Git:** read recent save points from history —
  `git log --pretty="%h%x09%cd%x09%s" --date=format:"%Y-%m-%d %H:%M" -- apps/<app-name>`
  — and keep the entries whose subject starts `checkpoint(<app-name>)` or
  `restore(<app-name>)`. The text after that prefix is the plain-language label. (If
  there are no labelled checkpoints but the app does have history, offer the most recent
  few commits touching it as save points instead.)
- **No git:** list the folders under `apps/<app-name>/.tmp/checkpoints/`, newest first,
  and read each folder's `label.txt` for its "what worked here" line (fall back to the
  folder's timestamp if the label is missing).
- **None found:** tell the user there are no save points yet for this app, and stop.

**2 — Show the list and let them choose.** Newest first, numbered, plain language:
```
Save points for "<app-name>" — newest first:
  1.  <date time>  — <label>
  2.  <date time>  — <label>
  ...
```
If there are 2–4, offer them with AskUserQuestion. If there are more, show the numbered
list and ask them to reply with the number. **Confirm their pick before changing anything.**

**3 — Save the current version FIRST** (the safety net — rule #5). Run the `/checkpoint`
procedure for this app with the label `before rolling back to <chosen date>`, so the
state you are about to leave is itself recoverable. Do this before touching any file.

**4 — Restore the chosen point's code — keep the documentation.** Bring back the *code*;
do **not** discard knowledge:
- **Git:** `git checkout <hash> -- apps/<app-name>/app` (also
  `apps/<app-name>/requirements.txt` if it differs at that point). Remove any files that
  were added *after* that point so the code matches exactly (safe — you saved them in
  step 3). Then commit: `restore(<app-name>): back to <date> — <label>`.
- **No git:** replace the live `apps/<app-name>/app/` with the chosen snapshot's `app/`
  so it matches exactly (safe — the current one was saved in step 3).
- **Keep the live `DIRECTIVE.md`** — do **not** overwrite it with the old copy. Rolling
  back code must not erase hard-won knowledge: the §9 "Lessons learned" stays. Then
  update §10 "Build state": add a dated **"Rolled back code to <save point> (<label>)"**
  note and re-tick the milestones to match the code you just restored.

**5 — Tell the user plainly:**
- "Done — '<app-name>' is back to the <date> save point (<label>)."
- "Your previous version was saved first, so we can return to it anytime — just run
  `/restore` again and it'll be at the top of the list."
- Suggest they run/test the app to confirm it's the version they wanted.

## Guidelines

- Plain language; define any technical word in one short sentence.
- **Never** use destructive git (`reset --hard`, force, history rewrites). Restore by
  bringing the old files back as a *new* change, so the full history stays intact.
- **Step 3 always comes before step 4** — the current state is saved before anything is
  overwritten. This is the rule that makes "go back" risk-free.
- **Code rolls back; documentation carries forward.** Keep §9 "Lessons learned"; update
  §10 "Build state" so a fresh session isn't confused about where things stand.
