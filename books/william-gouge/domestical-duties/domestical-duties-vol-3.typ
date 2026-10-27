#import "@local/fgbooks:0.13.3": *

// Edited by hand (first written by the earlier converter): a chapter added
// or renamed in source/edition.json needs its #include and <short> lines here.
//
// The imprint's 5.5x8.5 trim (the template's), at 10.5pt: at 290,000 words
// the whole work is four times the length of anything else in the imprint,
// and the smaller type keeps each volume a comfortable thickness.  The
// inside margin follows Lulu's recommendation for a block this thick.

#show outline: set text(9.5pt)

#show: book.with(
  title: [Of Domestical Duties],
  subtitle: [Volume III — The Fifth and Sixth Treatises: Of Children and Parents],
  author: "William Gouge",
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.0in),
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from William Gouge's _Of Domesticall Dvties_ (London, printed by John Haviland for William Bladen, 1622), with the spelling modernized. The text is the Text Creation Partnership transcription of the first edition (EEBO-TCP A68107).

    This is volume 3 of four. The complete work is in eight treatises: I, an exposition of Ephesians 5:21–6:9; II, of husband and wife; III, of wives; IV, of husbands; V, of children; VI, of parents; VII, of servants; VIII, of masters.
  ]),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Submitting your selves one to another in the fear of God._

        — Ephesians 5:21
      ]
    ]
  ]
)

#set text(font: "Libertinus Serif", size: 10.5pt)
// Orphans allowed (a paragraph's first line alone at a page's foot): with
// orphan control Typst can push a marker's line onto the next page after
// setting its footnote, so note and marker part. Widows are still avoided.
#set text(costs: (orphan: 0%))
// A note is kept whole on its page, never broken over to the next (a note's
// last words alone at the top of the next page's notes read as a stray).
#show footnote.entry: it => block(breakable: false, it)
// Lists 1622 prints without numbers (a brace's unnumbered branches, "- "
// lines) are set as it prints them: no bullet, set in past a paragraph's
// first-line indent, where the brace puts them.
#set list(marker: [], indent: 2em)

#metadata[Children Showing Respect for Parents] <short>
#include "chapters/typ/vol-3/01-children-showing-respect-for-parents.typ"

#metadata[Children Getting Parents’ Permission] <short>
#include "chapters/typ/vol-3/02-children-getting-parents-permission.typ"

#metadata[Children Obeying Parents’ Instruction and Correction] <short>
#include "chapters/typ/vol-3/03-children-obeying-parents-instruction-and-correction.typ"

#metadata[Children Giving Back to Parents] <short>
#include "chapters/typ/vol-3/04-children-giving-back-to-parents.typ"

#metadata[Children Honoring Father and Mother in the Lord] <short>
#include "chapters/typ/vol-3/05-children-honoring-father-and-mother-in-the-lord.typ"

#metadata[Parents Loving, Praying, and Providing for Children] <short>
#include "chapters/typ/vol-3/06-parents-loving-praying-and-providing-for-children.typ"

#metadata[Parents Nurturing, Teaching, and Training Children] <short>
#include "chapters/typ/vol-3/07-parents-nurturing-teaching-and-training-children.typ"

#metadata[Parents Admonishing and Correcting Children] <short>
#include "chapters/typ/vol-3/08-parents-admonishing-and-correcting-children.typ"

#metadata[Parents Directing Children into Adulthood] <short>
#include "chapters/typ/vol-3/09-parents-directing-children-into-adulthood.typ"

#metadata[Parents Being Faithful to All under Their Care] <short>
#include "chapters/typ/vol-3/10-parents-being-faithful-to-all-under-their-care.typ"
