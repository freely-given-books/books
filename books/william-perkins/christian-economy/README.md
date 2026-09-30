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
| `ebook-christian-economy.typ` | earlier ebook source (Typst HTML export), superseded by `ebook-front.html` + the TEI |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `cover.typ` | print wrap cover, from the shared `scripts/panel_cover.typ` design |
| `sources/dedication.typ`, `sources/treatise.typ` | original-spelling render, kept for reference |
| `sources/dedication_modern.typ`, `sources/treatise_modern.typ` | modernized render the chapters were split from |
| `source/A09377.tcp.xml` | untouched EEBO-TCP transcription of the 1609 printing (provenance) |
| `source/christian-economy.tei.xml` | enriched TEI edition: the 1609 text plus every editorial decision inline |
| `source/review-report.md` | review decisions carried from `chapters/typ` into the TEI |

The scripts in `sources/` are the first-pass converters, superseded by
`scripts/tei/` at the repo root. See `source/README.md` for extracting either
spelling from the TEI and for rebuilding it after further review.

## Steps for Generation

### ebook

The ebook text comes straight from the TEI (`scripts/tei/tei_to_html.py`):
each chapter keeps its own notes, and Greek and Hebrew are language-tagged.

``` sh
$ python3 ../../../scripts/tei/tei_to_html.py source/christian-economy.tei.xml \
        ebook-christian-economy.html --front ebook-front.html --title "Christian Economy"
$ ebook-convert ebook-christian-economy.html christian-economy.epub \
        --authors "William Perkins" \
        --title "Christian Economy" \
        --cover cover_front.jpg \
        --extra-css ../../resources/css/ebook.css \
        --extra-css ebook-override.css \
        --epub-version 2 \
        --level1-toc '//h:h3'
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
$ magick -density 300 "cover.pdf[0]" -background white -alpha remove \
        -crop 1650x2550+1785+37 +repage -resize 825x1275 -quality 92 cover_front.jpg
```

The second command cuts the front panel out of the wrap for the ebook cover;
its offsets are `bleed + trim + spine` across and `bleed` down, at 300 dpi, so
they move if the page count does.
