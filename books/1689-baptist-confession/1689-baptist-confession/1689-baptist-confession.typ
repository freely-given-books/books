#import "@local/fgbooks:0.13.2": book, publisher-page
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
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.625in, inside: 1in),
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  font-size: 10pt,
)
// the Scripture proofs under each paragraph and answer (proofs.typ); a
// chapter's first paragraph may run on past the page its heading is on
// the running head on a recto is the last <short> before it (the template):
// each chapter's title, and a catechism's own name where it has none
#show heading.where(level: 2): it => { it; [#metadata(it.body) <short>]; chapter-start }
#set text(hyphenate: false)
#set par(first-line-indent: 0pt)

= The Baptist Confession

#[
  #set text(size: 11pt)
  #after-part(include "chapters/typ/confession/00-preface.typ")
]

#[
  // the confession's chapter heads: "Chapter 14" in spaced capitals over
  // the title, regular weight, a diamond rule under
  #show heading.where(level: 2): it => {
    show regex("^(\d+)\. (.+)$"): m => {
      let (n, title) = m.text.match(regex("^(\d+)\. (.+)$")).captures
      text(9pt, weight: 400, tracking: 0.3em, upper[Chapter #n])
      linebreak()
      v(0.35em)
      text(14pt, weight: 400, tracking: 0.12em, upper(title))
      linebreak()
      v(0.2em)
      box(width: 1.1in, grid(columns: (1fr, auto, 1fr), column-gutter: 0.08in, align: horizon,
        line(length: 100%, stroke: 0.5pt), text(7pt, weight: 400, sym.diamond.filled),
        line(length: 100%, stroke: 0.5pt)))
    }
    it
  }
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
#metadata[The Baptist Catechism] <short>

#catechism(true)
#include "chapters/typ/baptist-catechism/questions.typ"

= An Orthodox Catechism
#metadata[An Orthodox Catechism] <short>

#catechism(false)
#after-part(include "chapters/typ/orthodox-catechism/00-preface.typ")

#catechism(true)
#for n in range(1, 7) {
  include "chapters/typ/orthodox-catechism/section-" + str(n) + ".typ"
}
