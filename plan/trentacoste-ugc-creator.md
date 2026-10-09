# Trentacoste Primitivo — UGC creator A-roll

A creator talks to her phone in her kitchen, holding the bottle, in lo-fi iPhone style with diegetic audio and a British accent. Editors cut B-roll in over it, and the "flash 99pts" graphic is theirs to add. The source seeds showed her holding a different bottle (Scaranto). Because the script describes the Trentacoste Primitivo, the start frames swap in the Trentacoste bottle from the product shot, with the label reproduced exactly.

- Four continuous takes (phone propped on the worktop, both hands free: bottle in her right, gestures with her left), alternating between two start frames so the joins read as natural jump cuts.
- Seedance 2.5 with native audio, generated from the start frame, the product reference and a voice reference so all four takes share one voice. Drafted at 480p, checked, then finalised at 1080p.
- Accent checked with an English-accent classifier: every take reads as England (~100 %). Speaker similarity between takes is 0.84–0.97, so it's the same voice throughout.
- 1080×1920, 24 fps, audio matched to −14 LUFS. No captions or on-screen text.

## Deliverables

| File | Link / location |
|---|---|
| Full-quality ZIP (A-roll + 4 takes, 94 MB) | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/895d5dff-df92-4b34-9fe9-f4718711301f.zip |
| Smaller copies sent directly (A-roll 26 MB, takes ZIP 26 MB) | `output/trentacoste-ugc/share/` (not committed) |

## Takes

| # | File | Length | Line as delivered |
|---|---|---|---|
| 1 | `01_hook_fat-duck.mp4` | 12.1 s | "Warning — if you love Italian wine and you keep scrolling, you're gonna miss the best deal this year. Right, so at the Fat Duck, the cheapest bottle you can get is eighty-five quid… and it's this one. This one! Eighty-five quid, honestly." *(bottle brought up to the lens)* |
| 2 | `02_heston_tenner.mp4` | 12.2 s | "And even then, they're rigorously critiqued and hand-picked to pair with Michelin-star dishes, served by Heston Blumenthal himself. Like… Heston! Except you can get this bottle for a tenner. A tenner, I know. So you can enjoy it whenever you like, without breaking the bank." |
| 3 | `03_puglia_maroni.mp4` | 10.1 s | "It's from a family-run estate down in Puglia, and it's rated near flawless by Luca Maroni, which puts it in the top three percent of wines in the world. Top three percent — honestly, insane value." |
| 4 | `04_winedrops_cta.mp4` | 11.1 s | "And the best bit? Winedrops will do free delivery on a case of six, at ten pounds a bottle. Honestly, I wouldn't wait, it won't be around for long. I'll put the link somewhere below. Go on." |

A-roll = takes 1–4 back to back, 45.6 s.

## Script changes and notes

- **"Except I got this bottle for a tenner" → "Except you can get this bottle for a tenner".** She's a generated creator, so she shouldn't claim a personal purchase. All the other beats are as scripted, lightly loosened for natural speech, with ad-libs filling the gaps.
- **Cut ad-lib:** take 2 originally ended "…and it's delicious". That was trimmed off, because it's an unscripted taste claim.
- **Kept ad-libs:** "honestly, insane value" (take 3) and "Go on" (take 4).
- **Listen for:** "scrolling" in take 1 (the transcriber kept hearing "sliding") and "Heston Blumenthal" in take 2 (heard as "Houston Blumenbach"). These are probably accent mishears; I couldn't listen myself.
- **Claims to verify before the ad runs:** Fat Duck's cheapest bottle £85 and that this is it, hand-picked to pair with Heston Blumenthal's Michelin-star dishes, family-run estate in Puglia, Luca Maroni "near flawless", top 3 % of wines in the world, Winedrops £10 a bottle with free delivery on a case of six. Because the creator is AI-generated, label the ad clearly as an ad.

## Generation ledger (Higgsfield)

- Seeds: `6b62539b-d147-4ded-a4e6-c9c9a9e70b22`, `7b656406-c990-4e8d-9987-0b2bacb787c5`; product shot `516ab5f9-9615-4c4c-8837-9f78dc1b1a8a`
- Start frames with the Trentacoste bottle (`gpt_image_2`): `19a11630-a276-4e12-950c-c9dd360e31eb` (takes 1, 3), `33649062-89bf-438d-8773-e2566ae7c6fa` (takes 2, 4)
- Voice reference: `45ba99cd-56e5-4906-ae53-179848fbfa5b` (from test draft `d1e5835d`)

| Take | Draft (480p) | Final (1080p) |
|---|---|---|
| 1 | `dd3f8b3a-a733-4e1d-a466-05432571c429` | `66e03166-102b-4844-87b0-00a09998602f` |
| 2 | `15ccd067-bb97-4f67-8c47-e014a2553b70` | `865f9231-7722-44f4-8887-9b620c2ac198` (trimmed at 12.2 s) |
| 3 | `ce4bfaa2-8240-48be-8c1c-712ccc741b5b` | `cf956095-1ec0-4303-a2b6-5ddd7904aa1e` |
| 4 | `b0e686d5-fab0-4c35-8b04-f5971ca475f2` | `31c66988-28f1-423e-a3f5-4b910121873d` |
