# _template — starter for a new app

**Don't build here.** Copy this whole folder to `apps/<your-app-name>/`, then:

1. Fill in `DIRECTIVE.md` (the spec + build manifest).
2. Implement the steps in `app/main.py` (and add UI/modules as needed).
3. List PyPI packages in `requirements.txt`.
4. Test with `python app/main.py`.
5. Rename `launch_app.bat` to match the app name (e.g. `launch_myapp.bat`)
   and adjust the `python` call inside if needed.
6. When ready to deliver: confirm the delivery form with the user (exe vs source
   — CLAUDE.md §5 stop #6), bump `version` in `DIRECTIVE.md`, write
   `README-exe.md` and/or `README-source.md` if shipping both forms (CLAUDE.md §7),
   then run:
   ```
   python tools/export_app.py <app-name> [--target exe|source]
   ```

Everything in this app stays inside this folder so it can be exported and shipped
on its own. Scratch files go in `.tmp/` (never shipped); the finished bundle lands
in `dist/`.
