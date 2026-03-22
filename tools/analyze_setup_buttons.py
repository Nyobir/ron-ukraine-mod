from PIL import Image
import os

out = os.path.join("C:", os.sep, "Projectsd", "ron-ukraine-mod", "art", "originals")
img = Image.open(os.path.join(out, "iface_setup_buttons.png"))
print(f"Size: {img.size}, Mode: {img.mode}")

# Crop bottom half where nation icons appear
bottom = img.crop((0, 128, 256, 256))
bottom.save(os.path.join(out, "setup_bottom.png"))

# Crop even more focused on the circular nation portraits
portraits = img.crop((0, 160, 256, 256))
portraits.save(os.path.join(out, "setup_portraits.png"))

# Finer strips
for y in range(160, 256, 24):
    strip = img.crop((0, y, 256, min(y+24, 256)))
    strip.save(os.path.join(out, f"setup_row_{y}.png"))
    print(f"Row y={y}: saved")
