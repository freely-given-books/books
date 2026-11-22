# True Grace, Distinguished from the Experience of Devils — Jonathan Edwards

Edwards's sermon on James 2:19, preached before the Synod of New York at Newark, New Jersey,
September 28, 1752, and printed at the Synod's desire (New York: James Parker, 1753). In modern
spelling from Evans-TCP N05520; a small book at the trim of *Sinners* (4.25 × 6.875in).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/sermon.typ` | the sermon; its IMPROVEMENT a heading |
| `true-grace-distinguished.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the Lulu cover wrap on `scripts/plate_cover.typ`: the day-star over dark hills before dawn, drawn in Typst |
| `ebook-front.html` | ebook front matter |
| `source/N05520.tcp.xml` | Evans-TCP [N05520](https://github.com/textcreationpartnership/N05520), untouched (also Sinners' source) |
| `source/true-grace-distinguished.tei.xml` | enriched TEI edition: the printed text plus every editorial decision inline |
| `source/editorial.py`, `source/nouns.py`, `source/outline.json` | the book's settings, its lowercased nouns, its outline levels |
| `source/review-report.md`, `source/proofread-report.md` | the editor decisions carried into the TEI; the proofread |
| `source/SOURCES.md` | the printing and witnesses used |

The working files (the Leeds 1806 scan, the close reads, the edit scripts) are in
`~/Projects/fgbooks/work/true-grace/`.

## Everyday commands

``` sh
$ ./fgb sync true-grace      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb check true-grace     # verify
$ ./fgb build true-grace     # print PDF and checked EPUB into dist/
```
