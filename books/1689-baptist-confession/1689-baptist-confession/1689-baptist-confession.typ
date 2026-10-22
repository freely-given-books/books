#import "@local/fgbooksLBCF:0.1.0": *
#import "proofs.typ": catechism, chapter-start

#show outline: set text(size: 8pt)

// A heading straight after a part page (the prefaces): the chapter heading's
// look, without the template's turn to a recto, which the part page has
// already made (two turns left a blank spread and a page with only a head).
#let after-part(body) = {
  show heading.where(level: 2): it => {
    v(5%)
    align(center, text(22pt, weight: 700, hyphenate: false, it.body))
    v(2.5em)
  }
  body
}
#show: book.with(
  title: [The 1689 Baptist Confession of Faith],
  subtitle: [With Catechisms],
  // the Common Weal Press publisher's page (common-weal-press/test-page)
  publishing-info: block(height: 6.9in, width: 100%, {
    set align(center)
    set text(font: "Libertinus Serif", size: 9pt)
    set par(justify: false, leading: 0.6em, spacing: 0.9em, first-line-indent: 0pt)
    let rule = line(length: 0.6in, stroke: 0.5pt)
    image("art/device-black.svg", width: 2.4in)
    v(0.8em)
    text(19pt)[Common Weal Press]
    v(-0.35em)
    text(10.5pt, style: "italic")[The Christian Inheritance. Freely Given.]
    v(0.1em)
    rule
    v(1fr)
    [This edition is published by Common Weal Press and dedicated to the
    public domain under the Creative Commons CC0 1.0 Universal Public Domain
    Dedication. You are free to copy, distribute, modify and use it for any
    purpose, without asking.
    #link("https://creativecommons.org/publicdomain/zero/1.0/")[creativecommons.org/publicdomain/zero/1.0]]
    parbreak()
    image("lcc_standard_pd.png", width: 42%)
    parbreak()
    [_Freely you have received; freely give._ — Matthew 10:8]
    parbreak()
    [Printed copies are sold at the cost of printing: no revenue or royalty
    is made from them. Free ebooks, PDFs and at-cost printed copies:]
    v(1fr)
    rule
    v(-0.2em)
    text(10pt, tracking: 0.05em)[commonwealpress.org]
    v(-0.3em)
    text(7.5pt)[Corrections and questions: #link("mailto:books@commonwealpress.org")[books\@commonwealpress.org]]
  }),
)
// the Scripture proofs under each paragraph and answer (proofs.typ); a
// chapter's first paragraph may run on past the page its heading is on
#show heading.where(level: 2): it => { it; chapter-start }
#set enum(numbering: n => text(weight: "bold", size: 9pt)[#n.])
#show enum: set text(size: 9pt)
#set text(hyphenate: false, size: 10pt)
#set par(first-line-indent: 0pt)

= The Baptist Confession

#[
  #set text(size: 11pt)
  #after-part(include "chapters/typ/confession/00-preface.typ")
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
#after-part(include "chapters/typ/orthodox-catechism/00-preface.typ")

#catechism(true)
#for n in range(1, 7) {
  include "chapters/typ/orthodox-catechism/section-" + str(n) + ".typ"
}
