# All of Grace — Charles Spurgeon

*All of Grace: An Earnest Word with Those Who Are Seeking Salvation by the
Lord Jesus Christ* (1886).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/chapter-01.typ` … `chapter-20.typ` | one file per chapter (extracted from the TEI) |
| `all-of-grace.typ` | print edition (imports the `@local/fgbooks` template) |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `cover.typ` | the cover, in the Common Weal Press plate design (`scripts/plate_cover.typ`): the wayside fountain of chapter 1, its cup on a chain; its front panel is the ebook cover, rendered at build time |
| `art/plate.png` | the cover's plate: an engraving made for this edition (ChatGPT, 2026-10-22), printed in the book's blue |
| `art/device-ebook.png` | the press's device, for the ebook's publisher's page |
| `source/grace.thml.xml` | our transcription (CC0) of the 1886 New York printing, as ThML: the provenance; how it was made is in `source/SOURCES.md` |
| `source/grace.ccel.witness.xml` | CCEL's ThML, untouched ([ccel.org/ccel/s/spurgeon/grace.xml](https://www.ccel.org/ccel/s/spurgeon/grace.xml)): a witness only |
| `source/ocr/` | Kraken's OCR of the 1886 scan, the transcription's base |
| `source/transcription/` | the scripts that made the transcription (vote, layout, italics, completeness) |
| `source/all-of-grace.tei.xml` | enriched TEI edition: the 1886 text plus every editorial decision inline |
| `source/editorial.py` | the book's settings (modern text: no spelling pass; quotes curled, dashes spaced) |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |

Since 2026-11-01 the text is Spurgeon's 1886 printing (Robert Carter &
Brothers, New York), transcribed from the page images (`source/SOURCES.md`).
It replaces CCEL's text, a modernized revision that rewords freely ("Listen
to a little sermon" → "This message is for you", "the Sabbath" → "Sunday")
and drops sentences and the closing paragraph. The edition keeps the 1886
wording, spelling, italics and small capitals; headings are set in title
case and Scripture references in the edition's style (Rom 8:33).

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync spurgeon      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find spurgeon WORD # every place a word is, as printed and as decided
$ ./fgb page spurgeon      # the side-by-side page (1886 print | edition)
$ ./fgb check spurgeon     # verify
$ ./fgb build spurgeon     # print PDF and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build spurgeon` makes them
in `dist/charles-spurgeon/all-of-grace/`.

`chapter-20.typ` centres its three closing appeals with `#align(center)`;
that is layout, not stored in the TEI, so `./fgb check` lists the file as
differing only by those lines.
