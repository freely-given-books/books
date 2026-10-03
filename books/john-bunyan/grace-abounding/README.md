# Grace Abounding to the Chief of Sinners — John Bunyan

*Grace Abounding to the Chief of Sinners: or, a Brief Relation of the
Exceeding Mercy of God in Christ, to His Poor Servant John Bunyan* (first
published 1666; enlarged by Bunyan up to the sixth edition, 1688).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/preface.typ` | Bunyan's preface to his "children" |
| `chapters/typ/relation.typ` | the relation itself, in Bunyan's numbered paragraphs |
| `chapters/typ/call-to-the-ministry.typ` | his call to the work of the ministry |
| `chapters/typ/imprisonment.typ` | his imprisonment |
| `chapters/typ/conclusion.typ` | the conclusion |
| `grace-abounding.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/panel_cover.typ`, ochre); its front panel is the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/grace.thml.xml` | CCEL's ThML, untouched ([ccel.org/ccel/b/bunyan/grace.xml](https://www.ccel.org/ccel/b/bunyan/grace.xml)): the provenance |
| `source/A30143.witness.xml` | witness: the 1666 first edition, EEBO-TCP [A30143](https://github.com/textcreationpartnership/A30143), untouched |
| `source/grace-abounding.tei.xml` | enriched TEI edition: the CCEL text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/review-report.md` | the editor decisions (corrections to CCEL) |
| `source/witness-report.md` | where the 1666 first edition differs: Bunyan's later additions and revisions |

The text is CCEL's, which is Bunyan's enlarged text. CCEL's clear errors are
corrected as editor decisions (Foxe's *Acts and Monuments*, "and", Psalm
cix., and stray spaces). CCEL's "Publisher's Foreword", a modern biography
of Bunyan, is not part of this edition (it stays in `grace.thml.xml`); nor
are CCEL's contents and scripture index.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync grace-abounding      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find grace-abounding WORD # every place a word is, in CCEL and as decided
$ ./fgb page grace-abounding      # the side-by-side page (CCEL | edition)
$ ./fgb check grace-abounding     # verify
$ ./fgb build grace-abounding     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build grace-abounding`
makes them in `dist/john-bunyan/grace-abounding/`.
