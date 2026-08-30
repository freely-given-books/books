# Steps for Generation

## ebook

``` sh
$ typst compile --features html ebook-the-secret-key-of-heaven.typ -f html
$ pandoc ebook-the-secret-key-of-heaven.html -o ebook-the-secret-key-of-heaven.xhtml
$ ebook-convert ebook-the-secret-key-of-heaven.xhtml the-secret-key-of-heaven.epub \
        --authors "Thomas Brooks" \
        --title "The Secret Key of Heaven" \
        --cover cover_front.jpg \
        --extra-css ../../resources/css/ebook.css \
        --extra-css ebook-override.css \
        --epub-version 2 \
        --level1-toc '//h:h2' \
        --level2-toc '//h:h3' \
        --level3-toc '//h:h4'
```

## pdf

``` sh
typst compile the-secret-key-of-heaven.typ the-secret-key-of-heaven.pdf
```
