#import "../../../scripts/panel_cover.typ": *

// ./fgb build gives the
// cover the compiled interior's page count and trim, and the spine is Lulu's
// own formula (scripts/panel_cover.typ); `pages` here is only for compiling
// the cover by itself.  VERIFY against a downloaded live 5.5x8.5
// perfect-bound template before ordering.
//
//   ./fgb build gouge renders the front panel alone (the ebook cover, and a
//   picture for the web) as cover-vol-1-front.png.
#panel-cover(
  title: [Of Domestical Duties],
  volume: [Volume I],
  subtitle: [The First Treatise: An Exposition of That Part of Scripture Out of Which Domestical Duties Are Raised],
  author: [William Gouge],
  pages: 235,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "olive",
  // the set's front and spine, lettered after the 1622 title page: the whole
  // work's eight treatises, this volume's picked out
  front-style: "set",
  spine-style: "set",
  title-display: [
    #lettered([Of], 13pt, tracking: 0.5em)
    #v(-0.06in)
    #lettered([Domestical], 31pt, tracking: 0.03em)
    #v(-0.12in)
    #lettered([Duties], 19pt, tracking: 0.42em)
  ],
  kicker: [Eight Treatises],
  contents: (
    ([I.], [An Exposition of That Part of Scripture out of Which Domestical Duties Are Raised]),
    ([II.], [Of a Right Conjunction of Man and Wife, and Their Common-Mutual Duties]),
    ([III.], [Particular Duties of Wives]),
    ([IV.], [Particular Duties of Husbands]),
    ([V.], [Duties of Children]),
    ([VI.], [Duties of Parents]),
    ([VII.], [Duties of Servants]),
    ([VIII.], [Duties of Masters]),
  ),
  current: (0,),
  volume-number: [I],
  imprint: [London, 1622],
  spine-author: [Gouge],
  back-lead: [The first of Gouge's eight treatises: a verse-by-verse exposition of Ephesians 5:21-6:4, the passage the whole work is raised out of. Wives and husbands, children and parents, and above them the marriage of Christ and His church.],
  epigraph: ["Submitting your selves one to another in the fear of God."],
  epigraph-source: [— Ephesians 5:21],
  // Uncomment once the volume has an ISBN; this puts the white field the
  // printer drops the barcode into on the back cover.
  // isbn: "978-0-000000-00-0",
)
