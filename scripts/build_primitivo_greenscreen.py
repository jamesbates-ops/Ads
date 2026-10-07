#!/usr/bin/env python3
"""Trim, loudness-match and assemble the Primitivo green-screen talking clips.

Inputs are the revoiced (Callum) Higgsfield clips in --src (H1..H3 hooks, B1..B8 body).
Outputs per-line clips plus one full-length green-screen cut per hook.
"""
import argparse, json, os, subprocess, numpy as np

HOOKS = ["H1", "H2", "H3"]
BODY = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"]
HEAD, TAIL = 0.12, 0.25          # seconds kept before first / after last speech
LUFS, TP = -14, -1.5             # social-platform loudness target


def run(cmd):
    subprocess.run(cmd, check=True)


def speech_bounds(path):
    raw = subprocess.check_output(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"])
    a = np.frombuffer(raw, np.int16).astype(float) / 32768
    win = 320  # 20 ms
    db = np.array([20 * np.log10(np.sqrt(np.mean(a[i:i + win] ** 2)) + 1e-9) for i in range(0, len(a) - win, win)])
    idx = np.where(db > db.max() - 30)[0]
    return idx[0] * 0.02, (idx[-1] + 1) * 0.02, len(a) / 16000


def loudnorm_params(path, ss, t):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-ss", f"{ss:.3f}", "-t", f"{t:.3f}", "-i", path,
                          "-af", f"loudnorm=I={LUFS}:TP={TP}:LRA=11:print_format=json", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return json.loads(out[out.rindex("{"):out.rindex("}") + 1])


def trim_clip(src, dst):
    on, off, dur = speech_bounds(src)
    ss, end = max(0.0, on - HEAD), min(dur, off + TAIL)
    t = end - ss
    m = loudnorm_params(src, ss, t)
    af = (f"loudnorm=I={LUFS}:TP={TP}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,"
          f"aresample=48000,afade=t=in:d=0.01,afade=t=out:st={t - 0.04:.3f}:d=0.04")
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{ss:.3f}", "-t", f"{t:.3f}", "-i", src,
         "-af", af, "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-r", "24",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart", dst])
    return dict(trim_in=round(ss, 2), trim_out=round(end, 2), duration=round(t, 2))


def concat(parts, dst):
    inputs = sum((["-i", p] for p in parts), [])
    streams = "".join(f"[{i}:v][{i}:a]" for i in range(len(parts)))
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex",
         f"{streams}concat=n={len(parts)}:v=1:a=1[v][a]", "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-r", "24",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", dst])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    clips_dir = os.path.join(args.out, "clips")
    os.makedirs(clips_dir, exist_ok=True)
    report = {}
    for name in HOOKS + BODY:
        report[name] = trim_clip(os.path.join(args.src, f"{name}.mp4"), os.path.join(clips_dir, f"{name}.mp4"))
        print(name, report[name])
    for i, hook in enumerate(HOOKS, 1):
        parts = [os.path.join(clips_dir, f"{n}.mp4") for n in [hook] + BODY]
        concat(parts, os.path.join(args.out, f"primitivo_greenscreen_hook{i}.mp4"))
    json.dump(report, open(os.path.join(args.out, "clip_timings.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
