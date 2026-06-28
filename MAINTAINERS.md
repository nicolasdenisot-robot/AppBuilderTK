# MAINTAINERS — for OROS, not for customers

> This file is **not** shipped to customers (it's excluded from the publish
> allowlist in `tools/publish_template.py`). It explains how distribution works.

## Two repos, two jobs

| Repo | Purpose | Visibility |
|------|---------|-----------|
| **`claude-nvgate-app`** (this folder's `origin`) | **Your private workspace.** You build & test real apps in `apps/`, and back everything up with `/sync-github`. | Private (only you) |
| **`oros-nvgate-app-builder`** | **The clean template customers receive.** Only the kit + `apps/_template`. No personal apps, no personal info. Marked as a GitHub *Template repository*. | Private (flip to Public anytime in repo Settings) |

Your real/experimental apps live only in your workspace repo. They are **never**
published, because the publish step copies an explicit **allowlist** (see
`INCLUDE` in `tools/publish_template.py`), not "everything minus some things".

## Updating what customers get

After you improve the kit (CLAUDE.md, helpers, docs, recipes…), first run
**`/audit-workspace`** — it checks the whole kit for inconsistencies and errors
(and verifies the helpers/docs against the real SDK) before customers ever see it.
Then publish:

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
gh repo create my-oros-apps --private --template chaorandu-ai/oros-nvgate-app-builder --clone
```

Then first-time setup: add the Framework SDK (`resources/README.md`), confirm
Python. Their apps and their `/sync-github` backups stay entirely in their repo.

> For a private template, the customer's GitHub account needs access (add them as
> a collaborator, or create the repo for them). Switch the template to **Public**
> (repo Settings → Danger Zone → Change visibility) and anyone can self-serve —
> but then the kit and the OROS manual text become world-visible.

## Testing it with a colleague (collaborator invite)

Have a colleague play "customer" end-to-end. Their account only gets read access
to the **template** — they never see your workspace (`claude-nvgate-app`).

**You (owner) — invite them to the template repo (read access):**
```
gh api -X PUT repos/chaorandu-ai/oros-nvgate-app-builder/collaborators/COLLEAGUE \
  --field permission=pull
```
(Or on GitHub: template repo → Settings → Collaborators → Add people →
their username → role **Read** → invite.) They get an email/GitHub invite to accept.

**Colleague (the "customer"):**
1. Accept the invite.
2. Install + log in to GitHub CLI: `winget install --id GitHub.cli`, then `gh auth login`.
3. Create their own private repo from the template and clone it:
   ```
   gh repo create my-oros-apps --private \
     --template chaorandu-ai/oros-nvgate-app-builder --clone
   ```
4. Open the folder in VS Code / Claude Code.
5. Add the Framework SDK (`resources/README.md`), confirm Python.
6. Build a tiny test app, then run `/sync-github` to back up to *their* repo.

**What success looks like:**
- Their `my-oros-apps` repo contains the template content (kit + `apps/_template`).
- Their test app and backups live only in *their* repo.
- They cannot see `claude-nvgate-app` or any of your apps.

To revoke access afterward:
```
gh api -X DELETE repos/chaorandu-ai/oros-nvgate-app-builder/collaborators/COLLEAGUE
```

## Moving the template to an OROS org later

You can transfer `oros-nvgate-app-builder` to an OROS GitHub organization (repo
Settings → Transfer), then publish with `--repo OROS/oros-nvgate-app-builder`.
