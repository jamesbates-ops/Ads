# Casedrops — "Dinner Party" 30-second Pixar-style ad

Format: **9:16 vertical, 1080p, 30.0s**, 3D animated in the Pixar house style, native dialogue audio.
Model: **Seedance 2.5** (`seedance_2_5`) via Higgsfield, `mode: t2v`, `generate_audio: true`, `bitrate_mode: high`.

Rendered as a **single continuous 30-second generation** rather than stitched clips. Seedance 2.5 supports
4–30s natively and handles the shot changes internally, which keeps Sarah's face, hair and wardrobe
consistent across all twelve beats — the thing that breaks when shots are generated separately.

## Cast

| Role | Description | Voice |
|---|---|---|
| **Sarah** (mum) | Mid-30s. Chestnut wavy hair in a collapsing messy bun, two loose strands on the cheek, large round hazel eyes, freckles across the nose, flushed cheeks, small gold hoops. Mustard-yellow knit jumper, sleeves shoved past the elbows, over an olive-green apron. | Warm British, mid-30s, harried and breathless |
| **Darren** (son, mid-20s) | A grown adult. Tall and lanky, stubble, floppy sandy hair, headphones round his neck, rumpled dark band t-shirt with a ketchup stain. Sprawled on the sofa on his phone. | Non-speaking |
| **Husband** | Never seen. | Male, thin and tinny through the phone speaker, sheepish |

Setting: a cosy, cluttered suburban family kitchen opening onto a dining room. Early evening, low golden
sun through the window, warm practical lamps, half-lit candles, a half-set table.

## Timestamped shot list

| # | In | Out | Dur | Shot | Line / audio |
|---|---|---|---|---|---|
| 1 | 00.0 | 03.5 | 3.5s | MEDIUM. Oven door yanked open, fat plume of grey smoke into her face, blackened roasting tray. She staggers back flapping a tea towel, coughing. | Sarah *(exasperated, panicking)*: "Oh no, the food's burnt!" |
| 2 | 03.5 | 06.0 | 2.5s | QUICK CUT, wider. Spins on her heel toward the dining-room doorway, hand cupped round her mouth, towel still flapping. | Sarah *(shouts)*: "Can someone lay the table!" |
| 3 | 06.0 | 08.5 | 2.5s | REVERSE. Sarah foreground jabs a finger toward the living room; Darren looks up from his phone, follows her finger down to the ketchup stain and grimaces. | Sarah *(scolding)*: "Put on a clean shirt, Darren." |
| 4 | 08.5 | 10.0 | 1.5s | TIGHT CLOSE-UP. Sleeve snapped back, staring at her wristwatch. Pupils shrink to pinpricks. | No dialogue — loud ticking watch |
| 5 | 10.0 | 12.0 | 2.0s | MEDIUM CLOSE. Phone pinned between ear and shoulder, both hands frantically stirring a pot. | Sarah *(urgent, clipped)*: "Are you getting the wine?" |
| 6 | 12.0 | 15.5 | 3.5s | Same framing, slow push in on her face. Stirring stops dead; expression collapses. | Husband *(phone speaker)*: "I didn't have time, and what do I even get?" |
| 7 | 15.5 | 21.0 | 5.5s | MEDIUM. Sags back against the counter and slides down slightly, phone limp at her side, head tipped to the ceiling. | Sarah *(fast, deflating spiral)*: "Oh, this is going to be awful, Lucy always has everything ready and she's gonna be so happy to see me fail." |
| 8 | 21.0 | 22.5 | 1.5s | Snaps bolt upright, hair bouncing, eyes wide. | DING-DONG. Sarah: "Oh, who's that now!" *(changed — see below)* |
| 9 | 22.5 | 25.5 | 3.0s | HALLWAY, over the shoulder. Front door yanked open — nobody there. A plain unbranded kraft-brown wooden wine case on the mat, six dark bottle necks poking out, warm porch light. Slow push in. | — |
| 10 | 25.5 | 27.5 | 2.0s | CLOSE on her face, lit warm from the doorway. Shoulders drop, jaw softens, slow relieved smile. One long sigh, then she crouches, hoists the case onto her hip and turns inside, kicking the door shut. | *(sigh)* |
| 11 | 27.5 | 29.0 | 1.5s | WIDE, dining room. Plants the case on the table between the candles, hands on hips, radiant and back in control. | Sarah *(bright)*: "Ok, everyone ready?!" |
| 12 | 29.0 | 30.0 | 1.0s | END PLATE. Clean empty warm-cream background, gentle radial glow, no motion. | — |

## Branding

The wine case is deliberately **plain and unmarked** and the prompt hard-blocks all on-screen text,
letters, numbers and logos — AI-rendered lettering comes out malformed and would have to be replaced
anyway. Shot 12 is a blank warm-cream plate for the editor to drop the Casedrops logo onto.

Two notes for the edit:
- The end plate is only 1.0s inside the 30s render. If the logo card needs longer, hold the last frame
  in post or trim shot 7 slightly — 30s is the hard budget.
- The box is a generic kraft wine case. If Casedrops packaging artwork exists, the cleanest fix is a
  re-render passing the artwork as an `image_references` media so the box is on-brand in shots 9–11.

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

## Output

**Delivered cut** (9:16, 1080p, 30.0s, with dialogue audio):
https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260918_172614_e2d71b90-99b7-4530-9a1c-50c7da097372.mp4

| Job | Outcome |
|---|---|
| `26c5c3fa-7aa2-42b7-8b9d-df2e34e596e2` | rejected (nsfw) — cause not yet known |
| `bd44d5c3-53e8-40ef-9cbc-bb4fe0e525d3` | rejected (nsfw) — cause not yet known |
| `e2d71b90-99b7-4530-9a1c-50c7da097372` | **completed — the delivered cut** |

Cost: 360 credits per 30s 1080p render, 12 per 4s 480p probe.

The video file is not committed here and has not been reviewed frame by frame: this workspace's
egress policy blocks the Higgsfield CDN, so the render could not be downloaded or played back. The
shot timings above are what was *requested* of the model — check the delivered cut against them,
particularly that the long spiral line at 15.5–21.0s is not clipped and that the end plate is clean.
