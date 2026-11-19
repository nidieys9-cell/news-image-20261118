#!/usr/bin/env python3
"""Draw the news-image-20261118 entry: one-day world news infographic.

Original drawing script for Wednesday, 18 November 2026.
All stories were verified from news reporting dated 18 Nov 2026
(see README.md for sources). Output: entry.png, 1000 x 1000.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

W, H = 1000, 1000
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_TITLE = font("DejaVuSans-Bold.ttf", 54)
F_SUB = font("DejaVuSans-Bold.ttf", 30)
F_DATE = font("DejaVuSans.ttf", 26)
F_HEAD = font("DejaVuSans-Bold.ttf", 27)
F_BODY = font("DejaVuSans.ttf", 21)
F_TAG = font("DejaVuSans-Bold.ttf", 17)
F_FOOT = font("DejaVuSans.ttf", 17)
F_ICON = font("DejaVuSans-Bold.ttf", 26)

NAVY = (13, 33, 66)
GOLD = (245, 183, 49)
BG = (244, 246, 249)
CARD = (255, 255, 255)
INK = (22, 28, 38)
MUTED = (84, 96, 112)

STORIES = [
    {
        "tag": "DIPLOMACY  -  CHINA",
        "color": (196, 30, 42),
        "icon": "XI",
        "head": "Xi Meets Putin in Shenzhen",
        "body": "Xi Jinping and Vladimir Putin met at APEC in Shenzhen ahead of Thursday's trilateral talks with Donald Trump on Ukraine and stability.",
    },
    {
        "tag": "WAR  -  UKRAINE",
        "color": (0, 91, 172),
        "icon": "UA",
        "head": "Kerch Bridge Hit, Span Falls",
        "body": "Ukrainian drones and missiles struck the bridge linking Russia to Crimea; part of a road span collapsed into the Kerch Strait.",
    },
    {
        "tag": "MIDDLE EAST  -  GULF",
        "color": (217, 119, 6),
        "icon": "IR",
        "head": "Iran Drones Target Kuwait, Bahrain",
        "body": "Iran said it sent drones at US bases in Kuwait and Bahrain intercepted attacks, after US strikes on a missile site on Qeshm Island.",
    },
    {
        "tag": "POLITICS  -  UNITED STATES",
        "color": (16, 122, 87),
        "icon": "US",
        "head": "Peltola Wins Alaska: Senate 56-44",
        "body": "Democrat Mary Peltola defeated Republican Dan Sullivan in Alaska, giving Democrats a projected 56-44 majority in the US Senate.",
    },
    {
        "tag": "HEALTH  -  UNITED STATES",
        "color": (124, 58, 237),
        "icon": "+",
        "head": "US Loses Measles-Free Status",
        "body": "After 26 years, the US lost measles elimination status in a record outbreak: more than 5,400 cases and 10 deaths reported.",
    },
    {
        "tag": "HUMANITARIAN  -  YEMEN",
        "color": (8, 145, 178),
        "icon": "UN",
        "head": "UNICEF: 64 Children Killed in Yemen",
        "body": "UNICEF said 64 children were killed and 64 injured since 3 September as fighting resumed; about 330,000 people are displaced.",
    },
]


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Header band (revised: shorter band, no clipped side label)
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 156], fill=GOLD)
    d.text((48, 20), "THE WORLD IN ONE DAY", font=F_TITLE, fill=(255, 255, 255))
    d.text((50, 88), "Wednesday, 18 November 2026", font=F_SUB, fill=GOLD)
    d.text((770, 92), "SIX STORIES", font=F_SUB, fill=(190, 205, 230))

    # Story cards: 6 rows (revised: taller cards so text never clips)
    top = 172
    card_h = 124
    gap = 8
    for i, s in enumerate(STORIES):
        y = top + i * (card_h + gap)
        x0, x1 = 36, W - 36
        d.rounded_rectangle([x0, y, x1, y + card_h], radius=14, fill=CARD,
                            outline=(214, 220, 229), width=1)
        # left colour bar
        d.rounded_rectangle([x0, y, x0 + 12, y + card_h], radius=6, fill=s["color"])
        # icon badge
        cx, cy, r = x0 + 62, y + card_h // 2, 30
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=s["color"])
        tw = d.textlength(s["icon"], font=F_ICON)
        d.text((cx - tw / 2, cy - 15), s["icon"], font=F_ICON, fill=(255, 255, 255))
        # tag + headline
        tx = x0 + 112
        d.text((tx, y + 10), s["tag"], font=F_TAG, fill=s["color"])
        d.text((tx, y + 33), s["head"], font=F_HEAD, fill=INK)
        lines = wrap(d, s["body"], F_BODY, x1 - tx - 22)
        for j, line in enumerate(lines[:2]):
            d.text((tx, y + 72 + j * 25), line, font=F_BODY, fill=MUTED)

    # Footer
    fy = top + 6 * (card_h + gap) + 4
    d.text((48, fy), "Sources: AFP, AP, UN News / UNICEF, Horizon daily brief - all dated 18 Nov 2026. See README.",
           font=F_FOOT, fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {img.size} {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
