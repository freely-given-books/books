// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as religious-affections.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.15.0": *
#import "../../../scripts/outline_marks.typ": outline-marks
#import "stray-notes.typ": keep-text

#show: book.with(
  title: [Religious Affections],
  subtitle: [A Treatise Concerning Religious Affections, in Three Parts \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Jonathan Edwards",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Though you#super[+] have not seen Him, you#super[+] love Him; and though you#super[+] do not see Him now, you#super[+] believe in Him and rejoice with joy unspeakable and full of glory._

        — 1 Peter 1:8

      #v(2em)
      #text(size: 8pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]
      ]
    ]
  ],
  // 6x9 at 10.5pt: the editor's choice for a book this long (2026-11-11)
  page-width: 6in,
  page-height: 9in,
  font-size: 10.5pt,
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.125in),   // Lulu: 401-600 pages
)

// Orphans allowed (a paragraph's first line alone at a page's foot): with orphan control Typst
// can push a marker's line onto the next page after setting its footnote. A note is kept whole
// on its page, never broken over to the next (as Gouge).
#set text(costs: (orphan: 0%))
// Edwards's longest notes (whole paragraphs of Shepard and Flavel) are kept whole only while
// they are short enough to move to the next page entire; a longer one may break.
#show footnote.entry: it => context {
  let h = measure(block(width: 6in - 0.75in - 1.125in, it)).height
  if h < 2.2in { block(breakable: false, it) } else { it }
}

// Sign XII's note 87 (Preston) kept whole on its page: its paragraph's word spacing
// wider (stray-notes.typ keep-text, print_check's footnote warning)
#show: keep-text.with(("This fruit of holy practice": "s++",))

// the outline: every level full width, each numbered point marked by its level
#show: outline-marks

#include "chapters/modern/preface.typ"


#heading(level: 1)[Part I: The Nature of the Affections]

#metadata((part: [Part I])) <kicker>
#include "chapters/modern/part-1/01-the-text.typ"

#metadata((part: [Part I])) <kicker>
#include "chapters/modern/part-1/02-what-the-affections-are.typ"

#metadata((part: [Part I])) <kicker>
#include "chapters/modern/part-1/03-religion-in-the-affections.typ"

#metadata((part: [Part I])) <kicker>
#include "chapters/modern/part-1/04-inferences.typ"


#heading(level: 1)[Part II: No Certain Signs]

#metadata((part: [Part II], sections: [No Certain Sign I])) <kicker>
#include "chapters/modern/part-2/sign-01.typ"

#metadata((part: [Part II], sections: [No Certain Sign II])) <kicker>
// its last lines would stand alone on the next page: its letter spacing a little tighter
// brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-2/sign-02.typ"
]

#metadata((part: [Part II], sections: [No Certain Sign III])) <kicker>
#include "chapters/modern/part-2/sign-03.typ"

#metadata((part: [Part II], sections: [No Certain Sign IV])) <kicker>
// its last lines would stand alone on the next page: its letter spacing a little tighter
// brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-2/sign-04.typ"
]

#metadata((part: [Part II], sections: [No Certain Sign V])) <kicker>
#include "chapters/modern/part-2/sign-05.typ"

#metadata((part: [Part II], sections: [No Certain Sign VI])) <kicker>
#include "chapters/modern/part-2/sign-06.typ"

#metadata((part: [Part II], sections: [No Certain Sign VII])) <kicker>
#include "chapters/modern/part-2/sign-07.typ"

#metadata((part: [Part II], sections: [No Certain Sign VIII])) <kicker>
#include "chapters/modern/part-2/sign-08.typ"

#metadata((part: [Part II], sections: [No Certain Sign IX])) <kicker>
#include "chapters/modern/part-2/sign-09.typ"

#metadata((part: [Part II], sections: [No Certain Sign X])) <kicker>
// its last lines would stand alone on the next page: its letter spacing a little tighter
// brings them back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "chapters/modern/part-2/sign-10.typ"
]

#metadata((part: [Part II], sections: [No Certain Sign XI])) <kicker>
#include "chapters/modern/part-2/sign-11.typ"

#metadata((part: [Part II], sections: [No Certain Sign XII])) <kicker>
#include "chapters/modern/part-2/sign-12.typ"


#heading(level: 1)[Part III: Distinguishing Signs]

#metadata((part: [Part III], sections: [Distinguishing Signs])) <kicker>
#include "chapters/modern/part-3/00-of-the-signs.typ"

#metadata((part: [Part III], sections: [Sign I])) <kicker>
// its last lines would stand alone on the next page: its letter spacing a little tighter
// brings them back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "chapters/modern/part-3/sign-01.typ"
]

#metadata((part: [Part III], sections: [Sign II])) <kicker>
#include "chapters/modern/part-3/sign-02.typ"

#metadata((part: [Part III], sections: [Sign III])) <kicker>
// its last lines would stand alone on the next page: its letter spacing a little tighter
// brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-3/sign-03.typ"
]

#metadata((part: [Part III], sections: [Sign IV])) <kicker>
// its last lines would stand alone on the next page: its letter spacing a little tighter
// brings them back (print_check's page warning)
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/part-3/sign-04.typ"
]

#metadata((part: [Part III], sections: [Sign V])) <kicker>
#include "chapters/modern/part-3/sign-05.typ"

#metadata((part: [Part III], sections: [Sign VI])) <kicker>
#include "chapters/modern/part-3/sign-06.typ"

#metadata((part: [Part III], sections: [Sign VII])) <kicker>
// its last lines would stand alone on the next page: its letter spacing a little tighter
// brings them back (print_check's page warning)
#[
  #set text(tracking: -0.02em)
  #include "chapters/modern/part-3/sign-07.typ"
]

#metadata((part: [Part III], sections: [Sign VIII])) <kicker>
#include "chapters/modern/part-3/sign-08.typ"

#metadata((part: [Part III], sections: [Sign IX])) <kicker>
#include "chapters/modern/part-3/sign-09.typ"

#metadata((part: [Part III], sections: [Sign X])) <kicker>
#include "chapters/modern/part-3/sign-10.typ"

#metadata((part: [Part III], sections: [Sign XI])) <kicker>
// a long sign's notes kept on their markers' pages (print_check): letter spacing a little tighter
#[
  #set text(tracking: -0.005em)
  #include "chapters/modern/part-3/sign-11.typ"
]

#metadata((part: [Part III], sections: [Sign XII])) <kicker>
// a long sign's notes kept on their markers' pages (print_check): letter spacing a little looser
#[
  #set text(tracking: 0.0035em)
  #include "chapters/modern/part-3/sign-12.typ"
]
