#import "@local/fgbooks:0.13.1": *

#show: book.with(
  title: [Sinners in the Hands of an Angry God],
  author: "Jonathan Edwards",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
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
      #text(size: 14pt)[_"Their foot shall slide in due time." - Deuteronomy 32:35_]
    ]
  ],
  page-height: 6.875in,
  page-width: 4.25in,
  page-margin: (top: 0.9in, bottom: 0.6in, outside: 0.6in, inside: 0.5in),   // Lulu: under 60 pages
  show-outline: false
)
#include "chapters/typ/sermon.typ"
