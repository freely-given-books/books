// Cover for The Anatomy of Simon Magus: the full wrap for Lulu, or with
// `--input front-only=true` the front alone (the ebook cover).
//
// Not the house design: the wrap was made outside this repository (Inkscape,
// 2026-03) and is the one Lulu sells, kept as it is (the editor's choice,
// 2026-10-26). art/cover-wrap.pdf is that file with its picture recompressed
// (JPEG, 300 ppi kept; the lettering stays vector). It was drawn for the
// 124-page interior and its spine cannot move, so any other page count stops
// the build: the interior is held at 124 pages (the-anatomy-of-simon-magus.typ).
//
// ./fgb build passes the interior's page count and trim (--input pages=N
// trim-width=W trim-height=H). Compiled on its own: typst compile cover.typ cover.pdf

#let pages = int(sys.inputs.at("pages", default: "124"))
#let trim-width = float(sys.inputs.at("trim-width", default: "5.5")) * 1in
#let trim-height = float(sys.inputs.at("trim-height", default: "8.5")) * 1in
#let front-only = sys.inputs.at("front-only", default: "false") == "true"

#assert(pages == 124, message: "the Simon Magus wrap was made for 124 pages, not "
  + str(pages) + ": keep the interior at 124 or remake the cover")
#assert(trim-width == 5.5in and trim-height == 8.5in,
  message: "the Simon Magus wrap is for the 5.5x8.5in trim")

#let BLEED = 0.125in
// the wrap as drawn: 833 x 630pt, back + spine + front with 0.125in bleed
#let WRAP_W = 833pt
#let WRAP_H = 630pt
#let wrap = image("art/cover-wrap.pdf", width: WRAP_W, height: WRAP_H)

#if front-only {
  // the front panel at the trim: the wrap's right edge less the bleed
  set page(width: trim-width, height: trim-height, margin: 0pt)
  place(top + left, dx: -(WRAP_W - BLEED - trim-width), dy: -BLEED, wrap)
} else {
  set page(width: WRAP_W, height: WRAP_H, margin: 0pt)
  wrap
}
