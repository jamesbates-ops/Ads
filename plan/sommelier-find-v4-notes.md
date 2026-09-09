# The Sommelier's Find — v4 build notes (natural pitch, quicker read)

## What changed from v3

Two corrections from the client:

1. Do not pitch bend the voice down. The v3 build ran Arthur at `pitch_rate` -6.
   v4 runs him at `pitch_rate` 0, his own unmodified voice.
2. Make the read quicker. v3 sat at 1.75 words per second. v4 runs at about
   2.38, roughly 36 per cent faster.

The client also clarified the original complaint: the problem with the very
first version was that the voice sounded like a woman's, not that it was too
fast. That matches the measurement taken during the v3 build, where the shipped
v1 track came out at 216 Hz with almost no energy below 160 Hz.

## Pitch across versions

Measured on the finished mix, cepstral median fundamental:

| Version | Voice | Pitch setting | Median F0 | Energy 110–160 Hz |
|---|---|---|---|---|
| v1/v2 | Callum | as generated, faulty | 216 Hz | 0.1 % |
| v3 | Arthur | bent down 6 steps | 110 Hz | 13.9 % |
| v4 | Arthur | natural, no bending | 151 Hz | 34.1 % |

Per line, v4 measures 129–145 Hz. The 151 Hz figure covers a window heavy with
spoken prices, which sit higher. It is a natural male register throughout.

## Voice settings

- Voice: Arthur, preset id `30fc8796-ceb6-4a66-b3a7-4a145ef7f346`
- Model: `seed_audio`, wav, 48 kHz
- `pitch_rate` 0, `speech_rate` -8
- One exception: the hook for cut 2 is generated at `speech_rate` 0. At -8 that
  line ran 4.61 s against 2.2–3.1 s for the other three hooks, which would have
  pushed every cut's body start out to 4.9 s. The faster take runs 3.46 s.

## Timeline (seconds from start of cut)

| Shot | Starts | Voice length |
|---|---|---|
| Hook | 0.00 | 2.2–3.5 |
| 2 | 3.76 | 6.80 |
| 3 (price cards) | 11.01 | 13.36 |
| 4 | 25.17 | 3.49 |
| 5 (vineyard B-roll) | 29.06 | 9.02 |
| 6 | 38.93 | 6.12 |
| 7 (wordmark) | 45.50 | 6.72 |
| 8 | 52.67 | 5.68 |
| 9 (offer card) | 59.15 | 7.11 |
| 10–11 | 66.70 | 12.47 |
| End card | 80.05 | 4.00 |

Total 1:23.8 per cut, down from 1:38.3. The body starts at 3.76 s in all four
cuts, close to the brief's 0:03 mark, and the price-card hold is now 13.4 s
against the brief's 12 s.

## Footage

Regenerated against the new audio: three lip-synced clips plus a 10 s vineyard
B-roll and four hook clips, all Seedance 2.5 at 1080p 9:16. The quicker read
means fewer clips than v3, since more lines fit inside the model's 30 s ceiling.

- A1 covers shots 2 to 4 from the bottle frame, 26 s
- B1 covers shots 6 to 9 from the glass frame, 28 s
- B2 covers shots 10 and 11 from the glass frame, 14 s

## Checks run

- Fundamental and band energy measured on the finished mix, table above.
- All 13 voiceover lines transcribed. No hallucinated or dropped words, no
  internal gaps over 0.7 s.
- Full decode pass over cut 1 with no errors.

## Deliverables

| Cut | Hook | URL |
|---|---|---|
| 1 | It's the only place I buy my wine | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/2d40a9b4-ba54-4d0a-8bd1-5e4c51101101.mp4 |
| 2 | Trust me, Châteauneuf can be this affordable | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/2c7164fc-a133-4b2b-88eb-3b2713d6f95f.mp4 |
| 3 | This is where I buy all my Châteauneuf | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/8fc6d754-4704-4dc1-9ee3-6e7924eed8b0.mp4 |
| 4 | If you don't like Châteauneuf, keep scrolling | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/c0c48e96-8678-477d-8365-07c6632865f8.mp4 |

All four are 1080x1920, 24 fps, 1:23.8, H.264 High profile with stereo AAC.

## Build

The v3 scripts still drive this build. `sommelier-find-v3-stage1.py` prepares the
voiceover, timeline and grouped audio tracks; only its source map and gap table
change per version. `sommelier-find-v3-assemble.py` is unchanged: it reads the
timeline and clip list and cuts the four finals, so it adapts to the new
grouping without edits.

## Still open

- End card and call to action remain placeholders, marked TBC in the brief.
- Runtime is 1:23.8 against the brief's 1:04. Dropping the vineyard section and
  the tasting-note lines would reach about 1:11; also cutting one price callout
  and the closing luxuries line would land near 1:02.
