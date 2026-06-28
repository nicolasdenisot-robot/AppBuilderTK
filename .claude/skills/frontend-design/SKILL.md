---
name: frontend-design
description: "Design or improve the user-facing screen of an NVGate app, built with the project's Python desktop stacks — PySide6/Qt, Streamlit, or Tkinter. Produces clean, legible, branded screens (using the shared/assets/logos convention) suited to either an engineer or a one-click line operator. Use when the user wants to build or refine an app's UI. Takes an app name."
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
disable-model-invocation: true
---

You design or improve the **screen an operator or engineer actually sees** for an NVGate
app. This workspace builds **Python desktop apps**, not websites — so you work in the
project's three UI stacks, never HTML/React/Vue.

Remember who the screen is for (CLAUDE.md §1, §5 stop #5): often a **line operator who
just clicks an icon**, or the **non-programmer engineer** themselves. The first goal is
**clarity and confidence** — a screen someone can use correctly under factory conditions
without a manual. Make it look considered and branded, but never at the cost of legibility.

## Input

- The **app name** — `apps/<app-name>/`. If none is given, list the folders under `apps/`
  (skip `_template`) and ask which one (AskUserQuestion).
- Read the app's `DIRECTIVE.md` first: it records the chosen **UI stack** (§2), who runs it,
  where results appear, and the **`logo:` brand**. Build for that stack. If no stack is
  chosen yet, propose one (see the table) with plain pros/cons and let the user pick.

## Choosing the stack (only if not already decided)

| Stack | Best for | Trade-off |
|-------|----------|-----------|
| **PySide6 / Qt** | Operator apps that ship as a double-click `.exe` | Most capable; a bit more code |
| **Streamlit** | A quick dashboard the engineer opens in a browser | Needs a browser/Python running; less "appliance"-like |
| **Tkinter** | The simplest built-in window, nothing extra to install | Dated look; limited styling |

## Design thinking (before coding)

- **Who uses it, and where?** A line operator at a station needs big targets, an
  unmistakable pass/fail verdict, and few choices. An engineer at a desk can handle more
  density and options.
- **What's the one thing they must not miss?** Usually the result/verdict or the current
  state (running / done / error). Make that the loudest element on screen.
- **Tone, within reason.** A clean, calm, branded look beats a generic gray default — but
  this is industrial test equipment, so favor **legible, restrained, high-contrast** over
  decorative. A green/red verdict must read across a noisy shop floor at a glance.

## Branding (the logo convention — CLAUDE.md §10)

Use the shared logo, don't invent one. Set `logo:` in `DIRECTIVE.md` (e.g. `logo: oros`)
and load it with the standard `_logo_path()` helper so it works both in development and in a
packaged `.exe`. Use `logo_color.png` on light screens (default) and `logo_white.png` on dark
ones. Full pattern and the copy-paste `_logo_path()` function:
`shared/assets/logos/README.md`. Add a customer brand by creating
`shared/assets/logos/<customer>/` with both files.

## Per-stack guidance

- **PySide6 / Qt:** lay out with `QVBoxLayout`/`QGridLayout`; style with a Qt Style Sheet
  (`setStyleSheet`) using a small, consistent set of colors and one or two font sizes. Big,
  obvious primary button; a clear status line; a verdict area that fills with color. Keep it
  resizable and readable at the station's screen size.
- **Streamlit:** use `st.set_page_config`, columns, `st.metric` for headline numbers, and
  `st.success`/`st.error` for verdicts; theme via `.streamlit/config.toml`. Keep it to one
  clear column of flow — don't bury the result below the fold.
- **Tkinter:** use `ttk` widgets and a `ttk.Style`; pick one accent color and one neutral.
  Accept its limits — aim for clean and legible rather than flashy.

Across all three: a small, consistent palette and spacing; one display weight for the
headline and one for body; generous whitespace around the thing that matters most.

## Build & verify

- Implement real, working code in the app's `app/` folder. Keep all logic deterministic and
  out of the UI where possible — the UI shows state and triggers steps; the tested code
  decides (CLAUDE.md §3).
- Reuse anything relevant from `shared/oros_helpers/` and existing apps before writing new
  widgets.
- Run it and confirm it launches and renders before handing back. If the change is part of a
  delivery, note the UI stack and any quirks in `DIRECTIVE.md`.

## Never

- Never produce HTML/CSS/JS or a web framework (React/Vue) for a desktop app — wrong toolchain.
- Never sacrifice the legibility of the result/verdict for decoration.
- Never hard-code a logo into the app folder; use the shared logo convention.
