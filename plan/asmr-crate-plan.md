# Winedrops ASMR box ad: plan

This ad replaces the Frankie & Chris phone-call idea. It has no dialogue, music or people, only hands.

Format: one continuous shot in vertical 9:16 at 1080p, about **23 seconds** long. The camera is locked off and does not move until the final pull-back. The Winedrops delivery box sits on a patio table. A hand sets six bottles of the same wine down in front of it, one at a time. Each bottle lands on the marble with a clean glass clink. Birdsong from the tree plays the whole way through. At the end, the camera slowly pulls back a little with the box and bottles still centred, and holds on the wider shot.

## Seed images (Higgsfield media)

| Role | What it shows | media_id |
|---|---|---|
| Table setting | Sunny outdoor patio: herringbone red-brown brick paving, round white marble table, ornate dark metal chairs, a leafy tree casting dappled shade, a red brick wall with built-in planters, and a white wall with black-framed glass doors | `95e4b22c-40d7-43c4-bd20-bd0f3f1217ac` |
| Wine | Dark glass bottle with a maroon foil capsule and a black label with gold/white lettering and a small red bird emblem | `a0f72f8b-0e2d-4378-92d5-778ba7558c0d` |
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

## Files

Filled in as assets are approved.
