#!/usr/bin/env bash
# Sommelier countdown (Winedrops Châteauneuf-du-Pape): to-camera clips for the edit, no B-roll.
# Each line is the 1080p generation (locked shot from the wine-shop seed) with the Callum
# voice-changed audio laid back on, cut tight to the speech and levelled to -16 LUFS.
# Writes clips/, a contact sheet and a README, then zips them.
# Needs curl, ffmpeg/ffprobe, python3 and zip.  Usage: bash sommelier-countdown-build.sh [workdir]
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
W=${1:-./sommelier_countdown_build}
rm -rf "$W"; mkdir -p "$W"/src "$W"/pkg/clips
cd "$W"
LUFS=-16
grep -v '^\s*$' "$HERE/sommelier-countdown-blocks.tsv" > blocks.tsv

# key | section | 1080p generation | voice-changed proxy (720p, same timing) | cut in s | line
# A line generated in two halves has "urlA|urlB" in both URL columns and "A_END|B_START|B_END"
# as its cut: half A runs to A_END, half B from B_START to B_END, joined with a 3-frame dissolve.
echo "download"
while IFS=$'\t' read -r k _ raw vc _; do
  IFS='|' read -ra R <<< "$raw"; IFS='|' read -ra V <<< "$vc"
  for i in "${!R[@]}"; do
    curl -sfL --retry 3 -o "src/${k}_raw$i.mp4" "${R[$i]}" &
    curl -sfL --retry 3 -o "src/${k}_vc$i.mp4" "${V[$i]}" &
  done
done < blocks.tsv
wait

# The voice change runs on a 720p proxy and keeps the timing, so its audio goes straight back
# onto the full-resolution picture.
while IFS=$'\t' read -r k _ raw _ cut _; do
  IFS='|' read -ra R <<< "$raw"
  for i in "${!R[@]}"; do
    [ -s "src/${k}_raw$i.mp4" ] && [ -s "src/${k}_vc$i.mp4" ] || { echo "missing clip $k"; exit 1; }
    ffmpeg -nostdin -loglevel error -i "src/${k}_raw$i.mp4" -i "src/${k}_vc$i.mp4" -map 0:v -map 1:a -c copy -shortest -y "src/${k}_$i.mp4"
  done
  if [ ${#R[@]} -eq 1 ]; then
    mv "src/${k}_0.mp4" "src/$k.mp4"
  else
    IFS='|' read -r a_end b_start b_end <<< "$cut"
    # The halves come from separate generations with different low-frequency room hum (mostly
    # 60-120 Hz); a low-cut on both keeps the background even across the join.
    x=0.125; off=$(python3 -c "print(round($a_end - $x, 3))"); lowcut="highpass=f=120,highpass=f=120"
    ffmpeg -nostdin -loglevel error -i "src/${k}_0.mp4" -i "src/${k}_1.mp4" -filter_complex \
      "[0:v]trim=0:$a_end,setpts=PTS-STARTPTS[va];[1:v]trim=$b_start:$b_end,setpts=PTS-STARTPTS[vb];[va][vb]xfade=transition=fade:duration=$x:offset=$off[v];
       [0:a]atrim=0:$a_end,asetpts=PTS-STARTPTS,aresample=48000,$lowcut[aa];[1:a]atrim=$b_start:$b_end,asetpts=PTS-STARTPTS,aresample=48000,$lowcut[ab];[aa][ab]acrossfade=d=$x[a]" \
      -map "[v]" -map "[a]" -c:v libx264 -preset slow -crf 12 -pix_fmt yuv420p -c:a pcm_s16le -y "src/$k.mkv"
  fi
done < blocks.tsv

gain(){ python3 - "$1" "$LUFS" <<'PY'
import re, subprocess, sys
out = subprocess.run(["ffmpeg", "-nostdin", "-i", sys.argv[1], "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])
print(round(float(sys.argv[2]) - i, 2))
PY
}
VENC=(-c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -r 24 -movflags +faststart)
AENC=(-c:a aac -b:a 192k -ar 48000 -ac 2)

echo "clips"
n=0
while IFS=$'\t' read -r k _ _ _ cut _; do
  n=$((n+1)); nn=$(printf %02d $n)
  f=src/$k.mp4; [ -s "$f" ] || f=src/$k.mkv
  case $cut in *'|'*) cut=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f");; esac
  g=$(gain "$f")
  ffmpeg -nostdin -loglevel error -i "$f" -t "$cut" \
    -af "volume=${g}dB,alimiter=limit=0.89:level=false,afade=t=out:st=$(python3 -c "print(round($cut - 0.08, 3))"):d=0.08" \
    "${VENC[@]}" "${AENC[@]}" -y "pkg/clips/${nn}_$k.mp4"
done < blocks.tsv

echo "contact sheet"
files=(pkg/clips/*.mp4); cols=$(( (${#files[@]} + 1) / 2 )); ins=(); i=0
for f in "${files[@]}"; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  ffmpeg -nostdin -loglevel error -ss "$(python3 -c "print(round($d*0.5,2))")" -i "$f" -frames:v 1 -vf "scale=180:-2" -y "cs_$i.png"
  ins+=(-i "cs_$i.png"); i=$((i+1))
done
if [ $((i % 2)) -eq 1 ]; then
  ffmpeg -nostdin -loglevel error -f lavfi -i "color=c=black:s=180x320" -frames:v 1 -y "cs_$i.png"; ins+=(-i "cs_$i.png"); i=$((i+1))
fi
top=""; bot=""
for ((j=0; j<cols; j++)); do top+="[$j]"; bot+="[$((j+cols))]"; done
ffmpeg -nostdin -loglevel error "${ins[@]}" -filter_complex "${top}hstack=$cols[t];${bot}hstack=$cols[b];[t][b]vstack" -q:v 3 -y pkg/contact_sheet.jpg

echo "readme"
HERE="$HERE" python3 - <<'PY'
import glob, os, subprocess
files = sorted(glob.glob("pkg/clips/*.mp4"))
rows = [l.rstrip("\n").split("\t") for l in open("blocks.tsv")]
dur = lambda f: float(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=duration", "-of", "csv=p=0", f]).decode())
length = {r[0]: dur(f) for r, f in zip(rows, files)}
name = {r[0]: os.path.basename(f) for r, f in zip(rows, files)}
hooks = [r[0] for r in rows if r[0].startswith("H")]
body = [r[0] for r in rows if r[0].startswith("B")]
total = sum(length[k] for k in body)
out = ["CHATEAUNEUF-DU-PAPE COUNTDOWN - SOMMELIER TO CAMERA (clips for edit)", "",
       "1080x1920 (9:16), 24 fps, H.264 + AAC 48 kHz stereo. One locked shot: the wine-shop seed frame, sommelier behind the marble counter.",
       "Headroom above him is left clear for the countdown clock. Voice: Callum (Higgsfield preset).",
       "Every clip is levelled to -16 LUFS with a -1 dB peak limiter. No music, no captions.", "",
       f"Each version = one hook, then {body[0]}-{body[-1]} in order. The body runs {total:.2f}s; with each hook: "
       + ", ".join(f"{h} {total + length[h]:.2f}s" for h in hooks) + ".", "",
       "CLIPS (clips/, cut tight to the speech)"]
for r in rows:
    out.append(f"  {name[r[0]]:12} {length[r[0]]:5.2f}s  {r[1]:17}  {r[5]}")
out += ["", "NOTES",
        "  - Every clip starts on the same frame as the seed and the camera never moves, so cuts between lines are near-seamless;",
        "    his head and hands shift a little during each line, so a B-roll cutaway or a small punch-in still helps at some joins.",
        "  - Clips are cut about 0.3s after the last word (0.9s on the last clip, so there is room to land the CTA)."]
notes = os.path.join(os.environ.get("HERE", "."), "sommelier-countdown-notes.txt")
if os.path.exists(notes):
    out += ["  - " + l.strip() for l in open(notes) if l.strip()]
open("pkg/README.txt", "w").write("\n".join(out) + "\n")
PY

echo "zip"
(cd pkg && zip -q -r -1 ../sommelier_countdown_clips.zip .)
ls -la pkg pkg/clips sommelier_countdown_clips.zip
