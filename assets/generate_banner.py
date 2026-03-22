#!/usr/bin/env python3
"""Generate a PNG banner for the repo README."""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH = 1200
HEIGHT = 400
BG_COLOR = (30, 30, 30)

# Claude Code accent colors
ORANGE = (217, 119, 87)       # #D97757
LIGHT_ORANGE = (232, 149, 106) # #E8956A
WHITE = (245, 245, 245)
MUTED = (106, 117, 133)       # #6a7585
DARK_MUTED = (61, 61, 61)

img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# Try to load a nice font, fall back to default
try:
    font_large = ImageFont.truetype("/System/Library/Fonts/SFMono-Bold.otf", 72)
    font_medium = ImageFont.truetype("/System/Library/Fonts/SFMono-Bold.otf", 48)
    font_small = ImageFont.truetype("/System/Library/Fonts/SFMono-Regular.otf", 18)
    font_tiny = ImageFont.truetype("/System/Library/Fonts/SFMono-Regular.otf", 14)
except:
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 72)
        font_medium = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 48)
        font_small = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 18)
        font_tiny = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 14)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_tiny = ImageFont.load_default()

# Line 1: "THE CORE" in orange
draw.text((60, 50), "THE CORE", fill=LIGHT_ORANGE, font=font_large)

# Line 2: "AI PM" in orange
draw.text((60, 135), "AI PM", fill=ORANGE, font=font_large)

# Line 3: "WORKFLOW" in white
draw.text((60, 220), "WORKFLOW", fill=WHITE, font=font_large)

# Accent bar
draw.rectangle([(60, 315), (140, 318)], fill=ORANGE)

# Tagline
draw.text((60, 335), "10 SKILLS  ·  1 TOOLKIT  ·  HOURS SAVED", fill=MUTED, font=font_small)

# Bottom right
draw.text((WIDTH - 340, HEIGHT - 30), "works with Claude Code & Cursor", fill=DARK_MUTED, font=font_tiny)

out_path = os.path.join(os.path.dirname(__file__), 'banner.png')
img.save(out_path, 'PNG')
print(f"Saved: {out_path}")
print(f"Size: {WIDTH}x{HEIGHT}")
