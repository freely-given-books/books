# A Divine and Supernatural Light — Jonathan Edwards

Edwards's sermon on Matt 16:17, preached at Northampton and published in Boston in 1734 "at the
desire of some of the hearers", with his preface to the people of his church. In modern spelling
from Evans-TCP N03122; a small book at the trim of *Sinners* and *God Glorified* (4.25 × 6.875in).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/preface.typ` | Edwards's preface |
| `chapters/typ/sermon.typ` | the sermon; the four parts he announces as edition headings |
| `a-divine-and-supernatural-light.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the Lulu cover wrap on `scripts/plate_cover.typ`: a honeycomb drawn in Typst (the sermon's honey) |
| `ebook-front.html` | ebook front matter |
| `source/N03122.tcp.xml` | Evans-TCP [N03122](https://github.com/textcreationpartnership/N03122), untouched |
| `source/a-divine-and-supernatural-light.tei.xml` | enriched TEI edition: the printed text plus every editorial decision inline |
| `source/editorial.py`, `source/nouns.py`, `source/outline.json` | the book's settings (gap fills among them), its lowercased nouns, its outline levels |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |
| `source/SOURCES.md` | the printing and witnesses used |

The working files (page images, the two reads, the review scripts) are in
`~/Projects/fgbooks/work/divine-and-supernatural-light/`.

## Everyday commands

``` sh
$ ./fgb sync supernatural      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb check supernatural     # verify
$ ./fgb build supernatural     # print PDF and checked EPUB into dist/
```
