---
name: cover-design
description: Design and build Common Weal Press book covers, the full Lulu wrap (back, spine, front) and the ebook front, in the plate design (scripts/plate_cover.typ), and the art that goes on them. Use this whenever the user wants a new cover, a cover redesign or mock-up, cover art or an image-generator (ChatGPT) prompt for a cover, to place, recolour, tint, upscale or check generated art, to choose what a book's cover should show, work on spines, back-cover text, the press's seal or device, the publisher's page or ebook front, or asks why a cover looks off. Also for thin spines, ISBN/barcode space, cover fonts, and previewing covers on the website before sign-off. For building a book's text or interior use eebo-tcp-book; for proofreading, book-review.
---

# Cover design

Covers are Typst, compiled by `./fgb build` with the interior's page count and
trim (`--input pages=N trim-width=W trim-height=H`), so a spine never goes
stale; `--input front-only=true` renders the front alone as the ebook cover.
The design every new cover uses is **`scripts/plate_cover.typ`**: an image (a
"plate") on the front, the house title block over it, the press's seal at the
foot, the spine and back in the plate's own colours. The older
`scripts/panel_cover.typ` (coloured panel on a pale ground) is what books not
yet redone still use; the 1689 Confession has its own engraved-frame cover.
A set of volumes lettered after its printed title page uses
**`scripts/set_cover.typ`** (Gouge's four): a double-ruled frame, the whole
work's contents with this volume's entries picked out, the volume in a
roundel, with the house's type, seal, name plate, spine and back; its
`spine-fit` sizes every spine to the thinnest volume's, so a set shelves
alike. `panel` fills inside the frame (Gouge: olive softly lit, a radial
gradient) with `ground` round it and on spine and back; the editor liked
the dark of the old covers kept this way. `front` gives a set a front of
its own over the house spine and back (Calvin). A set can step its ground
colour along a ramp, volume to volume, so it shelves as one band (Calvin).
Full-page plates are not the only answer: the editor found them "too
aggressive" for Calvin and preferred a small image on a plain ground.

Covers already done (read them as worked examples, `books/<author>/<book>/cover.typ`):

| book | art | kind |
|---|---|---|
| Pilgrim's Progress | Christian setting out toward the wicket-gate's light | ChatGPT engraving, hand-tinted, `art/plate.jpg` |
| All of Grace | the wayside fountain with a cup on a chain (ch. 1) | ChatGPT engraving, one ink, `art/plate.png` |
| Precious Remedies | the shield of faith, one fiery dart quenched in it | ChatGPT engraving, one ink, `art/plate.png` |
| Secret Key of Heaven | a key standing in an arched closet door | vector, `art/key.svg` + Typst arch |
| Glorious Feast | the cup in a wreath of vine | vector, `art/chalice.svg` |
| Sinners | the pit's glow, sparks, a spider small on its thread | vector + Typst (`art/spider.svg`) |
| Crook in the Lot | the Ettrick hills at dawn, a shepherd's crook in the near hill | ChatGPT engraving, hand-tinted, `art/plate.jpg` (`art/tint.py`) |
| Grace Abounding | Bunyan's vision (§53-55): poor women of Bedford in the sun on a mountainside, a snowy wall with one narrow gap ("Jesus Christ, who is the way") | ChatGPT engraving; colour painted by ChatGPT on a copy and transferred under the approved lines (`art/transfer.py`), `art/plate.jpg` |
| Christian Economy | a timber-framed house of 1609, the title page's "an house built" (Prov. 24:3) | ChatGPT engraving, one ink (deep mulberry) on pale rose, `art/plate.png` |
| Mortification of Sin | no picture: Romans 8:13, the verse the book expounds, "mortify" and "ye shall live" in gold | type only, oxblood and gold (Typst `art`) |
| Of Domestical Duties (4 vols) | no picture: lettered after the 1622 title page, the eight treatises with this volume's picked out | type only, olive and gold, `scripts/set_cover.typ` |
| Institutes (6 vols) | a small vignette, not a plate: spectacles on an open book (I.vi.1), pages filled in paper colour | ChatGPT engraving, `art/vignette.png` (`art/vignette.py`); grounds step sea-green to indigo across the set |

## What the editor wants (learned the hard way)

The catalogue will run to hundreds of books, so covers must be **recognizable
as one press yet each its own**. The house is the type, the title block, the
seal and name plate, and the plate treatment; everything else is the book's.

1. **One strong image per book, from the book itself.** Before proposing
   anything, search the edition's text (`chapters/typ`) for the author's own
   images: Spurgeon opens with a wayside fountain, Brooks's remedy is "the
   shield of faith ... to quench all the fiery darts", Bunyan's Evangelist
   says "Keep that light in your eye", Edwards has the spider over the fire.
   Quote what you find, then design from it. A generic symbol (a dove, a
   cross, light through clouds) fits any book and so says nothing; the
   author's figure that points to the gospel is better than trying to picture
   "the gospel".
   Not every cover needs a picture (the editor, 2026-10-23): where a
   book's own words carry it, type alone can be the image. For Owen, four
   were offered (fading strokes, a year of tally marks, the 1668 title
   page, Romans 8:13 set large); the verse was chosen.
2. **Calm, single-subject images.** "Too much happening" was the commonest
   complaint: one dart beat a volley, the shield alone beat the armour
   trophy, the fountain alone beat the symbol-laden frame.
3. **No all-over repeats** except where they truly belong: patterns read as
   "gift wrap". No giant title words ("distracting"). No all-cream sameness.
4. **Rich scenes are engravings, not Claude's vector drawing.** Claude's
   drawn map of the pilgrim's way looked like "a pirate treasure map", and a
   foreshortened arrow aimed at the viewer failed three times. Draw in
   vector only simple emblems (a key, a cup in a wreath, a spider). For
   anything with a landscape, figures or depth, write an image-generator
   prompt (references/prompts.md) and let the editor generate it.
5. **Colour suits the book** (the editor, 2026-10-23: "some deserve this
   soft color, some vibrant colors"). Choose per book among: one ink in the
   book's colour (Precious Remedies, All of Grace); a soft hand-tint, pale
   washes under the line (Pilgrim, Crook in the Lot); or vibrant colour,
   fuller and more saturated, for a book whose image is bold (a fire, a
   feast). Say which you chose and why; a wish for "more color" means tint.
6. **Spine:** the surname has a fixed place under the head rules on every
   book, so a shelf reads as a row of names (no per-author emblem). Thin
   spines still carry name, title and seal.
7. **Back:** the author's own words from the edition, quoted exactly and
   checked against `chapters/typ` (grep it), with where they come from; or
   the Scripture the book's back already had. Say which lines you chose; it
   is the editor's call. A book's existing back words may be kept on purpose
   (the 1689).
8. Show work as images (`SendUserFile`), compare options side by side, and
   say plainly what is weak in your own work.

## Workflow for a new cover

1. **Find the image**: read and grep the book for its figures; propose one or
   two with the quoted lines.
2. **Get the art**
   - *Engraving*: write a prompt from references/prompts.md (black ink on
     white, top third empty for the title, bottom sixth quiet for the seal,
     no text). The editor generates it (ChatGPT, 2:3 portrait, largest size)
     and drops it in Nextcloud `claude/fgbooks-generated-art/`, where every
     generated image is kept, used or rejected. Uploads from a phone arrive
     with a UUID name (`16A141D9-....PNG`): the newest file is the one meant;
     rename it for the book and what changed ("Crook In The Lot (crook
     revised).PNG") and note it in that folder's README.
   - A design the editor liked before is a good start: an earlier vector
     mock-up (the Crook's hills and crook, `art.py`) can be redrawn as an
     engraving prompt, enriched with more of the book's own images.
   - *Vector emblem*: draw it as SVG (common-weal-press/sources/vector-art/
     `art.py` has the key, chalice, spider, hills as examples).
3. **Check generated art for AI faults** before using it: crop and zoom on
   hands, faces, chains, mechanisms, text, symmetry. Seen so far: mismatched
   paired pillars, arrows stuck in backwards, smoke rising from the wrong end,
   fletching at both ends, a burden drawn as a modern backpack, a second
   figure nobody asked for, a shepherd's crook drawn as a jointed walking
   cane. Fixes go back to ChatGPT's edit tool: the editor selects only the
   faulty object, the prompt redraws it and ends "Change nothing else."
   Write that edit prompt when you report the fault. An edit can still
   redraw other small things: compare the two images (`magick compare
   -metric AE -fuzz 10%` over regions) and zoom on the rest (the sheep).
4. **Make the plate** (scripts below): upscale 2x, turn the white into
   transparency in the book's ink, or tint it (rule 5); keep a book's tint
   script beside its plate (`art/tint.py`).
5. **Write `cover.typ`** on `plate_cover.typ` (copy the nearest example) and
   check it alone, then with `./fgb build BOOK`; look at the wrap and the
   front at full size, the spine crop, and a 300 ppi crop of the art.
6. If the book had no `cover.typ` (its ebook cover was an image), point
   `EPUB["cover"]` in `source/editorial.py` at `cover.typ`.
7. Record the prompt (and any edit) in references/prompts.md and the book in
   the table above.
8. Commit on a branch; the editor signs books off, never Claude. Any change
   to a book's folder holds its signed release back.

## Making plates (scripts)

Upscale a 1024x1536 generated image to print (plain resampling; potrace
ruins these "engravings", which are really greyscale):

```sh
magick IN.png -colorspace gray -filter Lanczos -resize 200% -unsharp 0x1.2+0.6+0.02 plate-2x.png
```

One-ink plate (white becomes transparent, lines in the book's ink):

```sh
magick plate-2x.png -negate -level 4%,88% mask.png
magick -size 2048x3072 xc:'#173A57' mask.png -alpha off -compose CopyOpacity -composite art/plate.png
```

Smoke or anything that must fade under the title: multiply the mask by a
vertical gradient before compositing (Precious Remedies). Hand-tinting:
`scripts/tint_example.py` (Pilgrim's; Crook's is the book's `art/tint.py`):
washes under the line, each clipped to where the engraver drew densely so
colour stays inside the figure, the line multiplied over. Its masks are
Pilgrim's coordinates; copy and redraw them. For vibrant colour raise the
wash strengths and saturation, keep the line ink dark. Match `ground` to the
plate's colours down its edge (sample them), and where the plate stops short
of the foot, fade its last rows into one flat colour and give that as
`front-ground`, or a seam shows.
Save a tinted plate as JPEG quality 93, 4:4:4; a one-ink plate as PNG.

**Colour by transfer** (Grace Abounding): where Claude's washes stay flat (a
mountain the engraver left nearly blank), ask ChatGPT to hand-colour the
approved engraving, then keep only its colour: `art/transfer.py` aligns the
coloured copy (phase correlation), closes its lines over (max filter),
softens it into a wash and multiplies the approved engraving's own lines
over it. ChatGPT's colouring redraws details (it broke the fingers again);
the transfer keeps every approved line, face and hand. Prompt in
references/prompts.md.

At 2048x3072 a full-bleed plate prints at about 350 dpi; aim for 300+.

## plate_cover.typ, the parts

`plate-cover(...)`: `plate` (bytes) and `plate-at` (dx, dy, width, height
from the front's trim corner; it may run into the bleed and is cut at the
fold) or `art` (Typst content, same origin); `ground` (gradient stops head to
foot, or any fill: matched to the plate's edge, it is the spine and back);
`front-ground`; `title`, `tail` (second line, 0.66 size), `subtitle`,
`author`, `title-size`, `title-y`, `title-align` (`left` for Sinners),
`title-width`; `spine-title`, `spine-author` (surname); colours `ink` (title),
`accent` (author, rules, back press name), `label` and `paper` (the seal's
roundel and fountain, and the front name plate); `epigraph`,
`epigraph-source`; `isbn` (puts the 2in x 1.2in barcode field).

Spine rules: wide spines (safe strip over 0.2in) carry the surname across
(7-10.5pt), the title down, the seal at the foot; thin spines (0.25in and
up, about 80-170 pages) carry name, title and seal on one line, 1/16in off
each fold; under 0.25in (Sinners, 40 pages) nothing.

## Print rules

- Wrap = bleed + trim + spine + trim + bleed by bleed + trim + bleed; bleed
  0.125in; trim 5.5x8.5in unless the book sets otherwise.
- Spine = Lulu's `pages / 444 + 0.06in`; type inside 0.125in of each fold on
  normal spines.
- Type 0.5in inside the trim; the plate's busy parts out of the title's band.
- Never give the spine a colour of its own; it shares the back's ground.
- Images 300 dpi at printed size; vector stays vector in the PDF.
- Fonts: Cinzel (titles) over EB Garamond, in `fonts/` (OFL); `./fgb` sets
  `TYPST_FONT_PATHS`, so compile covers through `./fgb`, or set it yourself.

## The press: seal, device, publisher's page

In the template (`typst/fgbooks-typst/press/`, fgbooks 0.13.1, masters and
sources in `common-weal-press/`): `press-seal(width:, roundel:, fountain:)`,
`press-seal-knockout`, `press-seal-positive`, `press-device`, and
`publisher-page(note:, isbn:)` for `book(publishing-info: ...)`, with the
book's own lines (where its text comes from, volume notes) as `note`. No
"formatted by" line. The ebook front repeats it (`<div class="imprint">`,
styles in `books/resources/css/ebook.css`, `art/device-ebook.png` copied into
the book: the EPUB builder only takes images inside the book's folder).
Marks must be woodcut weight, black and white, no lettering in the image
(set words in type): fine hatching fills in at a quarter inch.

## Previewing

`dist/<author>/<book>/` after `./fgb build`. For the editor to inspect, build
into Nextcloud: `./fgb build [BOOK] --out ~/Nextcloud/claude/fgbooks/build-<date>`.

On the website, unsigned covers show only in the preview build: the site
reads `books/dist/`, so first `./fgb build` the books on main (all of them,
or the ones changed), then in `commonwealpress/` run `npm run build:unsigned`
and restart the preview server (`npx astro preview stop`, then
`npx astro preview --host 0.0.0.0 --port 4321`, LAN demo). A released book
changed since sign-off shows its main build marked Preview; a book never
released shows as available from main. `npm run build` is production and
takes signed releases only. Covers keep their file names, so tell the editor
to force-refresh if the old cover still shows.

## Covers with their own design

A book may keep a design of its own (the 1689's engraved frame), but the
press's marks sit where `plate_cover.typ` puts them, so a shelf lines up: on
the front the seal 0.74in wide with its top at trim height - 0.5in - 1.18in
and the name under it; on the back the seal 0.46in on the safety line, at
the foot; on the spine the seal 0.62in up from the foot, inside 1/8in of
each fold. Check by overlaying the wrap on a plate cover's (50% blend).
