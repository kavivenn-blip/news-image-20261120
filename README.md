# news-image-20261120 — "Friday 20 November 2026"

One image that sums up Friday 20 November 2026's world news: **36 stories**
on a single 1024&times;1024 page, built for the
[make.fun bounty](https://make.fun/bounty/news-image-20261120).

## What is on the page

- A giant serif masthead — **Friday 20 November 2026** — with the three
  biggest Friday stories as its subtitle.
- A region bar (Europe 6 &middot; The Americas 12 &middot; Asia-Pacific 10
  &middot; Mideast 4 &middot; Africa 2 &middot; Oceania 1 &middot; World 1)
  and a numbers strip (300,000+ evacuated as Cyclone Akvan hit &middot;
  9&ndash;6 ICJ verdict &middot; $1.84bn GTA VI sales estimate &middot;
  $81.3bn Anthropic valuation &middot; &minus;1,101 Dow points &middot;
  36 stories).
- **3 lead stories**: Cyclone Akvan makes landfall in Odisha; Trump puts
  the Iran call off to 2027; the ICJ finds Myanmar guilty of genocide
  (9&ndash;6, a first in 80 years).
- **10 feature stories**: the Shenzhen trilateral (Xi&ndash;Trump&ndash;Putin),
  Berlin ready for Russia talks, COP31's final day, the PIF Tower strike in
  Riyadh, the third Kerch Bridge attack, Voyager 1 crossing one light-day,
  GTA VI sales passing $1.84bn, Anthropic's $83 IPO debut, Han's 15-year
  term quashed, and Thursday's market fall.
- **23 briefs** (14&ndash;36), a **WHERE IT HAPPENED** world map with numbered
  pins, a **THE DAY IN UTC** timeline, a **DATE CHECK** strip, and a
  **LATER TODAY** strip.
- A sources footer naming the outlets each story was verified against.

## Honesty about dates

Several of the biggest stories of the day actually happened on **Thursday
19 November** (the ICJ verdict, the Shenzhen trilateral, Voyager 1, the PIF
Tower strike, the Anthropic debut, the Han retrial, the GTA VI launch).
They are shown with a Friday angle and flagged in the DATE CHECK strip
instead of being mis-dated as Friday. Events that had not happened yet when
the image was made (Trump's Friday press conference, F1 qualifying, the
COP31 final text) are listed under LATER TODAY with "results not yet known"
— nothing here invents a result for an event that had not happened.

Every story was verified against two or more independent sources before it
was drawn; figures marked "(est.)" are estimates.

## How the entry is produced

`render.html` is a static, self-contained page (system fonts only, no
network, no JavaScript) that draws the whole image as inline SVG
illustrations plus text. At build time it is screenshotted once with a
headless browser into `entry.png` (1024&times;1024, under 1 MiB).
Two independent screenshot runs produced byte-identical files.

`main.py` (Python 3.13, standard library only) copies `entry.png` into the
harness output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`).

## Files

| File | Purpose |
| --- | --- |
| `entry.png` | The entry image, 1024&times;1024 |
| `render.html` | The page the image is screenshotted from |
| `main.py` | Runner: copies `entry.png` to the output directory |
| `LICENSE` | MIT |
