@echo off
REM ── THD Calculator (UI) launcher ─────────────────────────────────────────
REM Double-click this file to open the THD Calculator window.
REM NVGate must be open and in connected mode.

cd /d "%~dp0"
python app\main.py

if errorlevel 1 (
    echo.
    echo The application closed with an error. See above for details.
    pause
)
