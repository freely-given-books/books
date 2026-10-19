#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in Brooks's palette, sage. ./fgb build gives it
// the interior's page count and trim; `pages` is only for compiling the
// cover by itself.
#panel-cover(
  title: [Precious Remedies \ Against Satan’s Devices],
  subtitle: [Or, Salve for Believers’ and Unbelievers’ Sores],
  author: [Thomas Brooks],
  pages: 380,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "sage",
  epigraph: [
    "Put on the whole armour of God, that ye may be able to stand against
    the wiles of the devil."
  ],
  epigraph-source: [— Ephesians 6:11],
)
