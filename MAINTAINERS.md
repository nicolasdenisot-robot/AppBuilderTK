# MAINTAINERS — for OROS, not for customers

> This file is **not** shipped to customers (it's excluded from the publish
> allowlist in `tools/publish_template.py`). It explains how distribution works.

## Two repos, two jobs

| Repo | Purpose | Visibility |
|------|---------|-----------|
| **`oros-nvgate-app-builder`** (this folder's `origin`) | **Your private workspace.** You build & test real apps in `apps/`, and back everything up with `/sync-github`. | Private (only you) |
| **`oros-nvgate-template`** | **The clean template customers receive.** Only the kit + `apps/_template`. No personal apps, no personal info. Marked as a GitHub *Template repository*. | Private (flip to Public anytime in repo Settings) |

Your real/experimental apps live only in your workspace repo. They are **never**
published, because the publish step copies an explicit **allowlist** (see
`INCLUDE` in `tools/publish_template.py`), not "everything minus some things".

## Updating what customers get

After you improve the kit (CLAUDE.md, helpers, docs, recipes…):

```
python tools/publish_template.py            # publish to the template repo
python tools/publish_template.py --dry-run  # preview the clean copy first
python tools/publish_template.py --repo OWNER/NAME   # different template repo
```

It clones the template repo, replaces its contents with the allowlisted kit,
commits, and pushes. Run it whenever you want customers' template to catch up.

## How a customer onboards

They never clone your repo. They create their **own** private repo from the
template (Claude can do this for them on first run):

```
gh repo create my-oros-apps --private --template chaorandu-ai/oros-nvgate-template --clone
```

Then first-time setup: add the Framework SDK (`resources/README.md`), confirm
Python. Their apps and their `/sync-github` backups stay entirely in their repo.

> For a private template, the customer's GitHub account needs access (add them as
> a collaborator, or create the repo for them). Switch the template to **Public**
> (repo Settings → Danger Zone → Change visibility) and anyone can self-serve —
> but then the kit and the OROS manual text become world-visible.

## Moving the template to an OROS org later

You can transfer `oros-nvgate-template` to an OROS GitHub organization (repo
Settings → Transfer), then publish with `--repo OROS/oros-nvgate-template`.
