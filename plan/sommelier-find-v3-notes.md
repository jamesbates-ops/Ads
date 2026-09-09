# The Sommelier's Find — v3 build notes (new voice, slower read)

## What changed from v2

The client asked for a British male voice in his 30s, deeper, and a slower read.

Investigating the v2 mix showed the old voiceover was not just high-pitched by
taste, it was wrong. Measured on the shipped audio:

| Version | Median fundamental | Energy 60–110 Hz | Energy 110–160 Hz |
|---|---|---|---|
| v2 (Callum, shipped) | 216 Hz | 0.3 % | 0.1 % |
| Callum preset preview | 116 Hz | 3.1 % | 10.8 % |
| v3 (Arthur, shipped) | 110 Hz | 41.0 % | 13.9 % |

The v2 track sat a full octave above the voice preset it was generated from and
had essentially no low-frequency energy, which is why it read as thin and fast.
v3 was regenerated from scratch at an explicit sample rate, so the pitch and pace
on disk are the pitch and pace as heard.

## Voice settings

- Voice: Arthur, preset id `30fc8796-ceb6-4a66-b3a7-4a145ef7f346`
- Model: `seed_audio`, `format` wav, `sample_rate` 48000
- `pitch_rate` -6, `speech_rate` -22
- Arthur is the one preset in the library that describes itself as British
  ("a soft-spoken British clarity"). Candidates were screened by measuring the
  fundamental of every male preview and transcribing the previews for accent.
- Pace is roughly 1.75 words per second against about 2.3 in v2, a 25 % slowdown.

## Timeline (seconds from start of cut)

| Shot | Starts | Voice length |
|---|---|---|
| Hook | 0.00 | 2.9–3.9 |
| 2 | 4.25 | 6.03 |
| 3 (price cards) | 10.83 | 17.88 |
| 4 | 29.61 | 5.17 |
| 5 (vineyard B-roll) | 35.23 | 10.49 |
| 6 | 46.72 | 7.15 |
| 7 (wordmark) | 54.42 | 8.13 |
| 8 | 63.10 | 6.16 |
| 9 (offer card) | 70.21 | 7.12 |
| 10–11 | 77.88 | 15.64 |
| End card | 94.21 | 4.00 |

Total 1:38.3 per cut. The body is locked at 4.25 s in all four cuts.

## Footage

The lip-synced footage had to be regenerated because it is driven by the audio.
Five body clips plus four hooks, all Seedance 2.5 at 1080p 9:16:

- A1 (shots 2–3, 26 s) and A2 (shot 4, 6 s) from Frame A, the bottle frame
- B1 (shots 6–8, 24 s) and B2 (shots 9–11, 25 s) from Frame B, the glass frame
- Vineyard B-roll regenerated at 12 s, text-to-video
- Four hook clips at 5 s each, trimmed to a 4.25 s slot

Clips are grouped so no single generation exceeds 29 s, which keeps every clip
inside the model's 30 s ceiling.

## Copy changes

The price line was shortened. At the slower pace the original wording ran 24.6 s
against a 12 s card hold. It now reads "Henri Bonneau's Célestins, eleven
eighty-nine. Beaucastel's Hommage à Jacques Perrin, nine fifty-one, on a
hundred-point Parker score. Rayas seventy-eight, four and a half thousand,"
which runs 17.9 s. The on-screen cards still show the exact figures.

## Open points

- Runtime is 1:38 against the brief's 1:04. The copy cannot be delivered at a
  slower pace inside 64 seconds. Cutting the B-roll and the tasting-note lines
  would bring it to about 1:20; dropping one of the three price callouts and the
  luxuries line would reach roughly 1:10.
- End card and call to action are still placeholders, marked TBC in the brief.

## Deliverables

| Cut | Hook | URL |
|---|---|---|
| 1 | It's the only place I buy my wine | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/4db43e08-88d3-4c97-ab3a-b6d42d7a39fd.mp4 |
| 2 | Trust me, Châteauneuf can be this affordable | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/0160928a-e862-4a64-a121-55012b66c97c.mp4 |
| 3 | This is where I buy all my Châteauneuf | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/5144f36f-bcd6-4881-ad56-e53466162213.mp4 |
| 4 | If you don't like Châteauneuf, keep scrolling | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/f5222409-ad65-4dfa-b2be-740ed60e9fd3.mp4 |

All four are 1080x1920, 24 fps, 1:38.3, H.264 High profile with stereo AAC.

## Checks run

- Fundamental frequency and band energy measured on the finished mix, table above.
- Every voiceover line transcribed and checked for hallucinated or dropped words.
- Full decode pass over cut 1 with no errors.
- Scene analysis of cut 1 returns the script in full and the right structure:
  bottle frame to 0:34, vineyard to 0:46, glass frame to 1:33, end card to 1:38.
- The scene analysis reports music under the end card. There is none. The last
  four seconds measure -31 LUFS of brown-noise room tone against -15 LUFS for
  the voice, and the mix contains no music track. Same false positive appeared
  on the v2 cut.

## Build

`sommelier-find-v3-stage1.py` prepares the voiceover and timeline and uploads the
grouped audio tracks. Those tracks drive nine Seedance generations. Then
`sommelier-find-v3-assemble.py` cuts the four finals. Accented characters in the
committed copy of the assemble script are transliterated so the file stays
ASCII-safe; the live script carries the proper accents.
