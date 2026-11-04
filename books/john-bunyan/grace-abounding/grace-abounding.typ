#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [Grace Abounding to the Chief of Sinners],
  subtitle: [Or, a Brief Relation of the Exceeding Mercy of God in Christ, to His Poor Servant John Bunyan],
  author: "John Bunyan",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Come and hear, all ye that fear God, and I will declare what he hath done for my soul._

        — Psalm 66:16
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

// The preface's dedication, set centred under its title (the layout's
// subtitle), stands a little apart from the text, as the ebook sets it.
#show align: it => if it.alignment == center { it + v(0.8em) } else { it }

#metadata[A Preface] <short>
#include "chapters/typ/preface.typ"

#metadata[Grace Abounding] <short>
#include "chapters/typ/relation.typ"

#metadata[The Author’s Call to the Ministry] <short>
#include "chapters/typ/call-to-the-ministry.typ"

#metadata[The Author’s Imprisonment] <short>
#include "chapters/typ/imprisonment.typ"

#metadata[The Conclusion] <short>
#include "chapters/typ/conclusion.typ"
