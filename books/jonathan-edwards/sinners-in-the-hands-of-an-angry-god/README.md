# Sinners in the Hands of an Angry God — Jonathan Edwards

The sermon preached at Enfield, Connecticut, July 8, 1741: a small book to
hand out, so its scripture quotations are from the Berean Standard Bible
(one KJV quotation kept on purpose, where Edwards expounds a KJV word).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/sermon.typ` | the sermon, as edited |
| `sinners-in-the-hands-of-an-angry-god.typ` | print edition, 4.25 × 6.875in (imports the `@local/fgbooks` template) |
| `cover.jpg` | the ebook cover |
| `ebook-front.html` | ebook front matter (licence, place and date, text) |
| `sinners-in-the-hands-of-an-angry-god.adoc` | earlier ebook source (asciidoctor-epub3), superseded by `ebook-front.html` + the TEI |
| `source/N05520.tcp.xml` | EEBO-TCP's Evans text [N05520](https://github.com/textcreationpartnership/N05520), untouched: Edwards's *True Grace* (New York, 1753) with the "second edition" of *Sinners* (pages 43–62) bound after it. The 1741 first edition has no TCP transcription. |
| `source/sinners-in-the-hands-of-an-angry-god.tei.xml` | enriched TEI edition: the printed text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |

The edition was finished before the TEI existed. The TEI was built from it,
so every difference from the printed sermon (about 2,000: modern spelling and
case, the BSB quotations, numbered points as lists) is recorded as an editor
decision. Restored from the printed text: the closing paragraph ("Therefore,
let every one that is out of Christ now awake…") and "several things
concerning that wrath that you are in such danger of", which the earlier copy
had lost. *True Grace* is in the TEI as printed but not in this edition.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync edwards      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find edwards WORD # every place a word is, as printed and as decided
$ ./fgb page edwards      # the side-by-side page (printed | edition)
$ ./fgb check edwards     # verify
$ ./fgb build edwards     # print PDF and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build edwards` makes them
in `dist/jonathan-edwards/sinners-in-the-hands-of-an-angry-god/`.
