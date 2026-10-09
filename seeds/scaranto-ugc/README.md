# Scarànto UGC ad

9:16 hyper-real UGC talking-head A-roll for Scarànto, in a **UK (British accent)** and a **US (American accent)** version. The presenter, kitchen and look are recreated from shot 1 of the reference Winedrops/Scarànto TikTok, with an entirely new presenter. The editors cut b-roll in over and between the takes.

The script for both versions is in [`SCRIPT.md`](SCRIPT.md).

## Deliverables

Review rough cuts (three takes butted together, loudness matched to about -16 LUFS, no b-roll):
- `aroll/UK_aroll_roughcut.mp4`, 52s
- `aroll/US_aroll_roughcut.mp4`, 52s

Full-quality individual takes (1080×1920, 24 fps, HEVC with native iPhone-style audio). Use these for the edit:

| Take | Length | UK | US |
|---|---|---|---|
| 1. Sassicaia and Tignanello, over 150 | 8s | [uk take 1](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123139_16dc8e8c-06b2-426b-a0cc-a31a68229c64.mp4) | [us take 1](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123944_b9b9e5f6-4e7c-4c4a-9f74-da0268564ad9.mp4) |
| 2. Scarànto: same style, 10, 100 pts, taste | 24s | [uk take 2](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123139_dab860d4-aff2-465d-870f-138af6d08259.mp4) | [us take 2](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123944_2d4e597e-b9f7-4bb5-b9e8-d97126897468.mp4) |
| 3. 12 for one Sassicaia, case of 6 offer | 20s | [uk take 3](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123139_22de8066-1cba-43b8-b5a1-469917a6e45a.mp4) | [us take 3](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261009_123944_42998832-18ec-44ab-b05c-c0e19278fcb8.mp4) |

Higgsfield job IDs: UK `16dc8e8c…`, `dab860d4…`, `22de8066…` · US `b9b9e5f6…`, `2d4e597e…`, `42998832…`.

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
- Checks: every take was transcribed and contains every scripted line. Voice pitch is consistent across takes within each version (UK 174–188 Hz, US 180–193 Hz median). Labels stay front-on and legible, there is exactly one bottle per hand, and there is no on-screen text.

## Known nits
- Transcripts spell the wine names oddly ("Scoronto", "Sasukea"), which is normal for the speech-to-text. Have someone listen for the pronunciation of Scarànto before sign-off.
- Take 1's trailing ad-lib ("Mad" / "Crazy") is soft and partly a laugh, so it's easy to trim if it doesn't land.
