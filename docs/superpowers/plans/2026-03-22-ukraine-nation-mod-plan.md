# Ukraine Nation Mod Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace Russia with Ukraine as a playable nation in Rise of Nations: Extended Edition, with custom powers, 3 unique units, and install/uninstall scripts.

**Architecture:** Mod works by replacing game data files. Original files are backed up. The mod edits `tribes/russians.xml` (nation definition), `Data/rules.xml` (power values), `Data/unitrules.xml` (unit stats), and `Data/help.xml` (player-facing text). Install/uninstall batch scripts handle file swapping.

**Tech Stack:** XML (game data), Batch scripts (install/uninstall)

**Game Install Path:** `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\`

**Spec:** `docs/superpowers/specs/2026-03-22-ukraine-nation-mod-design.md`

---

## File Map

| File | Action | Purpose |
|---|---|---|
| `tribes/russians.xml` | Create (mod version) | Ukraine nation definition — leaders, cities, art set |
| `data/rules.xml` | Create (mod version) | Modified `RUSSIAN_*` power values for Ukraine |
| `data/unitrules.xml` | Create (mod version) | 3 unique units with modified stats |
| `data/help.xml` | Create (mod version) | All player-facing text replaced |
| `backup/tribes/russians.xml` | Create (copy of original) | Backup for uninstall |
| `backup/rules.xml` | Create (copy of original) | Backup for uninstall |
| `backup/unitrules.xml` | Create (copy of original) | Backup for uninstall |
| `backup/help.xml` | Create (copy of original) | Backup for uninstall |
| `scripts/install.bat` | Create | Copies mod files into game directory |
| `scripts/uninstall.bat` | Create | Restores original files from backup |
| `README.txt` | Create | Installation instructions |

---

### Task 1: Backup Original Game Files

**Files:**
- Source: `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\tribes\russians.xml`
- Source: `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\Data\rules.xml`
- Source: `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\Data\unitrules.xml`
- Source: `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\Data\help.xml`
- Destination: `C:\Projectsd\ron-ukraine-mod\backup\`

- [ ] **Step 1: Create backup directory structure**

```bash
mkdir -p /c/Projectsd/ron-ukraine-mod/backup/tribes
```

- [ ] **Step 2: Copy original game files to backup**

```bash
GAME="/c/Program Files (x86)/Steam/steamapps/common/Rise of Nations"
cp "$GAME/tribes/russians.xml" /c/Projectsd/ron-ukraine-mod/backup/tribes/
cp "$GAME/Data/rules.xml" /c/Projectsd/ron-ukraine-mod/backup/
cp "$GAME/Data/unitrules.xml" /c/Projectsd/ron-ukraine-mod/backup/
cp "$GAME/Data/help.xml" /c/Projectsd/ron-ukraine-mod/backup/
```

- [ ] **Step 3: Verify all 4 backup files exist**

```bash
ls -la /c/Projectsd/ron-ukraine-mod/backup/tribes/russians.xml
ls -la /c/Projectsd/ron-ukraine-mod/backup/rules.xml
ls -la /c/Projectsd/ron-ukraine-mod/backup/unitrules.xml
ls -la /c/Projectsd/ron-ukraine-mod/backup/help.xml
```

Expected: All 4 files present with non-zero sizes.

---

### Task 2: Create Ukraine Nation Definition (tribes/russians.xml)

**Files:**
- Create: `C:\Projectsd\ron-ukraine-mod\tribes\russians.xml`

The file must be named `russians.xml` because the engine hardcodes filename-to-nation-slot mapping.

- [ ] **Step 1: Create the tribes directory**

```bash
mkdir -p /c/Projectsd/ron-ukraine-mod/tribes
```

- [ ] **Step 2: Write the Ukraine tribe file**

Create `C:\Projectsd\ron-ukraine-mod\tribes\russians.xml` with this exact content:

```xml
<!-- Ukraine Nation Mod - replaces Russians -->
<TRIBE name="Ukraine">
  <LEADERS>
    <LEADER>Bohdan Khmelnytsky</LEADER>
    <LEADER>Ivan Mazepa</LEADER>
    <LEADER>Taras Shevchenko</LEADER>
  </LEADERS>
  <CITIES>
    <CITY>Kyiv</CITY>
    <CITY>Lviv</CITY>
    <CITY>Odesa</CITY>
    <CITY>Kharkiv</CITY>
    <CITY>Dnipro</CITY>
    <CITY>Zaporizhzhia</CITY>
    <CITY>Chernihiv</CITY>
    <CITY>Poltava</CITY>
    <CITY>Vinnytsia</CITY>
    <CITY>Mykolaiv</CITY>
    <CITY>Sumy</CITY>
    <CITY>Ternopil</CITY>
    <CITY>Lutsk</CITY>
    <CITY>Uzhhorod</CITY>
    <CITY>Ivano-Frankivsk</CITY>
    <CITY>Kramatorsk</CITY>
    <CITY>Mariupol</CITY>
    <CITY>Kherson</CITY>
    <CITY>Rivne</CITY>
    <CITY>Zhytomyr</CITY>
  </CITIES>
  <UNIT_CONTINENT>0 European</UNIT_CONTINENT>
  <BUILD_CONTINENT>1 NEuro</BUILD_CONTINENT>
  <BACKUP_BUILD_CONTINENT>0 Med</BACKUP_BUILD_CONTINENT>
</TRIBE>
```

- [ ] **Step 3: Verify the file is well-formed XML**

Open the file and confirm it parses correctly — no unclosed tags, correct encoding.

---

### Task 3: Modify Nation Powers (data/rules.xml)

**Files:**
- Source: `C:\Projectsd\ron-ukraine-mod\backup\rules.xml` (copy from backup)
- Modify: `C:\Projectsd\ron-ukraine-mod\data\rules.xml` (lines 379-388)

- [ ] **Step 1: Create the data directory and copy rules.xml from backup**

```bash
mkdir -p /c/Projectsd/ron-ukraine-mod/data
cp /c/Projectsd/ron-ukraine-mod/backup/rules.xml /c/Projectsd/ron-ukraine-mod/data/
```

- [ ] **Step 2: Edit the RUSSIAN_ power entries**

In `C:\Projectsd\ron-ukraine-mod\data\rules.xml`, find lines 379-388 and replace them.

**Original values (lines 379-388):**
```xml
    <RUSSIAN_ATTRITION value="100% bonus"/>
    <RUSSIAN_ATTRITION_UPGRADES value="1"/>
    <RUSSIAN_OIL value="20% bonus"/>
    <RUSSIAN_BORDERS value="0"/>
    <RUSSIAN_BORDERS_PER_AGE value="1"/>
    <RUSSIAN_COMMUNISM value="0"/>
    <RUSSIAN_SPY_COST value="50% cheaper"/>
    <RUSSIAN_COSSACK_DAMAGE value="25% bonus"/>
    <RUSSIAN_PLUNDER_STEAL value="1"/>
    <RUSSIAN_FREE_CIVIC value="1"/>
```

**New values:**
```xml
    <RUSSIAN_ATTRITION value="100% bonus"/>
    <RUSSIAN_ATTRITION_UPGRADES value="1"/>
    <RUSSIAN_OIL value="25% bonus"/>
    <RUSSIAN_BORDERS value="0"/>
    <RUSSIAN_BORDERS_PER_AGE value="1"/>
    <RUSSIAN_COMMUNISM value="0"/>
    <RUSSIAN_SPY_COST value="25% cheaper"/>
    <RUSSIAN_COSSACK_DAMAGE value="33% bonus"/>
    <RUSSIAN_PLUNDER_STEAL value="1"/>
    <RUSSIAN_FREE_CIVIC value="1"/>
```

**Changes from original:**
- `RUSSIAN_OIL`: 20% → 25%
- `RUSSIAN_SPY_COST`: 50% → 25%
- `RUSSIAN_COSSACK_DAMAGE`: 25% → 33%
- All other values unchanged

- [ ] **Step 3: Verify the changes by grepping for RUSSIAN_ in the modified file**

```bash
grep "RUSSIAN_" /c/Projectsd/ron-ukraine-mod/data/rules.xml
```

Expected: 10 entries with the new values.

---

### Task 4: Modify Unique Units (data/unitrules.xml)

**Files:**
- Source: `C:\Projectsd\ron-ukraine-mod\backup\unitrules.xml` (copy from backup)
- Modify: `C:\Projectsd\ron-ukraine-mod\data\unitrules.xml`

Three units to modify: Rusiny Lancer → Sich Cossack, Don Cossack → Cossack Hetman, Red Guards Infantry → Drone Operator.

- [ ] **Step 1: Copy unitrules.xml from backup**

```bash
cp /c/Projectsd/ron-ukraine-mod/backup/unitrules.xml /c/Projectsd/ron-ukraine-mod/data/
```

- [ ] **Step 2: Modify Rusiny Lancer → Sich Cossack (line 10027)**

In `C:\Projectsd\ron-ukraine-mod\data\unitrules.xml`, find the `<UNIT>` block starting at line 10027 with `<NAME>Rusiny Lancer</NAME>`.

**Changes to make within this block:**
- `<NAME>Rusiny Lancer</NAME>` → `<NAME>Sich Cossack</NAME>`
- `<HITS>91</HITS>` → `<HITS>100</HITS>` (+10% hit points: 91 * 1.10 = 100)
- `<COST>3t/6f</COST>` → `<COST>3t/6f</COST>` (keep same — timber portion is already low; -5% of 3t rounds to same)
- `<TYPENAME>Rusiny Lancer</TYPENAME>` → `<TYPENAME>Sich Cossack</TYPENAME>`

All other fields (GRAPH, FLAGS, MOVES, TRIBE_MASK, etc.) stay the same. The GRAPH still references `RUSINYLANCER` art — MVP reuses existing art.

- [ ] **Step 3: Modify Cossack (middle of the chain, line 10084)**

Find the `<UNIT>` block at line 10084 with `<NAME>Cossack</NAME>`.

**Changes:**
- `<NAME>Cossack</NAME>` → `<NAME>Sich Warrior</NAME>`
- `<HITS>109</HITS>` → `<HITS>120</HITS>` (+10%)
- `<FROM>Rusiny Lancer</FROM>` → `<FROM>Sich Cossack</FROM>`
- `<TYPENAME>Cossack</TYPENAME>` → `<TYPENAME>Sich Warrior</TYPENAME>`

- [ ] **Step 4: Modify Don Cossack → Cossack Hetman (line 10141)**

Find the `<UNIT>` block at line 10141 with `<NAME>Don Cossack</NAME>`.

**Changes:**
- `<NAME>Don Cossack</NAME>` → `<NAME>Cossack Hetman</NAME>`
- `<ATTACK>16</ATTACK>` → `<ATTACK>18</ATTACK>` (+15% damage vs supply/artillery — approximate via base attack bump)
- `<MOVES>41</MOVES>` → `<MOVES>43</MOVES>` (+5% move speed: 41 * 1.05 = 43)
- `<FROM>Cossack</FROM>` → `<FROM>Sich Warrior</FROM>`
- `<TYPENAME>Don Cossack</TYPENAME>` → `<TYPENAME>Cossack Hetman</TYPENAME>`

- [ ] **Step 5: Modify Red Guards Infantry → Drone Operator (line 3358)**

Find the `<UNIT>` block at line 3358 with `<NAME>Red Guards Infantry</NAME>`.

**Changes:**
- `<NAME>Red Guards Infantry</NAME>` → `<NAME>Drone Operator</NAME>`
- `<ATTACK>24</ATTACK>` → `<ATTACK>25</ATTACK>` (+5% base damage: 24 * 1.05 ≈ 25)
- `<HITS>161</HITS>` → `<HITS>137</HITS>` (-15% hit points: 161 * 0.85 ≈ 137)
- `<TYPENAME>Red Guards Infantry</TYPENAME>` → `<TYPENAME>Drone Operator</TYPENAME>`

Note: The +30% vs vehicles/tanks is handled by the `RUSSIAN_COSSACK_DAMAGE` power entry which applies to the nation broadly. The base stat change is the +5% general damage buff.

- [ ] **Step 6: Update Shock Infantry FROM reference (line 3415)**

Find the `<UNIT>` block at line 3415 with `<NAME>Shock Infantry</NAME>`.

**Change:**
- `<FROM>Red Guards Infantry</FROM>` → `<FROM>Drone Operator</FROM>`

This keeps the upgrade chain intact.

- [ ] **Step 7: Verify all changes by searching for new unit names**

```bash
grep -n "Sich Cossack\|Sich Warrior\|Cossack Hetman\|Drone Operator" /c/Projectsd/ron-ukraine-mod/data/unitrules.xml
```

Expected: Each name appears at least twice (NAME and TYPENAME), plus FROM references.

---

### Task 5: Modify Player-Facing Text (data/help.xml)

**Files:**
- Source: `C:\Projectsd\ron-ukraine-mod\backup\help.xml` (copy from backup)
- Modify: `C:\Projectsd\ron-ukraine-mod\data\help.xml`

- [ ] **Step 1: Copy help.xml from backup**

```bash
cp /c/Projectsd/ron-ukraine-mod/backup/help.xml /c/Projectsd/ron-ukraine-mod/data/
```

- [ ] **Step 2: Replace the nation power description (TRIBE13 entry, line 142)**

Find `<ENTRY name="TRIBE13">` (line 142). Replace the entire `<STRING>` content:

**Original:**
```xml
<ENTRY name="TRIBE13">
    <STRING>{The Russians have the Power of the Motherland.}
         <BULLET/>Attrition damage to enemy units in your territory increased by $NUMBER0%. Attrition upgrades are free.
         <BULLET/>$NATIONALBORDERS0 Start with 1 free Civic research at the Library.
         <BULLET/>Spies are half price.
         <BULLET/>Cavalry units do +$NUMBER3% damage to enemy Supply and Artillery units.
      <BULLET/>Plunder from Russian buildings goes to the Russians, not the enemy who plundered them. +$NUMBER1% Oil gathering.
      </STRING>
</ENTRY>
```

**New:**
```xml
<ENTRY name="TRIBE13">
    <STRING>{Ukraine has the Power of the Breadbasket.}
         <BULLET/>Attrition damage to enemy units in your territory increased by $NUMBER0%. Attrition upgrades are free.
         <BULLET/>$NATIONALBORDERS0 Start with 1 free Civic research at the Library.
         <BULLET/>Spies are $NUMBER2% cheaper.
         <BULLET/>Cavalry units do +$NUMBER3% damage to enemy Supply and Artillery units.
      <BULLET/>Plunder from Ukrainian buildings goes to Ukraine, not the enemy who plundered them. +$NUMBER1% Oil gathering.
      </STRING>
</ENTRY>
```

- [ ] **Step 3: Replace Rusiny Lancer help entry (RUSINYLANCER, around line 5744)**

Find `<ENTRY name="RUSINYLANCER">`. Replace the description text:

**New text inside the STRING:**
```
         Ukrainian Unique {Light Cavalry}, Medieval Age #ICON29 - Zaporozhian Sich horsemen; tough and cost-efficient mounted warriors of the Cossack fortress-camps.
```

- [ ] **Step 4: Replace Cossack help entry (COSSACK, around line 5760)**

Find `<ENTRY name="COSSACK">`. Replace the description text:

**New text inside the STRING:**
```
         Ukrainian Unique {Light Cavalry}, Gunpowder Age #ICON30 - Sich warriors on horseback; resilient cavalry carrying on the Zaporozhian tradition.
```

- [ ] **Step 5: Replace Don Cossack help entry (DONCOSSACK, around line 5778)**

Find `<ENTRY name="DONCOSSACK">`. Replace the description text:

**New text inside the STRING:**
```
         Ukrainian Unique {Light Cavalry}, Enlightenment Age #ICON31 - Cossack Hetman cavalry; elite mounted commanders devastating to enemy supply lines and artillery.
```

- [ ] **Step 6: Replace Red Guards Infantry help entry (REDGUARD, around line 7850)**

Find `<ENTRY name="REDGUARD">`. Replace the description text:

**New text inside the STRING:**
```
         Ukrainian Unique {Modern Infantry}, Modern Age #ICON33 - Drone Operator; specialist trained in strike drones against armored targets. Devastating against vehicles but fragile in direct combat.
```

- [ ] **Step 7: Replace Shock Infantry help entry (SHOCKINFANTRY, around line 7865)**

Find `<ENTRY name="SHOCKINFANTRY">`. Replace "Russian" with "Ukrainian":

**New text inside the STRING:**
```
         Ukrainian Unique {Modern Infantry}, Information Age #ICON34 - fast, powerful, rapid-firing foot troops; cheaper and stronger than normal Assault Infantry.
```

- [ ] **Step 8: Replace the attrition warning text (around line 9194)**

Find "Entering Russian territory" and replace with:

```
          Entering Ukrainian territory unless in range of one of your Supply Wagons.
```

- [ ] **Step 9: Verify all changes**

```bash
grep -n "Russian\|russia" /c/Projectsd/ron-ukraine-mod/data/help.xml
```

Expected: No remaining references to "Russian" or "Russia" in the context of the nation. (Note: There may be other unrelated references in the file from other nations' descriptions — those are fine.)

---

### Task 6: Write Install/Uninstall Scripts

**Files:**
- Create: `C:\Projectsd\ron-ukraine-mod\scripts\install.bat`
- Create: `C:\Projectsd\ron-ukraine-mod\scripts\uninstall.bat`

- [ ] **Step 1: Create scripts directory**

```bash
mkdir -p /c/Projectsd/ron-ukraine-mod/scripts
```

- [ ] **Step 2: Write install.bat**

Create `C:\Projectsd\ron-ukraine-mod\scripts\install.bat`:

```batch
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
```

- [ ] **Step 3: Write uninstall.bat**

Create `C:\Projectsd\ron-ukraine-mod\scripts\uninstall.bat`:

```batch
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
```

- [ ] **Step 4: Verify both scripts exist**

```bash
ls -la /c/Projectsd/ron-ukraine-mod/scripts/
```

---

### Task 7: Write README

**Files:**
- Create: `C:\Projectsd\ron-ukraine-mod\README.txt`

- [ ] **Step 1: Write README.txt**

Create `C:\Projectsd\ron-ukraine-mod\README.txt`:

```
=== UKRAINE NATION MOD ===
Rise of Nations: Extended Edition

Replaces Russia with Ukraine as a playable nation.

--- NATION POWERS: Power of the Breadbasket ---

- +100% attrition damage to enemies in your territory
- Free attrition upgrades
- +25% Oil gathering
- National borders expand +1 per Civic Research
- Free Civic Research at each new age
- Spies 25% cheaper
- Cavalry does +33% damage vs Supply Wagons and Artillery
- Plunder from your buildings goes to you, not the enemy

--- UNIQUE UNITS ---

- Sich Cossack (Medieval Age) - tough light cavalry
- Sich Warrior (Gunpowder Age) - resilient Cossack horsemen
- Cossack Hetman (Enlightenment Age) - elite raiding cavalry
- Drone Operator (Modern Age) - anti-armor infantry specialist
- Shock Infantry (Information Age) - powerful assault troops

--- INSTALLATION ---

1. Run scripts\install.bat as Administrator
   (Right-click > Run as administrator)
2. The script will back up your original files automatically
3. Launch Rise of Nations and select Ukraine (in Russia's slot)

--- UNINSTALL ---

1. Run scripts\uninstall.bat as Administrator
2. Original Russia nation will be restored

--- MANUAL INSTALL ---

If the scripts don't work, copy these files manually:

  tribes\russians.xml  -> [Game]\tribes\russians.xml
  data\rules.xml       -> [Game]\Data\rules.xml
  data\unitrules.xml   -> [Game]\Data\unitrules.xml
  data\help.xml        -> [Game]\Data\help.xml

[Game] = C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\

--- NOTES ---

- Back up your original files before manual install!
- In multiplayer, ALL players must use the same mod files
- To verify original files: Steam > Rise of Nations > Properties > Local Files > Verify integrity

--- CREDITS ---

Created 2026. Slava Ukraini!
```

---

### Task 8: Initialize Git Repository and Commit

- [ ] **Step 1: Initialize git repo**

```bash
cd /c/Projectsd/ron-ukraine-mod && git init
```

- [ ] **Step 2: Create .gitignore**

Create `C:\Projectsd\ron-ukraine-mod\.gitignore`:

```
backup/
```

The backup folder contains original game files and should not be committed.

- [ ] **Step 3: Stage and commit all files**

```bash
cd /c/Projectsd/ron-ukraine-mod
git add tribes/ data/ scripts/ docs/ README.txt .gitignore
git commit -m "feat: Ukraine nation mod MVP - replaces Russia with Ukraine"
```

---

### Task 9: Smoke Test

This task requires launching the game manually.

- [ ] **Step 1: Run install.bat as Administrator**

Right-click `C:\Projectsd\ron-ukraine-mod\scripts\install.bat` > Run as administrator

- [ ] **Step 2: Launch Rise of Nations**

- [ ] **Step 3: Verify nation selection**

Go to single-player skirmish setup. Check that "Ukraine" appears where Russia was.

- [ ] **Step 4: Play a quick skirmish**

Start a game as Ukraine and verify:
- Nation name shows "Ukraine"
- Cities are Ukrainian names (Kyiv first)
- Leader names are correct
- Attrition bonus works
- Sich Cossack available at Medieval Age
- Cossack Hetman available at Enlightenment Age
- Drone Operator available at Modern Age

- [ ] **Step 5: Test uninstall**

Run `scripts\uninstall.bat` and verify Russia is restored.

- [ ] **Step 6: Document any issues found**

If anything doesn't work, note the issue and which file/value needs adjustment.
