#!/usr/bin/env python3
"""Author burned-in captions for "The Phone Call" from the known line grid.

Timings come from the audio layout, not from transcription, so the cards land
exactly on the reads. Frankie is white; Chris is amber and italic, so the two
speakers read apart on mute without labels eating screen space.
"""
import subprocess, sys, os

# line id -> (caption cards)   split at natural phrase boundaries
CARDS = {
    "11":  ["Hi there!"],
    "12":  ["Hey Frankie, it's Chris —", "you holding up after last night?"],
    "21":  ["Yeah, slightly tired,", "just cleaning up now —", "but it was so much fun! What's up?"],
    "32":  ["My girlfriend woke up", "in such a good mood.", "She usually gets these awful hangovers,",
            "but she feels amazing.", "Where did you get that amazing wine?"],
    "41":  ["Which one?"],
    "42":  ["Ooh, it was super dry and full bodied —", "tasted like black fruits,", "mocha, and cassis.",
            "In that heavy bottle."],
    "51":  ["The Raptor & Crimson?", "It's my absolute favourite,", "I drink it all the time."],
    "62":  ["Oh wow, just looking online now —", "it's so expensive!",
            "How do you have the money", "to buy this so often?"],
    "71":  ["Ha! On my salary I definitely can't.", "I tell you what —", "I'll let you in on a little secret."],
    "72":  ["Oh yeah? Is this another hack?"],
    "81":  ["It's this app I was recommended —", "for just $10 a month,", "you get sent great offers on crates",
            "of wine I'd never be able to afford."],
    "91":  ["They have great relationships", "with prestigious vineyards.",
            "I found that Raptor the other day,", "and I can't stop drinking it!"],
    "102": ["That's amazing —", "so how much was this crate?"],
    "111": ["It's just $20 a bottle —", "over 75% off where I usually buy it.",
            "Best of all, they deliver", "straight to my door.", "There's, like, zero stress."],
    "122": ["That's incredible,", "I'll get on it right away.", "We gotta repay the favour sometime!"],
    "131": ["Oh, that's easy —", "just make sure you buy", "some more of the Raptor for me.",
            "It can't be that cheap for long!"],
}

HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Frankie,Montserrat,62,&H00FFFFFF,&H00000000,&H96000000,-1,0,1,4,2,2,90,90,300,1
Style: Chris,Montserrat,62,&H007FD4FF,&H00000000,&H96000000,-1,-1,1,4,2,2,90,90,300,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def main(laypath, clipdir, out):
    rows = [l.split() for l in open(laypath) if l.strip()]
    events = []
    for lid, ms, tempo, who in rows:
        dur = float(subprocess.check_output(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", os.path.join(clipdir, f"p{lid}.wav")]))
        start = int(ms) / 1000.0
        cards = CARDS[lid]
        # split the line's window between cards in proportion to their length
        weights = [len(c) for c in cards]
        total = sum(weights)
        style = "Chris" if who == "C" else "Frankie"
        t = start
        for card, w in zip(cards, weights):
            span = dur * w / total
            events.append((t, t + span, style, card))
            t += span
    events.sort()
    with open(out, "w") as f:
        f.write(HEADER)
        for a, b, style, text in events:
            f.write(f"Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{text}\n")
    print(f"{len(events)} caption cards -> {out}")

if __name__ == "__main__":
    main(*sys.argv[1:])
