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
| `ebook-christian-economy.typ` | ebook edition (Typst HTML export) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `cover.typ` | print wrap cover, from the shared `scripts/panel_cover.typ` design |
| `dedication.typ`, `treatise.typ` | original-spelling render, kept for reference |
| `dedication_modern.typ`, `treatise_modern.typ` | modernized render the chapters were split from |

## Steps for Generation

### ebook

``` sh
$ typst compile --features html ebook-christian-economy.typ -f html
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
