# Stage 2 of the v3 build: pull the generated clips, time the captions from the
# voiceover, draw the graphics, mix the audio, and cut the four hook variants.
import os,sys,json,subprocess,math
from PIL import Image,ImageDraw,ImageFont
W,H=1080,1920
BA="https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/"
FD="/usr/share/fonts/truetype/higgsfield"; FONT=FD+"/Montserrat-ExtraBold.ttf"
GOLD=(212,175,55,255); WHITE=(255,255,255,255)
def sh(c): print(">>",c[:120],flush=True); subprocess.check_call(c,shell=True)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())
VID=json.load(open("vid.json"))
CUT="hf_20260909_090415_4f0b7e91-ae4c-4294-9b74-b6c2264132ef.png"
tl=json.load(open("timeline.json")); HK=tl["hook_slot"]; ST=tl["body_starts"]; CL=tl["clips"]
EC=tl["endcard_start"]; ECL=tl["endcard_len"]; TOT=tl["body_total"]
os.makedirs("cl",exist_ok=True)
for k,f in VID.items():
    if not os.path.exists(f"cl/{k}.mp4"): sh(f"curl -sf -o cl/{k}.mp4 {BA}{f}")
if not os.path.exists("cut.png"): sh(f"curl -sf -o cut.png {BA}{CUT}")
CH={"h1":[("It's the only place I buy my wine.",None)],"h2":[("Trust me, Chateauneuf can be this affordable.",None)],
"h3":[("This is where I buy all my Chateauneuf.",None)],"h4":[("If you don't like Chateauneuf, keep scrolling.",None)],
"s02":[("Chateauneuf-du-Pape. We all know it.",None),("Wine that trades in the thousands.",("wine",))],
"s03":[("Henri Bonneau's Celestins at 1,189 euro",None),("Beaucastel's Hommage a Jacques Perrin at 951",("beau","boca","bo")),("on a 100-point Parker score,",("on",)),("Rayas 1978 - four and a half thousand.",("ray","ria","rai"))],
"s04":[("Serious wines, for serious drinkers.",None)],
"s05":[("The grapes are hand-picked from ancient vines.",None),("And that stony soil gives a rich fruit flavour",("and",)),("that develops the longer you sip it.",("that",))],
"s06":[("Then again, Chateauneuf prices are expensive.",None),("That's why I buy direct from the producer.",("that",))],
"s07":[("Winedrops have spent years negotiating with sellers",None),("to find these wines without draining my wallet.",("to",))],
"s08":[("And this one? They got it so cheap,",None),("the producer does not want to be named.",("the",))],
"s09":[("A case of six should cost 480 pounds,",None),("and I just bought mine for 125.",("and",))],
"s1011":[("Over 90 points from all major critics.",None),("And the best part? It's exclusive to Winedrops.",("and",)),("I keep impressing my friends,",("i",)),("and I can save my money for other luxuries.",("and",))]}
# NOTE: accented caption text is written with the proper accents in the live
# script; it is transliterated here so the file stays ASCII-safe in git.
from faster_whisper import WhisperModel
wm=WhisperModel("small",device="cpu",compute_type="int8"); WORDS={}
for k in CH:
    segs,_=wm.transcribe(f"vo/{k}.wav",language="en",beam_size=5,word_timestamps=True,initial_prompt="Chateauneuf-du-Pape, Henri Bonneau, Beaucastel, Rayas, Winedrops.")
    WORDS[k]=[(w.word.strip().lower().strip(",.?!'’…"),w.start,w.end) for s in segs for w in s.words]
def times(k):
    words=WORDS[k]; ch=CH[k]; n=len(words); tot=sum(len(t.split()) for t,_ in ch); idx=[0]; cum=len(ch[0][0].split())
    for t,a in ch[1:]:
        i=int(round(cum/tot*n))
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
def tc(t): t=max(0,t); return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
def ass(path,ev,size=56,mv=290):
    hdr=f"[Script Info]\nScriptType: v4.00+\nPlayResX: {W}\nPlayResY: {H}\nWrapStyle: 0\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Cap,Montserrat ExtraBold,{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,3.5,1.5,2,70,70,{mv},1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    open(path,"w").write(hdr+"".join(f"Dialogue: 0,{tc(s)},{tc(e)},Cap,,0,0,0,,{{\\fad(120,120)}}{t}\n" for t,s,e in ev))
ev=[]
for k,o in ST.items():
    for t,s,e in times(k): ev.append((t,o+s-0.05,o+e+0.35))
ass("body.ass",ev)
for hk in ["h1","h2","h3","h4"]: ass(f"{hk}.ass",[(t,s,min(HK-0.05,e+0.4)) for t,s,e in times(hk)],size=60)
def F(s): return ImageFont.truetype(FONT,s)
def spaced(d,xy,text,f,fill,sp=2,center=None):
    x,y=xy; wd=sum(d.textlength(c,font=f)+sp for c in text)-sp
    if center: x=center-wd/2
    for c in text: d.text((x,y),c,font=f,fill=fill); x+=d.textlength(c,font=f)+sp
    return wd
def card(n,l1,l2,w=420,h=150):
    im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,w-1,h-1),22,fill=(20,10,15,222),outline=GOLD,width=3)
    spaced(d,(0,22),l1.upper(),F(24),GOLD,2,w/2); d.text((w/2,58),l2,font=F(62),fill=WHITE,anchor="ma"); im.save(n)
def tpng(n,txt,sz,fill=WHITE,pad=30,sp=0):
    f=F(sz); t=ImageDraw.Draw(Image.new("RGBA",(10,10))); wd=sum(t.textlength(c,font=f)+sp for c in txt)-sp
    im=Image.new("RGBA",(int(wd)+pad*2,sz+pad*2),(0,0,0,0)); d=ImageDraw.Draw(im)
    spaced(d,(pad+3,pad+3),txt,f,(0,0,0,170),sp); spaced(d,(pad,pad),txt,f,fill,sp); im.save(n); return im.size
def pill(n,txt,sz=30):
    f=F(sz); t=ImageDraw.Draw(Image.new("RGBA",(10,10))); wd=sum(t.textlength(c,font=f)+2 for c in txt)
    im=Image.new("RGBA",(int(wd)+70,sz+40),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rounded_rectangle((0,0,im.width-1,im.height-1),im.height//2,fill=(20,10,15,205),outline=GOLD,width=2)
    spaced(d,(0,19),txt,f,GOLD,2,im.width/2); im.save(n); return im.size
card("c1.png","Henri Bonneau . Celestins","1,189 euro"); card("c2.png","Beaucastel . Hommage a J. Perrin","951 euro"); card("c3.png","Chateau Rayas 1978","4,507 euro")
ts=tpng("title.png","Chateauneuf-du-Pape",66); ws=tpng("wm.png","Winedrops",104,sp=4)
ls=pill("lab.png","HAND-PICKED  .  ANCIENT VINES"); xs=pill("exc.png","90+ POINTS  .  EXCLUSIVE TO WINEDROPS")
im=Image.new("RGBA",(470,235),(0,0,0,0)); d=ImageDraw.Draw(im)
d.rounded_rectangle((0,0,469,234),24,fill=(20,10,15,225),outline=GOLD,width=3)
spaced(d,(0,20),"CASE OF 6",F(24),GOLD,3,235)
f1=F(48); d.text((40,92),"480",font=f1,fill=(200,200,200,255)); w1=d.textlength("480",font=f1)
d.line((36,120,44+w1,120),fill=(230,80,80,255),width=6); d.text((52+w1,88),"->",font=F(52),fill=GOLD); d.text((112+w1,66),"125",font=F(84),fill=GOLD)
im.save("offer.png")
cut=Image.open("cut.png").convert("RGBA"); cut=cut.crop(cut.getbbox())
cut.resize((int(cut.width*520/cut.height),520),Image.LANCZOS).save("pack.png")
ec=Image.new("RGBA",(W,H),(24,10,18,255)); d=ImageDraw.Draw(ec)
for y in range(H): d.line((0,y,W,y),fill=(24+int(22*y/H),10+int(6*y/H),18+int(12*y/H),255))
spaced(d,(0,150),"THE SOMMELIER'S FIND",F(28),GOLD,6,W/2)
spaced(d,(0,215),"Winedrops",F(112),WHITE,4,W/2); d.line((W/2-140,352,W/2+140,352),fill=GOLD,width=4)
big=cut.resize((int(cut.width*880/cut.height),880),Image.LANCZOS); ec.alpha_composite(big,(int(W/2-big.width/2),400))
d.text((W/2,1330),"Chateauneuf-du-Pape  .  Case of 6",font=F(42),fill=WHITE,anchor="ma")
f1=F(64); w1=d.textlength("480",font=f1); f2=F(112); w2=d.textlength("125",font=f2); x0=W/2-(w1+60+w2)/2
d.text((x0,1425),"480",font=f1,fill=(200,200,200,255)); d.line((x0-6,1462,x0+w1+6,1462),fill=(230,80,80,255),width=7)
d.text((x0+w1+60,1395),"125",font=f2,fill=GOLD)
d.rounded_rectangle((W/2-330,1575,W/2+330,1665),45,fill=GOLD); d.text((W/2,1592),"Exclusive to Winedrops",font=F(38),fill=(24,10,18,255),anchor="ma")
spaced(d,(0,1700),"SHOP THE CASE",F(26),WHITE,6,W/2); ec.convert("RGB").save("endcard.png")
sh(f"sox -n -r 48000 -c 2 amb.wav synth {int(TOT)+6} brownnoise lowpass 420 vol 0.035 fade 1 {int(TOT)+6} 1")
ins=" ".join(f"-i vo/{k}.wav" for k in ST)+" -i amb.wav"; n=len(ST)
fc=";".join(f"[{i}:a]adelay={int(o*1000)}|{int(o*1000)}[a{i}]" for i,o in enumerate(ST.values()))
fc+=f";[{n}:a]atrim=0:{TOT},volume=1[am];"+"".join(f"[a{i}]" for i in range(n))+f"[am]amix=inputs={n+1}:normalize=0:dropout_transition=0,loudnorm=I=-14:TP=-1.5:LRA=11,atrim=0:{TOT}[a]"
sh(f'ffmpeg -loglevel error -y {ins} -filter_complex "{fc}" -map "[a]" -ar 48000 -ac 2 body_audio.wav')
CEND=ST["s06"]
t3=ST["s03"]+0.05; t2=ST["s03"]+(anchor("s03",("beau","boca","bo")) or 5.0); t1=ST["s03"]+(anchor("s03",("ray","ria","rai")) or 12.0)
bs=[c for c in CL if c["name"]=="BROLL"][0]
OV=[("title.png",0.2,ST["s03"]-0.2,int(W/2-ts[0]/2),150),("c1.png",t3,CEND,640,290),("c2.png",t2,CEND,640,460),("c3.png",t1,CEND,20,290),
("lab.png",bs["start"]+0.3,CEND,int(W/2-ls[0]/2),150),("wm.png",ST["s07"]+0.1,ST["s08"]-0.1,int(W/2-ws[0]/2),190),
("pack.png",ST["s09"]+0.2,ST["s1011"]-0.1,720,420),("offer.png",ST["s09"]+0.5,ST["s1011"]-0.1,590,980),
("exc.png",ST["s1011"]+0.1,min(ST["s1011"]+6.5,EC-0.2),int(W/2-xs[0]/2),150)]
vin=" ".join(f"-i cl/{c['name']}.mp4" for c in CL)+f" -loop 1 -t {ECL} -i endcard.png "+" ".join(f"-loop 1 -t {e-s:.2f} -i {p}" for p,s,e,x,y in OV)
g=""
for i,c in enumerate(CL): g+=f"[{i}:v]trim=0:{c['total']:.3f},setpts=PTS-STARTPTS,fps=24,scale={W}:{H},setsar=1,format=yuv420p[p{i}];"
ne=len(CL)
g+=f"[{ne}:v]fps=24,scale={W}:{H},setsar=1,format=yuv420p,trim=0:{ECL},setpts=PTS-STARTPTS,fade=t=in:st=0:d=0.4[p{ne}];"
g+="".join(f"[p{i}]" for i in range(ne+1))+f"concat=n={ne+1}:v=1:a=0[v0]"
cur="v0"
for i,(p,s,e,x,y) in enumerate(OV):
    d0=e-s; g+=f";[{ne+1+i}:v]format=rgba,fade=t=in:st=0:d=0.3:alpha=1,fade=t=out:st={d0-0.3:.2f}:d=0.3:alpha=1,setpts=PTS+{s:.2f}/TB[o{i}];[{cur}][o{i}]overlay=x={x}:y='{y}+28*max(0,1-(t-{s:.2f})/0.35)':enable='between(t,{s:.2f},{e:.2f})':eof_action=pass[v{i+1}]"; cur=f"v{i+1}"
g+=f";[{cur}]ass=filename=body.ass:fontsdir={FD}[vout]"
open("fc.txt","w").write(g)
ENC="-c:v libx264 -preset veryfast -crf 19 -pix_fmt yuv420p -r 24 -g 48 -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart"
sh(f'ffmpeg -loglevel error -y {vin} -i body_audio.wav -filter_complex_script fc.txt -map "[vout]" -map {ne+1+len(OV)}:a -t {TOT} {ENC} body.mp4')
print("body",dur("body.mp4"),flush=True)
res={}
for i,hk in enumerate(["h1","h2","h3","h4"],1):
    fc=f"[0:v]trim=0:{HK},setpts=PTS-STARTPTS,fps=24,scale={W}:{H},setsar=1,format=yuv420p,ass=filename={hk}.ass:fontsdir={FD}[v];[1:a]apad,atrim=0:{HK}[a1];[2:a]atrim=0:{HK}[a2];[a1][a2]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
    sh(f'ffmpeg -loglevel error -y -i cl/{hk}.mp4 -i vo/{hk}.wav -i amb.wav -filter_complex "{fc}" -map "[v]" -map "[a]" -t {HK} {ENC} hook_{i}.mp4')
    open("l.txt","w").write(f"file 'hook_{i}.mp4'\nfile 'body.mp4'\n")
    sh(f"ffmpeg -loglevel error -y -f concat -safe 0 -i l.txt -c copy final_{i}.mp4")
    res[i]=dur(f"final_{i}.mp4"); print("final",i,res[i],flush=True)
for a in sys.argv[1:]:
    nm,url=a.split("=",1)
    print("upload",nm,subprocess.check_output(f"curl -s -o /dev/null -w '%{{http_code}}' -X PUT -H 'Content-Type: video/mp4' --data-binary @final_{nm}.mp4 '{url}'",shell=True).decode(),flush=True)
print("DONE",json.dumps(res),flush=True)
