# God Glorified in Man's Dependence — Jonathan Edwards

Edwards's first published sermon, on 1 Cor 1:29-31, preached on the public lecture in Boston,
July 8, 1731, with the preface "To the Reader" by Thomas Prince and William Cooper. In modern
spelling from Evans-TCP N02859; a small book at the trim of *Sinners* (4.25 × 6.875in).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/to-the-reader.typ` | the ministers' preface |
| `chapters/typ/sermon.typ` | the sermon; its USE a heading |
| `god-glorified-in-mans-dependence.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the Lulu cover wrap on `scripts/plate_cover.typ`: 1 Cor 1:31 in the title's type |
| `ebook-front.html` | ebook front matter |
| `source/N02859.tcp.xml` | Evans-TCP [N02859](https://github.com/textcreationpartnership/N02859), untouched |
| `source/god-glorified-in-mans-dependence.tei.xml` | enriched TEI edition: the printed text plus every editorial decision inline |
| `source/editorial.py`, `source/nouns.py`, `source/outline.json` | the book's settings, its lowercased nouns, its outline levels |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |
| `source/SOURCES.md` | the printing and witness used |

The working scripts (casing, spelling) are in `~/Projects/fgbooks/work/god-glorified/`.

## Everyday commands

``` sh
$ ./fgb sync god-glorified      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb check god-glorified     # verify
$ ./fgb build god-glorified     # print PDF and checked EPUB into dist/
```
