# All of Grace — Charles Spurgeon

*All of Grace: An Earnest Word with Those Who Are Seeking Salvation by the
Lord Jesus Christ* (1886).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/chapter-01.typ` … `chapter-20.typ` | one file per chapter (extracted from the TEI) |
| `all-of-grace.typ` | print edition (imports the `@local/fgbooks` template) |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-all-of-grace.typ` | earlier ebook source (Typst HTML export + Calibre), superseded by `ebook-front.html` + the TEI |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `cover_front.jpg` | the ebook cover (designed outside this repository, so kept as a source) |
| `source/grace.thml.xml` | CCEL's ThML, untouched ([ccel.org/ccel/s/spurgeon/grace.xml](https://www.ccel.org/ccel/s/spurgeon/grace.xml)): the provenance |
| `source/all-of-grace.tei.xml` | enriched TEI edition: the CCEL text plus every editorial decision inline |
| `source/editorial.py` | the book's settings (modern text: no spelling pass; quotes curled, dashes spaced) |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |

The edition differs from CCEL in about 160 recorded decisions: American
spelling (Savior, offense, marvelous), headings in title case, the opening
words of chapters in capitals, hymn stanzas run together and scripture set as
quotations, two typos (mutrition, wordly), and "Cor." written out.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync spurgeon      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find spurgeon WORD # every place a word is, in CCEL and as decided
$ ./fgb page spurgeon      # the side-by-side page (CCEL | edition)
$ ./fgb check spurgeon     # verify
$ ./fgb build spurgeon     # print PDF and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build spurgeon` makes them
in `dist/charles-spurgeon/all-of-grace/`.

`chapter-20.typ` centres its three closing appeals with `#align(center)`;
that is layout, not stored in the TEI, so `./fgb check` lists the file as
differing only by those lines.
