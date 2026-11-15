# The Mortification of Sin — John Owen

*Of the Mortification of Sin in Believers: the Necessity, Nature, and Means
of It; with a Resolution of Sundry Cases of Conscience Thereunto Belonging*
(first published 1656; the second edition 1668). Puritan Paperbacks #48,
here in full.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/preface.typ` | Owen's preface to the Christian reader |
| `chapters/typ/chapter-01.typ` … `chapter-14.typ` | the fourteen chapters, each opening with Owen's summary of it |
| `the-mortification-of-sin.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the cover wrap (`scripts/plate_cover.typ`, no picture: Romans 8:13 in oxblood and gold); its front is the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/A53715.tcp.xml` | the 1668 second edition, EEBO-TCP [A53715](https://github.com/textcreationpartnership/A53715), untouched: the text |
| `source/A53715.supplied.xml` | the transcription's keying slips, corrected to the 1668 page |
| `source/gap_fixes.py` | every illegible letter and the Greek, read from the 1668 page |
| `source/mort.ccel.witness.xml` | witness: Goold's text, CCEL's ThML ([ccel.org/ccel/o/owen/mort.xml](https://www.ccel.org/ccel/o/owen/mort.xml)), untouched |
| `source/outline.json` | the outline levels (Goold as witness) |
| `source/the-mortification-of-sin.tei.xml` | enriched TEI edition: the 1668 text plus every editorial decision inline |
| `chapters/modern/`, `the-mortification-of-sin-modern.typ`, `cover-modern.typ`, `ebook-front-modern.html` | the Modern English edition (`MODERN-ENGLISH-RULES.md`) |
| `source/editorial.py` | the book's settings |
| `source/review-report.md` | the editor decisions |

The text is Owen's second edition (London, 1668), the last in his lifetime, as EEBO-TCP A53715
transcribes it: its gaps restored from the 1668 page images, the transcription's slips corrected to
the page, and the print's own misprints and reference slips corrected in the reading text, Goold's
text (1850–53) agreeing (the editor, 2026-11-14: "I want the classic to stick close to the
original"). Until then the edition was Goold's text from CCEL. The work is in
`work/mortification-1668/`.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync the-mortification-of-sin      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find the-mortification-of-sin WORD # every place a word is, as printed and as decided
$ ./fgb page the-mortification-of-sin      # the side-by-side page (1668 | edition)
$ ./fgb check the-mortification-of-sin     # verify
$ ./fgb build the-mortification-of-sin     # print PDF, cover and checked EPUB into dist/
```

The PDF and the EPUB are not kept in git: `./fgb build the-mortification-of-sin`
makes them in `dist/john-owen/the-mortification-of-sin/`.
