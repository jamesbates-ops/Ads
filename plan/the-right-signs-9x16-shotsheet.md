# WINEDROPS — "The Right Signs" (9:16 paid social, 0:51)

Source brief: `The_Right_Signs.docx.pdf` (6 text pages).
Build branch: `claude/sweet-brown-5vnmyf`.

## 1. Brief summary

| Field | Value |
|---|---|
| Format | 9:16 vertical, 1080x1920 |
| Runtime | 0:51, 9 shots |
| Type | Talking head, single voice, in-room and close (no phone treatment) |
| Audio bed | Fire crackle + room tone kept in |
| Captions | Burned in throughout |
| Variants | 3 cuts, differing only in the opening line (shots 2-9 identical) |
| Body lock | Body always starts at 0:03, whatever the hook length |

### Hooks
1. "If I met a man who drank this, I'd never forget him."
2. "Yeah, this would keep us talking, all night."
3. "This tells me everything I need to know about him."

## 2. Deviations from the brief (deliberate, user-directed)

| Brief says | Delivered | Why |
|---|---|---|
| PRODUCT = Erikson & Caradin, "Raptor & Crimson", Napa Valley, black label / gold monogram / red bird | **Dolum Estates Cabernet Sauvignon**, cream label | User: "Keep the bottle of dolum estates as is", plus a supplied bottle reference image. User instruction overrides the brief. |
| Seed frames via 3 Google Drive links | User-supplied images | Drive is not reachable from this environment; the user attached the frames directly. |
| Both seed frames are landscape, "will need reframing, not a centre crop" | Seed frames rebuilt natively at 9:16 | Reframing by regeneration rather than crop, as instructed. |
| "See §10" / "see §9 before burning in competitor names" | n/a | **§8-§10 do not exist in the supplied PDF** — it ends at §7 plus the script page. See Open questions. |

## 3. Talent / continuity

- Woman, 40s, dark hair loosely up, rust satin shirt, fine gold necklace, small gold hoops.
- Warm, dry, self-possessed. Talking to camera as if to someone she already knows.
- Voice: American, female, deeper. Played **dry, not seductive** (brief §6 — the script carries the innuendo).
- Rustic timber cabin at dusk. Live stone fire, B&W snowy forest print over the mantel, tan leather sofas, lamps, candles. Dark blue evening light through the window.
- She never moves from the table. Only real change: bottle in hand (Frame A) vs on the table (Frame B).

### Hard continuity rules (brief §6)
- Fire stays lit and visible in every shot.
- Wine level only ever goes **down**. One sip, at shot 7.
- Label readable and steady for >= 2s in shot 5; can be soft everywhere else.
- Do not cut on every line — the long holds are the point.

## 4. Shot map

| # | TC | Dur | Frame | Voiceover | On-screen |
|---|---|---|---|---|---|
| 1 | 0:00-0:03 | 3s | B | HOOK (3 variants) | [hook line] |
| 2 | 0:03-0:07 | 4s | B | When I go on dates, I'm always looking for the right signs. | The signs I look for |
| 3 | 0:07-0:10 | 3s | B, slight push in | Great clothes, great taste, in shape. | Clothes. Taste. In shape. |
| 4 | 0:10-0:15 | 5s | B -> A | But bringing this bottle to the table, tells me everything I need to know. | But this? This is the tell. |
| 5 | 0:15-0:22 | 7s | A, tighter | It's a full-bodied Cabernet Sauvignon, aged in 18 month oak, and it's got this smoky, tobacco finish. | Full-bodied Cab · 18 months in oak |
| 6 | 0:22-0:30 | 8s | A -> B | It's exactly like the man I want. Original, not following trends with Caymus or Ridge Estates, and not like anyone else I'll meet. | Original. Not a trend. |
| 7 | 0:30-0:39 | 9s | B | [sips] Ugh, it's so velvety and rich, and those layers of blackcurrant, plum, and espresso get my pallet so excited. | Blackcurrant · Plum · Espresso |
| 8 | 0:39-0:47 | 8s | B | The best part? If he's smart, he won't need to spend $85 on a bottle, he can just buy a case of 6 at 75% off. | $85 a bottle · case of 6 at 75% off |
| 9 | 0:47-0:51 | 4s | B | Then we can get to know each other better, all night. | [end card / CTA — TBC] |

Shot 4: the bottle lift lands **on the word "bottle"**, not after it.
Shot 7: hold ~2s on the taste before she speaks. Do not trim the pause.
Shot 8: steadiest hold of the spot — this is the offer.

## 5. Build pipeline

1. Composite seed frames at 9:16 — likeness/skin quality from the woman reference, scene from the cabin frame, Dolum bottle held as-is.
2. Frame A (bottle in hand) derived from Frame B so lighting and position match exactly.
3. VO per line, single voice.
4. Per-shot lip-synced talking head: `wan2_7` (start_image + audio_references), 1080p, 9:16, exact per-shot durations.
5. Assemble 9 shots, burn captions, lay fire-crackle/room-tone bed, export 3 hook variants.

## 6. Open questions for the user

- **§8, §9 and §10 are referenced but absent from the PDF.** §9 governs whether competitor names (Caymus, Ridge Estates) may be burned into on-screen text. Handled conservatively: the names stay in the **spoken** line as scripted, but the shot-6 caption reads "Original. Not a trend." with no competitor names burned in — which is what the shot table itself specifies.
- **End card / CTA is TBC in the brief** and no brand assets were supplied. Shot 9 is delivered clean, holding her look, with space for an end card to be dropped on.

---

# BUILD RECORD — v1 delivered

## Delivered films (9:16, 1080x1920, 30fps, 51.000s, AAC 48kHz stereo)

| Cut | Hook line | media_id | URL |
|---|---|---|---|
| Hook 1 | "If I met a man who drank this, I'd never forget him." | `65826dd1-f317-42dd-862e-fe61a2a61784` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/65826dd1-f317-42dd-862e-fe61a2a61784.mp4 |
| Hook 2 | "Yeah, this would keep us talking, all night." | `62bfd4f5-0134-4ca6-812c-46b3e77f9296` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/62bfd4f5-0134-4ca6-812c-46b3e77f9296.mp4 |
| Hook 3 | "This tells me everything I need to know about him." | `5179b1e8-2152-47b7-9799-61979a9b0087` | https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/5179b1e8-2152-47b7-9799-61979a9b0087.mp4 |

## Seed frames

| Frame | Source | job_id |
|---|---|---|
| **Frame B** (bottle on table) — master, user-selected | Seedream 4.5, 3 refs: cabin + likeness + bottle | `70178f61-58b6-4477-9af7-67948ccfa904` |
| **Frame A** (bottle lifted beside face) | Seedream 4.5, derived from Frame B | `d076c3e9-c091-4b0b-8b1a-e570a9f40ada` |
| **Frame A tight** (label hero, shot 5) | Seedream 4.5, derived from Frame B | `30f75c08-8cfa-405b-a166-8249d82254a9` |

Frames A and A-tight are derived *from the approved Frame B*, not regenerated from
the original references, so lighting, wardrobe, seating and colour grade carry over
exactly. Only the bottle position and framing change — which is the brief's
"one position, two setups" rule.

## Shot renders — Wan 2.7 (start_image + audio_references), 1080p 9:16

| # | Start frame | End frame | Target | Rendered | Trim | job_id |
|---|---|---|---|---|---|---|
| 1 h1 | B | — | 3s | 3.019 | cut | `af7ab356-c876-42ee-9b37-81b04c8dd239` |
| 1 h2 | B | — | 3s | 3.019 | cut | `aa4f0da0-5ef2-44c4-a929-0155691cc80c` |
| 1 h3 | B | — | 3s | 3.019 | cut | `4dcfdf02-a2ef-441c-92b4-84548a9f431a` |
| 2 | B | — | 4s | 4.040 | cut | `6896fac7-1a1a-4ccf-b0ea-b9a3896c8b2a` |
| 3 | B | — | 3s | 3.019 | cut | `aed0ed5c-e2e8-4f8e-8728-8874d1cbf45e` |
| 4 | B | **A** | 5s | 5.062 | cut | `577d8399-84d7-4f14-ac41-24363d86c0b7` |
| 5 | A tight | — | 7s | 7.036 | cut | `ed329903-0658-43c5-90a4-fb59aa85031f` |
| 6 | A tight | **B** | 8s | 8.080 | cut | `85900eeb-c4c7-4116-afef-e5e308b0bdab` |
| 7 | B | — | 9s | 9.032 | cut | `e87dbd3a-5652-4149-8e25-94e60f5d3350` |
| 8 | B | — | 8s | 8.034 | cut | `3886b433-3196-40f1-aa4f-31f08a7e39d6` |
| 9 | B | — | 4s | 4.040 | cut | `e07f14ee-47f4-4303-af7c-a213868a878b` |

Every shot rendered **longer** than its slot, so all nine are straight trims.
Nothing was sped up or slowed down to fit — the performance runs at true speed.

Shots 4 and 6 use start+end keyframes so the B→A and A→B moves are real moves
rather than cuts, which is what the brief's "transition to FRAME A" asks for.

## Audio

Single voice, **Naomi** (`caeba733-3c17-43db-863e-69c7025512cd`, preset), ElevenLabs
engine via `text2speech_v2`. Per-shot stems were cut to exact shot length *before*
the video was generated, then used as the lip-sync driver — so the mouth is synced
to the very same audio that ends up on the timeline. No drift.

| Shot | Raw | Trimmed | Head pad | Tempo | Locked |
|---|---|---|---|---|---|
| h1 | 3.87 | 3.79 | 0.02 | **1.280** | 3.000 |
| h2 | 2.35 | 2.26 | 0.15 | 1.0 | 3.000 |
| h3 | 3.00 | 2.91 | 0.05 | 1.0 | 3.000 |
| 2 | 3.40 | 3.26 | 0.20 | 1.0 | 4.000 |
| 3 | 3.08 | 2.96 | 0.03 | 1.021 | 3.000 |
| 4 | 4.28 | 4.23 | 0.25 | 1.0 | 5.000 |
| 5 | 6.92 | 6.77 | 0.15 | 1.0 | 7.000 |
| 6 | 7.89 | 7.73 | 0.15 | 1.0 | 8.000 |
| 7 | 8.67 | 8.53 | 1.60 (sip) | **1.168** | 9.000 |
| 8 | 8.20 | 8.11 | 0.03 | 1.027 | 8.000 |
| 9 | 3.08 | 2.97 | 0.10 | 1.0 | 4.000 |

Bed: fire crackle and cabin room tone (`mirelo_text_to_audio`, 20s looped to 51s,
normalised to -30 LUFS, 1.5s fades at head and tail) sitting under the dialogue,
per brief section 3.

Final mix: dialogue to -16 LUFS, mixed with the bed, limited, final pass to
**-14 LUFS / -1.0 dBTP**. Measured on the delivered files: **-14.3, -14.4, -14.2 LUFS**
— within 0.2 LU across the three cuts, so the variants are genuinely comparable in test.

## Captions

`tools/build_right_signs_captions.py` — one burned-in card per shot, Montserrat
SemiBold 60px, white with a dark outline, 330px bottom margin to clear platform UI.
Cards are inset 0.15s inside each cut so they do not flick on the edit.
Shot 7's card waits for the sip (starts 31.70s, not 30.00s).
Copy is verbatim from the brief's shot table.

## Verification performed

- Picture: body 48.000s, each variant 51.000s, 1530 frames at 30fps, 1080x1920.
- Every source shot confirmed longer than its slot before trimming (no speed change).
- Audio stems confirmed at exactly their target lengths before being used as lip-sync drivers.
- Integrated loudness measured per delivered file.

**Not verified:** I could not view any frame. The media CDN is blocked from this
workspace by network policy, and the Higgsfield sandbox returns text only. So the
likeness, the label legibility in shot 5, the lip-sync quality and the wine-level
continuity are all *unreviewed by me* and need a human eye. The Frame B seed was
chosen by the user from a rendered set for exactly this reason.

## Open items

1. **No end card.** Shot 9 is delivered clean, holding her look for ~1s past the
   line, with space for an end card. The brief lists it as TBC and no brand assets
   were supplied.
2. **Sections 8, 9 and 10 are missing from the supplied PDF** (it ends at section 7
   plus the script page) though the text references them twice. Section 9 governs
   burning in competitor names. Handled conservatively: Caymus and Ridge Estates
   stay in the *spoken* line as scripted, but no competitor name is burned into
   on-screen text — which is what the shot table itself specifies.
3. **Shot 7 timing is over-subscribed in the brief.** The line at natural pace is
   8.53s; the shot is 9s and the brief also wants a ~2s sip hold before she speaks.
   That does not fit. Resolved as a 1.6s sip plus the line at 1.168x. The alternative
   is to let the sip run its full 2s and push the line to ~1.24x, or to extend shot 7
   — which would break the locked timeline the brief requires.
4. **Hook 1 runs 1.28x.** At natural pace it is 3.79s against a 3s slot. The brief
   locks the body to 0:03 in every cut, so the hook had to compress. Hooks 2 and 3
   sit inside their slot at natural pace.
5. **Voice not iterated**, per instruction that an editor will take it on. Stems are
   available if the VO is replaced — though note that replacing the audio breaks the
   lip-sync, since the mouth is synced to these exact takes. A re-voice means
   re-running the Wan 2.7 pass with the new stems.

---

# BUILD RECORD — v2: cut to the supplied voiceover

User instruction: *"Try generating the same video but with this seed image. I have
audio that works well, so please match the video frames to it."*

So in v2 **the audio is the master**. The picture is cut to it, and the supplied
WAV is muxed back in untouched rather than rebuilt.

## Delivered

**https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/aeece908-f418-4c39-8d31-eec87e984ae7.mp4**

1080x1920, 30fps, 1530 frames, 51.015s, AAC 44.1kHz stereo.
media_id `aeece908-f418-4c39-8d31-eec87e984ae7`.

## What the supplied audio actually contains

Transcribed with faster-whisper (`small.en`, word timestamps) rather than assumed.
Two structural differences from the brief, both followed as delivered:

1. **The hook is Hook 2** — "Yeah, this would keep us talking, all night." Only one
   cut is therefore possible from this VO, not three.
2. **Shot 7 is restructured.** The brief has `[sips it]` then "Ugh, it's so velvety
   and rich, and those layers...". The VO drops "Ugh", puts **"It's so velvety and
   rich."** *before* the sip, then takes a **2.30s sip pause** (30.48-32.78), then
   continues "And those layers of blackcurrant...". That reads better than the
   brief's order and the picture was built to match it.
3. **The VO ends at 46.98s** and the file runs to 51.014s, leaving a **4.03s silent
   hold** at the end — exactly where the brief's TBC end card belongs.

## Shot grid — derived from word timings, not the brief's timecodes

Cut points snapped to 30fps frame boundaries; every cut placed inside an
inter-word gap.

| # | In | Out | Frames | Dur | Frame | Line |
|---|---|---|---|---|---|---|
| 1 | 0.000 | 4.200 | 126 | 4.200 | B | hook |
| 2 | 4.200 | 7.367 | 95 | 3.167 | B | "When I go on dates..." |
| 3 | 7.367 | 10.800 | 103 | 3.433 | B | "Great clothes, great taste, in shape," |
| 4 | 10.800 | 14.067 | 98 | 3.267 | B -> A | "but bringing this bottle to the table..." |
| 5 | 14.067 | 21.200 | 214 | 7.133 | A tight | "It's a full-bodied Cabernet Sauvignon..." |
| 6 | 21.200 | 28.733 | 226 | 7.533 | A tight -> B | "It's exactly like the man I want. Original..." |
| 7 | 28.733 | 36.800 | 242 | 8.067 | B | "It's so velvety and rich." [SIP] "And those layers..." |
| 8 | 36.800 | 44.267 | 224 | 7.467 | B | "The best part?... 75% off." |
| 9 | 44.267 | 51.000 | 202 | 6.733 | B | "Then we can get to know each other better, all night." + 4s hold |

Shot 4's bottle lift is cued to land on the word "bottle" at 11.60s, 0.80s into the shot.
Shot 7's sip is cued at 1.75s-4.05s into the shot, matching the real gap.

## Frames

| Frame | job_id |
|---|---|
| Frame B — the user's supplied seed | media `792a2ea0-614e-467b-b98a-34b3624d6c94` |
| Frame A (bottle lifted) | `95a7e863-dd9d-43cd-87fb-e1b191fb96d9` |
| Frame A tight (label hero) | `e4ba6e14-4f96-4180-9137-d94ad884f453` |

Note: the supplied seed is the text-to-image render from the first, reference-less
batch of v1 — a different talent to the "Sara" likeness reference. That is the
user's explicit choice.

## Shot renders — Wan 2.7, each driven by its own slice of the client VO

| # | job_id | source dur | slot | trim |
|---|---|---|---|---|
| 1 | `1712364c-e554-470c-954c-763c15069d51` | 5.039 | 4.200 | cut |
| 2 | `e4536642-5070-4b70-a24f-960b6ffe39bd` | 4.040 | 3.167 | cut |
| 3 | `ba5f4bb9-d1d9-48bd-a700-040740731236` | 4.040 | 3.433 | cut |
| 4 | `eb0bedb5-7f80-495f-b220-b9978bfe6a8e` | 4.063 | 3.267 | cut |
| 5 | `f878b3bb-aeef-44f9-8e5a-91c5b8f5982a` | 8.034 | 7.133 | cut |
| 6 | `dae61f73-4270-47b0-b1ec-1863262b3a17` | 8.080 | 7.533 | cut |
| 7 | `575073c0-3f13-4c45-91f7-b0d8378de28a` | 9.032 | 8.067 | cut |
| 8 | `9e06bbae-5623-4efd-a633-e1264ace81e3` | 8.034 | 7.467 | cut |
| 9 | `20fd6e7c-cb93-461d-a2bd-6f6488b4d6f4` | 7.036 | 6.733 | cut |

All nine straight trims. No speed change anywhere.

**Aspect trap:** seven of the nine shots returned at **1076x1928**, not 1080x1920,
despite the 9:16 request. A concat of mixed dimensions silently produced a broken
1076x1928 master on the first pass. Fixed by normalising every shot with
`scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1`
— scale-to-cover then centre-crop, so faces are not stretched (a plain scale would
have squeezed them ~0.8% horizontally).

## Verification

- Picture: 1530 frames, all nine shots confirmed 1080x1920 before concat.
- **Audio integrity:** decoded final vs supplied source — 51.014s vs 51.014s,
  delta **0.0 ms**; envelope cross-correlation best lag **0 ms**, correlation
  **1.0000**. The client's VO is carried through un-retimed and un-shifted.
- **Cut placement:** at 10ms resolution, **8/8 cuts land in inter-word silence**.
  Tightest are 36.800s (7.98% of peak, 200ms gap) and 44.267s (8.91%, 220ms gap);
  the rest sit under 4.5%.

**Still not verified:** I cannot see any frame — the media CDN is blocked from this
workspace. Likeness, label legibility in shot 5, lip-sync quality and wine-level
continuity remain unreviewed by me.

## Open items carried forward

1. **One cut only.** The supplied VO contains Hook 2, so the three-variant test
   structure from the brief is not possible without VO for hooks 1 and 3.
2. **No end card.** The 4.03s silent tail is held on her look. Brand assets were
   never supplied.
3. **Competitor names** stay spoken (they are in the client's own VO) but are not
   burned into on-screen text, per the brief's shot table.
4. **No fire-crackle bed.** v1 added one; v2 uses the supplied mix exactly as given,
   since the instruction was to match the video to that audio. If room tone is
   wanted under it, it can be laid without touching the dialogue.
