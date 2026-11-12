#import "@local/fgbooks:0.15.0": *
#import "../../../scripts/outline_marks.typ": outline-marks

#show: book.with(
  title: [Religious Affections],
  subtitle: [A Treatise Concerning Religious Affections, in Three Parts],
  author: "Jonathan Edwards",
  // the Common Weal Press publisher's page, from the template
  publishing-info: publisher-page(),
  preface: [
    #align(center + horizon)[
      #text(size: 12pt)[
        _Whom having not seen, ye love; in whom, though now ye see him not, yet believing, ye rejoice with joy unspeakable and full of glory._

        — 1 Peter 1:8
      ]
    ]
  ],
  page-margin: (bottom: 0.6in, top: 0.9in, outside: 0.75in, inside: 1.125in),   // Lulu: 401-600 pages
)

// the outline: every level full width, each numbered point marked by its level
#show: outline-marks

#include "chapters/typ/preface.typ"


#heading(level: 1)[Part I: The Nature of the Affections]

#metadata((part: [Part I])) <kicker>
#include "chapters/typ/part-1/01-the-text.typ"

#metadata((part: [Part I])) <kicker>
#include "chapters/typ/part-1/02-what-the-affections-are.typ"

#metadata((part: [Part I])) <kicker>
#include "chapters/typ/part-1/03-religion-in-the-affections.typ"

#metadata((part: [Part I])) <kicker>
#include "chapters/typ/part-1/04-inferences.typ"


#heading(level: 1)[Part II: No Certain Signs]

#metadata((part: [Part II], sections: [No Certain Sign I])) <kicker>
#include "chapters/typ/part-2/sign-01.typ"

#metadata((part: [Part II], sections: [No Certain Sign II])) <kicker>
#include "chapters/typ/part-2/sign-02.typ"

#metadata((part: [Part II], sections: [No Certain Sign III])) <kicker>
#include "chapters/typ/part-2/sign-03.typ"

#metadata((part: [Part II], sections: [No Certain Sign IV])) <kicker>
#include "chapters/typ/part-2/sign-04.typ"

#metadata((part: [Part II], sections: [No Certain Sign V])) <kicker>
#include "chapters/typ/part-2/sign-05.typ"

#metadata((part: [Part II], sections: [No Certain Sign VI])) <kicker>
#include "chapters/typ/part-2/sign-06.typ"

#metadata((part: [Part II], sections: [No Certain Sign VII])) <kicker>
#include "chapters/typ/part-2/sign-07.typ"

#metadata((part: [Part II], sections: [No Certain Sign VIII])) <kicker>
#include "chapters/typ/part-2/sign-08.typ"

#metadata((part: [Part II], sections: [No Certain Sign IX])) <kicker>
#include "chapters/typ/part-2/sign-09.typ"

#metadata((part: [Part II], sections: [No Certain Sign X])) <kicker>
#include "chapters/typ/part-2/sign-10.typ"

#metadata((part: [Part II], sections: [No Certain Sign XI])) <kicker>
#include "chapters/typ/part-2/sign-11.typ"

#metadata((part: [Part II], sections: [No Certain Sign XII])) <kicker>
#include "chapters/typ/part-2/sign-12.typ"


#heading(level: 1)[Part III: Distinguishing Signs]

#metadata((part: [Part III], sections: [Distinguishing Signs])) <kicker>
#include "chapters/typ/part-3/00-of-the-signs.typ"

#metadata((part: [Part III], sections: [Sign I])) <kicker>
#include "chapters/typ/part-3/sign-01.typ"

#metadata((part: [Part III], sections: [Sign II])) <kicker>
#include "chapters/typ/part-3/sign-02.typ"

#metadata((part: [Part III], sections: [Sign III])) <kicker>
#include "chapters/typ/part-3/sign-03.typ"

#metadata((part: [Part III], sections: [Sign IV])) <kicker>
#include "chapters/typ/part-3/sign-04.typ"

#metadata((part: [Part III], sections: [Sign V])) <kicker>
#include "chapters/typ/part-3/sign-05.typ"

#metadata((part: [Part III], sections: [Sign VI])) <kicker>
#include "chapters/typ/part-3/sign-06.typ"

#metadata((part: [Part III], sections: [Sign VII])) <kicker>
#include "chapters/typ/part-3/sign-07.typ"

#metadata((part: [Part III], sections: [Sign VIII])) <kicker>
#include "chapters/typ/part-3/sign-08.typ"

#metadata((part: [Part III], sections: [Sign IX])) <kicker>
#include "chapters/typ/part-3/sign-09.typ"

#metadata((part: [Part III], sections: [Sign X])) <kicker>
#include "chapters/typ/part-3/sign-10.typ"

#metadata((part: [Part III], sections: [Sign XI])) <kicker>
#include "chapters/typ/part-3/sign-11.typ"

#metadata((part: [Part III], sections: [Sign XII])) <kicker>
#include "chapters/typ/part-3/sign-12.typ"
