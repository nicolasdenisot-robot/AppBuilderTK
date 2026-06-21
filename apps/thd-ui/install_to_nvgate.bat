@echo off
REM ── THD Calculator UI — NVGate integration installer ─────────────────────
REM Run this script ONCE after copying the app to this PC.
REM It registers "THD Calculator UI" in NVGate's Automation / Links menu.
REM
REM Nothing is installed system-wide. To uninstall, delete the file it creates:
REM   C:\OROS\NVGate data\Links\THD Calculator UI.bat

set "APP_BAT=%~dp0launch_thd_ui.bat"
set "LINKS_DIR=C:\OROS\NVGate data\Links"
set "LINK_FILE=%LINKS_DIR%\THD Calculator UI.bat"

echo.
echo Installing: THD Calculator UI
echo   App launcher : %APP_BAT%
echo   NVGate Links : %LINK_FILE%
echo.

REM Check the app launcher is present
if not exist "%APP_BAT%" (
    echo ERROR: launch_thd_ui.bat not found at:
    echo   %APP_BAT%
    echo Make sure you are running install_to_nvgate.bat from the same folder
    echo as launch_thd_ui.bat.
    echo.
    pause
    exit /b 1
)

REM Check the NVGate Links folder exists
if not exist "%LINKS_DIR%\" (
    echo ERROR: NVGate Links folder not found at:
    echo   %LINKS_DIR%
    echo Please check that NVGate is installed and that folder exists.
    echo.
    pause
    exit /b 1
)

REM Write the one-line launcher into the Links folder
(
    echo @echo off
    echo call "%APP_BAT%"
) > "%LINK_FILE%"

if errorlevel 1 (
    echo ERROR: Could not write to the Links folder.
    echo Try running this script as Administrator.
    echo.
    pause
    exit /b 1
)

echo Done.
echo.
echo "THD Calculator UI" now appears in NVGate under Automation / Execute.
echo You can run it at any time without re-running this installer.
echo.
pause
