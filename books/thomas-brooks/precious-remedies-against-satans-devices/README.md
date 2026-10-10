# Precious Remedies Against Satan’s Devices — Thomas Brooks

*Precious Remedies against Satans Devices. Or, Salve for Believers and
Unbelievers Sores* (London: M. Simmons for John Hancock, 1653, "The Second
Edition Corrected and Enlarged"), lightly modernized. Banner of Truth's
Puritan Paperbacks list, no. 31.

## Layout

| Path | What it is |
| --- | --- |
| `chapters/typ/dedication.typ`, `to-the-reader.typ` | The Epistle Dedicatory; A Word to the Reader |
| `chapters/typ/introduction.typ` | the text (2 Cor. 2. 11) opened and the point proved |
| `chapters/typ/sin-01.typ` … `sin-12.typ` | Part I: devices to draw the soul into sin |
| `chapters/typ/duties-01.typ` … `duties-08.typ` | Part II: devices to keep souls from holy duties |
| `chapters/typ/doubting-01.typ` … `doubting-08.typ` | Part III: devices to keep souls doubting |
| `chapters/typ/ranks-01.typ` … `ranks-05.typ` | Part IV: devices to destroy all ranks of men |
| `chapters/typ/propositions.typ`, `reasons.typ`, `use.typ` | the propositions, the reasons and the use |
| `chapters/typ/appendix-01.typ` … `appendix-05.typ` | the appendix: five more devices |
| `precious-remedies-against-satans-devices.typ` | print edition (`@local/fgbooks` template) |
| `cover.typ` | Lulu cover wrap (`scripts/panel_cover.typ`, palette sage, as Brooks's *Secret Key*); `./fgb build` gives it the page count and renders the ebook cover |
| `ebook-front.html`, `ebook-override.css` | ebook front matter and styling |
| `source/A77614.tcp.xml` | the 1653 edition as transcribed by EEBO-TCP ([A77614](https://github.com/textcreationpartnership/A77614)), untouched; the TCP header's date, 1658, is not the imprint's |
| `source/precious-remedies-against-satans-devices.tei.xml` | enriched TEI: the 1653 text and every editorial decision |
| `source/editorial.py` | the book's settings: layout, spelling and case rules, ebook and print |
| `source/gap_fixes.py` | the 436 gaps filled, with evidence |
| `source/review-report.md`, `source/proofread-report.md` | the editor's decisions; the proofread and its open questions |

## The edition

- **Base text:** the TCP's 1653 text. Each device opens its own file, followed
  by its remedies. The 1653 printing sets each device at the end of the
  previous division, so the layout cuts the text by its printed wording. The
  printed heads ("Now the Remedies against this Device of Satan are these.")
  are kept as bold lines.
- **Gaps:** 436 of the TCP's 441 gaps are filled. The letters come from
  context, Grosart's text and the 1652 and 1658 printings (page images on
  archive.org; the 1653 copy is not there). All Greek and Hebrew was read
  from those scans by hand.
- **Margin notes:** the margin's labels ("1 Remedy.", "2 Device.", "Use.")
  are left out because the text says the same. The notes are footnotes in
  modern spelling, with their Latin as printed.
- **Proofread:** the whole book was read against the 1653 printing and
  Grosart's edition (Monergism; a check only, its text is not used). See
  `source/proofread-report.md`.

Left out but kept in the TEI as printed: the title page, the printed table,
Caryll's imprimatur, the bookseller's catalogue and the errata.

## Everyday commands

``` sh
$ ./fgb sync precious     # after editing chapters/typ
$ ./fgb page precious     # the side-by-side page (1653 | edition)
$ ./fgb check precious    # verify
$ ./fgb build precious    # print PDF, cover and checked EPUB into dist/
```
