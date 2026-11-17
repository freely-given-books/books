// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as the-secret-key-of-heaven.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show outline: set text(10pt)

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
  title: [The Secret Key of Heaven],
  subtitle: [Or twenty arguments for closet prayer \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "Thomas Brooks",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from Thomas Brooks’s _The Privy Key of Heaven_ (1665), in modern English.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _But when you pray, go into your closet, shut your door, and pray to your Father, who is in secret. And your Father, who sees in secret, will reward you openly._

        — Matthew 6:6
      ]
      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), once in a sentence; a plain “you” is singular or general.]
    ]
  ]
)

#set text(font: "Libertinus Serif", size: 11pt)

#include "chapters/modern/chapter-01.typ"

#include "chapters/modern/chapter-02.typ"

#include "chapters/modern/chapter-03.typ"

= Twenty Arguments for Private Prayer

#include "chapters/modern/argument-01.typ"

#include "chapters/modern/argument-02.typ"

#include "chapters/modern/argument-03.typ"

#include "chapters/modern/argument-04.typ"

#include "chapters/modern/argument-05.typ"

#include "chapters/modern/argument-06.typ"

#include "chapters/modern/argument-07.typ"

#include "chapters/modern/argument-08.typ"

#include "chapters/modern/argument-09.typ"

#include "chapters/modern/argument-10.typ"

#include "chapters/modern/argument-11.typ"

#include "chapters/modern/argument-12.typ"

#include "chapters/modern/argument-13.typ"

#include "chapters/modern/argument-14.typ"

#include "chapters/modern/argument-15.typ"

#include "chapters/modern/argument-16.typ"

#include "chapters/modern/argument-17.typ"

#include "chapters/modern/argument-18.typ"

#include "chapters/modern/argument-19.typ"

#include "chapters/modern/argument-20.typ"

= Application

#include "chapters/modern/application-01.typ"

#include "chapters/modern/application-02.typ"

#include "chapters/modern/application-03.typ"

#include "chapters/modern/application-04.typ"

#include "chapters/modern/application-05.typ"
