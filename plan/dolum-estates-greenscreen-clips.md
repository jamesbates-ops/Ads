# Dolum Estates: green-screen presenter ad (Casedrops) — clip pack

Individual clips for a 9:16 green-screen edit: the presenter keyed over B-roll. Not assembled.

| Zip | Contents | Size |
|---|---|---|
| [dolum_presenter_greenscreen.zip](https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/5c655ea6-a470-4315-af93-6cb2b3a76e33.zip) | 17 lip-synced presenter clips on green screen (3 hook variants + 14 body lines), the reference still, `presenter_clips.csv`, README | 74 MB |
| [dolum_broll.zip](https://d2ol7oe51mr4n9.cloudfront.net/user_3IlTIleUqdksHUuNWaJnSBuISip/6c6cf7bf-6d26-4867-ba0b-e50627728b6d.zip) | 32 B-roll clips (1080x1920, 24 fps, 5 s, silent), `broll_shots.csv`, README | 331 MB |

## Presenter

- Seed image: `wine_image_3_rombauer_pour.png` (Higgsfield media `371525ee-08e0-44fc-94f6-1378979dd61d`). It shows a Rombauer Chardonnay pour with La Crema and Hagel & Ane bottles on a table, so the reference was re-made with the same man and suit, waist-up on chroma green, holding a glass of red, with no bottles or labels.
- Clips: Gemini Omni Flash, 720x1280, 24 fps. Gemini's filter blocked the two lines naming Robert Mondavi and Baron Philippe de Rothschild (files 05 and 06), so those were made on Kling 3.0 Pro from the same still.
- Voice: every clip re-voiced with the Higgsfield preset **Callum** (`858499d9-fef5-40e1-bc29-b4dc661dc283`); lip-sync timing is kept.
- Key colour about `#039E38`; ffmpeg `chromakey=0x039E38:0.12:0.06` + `despill` keys cleanly without eating the navy suit.
- Every clip was checked word-for-word against a Whisper transcript. In file 12 the opening "And" is soft.

## Timing

The brief's section timings don't fit the words: the revelation section alone is ~106 words, about 38 s of speech against a 30 s slot. All words are kept. Measured speech per clip:

| File | Section | Line | Speech in | Speech out | Speech length |
|---|---|---|---|---|---|
| `01_HOOK-1_opening+prohibition.mp4` | Opening + Hook 1 | Stay till the end for an amazing deal. Prohibition almost wiped Napa Valley off the map. | 0.31s | 6.08s | 5.8s |
| `02_HOOK-2_opening+opus-one.mp4` | Opening + Hook 2 | Stay till the end for an amazing deal. Some of the grapes in this bottle come from the same corner of Napa as Opus One. | 0.00s | 8.98s | 9.0s |
| `03_HOOK-3_opening+1966.mp4` | Opening + Hook 3 | Stay till the end for an amazing deal. In 1966, one man built a winery in Oakville and changed American wine. | 0.35s | 8.56s | 8.2s |
| `04_GAP-1_prohibition-1920.mp4` | Gap | When Prohibition hit in 1920, most of Napa's wineries shut down. The few that survived did it by making altar wine for the church. | 0.33s | 9.17s | 8.8s |
| `05_GAP-2_mondavi-1966.mp4` | Gap | It took until 1966 for anyone to build a major new winery in the valley. That was Robert Mondavi, and he built it in Oakville. | 0.59s | 9.50s | 8.9s |
| `06_GAP-3_rothschild-opus-one.mp4` | Gap | Thirteen years later he teamed up with Baron Philippe de Rothschild, the owner of Chateau Mouton Rothschild, and together they made the world famous Opus One, in Oakville. | 0.33s | 9.57s | 9.2s |
| `07_STAKE-1_opus-screaming-eagle.mp4` | Stake | Today a bottle of Opus One costs well over four hundred dollars, and Screaming Eagle, a few minutes down the road, sells for thousands. | 0.30s | 8.21s | 7.9s |
| `08_STAKE-2_oakville-stags-leap.mp4` | Stake | Oakville is a small patch of valley floor. Together with Stags Leap District, it's where Napa grows the Cabernet everyone else gets compared to. | 0.33s | 9.12s | 8.8s |
| `09_STAKE-3+REVEAL-1_land-price+dolum.mp4` | Stake / Revelation | Vineyard land here can cost half a million dollars an acre. Dolum Estates was founded by Chad Alexander. | 0.00s | 7.00s | 7.0s |
| `10_REVEAL-2_mount-veeder.mp4` | Revelation | He grew up on Mount Veeder, in the mountains on Napa's western edge, and made wine at Hess Persson and Robert Craig, before starting his own label. | 0.26s | 9.21s | 8.9s |
| `11_REVEAL-3_buys-cabernet.mp4` | Revelation | He buys Cabernet from Oakville and Stags Leap District, choosing the best grapes around. | 0.43s | 5.68s | 5.2s |
| `12_REVEAL-4_french-oak.mp4` | Revelation | And then he ages it in imported charred French oak, which is where the hint of campfire and vanilla comes from. | 0.46s | 7.15s | 6.7s |
| `13_REVEAL-5_flint-blackcurrant.mp4` | Revelation | The soil gives a flinty, graphite edge at the front, mixed with this beautiful blackcurrant. | 0.29s | 6.00s | 5.7s |
| `14_REVEAL-6_finish.mp4` | Revelation | And with a wine of this heritage, the finish is long and slow, with sweet cedar interspersed by espresso and dark chocolate. | 0.34s | 7.52s | 7.2s |
| `15_PAYOFF_scores.mp4` | Payoff + proof | Decanter gave it 94 points, James Suckling gave it 93, and Casedrops members rate it four and a half out of five across hundreds of reviews. | 0.00s | 9.28s | 9.3s |
| `16_CTA-1_price.mp4` | CTA | And that's where you should buy it, because this wine should be $60 a bottle. On Casedrops, it's 6 for $100. | 0.44s | 9.38s | 8.9s |
| `17_CTA-2_buy-today.mp4` | CTA | That's effectively 4 free bottles with your purchase. Buy it today, because once it's gone, it's gone. | 0.00s | 6.32s | 6.3s |

Cut back to back with only the end holds trimmed, the read runs about 1:58 (hook 1), 2:02 (hook 2) and 2:01 (hook 3). Tightening pauses over ~0.5 s inside lines brings hook 1 to about 1:54. Re-timed sections for hook 1 with pauses tightened:

| Section | Brief | Measured |
|---|---|---|
| Opening + hook | 0–6s | 0:00.0–0:05.4 |
| Gap | 6–33s | 0:05.4–0:32.4 |
| Stake | 33–58s | 0:32.4–~0:52 (ends inside file 09) |
| Revelation | 58–88s | ~0:52–1:29.1 |
| Payoff + proof | 88–98s | 1:29.1–1:38.4 |
| CTA | 98–110s | 1:38.4–1:53.6 |

## B-roll

Kling 3.0 Pro. No real people are shown (Mondavi, Rothschild and Chad Alexander appear only as hands or a figure from behind), and no real labels, logos or signage. There was no Dolum product shot, so every bottle is unbranded or label-away; drop in a real pack shot where the script says "this bottle".

| File | Made for |
|---|---|
| `B201_golden-hour-napa-aerial.mp4` | open (all hooks) |
| `B202_1920s-barrels-smashed.mp4` | Hook 1: Prohibition |
| `B203_cabernet-pour.mp4` | Hook 2: grapes in this bottle / Payoff |
| `B204_1960s-mission-winery.mp4` | Gap-2: built it in Oakville |
| `B205_1920s-padlocked-winery-door.mp4` | Gap-1: wineries shut down |
| `B206_sepia-monk-church-cellar.mp4` | Gap-1: altar wine |
| `B207_1960s-winery-construction.mp4` | Gap-2: took until 1966 |
| `B208_1960s-man-walking-vines.mp4` | Hook 3: one man / Gap-2 |
| `B209_bordeaux-chateau.mp4` | Gap-3: Chateau Mouton Rothschild |
| `B210_handshake-over-barrel.mp4` | Gap-3: teamed up with |
| `B211_limestone-winery-blue-hour.mp4` | Gap-3: Opus One in Oakville / Hook 2 |
| `B212_auction-bottles-velvet.mp4` | Stake-1: Screaming Eagle, thousands |
| `B213_gloved-hands-prestige-bottle.mp4` | Stake-1: Opus One $400+ |
| `B214_oakville-aerial-mist.mp4` | Stake-2: Oakville valley floor / Reveal-3 |
| `B215_stags-leap-palisades.mp4` | Stake-2: Stags Leap District |
| `B216_cabernet-clusters-macro.mp4` | Stake-2: the Cabernet |
| `B217_vineyard-estate-sunset-drone.mp4` | Stake-3: land half a million an acre |
| `B218_wine-thief-barrel.mp4` | Reveal-1: Dolum Estates founded |
| `B219_mount-veeder-aerial-fog.mp4` | Reveal-2: Mount Veeder |
| `B220_hillside-vineyard-sunrise.mp4` | Reveal-2: western mountains |
| `B221_punch-down-fermenting.mp4` | Reveal-2: made wine at |
| `B222_sorting-table.mp4` | Reveal-3: best grapes |
| `B223_barrel-toasting-fire.mp4` | Reveal-4: charred French oak |
| `B224_vanilla-campfire.mp4` | Reveal-4: campfire and vanilla |
| `B225_flint-graphite-slate.mp4` | Reveal-5: flinty graphite |
| `B226_blackcurrant-splash.mp4` | Reveal-5: blackcurrant |
| `B227_cabernet-swirl.mp4` | Reveal-6: long slow finish |
| `B228_espresso-chocolate-cedar.mp4` | Reveal-6: cedar, espresso, dark chocolate |
| `B229_glass-and-bottle-candlelight.mp4` | Payoff: scores |
| `B230_six-bottle-wooden-case.mp4` | CTA: 6 bottles / buy today |
| `B231_doorstep-delivery-box.mp4` | CTA: on Casedrops (delivery) |
| `B232_friends-clinking-glasses.mp4` | CTA: 4 free bottles |

## Tooling

`plan/dolum/` has the script used for a test assembly: `fetch.py` downloads every clip listed in `sources.json` (all Higgsfield job IDs and URLs), and `edit.py` keys the presenter over the B-roll, cuts B-roll on cue words and adds score and price callouts. Optional; the clips above are the deliverable.
