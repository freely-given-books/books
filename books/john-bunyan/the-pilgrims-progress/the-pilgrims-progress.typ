#import "@local/fgbooks:0.5.4": *



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
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.125in),
)

#set text(font: "Liberation Serif", size: 11pt)
#set par(first-line-indent: 0em, spacing: 1.5em)
#include "chapters/typ/apology.typ"

= PART ONE

#include "chapters/typ/part-1/stage-01.typ"

#include "chapters/typ/part-1/stage-02.typ"

#include "chapters/typ/part-1/stage-03.typ"

#include "chapters/typ/part-1/stage-04.typ"

#include "chapters/typ/part-1/stage-05.typ"

#include "chapters/typ/part-1/stage-06.typ"

#include "chapters/typ/part-1/stage-07.typ"

#include "chapters/typ/part-1/stage-08.typ"

#include "chapters/typ/part-1/stage-09.typ"

#include "chapters/typ/part-1/stage-10.typ"

#include "chapters/typ/part-1/conclusion.typ"

= PART TWO

// Part Two's title page, set as Part One's preface page is
#page(header: none)[#align(center + horizon)[#include "chapters/typ/part-2/title.typ"]]

#include "chapters/typ/part-2/authors-way.typ"

#include "chapters/typ/part-2/to-the-reader.typ"

#include "chapters/typ/part-2/stage-01.typ"

#include "chapters/typ/part-2/stage-02.typ"

#include "chapters/typ/part-2/stage-03.typ"

#include "chapters/typ/part-2/stage-04.typ"

#include "chapters/typ/part-2/stage-05.typ"

#include "chapters/typ/part-2/stage-06.typ"

#include "chapters/typ/part-2/stage-07.typ"

#include "chapters/typ/part-2/stage-08.typ"
