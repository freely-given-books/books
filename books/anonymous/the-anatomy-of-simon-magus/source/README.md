# Sources for *The Anatomy of Simon Magus*

| File | What it is |
| --- | --- |
| `A25330.tcp.xml` | The EEBO-TCP transcription of the 1700 printing ([textcreationpartnership/A25330](https://github.com/textcreationpartnership/A25330)). Untouched; this is the provenance. |
| `the-anatomy-of-simon-magus.tei.xml` | The enriched edition: the transcription with every editorial layer inline. Each decision says who made it: `#auto` (machine) or `#editor` (this edition). |
| `editorial.py` | This book's settings for the scripts: the chapter-heading macro, the printed divisions the edition leaves out, report notes. |
| `review-report.md` | Every edition decision carried into the TEI, grouped by kind. |

## How this edition was made

The modern text in `../chapters/typ` was finished by hand before the TEI
existed. The TEI was then built from the TCP file with that finished text as
the review (`build_tei.py --review`), so every difference from the 1700
printing is recorded as an `#editor` decision, and extracting the TEI gives
the finished text back exactly (the print PDF compiles identically, line for
line). What the edition changes, and how the TEI records it:

- spelling, case and modernized grammar (hath → has, thou → you, Holy Ghost
  → Holy Spirit, thereof → of that): `choice/orig` + `choice/reg`
- translations of Latin passages, inserted in brackets: part of the `reg`
- notes rewritten in modern form ("Matth. 21. 13." → "Matt 21:13"): `choice`
  inside the `note`; notes moved (e.g. from the start of a quotation to its
  end): the note stays where it was printed with `@target` pointing at an
  `<anchor>` where the edition puts it; a note the editor added:
  `note[@ana='#edition-only']`
- italics set roman / roman set italic: `hi[@ana='#print-only']` /
  `hi[@ana='#edition-only']`
- paragraphs run together: `@prev`/`@next` (both stay separate as printed);
  paragraphs split: the TEI paragraph is split; the block quotation:
  `p[@rend='quote']`
- spaces added or removed between words: `choice` with `reg[@type='spacing']`
- the chapter titles and their short running-head forms: `head[@type='edition']`,
  `head[@type='short']`
- "FINIS.": kept, `trailer[@ana='#in-edition']`

The table of contents and the publisher's advertisement are in the TEI as
printed but are not part of the edition.

## Getting text out

```sh
python3 ../../../../scripts/tei/tei_extract.py the-anatomy-of-simon-magus.tei.xml ../chapters/typ --layer reg
python3 ../../../../scripts/tei/tei_extract.py the-anatomy-of-simon-magus.tei.xml out-1700 --layer orig
```

The orig layer is the 1700 text (long s kept); add `--only-auto` to the reg
layer to see what the machine pass alone would have made of it.
