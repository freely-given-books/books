#import "@local/fgbooks:0.14.0": *
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

// Notes kept on their marker's page (stray-notes.typ, from Gouge; print_check.py):
// the paragraphs before notes 12 and 27 set with -/+0.01em letter spacing
#show: keep-text.with(("2. I Pass to the second, the": "t-", "2. The second heart-quieting": "t+", ))

// Orphans allowed (a paragraph's first line alone at a page's foot): with
// orphan control Typst can push a marker's line onto the next page after
// setting its footnote, so note and marker part (as Gouge). Widows are still avoided.
#set text(costs: (orphan: 0%))

#include "chapters/typ/to-the-reader.typ"

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

#include "chapters/typ/chapter-04.typ"

#include "chapters/typ/chapter-05.typ"

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"

// Chapter X set a hair tighter (leading 0.765em, the book's 0.78em): at full
// spacing its last two lines run onto a page of their own
#[
  #set par(leading: 0.765em)
  #include "chapters/typ/chapter-10.typ"
]

#include "chapters/typ/chapter-11.typ"

#include "chapters/typ/chapter-12.typ"

#include "chapters/typ/chapter-13.typ"

// Chapter XIV set a hair tighter (leading 0.775em, the book's 0.78em) so
// note 149 stays on its marker's page
#[
  #set par(leading: 0.775em)
  #include "chapters/typ/chapter-14.typ"
]

#include "chapters/typ/chapter-15.typ"

#include "chapters/typ/chapter-16.typ"
