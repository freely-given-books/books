# Steps for Generation

## ebook

``` sh
$ typst compile --features html ebook-the-pilgrims-progress.typ -f html
$ pandoc ebook-the-pilgrims-progress.html -o ebook-the-pilgrims-progress.xhtml
$ ebook-convert ebook-the-pilgrims-progress.xhtml the-pilgrims-progress.epub \
          --authors "John Bunyan" \
          --title "The Pilgrim's Progress" \
          --cover cover_front.jpg \
          --extra-css ../../resources/css/ebook.css \
          --extra-css ebook-override.css \
          --epub-version 3 \
          --level1-toc '//h:h2' \
          --level2-toc '//h:h3'
```

## pdf

``` sh
typst compile the-pilgrims-progress.typ the-pilgrims-progress.pdf
```
