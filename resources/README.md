# resources/

| Folder | What it is | In git? |
|--------|-----------|---------|
| `Framework/` | The official OROS SDK (pynvdrive, NVFileManager, DLLs, PDFs) | **No** — you add it (see below) |
| `manuals-text/` | Plain-text mirror of the OROS PDF manuals, for fast reading/search | Yes |

## Adding the Framework SDK (one-time)

The SDK is not shipped in this repo. Add it once:

1. Download the **Framework** zip from
   <https://my.oros.com/categories/software/nvgate/>.
2. Unzip it — you'll get a folder named **`Framework`**.
3. Copy that whole `Framework` folder into **this `resources/` folder**, so the
   path becomes **`resources/Framework/`**.

You should then see `resources/Framework/Python/pynvdrive/` and the PDF manuals.
The apps and helpers expect the SDK at exactly that path.
