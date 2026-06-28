@echo off
REM Accelerometer Calibration - double-click launcher (source delivery).
cd /d "%~dp0"
python app\main.py
if errorlevel 1 (
    echo.
    echo The application closed with an error. See above for details.
    pause
)
