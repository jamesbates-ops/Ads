# Dolum Estates (Napa Cabernet) — sommelier to-camera clips

This follows the same format as `plan/scaranto-sommelier-to-camera.md`. A sommelier talks to camera behind a marble counter in a fine-wine shop, and the editors add the B-roll and the countdown clock above him.

- **Shot:** every clip is generated from the seed image as its first frame with a locked camera, so the framing, counter, shelves and FINE WINES sign match the seed in every clip.
- **Seed:** Higgsfield media `486c92de-5e58-4b48-8d90-557a14a21eb6`, the same still as Scaranto (2.webp, re-sent as 7.webp, byte-identical).
- **Model:** Gemini Omni Flash 1.1, image-to-video, 1080p.
- **Voice:** changed to **Callum** (preset `858499d9-fef5-40e1-bc29-b4dc661dc283`), with a British delivery.
- **Format:** 1080×1920, 24 fps, H.264 + AAC 48 kHz stereo, loudness matched to −14 LUFS, trimmed to speech (0.12 s head, 0.25 s tail).
- **Checks:**
  - Every voiced clip was checked against a Whisper transcript: all words present and in order.
  - Every clip was scanned frame by frame for burned-in text.

## Deliverables

| File | Link / location |
|---|---|
| Full-quality ZIP (16 clips + 3 full cuts, 488 MB) | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/74b4cc2c-c9d4-46d9-a4b9-2b7e6b5a1abe.zip |
| Smaller ZIPs sent directly (2 parts) | `output/dolum-sommelier/share/` (not committed) |

- **Full cuts:** `dolum_full_hook{1,2,3}.mp4` are each hook followed by B01–B13. They run 1:32.9, 1:31.7 and 1:31.7.
- **Trim points:** `output/dolum-sommelier/clip_timings.json`.

## Clips

| Clip | Section | Line as spoken | Length |
|---|---|---|---|
| H1 | Interrupt | "I have just this long to sell this wine to you, and show you why it's the deal of the year." *(glances up at the clock)* | 7.15 s |
| H2 | Interrupt | "Prohibition almost killed Napa. You've got until that clock stops to taste how it came back." *(glance)* | 5.91 s |
| H3 | Interrupt | "A ninety-four point Napa Cab, and it's only this price until the timer hits zero." *(glance)* | 5.93 s |
| B01 | Gap | "When Prohibition hit in 1920, most of Napa's wineries shut down. It took until 1966 for anyone to build a major new one." | 8.37 s |
| B02 | Gap | "That was Mondavi, in Oakville." | 2.37 s |
| B03 | Gap | "And in 1979, he and Baron Philippe de Rothschild of Mouton started Opus One right there." | 6.75 s |
| B04 | Gap | "The rest, as they say, is history. Award after award, and a world-renowned vineyard that grows some of the finest red wine in the world." | 9.33 s |
| B05 | Gap | "Just… at four hundred dollars per bottle." | 3.31 s |
| B06 | Stake + mechanism | "But this here, is Dolum Estates. Founder Chad Alexander grew up on Mount Veeder, and made wine at the prestigious Hess Persson and Robert Craig." | 9.43 s |
| B07 | Stake + mechanism | "He uses those connections to buy Cabernet from Oakville and Stags Leap District, the best in Napa." | 6.69 s |
| B08 | Stake + mechanism | "And then he ages this in imported, charred French oak barrels." | 4.81 s |
| B09 | Revelation | "The soil gives a flinty, graphite edge at the front, mixed with this beautiful blackcurrant." | 6.29 s |
| B10 | Revelation | "And with a wine of this heritage, the finish is long and slow, with sweet cedar interspersed by espresso and dark chocolate." | 8.31 s |
| B11 | Proof | "Decanter gave it ninety-four, and our members rate it four and a half out of five." | 5.11 s |
| B12 | CTA | "Like Opus One, this wine retails above eighty dollars minimum. But Casedrops have bought too much." | 6.25 s |
| B13 | CTA | "Until the timer runs out, a case of this is under twenty bucks a bottle on their app. Tap below before it hits zero." *(glance; nod down)* | 7.75 s |

B01–B13 run 1:25. With a hook in front, a full cut is about 1:32. As requested, the script's own section timings were disregarded.

## Notes for the edit

- **"Robert Mondavi" can't be generated.** The video model's content filter blocked every take containing "Robert Mondavi", including a phonetic spelling, so B02 says "That was Mondavi, in Oakville." B03's "he" still refers back to him. The original line was split across B02 and B03 for this reason, so butt them together with no gap.
- **Timer glances:** on "just this long", "that clock" and "the timer" (H1–H3, B13) he glances briefly at the space above his head, where the countdown clock goes.
- **Pronunciations to listen for:** Dolum (written "Doh-lum" in his line), Mount Veeder, Hess Persson, Mouton (one take said "Mutant"; it was retaken), Rothschild. All of these transcribe as expected.
- **Text overlays:** the first takes of H1 and B06 came back with burned-in captions and were retaken. Quoted gesture cues in the prompt caused it, so the retakes describe the gestures in plain words.
- **Claims to verify before the ad runs** (all voiced as scripted):
  - **History:** Prohibition 1920; the Mondavi winery in 1966 as the first major new Napa winery; Opus One founded in 1979 by Mondavi and Baron Philippe de Rothschild.
  - **Opus One prices:** $400 a bottle, and "retails above $80 minimum" (as worded, "Like Opus One" reads as though Opus One is also around $80).
  - **Chad Alexander:** that he grew up on Mount Veeder and made wine at Hess Persson and Robert Craig.
  - **Sourcing and oak:** Oakville and Stags Leap fruit, and charred French oak.
  - **Ratings:** Decanter 94 and members' 4.5/5.
  - **Offer:** under $20 a bottle per case on the Casedrops app, and the time-limited offer.

## Generation ledger (Higgsfield)

| Clip | Talking job (i2v, 1080p) | Voice-changed job |
|---|---|---|
| H1 | `b0d92663-cdfa-4f47-99d9-225d0df150f8` (retake; `cfe58187` had a burned-in caption) | `b3b3012e-5ecb-48b2-82f2-07b949203a24` |
| H2 | `e3766cea-46e2-4653-b4aa-d22fc82f82f5` | `5a40f726-d108-476e-b837-8172187f49b4` |
| H3 | `4de303bc-fed8-4ecc-b177-a2be1d22800a` | `ccd366c2-005c-404d-8a15-9eff1ea2cadb` |
| B01 | `6f1fe0d2-ebc7-4c6c-a282-50c240f2b46f` | `0c4a86d3-0a09-4f8a-bef7-401fe53e8e29` |
| B02 | `243a7963-8703-452c-88b0-3ef5adeddf30` ("Robert Mondavi" takes blocked: `e83520b4`, `272fcbb6`, `b87e96bb`, `38a13408`) | `eee6cc8a-f467-4aac-bb8e-e4482421283b` |
| B03 | `46474dbb-5b59-4b17-a712-0f77490503e5` (retake; `84a74746` said "Mutant") | `b44a7e1a-fe78-43fb-a13b-e7b169793dee` |
| B04 | `b99a8a6b-a0e8-431d-9c62-2600bddd1731` | `f9bf8503-ed8b-42c7-a257-2ab37dc8885a` |
| B05 | `343d1f0d-7136-47ab-873c-856a7487b2d0` | `f52211a4-8f93-4d86-ae1c-9b628923eccc` |
| B06 | `433676ac-5f50-4ead-bbfe-0dc347465671` (retake; `9e4c9c35` had a burned-in caption) | `d7dd9035-a64b-498b-acac-ffc3b094d4a7` |
| B07 | `8fc01f73-e39b-4c8b-be44-81bf9847ef7a` | `968cfddd-9212-4a9b-9fbd-03f4f640e721` |
| B08 | `dcbbd678-2c0e-48d4-8bf9-00a403edbecd` | `9fa66fbe-3319-453a-b3fa-f6b0904f04d8` |
| B09 | `a7cb023b-db41-4670-ad63-8e2b9511b4e4` | `4aaf25b7-3b47-49e9-b9bd-af5da8ae352f` |
| B10 | `521e6875-345b-4900-a2b4-c3ce5cc3aee7` | `9c6b701a-bf61-4042-9e09-333f880253cb` |
| B11 | `9961118f-0d07-443e-9719-1b1fd6bdd257` | `b0136bb7-3e81-4279-a7b3-2f1bd115aff7` |
| B12 | `1fe04fc4-cfa9-4e4d-a12f-128f5a610ccc` | `5f1b95c3-af39-459f-b0d0-4d714ec01312` |
| B13 | `9c3ef3cc-5fd0-4067-8511-991f91b4a3a2` | `82422ca8-eaa5-492e-a904-1012441bb796` |
