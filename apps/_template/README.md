# _template — starter for a new app

**Don't build here.** Copy this whole folder to `apps/<your-app-name>/`, then:

1. Fill in `DIRECTIVE.md` (the spec + build manifest).
2. Implement the steps in `app/main.py` (and add UI/modules as needed).
3. List PyPI packages in `requirements.txt`.
4. Test with `python app/main.py`.
5. Package with `tools/export_app.py` when ready.

Everything in this app stays inside this folder so it can be exported and shipped
on its own. Scratch files go in `.tmp/` (never shipped); the finished bundle lands
in `dist/`.
