#import "@local/fgbooks:0.5.1": *



#show: book.with(
  title: [The Pilgrim's Progress],
  author: "John Bunyan",
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
  ],
  preface: [
    #align(center + horizon)[
      From This World to That Which is to Come;
      
      Delivered under the Similitude of a Dream
      
      by John Bunyan
    ]
  ],
  page-margin: (bottom: 0.75in, top: 0.75in, outside: 0.75in, inside: 1.125in),
)

#set text(font: "Liberation Serif", size: 11pt)
#set par(first-line-indent: 0em, spacing: 1.5em)
#include "apology.typ"

= PART ONE

#include "part1/chapters/typst/chapter1.typ"

#include "part1/chapters/typst/chapter2.typ"

#include "part1/chapters/typst/chapter3.typ"

#include "part1/chapters/typst/chapter4.typ"

#include "part1/chapters/typst/chapter5.typ"

#include "part1/chapters/typst/chapter6.typ"

#include "part1/chapters/typst/chapter7.typ"

#include "part1/chapters/typst/chapter8.typ"

#include "part1/chapters/typst/chapter9.typ"

#include "part1/chapters/typst/conclusion.typ"

= PART TWO

#include "part2/chapters/typst/1authorsway.typ"

#include "part2/chapters/typst/2tothereader.typ"

#include "part2/chapters/typst/chapter1.typ"

#include "part2/chapters/typst/chapter2.typ"

#include "part2/chapters/typst/chapter3.typ"

#include "part2/chapters/typst/chapter4.typ"

#include "part2/chapters/typst/chapter5.typ"

#include "part2/chapters/typst/chapter6.typ"

#include "part2/chapters/typst/chapter7.typ"

#include "part2/chapters/typst/chapter8.typ"
