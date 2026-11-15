// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as sinners-in-the-hands-of-an-angry-god.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [Sinners in the Hands of an Angry God],
  subtitle: [#text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Jonathan Edwards",
  // the Common Weal Press publisher's page, from the template, sized to this
  // small trim's text area (6.875in less 1.5in of margins)
  publishing-info: publisher-page(height: 5.35in, note: [
    Quoted bible verses from the Berean Standard Bible unless otherwise stated.
  ]),
  preface: [
    #align(center)[
      #text()[
        Enfield, Connecticut
    
        July 8, 1741 
      ]
    ]
    
    #align(center + horizon)[
      #text(size: 14pt)[_“Their foot shall slide in due time.” - Deuteronomy 32:35_]

      #v(2em)
      #text(size: 8pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), once in a sentence; a plain “you” is singular or general.]
    ]
  ],
  page-height: 6.875in,
  page-width: 4.25in,
  page-margin: (top: 0.9in, bottom: 0.6in, outside: 0.6in, inside: 0.5in),   // Lulu: under 60 pages
  show-outline: false
)
#include "chapters/modern/sermon.typ"
