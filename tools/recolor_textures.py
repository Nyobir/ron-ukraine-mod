"""
Recolor Rise of Nations unit textures for Ukraine mod.

Strategy per unit:
- RedGuard (Drone Operator): Shift Soviet-brown/olive uniform to modern Ukrainian pixel camo (green/tan/brown)
- T80_green (Oplot Tank): Shift Russian green to Ukrainian olive-tan with yellow-blue accent markings
- katyusha (Vilkha Rocket): Shift to Ukrainian military olive/sand tones
- Rusiny (Sich Cossack): Add blue/yellow accent tones to Cossack outfit
- Cossack (Sich Warrior): Add blue/yellow accent tones
- Don_cossack (Cossack Hetman): Add blue/yellow accent tones, gold details
"""

from PIL import Image, ImageEnhance, ImageDraw, ImageFilter
import os
import struct

def load_tga(path):
    """Load TGA file using Pillow."""
    return Image.open(path)

def save_tga(img, path):
    """Save as TGA, matching original format."""
    img.save(path, format='TGA')

def shift_hue_region(img, hue_range, new_hue, sat_boost=1.0):
    """Shift pixels within a hue range to a new hue."""
    hsv = img.convert('HSV')
    pixels = hsv.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            h_val, s, v = pixels[x, y]
            if hue_range[0] <= h_val <= hue_range[1] and s > 20:
                pixels[x, y] = (new_hue, min(255, int(s * sat_boost)), v)
    return hsv.convert('RGB')

def add_ukraine_camo(img):
    """Apply Ukrainian digital camo pattern — modern green/tan/brown, remove Soviet red/brown tones."""
    result = img.copy()
    pixels = result.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            brightness = (r + g + b) / 3
            if brightness < 20 or brightness > 245:
                continue

            saturation = max(r, g, b) - min(r, g, b)

            # Soviet brown/olive uniform areas — shift to modern Ukrainian green camo
            if r > g and r > b and saturation > 20 and brightness > 40:
                # Red/brown dominant -> shift to green-olive
                nr = int(r * 0.7 + g * 0.15)
                ng = int(g * 1.05 + r * 0.1 + 8)
                nb = int(b * 0.6 + 5)
                pixels[x, y] = (min(255, nr), min(255, ng), min(255, nb))
            elif g >= r and saturation > 15 and brightness > 30:
                # Already green-ish — enhance toward modern olive
                nr = int(r * 0.8 + 5)
                ng = int(g * 0.95 + 5)
                nb = int(b * 0.6)
                pixels[x, y] = (min(255, nr), min(255, ng), min(255, nb))
            elif saturation < 25 and 60 < brightness < 200:
                # Neutral/grey cloth — tint to olive-green
                nr = int(brightness * 0.75 + 15)
                ng = int(brightness * 0.82 + 10)
                nb = int(brightness * 0.55)
                pixels[x, y] = (min(255, nr), min(255, ng), min(255, nb))

    return result

def recolor_tank(img):
    """Recolor T-80 tank to Ukrainian Oplot style — olive/tan camo with subtle blue-yellow marking."""
    result = img.copy()
    pixels = result.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            brightness = (r + g + b) / 3

            # Skip very dark/bright
            if brightness < 15 or brightness > 245:
                continue

            # Detect green-ish pixels (the tank body) and shift to Ukrainian olive-tan
            if g > r and g > b and brightness > 30:
                # Shift green toward olive-tan (warmer, less saturated green)
                nr = int(r * 0.9 + g * 0.15 + 15)
                ng = int(g * 0.85 + r * 0.1)
                nb = int(b * 0.6 + 5)
                pixels[x, y] = (min(255, nr), min(255, ng), min(255, nb))
            elif brightness > 30:
                # General desaturation toward tan
                nr = int(r * 0.9 + brightness * 0.1)
                ng = int(g * 0.85 + brightness * 0.1)
                nb = int(b * 0.7 + brightness * 0.05)
                pixels[x, y] = (min(255, nr), min(255, ng), min(255, nb))

    return result

def recolor_rocket(img):
    """Recolor Katyusha to Vilkha — shift to Ukrainian military sand/olive."""
    result = img.copy()
    pixels = result.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            brightness = (r + g + b) / 3

            if brightness < 15 or brightness > 245:
                continue

            # Shift toward sand/olive tones
            nr = int(r * 0.85 + brightness * 0.15 + 8)
            ng = int(g * 0.85 + brightness * 0.1 + 3)
            nb = int(b * 0.65)
            pixels[x, y] = (min(255, nr), min(255, ng), min(255, nb))

    return result

def add_blue_yellow_accents(img, intensity=0.15):
    """Add subtle blue and yellow accent tones to cavalry unit textures."""
    result = img.copy()
    pixels = result.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y][:3]
            brightness = (r + g + b) / 3
            saturation = max(r, g, b) - min(r, g, b)

            if brightness < 20 or brightness > 240:
                continue

            # Detect blue-ish areas and make them more Ukrainian blue
            if b > r and b > g and saturation > 30:
                nb = min(255, int(b * 1.1 + 10))
                nr = max(0, int(r * 0.85))
                ng = max(0, int(g * 0.85))
                pixels[x, y] = (nr, ng, nb)

            # Detect yellow/gold areas and enhance them
            elif r > 120 and g > 100 and b < r * 0.6 and saturation > 40:
                nr = min(255, int(r * 1.05 + 5))
                ng = min(255, int(g * 1.02))
                nb = max(0, int(b * 0.8))
                pixels[x, y] = (nr, ng, nb)

            # Detect whitish cloth areas — tint slightly blue
            elif saturation < 30 and 100 < brightness < 220:
                nr = int(r * 0.95)
                ng = int(g * 0.95)
                nb = min(255, int(b * 1.05 + 3))
                pixels[x, y] = (nr, ng, nb)

    return result


def main():
    originals_dir = r"C:\Projectsd\ron-ukraine-mod\art\originals"
    output_dir = r"C:\Projectsd\ron-ukraine-mod\art"

    os.makedirs(output_dir, exist_ok=True)

    print("=== Ukraine Mod Texture Recoloring ===\n")

    # 1. Red Guard -> Drone Operator (most important — Soviet look is worst mismatch)
    print("Recoloring RedGuard -> Drone Operator...")
    img = load_tga(os.path.join(originals_dir, "RedGuard.tga"))
    img = img.convert('RGB')
    result = add_ukraine_camo(img)
    save_tga(result, os.path.join(output_dir, "RedGuard.tga"))
    print(f"  Saved {output_dir}\\RedGuard.tga")

    # 2. T80_green -> Oplot Tank
    print("Recoloring T80_green -> Oplot Tank...")
    img = load_tga(os.path.join(originals_dir, "T80_green.tga"))
    img = img.convert('RGB')
    result = recolor_tank(img)
    save_tga(result, os.path.join(output_dir, "T80_green.tga"))
    print(f"  Saved {output_dir}\\T80_green.tga")

    # 3. katyusha -> Vilkha Rocket
    print("Recoloring katyusha -> Vilkha Rocket...")
    img = load_tga(os.path.join(originals_dir, "katyusha.tga"))
    img = img.convert('RGB')
    result = recolor_rocket(img)
    save_tga(result, os.path.join(output_dir, "katyusha.tga"))
    print(f"  Saved {output_dir}\\katyusha.tga")

    # 4. Rusiny -> Sich Cossack (add blue/yellow accents)
    print("Recoloring Rusiny -> Sich Cossack...")
    img = load_tga(os.path.join(originals_dir, "Rusiny.tga"))
    img = img.convert('RGB')
    result = add_blue_yellow_accents(img)
    save_tga(result, os.path.join(output_dir, "Rusiny.tga"))
    print(f"  Saved {output_dir}\\Rusiny.tga")

    # 5. Cossack -> Sich Warrior
    print("Recoloring Cossack -> Sich Warrior...")
    img = load_tga(os.path.join(originals_dir, "Cossack.tga"))
    img = img.convert('RGB')
    result = add_blue_yellow_accents(img)
    save_tga(result, os.path.join(output_dir, "Cossack.tga"))
    print(f"  Saved {output_dir}\\Cossack.tga")

    # 6. Don_cossack -> Cossack Hetman (more golden accents for elite unit)
    print("Recoloring Don_cossack -> Cossack Hetman...")
    img = load_tga(os.path.join(originals_dir, "Don_cossack.tga"))
    img = img.convert('RGB')
    result = add_blue_yellow_accents(img, intensity=0.2)
    save_tga(result, os.path.join(output_dir, "Don_cossack.tga"))
    print(f"  Saved {output_dir}\\Don_cossack.tga")

    print("\n=== All textures recolored! ===")
    print(f"\nOutput directory: {output_dir}")
    print("Run install.bat to copy these into the game, or manually copy the .tga files to:")
    print("  C:\\Program Files (x86)\\Steam\\steamapps\\common\\Rise of Nations\\art\\")


if __name__ == "__main__":
    main()
