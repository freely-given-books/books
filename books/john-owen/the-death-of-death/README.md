# The Death of Death in the Death of Christ — John Owen

*Salus Electorum, Sanguis Jesu: or, The Death of Death in the Death of
Christ. A Treatise of the Redemption and Reconciliation That Is in the Blood
of Christ, with the Merit Thereof, and the Satisfaction Wrought Thereby*
(London, 1648). One volume, 484 pages at 10.5pt.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/epistle-dedicatory.typ`, `attestations.typ`, `to-the-reader.typ` | Owen's dedication to the Earl of Warwick, the two attestations, his preface |
| `chapters/typ/book-1/` … `book-4/` | the four Books, a chapter to a file |
| `chapters/typ/appendix-1-testimonies.typ`, `appendix-2-sprigge.typ` | the testimonies of the ancients and the appendix on Mr Sprigge's book |
| `the-death-of-death.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/panel_cover.typ`, Owen's slate); its front panel is the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/deathofdeath.thml.xml` | CCEL's ThML, untouched ([ccel.org/ccel/o/owen/deathofdeath.xml](https://www.ccel.org/ccel/o/owen/deathofdeath.xml)): the provenance |
| `source/the-death-of-death.tei.xml` | enriched TEI edition: the CCEL text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/SOURCES.md` | the sources and witnesses, and the editor's rules for the collation |
| `source/review-report.md` | the editor decisions |
| `source/collation/` | the collation against the 1648 first edition, Book by Book: every finding (`*.jsonl`), those held for the editor (`*.held.jsonl`), and the script that applies them |
| `source/ocr/` | local OCR of the 1648 edition and of Goold's printing (raw bundles git-ignored; see `source/SOURCES.md`) |

The text is CCEL's, which is Goold's (*The Works of John Owen*, vol. 10,
1850–53), with his page breaks kept in the TEI. Owen's own wording, from the
1648 first edition, is restored where Goold departed from it: chiefly his
quotations of Scripture, which Goold brought to the King James Version, and
words in his prose. Goold's corrections of the 1648 printer's misprints, his
corrected classical quotations and his light modernizing ("namely" for
"viz.") stand. Owen's scheme of the senses of "world" (Book IV, chapter I),
a brace diagram in 1648, is set as an outline. Goold's prefatory note and
analysis are not part of this edition (they stay in `deathofdeath.thml.xml`),
nor are CCEL's indexes.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync death      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find death WORD # every place a word is, in CCEL and as decided
$ ./fgb page death      # the side-by-side page (CCEL | edition)
$ ./fgb check death     # verify
$ ./fgb build death     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build death` makes them in
`dist/john-owen/the-death-of-death/`.
