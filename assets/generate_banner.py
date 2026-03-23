#!/usr/bin/env python3
"""Generate a PNG banner for the repo README."""

from PIL import Image, ImageDraw, ImageFont
import os

WIDTH = 1800
HEIGHT = 600
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
    font_large = ImageFont.truetype("/System/Library/Fonts/SFMono-Bold.otf", 150)
    font_small = ImageFont.truetype("/System/Library/Fonts/SFMono-Regular.otf", 24)
    font_tiny = ImageFont.truetype("/System/Library/Fonts/SFMono-Regular.otf", 16)
except:
    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 150)
        font_small = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 24)
        font_tiny = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 16)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_tiny = ImageFont.load_default()

# Helper to center text
def center_x(text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    return (WIDTH - tw) // 2

# Line 1: "THE CORE" in light orange
draw.text((center_x("THE CORE", font_large), 30), "THE CORE", fill=LIGHT_ORANGE, font=font_large)

# Line 2: "AI PM" in deeper orange
draw.text((center_x("AI PM", font_large), 170), "AI PM", fill=ORANGE, font=font_large)

# Line 3: "WORKFLOW" in white
draw.text((center_x("WORKFLOW", font_large), 310), "WORKFLOW", fill=WHITE, font=font_large)

# Accent bar (centered)
bar_w = 100
draw.rectangle([(WIDTH//2 - bar_w//2, 485), (WIDTH//2 + bar_w//2, 489)], fill=ORANGE)

# Tagline (centered)
tagline = "10 SKILLS  ·  1 TOOLKIT  ·  HOURS SAVED"
draw.text((center_x(tagline, font_small), 510), tagline, fill=MUTED, font=font_small)

# Bottom right
draw.text((WIDTH - 380, HEIGHT - 30), "works with Claude Code & Cursor", fill=DARK_MUTED, font=font_tiny)

out_path = os.path.join(os.path.dirname(__file__), 'banner.png')
img.save(out_path, 'PNG')
print(f"Saved: {out_path}")
print(f"Size: {WIDTH}x{HEIGHT}")
