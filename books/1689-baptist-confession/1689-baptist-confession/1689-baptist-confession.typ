#import "@local/fgbooksLBCF:0.1.0": *
#import "proofs.typ": catechism

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
// the Scripture proofs under each paragraph and answer (proofs.typ)
#set enum(numbering: n => text(weight: "bold", size: 9pt)[#n.])
#show enum: set text(size: 9pt)
#set text(hyphenate: false, size: 10pt)
#set par(first-line-indent: 0pt)

= The Baptist Confession

#[
  #set text(size: 11pt)
  #include "chapters/typ/confession/00-preface.typ"
]

#[
  // the confession's chapter titles in capitals, as it has always been set
  #show heading.where(level: 2): upper
  #for n in range(1, 33) {
    include "chapters/typ/confession/chapter-" + (if n < 10 { "0" } else { "" }) + str(n) + ".typ"
  }
  // the signatories a line each, close together
  #[
    #set par(spacing: 0.5em)
    #include "chapters/typ/confession/33-closing.typ"
  ]
]

= The Baptist Catechism

#catechism(true)
#include "chapters/typ/baptist-catechism/questions.typ"

= An Orthodox Catechism

#catechism(false)
#include "chapters/typ/orthodox-catechism/00-preface.typ"

#catechism(true)
#for n in range(1, 7) {
  include "chapters/typ/orthodox-catechism/section-" + str(n) + ".typ"
}
