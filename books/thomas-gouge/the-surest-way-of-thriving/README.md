# The Surest and Safest Way of Thriving — Thomas Gouge

*The Surest & Safest Way of Thriving, or, A Conviction of That Grand Mistake in Many, That What
Is Given to the Poor Is a Loss to Their Estate* (London, 1673), on Matt 10:41-42, in modern
spelling from EEBO-TCP A41657. Thomas Gouge (1605-1681) was William Gouge's son.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/ch01-…ch14-*.typ` | the treatise in fourteen chapters, cut at Gouge's own turns (the text opened, the doctrines, proofs, testimonies, examples, reasons, uses, directions, means, a word for the ministers, the application) |
| `the-surest-way-of-thriving.typ` | print edition, 5.5 × 8.5in (imports the `@local/fgbooks` template) |
| `cover.typ` | the Lulu cover wrap on `scripts/plate_cover.typ`: Prov 19:17 in the title's type |
| `ebook-front.html` | ebook front matter |
| `source/A41657.tcp.xml` | EEBO-TCP [A41657](https://github.com/textcreationpartnership/A41657), untouched |
| `source/the-surest-way-of-thriving.tei.xml` | enriched TEI edition: the printed text plus every editorial decision inline |
| `source/editorial.py`, `nouns.py`, `gap_fixes.py`, `outline.json` | the book's settings, lowercased nouns, the TCP's gaps (Greek read from the 1676 printing), outline levels |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |
| `source/SOURCES.md` | the printings used |

The working scripts (casing, spelling, hand edits) are in `~/Projects/fgbooks/work/surest-way/`,
run in order by its `rebuild.sh`.

## Everyday commands

``` sh
$ ./fgb check surest-way     # verify
$ ./fgb build surest-way     # print PDF and checked EPUB into dist/
```
