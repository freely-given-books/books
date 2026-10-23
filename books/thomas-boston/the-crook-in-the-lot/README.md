# The Crook in the Lot — Thomas Boston

*The Crook in the Lot: or, The Sovereignty and Wisdom of God, in the
Afflictions of Men, Displayed; together with a Christian Deportment under
Them. Being the Substance of Several Sermons on Eccles. vii. 13, Prov. xvi.
19, and 1 Pet. v. 6* (Edinburgh, 1737, five years after Boston's death).
Puritan Paperbacks #5, here in full.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/to-the-reader.typ` | the publishers' preface of the first edition |
| `chapters/typ/part-1.typ` | Part I, on Eccles. 7:13, with its three doctrines |
| `chapters/typ/part-2.typ` | Part II, on Prov. 16:19 |
| `chapters/typ/part-3.typ` | Part III, on 1 Pet. 5:6, with its two doctrines |
| `the-crook-in-the-lot.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/plate_cover.typ`, in Boston's heather); its front panel is the ebook cover |
| `art/plate.png` | the cover's engraving (the Ettrick hills at dawn, a shepherd's crook), printed in heather |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/crook.thml.xml` | our transcription of M'Millan's edition (1848), as ThML: the provenance |
| `source/crook.ccel.witness.xml` | witness: CCEL's ThML, untouched ([ccel.org/ccel/b/boston/crook.xml](https://www.ccel.org/ccel/b/boston/crook.xml)), a modernized revision |
| `source/the-crook-in-the-lot.tei.xml` | enriched TEI edition: the transcription plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/SOURCES.md` | where the text comes from and how it was transcribed |

There is no EEBO-TCP or ECCO-TCP text of this book, and CCEL's is a
modernized revision (*you* for *thou*, *has* for *hath*, verse references
dropped) with many spell-checker slips ("light of the world" for "light of
the word", "savvy name" for "savoury name"). The text here is Samuel
M'Millan's, from his edition of Boston's *Whole Works* (vol. 3, Aberdeen,
1848, "reprinted without abridgment"), transcribed from two scans of it and
checked against the page images; see `source/SOURCES.md`. The titles of the
three parts are this edition's: M'Millan heads each with its text only.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync crook      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find crook WORD # every place a word is, as transcribed and as decided
$ ./fgb page crook      # the side-by-side page (M'Millan | edition)
$ ./fgb check crook     # verify
$ ./fgb build crook     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build crook` makes them in
`dist/thomas-boston/the-crook-in-the-lot/`.
