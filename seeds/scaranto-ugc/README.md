# Scarànto UGC ad

9:16 hyper-real UGC talking-head A-roll for Scarànto, in a **UK (British accent)** and a **US (American accent)** version. The presenter, kitchen and look are recreated from shot 1 of the reference Winedrops/Scarànto TikTok, with an entirely new presenter. The editors cut b-roll in over and between the takes.

The script for both versions is in [`SCRIPT.md`](SCRIPT.md).

## Deliverables

Review rough cuts (three takes butted together, loudness matched to about -16 LUFS, no b-roll):
- `aroll/UK_aroll_roughcut.mp4`, 52s
- `aroll/US_aroll_roughcut.mp4`, 52s

Download everything at once (the three full-quality takes per version, zipped):
- UK: https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/b8b7f297-b63c-4899-b8d5-32971b729acd.zip (37 MB)
- US: https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/b36734cf-09bb-4235-ba69-c5c49ce4e3ee.zip (43 MB, final US takes with both fixes)

Full-quality individual takes (1080×1920, 24 fps, HEVC with native iPhone-style audio). Use these for the edit:

| Take | Length | UK | US |
|---|---|---|---|
| 1. Sassicaia and Tignanello, over 150 | 8s | [uk take 1](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123139_16dc8e8c-06b2-426b-a0cc-a31a68229c64.mp4) | [us take 1](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_131621_08570658-53f2-4def-9cbc-7c8d226df716.mp4) |
| 2. Scarànto: same style, 10 (UK) / 20 (US), 100 pts, taste | 24s | [uk take 2](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123139_dab860d4-aff2-465d-870f-138af6d08259.mp4) | [us take 2](https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/149c02cd-3dbe-49f0-91a8-06798bab28bc.mp4) ("just twenty" and "tannins" fixed, H.264) |
| 3. 12 for one Sassicaia, case of 6 offer | 20s | [uk take 3](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123139_22de8066-1cba-43b8-b5a1-469917a6e45a.mp4) | [us take 3](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123944_42998832-18ec-44ab-b05c-c0e19278fcb8.mp4) |

Higgsfield job IDs: UK `16dc8e8c…`, `dab860d4…`, `22de8066…` · US `08570658…`, `b9dea00c…`, `42998832…`. (Superseded US takes 1 and 2, which came out with a British accent: `b9b9e5f6…`, `2d4e597e…`.)

## Seed frames

| File | Used for | Higgsfield job |
|---|---|---|
| `seed_two_bottles.png` | Take 1: holding Sassicaia (frame left) and Tignanello (frame right) | `1eebe58f-96b2-40e2-96f9-b66bebe69ab5` |
| `seed_v2_label_fixed.png` | Takes 2 and 3: holding Scarànto, label corrected to the real charcoal-black label from the packshot | `921fee3a-d967-4037-87dd-26f315d2db1a` |
| `seed_v2.png` | First pass (navy label, superseded) | `771f1e1c-402f-4968-8a9a-0c6ae3c50a7a` |
| `seed_v1.png` | Alternative first pass, lower bottle (not used) | `09fd0bc3-7a5c-46ca-88ce-ef211cd188ef` |

References: `reference/original_shot1_0.1s.jpg` and `reference/original_bottle_closeup_8.6s.jpg` (frames from the source TikTok), plus `reference/bottles/` (Scarànto packshot, Sassicaia and Tignanello bottle shots).

## How it was made
- Seeds: GPT Image 2.5, high quality, 2K, 9:16. The presenter has long wavy dark-brunette hair, olive skin, small gold hoops and a white ribbed tank top.
- Takes: Seedance 2.5 image-to-video from the seed frame with native audio, 1080p, one continuous take per clip. The phone is propped on the worktop as a static camera, with ordinary daylight and unretouched skin. The audio is diegetic iPhone-mic sound (room tone, tile echo, glass knocks) with no music.
- US accent fix: the first US takes 1 and 2 drifted British, and only take 3 came out American. They were regenerated with a 10s clip of her American voice from US take 3 as a voice reference, an American persona, and American spellings with no mention of "British" in the prompt.
- US "tannins" fix: in US take 2 she said "tangers". Only that line (18.85–21.97s) was redone. A 4.5s section was re-rendered with its audio removed, so the model had to say the line fresh, with the same American voice reference. It was spliced back in with a 0.2s picture crossfade and 40ms audio crossfades, all inside the pauses either side of the line. The rest of the take is untouched. Unpatched original: `b9dea00c…`.
  - Verified with a forced-choice recogniser calibrated on the UK take (where she says it correctly): the patched line scores "tannins" 0.73 against "tangers" 0.65. Before the fix it was "tangers" 0.71 against "tannins" 0.62. The accent classifier reads the new line as US, and its pitch (182 Hz) matches the rest of the take.
- US price fix: US take 2 said "we'll do it for just ten", which didn't match six for under $120. Only that line (6.15–8.24s) was redone as "…just twenty", using the same method as the tannins fix (a 4.25s section re-rendered without its audio, with the American voice reference, then crossfaded back in the pauses either side). The forced-choice check scores "twenty" 0.78 against "ten" 0.65; on the take before the fix it was "ten" 0.70 against "twenty" 0.66. The accent reads US, and the tannins fix and everything else are unchanged.
- Checks: every take was transcribed and contains every scripted line, and no words leaked from the voice reference. An accent classifier (CommonAccent ECAPA) scores every 4s window of the UK takes closer to England than to US (a few windows top out as Australia, a neighbouring accent). Every window of the final US takes tops out as US or Canada. Voice pitch is consistent within each version (UK 174–188 Hz, US 180–188 Hz median). Labels stay front-on and legible, there is exactly one bottle per hand, and there is no on-screen text.

## Known nits
- Transcripts spell the wine names oddly ("Scoronto", "Sasukea"), which is normal for the speech-to-text. Have someone listen for the pronunciation of Scarànto before sign-off.
- Take 1's trailing ad-lib ("Mad" / "Crazy") is soft and partly a laugh, so it's easy to trim if it doesn't land.
