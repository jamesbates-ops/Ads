# Ode de Bellecôte UGC ad

9:16 hyper-real UGC talking-head A-roll for Ode de Bellecôte Châteauneuf-du-Pape, in a **UK (British accent)** and a **US (American accent)** version. Same presenter, kitchen and setup as the Scarànto ad. This is raw footage only: the editors add the price cards, b-roll and end card. The script is in [`SCRIPT.md`](SCRIPT.md).

## Downloads

Full-quality takes, zipped (1080×1920, 24 fps, iPhone-style diegetic audio):
- UK: https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/5dd2c9d1-3277-4b50-a06f-2abe529fd2dc.zip (42 MB)
- US: https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/4d3a538a-fddc-46e8-b1a4-0b8452539e56.zip (41 MB)

Each zip contains `take1_hook_point_up_8s`, `take2_scores_price_20s` and `take3_tasting_close_16s`.

Review rough cuts (three takes butted together, loudness matched to about -16 LUFS, no overlays): `aroll/UK_aroll_roughcut.mp4` and `aroll/US_aroll_roughcut.mp4`, both 44s.

Higgsfield job IDs: UK `4859fa09…` (take 1), `211239aa…` (take 2, before the fix), `a2e122ea…` (take 3), plus `27c4c4b0…` (take 2 line fix) · US `9420170c…`, `b453229b…`, `28a159b0…`.

## How it was made
- Seed: `seed_ode_de_bellecote.png`, which is the Scarànto seed with the bottle swapped for the supplied packshot (`reference/ode_de_bellecote_packshot.png`) using GPT Image 2.5. Clear wall space above her head is left for the price cards.
- Takes: Seedance 2.5 image-to-video with native audio at 1080p, one continuous take each. Both versions were steered from the first take with a voice reference: the UK takes use her British voice from the Scarànto UK take, and the US takes use her American voice from the Scarànto US take. She sounds like the same creator across both ads.
- UK take 2 fix: she said "Teller-Trier" for CellarTracker and "Leeve" for Leve. Only that line (6.80–10.61s) was re-rendered and spliced back in during the pauses either side, so the rest of the take is untouched. A forced-choice recogniser now picks "CellarTracker" (0.54 vs 0.50) and "Lev" (0.54 vs 0.49).

## Checks
- Every take was transcribed, and every scripted line is present, including "twenty-one quid", "nine hundred quid", "under forty bucks" and "a thousand dollars".
- Accent classifier: all UK takes read as England and all US takes as US.
- Voice pitch is consistent within each version. The patched UK line is 176 Hz against 180 Hz for the original line.
- Exactly one bottle, label front-on, no on-screen text, natural hands.

## Known nits
- US take 1 "points up" with a raised open palm while looking up, rather than a pointed finger as in the UK take. It still reads as "look up there" for the price cards. I can re-render it (about 96 credits) if you want a finger point.
- The accent classifier is unsure on two very short tails, UK take 1's "…these. Mmm" and UK take 3's "So grab yours today". All full sentences score clearly English, but those two moments are worth a quick listen.
