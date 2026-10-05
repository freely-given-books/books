# The Gospel Minister's Maintenance Vindicated — Benjamin Keach

*The Gospel Minister's Maintenance Vindicated. Wherein, a Regular Ministry in
the Churches, is First Asserted, and the Objections Against a Gospel
Maintenance for Ministers, Answered* (London: John Harris, 1689; Wing K711A).

Wing and EEBO-TCP catalogue the book under Hanserd Knollys, whose name heads
the eleven London elders who signed its recommendation (Keach among them).
The treatise is Benjamin Keach's, and this edition gives it to him; the
foreword says why. The TEI header names Keach (`AUTHOR` in
`source/editorial.py`) and keeps the catalogue attribution in `sourceDesc`.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/foreword.typ` | this edition's foreword (not in the TEI) |
| `chapters/typ/recommendation.typ` | the elders' recommendation "To the Congregations of Baptized Believers" |
| `chapters/typ/chapter-01.typ` … `chapter-04.typ` | the four parts of the treatise |
| `the-gospel-ministers-maintenance-vindicated.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/panel_cover.typ`, midnight); its front panel is the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/A47561.tcp.xml` | EEBO-TCP [A47561](https://github.com/textcreationpartnership/A47561), untouched: the provenance |
| `source/the-gospel-ministers-maintenance-vindicated.tei.xml` | enriched TEI edition: the 1689 text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/gap_fixes.py` | the illegible print filled in, with the evidence for each |
| `source/review-report.md` | the editor decisions |

The title page, the printed contents, the errata page and the publisher's
Advertisement (on the 38th of the Thirty-Nine Articles) are in the TEI as
printed but not in this edition. The errata are made in the text as editor
decisions.

Page images: the same microfilm, in grayscale, on archive.org
([bim_early-english-books-1641-1700_the-gospel-ministers-ma_knollys-hanserd_1689](https://archive.org/details/bim_early-english-books-1641-1700_the-gospel-ministers-ma_knollys-hanserd_1689));
scan `n` = printed page + 13 for the first hundred pages (+15 by p. 121).

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync gospel-minister      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find gospel-minister WORD # every place a word is, as printed and as decided
$ ./fgb page gospel-minister      # the side-by-side page (1689 | edition)
$ ./fgb check gospel-minister     # verify
$ ./fgb build gospel-minister     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build gospel-minister`
makes them in `dist/benjamin-keach/the-gospel-ministers-maintenance-vindicated/`.
