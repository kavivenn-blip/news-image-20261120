# news-image-20261120 — "Friday 20 November 2026" (v5, layout D)

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kavivenn-blip/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kavivenn-blip/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up Friday 20 November 2026's world news: **36 stories**
on a single 1024&times;1024 page, built for the
[make.fun bounty](https://make.fun/bounty/news-image-20261120).

This is the v5 revision, built from a layout drawn by the author himself
(layout D: three wide leads side by side across the top, eleven feature
cards in two rows, and a bottom row with the world map beside 22 briefs).
The typography is Gelasio 700 for headlines (56px masthead), Gelasio
Italic for the red subtitle, and Source Sans 3 for body text, labels and
lists; the illustrations are gradient vector scenes in a limited palette
of deep navy, cream, tan, brick red and gold, each carrying a short data
label. v5 keeps v4's 13 redrawn scenes, widens the three leads into
full-width cards with big red label blocks, and replaces Bukele's
third-term bid and Fiona the hippo (both first reported before Friday)
with two verified Friday stories: GTA VI first-day sales of $2.36bn (a
Sensor Tower estimate) and 111 Suneung exam cheats caught in South Korea.

## What is on the page

- A giant serif masthead — **Friday 20 November 2026** — with the four
  biggest Friday stories as its subtitle (Kyiv, Cyclone Akvan, the Asian
  AI sell-off, COP31).
- A numbers strip (300,000+ evacuated &middot; ~30 missiles at Kyiv
  &middot; &minus;7% Asia shares &middot; 2.3% Japan CPI &middot; 118
  Phillips &middot; $2.36bn GTA VI first-day sales, Sensor Tower est.)
  and a region bar (Europe 8 &middot; Americas 7 &middot; Asia-Pacific 11
  &middot; Mideast 3 &middot; Africa 2 &middot; Oceania 4 &middot;
  World/Space 1).
- **3 lead stories**, side by side across the top: Russian ballistic
  missiles hit Kyiv (~30 missiles, 3 killed, 15 hurt); Cyclone Akvan
  makes landfall in Odisha; the Asian AI sell-off (Nikkei &minus;4.9%,
  KOSPI &minus;5.7%, TAIEX &minus;6.8%).
- **11 feature stories**: COP31 reaching its final day deadlocked,
  BepiColombo reaching Mercury, the first EU&ndash;UK reset summit, Japan
  inflation at 2.3%, China holding lending rates for an 18th month,
  Phillips' 118 vs India, GTA VI making $2.36bn on day one (Sensor Tower
  estimate), a Russian Kh-101 cruise missile landing in a Polish field,
  Italy's CGIL general strike, a pancreatic cancer pill shrinking tumours
  60.7%, and 111 caught cheating at the Suneung exam.
- **22 briefs** (15&ndash;36), a **WHERE IT HAPPENED** dark-navy world map
  with numbered pins (Pins 1&ndash;14), a **DATE CHECK** strip, and a
  sources footer.

## Corrections from the sketch

Two figures in the author's sketch were corrected against live sources
before the build:

- **AI sell-off (lead 03):** the sketch read "Nikkei &minus;4.5%,
  KOSPI &minus;4.7%, SoftBank &minus;16%". The verified Friday figures
  (Reuters/TradingView) are Nikkei **&minus;4.90%** intraday to 56,517,
  KOSPI **&minus;5.7%**, TAIEX **&minus;6.8%**, SoftBank **&minus;15%**.
  The card now reads "Nikkei &minus;4.9%, KOSPI &minus;5.7%, TAIEX
  &minus;6.8%; SoftBank &minus;15%".
- **COP31 (feature 04):** the sketch used "$120BN FINANCE GAP" as the
  key fact. The $120bn adaptation-finance figure was **removed** from
  the COP31 closing draft, so presenting it as the finance gap would
  be misleading. The key fact is now "FINAL DAY &bull; DEADLOCK" and the
  body says adaptation finance "stays unresolved" with no nominal
  figure. "$120bn" appears nowhere on the page.

## Honesty about dates

All 36 stories on the page happened, or were first reported, on
**Friday 20 November 2026** in at least one time zone. Nine stories
first reported on **Thursday 19 November** (Bukele's third-term filing,
Fiona the hippo's death, the Trump&ndash;Xi&ndash;Putin Shenzhen summit,
Anthropic's $83 IPO pricing and Nasdaq debut, the ICJ Myanmar verdict,
the GTA VI midnight launch, the $190.4m Van Gogh sale, Voyager 1
crossing one light-day, and the Senate 48&ndash;51 Iran war-powers vote)
are listed in the DATE CHECK strip as "NOT shown as Friday's news" —
none of them appears as a story on the page. Two Friday stories need a
note: the GTA VI $2.36bn figure is a Sensor Tower estimate reported on
Friday (the midnight launch itself was Thursday, and is in the DATE
CHECK exclusions), and the 111 Suneung cheats were announced on Friday
by South Korea's education ministry (the exam itself was Thursday).
The Kh-101 missile landing in Poland was first reported on Friday 20
Nov (AP, Reuters): the missile fell near Nowy Lipowiec in the Lublin
region during the overnight Russian strike on Ukraine; Prime Minister
Donald Tusk called it a deliberate provocation. Nothing here invents a
result for an event that had not happened.

Every story was verified against two or more independent sources before
it was drawn.

## How the entry is produced

`render.html` is a static, self-contained page (locally embedded Gelasio
and Source Sans 3 fonts via `@font-face`, inline SVG illustrations, no
network, no JavaScript) that draws the whole image. At build time it is
screenshotted once with a headless browser into `entry.png`
(1024&times;1024, under 1 MiB). Three independent screenshot runs produced
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
