@echo off
setlocal

set "GAME_DIR=C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations"
set "MOD_DIR=%~dp0.."

echo === Ukraine Nation Mod - Uninstaller ===
echo.

:: Check backup exists
if not exist "%MOD_DIR%\backup\rules.xml" (
    echo ERROR: No backup found. Cannot restore original files.
    echo You may need to verify game files through Steam.
    pause
    exit /b 1
)

echo Restoring original files...
copy /Y "%MOD_DIR%\backup\rules.xml" "%GAME_DIR%\Data\rules.xml"
copy /Y "%MOD_DIR%\backup\unitrules.xml" "%GAME_DIR%\Data\unitrules.xml"
copy /Y "%MOD_DIR%\backup\help.xml" "%GAME_DIR%\Data\help.xml"
copy /Y "%MOD_DIR%\backup\tribes\russians.xml" "%GAME_DIR%\tribes\russians.xml"

echo.
echo === Uninstall complete! ===
echo Russia has been restored.
echo.
pause
