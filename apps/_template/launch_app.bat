@echo off
REM Rename this file to launch_<app-name>.bat when cloning the template.
REM Adjust the python call below if the entry point changes.
cd /d "%~dp0"
python app\main.py
if errorlevel 1 (
    echo.
    echo The application closed with an error. See above for details.
    pause
)
