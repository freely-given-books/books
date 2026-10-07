#import "@local/fgbooks:0.5.4": *

#show: book.with(
  title: [Sinners in the Hands of an Angry God],
  author: "Jonathan Edwards",
  publishing-info: [
    This copy is provided to you free of charge under the Creative Commons CC0 1.0 Universal license. 
    
    https://creativecommons.org/publicdomain/zero/1.0/

    #image("lcc_standard_pd.png", width: 50%)
    
    Freely you have received; freely give. - Matthew 10:8b
    
    To get more free ebooks or at-cost printed copies, visit:
    
    https://books.freely.giving
    
    Printed books are at the cost of the printing, no revenue or
    royalty is made from printings so you can get ahold of
    physical prints at the lowest cost possible.
    
    Book formatted by Courtney Allen Hicks
    
    #link("mailto:books@lyndnex.com")
    
    ebook and PDF also available.

    Quoted bible verses from the Berean Standard Bible unless otherwise stated.
  ],
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
