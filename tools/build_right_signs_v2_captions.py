#!/usr/bin/env python3
"""Caption cards for "The Right Signs" v2, timed to the SUPPLIED voiceover.

v1 timed cards to the brief's nominal shot table. This version times them to
word-level timestamps transcribed from the client's own VO, so each card lands
on the word that earns it rather than on a notional cut point.

Copy is verbatim from the brief's shot table (section 7). Shot 9 has no card:
the brief lists it as "[end card / CTA - TBC]" and no brand assets exist. The
supplied VO ends at 46.98s and runs to 51.014s, leaving a 4.03s silent hold
exactly where that end card belongs.
"""
import sys

# (start, end, text). Anchored to transcribed word times:
#   hook          0.74 - 3.60
#   "When I go"   4.76      "Great clothes"  7.74     "but bringing"  10.96
#   "It's a full" 14.20     "Original"      23.98     "And those"     32.78
#   "The best"    36.90     "Then we can"   44.38 (ends 46.98)
CARDS = [
    (0.60,  3.90,  "Yeah, this would keep us talking,\\Nall night."),
    (4.60,  7.20,  "The signs I look for"),
    (7.60,  10.70, "Clothes. Taste. In shape."),
    (10.90, 14.00, "But this? This is the tell."),
    (14.15, 21.00, "Full-bodied Cab  ·  18 months in oak"),
    # lands on "Original", not on the start of the shot
    (23.90, 28.60, "Original. Not a trend."),
    # waits out the 2.3s sip; lands on "And those layers..."
    (32.70, 36.75, "Blackcurrant  ·  Plum  ·  Espresso"),
    (36.90, 44.20, "$85 a bottle  ·  case of 6 at 75% off"),
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


if __name__ == "__main__":
    out = [HEADER]
    for start, end, text in CARDS:
        out.append("Dialogue: 0,%s,%s,Card,,0,0,0,,%s\n" % (ts(start), ts(end), text))
    sys.stdout.write("".join(out))
