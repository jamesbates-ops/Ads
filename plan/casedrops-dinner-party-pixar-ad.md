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
| **Darren** (son, ~10) | Messy sandy hair, oversized t-shirt with a huge ketchup stain, slumped on the sofa. | Non-speaking |
| **Husband** | Never seen. | Male, thin and tinny through the phone speaker, sheepish |

Setting: a cosy, cluttered suburban family kitchen opening onto a dining room. Early evening, low golden
sun through the window, warm practical lamps, half-lit candles, a half-set table.

## Timestamped shot list

| # | In | Out | Dur | Shot | Line / audio |
|---|---|---|---|---|---|
| 1 | 00.0 | 03.5 | 3.5s | MEDIUM. Oven door yanked open, fat plume of grey smoke into her face, blackened roasting tray. She staggers back flapping a tea towel, coughing. | Sarah *(exasperated, panicking)*: "Oh no, the food's burnt!" |
| 2 | 03.5 | 06.0 | 2.5s | QUICK CUT, wider. Spins on her heel toward the dining-room doorway, hand cupped round her mouth, towel still flapping. | Sarah *(shouts)*: "Can someone lay the table!" |
| 3 | 06.0 | 08.5 | 2.5s | REVERSE. Sarah foreground jabs a finger toward the living room; Darren freezes mid-slouch on the sofa behind. | Sarah *(scolding)*: "Put on a clean shirt, Darren." |
| 4 | 08.5 | 10.0 | 1.5s | TIGHT CLOSE-UP. Sleeve snapped back, staring at her wristwatch. Pupils shrink to pinpricks. | No dialogue — loud ticking watch |
| 5 | 10.0 | 12.0 | 2.0s | MEDIUM CLOSE. Phone pinned between ear and shoulder, both hands frantically stirring a pot. | Sarah *(urgent, clipped)*: "Are you getting the wine?" |
| 6 | 12.0 | 15.5 | 3.5s | Same framing, slow push in on her face. Stirring stops dead; expression collapses. | Husband *(phone speaker)*: "I didn't have time, and what do I even get?" |
| 7 | 15.5 | 21.0 | 5.5s | MEDIUM. Sags back against the counter and slides down slightly, phone limp at her side, head tipped to the ceiling. | Sarah *(fast, deflating spiral)*: "Oh, this is going to be awful, Lucy always has everything ready and she's gonna be so happy to see me fail." |
| 8 | 21.0 | 22.5 | 1.5s | Snaps bolt upright, hair bouncing, eyes wide. | DING-DONG. Sarah: "God, who's that!" |
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

## Output

- Higgsfield job: `26c5c3fa-7aa2-42b7-8b9d-df2e34e596e2`
- Cost: 360 credits
