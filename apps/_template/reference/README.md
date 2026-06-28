# reference/ — source documents that inform the build (never shipped)

Put here any document you receive or write that helps **build** the app but that
the app itself never opens when it runs:

- the initial spec or requirements (Word, PDF, email)
- an example of the desired output (a sample report, a filled-in Excel)
- screenshots, notes, customer correspondence

**These are never packaged for the operator.** The export tool only ships the
`app/` folder plus a few named files, so anything in `reference/` stays in your
workspace (and in git — so future sessions and `/explore-codebase` /
`/scope-feature` can read it).

Distil the actual requirements from these into `DIRECTIVE.md`, so the spec is
self-contained and you don't have to re-read a PDF every time.

> A document the app **does** open at runtime — an Excel template it fills, a
> report template, a config file, an image — does **not** go here. Put those as
> top-level files in `app/`, where the export tool bundles them automatically.
> See CLAUDE.md §6.
