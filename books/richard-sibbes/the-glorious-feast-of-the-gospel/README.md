# The Glorious Feast of the Gospel — Richard Sibbes

*The Glorious Feast of the Gospel. Or, Christ's gracious invitation and royal
entertainment of believers* (London, 1650): nine sermons on Isaiah 25:6–9,
with an epistle "To the Reader" by Arthur Jackson, James Nalton and William
Taylor.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/tothereader.typ`, `chapter1.typ` … `chapter9.typ` | To the Reader and the nine sermons, as edited |
| `the-glorious-feast-of-the-gospel.typ` | print edition (imports the `@local/fgbooks` template) |
| `full_cover.typ` | the Lulu cover wrap; its spine width follows the page count |
| `cover.jpg` | the ebook cover |
| `ebook-front.html` | ebook front matter (licence) |
| `ebook-the-glorious-feast-of-the-gospel.typ` | earlier ebook source (Typst HTML export + Calibre), superseded by `ebook-front.html` + the TEI |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/A93248.tcp.xml` | the 1650 edition as transcribed by EEBO-TCP ([A93248](https://github.com/textcreationpartnership/A93248)), untouched: the provenance |
| `source/the-glorious-feast-of-the-gospel.tei.xml` | enriched TEI edition: the 1650 text plus every editorial decision inline |
| `source/editorial.py` | the book's settings: file layout, gaps restored, ebook and print |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |
| `source/witness-report.md` | where this edition differs from both the 1650 text and Monergism's |

The edition was finished before the TEI existed. The TEI was built from it,
so its text is unchanged and every difference from the 1650 printing (about
8,200: modern spelling and case, scripture references added, "Obs."/"Use"
labels, quotations set as blocks, lists) is recorded as an editor decision.
The printed analytical table of contents and the alphabetical index are in
the TEI as printed but not in the edition.

Second witness: Monergism's PDF of the same 1650 text
([The_Glorious_Feast_of_the_Gospe_-_RIchard_Sibbes.pdf](https://www.monergism.com/thethreshold/sdg/sibbes/The_Glorious_Feast_of_the_Gospe_-_RIchard_Sibbes.pdf),
SDG reprint, © Monergism Books 2017) is a check only; none of its text is
used. It settled seven letters the 1650 print has lost.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync sibbes      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find sibbes WORD # every place a word is, as printed in 1650 and as decided
$ ./fgb page sibbes      # the side-by-side page (1650 | edition)
$ ./fgb check sibbes     # verify
$ ./fgb build sibbes     # print PDF, cover wrap and checked EPUB into dist/
```

The PDFs and the EPUB are not kept in git: `./fgb build sibbes` makes them
in `dist/richard-sibbes/the-glorious-feast-of-the-gospel/`.

`chapter3.typ` sets "There be four things in sight:" without its first-line
indent (`#par(first-line-indent: 0pt)`); that is layout, not stored in the
TEI, so `./fgb check` lists the file as differing from the extraction by that
line.
