#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [Indwelling Sin],
  subtitle: [The Nature, Power, Deceit, and Prevalency of the Remainders of Indwelling Sin in Believers],
  author: "John Owen",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _O wretched man that I am! who shall deliver me from the body of this death? I thank God through Jesus Christ our Lord._

        — Romans 7:24-25
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1in),   // Lulu: 151-400 pages
)

#include "chapters/typ/preface.typ"

#include "chapters/typ/chapter-01.typ"

#include "chapters/typ/chapter-02.typ"

#include "chapters/typ/chapter-03.typ"

#include "chapters/typ/chapter-04.typ"

#include "chapters/typ/chapter-05.typ"

#include "chapters/typ/chapter-06.typ"

#include "chapters/typ/chapter-07.typ"

#include "chapters/typ/chapter-08.typ"

#include "chapters/typ/chapter-09.typ"

#include "chapters/typ/chapter-10.typ"

#include "chapters/typ/chapter-11.typ"

#include "chapters/typ/chapter-12.typ"

#include "chapters/typ/chapter-13.typ"

#include "chapters/typ/chapter-14.typ"

#include "chapters/typ/chapter-15.typ"

#include "chapters/typ/chapter-16.typ"

#include "chapters/typ/chapter-17.typ"
