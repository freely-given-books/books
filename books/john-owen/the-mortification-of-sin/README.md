# The Mortification of Sin — John Owen

*Of the Mortification of Sin in Believers: the Necessity, Nature, and Means
of It; with a Resolution of Sundry Cases of Conscience Thereunto Belonging*
(first published 1656; the second edition 1668). Puritan Paperbacks #48,
here in full.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/preface.typ` | Owen's preface to the Christian reader |
| `chapters/typ/chapter-01.typ` … `chapter-14.typ` | the fourteen chapters, each opening with Owen's summary of it |
| `the-mortification-of-sin.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/panel_cover.typ`, slate); its front panel is the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/mort.thml.xml` | CCEL's ThML, untouched ([ccel.org/ccel/o/owen/mort.xml](https://www.ccel.org/ccel/o/owen/mort.xml)): the provenance |
| `source/A53715.witness.xml` | witness: the 1668 second edition, EEBO-TCP [A53715](https://github.com/textcreationpartnership/A53715), untouched |
| `source/the-mortification-of-sin.tei.xml` | enriched TEI edition: the CCEL text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/review-report.md` | the editor decisions (corrections to CCEL) |
| `source/witness-report.md` | the corrections from Goold's 1850 printing, and where the 1668 edition differs |

The text is CCEL's, which is Goold's (*The Works of John Owen*, vol. 6,
1850–53), with his page breaks kept in the TEI. Two lines CCEL dropped and
three slips are corrected from Goold's printing, with the 1668 edition
agreeing (`source/witness-report.md`). Goold's prefatory note is not part of
this edition (it stays in `mort.thml.xml`), nor are CCEL's indexes.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync the-mortification-of-sin      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find the-mortification-of-sin WORD # every place a word is, in CCEL and as decided
$ ./fgb page the-mortification-of-sin      # the side-by-side page (CCEL | edition)
$ ./fgb check the-mortification-of-sin     # verify
$ ./fgb build the-mortification-of-sin     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build the-mortification-of-sin`
makes them in `dist/john-owen/the-mortification-of-sin/`.
