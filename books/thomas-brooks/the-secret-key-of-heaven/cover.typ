#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), which was first drawn for this book: its sage.
// ./fgb build gives it the interior's page count and trim; `pages` is only
// for compiling the cover by itself.
#panel-cover(
  title: [The Secret Key \ of Heaven],
  subtitle: [Or, Twenty Arguments for Closet Prayer],
  author: [Thomas Brooks],
  pages: 290,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "sage",
  epigraph: [
    "But when you pray, go into your closet, shut your door, and pray to your
    Father, who is unseen. And your Father, who sees what is done in secret,
    will reward you."
  ],
  epigraph-source: [— Matthew 6:6],
)
