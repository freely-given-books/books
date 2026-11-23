// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as christian-economy.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show outline: set text(9.5pt)

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
  title: [Christian Economy],
  subtitle: [Or, a short survey of the right manner of erecting and ordering a family, according to the Scriptures \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "William Perkins",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from William Perkins’s _Christian Oeconomie_ (1609), translated out of the Latin by Thomas Pickering; here in Modern English.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _But if it is unpleasing in your#super[+] sight to serve the #smallcaps[Lord], then choose for yourselves this day whom you will serve… As for me and my house, we will serve the #smallcaps[Lord]!_

        — Joshua 24:15
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks every plural “you” (the older “ye”); a plain “you” is singular or general.]
    ]
  ]
)

#set text(font: "Libertinus Serif", size: 11pt)

#include "chapters/modern/dedication.typ"

#include "chapters/modern/chapter-01.typ"

#include "chapters/modern/chapter-02.typ"

#include "chapters/modern/chapter-03.typ"

#include "chapters/modern/chapter-04.typ"

// a short chapter ending pulled back (print_check's page warning): letter spacing a little tighter
#[
  #set text(tracking: -0.01em)
  #include "chapters/modern/chapter-05.typ"
]

#include "chapters/modern/chapter-06.typ"

#include "chapters/modern/chapter-07.typ"

#include "chapters/modern/chapter-08.typ"

#include "chapters/modern/chapter-09.typ"

#include "chapters/modern/chapter-10.typ"

#include "chapters/modern/chapter-11.typ"

#include "chapters/modern/chapter-12.typ"

#include "chapters/modern/chapter-13.typ"

#include "chapters/modern/chapter-14.typ"

#include "chapters/modern/chapter-15.typ"

#include "chapters/modern/chapter-16.typ"

#include "chapters/modern/chapter-17.typ"

#include "chapters/modern/chapter-18.typ"
