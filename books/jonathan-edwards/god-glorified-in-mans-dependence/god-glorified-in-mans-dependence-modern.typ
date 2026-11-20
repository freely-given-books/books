// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as god-glorified-in-mans-dependence.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.15.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [God Glorified in Man's Dependence],
  subtitle: [#text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Jonathan Edwards",
  // the Common Weal Press publisher's page, from the template, sized to this
  // small trim's text area (6.875in less 1.5in of margins)
  publishing-info: publisher-page(height: 5.35in),
  preface: [
    #align(center)[
      #text()[
        A sermon preached on the public lecture

        in Boston, July 8, 1731
      ]
    ]

    #align(center + horizon)[
      #text(size: 12pt)[_Lest Israel glorify themselves over Me, saying, ‘My own hand has saved me.’_

      — Judges 7:2]

      #v(2em)
      #text(size: 8pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]
    ]
  ],
  // the trim of Sinners: Edwards's sermons as small books
  page-height: 6.875in,
  page-width: 4.25in,
  page-margin: (top: 0.9in, bottom: 0.6in, outside: 0.6in, inside: 0.5in),   // Lulu: under 60 pages
  show-outline: false
)

// the outline: every level full width, each numbered point marked by its level
#show: outline-marks

// set a little looser, so the preface carries enough lines onto its last page (not two or three alone)
#[
  #set text(tracking: 0.015em)
  #include "chapters/modern/to-the-reader.typ"
]
#include "chapters/modern/sermon.typ"
