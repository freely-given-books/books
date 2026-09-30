#import "@local/fgbooksLBCF:0.1.0": *
#import "helpers.typ": *


#show outline: set text(size: 8pt)
#show: book.with(
  title: [The 1689 Baptist Confession of Faith],
  subtitle: [With Catechisms],
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
)
#set enum(numbering: n => text(weight: "bold", size: 9pt)[#n.])
#show enum: set text(size: 9pt)
#set text(hyphenate: false, size: 10pt)
#set par(first-line-indent: 0pt)

= The Baptist Confession 

#include "chapters/typ/preface.typ"

#lbcf-all-chapters()

#include "chapters/typ/ending_statement_and_signatories.typ"

= The Baptist Catechism

#bc1695-all-questions()

= An Orthodox Catechism

#include "chapters/typ/aoc_preface.typ"

#aoc1680-all-questions()
