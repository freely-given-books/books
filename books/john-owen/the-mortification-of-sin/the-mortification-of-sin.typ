#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [The Mortification of Sin],
  subtitle: [Of the Mortification of Sin in Believers: the Necessity, Nature, and Means of It; with a Resolution of Sundry Cases of Conscience Thereunto Belonging],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _For if ye live after the flesh, ye shall die: but if ye through the Spirit do mortify the deeds of the body, ye shall live._

        — Romans 8:13
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

// the outline: every level full width, each numbered point marked by its level and given
// a little space (scripts/outline_marks.typ; the editor's choice, 2026-11-09)
#show: outline-marks

// Owen's summary under each chapter's title (the TEI's <argument>, the book's only
// inset block): a line's space before the chapter's first paragraph.
#show block: it => if it.inset == (left: 1em, right: 1em) { block(below: 1.6em, it) } else { it }
// A note wholly in Greek or Hebrew is set ragged-right: its words cannot be
// hyphenated, and justified they leave wide gaps (Mortification ch. 6, note on
// Rom 7:23). A one-line note is unchanged.
#let note-text(c) = if type(c) == str { c } else if c.has("text") { c.text } else if c.has("children") { c.children.map(note-text).join("") } else if c.has("body") { note-text(c.body) } else { "" }
#show footnote.entry: it => if note-text(it.note.body).contains(regex("[A-Za-z]")) { it } else { set par(justify: false); it }

#include "chapters/typ/preface.typ"

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

// chapter 4 of the 1668 text would end on a few lines alone: its letter spacing a
// little looser carries more of it over (print_check's page warning; tightening
// instead would take the book under Lulu's 151 pages for this margin)
#[
  #set text(tracking: 0.01em)
  #include "chapters/typ/chapter-04.typ"
]

// chapter 5 of the 1668 text would end on a few lines alone: its letter spacing a
// little looser carries more of it over (print_check's page warning; tightening
// instead would take the book under Lulu's 151 pages for this margin)
#[
  #set text(tracking: 0.01em)
  #include "chapters/typ/chapter-05.typ"
]

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"

#include "chapters/typ/chapter-10.typ"

// chapter 11 of the 1668 text would end on a few lines alone: its letter spacing a
// little looser carries more of it over (print_check's page warning; tightening
// instead would take the book under Lulu's 151 pages for this margin)
#[
  #set text(tracking: 0.01em)
  #include "chapters/typ/chapter-11.typ"
]

#include "chapters/typ/chapter-12.typ"

#include "chapters/typ/chapter-13.typ"

#include "chapters/typ/chapter-14.typ"
