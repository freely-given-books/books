#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [The Gospel Minister’s Maintenance Vindicated],
  subtitle: [Wherein a Regular Ministry in the Churches Is First Asserted, and the Objections Against a Gospel Maintenance for Ministers Answered],
  author: "Benjamin Keach",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Even so hath the Lord ordained that they which preach the gospel should live of the gospel._

        — 1 Corinthians 9:14
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

#metadata[Foreword] <short>
#include "chapters/typ/foreword.typ"

#metadata[Recommendation] <short>
#include "chapters/typ/recommendation.typ"

#metadata[A Regular Ministry in the Church Asserted] <short>
#include "chapters/typ/chapter-01.typ"

#metadata[The Minister’s Maintenance Vindicated] <short>
#include "chapters/typ/chapter-02.typ"

#metadata[Motives to Press the Duty] <short>
#include "chapters/typ/chapter-03.typ"

#metadata[The Work of a Gospel Minister] <short>
#include "chapters/typ/chapter-04.typ"
