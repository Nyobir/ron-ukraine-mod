from PIL import Image
import os

out = os.path.join("C:", os.sep, "Projectsd", "ron-ukraine-mod", "art", "originals")
img = Image.open(os.path.join(out, "Iface_ALLCIVS_assets.png"))
print(f"Size: {img.size}, Mode: {img.mode}")

# Save strips every 32 pixels
for y_start in range(0, 256, 32):
    strip = img.crop((0, y_start, 512, y_start + 32))
    strip.save(os.path.join(out, f"strip_{y_start}.png"))
    print(f"Strip at y={y_start}: saved")
