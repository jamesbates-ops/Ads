#!/usr/bin/env python3
"""Download the voice-changed presenter clips and B-roll listed in sources.json
into talk/ and broll/ next to this script, ready for edit.py."""
import json, os, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(os.path.join(HERE, "sources.json")))
jobs = [(os.path.join(HERE, "talk", f"vc_{k}.mp4"), u) for k, u in src["voice_changed_urls"].items()]
jobs += [(os.path.join(HERE, "broll", f"{k}.mp4"), u) for k, u in src["broll_urls"].items()]
for path, url in jobs:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
        print("fetched", os.path.relpath(path, HERE))
