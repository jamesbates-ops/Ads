# Dolum Estates (Casedrops) UGC ad

9:16 hyper-real UGC talking-head A-roll for Dolum Estates California Cabernet Sauvignon, sold by Casedrops (US, American accent). Same presenter, kitchen and seeds as the Casedrops Cabernet ad, with the bottle lighting dulled to match the room. This is raw footage only: the editors add the b-roll, overlays, end card and the Jonny clip (between takes 5 and 6). The script is in [`SCRIPT.md`](SCRIPT.md).

Take 1 is three alternative hooks, one per video: **hook N + takes 2–6**.

## Downloads

All eight clips, zipped (1080×1920, 24 fps, iPhone-style diegetic audio):
https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/7bf56d14-b290-45b5-8142-24b50bc380ce.zip (90 MB)

| Clip | Length | Line |
|---|---|---|
| `hook1_four_hours_holiday_5s` | 5s | There are just four hours left to try your drink of the holiday season. |
| `hook2_four_hours_sommelier_6s` | 6s | There's only four hours until stock runs out on the sommelier's wine of the year. |
| `hook3_clock_ticking_6s` | 6s | The clock is ticking, and you don't want to miss out on this. Trust me. |
| `take2_reveal_napa_comparison_12s` | 12s | This is Dolum Estates… under twenty bucks. |
| `take3_california_chad_alexander_22s` | 22s | It's California Cab too… too new to command the same price tag. |
| `take4_tasting_value_13s` | 13s | Pour it, and you get blackcurrant… sixty to eighty dollars a bottle. |
| `take5_casedrops_70pct_off_10s` | 10s | But Casedrops doesn't settle for that… over seventy percent off. |
| `take6_cta_8s` | 8s | They drop hand-picked deals every single day… get yours today. |

Review rough cuts (hook + takes 2–6 butted together, no Jonny clip, loudness matched to about -16 LUFS, no overlays): `aroll/Dolum_hook1_roughcut.mp4` (70s), `aroll/Dolum_hook2_roughcut.mp4` and `aroll/Dolum_hook3_roughcut.mp4` (71s each).

Higgsfield job IDs: hooks `3e8fd6a3…`, `ad1c265b…`, `ebeb4364…` · take 2 `29de63c7…` (before the fix) plus `fb7fdbb6…` (Caymus fix) · take 3 `a549aec7…` · take 4 `904e9866…` · take 5 `53526a35…` · take 6 `7be2ca5f…`.

## Seeds
Reused from the Casedrops Cabernet ad, already approved with the dulled bottle lighting:
- `../casedrops-cab-ugc/seed_take1_empty.png`: the hooks.
- `../casedrops-cab-ugc/seed_A_dolum_hold.png`: take 2.
- `../casedrops-cab-ugc/seed_A_dolum_counter.png`: takes 3–6.

The packshot is `../casedrops-cab-ugc/reference/dolum_packshot.png`.

## How it was made
- Seedance 2.5 image-to-video with native audio at 1080p, one continuous take per clip.
- The packshot is an image reference, and her American voice from the Scarànto US take is a voice reference.
- Every bottle prompt specifies dulled room lighting: the bottle a touch darker than her, only a soft highlight on the glass, and a fully matte label no brighter than her white top.
- Each hook is prompted as a cold open.
- **Take 2 Caymus fix:** she dropped the M, so "Caymus" came out "KAY-us" (both recognisers heard "Caius").
  - A 4s section (4.5–8.5s) was re-rendered with its audio removed, so she says "Far Niente, Opus One, Caymus" fresh.
  - It's spliced back in silence to silence, with 2-frame picture crossfades and audio crossfades at both joins.
  - The out-point cuts at the best-matching frame pair, because the edit runs about 8% fast. This shortens the take by 0.17s; the rest is untouched.

## Checks
- **Words:** every clip was transcribed (faster-whisper medium) and every scripted line is present, including "four hours" (both hooks), "under 20 bucks", "California Cab", "Chad Alexander", "Stag's Leap", "$60 to $80", "Casedrops" and "over 70% off" (0.99).
- **Caymus:**
  - Forced choice before the fix was "Caius" 0.112 vs "Caymus" 0.093; after, "Caymus" 0.114 vs "Caius" 0.111.
  - Whisper given the names as a hint scores "Caymus" 0.58, up from 0.08 before. With no hint it now hears "Camus", with the M, rather than "Caius".
  - The spectrogram shows the nasal M between the vowels.
- **Accent:** CommonAccent ECAPA tops out as US or Canada on every 4s window of every clip. None read as England.
- **Pitch:** consistent, 180–198 Hz median. The hooks and take 5 sit at the brighter end because they're the excited lines.
- **Picture:**
  - One bottle, held firmly and label front-on in take 2, standing still on the counter in takes 3–6.
  - Natural hands, including hook 3's wrist tap. No on-screen text.
  - She gestures at the bottle and points down on "get yours today".

## Known nits (worth a listen)
- **Hook 2, "sommelier's":** the recogniser is unsure (0.49 even with the word as a hint). It probably sounds fine, but listen before using that hook.
- **Far Niente:** recognisers mangle it here and in the earlier Cabernet ad alike, so I left it. A quick listen is still worth it.
- **Take 2:** there's a tiny natural "uh" between "Napa" and "Cabs".
- **Take 2 to take 3:** the bottle goes from her hand to the counter. It's a jump cut, so b-roll should sit between them.
