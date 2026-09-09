import os,sys,json,subprocess,math
from PIL import Image,ImageDraw,ImageFont
W,H=1080,1920
B="https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/"
B2="https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/"
SRC={"h1":"hf_20260909_085126_676ef5db-0e0a-4f0d-a92c-c27486f299fe.mp4","h2":"hf_20260909_085126_64f641ca-6ed3-4418-b29f-5ae11f7497ab.mp4","h3":"hf_20260909_085126_46dc82a8-f166-4809-a1dd-0f40c8d67668.mp4","h4":"hf_20260909_085126_9d0e9b11-3db4-4dd9-b89f-3627ec57bc4b.mp4","bodyA":"hf_20260909_085127_a3b25f78-066f-4939-a7f2-f62141a5b961.mp4","bodyB1":"hf_20260909_085127_737c066e-bfaf-4f21-8a34-aa445169194e.mp4","bodyB2":"hf_20260909_085126_ec1123bc-1ada-4a61-9437-f8b2f50a15cf.mp4","v51":"hf_20260909_083251_857a1705-9f37-43e3-8d07-5253b568bdce.mp4","v52":"hf_20260909_083258_7965f0d6-aa1f-4bce-833d-b865ad5cd883.mp4","cut":"hf_20260909_090415_4f0b7e91-ae4c-4294-9b74-b6c2264132ef.png"}
FD="/usr/share/fonts/truetype/higgsfield"; FONT=FD+"/Montserrat-ExtraBold.ttf"
GOLD=(212,175,55,255); WHITE=(255,255,255,255)
def sh(c): print(">>",c[:160],flush=True); subprocess.check_call(c,shell=True)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode().strip())
os.makedirs("w",exist_ok=True); os.chdir("w")
for k,f in SRC.items():
    e=f.split(".")[-1]
    if not os.path.exists(f"{k}.{e}"): sh(f"curl -sf -o {k}.{e} {B}{f}")
if not os.path.isdir("vo"): sh(f"curl -sf -o work.tar {B2}93425187-9c3b-4e50-b0ac-8f72a9aa655e.tar && tar xf work.tar")
# ---- timeline (body-relative seconds) ----
HK=4.0
OFF={"s02":0.0,"s03":5.09,"s04":17.09}; A_LEN=20.8
BR=A_LEN; BR_LEN=8.0; B1=BR+BR_LEN
OFF1={"s06":0.0,"s07":7.98,"s08":15.29}; B1_LEN=20.29; B2=B1+B1_LEN
OFF2={"s09":0.0,"s1011":5.14}; B2_LEN=17.0; EC=B2+B2_LEN; EC_LEN=4.0; TOTAL=EC+EC_LEN
VO={"s02":OFF["s02"],"s03":OFF["s03"],"s04":OFF["s04"],"s05":BR+0.15,"s06":B1+OFF1["s06"],"s07":B1+OFF1["s07"],"s08":B1+OFF1["s08"],"s09":B2+OFF2["s09"],"s1011":B2+OFF2["s1011"]}
CH={"h1":[("It's the only place I buy my wine…",None)],"h2":[("Trust me, Châteauneuf can be this affordable…",None)],"h3":[("This is where I buy all my Châteauneuf",None)],"h4":[("If you don't like Châteauneuf, keep scrolling…",None)],
"s02":[("Châteauneuf-du-Pape. We all know it.",None),("Wine that trades in the thousands.",("wine",))],
"s03":[("Henri Bonneau's Réserve des Célestins at €1,189",None),("Beaucastel's Hommage à Jacques Perrin at €951",("beau","boca","bo")),("on a 100-point Parker score,",("on",)),("Rayas 1978 at €4,507",("ray","ria","rai"))],
"s04":[("Serious wines, for serious drinkers.",None)],
"s05":[("The grapes are hand-picked from ancient vines.",None),("And that stony soil gives a rich fruit flavour",("and",)),("that develops the longer you sip it.",("that",))],
"s06":[("Then again, Châteauneuf prices are expensive.",None),("That's why I buy direct from the producer.",("that",))],
"s07":[("Winedrops have spent years negotiating with sellers",None),("to find these wines without draining my wallet.",("to",))],
"s08":[("And this one? They got it so cheap,",None),("the producer does not want to be named.",("the",))],
"s09":[("A case of six should cost £480,",None),("and I just bought mine for £125.",("and",))],
"s1011":[("Over 90 points from all major critics,",None),("and the best part? It's exclusive to Winedrops,",("and",)),("I keep impressing my friends,",("i",)),("and I can save my money for other luxuries.",("and",))]}
from faster_whisper import WhisperModel
wm=WhisperModel("small",device="cpu",compute_type="int8")
WORDS={}
for k in CH:
    segs,_=wm.transcribe(f"vo/{k}.wav",language="en",beam_size=5,word_timestamps=True,initial_prompt="Châteauneuf-du-Pape, Henri Bonneau, Beaucastel, Rayas, Winedrops.")
    WORDS[k]=[(w.word.strip().lower().strip(",.?!'’…"),w.start,w.end) for s in segs for w in s.words]
def times(k):
    words=WORDS[k]; ch=CH[k]; n=len(words); tot=sum(len(t.split()) for t,_ in ch); idx=[0]; cum=len(ch[0][0].split())
    for t,a in ch[1:]:
        i=int(round(cum/tot*n)); 
        if a:
            best=None
            for j in range(max(1,idx[-1]+1),n):
                if any(words[j][0].startswith(x) for x in a): 
                    if best is None or abs(j-i)<abs(best-i): best=j
            if best is not None: i=best
        i=max(i,idx[-1]+1); idx.append(min(i,n-1)); cum+=len(t.split())
    out=[]
    for c in range(len(ch)):
        s=words[idx[c]][1]; e=words[idx[c+1]-1][2] if c+1<len(ch) else words[-1][2]
        out.append((ch[c][0],s,e))
    return out
def anchor(k,pref):
    for w,s,e in WORDS[k]:
        if any(w.startswith(p) for p in pref): return s
    return None
def tc(t): t=max(0,t); h=int(t//3600); m=int(t%3600//60); s=t%60; return f"{h}:{m:02d}:{s:05.2f}"
def ass(path,events,size=56,mv=290):
    hdr=f"[Script Info]\nScriptType: v4.00+\nPlayResX: {W}\nPlayResY: {H}\nWrapStyle: 0\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Cap,Montserrat ExtraBold,{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,3.5,1.5,2,70,70,{mv},1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    with open(path,"w") as f:
        f.write(hdr)
        for text,s,e in events: f.write(f"Dialogue: 0,{tc(s)},{tc(e)},Cap,,0,0,0,,{{\\fad(120,120)}}{text}\n")
# ---- captions ----
ev=[]
for k,o in VO.items():
    for t,s,e in times(k): ev.append((t,o+s-0.05,o+e+0.35))
ass("body.ass",ev)
for hk in ["h1","h2","h3","h4"]:
    sp=1.12 if hk=="h3" else 1.0
    ass(f"{hk}.ass",[(t,s/sp,min(3.95,e/sp+0.4)) for t,s,e in times(hk)],size=60)
# ---- graphics ----
def F(sz): return ImageFont.truetype(FONT,sz)
def spaced(d,xy,text,font,fill,sp=2,center=None):
    x,y=xy; wdt=sum(d.textlength(c,font=font)+sp for c in text)-sp
    if center: x=center-wdt/2
    for c in text: d.text((x,y),c,font=font,fill=fill); x+=d.textlength(c,font=font)+sp
    return wdt
def card(name,l1,l2,w=420,h=150):
    im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,w-1,h-1),22,fill=(20,10,15,222),outline=GOLD,width=3)
    spaced(d,(0,22),l1.upper(),F(24),GOLD,sp=2,center=w/2)
    f=F(62); d.text((w/2,58),l2,font=f,fill=WHITE,anchor="ma")
    im.save(name)
def text_png(name,txt,sz,fill=WHITE,pad=30,sp=0):
    f=F(sz); tmp=ImageDraw.Draw(Image.new("RGBA",(10,10)))
    wdt=sum(tmp.textlength(c,font=f)+sp for c in txt)-sp; im=Image.new("RGBA",(int(wdt)+pad*2,sz+pad*2),(0,0,0,0)); d=ImageDraw.Draw(im)
    spaced(d,(pad+3,pad+3),txt,f,(0,0,0,170),sp); spaced(d,(pad,pad),txt,f,fill,sp); im.save(name); return im.size
def pill(name,txt,sz=30):
    f=F(sz); tmp=ImageDraw.Draw(Image.new("RGBA",(10,10))); wdt=sum(tmp.textlength(c,font=f)+2 for c in txt)
    im=Image.new("RGBA",(int(wdt)+70,sz+40),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,im.width-1,im.height-1),im.height//2,fill=(20,10,15,205),outline=GOLD,width=2)
    spaced(d,(0,19),txt,f,GOLD,sp=2,center=im.width/2); im.save(name); return im.size
card("c1.png","Henri Bonneau · Célestins","€1,189"); card("c2.png","Beaucastel · Hommage à J. Perrin","€951"); card("c3.png","Château Rayas 1978","€4,507")
title_sz=text_png("title.png","Châteauneuf-du-Pape",66)
wm_sz=text_png("wm.png","Winedrops",104,sp=4)
lab_sz=pill("lab.png","HAND-PICKED  ·  ANCIENT VINES"); exc_sz=pill("exc.png","90+ POINTS  ·  EXCLUSIVE TO WINEDROPS")
# offer card
im=Image.new("RGBA",(470,235),(0,0,0,0)); d=ImageDraw.Draw(im)
d.rounded_rectangle((0,0,469,234),24,fill=(20,10,15,225),outline=GOLD,width=3)
spaced(d,(0,20),"CASE OF 6",F(24),GOLD,sp=3,center=235)
f1=F(56); d.text((40,88),"£480",font=f1,fill=(200,200,200,255)); w1=d.textlength("£480",font=f1); d.line((36,118,44+w1,118),fill=(230,80,80,255),width=6)
d.text((52+w1,84),"→",font=F(60),fill=GOLD); d.text((120+w1,58),"£125",font=F(100),fill=GOLD)
im.save("offer.png")
cut=Image.open("cut.png").convert("RGBA"); bb=cut.getbbox(); cut=cut.crop(bb)
pk=cut.resize((int(cut.width*520/cut.height),520),Image.LANCZOS); pk.save("pack.png")
# end card
ec=Image.new("RGBA",(W,H),(24,10,18,255)); d=ImageDraw.Draw(ec)
for y in range(H): d.line((0,y,W,y),fill=(24+int(22*y/H),10+int(6*y/H),18+int(12*y/H),255))
spaced(d,(0,150),"THE SOMMELIER'S FIND",F(28),GOLD,sp=6,center=W/2)
spaced(d,(0,215),"Winedrops",F(112),WHITE,sp=4,center=W/2); d.line((W/2-140,352,W/2+140,352),fill=GOLD,width=4)
big=cut.resize((int(cut.width*880/cut.height),880),Image.LANCZOS); ec.alpha_composite(big,(int(W/2-big.width/2),400))
d.text((W/2,1330),"Châteauneuf-du-Pape  ·  Case of 6",font=F(42),fill=WHITE,anchor="ma")
f1=F(64); t1="£480"; w1=d.textlength(t1,font=f1); f2=F(112); t2="£125"; w2=d.textlength(t2,font=f2); x0=W/2-(w1+60+w2)/2
d.text((x0,1425),t1,font=f1,fill=(200,200,200,255)); d.line((x0-6,1462,x0+w1+6,1462),fill=(230,80,80,255),width=7); d.text((x0+w1+60,1395),t2,font=f2,fill=GOLD)
d.rounded_rectangle((W/2-330,1575,W/2+330,1665),45,fill=GOLD); d.text((W/2,1592),"Exclusive to Winedrops",font=F(38),fill=(24,10,18,255),anchor="ma")
spaced(d,(0,1700),"SHOP THE CASE",F(26),WHITE,sp=6,center=W/2)
ec.convert("RGB").save("endcard.png")
# ---- ambience ----
sh("sox -n -r 48000 -c 2 amb.wav synth 80 brownnoise lowpass 420 vol 0.035 fade 1 80 1")
# ---- body audio ----
inp=" ".join(f"-i vo/{k}.wav" for k in VO)+" -i amb.wav"; n=len(VO)
fc=";".join(f"[{i}:a]adelay={int(o*1000)}|{int(o*1000)}[a{i}]" for i,o in enumerate(VO.values()))
fc+=f";[{n}:a]atrim=0:{TOTAL},volume=1[am];"+"".join(f"[a{i}]" for i in range(n))+f"[am]amix=inputs={n+1}:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11,atrim=0:{TOTAL}[a]"
sh(f'ffmpeg -loglevel error -y {inp} -filter_complex "{fc}" -map "[a]" -ar 48000 -ac 2 body_audio.wav')
# ---- body video ----
t3=OFF["s03"]+0.05; t2=OFF["s03"]+(anchor("s03",("beau","boca","bo")) or 4.0); t1=OFF["s03"]+(anchor("s03",("ray","ria","rai")) or 8.5); CEND=BR+BR_LEN
OV=[("title.png",0.2,OFF["s03"]-0.2,int(W/2-title_sz[0]/2),150),("c1.png",t3,CEND,640,290),("c2.png",t2,CEND,640,460),("c3.png",t1,CEND,20,290),
("lab.png",BR+0.3,CEND,int(W/2-lab_sz[0]/2),150),("wm.png",B1+OFF1["s07"]+0.1,B1+OFF1["s08"]-0.1,int(W/2-wm_sz[0]/2),190),
("pack.png",B2+0.2,B2+OFF2["s1011"]-0.1,720,420),("offer.png",B2+0.5,B2+OFF2["s1011"]-0.1,590,980),("exc.png",B2+OFF2["s1011"]+0.1,B2+OFF2["s1011"]+6.5,int(W/2-exc_sz[0]/2),150)]
ins=f"-i bodyA.mp4 -i v51.mp4 -i v52.mp4 -i bodyB1.mp4 -i bodyB2.mp4 -loop 1 -t {EC_LEN} -i endcard.png "+" ".join(f"-loop 1 -t {e-s:.2f} -i {p}" for p,s,e,x,y in OV)
g=f"[0:v]trim=0:{A_LEN},setpts=PTS-STARTPTS,fps=24,format=yuv420p[p0];[1:v]trim=0:4,setpts=PTS-STARTPTS,fps=24,scale={W}:{H},setsar=1,format=yuv420p[p1];[2:v]trim=0:4,setpts=PTS-STARTPTS,fps=24,scale={W}:{H},setsar=1,format=yuv420p[p2];[3:v]trim=0:{B1_LEN},setpts=PTS-STARTPTS,fps=24,format=yuv420p[p3];[4:v]trim=0:{B2_LEN},setpts=PTS-STARTPTS,fps=24,format=yuv420p[p4];[5:v]fps=24,scale={W}:{H},setsar=1,format=yuv420p,trim=0:{EC_LEN},setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.4[p5];[p0][p1][p2][p3][p4][p5]concat=n=6:v=1:a=0[v0]"
cur="v0"
for i,(p,s,e,x,y) in enumerate(OV):
    d=e-s; g+=f";[{6+i}:v]format=rgba,fade=t=in:st=0:d=0.3:alpha=1,fade=t=out:st={d-0.3:.2f}:d=0.3:alpha=1,setpts=PTS+{s:.2f}/TB[o{i}];[{cur}][o{i}]overlay=x={x}:y='{y}+28*max(0,1-(t-{s:.2f})/0.35)':enable='between(t,{s:.2f},{e:.2f})':eof_action=pass[v{i+1}]"; cur=f"v{i+1}"
g+=f";[{cur}]ass=filename=body.ass:fontsdir={FD}[vout]"
open("fc.txt","w").write(g)
ENC="-c:v libx264 -preset veryfast -crf 19 -pix_fmt yuv420p -r 24 -g 48 -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart"
sh(f'ffmpeg -loglevel error -y {ins} -i body_audio.wav -filter_complex_script fc.txt -map "[vout]" -map {6+len(OV)}:a -t {TOTAL} {ENC} body.mp4')
print("body",dur("body.mp4"),flush=True)
# ---- hooks + finals ----
res={}
for i,hk in enumerate(["h1","h2","h3","h4"],1):
    sp=1.12 if hk=="h3" else 1.0
    fc=f"[0:v]setpts=PTS/{sp},trim=0:{HK},setpts=PTS-STARTPTS,fps=24,format=yuv420p,ass=filename={hk}.ass:fontsdir={FD}[v];[1:a]atempo={sp},apad,atrim=0:{HK}[a1];[2:a]atrim=0:{HK}[a2];[a1][a2]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    sh(f'ffmpeg -loglevel error -y -i {hk}.mp4 -i vo/{hk}.wav -i amb.wav -filter_complex "{fc}" -map "[v]" -map "[a]" -t {HK} {ENC} hook_{i}.mp4')
    open("l.txt","w").write(f"file 'hook_{i}.mp4'\nfile 'body.mp4'\n")
    sh(f"ffmpeg -loglevel error -y -f concat -safe 0 -i l.txt -c copy final_{i}.mp4")
    res[i]=dur(f"final_{i}.mp4"); print("final",i,res[i],flush=True)
    if len(sys.argv)>i: 
        code=subprocess.check_output(f"curl -s -o /dev/null -w '%{{http_code}}' -X PUT -H 'Content-Type: video/mp4' --data-binary @final_{i}.mp4 '{sys.argv[i]}'",shell=True).decode(); print("upload",i,code,flush=True)
# QA sheet
ts=[1,5,9,14,19,23,27,33,44,52,58,68,72]
sh(" ".join(f"ffmpeg -loglevel error -y -ss {t} -i final_1.mp4 -frames:v 1 -vf scale=64:-1 q{j}.jpg;" for j,t in enumerate(ts))+" ffmpeg -loglevel error -y "+" ".join(f"-i q{j}.jpg" for j in range(len(ts)))+f" -filter_complex \"{''.join(f'[{j}]' for j in range(len(ts)))}hstack={len(ts)}\" -q:v 15 qa.jpg")
print("QA",subprocess.check_output("base64 -w0 qa.jpg",shell=True).decode(),flush=True)
print("DONE",json.dumps(res),flush=True)
