#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Keach's midnight navy. The back carries a passage
// from the last part of the treatise.
//
// Page count comes from the compiled interior; after the text changes length,
// check `pdfinfo` on the built PDF (./fgb build prints it) and change `pages`.
#panel-cover(
  title: [The Gospel Minister’s Maintenance Vindicated],
  subtitle: [
    Wherein a Regular Ministry in the Churches Is First Asserted, \
    and the Objections Against a Gospel Maintenance for Ministers Answered
  ],
  author: [Benjamin Keach],
  pages: 86,
  paper: "cream-60",
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "midnight",
  spine-style: "ruled",
  epigraph: [
    If one soul be worth more than all the world, how great is the charge of
    Christ’s ministers, that have many souls committed to their care and trust?
  ],
  epigraph-source: [— The Great and Weighty Work of a True Gospel Minister],
)
