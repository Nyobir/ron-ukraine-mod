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
    copy "%GAME_DIR%\Data\typenames.xml" "%MOD_DIR%\backup\typenames.xml"
    mkdir "%MOD_DIR%\backup\art" 2>nul
    copy "%GAME_DIR%\art\RedGuard.tga" "%MOD_DIR%\backup\art\RedGuard.tga"
    copy "%GAME_DIR%\art\Rusiny.tga" "%MOD_DIR%\backup\art\Rusiny.tga"
    copy "%GAME_DIR%\art\Cossack.tga" "%MOD_DIR%\backup\art\Cossack.tga"
    copy "%GAME_DIR%\art\Don_cossack.tga" "%MOD_DIR%\backup\art\Don_cossack.tga"
    copy "%GAME_DIR%\art\T80_green.tga" "%MOD_DIR%\backup\art\T80_green.tga"
    copy "%GAME_DIR%\art\katyusha.tga" "%MOD_DIR%\backup\art\katyusha.tga"
    echo Backup complete.
    echo.
)

echo Installing Ukraine mod...
echo  - Data files...
copy /Y "%MOD_DIR%\data\rules.xml" "%GAME_DIR%\Data\rules.xml"
copy /Y "%MOD_DIR%\data\unitrules.xml" "%GAME_DIR%\Data\unitrules.xml"
copy /Y "%MOD_DIR%\data\help.xml" "%GAME_DIR%\Data\help.xml"
copy /Y "%MOD_DIR%\tribes\russians.xml" "%GAME_DIR%\tribes\russians.xml"
copy /Y "%MOD_DIR%\data\typenames.xml" "%GAME_DIR%\Data\typenames.xml"
echo  - Unit textures...
copy /Y "%MOD_DIR%\art\RedGuard.tga" "%GAME_DIR%\art\RedGuard.tga"
copy /Y "%MOD_DIR%\art\Rusiny.tga" "%GAME_DIR%\art\Rusiny.tga"
copy /Y "%MOD_DIR%\art\Cossack.tga" "%GAME_DIR%\art\Cossack.tga"
copy /Y "%MOD_DIR%\art\Don_cossack.tga" "%GAME_DIR%\art\Don_cossack.tga"
copy /Y "%MOD_DIR%\art\T80_green.tga" "%GAME_DIR%\art\T80_green.tga"
copy /Y "%MOD_DIR%\art\katyusha.tga" "%GAME_DIR%\art\katyusha.tga"

echo.
echo === Installation complete! ===
echo Ukraine replaces Russia in the nation selection screen.
echo.
pause
