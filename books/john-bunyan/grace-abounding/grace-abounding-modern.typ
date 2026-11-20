// The Modern English edition (MODERN-ENGLISH-RULES.md): the same book as grace-abounding.typ,
// its text from chapters/modern, paragraph for paragraph with chapters/typ.
#import "@local/fgbooks:0.14.0": *

#show: book.with(
  title: [Grace Abounding to the Chief of Sinners],
  subtitle: [Or, a Brief Relation of the Exceeding Mercy of God in Christ, to His Poor Servant John Bunyan \ #v(0.6em) #text(size: 0.85em, tracking: 0.12em)[MODERN ENGLISH]],
  author: "John Bunyan",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Come and listen, all you#super[+] who fear God, and I will declare what He has done for my soul._

        — Psalm 66:16
      ]

      #v(2em)
      #text(size: 9pt)[Scripture is quoted from the Berean Standard Bible, kept closer to the author’s own Bible where his argument rests on its wording; capitals for God in quotations (He, His) follow the BSB. “You#super[+]” marks a plural “you” (the older “ye”), once in a sentence; a plain “you” is singular or general.]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 0.625in),   // Lulu: 61-150 pages
)

// The preface's dedication, set centred under its title (the layout's
// subtitle), stands a little apart from the text, as the ebook sets it.
#show align: it => if it.alignment == center { it + v(0.8em) } else { it }

#metadata[A Preface] <short>
#include "chapters/modern/preface.typ"

#metadata[Grace Abounding] <short>
#include "chapters/modern/relation.typ"

#metadata[The Author’s Call to the Ministry] <short>
#include "chapters/modern/call-to-the-ministry.typ"

#metadata[The Author’s Imprisonment] <short>
#include "chapters/modern/imprisonment.typ"

#metadata[The Conclusion] <short>
#include "chapters/modern/conclusion.typ"
