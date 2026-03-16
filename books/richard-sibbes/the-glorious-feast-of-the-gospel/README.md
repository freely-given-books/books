# Steps for Generation


## pdf

```sh
typst compile the-glorious-feast-of-the-gospel.typ the-glorious-feast-of-the-gospel.pdf
```

## ebook


```sh
$ typst compile --features html ebook-the-glorious-feast-of-the-gospel.typ -f html
$ pandoc ebook-the-glorious-feast-of-the-gospel.html -o ebook-the-glorious-feast-of-the-gospel.xhtml
$ ebook-convert ebook-the-glorious-feast-of-the-gospel.xhtml the-glorious-feast-of-the-gospel.epub \
  --authors "Richard Sibbes" \
  --title "The Glorious Feast of the Gospel" \
  --cover cover.jpg \
  --extra-css ../../resources/css/ebook.css \
  --extra-css ebook-override.css \
  --epub-version 3 \
  --level1-toc '//h:h3'
```
