#import "@local/fgbooks:0.15.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [A Divine and Supernatural Light],
  author: "Jonathan Edwards",
  // the Common Weal Press publisher's page, from the template, sized to this
  // small trim's text area (6.875in less 1.5in of margins)
  publishing-info: publisher-page(height: 5.35in),
  preface: [
    #align(center)[
      #text()[
        Immediately imparted to the soul by the Spirit of God,
        shown to be both a scriptural and rational doctrine

        #v(0.6em)
        A sermon preached at Northampton, 1734
      ]
    ]

    #align(center + horizon)[
      // from the 1734 title page
      #text(size: 12pt)[_Until the day dawn and the day-star arise in your hearts._

      — 2 Peter 1:19]
    ]
  ],
  // the trim of Sinners and God Glorified: Edwards's sermons as small books
  page-height: 6.875in,
  page-width: 4.25in,
  page-margin: (top: 0.9in, bottom: 0.6in, outside: 0.6in, inside: 0.5in),   // Lulu: under 60 pages
  show-outline: false
)

// the outline: every level full width, each numbered point marked by its level
#show: outline-marks

#include "chapters/typ/preface.typ"
#include "chapters/typ/sermon.typ"
