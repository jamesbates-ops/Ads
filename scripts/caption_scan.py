"""Flag frames with burned-in white caption text in the lower-middle of a 9:16 clip.

Counts near-white pixels (min channel > 225) in a central band of the lower half,
sampled at 6 fps, and compares against the clip's own median frame.
"""
import subprocess, sys, numpy as np

def scan(path, y0=0.55, y1=0.90, x0=0.12, x1=0.88, fps=6):
    probe = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                     "stream=width,height", "-of", "csv=p=0", path]).decode().strip().split(",")
    w, h = int(probe[0]), int(probe[1])
    sw, sh = 360, int(360 * h / w)
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={sw}:{sh}",
                                   "-f", "rawvideo", "-pix_fmt", "rgb24", "-"])
    fr = np.frombuffer(raw, np.uint8).reshape(-1, sh, sw, 3)
    band = fr[:, int(y0 * sh):int(y1 * sh), int(x0 * sw):int(x1 * sw), :]
    white = (band.min(axis=3) > 225).sum(axis=(1, 2))
    base = np.median(white)
    hits = [(round(i / fps, 2), int(c)) for i, c in enumerate(white) if c > base + 40]
    return int(base), hits

for p in sys.argv[1:]:
    base, hits = scan(p)
    flag = "CAPTIONS?" if hits else "clean"
    print(f"{p}: {flag} base={base} hits={hits[:12]}{' ...' if len(hits) > 12 else ''}")
