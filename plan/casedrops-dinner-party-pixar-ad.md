# Casedrops — "Dinner Party" 30-second Pixar-style ad

Format: **9:16 vertical, 1080p, ~45s across two renders**, 3D animated in the Pixar house style,
native dialogue audio, **American voices**.
Model: **Seedance 2.5** (`seedance_2_5`) via Higgsfield, `mode: t2v`, `generate_audio: true`, `bitrate_mode: high`.

Seedance 2.5 caps a single generation at 30 seconds, so the spot is built as **two renders**:

- **Part A (30.0s)** — `t2v`. The spiral, ending on the doorbell.
- **Part B (15.0s)** — `video_extension`, `extension_mode: forward`, taking Part A's job as its video
  reference. Extending rather than generating fresh is what carries Sarah's face, the house and the
  lighting across the join by construction, which matters because neither half can be previewed from
  this workspace.

Within each part, Seedance handles the shot changes internally, so the character stays consistent
across the beats — the thing that breaks when shots are generated separately.

## Cast

| Role | Description | Voice |
|---|---|---|
| **Sarah** (mum) | Mid-30s. Chestnut wavy hair in a collapsing messy bun, two loose strands on the cheek, large round hazel eyes, freckles across the nose, flushed cheeks, small gold hoops. Mustard-yellow knit jumper, sleeves shoved past the elbows, over an olive-green apron. | **American** (General American), mid-30s, harried and breathless |
| **Darren** (son, mid-20s) | A grown adult. Tall and lanky, stubble, floppy sandy hair, headphones round his neck, rumpled dark band t-shirt with a ketchup stain. Sprawled on the sofa on his phone. | Non-speaking |
| **Husband** | Never seen. | **American**, thin and tinny through the phone speaker, sheepish |

Setting: a cosy, cluttered suburban family kitchen opening onto a dining room. Early evening, low golden
sun through the window, warm practical lamps, half-lit candles, a half-set table.

## Timestamped shot list

### Part A — 30.0s (job `26bd53a9`)

| # | In | Out | Dur | Shot | Line / audio |
|---|---|---|---|---|---|
| 1 | 00.0 | 03.5 | 3.5s | MEDIUM. Oven door yanked open, plume of grey smoke, blackened roasting tray. She staggers back flapping a tea towel, coughing. | Sarah *(exasperated)*: "Oh no, the food's burnt!" |
| 2 | 03.5 | 06.0 | 2.5s | QUICK CUT, wider. Spins to the dining-room doorway, hand cupped round her mouth. | Sarah *(shouts)*: "Can someone lay the table!" |
| 3 | 06.0 | 08.5 | 2.5s | REVERSE. Jabs a finger at the living room; Darren looks up from his phone, clocks the ketchup stain, grimaces. | Sarah *(scolding)*: "Put on a clean shirt, Darren." |
| 4 | 08.5 | 10.0 | 1.5s | TIGHT CLOSE-UP. Sleeve snapped back, staring at her watch. Pupils shrink to pinpricks. | Ticking watch |
| 5 | 10.0 | 12.0 | 2.0s | MEDIUM CLOSE. Phone at her shoulder, both hands stirring a pot. | Sarah *(urgent)*: "Are you getting the wine?" |
| 6 | 12.0 | 15.5 | 3.5s | Slow push in. Stirring stops dead; expression collapses. | Husband *(phone speaker)*: "I didn't have time, and what do I even get?" |
| 7 | 15.5 | 21.0 | 5.5s | MEDIUM. Sags back against the counter, phone limp, head tipped to the ceiling. | Sarah *(deflating spiral)*: "Oh, this is going to be awful, Lucy always has everything ready and she's gonna be so happy to see me fail." |
| 8 | 21.0 | 28.5 | **7.5s** | **PANIC MONTAGE.** Hands to cheeks, then she bolts. Whip-pans follow her tearing round the house in a loop — hallway skid, round the dining table fast enough to bend the candle flames, past Darren lifting his feet without looking up, back to the kitchen. Two laps, faster the second. Hair shaking loose, apron strings flying. | Long high-pitched comedic wail, yelping |
| 9 | 28.5 | 30.0 | 1.5s | DING-DONG cuts through it. She stops dead mid-sprint, one foot skidding, frozen in a comic pose. | Sarah: "Oh, who's that now!" |

### Part B — 15.0s (job `faa9bb1e`, extends Part A forward)

| # | In | Out | Dur | Shot | Line / audio |
|---|---|---|---|---|---|
| 10 | 00.0 | 03.0 | 3.0s | HALLWAY, over the shoulder. Door pulled open — nobody there. A plain unmarked kraft-brown crate on the mat, six sealed corked necks, warm porch light. Slow push in. | — |
| 11 | 03.0 | 05.5 | 2.5s | CLOSE on her face, lit from the doorway. Shoulders drop, breathing slows, slow relieved smile. | *(one long sigh)* |
| 12 | 05.5 | 08.0 | 2.5s | Crouches, hoists the crate onto her hip, carries it inside, heels the door shut. | — |
| 13 | 08.0 | 10.0 | 2.0s | WIDE, dining room. Plants the crate on the table between the candles, hands on hips, radiant. | Sarah *(bright)*: "Ok, everyone ready?!" |
| 14 | 10.0 | 15.0 | **5.0s** | **HELD HERO SHOT for the text overlay.** Almost imperceptible push in on the crate on the candlelit table, Sarah beside it, calm. Only candle flicker and a drifting dust mote. Upper third kept clean — warm wall and soft bokeh — as reserved negative space. No cut, no fade. | Underscore resolving |

**Total ~45.0s.**

## Script change forced by the platform

**One line in the brief could not be rendered.** "God, who's that!" is blocked deterministically by
Higgsfield's content filter — it failed on two full 30s renders and then twice more on isolated
4-second probes of that line alone. It now reads:

> "Oh, who's that now!"

Alternatives that keep the same exasperation if you prefer a different swap: "Ugh, who's that now!",
"Who on earth is that!", "Oh no, who's that!". Every other line in the brief is verbatim.

### How that was established

Rather than keep re-rolling a 30s render, four 4-second 480p probes (12 credits each) isolated one
variable apiece:

| Probe | Variable under test | Result |
|---|---|---|
| 1 | Burnt food / oven smoke | passed |
| 2 | Wine crate + "Are you getting the wine?" | passed |
| 3 | "God, who's that!" | **failed** |
| 4 | The "this is going to be awful / see me fail" spiral | passed |
| 5 | "God, who's that!" re-run verbatim | **failed** (so it is deterministic, not a flake) |
| 6 | Same shot, line swapped to "Oh, who's that now!" | passed |

So the alcohol is fine, the despair is fine, and the son is fine. Only the interjection was blocked.

Two earlier 30s renders (`26c5c3fa`, `bd44d5c3`) were rejected before this was understood. Rejected
renders do not appear to consume credits — the balance did not move across the second rejection.

## Casting note — alcohol advertising

Darren is rendered as a **grown adult in his mid-twenties**, not a child. Alcohol advertising codes
(UK CAP among them) require that nobody who is, or looks, under 25 appears in an alcohol ad. The
scolding beat plays just as well with an adult son who still lives at home. If the ad will not run
under those codes and you want a young child instead, that is a one-line prompt change and a
re-render.

## Open issue — check Part B's aspect ratio first

`video_extension` mode **ignores the `aspect_ratio` parameter**. The model documentation says the
output instead follows the shape of the video being extended, which would make Part B 1080x1920
portrait like Part A. But the job metadata came back reading `16:9`, `1920x1080`. Those contradict
each other and the file cannot be opened from this workspace to settle it.

**Open Part B and check its orientation before cutting.** Part A is confirmed 1080x1920 in its own
metadata.

If Part B is landscape, the extension route will not serve a vertical ad. The fallback is to
re-render Part B as a standalone `t2v` at 9:16 with the character block copied verbatim from Part A's
prompt — cheaper and correctly shaped, but it gives up the extension's guaranteed continuity, so
Sarah should be compared across the join before committing.

## Output

| Job | Part | Outcome |
|---|---|---|
| `26c5c3fa-7aa2-42b7-8b9d-df2e34e596e2` | — | rejected (nsfw), cause then unknown |
| `bd44d5c3-53e8-40ef-9cbc-bb4fe0e525d3` | — | rejected (nsfw), cause then unknown |
| `e2d71b90-99b7-4530-9a1c-50c7da097372` | — | superseded 30s cut, British voices, no panic beat |
| `26bd53a9-8994-4c66-b8dc-9bdb93b3a761` | **A** | **current** — 30.0s, 1080x1920 |
| `faa9bb1e-b2a6-4bc9-980e-d9df3148d240` | **B** | **current** — 15.0s, aspect ratio to be confirmed |

Part A: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260918_175013_26bd53a9-8994-4c66-b8dc-9bdb93b3a761.mp4

Part B: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260918_175921_faa9bb1e-b2a6-4bc9-980e-d9df3148d240.mp4

Cost: 360 credits per 30s 1080p render, 180 per 15s extension, 12 per 4s 480p probe.

Neither file is committed here and **neither has been watched**: this workspace's egress policy
blocks the Higgsfield CDN, so the renders could not be downloaded or played back. The shot timings
above are what was *requested* of the model, not what has been verified. Worth checking on playback:
Part B's aspect ratio, that the spiral line at 15.5-21.0s is not clipped, that the panic montage
reads as comedy rather than distress, that both voices are American, and that the final 5 seconds
hold steady with usable clean space for the overlay.
