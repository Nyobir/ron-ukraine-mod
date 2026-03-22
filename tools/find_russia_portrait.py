from PIL import Image
import os

out = os.path.join("C:", os.sep, "Projectsd", "ron-ukraine-mod", "art", "originals")
img = Image.open(os.path.join(out, "iface_setup_buttons.png"))

# The portraits appear to start around y=160 and are in a grid
# Each portrait looks roughly 24x24 pixels
# Let me extract each individual portrait more carefully

# First let's look at the full bottom section with pixel-level detail
bottom = img.crop((0, 155, 220, 256))
# Scale up 4x so we can see clearly
scaled = bottom.resize((bottom.width * 4, bottom.height * 4), Image.NEAREST)
scaled.save(os.path.join(out, "portraits_zoomed.png"))

# Count the portraits - they seem to be in rows of ~9-10
# Let me try 24x24 grid starting from different offsets
for row in range(4):
    for col in range(10):
        x = col * 22
        y = 158 + row * 24
        portrait = img.crop((x, y, x + 22, y + 24))
        portrait_scaled = portrait.resize((88, 96), Image.NEAREST)
        idx = row * 10 + col
        portrait_scaled.save(os.path.join(out, f"portrait_{idx}.png"))

# Russia is TRIBE13, so let's check portrait_13
print("Saved individual portraits 0-39")
print("Russia = TRIBE13 = portrait_13.png")

# Also check the interface.xml tribe order
# Tribes in RoN (T&P):
# 0=Aztecs, 1=Bantu, 2=British, 3=Chinese, 4=Egyptians, 5=French
# 6=Germans, 7=Greeks, 8=Inca, 9=Japanese, 10=Koreans, 11=Maya
# 12=Mongols, 13=Russians, 14=Chinese(?), 15=Japanese(?)
# Actually let me check the tribe file order
