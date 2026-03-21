# Ukraine Nation Mod — Rise of Nations: Extended Edition

## Overview

Add Ukraine as a playable nation in Rise of Nations: Extended Edition by replacing Russia's nation slot. The mod retunes Russia's power entries, replaces its unique units, and updates all player-facing text to reflect Ukrainian identity.

**Scope:** MVP — functional gameplay with existing art assets. Visual polish deferred to a future pass.

**Distribution:** Manual install (batch scripts) and Steam Workshop compatible.

**Target Version:** Rise of Nations: Extended Edition (Steam, latest patch as of March 2026)

---

## Nation Identity

- **Nation Name:** Ukraine
- **Power Name:** Power of the Breadbasket
- **Replaced Nation:** Russia
- **Art Set:** European units (UNIT_CONTINENT 0), Northern European buildings (BUILD_CONTINENT 1)

### Leaders

- Bohdan Khmelnytsky
- Ivan Mazepa
- Taras Shevchenko

### Cities

Kyiv, Lviv, Odesa, Kharkiv, Dnipro, Zaporizhzhia, Chernihiv, Poltava, Vinnytsia, Mykolaiv, Sumy, Ternopil, Lutsk, Uzhhorod, Ivano-Frankivsk, Kramatorsk, Mariupol, Kherson, Rivne, Zhytomyr

---

## Nation Powers

Theme: Agricultural wealth, territorial defense, and Cossack military tradition.

All powers reuse Russia's `RUSSIAN_` entries in `rules.xml`. The variable names stay the same; only the values and help text change.

| Power Slot | Value | Player-Facing Effect |
|---|---|---|
| `RUSSIAN_ATTRITION` | 100% | +100% attrition damage to enemies in your territory |
| `RUSSIAN_ATTRITION_UPGRADES` | 1 | Attrition upgrades researched instantly and free |
| `RUSSIAN_OIL` | 25% | +25% Oil gather rate (engine hardcodes this to Oil — kept as-is; reframed as energy independence) |
| `RUSSIAN_BORDERS` | 0 | (base border bonus; 0 is intentional — scaling comes from PER_AGE below) |
| `RUSSIAN_BORDERS_PER_AGE` | 1 | National borders expand +1 per Civic Research |
| `RUSSIAN_COMMUNISM` | 0 | (unused) |
| `RUSSIAN_SPY_COST` | 25% | Spies cost 25% less |
| `RUSSIAN_COSSACK_DAMAGE` | 33% | Cavalry does +33% damage vs Supply Wagons and Artillery |
| `RUSSIAN_PLUNDER_STEAL` | 1 | Plunder from your buildings goes to you, not the enemy (1 = enabled; redirects 100% of plunder income — verify exact engine behavior during testing) |
| `RUSSIAN_FREE_CIVIC` | 1 | Free Civic Research at each new age |

### Player-Facing Description (help.xml)

> Power of the Breadbasket — Heirs to the Cossack tradition and the fertile steppe, Ukrainians excel at defending their homeland and feeding their people. Enemies suffer greatly in Ukrainian territory, while the nation's agricultural wealth fuels rapid growth.

---

## Unique Units

Three unique units spanning Gunpowder, Enlightenment, and Modern ages. Each replaces one of Russia's existing unique unit slots in `unitrules.xml`.

**Important:** All stat deltas below are relative to the replaced unit. Absolute values must be calculated from the original game files during implementation (Step 4). The developer must read the base stats of Rusiny Lancer, Don Cossack, and Red Guard from the game's `unitrules.xml` before applying percentage changes.

### Sich Cossack (Gunpowder Age)

- **Replaces:** Rusiny Lancer slot (cavalry class retained — this unit is cavalry, not infantry)
- **Role:** Tough, cost-efficient light cavalry
- **Stats vs replaced unit:**
  - +10% hit points
  - -5% Timber cost
  - Same move speed (cavalry)
- **Unique flag:** Y
- **Flavor:** Zaporozhian Sich horsemen — the mounted warriors of the Cossack fortress-camps.
- **Note:** Age changed from Medieval to Gunpowder to match the historical Sich period (15th-16th century). Unit class stays cavalry to match the Lancer slot's engine constraints.

### Cossack Hetman (Enlightenment Age)

- **Replaces:** Don Cossack (Hussar) slot
- **Role:** Raiding cavalry, anti-supply/artillery specialist
- **Stats vs replaced unit:**
  - +15% damage vs Supply Wagons and Artillery
  - +5% move speed
  - Same cost as Hussar
- **Unique flag:** Y
- **Synergy:** Expected to stack with `RUSSIAN_COSSACK_DAMAGE` (+33%). Stacking behavior (additive vs multiplicative) must be verified in-game during testing.
- **Flavor:** Hetman cavalry — the elite mounted commanders of the Ukrainian Cossack host.

### Drone Operator (Modern Age)

- **Replaces:** Red Guard (Infantry) slot
- **Role:** Anti-armor specialist, glass cannon
- **Stats vs replaced unit:**
  - +30% damage vs vehicles/tanks
  - +5% base damage vs all other units
  - -15% hit points
  - Same cost as standard infantry
- **Unique flag:** Y
- **Flavor:** A specialist trained in operating strike drones against armored targets. Fragile in direct combat but devastating against enemy vehicles.

### TRIBE_MASK

All three units have their `TRIBE_MASK` set so only Ukraine (Russia's slot position) can build them. All other nation bits set to 0.

---

## File Structure

```
C:\Projectsd\ron-ukraine-mod\
├── data/
│   ├── rules.xml            # RUSSIAN_ power values retuned for Ukraine
│   ├── unitrules.xml        # 3 unique unit slots modified
│   ├── help.xml             # All player-facing text replaced
│   └── unit_graphics.xml    # Only if graphic entry changes needed (may be unchanged for MVP)
├── tribes/
│   └── russians.xml         # Ukraine nation definition (filename kept for engine compat)
├── backup/
│   ├── rules.xml
│   ├── unitrules.xml
│   ├── help.xml
│   ├── unit_graphics.xml
│   └── tribes/
│       └── russians.xml
├── scripts/
│   ├── install.bat          # Backs up originals, copies mod files into game dir
│   └── uninstall.bat        # Restores original files from backup
└── README.txt               # Manual installation instructions
```

**Key constraint:** The tribe file must remain named `russians.xml` because the game engine hardcodes filename-to-slot mapping. Only the contents change.

---

## Implementation Steps

### Step 1 — Setup
- Locate RoN install directory (typically `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\`)
- Copy original game files into `backup/`

### Step 2 — Nation Definition
- Edit `tribes/russians.xml`: replace leaders, cities, and nation name with Ukraine's values

### Step 3 — Nation Powers
- Edit `rules.xml`: set the 10 `RUSSIAN_` entries to Ukraine's values per the power table above

### Step 4 — Unique Units
- Edit `unitrules.xml`: modify the 3 Russian unique unit slots with new stats
- Update `TRIBE_MASK` for each unit
- Set unique flag `Y` on all three

### Step 5 — Text & Descriptions
- Edit `help.xml`: replace all Russian nation text, power descriptions, and unit flavor text

### Step 6 — Install/Uninstall Scripts
- Write `install.bat` and `uninstall.bat` for file swapping

### Step 7 — Test
- Launch game, verify Ukraine appears in nation select
- Play skirmish: verify powers activate, unique units buildable at correct ages
- Test uninstall script restores Russia correctly

---

## Future Polish (Post-MVP)

- Custom nation icon (Ukrainian tryzub)
- Custom unit sprites/models for all 3 unique units
- Custom unit voice lines
- Loading screen text and historical flavor
- Balance tuning across all ages
- Steam Workshop listing with description and screenshots

---

## Constraints & Risks

- **Hardcoded nation count:** Cannot add a new nation slot; must replace an existing one.
- **Hardcoded power names:** `RUSSIAN_` prefixes remain in the XML; only values and help text change.
- **Hardcoded unit count:** Cannot add new unit slots; must repurpose existing Russian unique unit slots.
- **Multiplayer sync:** All players must use the same mod files or the session will desync.
- **Art assets:** MVP uses existing European art. Units will visually look like standard European units until custom art is created.
- **`RUSSIAN_OIL` hardcoded:** This variable likely controls Oil gather rate specifically, not a generic resource. We keep it as Oil (+25%) and reframe the flavor as energy independence rather than agriculture. Verify during testing.
- **Unit slot class constraints:** Unit slots may be class-locked (cavalry/infantry). The Sich Cossack retains cavalry class to match the Rusiny Lancer slot. If class can be changed, this opens future design options.

---

## Verification Checklist (Step 7)

- [ ] Ukraine appears in nation selection screen (in Russia's slot)
- [ ] Nation name displays as "Ukraine" in-game
- [ ] All 10 power effects activate correctly
- [ ] `RUSSIAN_OIL` confirmed to affect Oil gather rate
- [ ] `RUSSIAN_PLUNDER_STEAL` behaves as expected when enemy razes buildings
- [ ] Sich Cossack buildable at Gunpowder Age, unique flag shown
- [ ] Cossack Hetman buildable at Enlightenment Age, unique flag shown
- [ ] Cossack Hetman + COSSACK_DAMAGE stacking behavior documented
- [ ] Drone Operator buildable at Modern Age, unique flag shown
- [ ] Drone Operator deals bonus damage vs vehicles/tanks
- [ ] No other nation can build Ukraine's unique units (TRIBE_MASK correct)
- [ ] City names cycle correctly through all 20 entries
- [ ] Leader names display correctly
- [ ] Uninstall script restores original Russia successfully
- [ ] Game does not crash on load, skirmish start, or age advancement
