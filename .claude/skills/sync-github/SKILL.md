---
name: sync-github
description: "Sync your workspace to a private GitHub repository. Use when the user says '/sync-github', 'sync to github', 'push to github', 'back up my workspace', or 'save to github'."
allowed-tools:
  - Bash
  - Read
  - Write
  - AskUserQuestion
disable-model-invocation: true
---

You are a utility that backs up the user's workspace to a private GitHub repository. Walk through each step, confirming as you go.

## Steps

### 1. Check Prerequisites

This workspace runs on **Windows**. Run `gh --version` (or `which gh` in the Bash
tool / `Get-Command gh` in PowerShell) to check if the GitHub CLI is installed.

If not installed, tell the user to install it with one of:
```
winget install --id GitHub.cli        # recommended on Windows
choco install gh                      # if they use Chocolatey
```
Then authenticate:
```
gh auth login
```
Walk them through the browser login if needed. Don't proceed until `gh` is available and authenticated.

### 2. Check Git Status

Run `git rev-parse --is-inside-work-tree` to check if the workspace is already a git repo.

**If it's not a git repo:**
- Run `git init` to initialize one
- Tell the user you're setting up version control for the first time

### 3. Ensure .gitignore Exists

Check if `.gitignore` exists at the workspace root. If not, create one with sensible defaults:

```
.DS_Store
Thumbs.db
__pycache__/
*.py[cod]
.env
.venv/
**/.tmp/
**/dist/
**/build/
```

If a `.gitignore` already exists, read it and check if it covers the basics. Suggest additions if it's missing obvious entries (like .DS_Store or __pycache__), but don't modify it without asking.

### 4. Stage and Commit

Run `git status` to see what's changed.

If there are changes to commit:
- Run `git add -A` to stage everything
- Look at what changed and write a descriptive commit message based on the actual modifications (not just "sync" — something like "Add Q2 planning project and update CLAUDE.md preferences" or "Initial OS setup with CLAUDE.md and project structure")
- Run `git commit -m "your descriptive message"`

If there are no changes, tell the user everything is already up to date.

### 5. Check Remote

Run `git remote -v` to check if a remote exists.

**If no remote exists:**
- Ask the user what they want to name the repo (suggest their workspace folder name as default)
- Create a private repo: `gh repo create REPO_NAME --private --source=. --remote=origin`
- Confirm the repo was created

**If a remote exists:**
- Confirm it's pointing to the right place

### 6. Push

Detect the current branch automatically, then push it (do not hard-code `main` —
this workspace's branch may be `master`):

```
git push -u origin "$(git branch --show-current)"
```
In PowerShell: `git push -u origin (git branch --show-current)`.

If that fails because the branch doesn't exist on remote yet, `git push -u origin HEAD` also works.

### 7. Confirm

Tell the user:
- Their workspace is backed up to GitHub
- Show them the repo URL (run `gh repo view --web` or construct it from the remote URL)
- Remind them they can run `/sync-github` any time to save their latest changes
- Mention that `git log --oneline -5` shows their recent save points if they ever need to go back
