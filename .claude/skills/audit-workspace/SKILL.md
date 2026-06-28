---
name: audit-workspace
description: "Thoroughly audit this workspace/kit for inconsistencies, errors, and improvements before delivering it to customers. Verifies the helpers and docs against the real OROS SDK, checks every cross-reference, and flags maintainer-only leaks. Use when the user says '/audit-workspace', 'audit the workspace', 'audit the project', 'check the kit before delivery', or 'review the whole workspace'."
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Edit
  - Write
  - AskUserQuestion
  - TodoWrite
disable-model-invocation: true
---

You perform a **thorough, end-to-end audit of this workspace** (the OROS NVGate App
Builder kit) so the maintainer can confirm it is solid before handing it to
customers. You find inconsistencies, real errors, and worthwhile improvements,
report them clearly, then fix them on approval.

This is **maintainer-only** (like `/publish-template`). It is not shipped to
customers. The person running it built this kit; write findings so they are
**precise about the problem but plain-language about the impact** — for each finding
say, in one sentence, what breaks or who gets confused if it is left as-is.

## Scope & ground rules

**Audit everything in the workspace EXCEPT:**
- **`apps/<real-app>/`** — skip every app folder under `apps/` **except `_template/`**.
  The real apps are examples/experiments, not part of the kit. Always audit
  `apps/_template/` (customers clone it).
- **Inside `resources/Framework/`** — this is the **read-only OROS SDK**. Do **not**
  flag inconsistencies in its own files, and never edit it. BUT you **must read it**
  to verify the kit is correct (see the verification principle below). Reading is
  fine; flagging/altering its contents is not.

**The verification principle (most important).** A wrong command name or signature in
a helper or recipe will make a *delivered* app fail to build or run. So do not trust
the docs or helpers from memory — **verify them against the actual SDK** under
`resources/Framework/Python/pynvdrive/pynvdrive/`:
- Every `pynvdrive` class/command a helper imports or a doc names must actually exist
  there (`grep -rn "class Name" ...`).
- Every constructor keyword and result attribute a helper uses must match the real
  `__init__` and the parsed result object.
- If a doc claims a feature exists "in pynvdrive", confirm it does — some NVDrive
  *protocol* commands (e.g. the §3.9 notification/`Register*` commands) are **not**
  wrapped as Python classes, and saying they are is an error.

## Process

**Step 1 — Plan.** Open a short `TodoWrite` list with one item per audit area (below)
so progress is visible. Inventory the tree first (`find . -type f` excluding `.git`,
`resources/Framework`, real app folders, `__pycache__`).

**Step 2 — Audit each area.** Read the files and check, concretely:

- **Root docs** — `CLAUDE.md`, `README.md`, `MAINTAINERS.md`, `docs/workspace-layout.md`:
  internal consistency; every path/file/skill they reference exists; **no
  maintainer-only leak** into customer-facing files (grep `CLAUDE.md` and `README.md`
  for `publish.template`, `MAINTAINERS`, the template repo owner/name — they must be
  clean).
- **`docs/`** (`algorithms.md`, `app-archetypes.md`, `exporting.md`, `export-forms.md`,
  `nvdrive-cheatsheet.md`, `recipes/*`): every NVDrive command/class/parameter named
  must exist in the SDK; every recipe's code must use real helper signatures; every
  `docs/...md` cross-link must resolve; the frontmatter fields the export doc lists
  must match what `tools/export_app.py` actually reads.
- **`shared/oros_helpers/`** (`connection`, `settings`, `results`, `nvgate_display`,
  `export`, `report`, `_bootstrap`, `__init__`): verify each imported command and
  every constructor kwarg / result attribute against the SDK (per the verification
  principle); confirm `__init__.py` exports match what the modules define and what the
  README documents; sanity-check the context-manager and bundle-path logic.
- **`shared/assets/logos/`**: each brand has `logo_color.png` + `logo_white.png` (the
  names the export tool and `_logo_path()` require); files are transparent PNGs at a
  sensible resolution; the README matches the files actually present.
- **`tools/`** (`export_app.py`, `publish_template.py`, `README.md`): both compile
  (`python -m py_compile`); the publish **allowlist** includes everything customers
  need AND excludes maintainer-only items (`publish_template.py` itself,
  `MAINTAINERS.md`, the `publish-template` and `audit-workspace` skills, real apps);
  staging/exclusion logic skips `__pycache__`/`.pyc`/`.tmp`/`dist`.
- **`apps/_template/`**: structure complete (`DIRECTIVE.md`, `README.md`,
  `CHANGELOG.md`, `app/main.py`, `app/__init__.py`, `launch_*.bat`, `requirements.txt`,
  `reference/`); `DIRECTIVE.md` frontmatter parses cleanly with `export_app.parse_frontmatter`;
  `app/main.py` bootstrap paths are right for dev and bundle.
- **`.claude/`**: `settings.json` is valid JSON and its `deny` rules protect the SDK
  (`Write` **and** `Edit` on `resources/Framework/**`) and the NVGate data folder;
  each skill's frontmatter is valid; the publish allowlist lists the customer-facing
  skills and omits the maintainer-only ones.
- **Cross-cutting**: `.gitignore` covers `__pycache__`/`*.pyc`/`**/.tmp/`/`**/dist/`/
  `resources/Framework/`; no `.pyc`/`__pycache__` is tracked (`git ls-files | grep`);
  no stale references to deleted files; `git status` is sane.

**Step 3 — Classify findings by severity:**
- **High** — correctness: would fail at runtime/build, or misleads a future build
  (e.g. a non-existent command name, a wrong helper signature).
- **Medium** — safety hardening or a genuinely confusing/contradictory doc.
- **Low** — polish: wording, resolution, housekeeping, optional additions.

**Step 4 — Report** (worst first) in this shape — be specific, cite `file:line`, and
give a concrete fix for each:

```markdown
## 🔴 Correctness  — N findings
1. {what is wrong} — {plain-language impact} — `path:line`. Fix: {concrete change}.

## 🟠 Medium
...

## 🟡 Low / polish
...

## ✅ Verified solid (no action)
{What you checked and found correct — e.g. "all helper signatures match the SDK",
"all doc links resolve", "no maintainer leaks" — so the maintainer trusts the audit.}
```

Lead with a one-line verdict (e.g. "Overall solid; 2 correctness items to fix before
delivery"). Optionally offer to save the report to `.tmp/audit-<YYYY-MM-DD>.md`
(gitignored).

**Step 5 — Offer to fix.** Do not auto-change anything first. Ask which to fix (the
user may say "fix all"). When fixing:
- Make surgical edits; don't rewrite files wholesale. Protect `DIRECTIVE.md`/data
  (rule #5) and never touch `resources/Framework/`.
- After edits, **re-validate**: `python -m py_compile` the tools, `json.load` the
  settings, re-grep that fixed command names now resolve.
- Then commit (this workspace works on `main` and backs up via `/sync-github`): one
  clear commit, message summarising the fixes, with the standard `Co-Authored-By`
  trailer. Report the commit and leave the tree clean.

## Guidelines

- **Verify, don't recall.** Ground every command/signature claim in a `grep` of the
  real SDK. This is the difference between a useful audit and a plausible-sounding one.
- Be specific — name real files, lines, command classes, and the exact fix.
- Plain-language impact for every finding (the maintainer is a sound-&-vibration
  engineer, not a programmer): say what breaks and for whom.
- Don't flag the contents of `resources/Framework/` or the real apps under `apps/`.
- Separate "must fix before delivery" (High) from "nice to have" (Low) so the
  maintainer can ship with confidence.
- If a fix is a real judgment call (a licence's exact wording, a brand asset only OROS
  owns), do the safe reversible thing and flag it for confirmation rather than guessing.
