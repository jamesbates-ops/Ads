# WINEDROPS — block clips (11 lines, 9:16)

User direction: *"Let's do this in block clips... let's take it audio line by audio line.
I just want her talking to camera."* Briefing notes explicitly set aside — no shot map,
no captions, no end card, no assembled film. Eleven independent clips.

## The lip-sync problem, and why the route changed

Every earlier delivery used **Wan 2.7** with the voiceover passed as `audio_references`.
That was wrong, and it is worth stating plainly:

- Wan 2.7 **passes the supplied audio straight through to the soundtrack and animates the
  mouth independently of it.** Measured on the test clip: the output audio matched the
  supplied VO at **lag 0, correlation 0.9999** — the user's audio is intact and untouched,
  but nothing drives the lips from it.
- So this was never a sync *offset* that could be nudged. There is no audio-driven lip
  animation in that path at all.
- The two films already delivered (`805d8275...`, `aeece908...`) were built this way. Their
  lip-sync is therefore very likely wrong. It was reported at the time as "unverified"
  because picture cannot be viewed from this environment; it is now known to be wrong.

Ruled out on the way to a fix:
- No dedicated lip-sync / talking-photo model exists in the catalogue.
- **Grok Video 1.5** rejects `start_image` combined with reference media, and caps at 720p
  with reference media.
- **Seedance 2.5** with `audio_references` + `generate_audio:true` ignores the reference and
  synthesises its own speech (correlation 0.83 at a -520ms lag — envelope coincidence).

**Chosen route (user decision): Seedance 2.5 native speech.** `mode:"omni_reference"`,
`generate_audio:true`, and the spoken line carried verbatim in an `Audio:` line inside the
prompt, per the bundled `ugc-review-video` workflow. The mouth genuinely matches because the
model generates the speech itself.

**Cost of the route:** the voice is Seedance's, not the supplied ElevenLabs read
(Jessica Anne Bogart). The client's VO file is not used in these clips.

## Seed

9:16 master frame `93599e27-ab73-427f-b2f3-762a1d56d48f` — the supplied landscape fireside
image recomposed vertical via Seedream 4.5, keeping likeness, wardrobe, room and grade, with
the Dolum bottle kept in frame. Framing B (tighter medium close) chosen by the user over a
wider alternative. One seed drives all eleven clips, so identity is consistent.

## Delivered clips

All 1080x1920, single continuous shot, locked-off camera, head and face movement only.

| # | job_id | Clip | Speech in/out | Line |
|---|---|---|---|---|
| 1 | `1af6b95e-dc00-46bc-9586-68c57b1f34e6` | 5.05s | 0.80-4.50 | If I met a man who drank this, I'd never forget him. |
| 2 | `b0bbce5d-33c9-4956-814e-616ea2d27713` | 6.05s | 2.10-5.04 | Yeah, this would keep us talking. |
| 3 | `2572c474-4ca6-4d0a-833e-5997cfb89a63` | 7.05s | 1.20-3.74 | This tells me everything I need to know about him. |
| 4 | `c3400492-195c-4fd4-b3ef-e49e99d4f8bf` | 8.05s | 3.06-7.34 | When I go on dates, I'm always looking for the right signs. |
| 5 | `9d216521-611b-4e2a-871d-d6e99b19d5dc` | 7.05s | 0.00-6.20 | Great clothes, great taste, in shape. |
| 6 | `156823a7-7716-480c-a189-38f20344d22d` | 9.05s | 0.64-6.32 | But bringing this bottle to the table, tells me everything I need to know. |
| 7 | `1d02c403-4680-43f4-9d44-c144eeae848c` | 14.05s | 0.00-13.18 | It's a full-bodied Cabernet Sauvignon, aged in 18 month oak... |
| 8 | `5a91d92f-14ff-4c2e-b052-1ffd3d73f487` | 15.05s | 0.00-11.30 | It's exactly like the man I want. He's not following trends... |
| 9 | `e731b3fe-839c-4bb6-8511-6bf23695f78e` | 14.05s | 0.00-13.50 | Ugh, it's so velvety and rich... |
| 10 | `a49a320e-fe77-4ef7-9575-69b0b1d63143` | 15.05s | 0.00-11.86 | The best part? If he's smart... |
| 11 | `b5f0f20a-bf47-4f5e-9586-c6e0c818282d` | 7.05s | 0.58-4.14 | Then we can spend more time, getting to know each other. |

Speech in/out are measured from a word-level transcript of each clip's own audio — use them
as trim handles; the surrounding silence is padding, not performance.

## Copy verification

Every clip's generated audio was transcribed with faster-whisper and compared word-for-word
against the intended line. This caught two genuine defects:

1. **Clip 5 — stage direction spoken aloud.** First render said *"great clothes, her
   expressive eyebrows, great taste, in shape."* Seedance read part of the scene description
   as dialogue. Fixed by removing the descriptive clause and adding an explicit
   "says exactly this and nothing else" instruction. Re-render verified clean.
2. **Clip 9 — mispronunciations.** First render said *"Ooh"* for "Ugh" and *"expresso"* for
   "espresso". Re-rendered; both now correct.

False positives, checked and dismissed — spoken content is right, only the transcript's
orthography differs:
- Clip 7: "18-month" vs "eighteen month"
- Clip 10: "$85" / "75%" vs "eighty-five dollars" / "seventy-five percent"

## Open / unverified

- **Clip 8 proper nouns.** Transcript reads *"buying from chaos or rigid states"* against
  "Caymus or Ridge Estates". Most likely speech-recognition error on brand names — these are
  exactly the substitutions ASR makes — but not re-rendered, so it needs a listen.
- **Clip 9 "blackcurrant"** transcribes as "black currate". Same uncertainty.
- **Lip-sync quality itself is unverified by me.** Picture cannot be viewed from this
  environment. The user approved clip 1's sync by eye; the remaining ten use the identical
  route and seed but have not been individually watched.
- **The supplied ElevenLabs VO is unused.** If its voice is wanted, the route is to
  voice-convert these clips toward that timbre — lip-sync survives because timing is
  unchanged.

## Note for future runs

`get_workflow_instructions` should have been called at the very start of this brief — the
bundled `ugc-review-video` workflow documents the native-speech talking-head route and would
have avoided the Wan 2.7 dead end entirely.
