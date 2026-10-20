---
name: cover-design
description: Design and build Freely Given Books paperback covers and ebook fronts — the full wrap (back, spine, front) to Lulu's rules, in Typst — and the art that goes on them. Use this whenever the user wants a new cover, a cover redesign or mock-up, wants to match an AI-generated or sketched cover mock-up, works on spine layout, author emblems, front engravings, corner ornaments, frames, cover fonts, the imprint mark, back-cover text, ISBN/barcode fields, or asks to cut art out of an image, prepare images for print, check cover image resolution, or export a cover as PDF/PNG/JPG. Also for the "engraved" cover system (remedies-cover-experiment/, WIP) and the existing panel_cover.typ covers, and for page counts and spine widths on covers. For building a whole book (interior, EPUB), use eebo-tcp-book; for the text, book-review.
---

# Cover design

Covers are Typst files compiled to a full-wrap PDF for Lulu (back, spine and
front in one sheet, with bleed) and, with `--input front-only=true`, to the
ebook's front image. Two designs exist:

- **`scripts/panel_cover.typ`** — what every printed book uses today: a
  coloured panel on a pale ground, one palette per author (`PALETTES`).
  Each book's `cover.typ` calls `panel-cover(...)`; `./fgb build` compiles
  it with the interior's page count and trim and renders the ebook front.
- **The engraved design** — WIP, `remedies-cover-experiment/` (branch
  `wip/engraved-cover`): a cream paper wrap, double gold frame with
  fleur-de-lis corners, Cinzel capitals over EB Garamond, an engraving on the
  front, an author emblem and the book's art on the spine. Mocked up on
  *Precious Remedies* (2026-10-19). Its state and next steps are in
  `remedies-cover-experiment/README.md`; read that first.

## Print rules (both designs)

- Wrap: `bleed + trim + spine + trim + bleed` by `bleed + trim + bleed`;
  bleed 0.125in; type at least 0.5in inside the trim (SAFETY).
- Spine: Lulu's formula, `pages / 444 + 0.06in`, never caliper × pages.
- `./fgb build` passes `--input pages=N trim-width=W trim-height=H` from the
  compiled interior, so a built cover is never stale. The `pages:` in a cover
  file is only for compiling it alone; keep it equal to the built count (the
  book-review checklist checks it; 15 had gone stale by 2026-10-19).
- A barcode needs a white field (2in × 1.2in) on the back only once the book
  has an ISBN; before that the space is kept clear.
- Never give the spine its own ground colour: a fold that drifts shows it as
  a stripe on the front. Frames sit 0.3in inside the trim, outside SAFETY.
- Images: 300 dpi at printed size at least. Check it: pixels ÷ inches
  printed. Vector (SVG) art stays vector in Typst's PDF — prefer it for
  ornaments, marks and emblems.

## The engraved system (the design rule)

A catalogue of hundreds of books must read as one house and still be
tellable apart, so roughly three parts fixed to one part variable:

| fixed, every book | per author | per book |
|---|---|---|
| paper ground, double gold frame + corner ornaments, Cinzel/EB Garamond, diamond rules, spine layout, imprint mark + name at the foot of front, spine and back | **emblem** at the spine's head under the surname (same on every book by that author); a restrained **accent** colour for the title | title, front engraving, **spine art** under the title (pinned at one height so shelves line up), back passages, volume number |

Emblem first, accent second; never a ground colour per author. Decided with
the user on the Precious Remedies mock-up:

- Spine, top to bottom: surname; author emblem (0.3in, larger than a
  diamond); title rotated (bold Cinzel, accent colour); the book's art,
  small (1.05in) and **pinned** (`SPINE_ART_FOOT`, foot 1.75in above the
  trim); the rest of the title stacked under the art with open leading; the
  imprint mark; gold double rules across head and foot.
- Spines under ~0.5in (~200 pages) drop the across-spine type and art: title
  and author rotated, and the mark.
- Corners: the inner rule bends in and ends as a scroll at each corner, a
  fleur-de-lis pointing into the corner (`art/corner.svg`, top-left,
  mirrored for the rest). The ornament *joins* the inner rule; a separate
  ornament set inside a square frame did not look right.
- Back: a heading, a passage from the book with a 3-line drop cap
  (`@preview/droplet:0.3.1`), a short italic quotation with its source, a
  few lines about the book, the imprint at the foot left, the barcode field
  right.

## Back-cover and cover text

Use the author's own words from the edition (`chapters/typ`), quoted
exactly, and say where they come from. AI mock-ups invent plausible
"quotations" (the Precious Remedies mock-up's "The great end of my writing
is…" and "turn again to the Lord" are not in the book): never carry those
over. Any description of the book written for the cover is the editor's to
approve — say which lines are yours.

## Art

**Getting art made.** Ask the image generator for *black ink line
engraving on a plain white background, no glow, no vignette, no shading
behind the subject*, one subject per image, square or the subject's own
shape, the largest size it offers. Engraving style suits these books
(woodcut/steel-engraving vignettes). Art lit against black, or with a glow
behind it, can be cut out but loses a little (see below).

**Cutting art out: `remedies-cover-experiment/extract.py`.**

```sh
uv run --no-project --with numpy --with pillow --with scipy \
  python -I extract.py SOURCE.png OUT.png x0 y0 x1 y1 [#2B2118]
```

It crops the box, finds the engraved (textured) region, and writes the
lines as ink (default `HOUSE.ink`, #2B2118) on a transparent ground,
trimmed to the art. Tone is measured against each pixel's *surroundings*
(a grey closing, smoothed), not against white: a smooth glow behind the
subject becomes paper and only the cut lines become ink. Measuring against
white turned the Precious Remedies glow into a grey cloud behind the bush.
Look at the result flattened on the ground colour
(`magick out.png -background "#EEE5D0" -flatten check.png`) and at 300 dpi
before using it.

**Ornaments, emblems, the imprint mark**: SVG, single colour (gold
#A9843F or ink), drawn in a 100-unit viewBox; place with
`image(read("x.svg", encoding: none), format: "svg", width: ...)`.

## Fonts

Cinzel (Regular, Bold) and EB Garamond (Regular, Italic, Medium), OFL, in
`remedies-cover-experiment/fonts/` — static instances only: **Typst 0.15
ignores variable fonts** (`Cinzel[wght].ttf` from google/fonts did not
load). Sources: github.com/NDISCOVER/Cinzel `fonts/ttf/`,
github.com/octaviopardo/EBGaramond12 `fonts/ttf/`. Typst needs
`--font-path` with an **absolute** path (a relative `.` was not picked up
by `typst fonts`); `./fgb` does not pass one yet.

## Building and checking

```sh
cd remedies-cover-experiment
typst compile --root .. --font-path "$PWD/fonts" cover.typ cover.pdf
typst compile --root .. --font-path "$PWD/fonts" --input front-only=true cover.typ front.png --ppi 150
typst compile --root .. --font-path "$PWD/fonts" cover.typ cover.png --ppi 300   # full wrap image
magick cover.png -quality 92 cover.jpg
```

Look at every render: the whole wrap at ~110 ppi, then crops at 300 ppi of
the spine, a corner and the engraving (`magick in.png -crop WxH+X+Y +repage
out.png`). Check that nothing overflows its box (a `v(1fr)` cannot go
negative — content just runs past the safety line), and the spine for the
page count actually built. For panel_cover books use `./fgb build BOOK`;
`./fgb pdf BOOK` gives the interior page count.
