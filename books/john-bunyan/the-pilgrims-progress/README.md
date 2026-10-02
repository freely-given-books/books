# The Pilgrim's Progress — John Bunyan

*The Pilgrim's Progress from This World to That Which is to Come; Delivered
under the Similitude of a Dream*, Parts I (1678) and II (1684).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/apology.typ` | The Author's Apology for his Book |
| `chapters/typ/part-1/stage-01.typ` … `stage-10.typ`, `conclusion.typ` | Part I (extracted from the TEI) |
| `chapters/typ/part-2/title.typ`, `authors-way.typ`, `to-the-reader.typ`, `stage-01.typ` … `stage-08.typ` | Part II |
| `the-pilgrims-progress.typ` | print edition (imports the `@local/fgbooks` template) |
| `ebook-front.html` | ebook front matter (licence) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `cover.typ` | the cover, in the imprint's panel design (`scripts/panel_cover.typ`, palette `ochre`); its front panel is the ebook cover, rendered at build time |
| `source/pilgrim.thml.xml` | CCEL's ThML, untouched ([ccel.org/ccel/b/bunyan/pilgrim.xml](https://www.ccel.org/ccel/b/bunyan/pilgrim.xml); Logos's text of the 1853 Auburn edition): the provenance |
| `source/the-pilgrims-progress.tei.xml` | enriched TEI edition: the CCEL text plus every editorial decision inline |
| `source/editorial.py` | the book's settings (modern text; the layout into stages; verse line by line) |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |
| `source/A30170.witness.xml` | witness: the 1678 first edition of Part I, EEBO-TCP A30170, untouched |
| `source/witness-report.md` | where the witnesses differ from the edition |

The edition is CCEL's text. It departs from it in 38 recorded decisions:
three typos ("sufferet do", "scouged", "similtudes"), elisions CCEL keyed
with an opening quote (‘Tis → ’Tis), Part II's subtitle capitalized, and a
line of prose CCEL put inside a verse. Two witnesses were compared with it
(`source/witness-report.md`, made with `scripts/tei/drift.py`):

- the 1678 first edition of Part I (EEBO-TCP A30170), which lacks the
  passages Bunyan added in later editions (Mr. Worldly Wiseman, Charity,
  By-ends' friends, Lot's wife, Diffidence and others: the edition's
  Part I is about 9,400 words longer);
  there is no TCP transcription of Part II;
- the copy this book was first published from, which was CCEL's text, but
  whose book file left out the whole Tenth Stage of Part I and set the
  Apology as running prose.

Verse is set line by line: as an indented quotation in the narrative, as
plain stanzas in the sections made of verse (the Apology, the Conclusion,
the Author's Way). CCEL's small capitals (the Author's Way's "Objection" and
"answer", Part II's subtitle) are set bold.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync pilgrim       # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find pilgrim WORD  # every place a word is, in CCEL and as decided
$ ./fgb page pilgrim       # the side-by-side page (CCEL | edition)
$ ./fgb check pilgrim      # verify
$ ./fgb build pilgrim      # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build pilgrim` makes them
in `dist/john-bunyan/the-pilgrims-progress/`. `cover.typ` is set for 404
pages (spine by Lulu's formula, 0.97"); change `pages` if the count changes.
