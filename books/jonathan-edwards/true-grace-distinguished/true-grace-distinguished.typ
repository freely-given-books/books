#import "@local/fgbooks:0.15.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [True Grace, Distinguished from the Experience of Devils],
  author: "Jonathan Edwards",
  // the Common Weal Press publisher's page, from the template, sized to this
  // small trim's text area (6.875in less 1.5in of margins)
  publishing-info: publisher-page(height: 5.35in),
  preface: [
    #align(center)[
      #text()[
        A sermon preached before

        the Synod of New York,

        convened at Newark,

        in New Jersey,

        September 28, 1752

        #v(0.6em)
        #text(size: 0.9em, style: "italic")[Printed by the desire of the Synod]
      ]
    ]

    #align(center + horizon)[
      #text(size: 11pt)[_I fear, lest by any means, as the serpent beguiled Eve through his subtlety, so your minds should be corrupted from the simplicity that is in Christ._

      — 2 Corinthians 11:3

      #v(0.8em)
      _For Satan himself is transformed into an angel of light._

      — 2 Corinthians 11:14]
    ]
  ],
  // the trim of Sinners: Edwards's sermons as small books
  page-height: 6.875in,
  page-width: 4.25in,
  page-margin: (top: 0.9in, bottom: 0.6in, outside: 0.6in, inside: 0.625in),   // Lulu: 61-150 pages
  show-outline: false
)

// the outline: every level full width, each numbered point marked by its level
#show: outline-marks

#metadata[True Grace] <short>
#include "chapters/typ/sermon.typ"
