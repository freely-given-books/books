# Of Temptation — John Owen

*Of Temptation: the Nature and Power of It; the Danger of Entering into It;
and the Means of Preventing That Danger: with a Resolution of Sundry Cases
Thereunto Belonging* (Oxford, 1658). Puritan Paperbacks #25 (*Temptation:
Resisted and Repulsed*), here in full.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/to-the-reader.typ` | Owen's preface to the Christian reader |
| `chapters/typ/chapter-01.typ` … `chapter-09.typ` | the nine chapters, each opening with Goold's summary of it |
| `of-temptation.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/panel_cover.typ`, Owen's slate); its front panel is the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/temptation.thml.xml` | CCEL's ThML, untouched ([ccel.org/ccel/o/owen/temptation.xml](https://www.ccel.org/ccel/o/owen/temptation.xml)): the provenance |
| `source/A90277.witness.xml` | witness: the 1658 first edition, EEBO-TCP [A90277](https://github.com/textcreationpartnership/A90277), untouched |
| `source/of-temptation.tei.xml` | enriched TEI edition: the CCEL text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/review-report.md` | the editor decisions (corrections to CCEL) |
| `source/witness-report.md` | the corrections from Goold's printings and the 1658 edition |

The text is CCEL's, which is Goold's (*The Works of John Owen*, vol. 6,
1850–53), with his page breaks kept in the TEI. CCEL's text of this treatise
dropped words and whole lines in many places; they are restored from
Goold's printing, with the 1658 edition agreeing, and where Goold departs
from Owen's own words, Owen's are kept (`source/witness-report.md`).
Goold's prefatory note is not part of this edition (it stays in
`temptation.thml.xml`), nor are CCEL's indexes.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync of-temptation      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find of-temptation WORD # every place a word is, in CCEL and as decided
$ ./fgb page of-temptation      # the side-by-side page (CCEL | edition)
$ ./fgb check of-temptation     # verify
$ ./fgb build of-temptation     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build of-temptation`
makes them in `dist/john-owen/of-temptation/`.
