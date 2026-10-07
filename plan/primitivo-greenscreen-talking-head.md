# Trentacoste Primitivo — green-screen talking-head clips

Format: 9:16 portrait, the presenter from the seed photo (navy pinstripe suit, black shirt) talking straight to camera on a flat chroma green (#00B140) background, for the editors to key over their own B-roll. No B-roll or keying is done here.

- Resolution 720×1280, 24 fps, H.264 + AAC 48 kHz stereo, loudness matched to −14 LUFS.
- Voice: **Callum** (Higgsfield preset `858499d9-fef5-40e1-bc29-b4dc661dc283`) on every line.
- Each line is its own generation, trimmed to the speech (0.12 s head, 0.25 s tail). Full versions are the lines butted together as hard jump cuts.

## Deliverables

| File | Length | Link |
|---|---|---|
| Full cut, Hook 1 ("double life") | 1:01.0 | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/f45913a3-2f5f-417a-87c2-6d08cf56e736.mp4 |
| Full cut, Hook 2 ("symbolises Italy") | 0:59.6 | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/2411118b-1ea3-4798-9890-21eecc75c139.mp4 |
| Full cut, Hook 3 ("best Primitivo") | 0:59.6 | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/557b8117-e128-4c92-acb9-dae9125cae19.mp4 |
| ZIP of the 11 per-line clips (H1–H3, B1–B8) | — | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/08bea6ce-59ef-4914-81a6-62873c4ebe4c.zip |
| Green-screen presenter still (identity reference) | — | https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20261007_102506_5f4f1337-6ecf-4d3d-9ea9-a3f29dbd4f48.png |

The MP4s and ZIP are not committed (size). Rebuild them locally from the revoiced Higgsfield clips with `scripts/build_greenscreen_cuts.py`; `output/primitivo-greenscreen/clip_timings.json` holds the trim points.

## Line timings

Body timecodes are given for the Hook 1 cut. Hooks 2 and 3 are 1.42 s and 1.40 s shorter, so subtract that from every body line in those cuts.

| Clip | Section | Line | Clip length | In (Hook 1 cut) | Out (Hook 1 cut) |
|---|---|---|---|---|---|
| H1 | Interrupt | "This grape lived a double life for about a hundred years." | 4.03 s | 00:00.00 | 00:04.03 |
| H2 | Interrupt | "This wine symbolises Italy." | 2.61 s | (Hook 2 cut) 00:00.00 | 00:02.61 |
| H3 | Interrupt | "This is the best Primitivo I've tried this year." | 2.63 s | (Hook 3 cut) 00:00.00 | 00:02.63 |
| B1 | Gap | "In California they called it Zinfandel. In the heel of Italy they called it Primitivo, because it ripens before anything else in the vineyard." | 7.75 s | 00:04.03 | 00:11.78 |
| B2 | Gap | "It wasn't until DNA testing that winemakers discovered they were the same." | 4.13 s | 00:11.78 | 00:15.91 |
| B3 | Stake + mechanism | "Its Italian home is Puglia, the strip of land between the Adriatic and the Ionian Sea, where it's hot enough to turn grapes into jam." | 8.77 s | 00:15.91 | 00:24.68 |
| B4 | Stake + mechanism | "For a long time a lot of the wine made down here got shipped north to give other regions' wines more colour and strength." | 6.71 s | 00:24.68 | 00:31.39 |
| B5 | Producer | "Trentacoste is a family-run estate around Manduria, the town Puglian Primitivo is best known for." | 5.93 s | 00:31.39 | 00:37.32 |
| B6 | Taste | "You get this wonderful black cherry and dark plum first, then it collapses into espresso and cocoa notes on the finish." | 6.73 s | 00:37.32 | 00:44.05 |
| B7 | Payoff + proof | "Luca Maroni rated it near flawless. And Heston Blumenthal's Fat Duck pairs it with his Michelin-star courses, at eighty-five pounds a bottle." | 7.95 s | 00:44.05 | 00:52.00 |
| B8 | CTA | "But six bottles are just £64.99 on Wine-drops… under eleven pounds a bottle. So tell this story to friends, and save money, whilst you savour." | 8.97 s | 00:52.00 | 01:00.97 |

Every line was checked against a Whisper transcript after the voice change; all words are present, in order, with no repeats.

## Notes for the edit

- **Runtime is about 60 s, not 44 s.** At a natural pace the script is about 170 words, which runs around 57 s of speech. To land near 45 s, cut words from the script; speeding the voice up would make it sound rushed.
- **"Trentacoste"** is said tren-tah-KAW-steh. B5 was retaken with the phonetic spelling in the line, because the first take said "Trenta-costa".
- **Framing:** some clips have a slight camera push-in, so his scale shifts a little from line to line. The most visible jump is H1 → B1, where H1 ends punched in. Most edits will rescale the keyed presenter anyway.
- **Green level** varies slightly between clips. Key each clip separately rather than reusing one key setting.
- **Claims to verify before the ad runs** (they are voiced exactly as scripted): the Luca Maroni rating, The Fat Duck pairing and its £85 list price, and £64.99 / 6 bottles / "under £11 a bottle" on Wine-drops.

## Generation ledger (Higgsfield)

- Seed upload: `b30d13e4-0367-494f-b289-be27a6a0f70e`
- Green-screen still (`gpt_image_2`, 9:16): `5f4f1337-6ecf-4d3d-9ea9-a3f29dbd4f48`
- Talking clips (`gemini_omni`, 9:16, 720p) → Callum voice change:

| Clip | Talking job | Voice-changed job |
|---|---|---|
| H1 | `3343023f-9f04-4d85-8b63-13cd9c14542a` | `3fdc1382-2a4f-4ec9-a751-ea8d63492e10` |
| H2 | `ec1aad84-7aad-41ba-a0ab-99765675cb47` | `173aeacd-069c-4aec-a247-91c4974e8df4` |
| H3 | `4a12ab64-3c95-4720-a0b5-4ab326402682` | `0bc81e48-c3b7-4ff7-90ed-52eb24958c3b` |
| B1 | `b24860da-e900-4f4c-a4d5-ef62b850324d` | `578dddd7-87d2-48ff-81df-9d65e1641427` |
| B2 | `c471a5ef-fd4b-4f5c-aee7-adb4378e54f6` | `93279be2-789b-42c2-a455-a0eb746b3eb4` |
| B3 | `3c512e7d-b987-4a3b-8897-deea331b0c12` | `f476feeb-cd71-42cf-9311-5bd15778b2ae` |
| B4 | `2689545f-7712-41b4-87e6-10710f46c291` (retake; the first take repeated a phrase) | `cb309469-d795-4bd6-9242-043abd90c8d9` |
| B5 | `c1c697db-44b3-418d-858c-cc6f9dbba289` (retake for tren-tah-KAW-steh; first take `6adbdcda-f032-4259-9630-8bf5af5e3aaf` said "Trenta-costa") | `553065d4-fbda-4ca5-b797-ded77ecc6519` |
| B6 | `9e93dcfe-6bb4-4910-ad8f-5c774c68ac2a` | `b31afcc5-40a9-44a5-aa6a-7cd321b316f3` |
| B7 | `82f76138-41b5-473a-8369-ed70f5e8e6b2` | `9b83f578-42c8-4975-a124-b09b8c1b1f82` |
| B8 | `7ce86a1d-4996-442f-abfd-1caa03a177a4` | `737263cc-28f2-46e9-bb41-a561d152aaa7` |
