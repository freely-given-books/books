# Religious Affections — Jonathan Edwards

*A Treatise Concerning Religious Affections, in Three Parts* (Boston, 1746),
the first edition, in modern spelling. Edwards made no later revision. Set
6 × 9in at 10.5pt because of the book's length (the editor, 2026-11-11).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/preface.typ` | Edwards's preface |
| `chapters/typ/part-1/` | Part I: the text (1 Pet 1:8) and the doctrine, what the affections are, religion in the affections, inferences |
| `chapters/typ/part-2/sign-01…12.typ` | Part II: twelve things that are no signs either way |
| `chapters/typ/part-3/` | Part III: the introduction and the twelve distinguishing signs |
| `religious-affections.typ` | print edition, 6 × 9in (imports the `@local/fgbooks` template) |
| `cover.typ` | the Lulu cover wrap on `scripts/plate_cover.typ`: 1 Peter 1:8 in gold |
| `ebook-front.html` | ebook front matter |
| `source/N04635.tcp.xml` | Evans-TCP [N04635](https://github.com/textcreationpartnership/N04635), untouched |
| `source/N04635.supplied.xml` | corrections to the TCP, each read on the 1746 page images |
| `source/gap_fixes.py` | the TCP's illegible letters and words, filled from the 1746 scan |
| `source/nouns.py` | the common nouns lowercased in the reading text |
| `source/outline.json` | the outline levels (I. › 1. › (1.) › [1.]) |
| `source/religious-affections.tei.xml` | enriched TEI edition: the printed text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |
| `source/SOURCES.md` | the printings and scans used |

The text was collated with local OCR of the 1746 and 1768 printings; the
1746 errata page ("ERRORS to be corrected") is applied as editor's
readings, and the TCP's own printing of the errata, index and booksellers'
notice is kept in the TEI but not printed. The working scripts (gap fills,
collation, case, spelling, errata) are in `~/Projects/fgbooks/work/religious-affections/`,
run in order by its `rebuild.sh`.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync religious-affections      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find religious-affections WORD # every place a word is, as printed and as decided
$ ./fgb page religious-affections      # the side-by-side page (printed | edition)
$ ./fgb check religious-affections     # verify
$ ./fgb build religious-affections     # print PDF and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build religious-affections` makes them
in `dist/jonathan-edwards/religious-affections/`.
