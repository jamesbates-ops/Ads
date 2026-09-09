# Stage 1 of the v3 build: fetch the Arthur voiceover takes, trim them,
# choose between alternate takes, lay out the timeline, and build the
# grouped audio tracks that drive the lip-synced video generations.
import os,sys,json,subprocess,math
B="https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/"
RAW={
"h1a":"hf_20260909_125858_f4ac1e37-4821-46bf-b323-d3c1cc710c4f.wav",
"h1b":"hf_20260909_130339_5c1cfcc4-e5cc-4c12-94c2-6e5b44aebe84.wav",
"h1c":"hf_20260909_130339_831c4aaa-f9c6-41e3-9010-a3e019a83c93.wav",
"h2":"hf_20260909_125858_6ee43d39-0318-4894-b4a0-390597f06f02.wav",
"h3":"hf_20260909_125858_395ec1df-8932-4e7d-98b2-deb91721edd9.wav",
"h4":"hf_20260909_125858_4bc44c74-d0eb-4e67-bbc5-232d90824688.wav",
"s02":"hf_20260909_125858_5adf9d64-259f-4cf0-a886-2c27f1becfc1.wav",
"s03a":"hf_20260909_130338_b8486ed8-b03b-445e-91b7-413b979baac3.wav",
"s03b":"hf_20260909_130338_b4c18c37-cb90-466f-b30c-8c61eaca1c8c.wav",
"s04":"hf_20260909_125858_2601caa4-59ed-4f1e-baf6-9258df2f1d3d.wav",
"s05":"hf_20260909_125858_e6f8bdcd-c1c9-439a-ab6c-634718298c6a.wav",
"s06":"hf_20260909_125858_d42a38a7-02e8-4573-ac94-f97dd86c7baf.wav",
"s07":"hf_20260909_125858_c2949f7d-7d3c-4dc3-bbdf-ed755ed765aa.wav",
"s08":"hf_20260909_125858_c2248083-58b4-4a75-90e5-2d13b45809c9.wav",
"s09":"hf_20260909_125858_1fcf4a57-8b4e-430c-99ff-4631ec3e837e.wav",
"s1011":"hf_20260909_125907_62cd71c3-2f77-458b-b0f1-dc876689d960.wav"}
def sh(c): subprocess.check_call(c,shell=True)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())
os.makedirs("raw",exist_ok=True); os.makedirs("vo",exist_ok=True); os.makedirs("tracks",exist_ok=True)
for k,f in RAW.items():
    if not os.path.exists(f"raw/{k}.wav"): sh(f"curl -sf -o raw/{k}.wav {B}{f}")
TR="silenceremove=start_periods=1:start_silence=0.05:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_silence=0.05:start_threshold=-50dB,areverse"
for k in RAW:
    if not os.path.exists(f"vo/{k}.wav"):
        sh(f'ffmpeg -v error -y -i raw/{k}.wav -af "{TR},loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -ac 1 vo/{k}.wav')
D={k:dur(f"vo/{k}.wav") for k in RAW}
h1=min(["h1a","h1b","h1c"],key=lambda k:abs(D[k]-4.0))
s03="s03a" if D["s03a"]<=18.0 else "s03b"
for src,dst in [(h1,"h1"),(s03,"s03")]: sh(f"cp vo/{src}.wav vo/{dst}.wav")
D["h1"]=D[h1]; D["s03"]=D[s03]
print("takes: h1="+h1+f" ({D['h1']:.2f}s)  s03="+s03+f" ({D['s03']:.2f}s)")
GAP={"s02":0.55,"s03":0.90,"s04":0.45,"s05":1.00,"s06":0.55,"s07":0.55,"s08":0.95,"s09":0.55,"s1011":0.70}
slot={k:D[k]+GAP[k] for k in GAP}
CAP=29.0   # keep every generated clip inside the model's 30 s ceiling
def pack(keys):
    out=[];cur=[]
    for k in keys:
        if cur and sum(slot[x] for x in cur)+slot[k]>CAP: out.append(cur); cur=[]
        cur.append(k)
    if cur: out.append(cur)
    return out
clips=[]
for i,g in enumerate(pack(["s02","s03","s04"])): clips.append({"name":f"A{i+1}","frame":"A","lines":g})
clips.append({"name":"BROLL","frame":"-","lines":["s05"]})
for i,g in enumerate(pack(["s06","s07","s08","s09","s1011"])): clips.append({"name":f"B{i+1}","frame":"B","lines":g})
t=0.0; starts={}
for c in clips:
    c["start"]=t; off=0.0; c["offsets"]={}
    for k in c["lines"]:
        c["offsets"][k]=off; starts[k]=t+off; off+=slot[k]
    c["total"]=off; c["video_dur"]=int(math.ceil(off)); t+=c["total"]
HK=round(max(D["h1"],D["h2"],D["h3"],D["h4"])+0.35,2)
EC=t; ECL=4.0
tl={"hook_slot":HK,"clips":clips,"line_dur":{k:D[k] for k in GAP},"slot":slot,"body_starts":starts,
    "endcard_start":EC,"endcard_len":ECL,"body_total":t+ECL,"final_total":HK+t+ECL}
json.dump(tl,open("timeline.json","w"),indent=1)
print(json.dumps({"HK":HK,"clips":[{"n":c["name"],"lines":c["lines"],"start":round(c["start"],2),"total":round(c["total"],2),"vdur":c["video_dur"]} for c in clips],"body":round(t+ECL,2),"final":round(HK+t+ECL,2)}))
for c in clips:
    if c["name"]=="BROLL": continue
    n=len(c["lines"]); ins=" ".join(f"-i vo/{k}.wav" for k in c["lines"])
    fc=";".join(f"[{i}:a]adelay={int(c['offsets'][k]*1000)}|{int(c['offsets'][k]*1000)}[a{i}]" for i,k in enumerate(c["lines"]))
    fc+=";"+"".join(f"[a{i}]" for i in range(n))+f"amix=inputs={n}:normalize=0:dropout_transition=0,apad,atrim=0:{c['video_dur']}[a]"
    sh(f'ffmpeg -v error -y {ins} -filter_complex "{fc}" -map "[a]" -ar 48000 -ac 1 tracks/{c["name"]}.wav')
for k in ["h1","h2","h3","h4"]: sh(f'ffmpeg -v error -y -i vo/{k}.wav -af apad -t {HK} -ar 48000 -ac 1 tracks/{k}.wav')
print("tracks ok")
for a in sys.argv[1:]:
    nm,url=a.split("=",1)
    sh(f"ffmpeg -v error -y -i tracks/{nm}.wav -b:a 192k tracks/{nm}.mp3")
    print("upload",nm,subprocess.check_output(f"curl -s -o /dev/null -w '%{{http_code}}' -X PUT -H 'Content-Type: audio/mpeg' --data-binary @tracks/{nm}.mp3 '{url}'",shell=True).decode(),flush=True)
