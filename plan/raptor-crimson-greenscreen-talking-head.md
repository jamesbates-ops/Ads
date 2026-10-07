# Raptor & Crimson (Napa Cabernet) — green-screen talking-head clips

Same presenter, seed and green-screen still as the Primitivo clips (`plan/primitivo-greenscreen-talking-head.md`): 9:16 portrait, seated waist-up on flat chroma green, voiced by **Callum** (Higgsfield preset `858499d9-fef5-40e1-bc29-b4dc661dc283`) with a British delivery. No B-roll or keying is done here.

- 720×1280, 24 fps, H.264 + AAC 48 kHz stereo, loudness matched to −14 LUFS.
- Each line is its own generation, trimmed to the speech (0.12 s head, 0.25 s tail).

## Deliverables

| File | Link |
|---|---|
| ZIP of all 18 clips (H1–H3, B1–B15) | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/a4fbcfd0-7814-43c9-83c1-aa777e95beac.zip |

The ZIP is not committed (size). `output/raptor-crimson-greenscreen/clip_timings.json` holds the trim points. To rebuild locally, run `scripts/build_greenscreen_cuts.py --hooks 3 --body 15 --name raptor_crimson` against the revoiced clips. The script also writes a full cut per hook (hook + B1–B15), about 2:01–2:03 each.

## Clips

| Clip | Section | Line as spoken | Length |
|---|---|---|---|
| H1 | Interrupt | "In 1976, nine French judges tasted wine blind and picked a California Cabernet over Bordeaux." | 6.63 s |
| H2 | Interrupt | "By 1976, America had beaten France at growing their own grapes." | 4.57 s |
| H3 | Interrupt | "After the Judgment of Paris, America became the best red wine grower in the world." | 5.11 s |
| B1 | Gap | "In 1976, at the Judgment of Paris, America produced a French style wine, better than the French." | 6.91 s |
| B2 | Gap | "Nine French judges sat and drank Cabernet Sauvignon, held up the unmarked bottle, and called it the best in the world." | 7.95 s |
| B3 | Gap | "The winning red came from the Stags Leap District in Napa, and the story was so famous, the bottle ended up in the Smithsonian." | 7.79 s |
| B4 | Gap → Stake | "After that, Napa wasn't farm country any more. It was the most famous red wine name in America. Napa as a region is really small." | 9.67 s |
| B5 | Stake | "The whole valley is a fraction of the size of Bordeaux, and that means prime vineyard land goes for half a million dollars an acre." | 8.39 s |
| B6 | Stake | "Most of the county is protected from development, so it can't get any bigger. So Napa producers can afford to charge hundreds per bottle." | 8.51 s |
| B7 | Winemaker | "Raptor and Crimson is made by Kevin Morrissey, who grew market standard wines at Etude and Ehlers Estate." | 6.79 s |
| B8 | Fruit | "He pulls Cabernet from Stags Leap District, Oakville, Atlas Peak and Diamond Mountain, where the best vines are found." | 7.99 s |
| B9 | Fruit | "He mixes this with more recent vines, to give some freshness to the blend, then ages it for eighteen months in American oak." | 7.51 s |
| B10 | Taste | "And the result is stunning. You get this potent hit of blackcurrant, plum and espresso to start," | 6.51 s |
| B11 | Taste | "before the taste mellows on the palate, fading to subtle dark chocolate and tobacco notes that sit long on the tongue." | 7.21 s |
| B12 | Payoff + proof | "And it shows. The Tasting Panel gave it 96 points, and Vivino drinkers put it in the top four percent of wines in the world." | 8.73 s |
| B13 | Payoff → CTA | "This wine is so special, and it's a privilege to have a bottle. And that's because it should be $85 per bottle." | 8.39 s |
| B14 | CTA | "But, do it the smart way. Click below and the link will give you a case of 6 for just $20 per bottle." | 7.53 s |
| B15 | CTA | "Now you can enjoy the very best of American heritage, for as much as a bottom shelf Costco." | 5.89 s |

Every revoiced clip was checked against a Whisper transcript: all words present, in order, nothing added.

## Notes for the edit

- **Runtime is about 2 minutes, not 44 s.** The script is about 320 words, and the body alone runs 1:56. Hitting 44 s means cutting the script to roughly a third; speeding up the voice won't get there.
- **One script fix:** "who's grew" was read as "who grew".
- **B10 → B11 is one sentence split across two clips** (the taste line was too long for a single clip). B10 ends on "to start," and B11 starts on "before…". Butt them together with no gap.
- **B6, B13 and B14** were generated from the green-screen still as the first frame (Gemini Omni Flash 1.1, image-to-video). The earlier takes drifted to a tight close-up on a muted green. They match the others, but the first few frames ease in from the still.
- **Accent:** the delivery is British, matching the Primitivo clips, even though the copy is US-facing ($, Costco). Clips can be regenerated with an American delivery if needed.
- **Names to listen for:** "Ehlers" (heard as "Ela's") and "Etude".
- **Claims to verify before the ad runs** (they are voiced exactly as scripted): nine French judges / the Smithsonian bottle, half a million dollars an acre, Kevin Morrissey's involvement and history, The Tasting Panel 96 points, Vivino top 4 %, the $85 value and $20 per bottle for 6. "Best red wine grower in the world" (H3) is a superlative.

## Generation ledger (Higgsfield)

Green-screen still: `5f4f1337-6ecf-4d3d-9ea9-a3f29dbd4f48` (same as Primitivo). Talking clips are `gemini_omni` (9:16, 720p) unless marked i2v (`gemini_omni_flash_1_1`, image-to-video from the still).

| Clip | Talking job | Voice-changed job |
|---|---|---|
| H1 | `7b07d006-19d3-4ea2-82d5-12198c030017` | `727e2fa6-ec98-46aa-89c8-c93b540b6c39` |
| H2 | `fc497e24-d129-418d-bbd0-8fe66f4fdd0c` | `9d4d39f5-12ac-47c6-9080-3f944a1d555c` |
| H3 | `1291051b-4e69-48ed-a52c-90cf9ccd57c0` | `5c743e0d-b467-4ad9-a74d-5a7525034876` |
| B1 | `eedca806-7853-4ec4-909b-1352dcf06b8f` | `e9dc3155-00aa-42c3-a23b-5d29c4a7175d` |
| B2 | `9e8ebad0-b4e6-4243-9e15-bac6df00f7f3` | `5d35e1f5-0da8-4ad5-a754-834b9272b6a4` |
| B3 | `2554df89-9eda-4fd7-9f09-50d770ea2c87` | `88f01a9f-d3c9-46e3-a81a-68a98e965728` |
| B4 | `88a542de-6009-4790-9ffe-d038094f4f02` | `3cf7f70a-3e13-4405-840e-e44f8d4c3939` |
| B5 | `aba231ca-f795-4bfc-ae70-0dfe51c9d65b` | `4120733b-07d8-42e0-806a-7d4c5a375c6f` |
| B6 | `d3bf48a5-4e40-4e74-a8ab-996a07783f2c` (i2v) | `cbc0679c-9caa-4281-8387-d48d1a668186` |
| B7 | `b40fa7f8-0a48-4071-9e8d-afd1a093325b` | `8736847a-2540-4deb-922f-82f1e06acb0d` |
| B8 | `6bd33def-4f49-4be5-99ec-612fc0bf6d78` | `3d221ac5-c1a7-483b-a014-c3457102fba0` |
| B9 | `c09c11fa-f849-4de2-8bcd-56a3c8f2d469` (retake; first take added "and") | `f446569f-5da7-44b5-a79c-4a49d1db5860` |
| B10 | `198a0d21-73c3-4fd6-b08f-ffa3dbf24329` | `7282f3d1-4583-40ac-9182-5b58f12339c0` |
| B11 | `a67e1498-d9b1-42dd-bfa2-20965175071f` | `4f2e628a-9d62-4de4-8f85-c8edc7a5e8a7` |
| B12 | `3879b162-f4d5-4086-ab65-b3e7cfefb033` | `a8a13778-1c38-4749-b7a9-b2ebc9a7eebb` |
| B13 | `c5a7877b-6456-47a5-9371-a4ca4f736816` (i2v) | `127e32a9-14ba-41a7-bfd1-c192c95ed06e` |
| B14 | `ce4437b7-971c-430b-9eab-145a8fae8994` (i2v) | `87c77093-ff79-4412-b983-48b11b4296c0` |
| B15 | `3be6259f-2429-4fee-8d59-7c9ca1b27064` | `3dc203b2-f87c-4920-b754-2d770da71b51` |
