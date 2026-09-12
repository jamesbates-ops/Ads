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
