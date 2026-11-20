# news-image-20261120 — "Friday 20 November 2026" (v4, layout D)

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kavivenn-blip/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kavivenn-blip/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up Friday 20 November 2026's world news: **36 stories**
on a single 1024&times;1024 page, built for the
[make.fun bounty](https://make.fun/bounty/news-image-20261120).

This is the v4 revision, built from a layout drawn by the author himself
(layout D: three leads stacked on the left, the world map top-right, ten
feature cards in two rows, 23 briefs below). The typography is Gelasio 700
for headlines (56px masthead), Gelasio Italic for the red subtitle, and
Source Sans 3 for body text, labels and lists; the illustrations are
gradient vector scenes in a limited palette of deep navy, cream, tan, brick
red and gold, each carrying a short data label. v4 redraws all 13 scenes
with richer gradients and data labels, and replaces the Yenne boat story
(Wednesday 18 Nov) with a verified Friday story: a Russian Kh-101 cruise
missile landing in a Polish field.

## What is on the page

- A giant serif masthead — **Friday 20 November 2026** — with the four
  biggest Friday stories as its subtitle (Cyclone Akvan, Kyiv, COP31, the
  Asian AI sell-off).
- A numbers strip (300,000+ evacuated &middot; ~30 missiles at Kyiv
  &middot; &minus;7% Asia shares &middot; 2.3% Japan CPI &middot; 118
  Phillips &middot; 8 years for BepiColombo) and a region bar (Europe 8
  &middot; Americas 8 &middot; Asia-Pacific 10 &middot; Mideast 3
  &middot; Africa 2 &middot; Oceania 4 &middot; World/Space 1).
- **3 lead stories**: Cyclone Akvan makes landfall in Odisha; Russian
  ballistic missiles hit Kyiv (~30 missiles, 3 killed, 15 hurt); COP31
  reaches its final day deadlocked.
- **10 feature stories**: the Asian AI sell-off (Nikkei &minus;4.9%,
  KOSPI &minus;5.7%, TAIEX &minus;6.8%), BepiColombo reaching Mercury,
  the first EU&ndash;UK reset summit, Japan inflation at 2.3%, China
  holding lending rates for an 18th month, Phillips' 118 vs India,
  Bukele's third-term bid, a Russian Kh-101 cruise missile landing in a
  Polish field, Italy's CGIL general strike, and a pancreatic cancer pill
  shrinking tumours 60.7%.
- **23 briefs** (14&ndash;36), a **WHERE IT HAPPENED** dark-navy world map
  with numbered pins (Pins 1&ndash;13), a **DATE CHECK** strip, and a
  sources footer.

## Corrections from the sketch

Two figures in the author's sketch were corrected against live sources
before the build:

- **AI sell-off (feature 04):** the sketch read "Nikkei &minus;4.5%,
  KOSPI &minus;4.7%, SoftBank &minus;16%". The verified Friday figures
  (Reuters/TradingView) are Nikkei **&minus;4.90%** intraday to 56,517,
  KOSPI **&minus;5.7%**, TAIEX **&minus;6.8%**, SoftBank **&minus;15%**.
  The card now reads "Nikkei &minus;4.9%, KOSPI &minus;5.7%, TAIEX
  &minus;6.8%; SoftBank &minus;15%".
- **COP31 (lead 03):** the sketch used "$120BN FINANCE GAP" as the
  key fact. The $120bn adaptation-finance figure was **removed** from
  the COP31 closing draft, so presenting it as the finance gap would
  be misleading. The key fact is now "FINAL DAY &bull; DEADLOCK" and the
  body says adaptation finance "stays unresolved" with no nominal
  figure. "$120bn" appears nowhere on the page.

## Honesty about dates

34 stories on the page happened, or were first reported, on
**Friday 20 November 2026** in at least one time zone. Seven stories
that were first reported on **Thursday 19 November** (the
Trump&ndash;Xi&ndash;Putin Shenzhen summit, Anthropic's $83 IPO pricing
and Nasdaq debut, the ICJ Myanmar verdict, the GTA VI midnight launch,
the $190.4m Van Gogh sale, Voyager 1 crossing one light-day, and the
Senate 48&ndash;51 Iran war-powers vote) are listed in the DATE CHECK
strip as "NOT shown as Friday's news". Two more stories are shown
on the page but were first reported earlier, and are flagged in the
DATE CHECK: Bukele's third-term filing (Thu 19 Nov) and Fiona the
hippo's death (Thu 19 Nov). The Kh-101 missile landing in Poland was
first reported on Friday 20 Nov (AP, Reuters): the missile fell near
Nowy Lipowiec in the Lublin region during the overnight Russian strike
on Ukraine; Prime Minister Donald Tusk called it a deliberate
provocation. Nothing here invents a result for an event that had not
happened.

Every story was verified against two or more independent sources before
it was drawn.

## How the entry is produced

`render.html` is a static, self-contained page (locally embedded Gelasio
and Source Sans 3 fonts via `@font-face`, inline SVG illustrations, no
network, no JavaScript) that draws the whole image. At build time it is
screenshotted once with a headless browser into `entry.png`
(1024&times;1024, under 1 MiB). Two independent screenshot runs produced
byte-identical files.

`main.py` (Python 3.13, standard library only) copies `entry.png` into the
harness output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`).

## Files

| File | Purpose |
| --- | --- |
| `entry.png` | The entry image, 1024&times;1024 |
| `render.html` | The page the image is screenshotted from |
| `fonts/` | Gelasio + Source Sans 3 woff2 files (local, deterministic) |
| `main.py` | Runner: copies `entry.png` to the output directory |
| `LICENSE` | MIT |
