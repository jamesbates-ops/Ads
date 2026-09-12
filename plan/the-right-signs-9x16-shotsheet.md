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
