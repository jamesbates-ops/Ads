# Trentacoste Primitivo — UGC creator A-roll #2 ("Gianfranco Fino" / four hours)

This is the second UGC ad for the Trentacoste Primitivo. It uses the same creator, kitchen, bottle and voice as `plan/trentacoste-ugc-creator.md`, at the same unhurried pace (about 2.4 words/s). She is in 9:16 lo-fi iPhone style with diegetic kitchen audio and a British accent. Editors add the B-roll, the 99 pts graphic and the Jonny clip.

- **Takes:** one continuous take per hook or script beat (Seedance 2.5 with native audio, drafted at 480p and finalised at 1080p). Takes alternate between two start frames so each join reads as a jump cut.
- **Accent:** every final take was scored with an English-accent classifier, and every one reads as England (96.6–100 %). Takes it heard as American, Australian or New Zealand were regenerated. You confirmed the classifier's call on a male test voice ("not British"), which is why it was trusted here.
- **Voice:** speaker similarity between takes is 0.71–0.84, so it's the same voice throughout.
- **Words:** every take was checked against a Whisper transcript. "Trentacoste" was also checked with a phoneme recogniser, since the transcriber can't judge an Italian name.
- **Format:** 1080×1920, 24 fps, audio −14 LUFS, trimmed tight to speech (`build_greenscreen_cuts.py --thresh 21`). No captions or on-screen text.

## Deliverables

| File | Link / location |
|---|---|
| Full-quality ZIP (3 full cuts + 14 clips, 373 MB) | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/b898850d-fbca-4240-989c-ad09d3a88a05.zip |
| Smaller copies sent directly (clips in two ZIPs, 28 MB and 20 MB, plus the 3 full cuts) | `output/trentacoste-ugc2/share/` (not committed) |

`output/trentacoste-ugc2/clip_timings.json` holds the trim points.

- **Full cuts:** `trentacoste_ugc2_hook{1,2,3}.mp4`, each the hook followed by clips 01–10. They run 1:34.2, 1:34.3 and 1:33.2 respectively.
- **Runtime:** the script is about 220 words, so at a natural pace it runs about 1:25 of speech. To get near 45–60 s, the script has to lose words; speeding her up would undo the "not rushed" pace.

## Clips (timecodes are for the Hook 1 cut)

Hook 2 is 0.10 s longer and Hook 3 is 1.00 s shorter, so shift the body timecodes by that amount in those cuts.

| File | In | Length | Line as delivered |
|---|---|---|---|
| `00_hook1_four-hours` | 0:00.0 | 7.9 s | "There are just four hours left to try your drink of the holiday season. Four hours." *(four fingers up)* |
| `00_hook2_sommelier` | — | 8.0 s | "There's only four hours until stock runs out on the sommelier's wine of the year. Seriously." |
| `00_hook3_clock-ticking` | — | 6.9 s | "That clock is ticking, and… you don't want to miss out on this. Trust me." *(taps wrist; about 1 s pause after "and")* |
| `01_this-is-trentacoste_fino` | 0:07.9 | 7.7 s | "This is Trentacoste. It's likened to the very best wines produced by the great Gianfranco Fino." |
| `02_120-200_tenner` | 0:15.6 | 9.9 s | "But his wines are anywhere from a hundred and twenty to two hundred pounds, whereas this one… is a tenner. A tenner?" |
| `03_same-bit-of-italy` | 0:25.5 | 6.0 s | "Same bit of Italy, same grapes, and they're grown to exactly the same standards." |
| `04_fat-duck_whisper` | 0:31.5 | 9.5 s | "This Trentacoste is so good, it's the Primitivo of choice at Heston Blumenthal's Fat Duck… *(leans in, cheeky whisper)* for eighty-five pounds per bottle." |
| `05_family-estate` | 0:41.0 | 11.7 s | "It's a small family estate, and they're well known in Italy. But their name isn't famous enough yet to command the same price tag. Yet." |
| `06_tasting-notes` | 0:52.7 | 8.7 s | "You get this wonderful black cherry and dark plum first, then it collapses into espresso and cocoa notes on the finish." |
| `07_maroni` | 1:01.4 | 7.6 s | "Luca Maroni rated it nearly flawless… That's unheard of for wine this cheap. Unheard of." |
| `08_50-80_winedrops` | 1:09.0 | 6.8 s | "It should be around fifty to eighty pounds per bottle. But Winedrops don't settle for that." |
| `08alt_50-80_casedrops` | — | 7.5 s | Same line with "Casedrops"; swap it in if that's the brand for this run. |
| `09_bulk-buying` | 1:15.8 | 8.9 s | "They buy in massive bulk, straight from the vineyard, and that means they're selling crates at a huge discount. Huge." |
| `10_cta` | 1:24.7 | 9.4 s | "Their platform gets hand-picked deals every day, but this one is too good to ignore. Don't wait around… get yours today." *(points down)* |

## Notes for the edit

- **99 pts flash:** "nearly flawless" lands at about **1:03.1–1:03.9** in the Hook 1 cut (1.7–2.5 s into `07_maroni`). She leaves a pause after it for the graphic.
- **Jonny clip** ("I can't believe I've done this / I've overordered, can you help me out?") goes between `09_bulk-buying` and `10_cta`, at 1:24.7 in the Hook 1 cut.
- **Cheeky whisper:** in `04`, she leans into the lens with a hand by her mouth for "for eighty-five pounds per bottle".
- **Ad-libs** (none adds a fact, number or taste claim, so they're safe to trim):
  - "Four hours." (hook 1)
  - "Seriously." (hook 2)
  - "Trust me." (hook 3)
  - "A tenner?" (02)
  - "Yet." (05)
  - "Unheard of." (07)
  - "Huge." (09)

## Script changes

- **"They come from the same region, using the same grapes and growing standards"** became **"Same bit of Italy, same grapes, and they're grown to exactly the same standards."**
  - 13 generations of the scripted wording (including rewordings, a different start frame, a stronger voice reference and a longer combined take) all came out with an American accent on the classifier.
  - This looser wording is the only version that stayed English (100 %). The meaning and beat are unchanged.
- **"The Trentacoste is so good"** became "This Trentacoste…".
- **"hand-picked deals per day"** became "hand-picked deals every day".
- **"£85" / "£50–80" / "£120–£200"** are spoken as "eighty-five pounds" / "fifty to eighty pounds" / "a hundred and twenty to two hundred pounds".
- **"Casedrops/Winedrops":** both versions of line 08 are provided. No other line names the brand.

## Listen for

These are the transcriber's or phoneme recogniser's readings. I couldn't listen myself.

- **"Trentacoste"** comes out roughly *tren-ti-KOS-tuh* (01) and *tren-ti-KOS-tay* (04). Of six attempts, these were the closest to tren-tah-KAW-steh.
- **"likened"** in 01 is slightly over-stressed ("LIKE-end").
- **"Maroni"** is transcribed as "Morrani".

## Claims to verify before the ad runs

- Only 4 hours left / stock runs out (time-limited claim).
- "Sommelier's wine of the year".
- Likened to Gianfranco Fino's best wines; his wines are £120–£200.
- Same region, grapes and growing standards.
- Primitivo of choice at the Fat Duck at £85 a bottle.
- Small family estate, well known in Italy.
- Luca Maroni "nearly flawless" / 99 pts.
- "Should be around £50–80".
- Bulk buying straight from the vineyard.

Because the creator is AI-generated, label the ad clearly as an ad.

## Generation ledger (Higgsfield)

- Start frames: `19a11630-a276-4e12-950c-c9dd360e31eb` (sf1), `33649062-89bf-438d-8773-e2566ae7c6fa` (sf2); product `516ab5f9-9615-4c4c-8837-9f78dc1b1a8a`
- Voice references:
  - `5bc8dce5-df7c-4206-8d1f-8fe95a6a9db8` (the v2 hook)
  - `311e0e75-85f6-4bab-8ca6-5ce0280718da` (audio of final 05, used for the B3 retakes)

| Clip | Draft (480p) | Final (1080p) |
|---|---|---|
| Hook 1 | `4971f942-917a-45cb-8137-265d9dc40e9c` | `2c9ecfb1-3a79-4428-bcc5-9ed8e3a707d9` |
| Hook 2 | `db477fc7-a2f0-48c9-87f8-256b23b5617a` | `77e1deb8-99c3-4dbc-90c1-0966dfa26e99` |
| Hook 3 | `67aada14-c3c5-4e83-9809-14f49a2fdd45` | `5200412b-476c-4336-8d26-809e9c2c25f7` |
| 01 | `199c8c40-6dca-450c-9a03-8e02ed290509` | `3d4e0ddd-d97a-42db-a2da-c48affc85504` |
| 02 | `07914c7e-bc27-4310-82f0-5cb3d7b06fca` | `cd49f92e-c5a2-4562-9442-e3f12f9aae32` |
| 03 | `aa8e9493-1c98-41e2-b149-a9e441190f2f` | `e805deaa-044e-4da7-8cf5-53d2265dea88` |
| 04 | `f1350ffc-a66e-42d5-b073-2d14fdaa8346` | `bd86599a-175b-4609-8838-3ae94e47a470` |
| 05 | `69035bf6-197e-4977-94a5-56cb8acabdbc` | `71b3586e-090f-44a6-8060-eae7b8795520` |
| 06 | `c3f3b963-5393-40ce-8157-a9d9beacf082` | `6beb9f62-c014-49ca-b3be-5112e886aa6b` |
| 07 | `2bf950eb-1af3-4d54-b17f-02cf296034fb` | `33986ff4-6086-46b1-805f-765ad21abb44` |
| 08 | `0edcf336-bc39-451e-81ca-3440e4038da7` | `422327b9-3d38-4c05-8be1-6646ceb64806` |
| 08alt | `3b265225-59d8-410c-97d9-c1ff2a67baa9` | `483ba3cd-08eb-499c-902c-397eb81f5c82` |
| 09 | `8704cdd3-334f-44f2-b8ee-65b6d8840abd` | `9acf6c96-210f-499f-b5fb-394ded0090f7` |
| 10 | `67ca9aae-c415-455e-81b7-0fd036644428` | `d2e5e5f0-d40c-4662-939e-f8985ba4e145` |

**Rejected:**

- **Non-British accent:**
  - Hook 1: `0e0f98ac` (US)
  - 03: `74e4fd10` (US), plus 12 further drafts (US/NZ)
  - 10: `824bc3fb` and `0227b892` (Australian/borderline)
- **Mispronounced names:**
  - 01: first draft "tren-ta-ta-kau"; one take said "liked to" for "likened to"
  - 04: "Blumenberg's"
- **Other faults:**
  - Hook 2: one take repeated "four hours"
  - 04: one take read the pronunciation note aloud
