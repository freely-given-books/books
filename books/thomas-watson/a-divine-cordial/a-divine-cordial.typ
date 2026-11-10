#import "@local/fgbooks:0.14.0": *
#import "../../../scripts/outline_marks.typ": outline-marks
#import "stray-notes.typ": keep-text

#show: book.with(
  title: [A Divine Cordial],
  subtitle: [Or, the Transcendent Privilege of Those That Love God and Are Savingly Called],
  author: "Thomas Watson",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _But as for you, ye thought evil against me; but God meant it unto good._

        — Genesis 50:20
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

// the outline: every level full width, each numbered point marked by its level and given
// a little space (scripts/outline_marks.typ; the editor's choice, 2026-11-09)
#show: outline-marks

// Notes kept on their marker's page (stray-notes.typ, from Gouge; print_check.py):
// the paragraphs before notes 12 and 27 set with -/+0.01em letter spacing
#show: keep-text.with(("2. I Pass to the second, the": "t-", "2. The second heart-quieting": "t+", ))

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/chapter-01.typ"

// Chapter 2's letter spacing a hair tighter (-0.02em) so its notes stay on their markers'
// pages and no page ends on a lone heading or a chapter on a few lines (print_check)
#[
  #set text(tracking: -0.02em)
  #include "chapters/typ/chapter-02.typ"
]

#include "chapters/typ/chapter-03.typ"

#include "chapters/typ/chapter-04.typ"

// Chapter 5's letter spacing a hair tighter (-0.02em) so its notes stay on their markers'
// pages and no page ends on a lone heading or a chapter on a few lines (print_check)
#[
  #set text(tracking: -0.02em)
  #include "chapters/typ/chapter-05.typ"
]

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

// Chapter 9's letter spacing a hair looser (0.01em) so its notes stay on their markers'
// pages and no page ends on a lone heading or a chapter on a few lines (print_check)
#[
  #set text(tracking: 0.01em)
  #include "chapters/typ/chapter-09.typ"
]

// Chapter 10's letter spacing a hair tighter (-0.01em) so its notes stay on their markers'
// pages and no page ends on a lone heading or a chapter on a few lines (print_check)
#[
  #set text(tracking: -0.01em)
  #include "chapters/typ/chapter-10.typ"
]

#include "chapters/typ/chapter-11.typ"

#include "chapters/typ/chapter-12.typ"

// Chapter 13's letter spacing a hair looser (0.01em) so its notes stay on their markers'
// pages and no page ends on a lone heading or a chapter on a few lines (print_check)
#[
  #set text(tracking: 0.01em)
  #include "chapters/typ/chapter-13.typ"
]

#include "chapters/typ/chapter-14.typ"

#include "chapters/typ/chapter-15.typ"

#include "chapters/typ/chapter-16.typ"
