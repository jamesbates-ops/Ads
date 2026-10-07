#!/usr/bin/env python3
"""Assemble the Dolum Estates green-screen ad: presenter (keyed) over B-roll.

Builds one cut per hook (H1, H2, H3). All body blocks are shared.
Inputs (relative to this script's directory):
  talk/vc_<block>.mp4   voice-changed presenter clips (720x1280, green screen)
  broll/<shot>.mp4      B-roll clips (1080x1920, 5s)
  speech.json           silencedetect speech bounds + pauses per block
  words.json            whisper word timings per block
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 24
W, H = 1080, 1920
KEY = "0x039E38"            # measured from the talk clips' wall
PRES_H = 1190               # presenter height on the 1920 canvas (~62%)
HEAD, TAIL = 0.06, 0.18     # keep before first / after last speech
PAUSE_MAX, PAUSE_KEEP = 0.55, 0.20  # pauses longer than this are cut to 2*KEEP
OUT = os.path.join(HERE, "build")
os.makedirs(OUT, exist_ok=True)

speech = json.load(open(os.path.join(HERE, "speech.json")))
words = json.load(open(os.path.join(HERE, "words.json")))

def fr(t):  # snap to frame grid
    return round(t * FPS) / FPS

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(" ".join(cmd) + "\n" + r.stderr[-3000:])
        raise SystemExit(1)

# ---------------------------------------------------------------- presenter
def block_segments(k, hold_to_end=False):
    s = speech[k]
    a = fr(max(0.0, s["sp_start"] - HEAD))
    b = s["dur"] if hold_to_end else min(s["dur"], s["sp_end"] + TAIL)
    b = fr(min(b, s["dur"] - 1 / FPS / 2))
    segs, cur = [], a
    for ps, pe in s["pauses"]:
        if pe - ps > PAUSE_MAX and ps > a and pe < b:
            segs.append((cur, fr(ps + PAUSE_KEEP)))
            cur = fr(pe - PAUSE_KEEP)
    segs.append((cur, b))
    return [(x, y) for x, y in segs if y - x > 1.5 / FPS]

def mapper(segs):
    def m(t):
        acc = 0.0
        for a, b in segs:
            if t < a:
                return acc
            if t <= b:
                return acc + (t - a)
            acc += b - a
        return acc
    return m

def render_block(k, segs):
    out = os.path.join(OUT, f"p_{k}.mov")
    src = os.path.join(HERE, "talk", f"vc_{k}.mp4")
    parts, labels = [], []
    for i, (a, b) in enumerate(segs):
        d = b - a
        parts.append(f"[0:v]trim=start={a:.4f}:end={b:.4f},setpts=PTS-STARTPTS[v{i}]")
        parts.append(f"[0:a]atrim=start={a:.4f}:end={b:.4f},asetpts=PTS-STARTPTS,"
                     f"afade=t=in:st=0:d=0.012,afade=t=out:st={max(0, d - 0.015):.4f}:d=0.015[a{i}]")
        labels.append(f"[v{i}][a{i}]")
    parts.append("".join(labels) + f"concat=n={len(segs)}:v=1:a=1[v][a]")
    run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-i", src,
         "-filter_complex", ";".join(parts), "-map", "[v]", "-map", "[a]",
         "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "12", "-pix_fmt", "yuv420p",
         "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2", out])
    return out

# ---------------------------------------------------------------- B-roll plan
# (shot, cue word index or 0 for block start, source in-point)
PLAN = {
    "101": [(201, 0, 0.0), (202, 8, 0.0)],
    "102": [(201, 0, 0.0), (203, 8, 0.0), (211, 19, 0.0)],
    "103": [(201, 0, 0.0), (208, 8, 0.0)],
    "1":   [(205, 0, 0.0), (206, 11, 0.0)],
    "2":   [(207, 0, 0.0), (204, 15, 0.0)],
    "3":   [(210, 0, 0.0), (209, 11, 0.0), (211, 17, 0.0)],
    "4":   [(213, 0, 0.0), (212, 10, 0.0)],
    "5":   [(214, 0, 0.0), (215, 8, 0.0), (216, 13, 0.0)],
    "6":   [(217, 0, 0.0), (218, 11, 0.0)],
    "7":   [(219, 0, 0.0), (220, 6, 0.0), (221, 13, 0.0)],
    "8":   [(214, 0, 1.0), (222, 9, 0.0)],
    "9":   [(223, 0, 0.0), (224, 13, 0.0)],
    "10":  [(225, 0, 0.0), (226, 10, 0.0)],
    "11":  [(227, 0, 0.0), (228, 13, 0.0)],
    "12":  [(229, 0, 0.0), (203, 10, 0.3)],
    "13":  [(230, 0, 0.0), (231, 15, 0.0)],
    "14":  [(232, 0, 0.0), (230, 8, 1.2)],
}
CUE_LEAD = 0.10
BROLL_LEN = 5.0

# text callouts: (block, cue word index, until: 'block' | 'end', card id)
CARDS = [
    ("12", 0, "block", "decanter"),
    ("12", 5, "block", "suckling"),
    ("12", 10, "block", "members"),
    ("13", 12, "s19", "price60"),
    ("13", 19, "block", "price60x"),
    ("13", 19, "block", "sixfor100"),
    ("14", 2, "end", "fourfree"),
    ("14", 8, "end", "buytoday"),
]

FONT_B = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FONT_M = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
# cards stack downward from CARD_TOP inside their group, clear of the
# platform UI band at the top and of the presenter's head (~y 800)
CARD_TOP, CARD_GAP = 290, 18
CARD_SLOT = {"decanter": ("pay", 0), "suckling": ("pay", 1), "members": ("pay", 2),
             "price60": ("price", 0), "price60x": ("price", 0), "sixfor100": ("price", 1),
             "fourfree": ("cta", 0), "buytoday": ("cta", 1)}

def card_y(cid):
    grp, slot = CARD_SLOT[cid]
    y = CARD_TOP
    for other, (g, s) in CARD_SLOT.items():
        if g == grp and s < slot and other != "price60x":
            y += Image.open(os.path.join(OUT, f"card_{other}.png")).height + CARD_GAP
    return y

def make_card(cid):
    spec = {
        "decanter":  ("DECANTER", "94 PTS"),
        "suckling":  ("JAMES SUCKLING", "93 PTS"),
        "members":   ("CASEDROPS MEMBERS", "4.5 / 5"),
        "price60":   ("USUALLY", "$60 / BOTTLE"),
        "price60x":  ("USUALLY", "$60 / BOTTLE"),
        "sixfor100": ("ON CASEDROPS", "6 FOR $100"),
        "fourfree":  ("THAT'S", "4 FREE BOTTLES"),
        "buytoday":  ("ONCE IT'S GONE, IT'S GONE", "BUY TODAY"),
    }[cid]
    small, big = spec
    hot = cid in ("sixfor100", "fourfree", "buytoday")
    s_sz, b_sz = (38, 92) if hot else (36, 76)
    fs, fb = ImageFont.truetype(FONT_M, s_sz), ImageFont.truetype(FONT_B, b_sz)
    d0 = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    ws = d0.textlength(small, font=fs); wb = d0.textlength(big, font=fb)
    pad_x, pad_t, gap = 48, 20, 6
    bb = d0.textbbox((0, 0), big, font=fb)            # ink box of the big line
    cw = int(max(ws, wb) + 2 * pad_x)
    ch = pad_t + s_sz + gap + (bb[3] - bb[1]) + 28
    img = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    fill = (122, 18, 40, 240) if hot else (14, 12, 12, 205)
    d.rounded_rectangle([0, 0, cw - 1, ch - 1], radius=28, fill=fill)
    d.text(((cw - ws) / 2, pad_t), small, font=fs, fill=(236, 214, 170, 255))
    by = pad_t + s_sz + gap - bb[1]
    d.text(((cw - wb) / 2, by), big, font=fb, fill=(255, 255, 255, 255))
    if cid == "price60x":
        ly = by + bb[1] + (bb[3] - bb[1]) * 0.5
        d.line([((cw - wb) / 2 - 12, ly), ((cw + wb) / 2 + 12, ly)], fill=(235, 45, 65, 255), width=10)
    p = os.path.join(OUT, f"card_{cid}.png")
    img.save(p)
    return p

# ---------------------------------------------------------------- build a version
def build(hook, tag):
    order = [hook] + [str(i) for i in range(1, 15)]
    blocks, t0 = [], 0.0
    for k in order:
        segs = block_segments(k, hold_to_end=(k == "14"))
        dur = sum(b - a for a, b in segs)
        blocks.append(dict(k=k, segs=segs, start=t0, dur=dur, m=mapper(segs)))
        t0 += dur
    total = t0

    # presenter track
    for b in blocks:
        p = os.path.join(OUT, f"p_{b['k']}.mov")
        if not os.path.exists(p):
            render_block(b["k"], b["segs"])
    lst = os.path.join(OUT, f"pres_{tag}.txt")
    with open(lst, "w") as f:
        for b in blocks:
            f.write(f"file 'p_{b['k']}.mov'\n")
    pres = os.path.join(OUT, f"pres_{tag}.mov")
    run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", pres])

    # B-roll cut list
    cuts = []
    for b in blocks:
        for shot, wi, src_in in PLAN[b["k"]]:
            if wi == 0:
                t = b["start"]
            else:
                t = b["start"] + max(0.0, b["m"](words[b["k"]][wi][0]) - CUE_LEAD)
            cuts.append([fr(t), shot, src_in, b["k"]])
    cuts.sort()
    segs_bg = []
    for i, (t, shot, src_in, k) in enumerate(cuts):
        end = cuts[i + 1][0] if i + 1 < len(cuts) else fr(total)
        segs_bg.append(dict(t=t, d=end - t, shot=shot, src_in=src_in, k=k))

    seglist = os.path.join(OUT, f"bg_{tag}.txt")
    with open(seglist, "w") as f:
        for j, s in enumerate(segs_bg):
            avail = BROLL_LEN - s["src_in"]
            speed = 1.0 if s["d"] <= avail else s["d"] / avail   # slow-mo when a shot is short
            s["speed"] = round(speed, 3)
            nframes = int(round(s["d"] * FPS))
            sp = os.path.join(OUT, f"bg_{tag}_{j:02d}.mp4")
            vf = (f"trim=start={s['src_in']:.3f},setpts=(PTS-STARTPTS)*{speed:.4f},fps={FPS},"
                  f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,"
                  f"tpad=stop_mode=clone:stop_duration=1")
            run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error",
                 "-i", os.path.join(HERE, "broll", f"{s['shot']}.mp4"), "-vf", vf, "-frames:v", str(nframes),
                 "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "14", "-pix_fmt", "yuv420p", sp])
            f.write(f"file '{os.path.basename(sp)}'\n")
    bg = os.path.join(OUT, f"bg_{tag}.mp4")
    run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", seglist,
         "-c", "copy", bg])

    # cards: compute windows
    bymap = {b["k"]: b for b in blocks}
    card_windows = []
    for k, wi, until, cid in CARDS:
        b = bymap[k]
        st = b["start"] + max(0.0, b["m"](words[k][wi][0]) - CUE_LEAD)
        if until == "block":
            en = b["start"] + b["dur"]
        elif until == "end":
            en = total
        else:  # until another word in the same block
            en = b["start"] + max(0.0, b["m"](words[k][int(until[1:])][0]) - CUE_LEAD)
        card_windows.append((round(st, 3), round(en, 3), cid))

    # final composite
    for cid in CARD_SLOT:
        make_card(cid)
    inputs = ["-i", bg, "-i", pres]
    fc = [f"[1:v]chromakey={KEY}:0.12:0.06,despill=type=green:mix=0.6:expand=0.1,"
          f"scale=-2:{PRES_H}:flags=lanczos[fg]",
          "[0:v][fg]overlay=x=(W-w)/2:y=H-h:format=auto[c0]"]
    last = "c0"
    for i, (st, en, cid) in enumerate(card_windows):
        p = os.path.join(OUT, f"card_{cid}.png")
        inputs +=["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.3f}", "-i", p]
        idx = 2 + i
        fd = 0.18
        fc.append(f"[{idx}:v]format=rgba,fade=t=in:st={st:.3f}:d={fd}:alpha=1,"
                  f"fade=t=out:st={max(st, en - fd):.3f}:d={fd}:alpha=1[t{i}]")
        nxt = f"c{i + 1}"
        fc.append(f"[{last}][t{i}]overlay=x=(W-w)/2:y={card_y(cid)}:"
                  f"enable='between(t,{st:.3f},{en:.3f})'[{nxt}]")
        last = nxt
    fc.append(f"[{last}]format=yuv420p[vout]")
    fc.append("[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    final = os.path.join(OUT, f"dolum_{tag}.mp4")
    run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", *inputs,
         "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
         "-t", f"{total:.3f}", "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-profile:v", "high", "-pix_fmt", "yuv420p",
         "-movflags", "+faststart", "-c:a", "aac", "-b:a", "192k", final])

    # timing sheet
    sheet = dict(version=tag, total=round(total, 2),
                 blocks=[dict(k=b["k"], start=round(b["start"], 2), end=round(b["start"] + b["dur"], 2))
                         for b in blocks],
                 broll=[dict(start=round(s["t"], 2), dur=round(s["d"], 2), shot=s["shot"], speed=s["speed"])
                        for s in segs_bg],
                 cards=card_windows)
    json.dump(sheet, open(os.path.join(OUT, f"timing_{tag}.json"), "w"), indent=1)
    print(tag, "total", round(total, 2), "->", final)
    return sheet

if __name__ == "__main__":
    which = sys.argv[1:] or ["H1", "H2", "H3"]
    hooks = {"H1": "101", "H2": "102", "H3": "103"}
    for tag in which:
        build(hooks[tag], tag)
