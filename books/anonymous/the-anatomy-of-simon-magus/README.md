# The Anatomy of Simon Magus — Anonymous, 1700

*The Anatomy of Simon Magus, or, The Sin of Simony Laid Open* (London,
Charles Brome, 1700), EEBO-TCP `A25330`, with a modern foreword and an
abbreviations guide.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/chapter-01.typ` … `chapter-08.typ` | the eight chapters (modernized); extracted from the TEI, still the place to edit |
| `chapters/typ/foreword.typ`, `abbreviations.typ` | modern matter, not in the 1700 text and not in the TEI |
| `common.typ` | the `#chapter[long][short]` heading macro (short title for running heads) |
| `the-anatomy-of-simon-magus.typ` | print edition (imports the `fgbooks` template) |
| `ebook-front.html`, `ebook-appendix.html` | ebook title page and appendix divider |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `ebook-the-anatomy-of-simon-magus.typ` | earlier ebook source (Typst HTML + pandoc + Calibre), superseded by the TEI build |
| `source/` | the TCP transcription, the enriched TEI and its tables; see `source/README.md` |

## Steps for Generation

### ebook

The EPUB 3 is built from the TEI by `scripts/tei/tei_epub.py`; the foreword
and the abbreviations guide are rendered from their Typst files.

``` sh
$ python3 ../../../scripts/tei/tei_epub.py source/the-anatomy-of-simon-magus.tei.xml \
        the-anatomy-of-simon-magus.epub \
        --title "The Anatomy of Simon Magus" --author "Anonymous" \
        --front ebook-front.html --cover cover_front.jpg \
        --before chapters/typ/foreword.typ \
        --after ebook-appendix.html --after chapters/typ/abbreviations.typ \
        --css ../../resources/css/ebook.css --css ebook-override.css
$ epubcheck the-anatomy-of-simon-magus.epub   # 0 errors, 0 warnings
```

### pdf

``` sh
typst compile the-anatomy-of-simon-magus.typ the-anatomy-of-simon-magus.pdf
```

### after editing a chapter

Rebuild the TEI so it keeps up with `chapters/typ`, then check:

``` sh
$ cd source
$ python3 ../../../../scripts/tei/build_tei.py A25330.tcp.xml the-anatomy-of-simon-magus.tei.xml \
        --review ../chapters/typ --report review-report.md
$ cd ../../../.. && python3 scripts/tei/verify.py books/anonymous/the-anatomy-of-simon-magus
```

### side-by-side reading copy

The 1700 text next to the edition, block by block, with every editorial
change marked (hover a word to see the printed reading, the machine's and
the editor's), with the foreword and appendix in the edition column. It is read-only: edit `chapters/typ`, rebuild the TEI as
above, then regenerate it. It is git-ignored.

``` sh
$ python3 ../../../scripts/tei/tei_review.py source/the-anatomy-of-simon-magus.tei.xml side-by-side.html \
        --before chapters/typ/foreword.typ \
        --after ebook-appendix.html --after chapters/typ/abbreviations.typ
```
