#!/usr/bin/env bash
# Package voiced green-screen presenter clips for an editor (no B-roll).
#
#   bash greenscreen-package.sh BLOCKS.tsv PREFIX "TITLE" [NOTES.txt] [WORKDIR]
#
# BLOCKS.tsv, one line per clip, tab-separated, in timeline order:
#   key  section  voiced_clip_url  regreened_video_url|-  cut_seconds  spoken_line  [on-screen text cue]
# Keys starting with H are hooks; keys starting with B are the shared body, in file order.
# It writes each line trimmed and untrimmed, a contact sheet and a README, then zips it all
# to WORKDIR/PREFIX.zip. Unless CLIPS_ONLY=1 is set, it also builds PREFIX_hookN.mp4 for every
# hook (that hook + the whole body), and the README lists timecodes for each of those versions.
# Every line is levelled to -16 LUFS. A regreened URL replaces that clip's video and keeps
# its voiced audio. Use it when a generation landed on a different shade of green.
# Needs curl, ffmpeg/ffprobe, python3 and zip.
set -euo pipefail
BLOCKS=$(realpath "$1"); PREFIX=$2; TITLE=$3
NOTES=$( [ -n "${4:-}" ] && realpath "$4" || true )
W=${5:-./${PREFIX}_build}
LUFS=-16
rm -rf "$W"; mkdir -p "$W"/src "$W"/pkg/{lines,lines_untrimmed}
cd "$W"
grep -v '^\s*$' "$BLOCKS" > blocks.tsv

echo "download"
while IFS=$'\t' read -r k _ talk regreen _; do
  curl -sfL --retry 3 -o "src/${k}_talk.mp4" "$talk" &
  [ "$regreen" = "-" ] || curl -sfL --retry 3 -o "src/${k}_regreen.mp4" "$regreen" &
done < blocks.tsv
wait
while IFS=$'\t' read -r k _ _ regreen _; do
  [ -s "src/${k}_talk.mp4" ] || { echo "missing clip $k"; exit 1; }
  if [ "$regreen" = "-" ]; then
    mv "src/${k}_talk.mp4" "src/$k.mp4"
  else
    ffmpeg -nostdin -loglevel error -i "src/${k}_regreen.mp4" -i "src/${k}_talk.mp4" -map 0:v -map 1:a -c copy -shortest -y "src/$k.mp4"
  fi
done < blocks.tsv

gain(){ python3 - "$1" "$LUFS" <<'PY'
import re, subprocess, sys
out = subprocess.run(["ffmpeg", "-nostdin", "-i", sys.argv[1], "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])
print(round(float(sys.argv[2]) - i, 2))
PY
}
fade_at(){ python3 -c "print(round($1 - 0.08, 3))"; }
VENC=(-c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -r 24 -movflags +faststart)
AENC=(-c:a aac -b:a 192k -ar 48000 -ac 2)

echo "lines"
n=0; : > gains.txt
while IFS=$'\t' read -r k _ _ _ cut _; do
  n=$((n+1)); nn=$(printf %02d $n); g=$(gain "src/$k.mp4"); echo "$k $g" >> gains.txt
  af="volume=${g}dB,alimiter=limit=0.89:level=false"
  ffmpeg -nostdin -loglevel error -i "src/$k.mp4" -t "$cut" -af "$af,afade=t=out:st=$(fade_at "$cut"):d=0.08" "${VENC[@]}" "${AENC[@]}" -y "pkg/lines/${nn}_$k.mp4"
  ffmpeg -nostdin -loglevel error -i "src/$k.mp4" -af "$af" "${VENC[@]}" "${AENC[@]}" -y "pkg/lines_untrimmed/${nn}_$k.mp4"
done < blocks.tsv

echo "full versions"
BODY=$(awk -F'\t' '$1 ~ /^B/ {print $1}' blocks.tsv)
HOOKS=$(awk -F'\t' '$1 ~ /^H/ {print $1}' blocks.tsv)
version(){ # version HOOK OUTFILE
  local ins=() fc="" i=0 k cut g
  for k in "$1" $BODY; do
    cut=$(awk -F'\t' -v k="$k" '$1==k{print $5}' blocks.tsv); g=$(awk -v k="$k" '$1==k{print $2}' gains.txt)
    ins+=(-t "$cut" -i "src/$k.mp4")
    fc+="[$i:v]fps=24,format=yuv420p,setsar=1[v$i];[$i:a]volume=${g}dB,alimiter=limit=0.89:level=false,afade=t=out:st=$(fade_at "$cut"):d=0.08,aresample=48000,aformat=channel_layouts=stereo[a$i];"
    i=$((i+1))
  done
  for ((j=0; j<i; j++)); do fc+="[v$j][a$j]"; done
  fc+="concat=n=$i:v=1:a=1[v][a]"
  ffmpeg -nostdin -loglevel error "${ins[@]}" -filter_complex "$fc" -map "[v]" -map "[a]" "${VENC[@]}" "${AENC[@]}" -y "pkg/$2"
}
if [ "${CLIPS_ONLY:-0}" != 1 ]; then
  h=0
  for k in $HOOKS; do h=$((h+1)); version "$k" "${PREFIX}_hook${h}.mp4" & done
  wait
fi

echo "contact sheet"
files=(pkg/lines/*.mp4); cols=$(( (${#files[@]} + 1) / 2 )); ins=(); i=0
for f in "${files[@]}"; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  ffmpeg -nostdin -loglevel error -ss "$(python3 -c "print(round($d*0.5,2))")" -i "$f" -frames:v 1 -vf "scale=180:-2" -y "cs_$i.png"
  ins+=(-i "cs_$i.png"); i=$((i+1))
done
if [ $((i % 2)) -eq 1 ]; then  # pad to an even count with a blank tile
  ffmpeg -nostdin -loglevel error -f lavfi -i "color=c=black:s=180x320" -frames:v 1 -y "cs_$i.png"; ins+=(-i "cs_$i.png"); i=$((i+1))
fi
top=""; bot=""
for ((j=0; j<cols; j++)); do top+="[$j]"; bot+="[$((j+cols))]"; done
ffmpeg -nostdin -loglevel error "${ins[@]}" -filter_complex "${top}hstack=$cols[t];${bot}hstack=$cols[b];[t][b]vstack" -q:v 3 -y pkg/contact_sheet.jpg

echo "readme"
python3 - "$PREFIX" "$TITLE" "${NOTES:-}" "${CLIPS_ONLY:-0}" <<'PY'
import glob, os, subprocess, sys
prefix, title, notes, clips_only = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] == "1"
files = sorted(glob.glob("pkg/lines/*.mp4"))
rows = [l.rstrip("\n").split("\t") for l in open("blocks.tsv")]
def dur(f, stream=True):
    args = ["-select_streams", "v:0", "-show_entries", "stream=duration"] if stream else ["-show_entries", "format=duration"]
    return float(subprocess.check_output(["ffprobe", "-v", "error", *args, "-of", "csv=p=0", f]).decode())
length = {r[0]: dur(f) for r, f in zip(rows, files)}
name = {r[0]: os.path.basename(f) for r, f in zip(rows, files)}
info = {r[0]: r for r in rows}
hooks = [r[0] for r in rows if r[0].startswith("H")]
body = [r[0] for r in rows if r[0].startswith("B")]
tc = lambda s: f"{int(s // 60):02d}:{s % 60:05.2f}"
out = [title, "",
       "720x1280 (9:16), 24 fps, H.264 + AAC 48 kHz stereo, on a flat chroma green (about RGB 2,157,57 / #029D39).",
       "Voice: Callum (Higgsfield preset). Every line is levelled to -16 LUFS with a -1 dB peak limiter. No music, no captions.", ""]
cue = lambda r: f"   [on-screen: {r[6]}]" if len(r) > 6 and r[6] else ""
if clips_only:
    total = sum(length[k] for k in body)
    out += [f"Each version = one hook, then {body[0]}-{body[-1]} in order. The body runs {total:.2f}s; with each hook: "
            + ", ".join(f"{h} {total + length[h]:.2f}s" for h in hooks) + ".", "",
            "CLIPS (lines/, cut tight to the speech)"]
    for k in hooks + body:
        r = info[k]
        out.append(f"  {name[k]:12} {length[k]:5.2f}s  {r[1]:17}  {r[5]}{cue(r)}")
    out.append("")
for n, h in enumerate([] if clips_only else hooks, 1):
    fname = f"{prefix}_hook{n}.mp4"
    out.append(f"{fname}  ({dur('pkg/' + fname, stream=False):.2f}s)")
    t = 0.0
    for k in [h] + body:
        r = info[k]
        out.append(f"  {tc(t)}  {k:3}  {r[1]:17}  {r[5]}{cue(r)}")
        t += length[k]
    out += [f"  {tc(t)}  end", ""]
out += ["FOLDERS",
        "  lines/            each line on its own, cut tight to the speech",
        "  lines_untrimmed/  the same lines with the full generated tail (a second or so of him holding a look) for handles",
        "  contact_sheet.jpg one frame per line, in timeline order", "",
        "NOTES",
        "  - Each line is a separate generation, so his pose shifts slightly at every cut. Cover the cuts with B-roll or a punch-in."]
regreened = [r[0] for r in rows if r[3] != "-"]
if regreened:
    verb = "was" if len(regreened) == 1 else "were"
    out.append(f"  - {', '.join(regreened)} came out on an olive green and {verb} re-keyed onto the same green as the rest, so one key setting covers the whole track.")
if notes:
    out += ["  - " + l.strip() for l in open(notes) if l.strip()]
open("pkg/README.txt", "w").write("\n".join(out) + "\n")
PY

echo "zip"
(cd pkg && zip -q -r -1 "../${PREFIX}.zip" .)
ls -la pkg "${PREFIX}.zip"
