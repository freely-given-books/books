# The Anatomy of Simon Magus — Anonymous, 1700

*The Anatomy of Simon Magus, or, The Sin of Simony Laid Open* (London,
Charles Brome, 1700), EEBO-TCP `A25330`, with a modern foreword and an
abbreviations guide.

## Corrections to the 1700 text

Besides spelling and punctuation, the edition corrects two slips of the
author's: chapter 2 has "John the Seer" for the seer who rebuked
Jehoshaphat (2 Chron 19:2), now "Jehu the Seer", and "Apollo" for Apollos
(Acts 18:24-27). The end of chapter 6, lost from the earlier edition, is
restored from the 1700 printing.

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

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync simon      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find simon WORD # every place a word is, as printed and as decided
$ ./fgb page simon      # the side-by-side page
$ ./fgb check simon     # verify
$ ./fgb epub simon      # the EPUB, checked with epubcheck
$ ./fgb pdf simon       # the print PDF
```

The long forms below do the same.

## Steps for Generation

The PDF and the EPUB are not kept in git: `./fgb build simon` makes them in
`dist/anonymous/the-anatomy-of-simon-magus/`. The cover was designed outside
this repository, so its front, `cover_front.jpg`, is kept here as a source
(the EPUB needs it at build time); the full print wrap for Lulu,
`full_cover_lulu.pdf`, is a print file kept with the published PDFs, not in git.

### ebook

The EPUB 3 is built from the TEI by `colophon/tei_epub.py`; the foreword
and the abbreviations guide are rendered from their Typst files.

``` sh
$ python3 ../../../colophon/tei_epub.py source/the-anatomy-of-simon-magus.tei.xml \
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
$ python3 ../../../../colophon/build_tei.py A25330.tcp.xml the-anatomy-of-simon-magus.tei.xml \
        --review ../chapters/typ --report review-report.md
$ cd ../../../.. && python3 colophon/verify.py books/anonymous/the-anatomy-of-simon-magus
```

### side-by-side reading copy

The 1700 text next to the edition, block by block, with every editorial
change marked (hover a word to see the printed reading, the machine's and
the editor's), with the foreword and appendix in the edition column. It is read-only: edit `chapters/typ`, rebuild the TEI as
above, then regenerate it. It is git-ignored.

``` sh
$ python3 ../../../colophon/tei_review.py source/the-anatomy-of-simon-magus.tei.xml side-by-side.html \
        --before chapters/typ/foreword.typ \
        --after ebook-appendix.html --after chapters/typ/abbreviations.typ
```
