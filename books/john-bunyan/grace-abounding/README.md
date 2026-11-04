# Grace Abounding to the Chief of Sinners — John Bunyan

*Grace Abounding to the Chief of Sinners: or, a Brief Relation of the
Exceeding Mercy of God in Christ, to His Poor Servant John Bunyan* (first
published 1666; enlarged by Bunyan up to the sixth edition, 1688).

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/preface.typ` | Bunyan's preface to his "children" |
| `chapters/typ/relation.typ` | the relation itself, in Bunyan's numbered paragraphs |
| `chapters/typ/call-to-the-ministry.typ` | his call to the work of the ministry |
| `chapters/typ/imprisonment.typ` | his imprisonment |
| `chapters/typ/conclusion.typ` | the conclusion |
| `grace-abounding.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/panel_cover.typ`, ochre); its front panel is the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/grace-abounding-1688.tcp.xml` | **the source**: our transcription (CC0) of the sixth edition (London: Nath. Ponder, 1688), the last in Bunyan's lifetime, as printed (spelling, section numbers, italics, page breaks); `source/transcription-report.md` says how it was made |
| `source/transcription/` | the scripts that made it from the Kraken OCR and the witnesses, and the reading text's decisions (`apply_1688.py`) |
| `source/grace-abounding.tei.xml` | enriched TEI edition: the 1688 text plus every editorial decision inline |
| `source/editorial.py` | the book's settings |
| `source/review-report.md` | the editor decisions (the reading text against the 1688 print) |
| `source/grace.ccel.witness.xml` | witness: CCEL's ThML ([ccel.org/ccel/b/bunyan/grace.xml](https://www.ccel.org/ccel/b/bunyan/grace.xml)), a later printing's text, the previous edition's source |
| `source/A30143.witness.xml` | witness: the 1666 first edition, EEBO-TCP [A30143](https://github.com/textcreationpartnership/A30143), untouched; the text of the passages 1688 cut |
| `source/witness-report.md` | the previous edition's collations (1666, 1688 OCR, RTS 1905) and the editor's rule of 2026-10-26 |
| `source/ocr/` | the 1688 GLM-OCR and Tesseract witnesses; the raw bundle (`ocr-witnesses/`) is not in git |

The text is the 1688 sixth edition, newly transcribed from the page images
(2026-11-01): Kraken OCR of every page, corrected where six witnesses outvote
it, every disagreement read on the page image. The reading text keeps the
editor's rule of 2026-10-26: Bunyan's 1688 wording in modern spelling; the
passages 1688 cut kept from 1666 (the five the rule names, and two more);
period grammar and old words with a clean modern equivalent modern; and the
1688 italics (the editor, 2026-11-01: they meant something then). The
section numbers are the standard ones; the 1688 layer keeps the print's
(which skip 73 and give 285 twice).

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync grace-abounding      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find grace-abounding WORD # every place a word is, in CCEL and as decided
$ ./fgb page grace-abounding      # the side-by-side page (CCEL | edition)
$ ./fgb check grace-abounding     # verify
$ ./fgb build grace-abounding     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build grace-abounding`
makes them in `dist/john-bunyan/grace-abounding/`.
