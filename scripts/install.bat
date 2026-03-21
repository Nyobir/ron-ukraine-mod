@echo off
setlocal

set "GAME_DIR=C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations"
set "MOD_DIR=%~dp0.."

echo === Ukraine Nation Mod - Installer ===
echo.
echo Game directory: %GAME_DIR%
echo Mod directory:  %MOD_DIR%
echo.

:: Check game directory exists
if not exist "%GAME_DIR%\Data\rules.xml" (
    echo ERROR: Game not found at %GAME_DIR%
    echo Please edit this script and set GAME_DIR to your Rise of Nations install path.
    pause
    exit /b 1
)

:: Check if backup already exists (don't overwrite previous backup)
if exist "%MOD_DIR%\backup\rules.xml" (
    echo Backup already exists - skipping backup step.
    echo If you want a fresh backup, delete the backup folder first.
    echo.
) else (
    echo Backing up original files...
    mkdir "%MOD_DIR%\backup\tribes" 2>nul
    copy "%GAME_DIR%\Data\rules.xml" "%MOD_DIR%\backup\rules.xml"
    copy "%GAME_DIR%\Data\unitrules.xml" "%MOD_DIR%\backup\unitrules.xml"
    copy "%GAME_DIR%\Data\help.xml" "%MOD_DIR%\backup\help.xml"
    copy "%GAME_DIR%\tribes\russians.xml" "%MOD_DIR%\backup\tribes\russians.xml"
    echo Backup complete.
    echo.
)

echo Installing Ukraine mod...
copy /Y "%MOD_DIR%\data\rules.xml" "%GAME_DIR%\Data\rules.xml"
copy /Y "%MOD_DIR%\data\unitrules.xml" "%GAME_DIR%\Data\unitrules.xml"
copy /Y "%MOD_DIR%\data\help.xml" "%GAME_DIR%\Data\help.xml"
copy /Y "%MOD_DIR%\tribes\russians.xml" "%GAME_DIR%\tribes\russians.xml"

echo.
echo === Installation complete! ===
echo Ukraine replaces Russia in the nation selection screen.
echo.
pause
