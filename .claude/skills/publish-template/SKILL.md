---
name: publish-template
description: "Publish the clean customer template: push the kit from this workspace to the oros-nvgate-app-builder template repo. Use when the user says '/publish-template', 'publish the template', 'update the template repo', or 'push the kit to customers'."
allowed-tools:
  - Bash
  - Read
disable-model-invocation: true
---

You publish the **clean customer template** from this private workspace to the
separate template repo. This is maintainer-only and is **not** `/sync-github`
(that backs up the workspace). Keep the two separate. Walk through each step,
confirming before anything is pushed.

## Steps

### 1. Preflight

- Confirm `tools/publish_template.py` exists in the workspace. If not, stop and
  tell the user this command must be run from the maintainer workspace
  (`claude-nvgate-app`), not a customer copy.
- Optional: run `git remote -v` and note the target template repo (the script's
  `DEFAULT_REPO`, currently `chaorandu-ai/oros-nvgate-app-builder`).

### 2. Preview (always)

Run:
```
python tools/publish_template.py --dry-run
```
Show the user the list of items that would be published. Remind them this copies
an **allowlist** of kit files only — their `apps/`, personal files, `.env`, and
`.tmp/` are never included.

### 3. Confirm

Ask the user to confirm they want to push these to the customer template repo.
This is outward-facing (customers will receive it), so do not proceed without a
clear yes. If they want a custom commit message, accept one.

### 4. Publish

Run (add `--message "..."` if they gave one):
```
python tools/publish_template.py
```

### 5. Report

Tell the user:
- The template repo was updated (name it), and summarize what changed.
- Their workspace backup is **separate** — if they also want to save their own
  work, run `/sync-github`.
- Customers get the update next time they pull, or new customers via the template.

### Notes
- Publishing uses the files **as they are on disk**, committed or not.
- This does **not** commit or back up the workspace. That is `/sync-github`'s job.
