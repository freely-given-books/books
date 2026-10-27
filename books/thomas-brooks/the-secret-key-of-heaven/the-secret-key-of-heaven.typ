#import "@local/fgbooks:0.13.3": *

#show outline: set text(10pt)

#show: book.with(
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
  title: [The Secret Key of Heaven],
  subtitle: [Or twenty arguments for closet prayer],
  author: "Thomas Brooks",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from Thomas Brooks’s _The Privy Key of Heaven_ (1665), and lightly modernized.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _But thou, when thou prayest, enter into thy closet, and when thou hast shut thy door, pray to thy Father which is in secret; and thy Father which seeth in secret shall reward thee openly._

        — Matthew 6:6
      ]
    ]
  ]
)

#set text(font: "Libertinus Serif", size: 11pt)

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

= Twenty Arguments for Private Prayer

#include "chapters/typ/argument-01.typ"

#include "chapters/typ/argument-02.typ"

#include "chapters/typ/argument-03.typ"

#include "chapters/typ/argument-04.typ"

#include "chapters/typ/argument-05.typ"

#include "chapters/typ/argument-06.typ"

#include "chapters/typ/argument-07.typ"

#include "chapters/typ/argument-08.typ"

#include "chapters/typ/argument-09.typ"

#include "chapters/typ/argument-10.typ"

#include "chapters/typ/argument-11.typ"

#include "chapters/typ/argument-12.typ"

#include "chapters/typ/argument-13.typ"

#include "chapters/typ/argument-14.typ"

#include "chapters/typ/argument-15.typ"

#include "chapters/typ/argument-16.typ"

#include "chapters/typ/argument-17.typ"

#include "chapters/typ/argument-18.typ"

#include "chapters/typ/argument-19.typ"

#include "chapters/typ/argument-20.typ"

= Application

#include "chapters/typ/application-01.typ"

#include "chapters/typ/application-02.typ"

#include "chapters/typ/application-03.typ"

#include "chapters/typ/application-04.typ"

#include "chapters/typ/application-05.typ"
