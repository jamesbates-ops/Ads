# Bottle hold shots: 4 × 4s, 9:16

One short insert per bottle: the woman from the seed image holds the bottle to camera in both hands, with the same framing as the seed image. The editors splice these into the main cut, so each clip is silent.

Seed image (framing, woman, set, light): Higgsfield media `d7653e47-e126-44d6-8a6e-45fe189b4777`

## Recipe (identical for every bottle; only the bottle reference changes)

### Step 1: start frame (still)
- Model: `gpt_image_2_5` (flare), quality `high`, resolution `2k`, aspect `9:16` (renders 1520×2688)
- References (`image_references`): seed image, then the bottle image
- Generate 2 variants and pick one by eye, checking the framing, the label text and the face

Prompt:

```
Edit the photo of the woman. Keep that photo exactly as it is: the same woman (identical face, hair, makeup, skin, expression style), the same clothing, the same room and background, the same lighting and colour grade, and the same camera position, lens, distance, angle and crop. Do not reframe, zoom or move the camera.

The only change: she now holds the bottle from the product reference image up toward the camera with BOTH hands, at about chest height, centred in frame, front label facing the camera squarely, fully visible and not covered by her fingers. One hand cradles the base, the other holds the body/shoulder of the bottle. Relaxed, natural grip, arms comfortable, a warm, genuine slight smile at the lens.

Reproduce the bottle exactly as in the product reference: same bottle shape and proportions, glass colour, capsule/closure, label design, colours, logo and all label text spelled exactly as shown. Realistic scale for a bottle in a woman's hands.

Authentic UGC smartphone photo, vertical 9:16, natural skin texture, no retouched look, no added text, captions, graphics or watermarks.
```

### Step 2: 4s clip
- Model: `kling3_0`, mode `pro`, aspect `9:16`, duration `4`, sound `off`, 6 credits per clip (Seedance 2.5 costs 48 credits for the same clip)
- Media: the chosen still as `start_image`

Prompt:

```
Locked-off vertical smartphone UGC shot, same framing as the start frame throughout. The woman holds the wine bottle steady in both hands at chest height, front label facing the camera squarely the whole time. She gives a small, natural, warm smile to the lens, a subtle breath and a tiny relaxed shift of her shoulders; the bottle moves only very slightly with her hands. Very gentle handheld phone sway. The bottle keeps its exact shape, glass colour and label — label text and design stay sharp, legible and unchanged, never covered by her fingers. No camera zoom or push-in, no cuts, no talking, no mouth movement, no added text or graphics.
```

## Shots

| # | Bottle | Bottle ref (media id) | Start frame (chosen) | 4s clip |
|---|---|---|---|---|
| 1 | Bottle 1 (screenshot upload) | `62c45db9-c994-4eab-88da-bd1589542755` | B: `4198faa2-6f23-449e-851a-116303f14f75` ([png](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_160218_4198faa2-6f23-449e-851a-116303f14f75.png)) | `d35dcb13-7f5b-421b-8f47-294256f2b74b` ([mp4](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_160758_d35dcb13-7f5b-421b-8f47-294256f2b74b.mp4)) |
| 2 | — | — | — | — |
| 3 | — | — | — | — |
| 4 | — | — | — | — |

Frame A for bottle 1, not used: `81c73529-d013-4550-ae0f-bcc552092be8`.
