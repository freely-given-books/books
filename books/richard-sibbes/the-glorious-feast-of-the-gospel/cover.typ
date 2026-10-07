#import "../../../scripts/panel_cover.typ": *

// Full-wrap paperback cover, in the imprint's single-volume design (see
// scripts/panel_cover.typ), in this book's sky blue. ./fgb build gives it the
// interior's page count and trim; `pages` is only for compiling the cover by
// itself.
#panel-cover(
  title: [The Glorious Feast \ of the Gospel],
  subtitle: [The Marriage Feast Between \ Christ and His Church],
  author: [Richard Sibbes],
  pages: 196,
  trim-width: 5.5in,
  trim-height: 8.5in,
  palette: "sky",
  back-lead: [
    #align(center, emph[
      Christ's gracious Invitation and royal Entertainment of Believers.
      Wherein amongst other things these comfortable doctrines are handled:
    ])
    #v(0.8em)
    #set text(size: 10pt)
    #align(left)[
      + The Marriage Feast between Christ and the Church.
      + The veil of Ignorance and Unbelief removed.
      + Christ's Conquest over death.
      + The wiping away of tears from the faces of God's people.
      + The taking away of their Reproaches.
      + The precious Promises of God, and their certain performance.
      + The Divine Authority of the Holy Scriptures.
      + The Duty and comfort of waiting upon God.
    ]
  ],
  epigraph: [
    Wisdom has built her house; she has carved out her seven pillars. She has
    prepared her meat and mixed her wine; she has also set her table. She has
    sent out her maidservants; she calls out from the heights of the city.
    "Whoever is simple, let him turn in here!" she says to him who lacks
    judgment. "Come, eat my bread and drink the wine I have mixed."
  ],
  epigraph-source: [— Proverbs 9:1–5],
)
