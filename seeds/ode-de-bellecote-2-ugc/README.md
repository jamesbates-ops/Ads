# Ode de Bellecôte (hooks format) UGC ad — UK and US

9:16 hyper-real UGC talking-head A-roll for Ode de Bellecôte Châteauneuf-du-Pape, in the same format as the Dolum (Casedrops) ad.
- **UK version:** Winedrops, British accent, £.
- **US version:** Casedrops, American accent, $.
- **Footage:** raw only. The editors add the b-roll, overlays, end cards and the Jonny clip, which goes between takes 5 and 6.
- **Script:** in [`SCRIPT.md`](SCRIPT.md).

Take 1 is three alternative hooks, one per video: **hook N + takes 2–6**.

## Downloads

All eight clips per version, zipped (1080×1920, 24 fps, iPhone-style diegetic audio):
- UK (Winedrops): https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/ac7d7686-cfe7-4c59-91ad-65b24398b369.zip (77 MB)
- US (Casedrops): https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/aeb6ae3d-2397-4640-a139-c44f8dbacf82.zip (78 MB)

Each zip contains `hook1…`, `hook2…`, `hook3…`, `take2_reveal_hommage_price_12s`, `take3_region_galets_ageing_20s`, `take4_tasting_92pts_19s`, `take5_value_discount_13s` and `take6_cta_8s`.

**Review rough cuts:**
- Six files, one per hook per version: `aroll/Ode_UK_hook{1,2,3}_roughcut.mp4` and `aroll/Ode_US_hook{1,2,3}_roughcut.mp4`, about 79s each.
- Each is a hook plus takes 2–6, with no Jonny clip, loudness matched to about -16 LUFS and no overlays.

**Higgsfield job IDs:**
- **UK:**
  - Hooks `11805882…`, `1def76c6…`, `46280f5b…`.
  - Take 2 `7932222a…`.
  - Take 3 `48e235fa…` (before the fix), plus `32099719…` (the line fix used). An earlier fix attempt, `594e646e…`, was not used.
  - Takes 4–6 `5a3e8ce1…`, `fb1be6f0…`, `3fb9ebc0…`.
- **US:**
  - Hooks `2ed51a2c…`, `d3cd948b…`, `4cca5319…` (hook 3 re-render; the first take, `878a0201…`, was not used).
  - Takes 2–6 `09c2250d…`, `e62c910c…`, `df031677…`, `39534ad4…`, `5674b7fa…`.

## Seeds
| File | Used for | Higgsfield ID |
|---|---|---|
| `../casedrops-cab-ugc/seed_take1_empty.png` | The hooks, empty-handed | `557e9fd6…` |
| `seed_ode_hold.png` | Take 2: holding Ode | `41e63668…` |
| `seed_ode_counter.png` | Takes 3–6: Ode on the worktop | `d5c2de5b…` |

- The Ode seeds were made by swapping the bottle into the approved Dolum frames. They keep the same dulled lighting: matte label, the bottle a touch darker than her.
- The label is kept exactly as on the supplied packshot (`../ode-de-bellecote-ugc/reference/ode_de_bellecote_packshot.png`).

## How it was made
- **Model:** Seedance 2.5 image-to-video with native audio at 1080p, one continuous take per clip.
- **References:** the packshot is an image reference. Her voice comes from her own earlier takes: the British voice from the Scarànto UK ad and the American voice from the Scarànto US ad.
- **UK take 3 fix:** she read the pronunciation note in the prompt aloud ("galets roulés, *pronounced* galets roulés, in the soil").
  - The first re-render of that line (3.83–7.83s) said the phrase twice, so it was rejected.
  - The second was told to say "That means… galets roulés… in the soil" exactly once, slowly, with pauses filling the gap.
  - It is spliced in with a 2-frame crossfade at the start and a 0.25s dissolve back out, which hides a small pose difference.
  - The rest of the take is untouched.
- **US hook 3 re-render:** a wristwatch appeared on her bare wrist mid-take, so the hook was re-rendered with "bare wrists, no watch" and the "where a watch would be" wording removed.

## Checks
- **Words:** every clip was transcribed (faster-whisper medium) and every scripted line is present.
  - UK prices: "eighty quid" and "over seventy percent off" (0.99).
  - US prices: "$120", "over sixty-five percent off" (1.00) and "$850 … under forty bucks".
  - Both: "ninety-two points and up" and "top two percent".
- **Accent:** CommonAccent ECAPA.
  - Every UK clip reads as England overall, with a few 4s windows as Australia, the neighbouring accent.
  - Every US clip reads as US, with the odd window as Canada.
- **Picture:**
  - One bottle, held label-front in take 2 and standing still on the worktop in takes 3–6.
  - Natural hands, bare wrists, no on-screen text.
  - She points down on "get yours today" in both take 6s.

## Known nits (worth a listen)
- **Unscripted ad-libs:**
  - US hook 2 ends with "I'm serious." and US take 5 has "Nope," before "Casedrops doesn't settle for that".
  - Both are natural, but they weren't in the script. They're easy to trim.
- **US hook 3:** the wrist tap lands a beat after "The clock is ticking", not on it.
- **Hard names:**
  - "Sommelier's" in UK hook 2 came out a bit mushy (heard as "Sonnoir's" at 0.49).
  - The recognisers also mangle "Ode de Bellecôte", "Beaucastel's Hommage à Jacques Perrin" and "galets roulés", as they do any French name.
  - Have someone listen to the names in take 2 before sign-off.
- **Take 2 to take 3:** the bottle goes from her hand to the worktop. It's a jump cut, so b-roll should sit between them.
