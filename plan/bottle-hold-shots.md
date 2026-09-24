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

**White wine variant:** for a white bottle, the wine in the glass in the scene must be white too. Replace the paragraph starting "The only change:" with:

```
The only changes: (1) she now holds the bottle from the product reference image up toward the camera with BOTH hands, at about chest height, centred in frame, front label facing the camera squarely, fully visible and not covered by her fingers. One hand cradles the base, the other holds the body/shoulder of the bottle. Relaxed, natural grip, arms comfortable, a warm, genuine slight smile at the lens. (2) The glass of wine in the scene now contains WHITE wine instead of red: a clear, pale straw-gold white wine. Keep the same glass, the same fill level, the same position and the same reflections and lighting on the glass.
```

### Step 2: 4s clip
- Model: `kling3_0`, mode `pro`, aspect `9:16`, duration `4`, sound `off`, 6 credits per clip (Seedance 2.5 costs 48 credits for the same clip)
- Media: the chosen still as `start_image`
- White wine bottle: add this sentence before "No camera zoom": `The wine in the glass in the scene stays pale straw-gold white wine throughout.`

Prompt:

```
Locked-off vertical smartphone UGC shot, same framing as the start frame throughout. The woman holds the wine bottle steady in both hands at chest height, front label facing the camera squarely the whole time. She gives a small, natural, warm smile to the lens, a subtle breath and a tiny relaxed shift of her shoulders; the bottle moves only very slightly with her hands. Very gentle handheld phone sway. The bottle keeps its exact shape, glass colour and label — label text and design stay sharp, legible and unchanged, never covered by her fingers. No camera zoom or push-in, no cuts, no talking, no mouth movement, no added text or graphics.
```

## Shots

| # | Bottle | Bottle ref (media id) | Start frame (chosen) | 4s clip |
|---|---|---|---|---|
| 1 | Bottle 1 (screenshot upload) | `62c45db9-c994-4eab-88da-bd1589542755` | B: `4198faa2-6f23-449e-851a-116303f14f75` ([png](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_160218_4198faa2-6f23-449e-851a-116303f14f75.png)) | `d35dcb13-7f5b-421b-8f47-294256f2b74b` ([mp4](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_160758_d35dcb13-7f5b-421b-8f47-294256f2b74b.mp4)) |
| 2 | Bottle 2, **white** (Screenshot 13.24.10); glass changed to white wine | `53380bd0-04b9-431b-a22c-9c85bb926375` | B: `29b36c39-58ae-4bc3-8377-9ac98533cdbe` ([png](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_161426_29b36c39-58ae-4bc3-8377-9ac98533cdbe.png)) | `c2f91e46-1ac8-46ba-a10a-2ffe1ee96954` ([mp4](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_162705_c2f91e46-1ac8-46ba-a10a-2ffe1ee96954.mp4)) |
| 3 | Bottle 3, red (Screenshot 13.25.07) | `b7836d6c-a4e1-4df2-9d5e-1f28e777b5b6` | B: `b86a4106-2fe2-4010-ae0d-034f9b4b0135` ([png](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_161426_b86a4106-2fe2-4010-ae0d-034f9b4b0135.png)) | `b94b3140-4458-4322-a3a7-5be5bd705c3f` ([mp4](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_162657_b94b3140-4458-4322-a3a7-5be5bd705c3f.mp4)) |
| 4 | Bottle 4, red (Dolum Estates) | `ce98b238-e22c-4468-91e0-4d13208498da` | A: `45baef2e-2951-4042-9089-b8c8a2d5eaad` ([png](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_161426_45baef2e-2951-4042-9089-b8c8a2d5eaad.png)) | `efc8b4b3-d4d6-43c0-a5f1-d1e3faa6d3a4` ([mp4](https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260924_162657_efc8b4b3-d4d6-43c0-a5f1-d1e3faa6d3a4.mp4)) |

Unused frames: 1A `81c73529-d013-4550-ae0f-bcc552092be8`, 2A `e2916db5-a3f5-4bc1-bcbc-715f0aa7dc4c`, 3A `9096fc17-85d9-4eb4-864b-9186a8491679`, 4B `b0b8618e-40e0-46b2-95c3-afc56787576d`.
