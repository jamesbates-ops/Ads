#!/usr/bin/env python3
"""Burned-in caption cards for WINEDROPS "The Right Signs" (9:16, 0:51).

One card per shot, exactly as specified in the brief's shot table (section 7).
The three hook variants differ only in the shot-1 card; shots 2-9 are identical
across all cuts, which is what keeps the variants comparable in test.

Shot 9's card is intentionally absent: the brief lists it as
"[end card / CTA - TBC]" and no brand assets were supplied.
"""
import sys

HOOKS = {
    1: "If I met a man who drank this,\\NI'd never forget him.",
    2: "Yeah, this would keep us talking,\\Nall night.",
    3: "This tells me everything\\NI need to know about him.",
}

# (start, end, text) -- seconds. Shots are cut at
# 0/3/7/10/15/22/30/39/47/51; cards are inset so they do not flick on the cut.
CARDS = [
    (3.15,  6.85,  "The signs I look for"),
    (7.15,  9.85,  "Clothes. Taste. In shape."),
    (10.15, 14.85, "But this? This is the tell."),
    (15.15, 21.85, "Full-bodied Cab  ·  18 months in oak"),
    (22.15, 29.85, "Original. Not a trend."),
    # Shot 7 opens on a ~1.6s sip before she speaks; the card waits for the line.
    (31.70, 38.85, "Blackcurrant  ·  Plum  ·  Espresso"),
    (39.15, 46.85, "$85 a bottle  ·  case of 6 at 75% off"),
]

HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Card,Montserrat,60,&H00FFFFFF,&H00FFFFFF,&H00101010,&H80000000,-1,0,0,0,100,100,0.6,0,1,3.4,1.6,2,90,90,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ts(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return "%d:%02d:%05.2f" % (h, m, s)


def build(variant):
    rows = [(0.15, 2.85, HOOKS[variant])] + CARDS
    out = [HEADER]
    for start, end, text in rows:
        out.append("Dialogue: 0,%s,%s,Card,,0,0,0,,%s\n" % (ts(start), ts(end), text))
    return "".join(out)


if __name__ == "__main__":
    variant = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    sys.stdout.write(build(variant))
