#import "@local/fgbooks:0.13.2": *

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
  subtitle: [Volume I — The First Treatise: An Exposition of That Part of Scripture Out of Which Domestical Duties Are Raised],
  author: "William Gouge",
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.0in),
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from William Gouge's _Of Domesticall Dvties_ (London, printed by John Haviland for William Bladen, 1622), with the spelling modernized. The text is the Text Creation Partnership transcription of the first edition (EEBO-TCP A68107).

    This is volume 1 of four. The complete work is in eight treatises: I, an exposition of Ephesians 5:21–6:9; II, of husband and wife; III, of wives; IV, of husbands; V, of children; VI, of parents; VII, of servants; VIII, of masters.
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

#metadata[The Epistle Dedicatory] <short>
#include "chapters/typ/vol-1/dedication.typ"

#metadata[Serving Each Other in the Fear of the Lord] <short>
#include "chapters/typ/vol-1/01-serving-each-other-in-the-fear-of-the-lord.typ"

#metadata[Particular Callings and the Wife’s Submission] <short>
#include "chapters/typ/vol-1/02-particular-callings-and-the-wifes-submission.typ"

#metadata[Headship in Marriage and the Church] <short>
#include "chapters/typ/vol-1/03-headship-in-marriage-and-the-church.typ"

#metadata[Husbands and the Love of Christ] <short>
#include "chapters/typ/vol-1/04-husbands-and-the-love-of-christ.typ"

#metadata[Love That Purifies the Unclean] <short>
#include "chapters/typ/vol-1/05-love-that-purifies-the-unclean.typ"

#metadata[Redeemed for Glory] <short>
#include "chapters/typ/vol-1/06-redeemed-for-glory.typ"

#metadata[Marital Love and Self-Love] <short>
#include "chapters/typ/vol-1/07-marital-love-and-self-love.typ"

#metadata[Christ’s Union with His Beloved Body] <short>
#include "chapters/typ/vol-1/08-christs-union-with-his-beloved-body.typ"

#metadata[The Ancient Law and Unique Bond of Marriage] <short>
#include "chapters/typ/vol-1/09-the-ancient-law-and-unique-bond-of-marriage.typ"

#metadata[The Mystery and Practice of Marriage] <short>
#include "chapters/typ/vol-1/10-the-mystery-and-practice-of-marriage.typ"

#metadata[The Child’s Duties to His Parents] <short>
#include "chapters/typ/vol-1/11-the-childs-duties-to-his-parents.typ"

#metadata[The Parents’ Duty towards Their Children] <short>
#include "chapters/typ/vol-1/12-the-parents-duty-towards-their-children.typ"
