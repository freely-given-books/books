# Steps for Generation

## ebook

``` sh
$ typst compile --features html ebook-the-anatomy-of-simon-magus.typ -f html
$ pandoc ebook-the-anatomy-of-simon-magus.html -o ebook-the-anatomy-of-simon-magus.xhtml
$ ebook-convert ebook-the-anatomy-of-simon-magus.xhtml the-anatomy-of-simon-magus.epub \
        --authors "Anonymous" \
        --title "The Anatomy of Simon Magus" \
        --cover cover_front.jpg \
        --extra-css ../../resources/css/ebook.css \
        --extra-css ebook-override.css \
        --epub-version 3 \
        --level1-toc '//h:h2' \
        --level2-toc '//h:h3'
```

## pdf

``` sh
typst compile the-anatomy-of-simon-magus.typ the-anatomy-of-simon-magus.pdf
```
