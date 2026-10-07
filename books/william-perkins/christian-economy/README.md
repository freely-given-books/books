# Christian Economy — William Perkins

*Christian Oeconomie: or, A Short Survey of the Right Manner of Erecting and
Ordering a Family, According to the Scriptures* (1609), translated out of the
Latin by Thomas Pickering.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/dedication.typ` | Pickering's epistle dedicatory to Lord Rich |
| `chapters/typ/chapter-01.typ` … `chapter-18.typ` | one file per chapter of the treatise |
| `christian-economy.typ` | print edition (imports the `fgbooks` template) |
| `ebook-front.html` | ebook front matter (title page, licence, epigraph) |
| `ebook-christian-economy.typ` | earlier ebook source (Typst HTML export + Calibre), superseded by `ebook-front.html` + the TEI |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `cover.typ` | print wrap cover, from the shared `scripts/panel_cover.typ` design |
| `sources/dedication.typ`, `sources/treatise.typ` | original-spelling render, kept for reference |
| `sources/dedication_modern.typ`, `sources/treatise_modern.typ` | modernized render the chapters were split from |
| `sources/*.py`, `sources/CLAUDE.md` | the first-pass converter and its notes (provenance) |
| `source/A09377.tcp.xml` | untouched EEBO-TCP transcription of the 1609 printing (provenance) |
| `source/christian-economy.tei.xml` | enriched TEI edition: the 1609 text plus every editorial decision inline |
| `source/review-report.md` | review decisions carried from `chapters/typ` into the TEI |

The scripts in `sources/` are the first-pass converters, superseded by
`colophon/` at the repo root. See `source/README.md` for extracting either
spelling from the TEI and for rebuilding it after further review.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync perkins      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find perkins WORD # every place a word is, as printed and as decided
$ ./fgb page perkins      # the side-by-side page
$ ./fgb check perkins     # verify
$ ./fgb epub perkins      # the EPUB, checked with epubcheck
$ ./fgb pdf perkins       # the print PDF
```

The long forms below do the same.

## Steps for Generation

The PDFs and the EPUB are not kept in git: they are built from the
repository, reproducibly. `./fgb build perkins` makes all of them in
`dist/william-perkins/christian-economy/` (print PDF, cover wrap, the
cover's front panel as an image, checked EPUB); the long forms follow.

### ebook

The EPUB 3 is built straight from the TEI by `colophon/tei_epub.py`: one
file per chapter, notes as pop-up footnotes (shown after the chapter on
readers without pop-ups), Greek and Hebrew language-tagged.

``` sh
$ python3 ../../../colophon/tei_epub.py source/christian-economy.tei.xml christian-economy.epub \
        --title "Christian Economy" --author "William Perkins" \
        --front ebook-front.html --cover cover-front.png \
        --css ../../resources/css/ebook.css --css ebook-override.css
$ epubcheck christian-economy.epub   # 0 errors, 0 warnings
```

### side-by-side reading copy

The 1609 text next to the edition, block by block, with every editorial
change marked (hover a word to see the printed reading, the machine's and
the editor's). It is read-only: edit `chapters/typ`, rebuild the TEI, then
regenerate it. It is git-ignored.

``` sh
$ python3 ../../../colophon/tei_review.py source/christian-economy.tei.xml side-by-side.html
```

### pdf

``` sh
$ typst compile christian-economy.typ christian-economy.pdf
```

### cover

`cover.typ` calls `scripts/panel_cover.typ`.

Because the import reaches above this directory, the compile needs a `--root`.

``` sh
$ typst compile --root ../../../ cover.typ cover.pdf
$ typst compile --root ../../../ --input front-only=true --format png --ppi 150 \
        cover.typ cover-front.png
```

The second command renders the front panel alone, at the trim size: the
ebook cover (the `EPUB` setting's `cover` names `cover.typ`, so `./fgb`
does this itself) and a picture for the web.
