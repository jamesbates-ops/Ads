#!/usr/bin/env bash
# Scaranto Governo green-screen ad: assemble 3 hook variants + package.
set -uo pipefail
W=/home/user/build
rm -rf "$W"; mkdir -p "$W"/{src,blk,talk,out} "$W"/pkg/{greenscreen,broll,reference}
cd "$W"
U=https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip
FONT=/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf
COMP="$HF_WORKFLOWS/narration/scripts/presenter_composite.sh"
log(){ echo "[$(date +%T)] $*"; }
die(){ log "FATAL: $*"; echo FAIL > "$W/status.txt"; exit 1; }
chk(){ grep -qs FAIL "$W/status.txt" && { log "aborting after failed step"; exit 1; }; return 0; }
dur(){ ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }

cat > talks.txt <<'EOF'
H1 hf_20261007_095509_2ab5ee83-318a-4840-8b47-9baa4303b8e0
H2 hf_20261007_095511_0feffe8a-3076-4bcd-8dcc-7514ff3005db
H3 hf_20261007_095514_233ba7e4-a0fe-4b00-ab19-92f5a934d8d3
B01 hf_20261007_095740_e1895c87-240e-402f-be4f-d873abcb7ee0
B02 hf_20261007_095910_f62f818f-b12a-46ca-a056-2309a0594bec
B03 hf_20261007_095742_79bf447d-8e85-4c31-b6f1-d5ce3f6e59e7
B04 hf_20261007_095515_0c449be4-0b6e-4d19-afd4-d2181d99623f
B05 hf_20261007_095518_8924c62f-411b-488b-bdca-4213ffc4956b
B06 hf_20261007_095521_4b53ced3-0bf1-43bd-acae-c9a7c9bacf7c
B07 hf_20261007_100405_9680243c-977a-4972-8701-863ba7e7a6f1
B08 hf_20261007_095523_fce0af41-4e63-4d16-bb83-66f24b1d3594
B09 hf_20261007_095525_48147e82-d2a8-4db4-92c3-ba2c8038f70a
EOF
cat > brolls.txt <<'EOF'
R00_dinner_table hf_20261007_095251_9e99fae2-13d2-4e54-ac5c-02a13f1ff507
R01_tuscan_hills hf_20261007_095251_75eb2adb-344e-48da-8c65-77b30535eaad
R02_table_wine_carafe hf_20261007_095346_3ad6a41d-0616-49ae-becb-2915c9a69712
R03_collector_cellar hf_20261007_095346_865674ed-2697-4ca3-8878-ebfd44b0dd28
R04_hand_picking hf_20261007_095251_50e8c388-c113-4727-a269-345350eb62d3
R05_drying_grapes hf_20261007_095738_43e3cd62-48b2-4288-ab35-f1f597088fe1
R06_french_oak hf_20261007_095252_a3c4cbbc-f7a7-489d-9a00-28dce1c4b64f
R07_critic_tasting hf_20261007_095346_2402dbf5-343e-4f22-a85c-886189eef253
R08_pour_tasting_notes hf_20261007_095251_bd1b794a-d78a-4399-be4b-f8a4482788ba
R09_case_of_six hf_20261007_095251_57330cfe-6afa-4288-ad0b-36ce0caa38c7
R10_dinner_party hf_20261007_095252_5b3dfe06-2cad-4849-85a2-8a0bf997d3cc
EOF

log "download"
while read -r k f; do curl -sfL --retry 3 -o "src/$k.mp4" "$U/$f.mp4" & done < talks.txt
while read -r k f; do curl -sfL --retry 3 -o "src/$k.mp4" "$U/$f.mp4" & done < brolls.txt
curl -sfL --retry 3 -o pkg/reference/greenscreen_reference.png "$U/hf_20261007_094818_5878666a-29e4-4505-8e0c-ed0eb989d9e7.png" &
curl -sfL --retry 3 -o pkg/reference/seed_original.png "https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/5f67d9d3-1f39-49b3-ae68-daa00a273b5d.png" &
wait
for k in $(cut -d' ' -f1 talks.txt brolls.txt); do [ -s "src/$k.mp4" ] || die "missing src/$k.mp4"; done
rm -f status.txt

log "measure speech"
python3 - <<'EOF' || die "whisper timing failed"
import subprocess
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
keys = "H1 H2 H3 B01 B02 B03 B04 B05 B06 B07 B08 B09".split()
with open("timings.env", "w") as out, open("speech_report.txt", "w") as rep:
    for k in keys:
        f = f"src/{k}.mp4"
        D = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())
        segs, _ = m.transcribe(f, word_timestamps=True, language="en")
        words = [w for s in segs for w in s.words]
        end = words[-1].end
        pad = 0.30 if k.startswith("H") else (0.9 if k == "B09" else 0.35)
        L = round(min(D - 0.04, end + pad), 2)
        out.write(f"L_{k}={L}\n")
        if k == "B05":
            sp = [w.start for w in words if w.word.strip().lower().startswith("after")]
            out.write(f"SPLIT_B05={round(sp[0] - 0.15 if sp else L * 0.62, 2)}\n")
        rep.write(f"{k} clip={D:.2f}s speech_end={end:.2f}s cut={L:.2f}s | {' '.join(w.word.strip() for w in words)}\n")
EOF
cat speech_report.txt timings.env
# shellcheck disable=SC1091
source timings.env

GRADE70="curves=preset=vintage,eq=saturation=0.8:contrast=1.04,noise=alls=12:allf=t+u,vignette=angle=PI/5"
# make_blk OUT SRC SECONDS [GRADE]: B-roll trimmed to SECONDS, slowed if it is too short.
make_blk(){
  local out=$1 src=$2 L=$3 grade=${4:-} bd f
  bd=$(dur "$src")
  f=$(python3 -c "print(max(1.0, ($L + 0.1) / $bd))")
  ffmpeg -nostdin -loglevel error -i "$src" -an \
    -vf "setpts=${f}*PTS,${grade:+$grade,}scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=24,format=yuv420p" \
    -t "$L" -c:v libx264 -preset veryfast -crf 16 -y "$out" || die "blk $out"
}
# make_talk KEY: voiced green-screen clip trimmed to its speech, short audio fade-out.
make_talk(){
  local k=$1 L v
  v="L_$1"; L=${!v}
  ffmpeg -nostdin -loglevel error -i "src/$k.mp4" -t "$L" \
    -af "afade=t=out:st=$(python3 -c "print($L - 0.08)"):d=0.08" \
    -c:v libx264 -preset veryfast -crf 16 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -y "talk/$k.mp4" || die "talk $k"
}

log "prep blocks"
for k in H1 H2 H3 B01 B02 B03 B04 B05 B06 B07 B08 B09; do make_talk "$k" & done; wait; chk
make_blk blk/H1.mp4 src/R00_dinner_table.mp4 "$L_H1" &
make_blk blk/H2.mp4 src/R00_dinner_table.mp4 "$L_H2" &
make_blk blk/H3.mp4 src/R00_dinner_table.mp4 "$L_H3" &
make_blk blk/B01.mp4 src/R01_tuscan_hills.mp4 "$L_B01" "$GRADE70" &
make_blk blk/B02.mp4 src/R02_table_wine_carafe.mp4 "$L_B02" "$GRADE70" &
make_blk blk/B03.mp4 src/R03_collector_cellar.mp4 "$L_B03" &
wait; chk
make_blk blk/B04.mp4 src/R04_hand_picking.mp4 "$L_B04" &
make_blk blk/B05a.mp4 src/R05_drying_grapes.mp4 "$SPLIT_B05" &
make_blk blk/B05b.mp4 src/R06_french_oak.mp4 "$(python3 -c "print(round($L_B05 - $SPLIT_B05, 2))")" &
make_blk blk/B06.mp4 src/R07_critic_tasting.mp4 "$L_B06" &
make_blk blk/B07.mp4 src/R08_pour_tasting_notes.mp4 "$L_B07" &
make_blk blk/B08.mp4 src/R09_case_of_six.mp4 "$L_B08" &
make_blk blk/B09.mp4 src/R10_dinner_party.mp4 "$L_B09" &
wait; chk
printf "file 'B05a.mp4'\nfile 'B05b.mp4'\n" > blk/b05.txt
ffmpeg -nostdin -loglevel error -f concat -safe 0 -i blk/b05.txt -c copy -y blk/B05.mp4 || die "B05 join"

log "composite"
comp(){
  bash "$COMP" "blk/$1.mp4" "talk/$1.mp4" "out/$1.mp4" --style cutout --pos br --cut-w-frac 1.0 --cut-h-frac 0.6 > "out/$1.log" 2>&1
  grep -q '"result":"PASS"' "out/$1.mp4.qc.json" 2>/dev/null || { cat "out/$1.log"; die "composite QC $1"; }
}
for g in "H1 H2 H3" "B01 B02 B03" "B04 B05 B06" "B07 B08 B09"; do
  for k in $g; do comp "$k" & done; wait; chk
done
for k in H1 H2 H3 B01 B02 B03 B04 B05 B06 B07 B08 B09; do [ -s "out/$k.mp4" ] || die "no out/$k.mp4"; done

log "on-screen text"
txt(){ # txt TEXT Y START
  echo "drawtext=fontfile=$FONT:text='$1':fontsize=66:fontcolor=white:box=1:boxcolor=0x5a0f1e@0.88:boxborderw=24:x=90:y=$2:alpha='if(lt(t,$3),0,min(1,(t-$3)/0.3))'"
}
ffmpeg -nostdin -loglevel error -i out/B04.mp4 -vf "$(txt 'Hand-picked' 300 0.6)" \
  -c:v libx264 -preset veryfast -crf 16 -pix_fmt yuv420p -c:a copy -y out/B04_ost.mp4 || die "ost B04"
ffmpeg -nostdin -loglevel error -i out/B05.mp4 -vf "$(txt 'Hand-picked' 300 0),$(txt 'Dried grapes' 420 0.4),$(txt 'French oak' 540 "$SPLIT_B05")" \
  -c:v libx264 -preset veryfast -crf 16 -pix_fmt yuv420p -c:a copy -y out/B05_ost.mp4 || die "ost B05"

log "final cuts"
BODY="out/B01.mp4 out/B02.mp4 out/B03.mp4 out/B04_ost.mp4 out/B05_ost.mp4 out/B06.mp4 out/B07.mp4 out/B08.mp4 out/B09.mp4"
final(){ # final HOOK OUTNAME
  local ins=() fc="" i=0 f
  for f in "out/$1.mp4" $BODY; do
    ins+=(-i "$f")
    fc+="[$i:v]fps=24,format=yuv420p,setsar=1[v$i];[$i:a]aresample=48000,aformat=channel_layouts=stereo[a$i];"
    i=$((i+1))
  done
  for ((j=0;j<i;j++)); do fc+="[v$j][a$j]"; done
  fc+="concat=n=$i:v=1:a=1[v][a]"
  ffmpeg -nostdin -loglevel error "${ins[@]}" -filter_complex "$fc" -map "[v]" -map "[a]" \
    -c:v libx264 -preset fast -crf 19 -profile:v high -pix_fmt yuv420p -r 24 \
    -c:a aac -b:a 192k -ar 48000 -movflags +faststart -y "pkg/$2" || die "final $2"
}
final H1 scaranto_hook1_best_story.mp4 &
final H2 scaranto_hook2_critics_illegal.mp4 &
final H3 scaranto_hook3_broke_the_rules.mp4 &
wait; chk

log "green-screen deliverables"
n=0
for k in H1 H2 H3 B01 B02 B03 B04 B05 B06 B07 B08 B09; do
  n=$((n+1)); cp "talk/$k.mp4" "pkg/greenscreen/$(printf %02d $n)_$k.mp4"
done
printf "file '%s'\n" $(for k in B01 B02 B03 B04 B05 B06 B07 B08 B09; do echo "$W/talk/$k.mp4"; done) > gs_body.txt
ffmpeg -nostdin -loglevel error -f concat -safe 0 -i gs_body.txt -c copy -y pkg/greenscreen/greenscreen_body_track_B01-B09.mp4 || die "gs body"
for k in $(cut -d' ' -f1 brolls.txt); do cp "src/$k.mp4" "pkg/broll/$k.mp4"; done

log "contact sheet + QC"
i=0; ins=(); fc=""
for k in H1 H2 H3 B01 B02 B03 B04_ost B05_ost B06 B07 B08 B09; do
  d=$(dur "out/$k.mp4"); t=$(python3 -c "print(round($d*0.55,2))")
  ffmpeg -nostdin -loglevel error -ss "$t" -i "out/$k.mp4" -frames:v 1 -vf "scale=270:-2" -y "cs_$i.png"
  ins+=(-i "cs_$i.png"); i=$((i+1))
done
ffmpeg -nostdin -loglevel error "${ins[@]}" -filter_complex "[0][1][2][3][4][5]hstack=6[t];[6][7][8][9][10][11]hstack=6[b];[t][b]vstack" -q:v 3 -y pkg/contact_sheet.jpg || die "contact sheet"
ffmpeg -nostdin -loglevel error -i pkg/contact_sheet.jpg -vf scale=1080:-2 -q:v 5 -y contact_small.jpg
{
  for f in pkg/*.mp4; do echo "$f $(ffprobe -v error -show_entries format=duration:stream=codec_type,width,height -of csv=p=0 "$f" | tr '\n' ' ')"; done
  cat speech_report.txt
} > qc.txt
python3 - <<'EOF' >> qc.txt
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8")
segs, _ = m.transcribe("pkg/scaranto_hook1_best_story.mp4", language="en")
print("FINAL HOOK1 TRANSCRIPT:", " ".join(s.text.strip() for s in segs))
EOF

log "readme + zip"
python3 - <<'EOF'
import re
L = dict(re.findall(r"L_(\w+)=([\d.]+)", open("timings.env").read()))
body = sum(float(L[k]) for k in "B01 B02 B03 B04 B05 B06 B07 B08 B09".split())
lines = {
 "H1": "This is the bottle with the best story on any dinner table.",
 "H2": "Two critics gave this ninety-nine and one hundred points, but the style was illegal in Italy.",
 "H3": "This wine exists because a few Tuscan families broke the rules.",
 "B01": "Back in the seventies, Chianti law told Tuscan winemakers exactly which grapes they could use.",
 "B02": "A few families planted Merlot and Cabernet anyway, and had to sell what they made as plain table wine.",
 "B03": "Those table wines turned into Sassicaia and Tignanello. Collectors now pay well over fifty pounds a bottle for them, and the wine world gave them their own name: Super Tuscans.",
 "B04": "Scaranto is Matteo Bernabei's project, made with his dad Franco, one of the best-known winemakers in Tuscany. They named this one Governo after an old Tuscan farmhouse trick.",
 "B05": "Some of the grapes are left to dry, then go back into the wine, which makes it softer and rounder. After that it spends three months in French oak.",
 "B06": "Then the critics tasted it. Luca Maroni gave it ninety-nine. Cosimo Dell'Anna gave it a perfect one hundred.",
 "B07": "In the glass you get black cherry, dried rose, a bit of tobacco, and a finish that keeps going.",
 "B08": "And Winedrops will do a case of six for sixty-nine pounds ninety-nine, so under twelve pounds each. That's seventy percent off its normal price.",
 "B09": "Get on the app, and tell people its story over a nice glass at dinner.",
}
broll = {"H1":"R00","H2":"R00","H3":"R00","B01":"R01 (70s film grade)","B02":"R02 (70s film grade)","B03":"R03","B04":"R04","B05":"R05 then R06","B06":"R07","B07":"R08","B08":"R09","B09":"R10"}
ost = {"B04":"Hand-picked","B05":"Hand-picked / Dried grapes / French oak"}
out = ["SCARANTO GOVERNO - GREEN-SCREEN AD (Winedrops)", "", "Format: 1080x1920 (9:16), 24 fps, H.264/AAC. Presenter keyed bottom-right over full-frame B-roll.",
       "Voice: Callum (Higgsfield preset 858499d9-fef5-40e1-bc29-b4dc661dc283), applied to every clip with voice_change.", "",
       "FINAL CUTS (hook + shared body)"]
for h, name in [("H1","scaranto_hook1_best_story.mp4"),("H2","scaranto_hook2_critics_illegal.mp4"),("H3","scaranto_hook3_broke_the_rules.mp4")]:
    out.append(f"  {name}: {float(L[h]) + body:.1f}s")
out += ["", "TIMELINE (block / length / B-roll / on-screen text / line)"]
for k in lines:
    out.append(f"  {k:4} {float(L[k]):5.2f}s  {broll[k]:22} {ost.get(k,''):40} {lines[k]}")
out += ["", "FOLDERS",
 "  greenscreen/  voiced green-screen presenter clips, trimmed to the cut (720x1280), plus the B01-B09 body as one track",
 "  broll/        untrimmed B-roll clips (1080x1920, silent)",
 "  reference/    original seed photo and the green-screen identity still the clips were generated from",
 "  contact_sheet.jpg  one frame per block (top: hooks 1-3, B01-B03; bottom: B04-B09)", "",
 "NOTES",
 "  - No music bed (none requested). Speech is normalised to about -16 LUFS per block.",
 "  - B-roll bottles have blank labels on purpose. Swap in a real Scaranto Governo packshot for the hook and CTA if you have one.",
 "  - The 100-point critic (Cosimo Dell'Anna) was filled in from retailer listings for the 2020 vintage. Check the scores against the vintage Winedrops is selling before this runs.",
]
open("pkg/README.txt", "w").write("\n".join(out) + "\n")
EOF
cp qc.txt pkg/qc_report.txt
(cd pkg && zip -q -r -1 ../scaranto_governo_greenscreen_ad.zip .) || die "zip"
ls -la pkg pkg/* scaranto_governo_greenscreen_ad.zip

log "upload"
put(){ # put FILE CONTENT_TYPE URL
  local code
  code=$(curl -sS -o /dev/null -w "%{http_code}" -X PUT -H "Content-Type: $2" -H "If-None-Match: *" --upload-file "$1" "$3")
  echo "$1 $code" >> upload_status.txt
}
: > upload_status.txt
source /home/user/urls.env
put pkg/scaranto_hook1_best_story.mp4 video/mp4 "$UP_H1" &
put pkg/scaranto_hook2_critics_illegal.mp4 video/mp4 "$UP_H2" &
put pkg/scaranto_hook3_broke_the_rules.mp4 video/mp4 "$UP_H3" &
put pkg/contact_sheet.jpg image/jpeg "$UP_CS" &
wait
put scaranto_governo_greenscreen_ad.zip application/octet-stream "$UP_ZIP"
cat upload_status.txt
log "done"
echo DONE > status.txt
