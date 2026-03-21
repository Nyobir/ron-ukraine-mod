# Ukraine Nation Mod — Visual Polish Plan

This document details every visual and audio element needed to make the Ukraine mod feel like it shipped with the game. The MVP is functional but uses placeholder art from existing European/Russian assets. This plan covers what needs to be created, the technical specs for each asset, and where each file goes.

---

## 1. Nation Icon / Flag

**What:** The icon shown in the nation selection screen, diplomacy panel, and minimap markers.

**Asset needed:**
- Ukrainian Tryzub (trident coat of arms) or blue-and-yellow flag
- Format: TGA or BMP (check existing nation icons in `art/` folder for exact format)
- Sizes needed:
  - Large icon (nation select screen): ~128x128 px
  - Small icon (minimap/diplomacy): ~32x32 px
  - Medium icon (in-game UI): ~64x64 px

**Where it goes:**
- Check `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\art\` for existing nation icon paths
- The icon file path is likely referenced in the tribe XML or a UI configuration file

**Design notes:**
- Use the golden tryzub on a blue background for clear visual contrast
- Must be readable at 32x32 — keep the tryzub simple, not ornate
- Study existing nation icons (British lion, French fleur-de-lis) for style reference

---

## 2. Unique Unit Models / Sprites

Each unique unit currently reuses existing European 3D models. For full polish, each needs its own model or at minimum a texture reskin.

### 2a. Sich Cossack (Medieval Age — Light Cavalry)

**Currently uses:** `RUSINYLANCER` model (Russian Lancer appearance)

**Target look:** Zaporozhian horseman with characteristic oseledets (Cossack topknot hairstyle), fur-trimmed coat, saber, light shield

**Assets needed:**
- 3D model (.BH3 format — RoN's proprietary model format) OR texture reskin of existing Lancer model
- Texture file: TGA format, power-of-2 dimensions (e.g., 256x256 or 512x512)
- Animation: Can reuse existing Light Cavalry animation set

**Minimum viable reskin:**
- Recolor the existing Lancer texture: change tabard/clothing colors to blue and yellow
- Add Cossack-style hat (papakha) via texture painting

### 2b. Sich Warrior (Gunpowder Age — Light Cavalry)

**Currently uses:** `COSSACK` model

**Target look:** More armored Cossack horseman, characteristic Cossack hat, armed with saber and pistol

**Assets needed:** Same format as above. This is the Gunpowder evolution, so the design should show progression — heavier gear, firearms visible.

**Minimum viable reskin:**
- Recolor existing Cossack texture to Ukrainian blue/yellow accents
- The existing Cossack model is already fairly appropriate — least effort needed here

### 2c. Cossack Hetman (Enlightenment Age — Light Cavalry)

**Currently uses:** `DONCOSSACK` model

**Target look:** Elite Cossack commander — ornate coat (zhupan), bulava (ceremonial mace), plumed hat

**Assets needed:** Same format as above. Should look visibly more commanding than the Sich Warrior.

**Minimum viable reskin:**
- Recolor Don Cossack texture, add gold/ornate details via texture painting

### 2d. Drone Operator (Modern Age — Infantry)

**Currently uses:** `REDGUARD` model (Soviet-style infantry)

**Target look:** Modern Ukrainian soldier in pixelated camouflage, carrying a drone controller or small FPV drone

**Assets needed:**
- This is the most visually distinct unit — a Soviet-looking infantry is the worst mismatch
- New 3D model preferred, or heavy texture reskin
- Modern military camouflage pattern (Ukrainian pixel camo)
- Drone element visible (even if just a textured backpack/controller)

**Minimum viable reskin:**
- Recolor Red Guard texture to green/tan modern camo pattern
- Remove any Soviet-era visual elements via texture edit

### 2e. Oplot Tank (Information Age — Heavy Tank)

**Currently uses:** `RUSSHEAVYTANK` model (T-80 appearance)

**Target look:** Ukrainian Oplot main battle tank — distinct turret shape, ERA (explosive reactive armor) blocks

**Assets needed:**
- Texture reskin: Ukrainian camo pattern, Ukrainian military markings
- The T-80 and Oplot share similar chassis, so a texture swap is reasonable

**Minimum viable reskin:**
- Recolor to Ukrainian military green/tan camo
- Add Ukrainian cross or tryzub marking on turret

### 2f. Vilkha Rocket (Modern Age — Artillery)

**Currently uses:** `KATYUSHA` model

**Target look:** Modern MLRS system — Vilkha launcher on truck chassis

**Assets needed:**
- Texture reskin to modern Ukrainian military colors
- The Katyusha model is a truck-mounted rocket launcher, which is visually similar enough

**Minimum viable reskin:**
- Modern camo paint scheme
- Remove any Soviet-era markings

---

## 3. Unit Voice Lines / Sound Effects

**What:** Audio that plays when units are selected, given orders, or engage in combat.

**Currently:** Uses default European voice lines (English-accented)

**Target:** Ukrainian-language voice lines

### Needed recordings per unit type:

Each unit type needs these voice clips (WAV format, 22050 Hz, mono):
- **Select** (3-4 variants): "Tak?" / "Slukhayu" / "Hovoryt" (Yes? / Listening / Speak)
- **Move order** (3-4 variants): "Rozumiy" / "Vykonuyu" / "V dorohu" (Understood / Executing / On the way)
- **Attack order** (3-4 variants): "V ataku!" / "Za Ukrainu!" / "Vohnʹ!" (Attack! / For Ukraine! / Fire!)
- **Death/defeated** (2-3 variants): pain/death sounds

### Sound file locations:
- Check `C:\Program Files (x86)\Steam\steamapps\common\Rise of Nations\sounds\` for existing voice line structure
- Referenced in `Data\soundtypes.xml` — each unit type has mapped sound events

### Priority order:
1. Generic infantry voice set (covers Drone Operator, Shock Infantry)
2. Cavalry voice set (covers Sich Cossack, Sich Warrior, Cossack Hetman)
3. Vehicle voice set (covers Oplot Tank, Vilkha Rocket)

---

## 4. Loading Screen / Nation Description

**What:** Text and imagery shown when loading a game as Ukraine.

**Assets needed:**
- Loading screen tip text mentioning Ukraine's strengths (already partially done in help.xml)
- Historical description paragraph for the nation info screen
- Loading screen background image (if the game supports per-nation loading screens — verify)

**Text draft for nation info:**
> "Ukraine, the breadbasket of Europe, has a proud history of fierce independence and Cossack military tradition. From the Zaporozhian Sich to the modern era, Ukrainians have defended their homeland with tenacity and ingenuity. The fertile black soil of the steppe fuels a powerful economy, while the Cossack heritage produces elite cavalry and resilient warriors."

---

## 5. Wonder / Unique Building (Optional)

**What:** If the game supports nation-specific wonders, assign one to Ukraine.

**Candidates:**
- Saint Sophia Cathedral (Kyiv) — already exists as a wonder in the game's generic pool
- Khortytsia Fortress — Zaporozhian Sich fortress

**Investigation needed:** Check if wonders are assignable per-nation in the game files, or if they're always random/universal.

---

## 6. Map Territory Color

**What:** The color that represents Ukraine on the map and in UI elements.

**Target:** Blue and yellow (Ukrainian national colors)
- Primary: Blue (#005BBB)
- Secondary: Yellow (#FFD500)

**Where:** Check `Data\alternatecolors.xml` or nation-specific color assignments in the game files.

---

## 7. Tools and Workflow

### For texture/model work:
- **Texture editing:** Photoshop, GIMP, or Paint.NET (TGA export support needed)
- **3D model viewing/editing:** Need to research RoN BH3 model format — community tools may exist
- **Reference models:** Extract existing unit textures from game files to use as templates

### For audio:
- **Recording:** Any microphone + Audacity for editing
- **Format:** WAV, 22050 Hz, 16-bit, mono
- **Alternative:** AI voice generation for Ukrainian voice lines (check quality)

### For icons:
- **Tool:** Any image editor with TGA export
- **Size reference:** Extract existing nation icons to determine exact pixel dimensions

---

## 8. Priority Order for Visual Work

| Priority | Element | Effort | Impact |
|---|---|---|---|
| 1 | Nation icon (tryzub) | Low | High — most visible identity element |
| 2 | Drone Operator reskin | Medium | High — worst visual mismatch (Soviet → Modern Ukrainian) |
| 3 | Map territory color | Low | Medium — blue/yellow immediately recognizable |
| 4 | Oplot Tank reskin | Medium | Medium — T-80 looks too Russian |
| 5 | Sich Cossack/Warrior/Hetman reskins | Medium | Low-Medium — existing Cossack models are acceptable |
| 6 | Vilkha Rocket reskin | Low | Low — Katyusha looks generic enough |
| 7 | Voice lines | High | High — but most effort; defer to last |
| 8 | Loading screen text | Low | Low — nice-to-have |
| 9 | Wonder assignment | Low | Low — if even possible |

---

## 9. File Format Investigation Needed

Before starting visual work, these technical questions must be answered:

- [ ] What exact image format and dimensions are used for nation icons? (Extract an existing one)
- [ ] Can RoN BH3 models be opened/edited with any community tools?
- [ ] What is the texture file naming convention? (e.g., does `RUSINYLANCER` model look for `rusinylancer.tga`?)
- [ ] How are unit sound events mapped in `soundtypes.xml`? Extract an existing mapping as reference.
- [ ] Are nation colors defined in `alternatecolors.xml` or elsewhere?
- [ ] Can wonders be assigned per-nation?

Each of these should be investigated by extracting and examining existing game files before any art production begins.
