# Steps for Generation

## ebook

``` sh
$ typst compile --features html ebook-all-of-grace.typ -f html
$ pandoc ebook-all-of-grace.html -o ebook-all-of-grace.xhtml
$ ebook-convert ebook-all-of-grace.xhtml all-of-grace.epub \
        --authors "Charles Spurgeon" \
        --title "All of Grace" \
        --cover cover_front.jpg \
        --extra-css ../../resources/css/ebook.css \
        --extra-css ebook-override.css \
        --epub-version 3 \
        --level1-toc '//h:h3'
```

## pdf

``` sh
typst compile all-of-grace.typ all-of-grace.pdf
```
