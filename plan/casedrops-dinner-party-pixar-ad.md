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
| **Sarah** (mum) | Mid-30s. Chestnut wavy hair in a collapsing messy bun, two loose strands on the cheek, large round hazel eyes, freckles across the nose, flushed cheeks, small gold hoops. Mustard-yellow knit sweater, sleeves shoved past the elbows, over an olive-green apron. | American, General American accent, mid-30s, harried and breathless |
| **Darren** (son, mid-20s) | A grown adult. Tall and lanky, stubble, floppy sandy hair, headphones round his neck, rumpled dark band t-shirt with a ketchup stain. Sprawled on the sofa on his phone. | Non-speaking |
| **Husband** | Never seen. | American, thin and tinny through the phone speaker, sheepish |

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
| 11 | 03.0 | 05.0 | 2.0s | CLOSE on her face, lit from the doorway. Shoulders drop, breathing slows, slow relieved smile. | *(one long sigh)* |
| 12 | 05.0 | 07.5 | 2.5s | Crouches, hoists the crate onto her hip, carries it inside, heels the door shut. | — |
| 13 | 07.5 | 10.0 | 2.5s | WIDE, dining room. Sets the crate down on the table between the candles, hands on hips, radiant. | Sarah *(bright)*: "Ok, everyone ready?!" |
| 14 | 10.0 | 15.0 | **5.0s** | **AERIAL PULL-OUT for the text overlay.** Hard cut to exterior. The camera rises steadily up and back from the house — roof falls away, then the yard, the driveway, the front tree, then the neighbouring houses and the street, all in warm dusk with Sarah's windows glowing golden. Continuous, never stops. House sits low in the bottom third; the upper two-thirds is open clean dusk sky held as negative space for "Casedrops". No cut, no fade. | Underscore resolving |

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

## Getting the voices American

The first American attempt still came back British. The accent instruction was there, but **the whole
scene description was written in British English** — jumper, hob, tea towel, mum, sofa, roasting tray,
chopping boards, "cosy". Seedance casts the voice to match the world the prompt describes, so every
one of those words was pulling the read back toward RP no matter what the audio block said.

The fix was to Americanise the world, not just the instruction:

| Was | Now |
|---|---|
| jumper | sweater |
| hob | stove |
| tea towel | dish towel |
| sofa | couch |
| roasting tray | roasting pan |
| chopping boards | cutting boards |
| mum | mom |
| "cosy suburban family kitchen" | "American suburban family home in the United States" |

The accent instruction is also now stated three times — as the first line of the prompt, in the audio
block, and inline on each spoken line — and the hard-rules block names the accents to avoid.

**One British phrase remains, and it is in the dialogue:** "Can someone lay the table!" An American
would say *set* the table. It was left verbatim because it is the client's script, but it is the last
remaining cue pulling the read British. If the accent is still not clean, switching that one word is
the next thing to try.

If a re-render still will not hold the accent, the fallback is post-hoc: Higgsfield's `dubbing` or
`voice_change` tools can re-voice a finished render without regenerating the animation.

## Content-filter constraint (still applies)

"God, who's that!" is blocked deterministically and reads "Oh, who's that now!" — see the probe table
further down. Darren stays a mid-twenties adult so no under-25 appears in an alcohol ad.

## Output

| Job | Part | Outcome |
|---|---|---|
| `26c5c3fa` | — | rejected (nsfw), cause then unknown |
| `bd44d5c3` | — | rejected (nsfw), cause then unknown |
| `e2d71b90` | — | superseded: 30s single cut, British voices, no panic beat |
| `26bd53a9` | A | superseded: British voices |
| `faa9bb1e` | B | superseded: British voices, static end hero. Confirmed 9:16 on playback |
| `d3907287-0937-4084-be9d-03a633db52b6` | **A** | **current** — 30.0s, 1080x1920, American prompt |
| `3a43668f-c2c4-446d-9c7c-f4cbed318c0f` | **B** | **current** — 15.0s, American prompt, aerial ending |

Part A: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260921_082825_d3907287-0937-4084-be9d-03a633db52b6.mp4

Part B: https://d8j0ntlcm91z4.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/hf_20260921_083730_3a43668f-c2c4-446d-9c7c-f4cbed318c0f.mp4

Cost: 360 credits per 30s 1080p render, 180 per 15s extension, 12 per 4s 480p probe.
Balance after this round: roughly 750 credits — about two more 30s renders.

`video_extension` reports `16:9` / `1920x1080` in its echoed job metadata, but the earlier Part B was
confirmed **9:16 on playback**. The metadata is wrong; the output does follow the source. Ignore it.

Neither file is committed here and **neither has been watched**: this workspace's egress policy
blocks the Higgsfield CDN, so the renders could not be downloaded or played back. The shot timings
above are what was *requested* of the model, not what has been verified. Worth checking on playback:
that both voices are genuinely American, that the spiral line at 15.5-21.0s is not clipped, that the
panic montage reads as comedy rather than distress, and that the aerial pull-out keeps rising for the
full five seconds with enough clean sky for the "Casedrops" overlay.
