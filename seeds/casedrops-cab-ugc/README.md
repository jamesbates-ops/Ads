# Casedrops Cabernet UGC ad

9:16 hyper-real UGC talking-head A-roll for Casedrops, in two versions (US / American accent only):
- **Version A**: Dolum Estates California Cabernet Sauvignon.
- **Version B**: Raptor & Crimson Napa Valley Cabernet Sauvignon.

Same presenter, kitchen and setup as the Scarànto and Ode de Bellecôte ads, with the framing pulled back slightly so she can set the bottle on the counter. This is raw footage only: the editors add the Decanter 94 card, b-roll and end card. The script is in [`SCRIPT.md`](SCRIPT.md).

## Downloads

Full-quality takes, zipped (1080×1920, 24 fps, iPhone-style diegetic audio):
- A (Dolum): https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/b7cf7bbd-72e9-4825-9f22-49d9b5788bfe.zip (44 MB)
- B (Raptor & Crimson): https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/b1763f9d-ea26-45b6-8fcd-d950751a960a.zip (46 MB, with the Petrus fix)

Each zip contains `take1_hook_400_8s`, `take2_setdown_winemaker_102_17s`, `take3_top1pct_tasting_18s` and `take4_delivery_price_cta_16s`. Take 1 has no bottle, so it is the same clip in both.

Review rough cuts (four takes butted together, loudness matched to about -16 LUFS, no overlays): `aroll/A_Dolum_aroll_roughcut.mp4` and `aroll/B_RaptorCrimson_aroll_roughcut.mp4`, both 59s.

Higgsfield job IDs:
- Shared take 1: `71035fd1…`
- A: `79b5ced0…` (take 2), `044da727…` (take 3), `b039301d…` (take 4)
- B: `194b1a91…` (take 2, before the fix), `24b39528…` (take 3), `daf70510…` (take 4), plus `cd12b07b…` (take 2 Petrus fix)
- Superseded first-pass bottle takes, before the lighting fix: three A and three B takes rendered 15:37–15:42.

## Seed frames

| File | Used for | Higgsfield ID |
|---|---|---|
| `seed_take1_empty.png` | Take 1, empty-handed, wider framing | `557e9fd6…` |
| `seed_A_dolum_hold.png` | A take 2: holding Dolum, about to set it down | `ab48ae6f…` |
| `seed_A_dolum_counter.png` | A takes 3 and 4: Dolum on the counter | `80edb72d…` |
| `seed_B_raptor_hold.png` | B take 2: holding Raptor & Crimson | `484fd888…` |
| `seed_B_raptor_counter.png` | B takes 3 and 4: Raptor & Crimson on the counter | `568ee069…` |

References: `reference/dolum_packshot.png` and `reference/raptor_crimson_packshot.png` (the supplied packshots).

## How it was made
- Seeds: GPT Image 2.5, with the bottle composited from the supplied packshot. After feedback, the bottles were relit to match the room: the same soft window daylight from frame right, the bottle a touch darker than her, only a soft highlight on the glass, a matte label with no sheen, and a soft contact shadow on the counter.
- Takes: Seedance 2.5 image-to-video with native audio at 1080p, one continuous take each. The packshot is an image reference so the label stays true, and her American voice from the Scarànto US take is a voice reference. The matte, no-sheen lighting is written into every bottle prompt.
- B take 2 Petrus fix: she dropped the final S, so "Petrus" came out as "Pe-troo" and both recognisers heard "Petri".
  - A 4s section (9.0–13.0s) was re-rendered with its audio removed, so she said "who used to make Petrus" fresh, with the same voice reference.
  - It was spliced back in over 9.08–12.00s, starting and ending in pauses, with 0.18s picture fades and 40ms audio crossfades.
  - The rest of the take is untouched. The edit matches the source frame for frame at the start (41.8 dB PSNR), and the end join sits in a still pause.

## Checks
- **Words:** every take was transcribed (faster-whisper) and contains every scripted line, with nothing leaked from the voice reference.
  - Version A's key words win a forced choice against their alternatives: "California" over "Napa", "Chad Alexander", "Silver Oak", "a hundred and two".
  - Version B's do too: "Napa" over "California", "Kevin Morrissey", "Petrus", "a hundred and two".
  - Both versions: "top one percent", "under twenty bucks", "sixty to eighty dollars" and "seventeen bucks each".
- **Petrus:** forced choice before the fix was "Petri" 0.085 vs "Petrus" 0.077; after, "Petrus" 0.080 vs "Petri" 0.069. Whisper now hears "Petrus" (0.82 with the medium model, 0.78 with small). A spectrogram shows the final S hiss that the original lacked.
- **Accent:** CommonAccent ECAPA tops out as US or Canada on every 4s window of all seven takes, the fixed one included. It never reads as England.
- **Pitch:** consistent at 178–188 Hz median across takes 2–4.
- **Picture:**
  - Exactly one bottle, label front-on and legible. She sets it down cleanly in take 2, and it stays put in takes 3 and 4.
  - Natural hands, no on-screen text.
  - She points down on "link's below" in both take 4s.

## Known nits
- Between take 2 and take 3 the bottle sits a little further right on the counter: about 160px in A, less in B. It reads as an ordinary jump cut, and the b-roll covers it.
- The re-spoken "who used to make Petrus" is a little brighter than the rest of B take 2 (about 193 Hz against 178 Hz), like an excited emphasis. Worth a quick listen.
- Take 1 is also a touch higher (195 Hz), since it's the incredulous hook.
- In A take 2, whisper's small model heard "the same grapes" as "creeps" (0.55). The medium model hears "grapes", and 12 of 12 sampled decodes of the phrase say "grapes", the same as in B, so it is fine. Still worth a listen at sign-off.
