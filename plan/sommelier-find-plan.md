# The Sommelier's Find — build notes and timeline

Brief: "The Sommelier's Find", editor brief, straight to camera, 9:16, target 1:04, four cuts that differ only in the opening hook. Talent, setting and both seed frames (Frame A bottle in hand, Frame B glass in hand) come from the brief. Everything was generated and assembled on Higgsfield.

## Deliverables

| Cut | Hook line | Length | File |
|---|---|---|---|
| 1 | "It's the only place I buy my wine…" | 1:14.1 | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/3dd993ca-9965-4af2-a520-b8fa0b682075.mp4 |
| 2 | "Trust me, Châteauneuf can be this affordable…" | 1:14.1 | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/c2f2710c-6daf-4fe1-9c16-ed5a2f1c8cc2.mp4 |
| 3 | "This is where I buy all my Châteauneuf" | 1:14.1 | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/0f2159a2-b9ff-4b45-b197-4a9b5f4e7a27.mp4 |
| 4 | "If you don't like Châteauneuf, keep scrolling…" | 1:14.1 | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/83e47888-6eaf-44a7-a2d3-458ee86a44c1.mp4 |

1080×1920, 24 fps, H.264 + AAC. Shots 2 to 11 are byte-identical across the four cuts (one shared body master, hook segments concatenated in front), so the timeline is locked from the body start in every cut.

## Timeline (all cuts)

Body starts at 0:04.0 rather than the brief's 0:03. The natural British read of each hook runs 2.0–4.4 s; the slot was locked at 4.0 s for all four so the body stays identical. Hook 3 is played 12% faster to fit. Total VO runs longer than the brief's 1:04 target because the Châteauneuf price line alone takes 11 s at a natural pace; the brief anticipated a cutdown.

| # | In | Out | VO | Frame / graphics |
|---|---|---|---|---|
| 1 | 0:00.0 | 0:04.0 | Hook | Frame A. Hook line burned in. |
| 2 | 0:04.0 | 0:09.1 | Châteauneuf-du-Pape. We all know it. Wine that trades in the thousands. | Frame A. Title "Châteauneuf-du-Pape". |
| 3 | 0:09.1 | 0:21.1 | Henri Bonneau… €1,189, Beaucastel… €951, Rayas 1978… €4,507 | Frame A, no cut. Three price cards build on the names and stack. |
| 4 | 0:21.1 | 0:24.8 | Serious wines, for serious drinkers. | Frame A. Cards hold. |
| 5 | 0:24.8 | 0:32.8 | The grapes are hand-picked… the longer you sip it. | Vineyard B-roll (hand-picking, then galets roulés). Cards hold. Label "Hand-picked · Ancient vines". |
| 6 | 0:32.8 | 0:40.8 | Then again, Châteauneuf prices are expensive… direct from the producer. | Frame B. Cards clear on "Then again". |
| 7 | 0:40.8 | 0:48.1 | Winedrops have spent years negotiating… | Frame B. "Winedrops" wordmark, held clean. |
| 8 | 0:48.1 | 0:53.1 | And this one? They got it so cheap… | Frame B. No graphic. |
| 9 | 0:53.1 | 0:58.2 | A case of six should cost £480, and I just bought mine for £125. | Frame B. Bottle pack-shot super (cut out of Frame A) + "£480 → £125 · Case of 6". |
| 10 | 0:58.2 | 1:04.5 | Over 90 points… exclusive to Winedrops, | Frame B. "90+ points · Exclusive to Winedrops". Runs into 11 without a cut. |
| 11 | 1:04.5 | 1:10.1 | I keep impressing my friends… other luxuries. | Frame B. Holds the look past the line. |
| 12 | 1:10.1 | 1:14.1 | — | End card (placeholder: Winedrops, bottle, £480 → £125, "Exclusive to Winedrops", "Shop the case"). CTA is TBC per brief. |

Captions are burned in throughout, timed from a word-level transcript of the voice track.

## How it was made

- Voice: Higgsfield Seed Audio, preset voice "Callum" (British male). "Châteauneuf" is spelled phonetically in the TTS prompt ("Shatoneuf") to get a consistent pronunciation; the on-screen text uses the correct spelling.
- Lip-sync clips: Seedance 2.5 omni-reference, seed frame as start image and the clean voice track as audio reference. Seven clips: four hooks (Frame A), one 21 s Frame A body (shots 2–4), two Frame B bodies (shots 6–8, shots 9–11).
- B-roll: two 5 s Seedance 2.5 text-to-video clips, 4 s of each used.
- Pack shot: bottle cropped from Frame A, background removed with Higgsfield.
- Audio bed: synthesised low shop room tone under the voice, no music anywhere (per brief). Mix normalised to -14 LUFS.
- Assembly: ffmpeg in the Higgsfield sandbox. Price cards, offer card, wordmark, pills and end card rendered with Pillow in Montserrat ExtraBold; captions via libass.

## Source assets on Higgsfield

- Frame A (bottle): media 58bb154b-2da5-424d-bc8b-9946401bfc27
- Frame B (glass): media dec362c8-6568-40ae-86d6-dd708ccb3803
- Voice tracks and timeline: https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/93425187-9c3b-4e50-b0ac-8f72a9aa655e.tar
- Assembly script: https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/5a462965-06b9-4915-9185-3962bbf37f30.py

## Open points for the editor

- End card / CTA copy is a placeholder; the brief marks it TBC.
- Runtime is 1:14 against a 1:04 target. Cutting shot 5 (B-roll) to 5 s and tightening the gaps between shots 6–8 would bring it to about 1:08 without touching the voice.
- On-screen text lines follow the brief's suggestions and are for approval, not final copy.

## QA checks on the final cuts

- Container: 1080×1920, H.264 24 fps, AAC stereo 48 kHz, 74.15 s per cut.
- Audio bed: brown-noise shop ambience only, no music. End card measures −31.4 LUFS with almost no energy above 1 kHz; the voiced section measures −15.4 LUFS, so the ambience sits about 16 LU under the voice.
- Automated scene analysis of the hook-1 cut confirmed the structure: hook, price cards building during shot 3 and holding over the vineyard B-roll, wordmark in shot 7, bottle pack shot with the offer card in shot 9, end card.
- Frame-level checks of the graphics (price cards, B-roll label, wordmark, offer card and pack shot, exclusive pill, end card) confirmed nothing covers the presenter's face. The offer card's large price originally ran past the card border; the card typography was tightened and all four cuts were re-rendered (v2 URLs above).
