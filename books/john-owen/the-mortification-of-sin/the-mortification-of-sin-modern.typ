// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as
// the-mortification-of-sin.typ, its text from chapters/modern, paragraph for paragraph
// with chapters/typ.
#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [The Mortification of Sin],
  subtitle: [Of the Mortification of Sin in Believers: the Necessity, Nature, and Means of It; with a Resolution of Sundry Cases of Conscience Thereunto Belonging \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _For if you#super[+] live according to the flesh, you#super[+] will die; but if by the Spirit you#super[+] put to death the deeds of the body, you#super[+] will live._

        — Romans 8:13
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
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

// the preface's signature would stand alone on the next page: its letter spacing a little tighter brings it back
#[
  #set text(tracking: -0.015em)
  #include "chapters/modern/preface.typ"
]

#include "chapters/modern/chapter-01.typ"

#include "chapters/modern/chapter-02.typ"

#include "chapters/modern/chapter-03.typ"

#include "chapters/modern/chapter-04.typ"

#include "chapters/modern/chapter-05.typ"

#include "chapters/modern/chapter-06.typ"

#include "chapters/modern/chapter-07.typ"

#include "chapters/modern/chapter-08.typ"

// chapter 9's last lines would stand alone on the next page: its letter spacing a little tighter brings it back
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter-09.typ"
]

#include "chapters/modern/chapter-10.typ"

// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.005em)
  #include "chapters/modern/chapter-11.typ"
]

#include "chapters/modern/chapter-12.typ"

#include "chapters/modern/chapter-13.typ"

#include "chapters/modern/chapter-14.typ"
