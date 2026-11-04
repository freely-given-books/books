#import "@local/fgbooks:0.15.0": *
#import "stray-notes.typ": keep-notes, keep-text

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
  subtitle: [Volume II — The Second, Third and Fourth Treatises: Of Husband and Wife],
  author: "William Gouge",
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.0in),
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(note: [
    Set from William Gouge's _Of Domesticall Dvties_ (London, printed by John Haviland for William Bladen, 1622), with the spelling modernized. The text is the Text Creation Partnership transcription of the first edition (EEBO-TCP A68107).

    This is volume 2 of four. The complete work is in eight treatises: I, an exposition of Ephesians 5:21–6:9; II, of husband and wife; III, of wives; IV, of husbands; V, of children; VI, of parents; VII, of servants; VIII, of masters.
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
// Notes kept on their marker's page (stray-notes.typ; print_check.py)
#show: keep-notes.with(("16": "w", "104": "s+", "224": "b", "527": "w", "540": "t+", "596": "b", "681": "b", "703": "s++", "705": "w", "718": "b", "719": "s-", "851": "w", "1025": "s--", "1106": "w", "1116": "b", "1184": "b",))
#show: keep-text.with(("§. 12. Of wife-like modesty": "b", "§. 58. Of wives complemental": "b", "to enforce the same": "s+", "That matrimonial society may": "k", "the other from the": "k", "and content with his": "k", "§. 30. Of husbands and": "b", "§. 21. Of the things": "b", "§. 25. Of the law": "b", "§. 16. Of husbands ready": "b", "§. 13. Of that mutual": "b", "§. 32. Of husbands and": "b", "§. 20. Of Husbands encouraging": "b", "§. 21. Of husbands ungrateful": "b", "when we come to": "k", "On the other side,": "ts-", "If a wife must": "t+", "Others, through discontent lie": "t-",))

#metadata[Seeking Marriage] <short>
#metadata((part: [The Second Treatise, Part I: Of Husband and Wife], sections: [§§. 1–13])) <kicker>
#include "chapters/typ/vol-2/01-seeking-marriage.typ"

#metadata[Getting Married] <short>
#metadata((part: [The Second Treatise, Part I: Of Husband and Wife], sections: [§§. 14–28])) <kicker>
#include "chapters/typ/vol-2/02-getting-married.typ"

#metadata[Marital Unity and Sexual Faithfulness] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 1–9])) <kicker>
#include "chapters/typ/vol-2/03-marital-unity-and-sexual-faithfulness.typ"

#metadata[Living Together in Love] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 10–17])) <kicker>
#include "chapters/typ/vol-2/04-living-together-in-love.typ"

#metadata[Caring for Each Other’s Souls] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 18–28])) <kicker>
#include "chapters/typ/vol-2/05-caring-for-each-others-souls.typ"

#metadata[Guarding Each Other’s Health, Reputation, and Property] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 29–39])) <kicker>
#include "chapters/typ/vol-2/06-guarding-each-others-health-reputation-and-property.typ"

#metadata[Serving Together in Family Ministry] <short>
#metadata((part: [The Second Treatise, Part II: Of Their Common Duties], sections: [§§. 40–45])) <kicker>
#include "chapters/typ/vol-2/07-serving-together-in-family-ministry.typ"

#metadata[A Wife’s Respect for Her Husband] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 1–16])) <kicker>
#include "chapters/typ/vol-2/08-a-wifes-respect-for-her-husband.typ"

#metadata[A Wife’s Not Going Against Her Husband’s Will (I)] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 17–32])) <kicker>
#include "chapters/typ/vol-2/09-a-wifes-not-going-against-her-husbands-will-i.typ"

#metadata[A Wife’s Not Going Against Her Husband’s Will (II)] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 33–42])) <kicker>
#include "chapters/typ/vol-2/10-a-wifes-not-going-against-her-husbands-will-ii.typ"

#metadata[A Wife’s Active Obedience to Her Husband] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 43–50])) <kicker>
#include "chapters/typ/vol-2/11-a-wifes-active-obedience-to-her-husband.typ"

#metadata[A Wife’s Submission to Christ First] <short>
#metadata((part: [The Third Treatise: Of Wives], sections: [§§. 51–74])) <kicker>
#include "chapters/typ/vol-2/12-a-wifes-submission-to-christ-first.typ"

#metadata[A Husband’s Affectionate Authority over His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 1–12])) <kicker>
#include "chapters/typ/vol-2/13-a-husbands-affectionate-authority-over-his-wife.typ"

#metadata[A Husband’s Humble Gentleness to His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 13–23])) <kicker>
#include "chapters/typ/vol-2/14-a-husbands-humble-gentleness-to-his-wife.typ"

#metadata[A Husband’s Patient Correcting of His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 24–39])) <kicker>
#include "chapters/typ/vol-2/15-a-husbands-patient-correcting-of-his-wife.typ"

#metadata[A Husband’s Kind Conduct toward His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 40–46])) <kicker>
#include "chapters/typ/vol-2/16-a-husbands-kind-conduct-toward-his-wife.typ"

#metadata[A Husband’s Providing for His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 46–60])) <kicker>
#include "chapters/typ/vol-2/17-a-husbands-providing-for-his-wife.typ"

#metadata[A Husband’s Sincere and Steady Love for His Wife] <short>
#metadata((part: [The Fourth Treatise: Of Husbands], sections: [§§. 61–76])) <kicker>
#include "chapters/typ/vol-2/18-a-husbands-sincere-and-steady-love-for-his-wife.typ"
