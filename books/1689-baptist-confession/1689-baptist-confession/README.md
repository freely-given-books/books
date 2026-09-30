# The 1689 Baptist Confession of Faith — With Catechisms

The Second London Baptist Confession of Faith (1689), bound with the Baptist
Catechism (1695) and An Orthodox Catechism (1680).

The confession paragraphs, catechism questions and Scripture proofs are not
typed into this book; they are read at compile time from the YAML files in
[symbolics-data](https://gitlab.com/svrbc/symbolics-data), a git submodule.

## Layout

| Path | What it is |
| --- | --- |
| `symbolics-data/` | submodule: `confessions/lbcf1689`, `catechisms/bc1695`, `catechisms/aoc1680` |
| `helpers.typ` | loads the YAML and renders paragraphs, questions and numbered proofs |
| `chapters/typ/preface.typ` | "Courteous Reader" preface to the confession |
| `chapters/typ/ending_statement_and_signatories.typ` | closing statement and the list of signing ministers |
| `chapters/typ/aoc_preface.typ` | preface to An Orthodox Catechism |
| `1689-baptist-confession.typ` | print edition (imports the `@local/fgbooksLBCF` template) |
| `ebook-1689-baptist-confession.typ` | ebook edition (Typst HTML export, no print template) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `cover.typ` | print wrap cover, 5.5" × 8.5" trim, 0.524" spine |
| `cover.jpg` | front cover for the ebook |

## Setup

Fetch the data submodule before the first build:

``` sh
$ git submodule update --init books/1689-baptist-confession/1689-baptist-confession/symbolics-data
```

The print edition also needs the `fgbooksLBCF` template installed as a local
Typst package at `~/.local/share/typst/packages/local/fgbooksLBCF/0.1.0/`.

## Steps for Generation

Run these from this directory.

### ebook

``` sh
$ typst compile --features html ebook-1689-baptist-confession.typ -f html
$ ebook-convert ebook-1689-baptist-confession.html 1689-baptist-confession.epub \
        --authors "Particular Baptist Churches" \
        --title "The 1689 Baptist Confession of Faith" \
        --cover cover.jpg \
        --extra-css ../../resources/css/ebook.css \
        --extra-css ebook-override.css \
        --epub-version 2 \
        --level1-toc '//h:h2' \
        --level2-toc '//h:h3'
```

The ebook can't be exported from the print file: the template draws headings
through `page()` and `layout()`, which HTML export drops, leaving an ebook with
no headings and an empty table of contents. For the same reason
`render-catechism-question` in `helpers.typ` skips its `layout()` measurement
when `target()` is `"html"`.

### pdf

``` sh
$ typst compile 1689-baptist-confession.typ 1689-baptist-confession.pdf
```

### cover

``` sh
$ typst compile cover.typ cover.pdf
```

The spine width in `cover.typ` is fixed at 0.524" for the current 210-page
interior. If the page count changes, update `spine-width` and the total
document width to match Lulu's cover template for the new count.
