#!/usr/bin/env bash
# Scaranto Governo (Winedrops): green-screen presenter package, no B-roll.
# Builds the three hook versions as continuous green-screen tracks, each line as its own
# clip (tight and untrimmed), a contact sheet and a README with timecodes, then zips it all.
# Needs curl, ffmpeg/ffprobe, python3 and zip.  Usage: bash scaranto-governo-greenscreen-build.sh [workdir]
set -euo pipefail
W=${1:-./scaranto_greenscreen_build}
rm -rf "$W"; mkdir -p "$W"/src "$W"/pkg/{lines,lines_untrimmed,reference}
cd "$W"
G=https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip   # Higgsfield generations
M=https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip   # Higgsfield uploads
LUFS=-16

# key | section | voiced green-screen clip | re-greened video (B02/B07 only) | cut in s (speech end + pad) | line
cat > blocks.tsv <<EOF
H1	Hook 1	$G/hf_20261007_095509_2ab5ee83-318a-4840-8b47-9baa4303b8e0.mp4	-	3.72	This is the bottle with the best story on any dinner table.
H2	Hook 2	$G/hf_20261007_095511_0feffe8a-3076-4bcd-8dcc-7514ff3005db.mp4	-	5.30	Two critics gave this ninety-nine and one hundred points, but the style was illegal in Italy.
H3	Hook 3	$G/hf_20261007_095514_233ba7e4-a0fe-4b00-ab19-92f5a934d8d3.mp4	-	4.56	This wine exists because a few Tuscan families broke the rules.
B01	Gap	$G/hf_20261007_095740_e1895c87-240e-402f-be4f-d873abcb7ee0.mp4	-	5.95	Back in the seventies, Chianti law told Tuscan winemakers exactly which grapes they could use.
B02	Gap	$G/hf_20261007_095910_f62f818f-b12a-46ca-a056-2309a0594bec.mp4	$M/ee835294-95af-4bb5-a901-016c0fd57436.mp4	6.67	A few families planted Merlot and Cabernet anyway, and had to sell what they made as plain table wine.
B03	Stake + mechanism	$G/hf_20261007_095742_79bf447d-8e85-4c31-b6f1-d5ce3f6e59e7.mp4	-	9.89	Those table wines turned into Sassicaia and Tignanello. Collectors now pay well over fifty pounds a bottle for them, and the wine world gave them their own name: Super Tuscans.
B04	Revelation	$G/hf_20261007_095515_0c449be4-0b6e-4d19-afd4-d2181d99623f.mp4	-	9.96	Scaranto is Matteo Bernabei's project, made with his dad Franco, one of the best-known winemakers in Tuscany. They named this one Governo after an old Tuscan farmhouse trick.
B05	Revelation	$G/hf_20261007_095518_8924c62f-411b-488b-bdca-4213ffc4956b.mp4	-	9.71	Some of the grapes are left to dry, then go back into the wine, which makes it softer and rounder. After that it spends three months in French oak.
B06	Payoff + proof	$G/hf_20261007_151048_587999a4-f019-45e8-a12b-2fba2236885b.mp4	-	6.96	Then the critics tasted it. Luca Maroni gave it ninety-nine. The Italian Wine Guy gave it a perfect one hundred.
B07	Payoff + proof	$G/hf_20261007_100405_9680243c-977a-4972-8701-863ba7e7a6f1.mp4	$M/21a7e783-1c10-474a-81e3-afab8806be28.mp4	6.79	In the glass you get black cherry, dried rose, a bit of tobacco, and a finish that keeps going.
B08	CTA	$G/hf_20261007_095523_fce0af41-4e63-4d16-bb83-66f24b1d3594.mp4	-	7.96	And Winedrops will do a case of six for sixty-nine pounds ninety-nine, so under twelve pounds each. That's seventy percent off its normal price.
B09	CTA	$G/hf_20261007_095525_48147e82-d2a8-4db4-92c3-ba2c8038f70a.mp4	-	5.96	Get on the app, and tell people its story over a nice glass at dinner.
EOF

echo "download"
while IFS=$'\t' read -r k _ talk regreen _ _; do
  curl -sfL --retry 3 -o "src/${k}_talk.mp4" "$talk" &
  [ "$regreen" = "-" ] || curl -sfL --retry 3 -o "src/${k}_regreen.mp4" "$regreen" &
done < blocks.tsv
curl -sfL --retry 3 -o pkg/reference/greenscreen_reference.png "$G/hf_20261007_094818_5878666a-29e4-4505-8e0c-ed0eb989d9e7.png" &
wait

# B02 and B07 were generated on an olive green; their re-greened video (same frames, keyed onto
# the #029D3A green the other ten clips use) is muxed with the original voiced audio.
while IFS=$'\t' read -r k _ _ regreen _ _; do
  if [ "$regreen" = "-" ]; then
    mv "src/${k}_talk.mp4" "src/$k.mp4"
  else
    ffmpeg -nostdin -loglevel error -i "src/${k}_regreen.mp4" -i "src/${k}_talk.mp4" -map 0:v -map 1:a -c copy -shortest -y "src/$k.mp4"
  fi
done < blocks.tsv

# Per-clip gain so every line sits at the same loudness.
gain(){ python3 - "$1" "$LUFS" <<'PY'
import re, subprocess, sys
out = subprocess.run(["ffmpeg", "-nostdin", "-i", sys.argv[1], "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", out)[-1])
print(round(float(sys.argv[2]) - i, 2))
PY
}
VENC=(-c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -r 24 -movflags +faststart)
AENC=(-c:a aac -b:a 192k -ar 48000 -ac 2)

echo "lines"
n=0
: > gains.txt
while IFS=$'\t' read -r k _ _ _ cut _; do
  n=$((n+1)); nn=$(printf %02d $n); g=$(gain "src/$k.mp4"); echo "$k $g" >> gains.txt
  af="volume=${g}dB,alimiter=limit=0.89:level=false"
  ffmpeg -nostdin -loglevel error -i "src/$k.mp4" -t "$cut" -af "$af,afade=t=out:st=$(python3 -c "print($cut-0.08)"):d=0.08" "${VENC[@]}" "${AENC[@]}" -y "pkg/lines/${nn}_$k.mp4"
  ffmpeg -nostdin -loglevel error -i "src/$k.mp4" -af "$af" "${VENC[@]}" "${AENC[@]}" -y "pkg/lines_untrimmed/${nn}_$k.mp4"
done < blocks.tsv

echo "full versions"
version(){ # version HOOK OUTNAME
  local ins=() fc="" i=0 k cut g
  for k in "$1" B01 B02 B03 B04 B05 B06 B07 B08 B09; do
    cut=$(awk -F'\t' -v k="$k" '$1==k{print $5}' blocks.tsv); g=$(awk -v k="$k" '$1==k{print $2}' gains.txt)
    ins+=(-t "$cut" -i "src/$k.mp4")
    fc+="[$i:v]fps=24,format=yuv420p,setsar=1[v$i];[$i:a]volume=${g}dB,alimiter=limit=0.89:level=false,afade=t=out:st=$(python3 -c "print($cut-0.08)"):d=0.08,aresample=48000,aformat=channel_layouts=stereo[a$i];"
    i=$((i+1))
  done
  for ((j=0; j<i; j++)); do fc+="[v$j][a$j]"; done
  fc+="concat=n=$i:v=1:a=1[v][a]"
  ffmpeg -nostdin -loglevel error "${ins[@]}" -filter_complex "$fc" -map "[v]" -map "[a]" "${VENC[@]}" "${AENC[@]}" -y "pkg/$2"
}
version H1 scaranto_greenscreen_hook1_best_story.mp4
version H2 scaranto_greenscreen_hook2_critics_illegal.mp4
version H3 scaranto_greenscreen_hook3_broke_the_rules.mp4

echo "contact sheet"
i=0; ins=()
for f in pkg/lines/*.mp4; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  ffmpeg -nostdin -loglevel error -ss "$(python3 -c "print(round($d*0.5,2))")" -i "$f" -frames:v 1 -vf "scale=180:-2" -y "cs_$i.png"
  ins+=(-i "cs_$i.png"); i=$((i+1))
done
ffmpeg -nostdin -loglevel error "${ins[@]}" -filter_complex "[0][1][2][3][4][5]hstack=6[t];[6][7][8][9][10][11]hstack=6[b];[t][b]vstack" -q:v 3 -y pkg/contact_sheet.jpg

echo "readme"
python3 - <<'PY'
import subprocess, glob
rows = [l.rstrip("\n").split("\t") for l in open("blocks.tsv")]
def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=duration", "-of", "csv=p=0", f]).decode())
files = sorted(glob.glob("pkg/lines/*.mp4"))
length = {r[0]: dur(f) for r, f in zip(rows, files)}
line = {r[0]: r[5] for r in rows}
section = {r[0]: r[1] for r in rows}
def tc(s):
    return f"{int(s // 60):02d}:{s % 60:05.2f}"
ost = {"B04": "On-screen text cue: 'Hand-picked' in", "B05": "On-screen text cue: 'Dried grapes' in; 'French oak' at 'After that' (+6.75s)"}
out = ["SCARANTO GOVERNO - GREEN-SCREEN PRESENTER (for edit)", "",
       "720x1280 (9:16), 24 fps, H.264 + AAC 48 kHz stereo. Background is flat chroma green, about RGB 2,157,57 (#029D39).",
       "Voice: Callum (Higgsfield preset). Every line is levelled to -16 LUFS with a -1 dB peak limiter. No music, no captions.", ""]
for hook, name in [("H1", "scaranto_greenscreen_hook1_best_story.mp4"), ("H2", "scaranto_greenscreen_hook2_critics_illegal.mp4"), ("H3", "scaranto_greenscreen_hook3_broke_the_rules.mp4")]:
    t, total = 0.0, dur("pkg/" + name)
    out.append(f"{name}  ({total:.2f}s)")
    for k in [hook] + [f"B0{i}" for i in range(1, 10)]:
        cue = f"   [{ost[k]}]" if k in ost else ""
        out.append(f"  {tc(t)}  {k:3}  {section[k]:17}  {line[k]}{cue}")
        t += length[k]
    out.append(f"  {tc(t)}  end")
    out.append("")
out += ["FOLDERS",
        "  lines/            each line on its own, cut tight to the speech (these are what the full versions are built from)",
        "  lines_untrimmed/  the same lines with the full generated tail (a second or so of him holding a look) for handles",
        "  reference/        the green-screen still the clips were generated from",
        "  contact_sheet.jpg one frame per line (top: H1 H2 H3 B01 B02 B03, bottom: B04-B09)", "",
        "NOTES",
        "  - Each line is a separate generation, so there is a small jump in pose at every cut. Cover the cuts with B-roll or a punch-in.",
        "  - B02 and B07 were generated on an olive green and re-keyed onto the same green as the rest, so one key setting covers the whole track.",
        "  - The voiceover runs about 69s plus the hook, longer than the 45s in the brief. Speech was not sped up.",
        "  - The 100-point score is credited to The Italian Wine Guy. Check both scores against the vintage being sold."]
open("pkg/README.txt", "w").write("\n".join(out) + "\n")
PY

echo "zip"
(cd pkg && zip -q -r -1 ../scaranto_governo_greenscreen.zip .)
ls -la pkg scaranto_governo_greenscreen.zip
