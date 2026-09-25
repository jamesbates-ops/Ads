# Winedrops ASMR box ad: plan

This ad replaces the Frankie & Chris phone-call idea. It has no dialogue, music or people, only hands.

Format: one continuous shot in vertical 9:16 at 1080p, about **23 seconds** long. The camera is locked off and does not move until the final pull-back. The Winedrops delivery box sits on a patio table. A hand sets six bottles of the same wine down in front of it, one at a time. Each bottle lands on the marble with a clean glass clink. Birdsong from the tree plays the whole way through. At the end, the camera slowly pulls back a little with the box and bottles still centred, and holds on the wider shot.

## Seed images (Higgsfield media)

| Role | What it shows | media_id |
|---|---|---|
| Table setting | Sunny outdoor patio: herringbone red-brown brick paving, round white marble table, ornate dark metal chairs, a leafy tree casting dappled shade, a red brick wall with built-in planters, and a white wall with black-framed glass doors | `95e4b22c-40d7-43c4-bd20-bd0f3f1217ac` |
| Wine | Dark glass bottle with a maroon foil capsule and a dark label with a gold "E" crest, gold/white lettering and a small red bird emblem | `a0f72f8b-0e2d-4378-92d5-778ba7558c0d` |
| Box | Brown cardboard Winedrops delivery box with purple printing. The seed photo is a selfie, so only the box is used. | `0861f5e1-5fe0-4da1-bdc1-f2af2b19e89c` |

## Timeline

Timecodes are mm:ss.s.

| # | In | Out | Dur | Action | Sound |
|---|---|---|---|---|---|
| 1 | 00:00.0 | 00:01.5 | 1.5s | Box alone on the marble table. Leaf shadows drift slightly across the tabletop. | Birdsong, a faint breeze in the leaves |
| 2 | 00:01.5 | 00:04.5 | 3.0s | A hand comes in from frame right with bottle 1. It sets the bottle upright in front of the box, far left of the row, and leaves. | Soft glass-on-marble **clink** as it lands (~00:03.0) |
| 3 | 00:04.5 | 00:07.5 | 3.0s | Bottle 2 goes next to bottle 1. | Clink (~00:06.0) |
| 4 | 00:07.5 | 00:10.5 | 3.0s | Bottle 3. | Clink (~00:09.0) |
| 5 | 00:10.5 | 00:13.5 | 3.0s | Bottle 4. | Clink (~00:12.0) |
| 6 | 00:13.5 | 00:16.5 | 3.0s | Bottle 5. | Clink (~00:15.0) |
| 7 | 00:16.5 | 00:19.0 | 2.5s | Bottle 6 finishes the row. The hand leaves and nothing moves. | Last clink (~00:17.8), then birdsong only |
| 8 | 00:19.0 | 00:23.0 | 4.0s | Slow, eased pull-back to about 15% wider. The box and six bottles stay centred, and more of the patio shows at the edges. Hold on the wider frame. | Birdsong continues and fades slightly at the end |

For the end card, put the logo and CTA over the held wide frame in shot 8, in the space above the box. There is no separate end card, so the ad ends on the scene without a cut. Editors supply the brand assets.

Label direction: every bottle is set down with its label facing the camera, so the finished row reads as six matching labels.

## How it is generated

1. **Start frame.** Generate a 9:16 still of the box on the patio table, with the table front clear for the bottles. It uses Nano Banana Pro at 2K with the table and box seeds as references. The user approves it before any video is made.
2. **Video.** Use Seedance 2.5 (`seedance_2_5`, `omni_reference` mode) at 1080p and 9:16 with native audio on. The approved start frame goes in as `start_image` and the wine seed as an `image_reference`, so the bottles match the real label.
   - Plan A is a single 22–23s take, which the model supports up to 30s. It gives one continuous shot and one continuous audio bed.
   - Plan B applies if the model miscounts bottles or drifts. Generate it in three parts, each continuing the last with `video_extension` (forward): bottles 1–3 (~10.5s), bottles 4–6 (~8.5s), then the pull-back (~4s). Any bad part can be regenerated without redoing the rest.
   - Wan 3.0 (`wan3_0`) is the fallback model. It also does start/end frames and native audio up to 30s.
3. **Sound.** The clinks and birdsong come from the video model's own audio, so each clink lines up with its bottle landing. Higgsfield has no separate sound-effects model for standalone use. If the clinks come out weak or muddy, the editors should layer library SFX on the landing frames listed above.

## Video prompt (Plan A)

> Locked-off static shot, vertical, photoreal. A brown cardboard Winedrops delivery box with purple printing sits centred on a round white marble table on a sunny brick patio, with dappled leaf shadows gently moving across the table. The camera does not move. One at a time, a hand enters from the right holding a dark wine bottle with a maroon foil capsule and a black label with gold lettering and a small red bird (exactly like the reference bottle). The hand sets the bottle down upright on the marble in front of the box, label facing the camera, with a soft crisp glass clink, then leaves the frame. This repeats slowly and calmly until there are exactly six identical bottles standing in a neat row in front of the box, evenly spaced. After the sixth bottle nothing moves for a moment. Then the camera slowly and smoothly pulls back to a slightly wider framing, keeping the box and the six bottles centred, revealing more of the patio, and holds. Audio: ASMR. Gentle birdsong from the tree throughout, a faint breeze in the leaves, and a clean delicate glass-on-marble clink each time a bottle lands. No music, no voices, no speech.

## Approved start frame

Frame 1 of 2 was approved (job `cef8b96e-d47e-455e-9a0e-6a1f4f396352`, 1536×2752). The Winedrops box sits in the centre foreground of a long white marble table on the brick patio. Behind it are a large white-and-pink flower arrangement, wine glasses and a silver ice bucket, with the trees and brick softly out of focus.

- Still: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260925_110452_cef8b96e-d47e-455e-9a0e-6a1f4f396352.png
- Rejected alternative (round table): https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260925_110452_b0dd5c8d-1e02-41e7-8169-66ac411e1690.png

## Video takes

All takes are 1080×1920 at 24 fps, 23.05s long, with stereo audio at 32 kHz. None of them contains speech. This was checked with Whisper, but the timings below come from audio-transient and motion analysis, not from watching the takes. Bottle count and label orientation still need someone to check by eye.

| Take | Model | Job | Clinks (strong transients) | Hand activity | Pull-back | Notes |
|---|---|---|---|---|---|---|
| A | Seedance 2.5 | `6d094bac-89a8-4efd-9f3f-aee20a90db3f` | ~6.2, 8.6, 11.2, 13.5, 14.5, 15.8s | Six separate bursts at ~5, 8, 10.5, 13, 14.5 and 16.5s, still between | 18.5–23s, eased in and out | Most even rhythm; clinks quieter |
| B | Seedance 2.5 | `c4d5b2ee-cfd8-486f-9d5d-8993b98c6787` | 6.0, 8.3, 10.3, 12.2, 13.5, 14.5s | Continuous 4.5–14.5s | 19–23s | Loudest, cleanest clinks; placements speed up towards the end |
| C | Wan 3.0 | `80043fd2-fbed-4e54-80fd-f0d2ac357469` | Irregular: 4.4, 8.8, 15.3, 18.2, 19.2s | Only ~4–5 bursts (2.5, 5.5, 11, 13–14.5s) | Starts early at ~16s and overlaps clinks at 18–19s | Weakest. Audio ~13 dB quieter, 30 fps, and the bottle comes from the text description only because Wan can't combine a start frame with reference images. |

Both Seedance takes open with about 4.5s of stillness before the first hand appears, which is longer than the 1.5s in the plan. Trimming the first ~3s in the edit brings the first bottle in at ~1.5–2s and gives a ~20s ad.

- Take A: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260925_111045_6d094bac-89a8-4efd-9f3f-aee20a90db3f.mp4
- Take B: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260925_111045_c4d5b2ee-cfd8-486f-9d5d-8993b98c6787.mp4
- Take C: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260925_111056_80043fd2-fbed-4e54-80fd-f0d2ac357469.mp4

## Revision 2: take B with the correct box and a sixth bottle

Feedback: take B worked best as a video, but it only shows five bottles, and the box carried the wrong logo. The corrected box image is media `598a3ccd-d96b-46fd-b1d2-3e304def36b8`.

What was done:

1. **Trim.** Take B was cut to 3.0–18.0s (media `46caab7b-abc4-4c2a-91bf-afabeec888bd`). That leaves 1.5s of stillness, then bottles 1–5, ending on a still frame before the original pull-back.
2. **Box swap, two versions.** Genjutsu (`hf_mult_replace_object`, job `246f1496-8cab-4520-8516-28afc52c06ad`) and Seedance 2.5 `video_edit` (job `be6c89f7-f8ac-4080-be67-f5135dbd4eae`) both ran at 1080p. Both came back 7 frames short (14.71s) and drifted up to 4 frames ahead of the audio. Each was stretched back to exactly 15.0s, which puts it within 1 frame of the original motion, and take B's original audio was laid back on. The results are media `74fe0c29-…` (Genjutsu) and `835955a6-…` (Seedance).
3. **Sixth bottle and pull-back.** Each corrected clip was extended forward 8s with Seedance 2.5 `video_extension` (jobs `0af155aa-cb64-4601-827a-c902111b84dd` and `42fdd6fc-2b8e-42db-a0fb-ee2c8fbcbd08`). A hand sets a sixth bottle centred in front of the row of five with one clink (1.7s / 1.5s into the extension), there is a still beat, and then a centred pull-back. At the end the original view fills the middle ~80% (A) or ~84% (B) of the frame.
4. **Assembly.** Each clip was joined to its extension with a 4-frame blend at the join. The extension's birdsong was raised ~6 dB to match the original, and the audio fades in over 0.25s and out over 1.0s. Loudness was normalised with a linear gain and peaks capped at -1.5 dBTP. The mix is **not** limited up to -14 LUFS because that would squash the clinks. It lands at -17.5 LUFS (A) and -18.4 LUFS (B), and platforms raise or lower it from there.
5. **Updated still.** The approved start frame was re-rendered with the corrected box (job `8883bde1-3301-475a-826d-2d5e7344c198`). Only the box area changed: mean pixel difference elsewhere is ≤2/255.

### Final cuts (23.0s, 1080×1920, 24 fps, AAC 256k)

| Cut | Box swap | URL |
|---|---|---|
| Final A | Genjutsu | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/86edb98e-6336-4587-bd0e-7cdaeeb4e110.mp4 |
| Final B | Seedance video edit | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/49942b81-76a2-4283-9eaa-2f517756a9f6.mp4 |

Timeline of the finals: first hand at ~1.5s; clinks for bottles 1–5 at about 3.0, 5.3, 7.3, 9.2 and 11.5s; bottle 6 lands at ~16.7s (A) / ~16.5s (B); pull-back from ~18.5s to the end.

**Final B was approved** and became the master for the bottle variants below.

## Bottle variants (Ad Multiplier from Final B)

Final B (media `49942b81-76a2-4283-9eaa-2f517756a9f6`, 22.999s) was re-rendered with Higgsfield Ad Multiplier (`video_edit`, 1080p, silent render). Each version swaps every placed bottle for one new wine, keeping the hand motion, timing, pull-back and Casedrops box. Versions 1 and 5 also swap the box back to the original **Winedrops** box. The reference for that box is the approved start frame (job `cef8b96e-…`), not the selfie seed, so no person could leak into the render.

Ad Multiplier returned every version 7 frames short (545 of 552 frames). Each was stretched by ×1.0128 back to exactly 22.999s and given Final B's original audio (clinks and birdsong), so each bottle lands on its original clink. QC on every final: 23.0s, 1080×1920, AAC, and motion sync against Final B within ±2 frames in all four windows.

| Output | Bottle reference | Box | Ad Multiplier job | Final |
|---|---|---|---|---|
| 1 | `915dcf31-…` dark glass, black label with gold script, red seal | Winedrops | `f9d9e64b-0e02-459d-9275-91770b0ebb5e` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/46652a3e-967a-4c6f-a491-f90a9d856750.mp4 |
| 2 | `7153bc7f-…` green glass white wine, white label with green border | Casedrops | `0718a263-f48a-480d-8932-c33c0a6394e1` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/e5bb2d8f-706b-44c4-9617-90d303392825.mp4 |
| 3 | `dc39f0c8-…` dark glass, cream textured label with red crest | Casedrops | `dbf7d67a-7ca4-4431-ada1-c3165028f7c8` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/8f15d2f4-cf94-429e-8478-fa772d0fb02b.mp4 |
| 4 | `90418787-…` Dolum Estates, white label with triangle graphic | Casedrops | `25a5120e-6320-4759-8de7-3a8bf5f22618` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/d661a61c-91c1-4e7d-b066-d6920feef122.mp4 |
| 5 | `aa8b32d6-…` dark glass, mosaic sun label | Winedrops | `1306e81f-2896-4cb4-8953-35b44ba741da` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/5b83e10e-725a-4f1c-b7c3-1e5fe425ae60.mp4 |

Checked by measurement only. Label text, bottle shape and the box logo still need a look by eye.

Still to check by eye on Final B:
- The logo on the box. Genjutsu's prompt rewriter read the new box as "Casedrops", so check that the brand name renders correctly.
- The sixth bottle's label.
- The join at 15.0s.
