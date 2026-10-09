# Trentacoste Primitivo — UGC creator A-roll

A creator talks to her phone in her kitchen, holding the bottle, in lo-fi iPhone style with diegetic audio and a British accent. Editors cut B-roll in over it, and the "flash 99pts" graphic is theirs to add. The source seeds showed her holding a different bottle (Scaranto). Because the script describes the Trentacoste Primitivo, the start frames swap in the Trentacoste bottle from the product shot, with the label reproduced exactly.

**Current version: v2.** v2 is a full redo at a natural, unhurried pace, after v1 came out too fast. v1 is kept below for reference.

- Seven continuous takes, one per script beat. The phone is propped on the worktop, with the bottle in her right hand and her left hand free to gesture. The takes alternate between two start frames, so each join reads as a natural jump cut.
- Seedance 2.5 with native audio, generated from the start frame, the product reference and a voice reference. Drafted at 480p, checked, then finalised at 1080p.
- **Pace:** she was directed to speak like she's chatting to a friend, with a breath between phrases. v2 runs at about 2.4 words/s including pauses, against about 3.3 words/s in v1. The same script now runs 1:04 instead of 0:46.
- Every final take was checked three ways:
  - **Accent:** an English-accent classifier reads every take as England (≥ 99.8 %).
  - **Voice:** speaker similarity between takes is 0.73–0.87, so it's the same voice throughout.
  - **Words:** a Whisper transcript of each take has every scripted word present and in order.
- 1080×1920, 24 fps, audio −14 LUFS. No captions or on-screen text.
- Trimmed tight to her speech with `scripts/build_greenscreen_cuts.py --thresh 21`. The stricter threshold keeps the kitchen room tone from counting as speech.

## Deliverables (v2)

| File | Link / location |
|---|---|
| Full-quality ZIP (A-roll + 7 takes, 114 MB) | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/b48be319-153c-418d-b1e3-70fc40764d0a.zip |
| Smaller copies sent directly (A-roll 27 MB, takes ZIP 27 MB) | `output/trentacoste-ugc-v2/share/` (not committed) |

`output/trentacoste-ugc-v2/clip_timings.json` holds the trim points.

## Takes (v2)

| # | File | A-roll in | Length | Line as delivered |
|---|---|---|---|---|
| 1 | `01_hook_warning.mp4` | 0:00.0 | 8.2 s | "Warning… if you love Italian wine and you keep on scrolling through your phone, you'll miss out on the best deal this year." |
| 2 | `02_fat-duck_85.mp4` | 0:08.2 | 8.9 s | "At the Fat Duck, the lowest price of a bottle is eighty-five pounds. That's this one *(bottle to the lens)*. Yeah, this one." |
| 3 | `03_heston.mp4` | 0:17.1 | 9.9 s | "And even then, they're rigorously critiqued and then hand-picked to pair with Michelin star dishes, served by Heston Blumenthal himself… Himself." |
| 4 | `04_tenner.mp4` | 0:27.0 | 10.1 s | "Except… I got this bottle for a tenner. So you can enjoy it whenever you like, without breaking the bank. A tenner!" |
| 5 | `05_puglia_maroni.mp4` | 0:37.1 | 11.8 s | "It's from a family-run estate in Puglia, and it's rated near flawless… by Luca Maroni. That puts it in the top three percent of wines in the world." |
| 6 | `06_winedrops_offer.mp4` | 0:48.9 | 7.1 s | "Except at Winedrops, they'll do free delivery on a case of six, for ten pounds a bottle." |
| 7 | `07_cta.mp4` | 0:56.0 | 7.6 s | "I wouldn't wait. It won't be around for long. I'll put the link somewhere below *(points down)*. Go on." |

A-roll = takes 1–7 back to back, 1:03.7.

## Notes for the edit (v2)

- **Flash 99pts:** "near flawless" lands at about **0:41.3–0:42.3** in the A-roll (4.2–5.2 s into take 5). She pauses after it before "by Luca Maroni", which leaves room for the graphic.
- **Built-in pauses:**
  - About 1 s after "Warning" in the hook.
  - A drawn-out, leaning-in "Except…" at the top of take 4, followed by about 1 s of silence.
  - Tighten either one in the edit if you want a faster open.
- **Ad-libs** (all add no facts or taste claims, so trim them if they're not wanted):
  - "Yeah, this one." (take 2)
  - "Himself." (take 3)
  - "A tenner!" (take 4)
  - "Go on." (take 7)

## Script changes and notes (v2)

- **Hook wording:** "and keep scrolling" became "and you keep on scrolling through your phone". Three takes with the plain wording all came out as "keep sliding" in the transcript, and the reworded take is the only one that reads clearly as "scrolling". The meaning is unchanged.
- **"At Fat Duck"** is said as "At the Fat Duck", the restaurant's name.
- **"Except I got this bottle for a tenner"** is voiced as scripted (v1 had changed it to "you can get"). This is a first-person purchase claim from an AI-generated creator. Make sure the ad is clearly labelled as an ad, and that the line is acceptable under the platform's and ASA's rules on testimonials.
- **Listen for** the following. Both are most likely transcriber mishears, but I couldn't listen myself:
  - "Heston": the small transcriber heard "Hitter"; the larger one, with a hint, heard "Heston".
  - "Maroni": transcribed as "Morone".
- **Claims to verify before the ad runs:**
  - Fat Duck's cheapest bottle is £85, and it's this wine.
  - Hand-picked to pair with Heston Blumenthal's Michelin-star dishes.
  - Family-run estate in Puglia.
  - Luca Maroni "near flawless" / 99 pts.
  - Top 3 % of wines in the world.
  - "I got this bottle for a tenner".
  - Winedrops £10 a bottle with free delivery on a case of six.

## Generation ledger (Higgsfield)

- Seeds: `6b62539b-d147-4ded-a4e6-c9c9a9e70b22`, `7b656406-c990-4e8d-9987-0b2bacb787c5`; product shot `516ab5f9-9615-4c4c-8837-9f78dc1b1a8a`
- Start frames with the Trentacoste bottle (`gpt_image_2`):
  - `19a11630-a276-4e12-950c-c9dd360e31eb` (v2 takes 1, 3, 5, 7)
  - `33649062-89bf-438d-8773-e2566ae7c6fa` (v2 takes 2, 4, 6)
- Voice references:
  - v1: `45ba99cd-56e5-4906-ae53-179848fbfa5b` (from test draft `d1e5835d`)
  - v2: `5bc8dce5-df7c-4206-8d1f-8fe95a6a9db8` (first 7.4 s of the slow hook test `9b61946c`, generated with the v1 reference, so the voice is the same)

### v2

| Take | Draft (480p) | Final (1080p) |
|---|---|---|
| 1 | `ecca1978-2688-48c6-8aad-9cdfc12eb670` (rejected: `9b61946c` and `9e5afeac` said "sliding"; `12dc8e18` said "sliding" and "Warning" twice) | `aa454c00-76b5-4760-a93f-137731e8203f` |
| 2 | `c95fa2fa-3e36-4802-af1d-2f8f16f701a1` | `6e938387-47d5-43b1-850f-9c79c59f0a08` |
| 3 | `aae18585-5588-41cb-b615-3d183cf0fb16` | `835368a1-070d-4f94-b1ff-c307ff4f9007` |
| 4 | `e5be7113-f44f-4a6a-b500-48a2cf5a8286` | `bc9ce75d-6800-452c-b7a1-d2a1a37b6829` |
| 5 | `1b434318-1bac-414f-96a8-d86199f1d871` | `03abb6aa-8788-4092-9736-bae828bb5cac` |
| 6 | `9f04605c-ee83-4933-9a4f-a64f833c7b3c` | `ca38abd6-83dd-483e-a635-85de1a05f9fd` |
| 7 | `deafb4f6-a7e7-4393-9875-67fbf0528132` | `2dde0f8e-e269-4a39-b1c2-e063270ebf8b` |

## v1 (superseded: too fast)

Four longer takes (45.6 s in total), packed with loosened script and ad-libs, at about 3.3 words/s. Full-quality ZIP: https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/895d5dff-df92-4b34-9fe9-f4718711301f.zip (files in `output/trentacoste-ugc/`).

- **Changes from the script:**
  - "Except you can get this bottle for a tenner" replaced the scripted first-person line.
  - An unscripted "…and it's delicious" was trimmed off take 2.

| Take | Draft (480p) | Final (1080p) |
|---|---|---|
| 1 | `dd3f8b3a-a733-4e1d-a466-05432571c429` | `66e03166-102b-4844-87b0-00a09998602f` |
| 2 | `15ccd067-bb97-4f67-8c47-e014a2553b70` | `865f9231-7722-44f4-8887-9b620c2ac198` (trimmed at 12.2 s) |
| 3 | `ce4bfaa2-8240-48be-8c1c-712ccc741b5b` | `cf956095-1ec0-4303-a2b6-5ddd7904aa1e` |
| 4 | `b0e686d5-fab0-4c35-8b04-f5971ca475f2` | `31c66988-28f1-423e-a3f5-4b910121873d` |
