# Layout — full annotated trees

Compact versions live in `CLAUDE.md` (§4 workspace, §6 per-app). These are the
fully annotated references.

## Workspace

```
Claude-NVGate/
├── CLAUDE.md                 ← the operating manual (read it fully first)
├── README.md                 ← 1-page human start
├── resources/
│   ├── Framework/            ← OROS SDK + manuals (READ-ONLY; NOT in git — added by user, see README)
│   │   ├── NVDrive_Reference_Manual.pdf  (live control, 386 pages)
│   │   ├── OR3x_Developer_Toolkit.pdf    (toolkit overview)
│   │   └── Python/pynvdrive/             (the live-control library you import)
│   └── manuals-text/        ← plain-text mirror of the PDFs (committed; read THESE,
│                              since PDFs may not render — e.g. NVDrive_Reference_Manual.txt)
├── docs/                     ← distilled guidance — READ THIS, not the 386-page PDF
│   ├── nvdrive-cheatsheet.md     top ~30 commands with examples
│   ├── algorithms.md             where to get calculations (turbomachinery, sound quality)
│   ├── app-archetypes.md         app types → which example to copy
│   ├── build-slicing.md          how to split a build into milestones + prototype the UI cheaply
│   ├── workspace-layout.md       this file
│   └── recipes/                  proven copy-adapt patterns
├── shared/
│   ├── oros_helpers/         ← reusable Python helpers (reuse these!)
│   └── assets/
│       └── logos/            ← brand logos for app UIs (brand logos live here, not in app/;
│                               app-specific runtime assets do go in app/ — see CLAUDE.md §6)
│           ├── oros/         ← OROS brand: logo_color.png (light) · logo_white.png (dark)
│           └── <customer>/   ← add a folder here for each customer brand
├── apps/                     ← the user's applications, one self-contained folder each
│   └── _template/                clone this to start a new app
└── tools/export_app.py       ← bundles an app into a standalone deliverable
```

## Per-app folder

```
apps/<app-name>/
├── DIRECTIVE.md      ← the app's spec + build manifest (the heart — has YAML frontmatter)
├── README.md         ← plain-language guide for whoever will use this app (rule #7)
├── CHANGELOG.md      ← plain-language version history; shipped as WHATS-NEW.txt (rule #9)
├── app/              ← deterministic Python (UI + logic) = the runtime; ALSO holds
│                       runtime assets the app loads (templates, images) as top-level files
├── launch_<name>.bat ← double-click launcher (source delivery); export_app.py looks for launch_*.bat
├── reference/        ← source docs that inform the build (specs, examples) — NEVER shipped
├── requirements.txt  ← PyPI packages this app needs (numpy, openpyxl, …)
├── .tmp/             ← scratch / intermediate files — gitignored, NEVER exported
└── dist/             ← generated operator package (built by tools/export_app.py)
```
