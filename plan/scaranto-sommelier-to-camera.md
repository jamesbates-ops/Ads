# Scaranto (Super Tuscan) — sommelier to-camera clips

A sommelier talks to camera behind a marble counter in a fine-wine shop. Editors add the B-roll and the countdown clock above him. Every clip is generated from the seed image as its **first frame** with a locked camera, so the framing, counter, shelves and FINE WINES sign match the seed in every clip. Each clip opens on the seed's closed-mouth pose, trimmed to just before he speaks.

- Seed: Higgsfield media `486c92de-5e58-4b48-8d90-557a14a21eb6` (the supplied still, centre-cropped from 1131×2000 to 1125×2000 for exact 9:16).
- Model: Gemini Omni Flash 1.1, image-to-video, 1080p. Voice changed to **Callum** (preset `858499d9-fef5-40e1-bc29-b4dc661dc283`), British delivery.
- 1080×1920, 24 fps, H.264 + AAC 48 kHz stereo, loudness matched to −14 LUFS, trimmed to speech (0.12 s head, 0.25 s tail).

## Deliverables

| File | Link |
|---|---|
| ZIP of all 14 clips (128 MB) | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/7ec82538-0681-4afe-b3e1-c5ff724ca6f6.zip |

Six smaller ZIPs under 30 MB each (H1–H3, B1–B2, B3–B4, B5–B7, B8–B10, B11) were sent directly. None of the media is committed. `output/scaranto-sommelier/clip_timings.json` holds the trim points.

## Clips

| Clip | Section | Line as spoken | Length |
|---|---|---|---|
| H1 | Interrupt | "Before that timer runs out, you'll want to hear how this wine came about." | 4.99 s |
| H2 | Interrupt | "This bottle has a story worthy of any dinner party, and it's only here until that clock stops." | 5.67 s |
| H3 | Interrupt | "A few Tuscan families broke the rules to make this wine. You've got until the timer ends to try it." | 6.25 s |
| B1 | Gap | "Back in the seventies, Chianti law told Tuscan winemakers what grapes to use. All of them Italian." | 6.55 s |
| B2 | Gap | "But a few families planted Merlot and Cabernet anyway, and sold the results as plain table wine. Thing is, people loved it." | 7.73 s |
| B3 | Gap | "And over time, those wines were so good, they grew world famous. Now, we all know bottles like Sassicaia and Tignanello, and the name: Super Tuscans." | 9.94 s |
| B4 | Producer | "Scaranto is made by Matteo Bernabei and his dad Franco, one of the best-known winemakers in Tuscany." | 6.95 s |
| B5 | Method | "They named this one Governo after an old farmhouse trick: some grapes are dried, then added back in, so the wine comes out softer and rounder." | 9.29 s |
| B6 | Method | "They're then aged in French oak, and given a distinctly French richness to the profile." | 5.33 s |
| B7 | Stake | "Sassicaia and Tignanello are old guard. They're super expensive, super Tuscans. This one, is their alternative younger brother." | 6.63 s |
| B8 | Taste | "You get a full-bodied wine with these melting tannins. And on the palate, black cherry, dried rose and a hint of tobacco." | 7.75 s |
| B9 | Proof | "Luca Maroni gave it ninety-nine, and the Italian Wine Guy gave it a hundred. That clock hasn't stopped by the way." | 7.37 s |
| B10 | Offer | "Right now, this bottle should be fifty pounds per bottle. Winedrops will do it for twelve pounds. And free delivery." | 7.45 s |
| B11 | CTA | "When the timer hits zero, this offer's gone. So tap below, and show off when you're next hosting." | 5.69 s |

Hooks plus body run about 1:39 of speech (H1 + B1–B11 ≈ 1:36). Every revoiced clip was checked against a Whisper transcript (all words present, in order) and scanned frame by frame for burned-in text.

## Notes for the edit

- **Timer glances:** on "that timer" / "that clock" / "the timer" (H1, H2, H3, B9, B11) he was directed to glance up briefly at the space above his head, where the countdown clock goes.
- **B7** finishes on "younger brother" with a slightly rising, mid-sentence intonation. The take ran on and the clip is cut just after "brother". A cleaner-ending retake failed on Higgsfield's side; it can be retried.
- **Pronunciations to listen for:** Sassicaia, Tignanello, Scaranto, Bernabei, Governo. All transcribe correctly, which suggests they're pronounced right.
- **Claims to verify before the ad runs** (voiced as scripted): Luca Maroni 99, Italian Wine Guy 100, £50 value vs £12 on Winedrops with free delivery, Franco Bernabei as one of the best-known winemakers in Tuscany, and the time-limited offer.

## Generation ledger (Higgsfield)

| Clip | Talking job (i2v, 1080p) | Voice-changed job |
|---|---|---|
| H1 | `50097571-bff1-4bb8-9f74-0df1383af74c` (retake; `57009f3e` had burned-in subtitles) | `3b8a9c8d-a047-4a23-9be7-804b6dad5ed7` |
| H2 | `f35a6194-3642-4364-b625-d12eabdc4426` | `282b7305-b4f2-47d9-b9f7-45899c6a3dff` |
| H3 | `8a7e715e-39c1-4020-996f-2627695e1b91` | `a4eb700c-e884-45e9-9d80-288daf5b0ce5` |
| B1 | `89a6017f-eb56-4b57-9065-b3f7f3a6d203` | `337fe990-7538-4159-856e-46532a2c1db9` |
| B2 | `13c8c440-525e-4bd4-a7e7-c5f0a4f04c7e` | `cf5a563a-4d58-4b8d-af4f-09b2bb53779e` |
| B3 | `c645d2d7-51db-47de-97e2-43dda55c7250` | `926a05ca-8900-4457-830c-33d437c48327` |
| B4 | `4373fd73-49fe-4671-959c-9d32b541d654` | `9e6765b7-1812-4750-be64-eb4d775b5c9c` |
| B5 | `13751300-bb89-4e62-a1d9-1244b2756549` | `6fe3de97-dac5-408a-a4e0-0cbf5098779e` |
| B6 | `dacff30b-e853-4429-8289-633bb5d97f94` | `9b76ce18-2947-4a3a-82bd-31e34087bb5a` |
| B7 | `0c5d4eb9-d1b0-4ade-91ec-a96c536a3c93` (retake, cut at 6.72 s; `3a3fc376` ran out of time before "brother") | `bed1859f-4d52-49a7-92f6-fc8ef4beea77` |
| B8 | `4c1fc5c2-cce0-4417-b048-10fe9ad9d721` | `ecaf77c1-3b14-4d61-94b4-e55fd02098fc` |
| B9 | `488e8970-eb9a-47eb-8a30-4353d0796dda` | `bf2bd456-d4ec-45c9-b620-3eb98fe3d4ce` |
| B10 | `b0748b81-b820-490b-a2e6-5ad60e2f5e93` | `c14bec30-3c91-410f-a92b-0a626e6656e3` |
| B11 | `baa7d231-4558-4b95-a93f-0075223567ff` (retake; `1397d7a9` had burned-in subtitles) | `7ee79b99-9139-4adb-a80d-a5fc141f5137` |
