# The Secret Key of Heaven — Thomas Brooks

*The Privie Key of Heaven, or, Twenty Arguments for Closet-Prayer* (London,
1665), published here as *The Secret Key of Heaven*.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/chapter-01.typ` … `chapter-03.typ` | Preface, To the Reader, Introduction |
| `chapters/typ/argument-01.typ` … `argument-20.typ` | the twenty arguments |
| `chapters/typ/application-01.typ` … `application-05.typ` | the application |
| `the-secret-key-of-heaven.typ` | print edition (imports the `@local/fgbooks` template) |
| `cover.typ` | the Lulu cover wrap; its spine width follows the page count |
| `cover_front.jpg` | the ebook cover |
| `ebook-front.html` | ebook front matter (licence, epigraph) |
| `ebook-the-secret-key-of-heaven.typ` | earlier ebook source (Typst HTML export + Calibre), superseded by `ebook-front.html` + the TEI |
| `ebook-override.css` | ebook styling on top of `../../resources/css/ebook.css` |
| `source/A29703.tcp.xml` | the 1665 edition as transcribed by EEBO-TCP ([A29703](https://github.com/textcreationpartnership/A29703)), untouched: the provenance |
| `source/the-secret-key-of-heaven.tei.xml` | enriched TEI edition: the 1665 text plus every editorial decision inline |
| `source/editorial.py` | the book's settings: file layout, headings, ebook and print |
| `source/review-report.md` | the editor decisions carried from `chapters/typ` into the TEI |

The edition was finished before the TEI existed, lightly modernized from the
1665 text with some of the structure of Chapel Library's edition (whose text
is public domain; its annotations are its own and are not used). The TEI was
built from it, so every difference from the 1665 printing (about 19,500:
spelling and case, scripture references, lists, quotation marks) is recorded
as an editor decision. The headings below each file title are the edition's
own, kept in the TEI as `label[@type="head"]`, not as printed text.

Left out of this edition but kept in the TEI as printed: most of the long
epistle dedicatory (the twenty lessons of "the rod", the plague of 1665;
only its closing paragraph is the Preface), the publisher's list of books,
the errata and the printed table of heads.

## Everyday commands

From anywhere in the repository (`./fgb --help` for the rest):

``` sh
$ ./fgb sync brooks      # after editing chapters/typ: into the TEI, list the changes
$ ./fgb find brooks WORD # every place a word is, as printed in 1665 and as decided
$ ./fgb page brooks      # the side-by-side page (1665 | edition)
$ ./fgb check brooks     # verify
$ ./fgb build brooks     # print PDF, cover wrap and checked EPUB into dist/
```

The PDFs and the EPUB are not kept in git: `./fgb build brooks` makes them
in `dist/thomas-brooks/the-secret-key-of-heaven/`.

Layout lines are not stored in the TEI, so `./fgb check` lists the files
that have them as differing from the extraction: the `#align`/`#linebreak()`
around the text in `chapter-03.typ` and its indented Doctrine
(`#block(inset: …)`), and the `#linebreak()`/`#pagebreak()` lines elsewhere.
Keep them in `chapters/typ`.
