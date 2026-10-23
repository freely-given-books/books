#import "@local/fgbooksLBCF:0.1.0": *
#import "@local/fgbooks:0.13.0": publisher-page
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
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
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
