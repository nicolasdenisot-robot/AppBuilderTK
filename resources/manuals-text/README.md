# manuals-text

Plain-text extractions of the OROS PDF manuals, for fast searching/reading
(the PDFs themselves live in `resources/Framework/`, which is not in the repo).

| File | Extracted from |
|------|----------------|
| `NVDrive_Reference_Manual.txt` | `Framework/NVDrive_Reference_Manual.pdf` (386 pages) |
| `OR3x_Developer_Toolkit.txt` | `Framework/OR3x_Developer_Toolkit.pdf` |

These are committed to the repo so they travel with it. If you update the SDK,
regenerate them with `pdftotext -layout <file>.pdf <file>.txt`.
