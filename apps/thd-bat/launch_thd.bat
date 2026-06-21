@echo off
REM ── THD Calculator launcher ──────────────────────────────────────────────
REM Double-click this file to run the THD calculation.
REM NVGate must be open and in connected mode before you start.

cd /d "%~dp0"
python app\main.py

echo.
if errorlevel 1 (
    echo Something went wrong. Read the message above for details.
) else (
    echo THD calculation complete.
)
echo.
pause
