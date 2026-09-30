# Sources for *Christian Economy*

| File | What it is |
| --- | --- |
| `A09377.tcp.xml` | The EEBO-TCP transcription of the 1609 printing, exactly as published by the Text Creation Partnership ([textcreationpartnership/A09377](https://github.com/textcreationpartnership/A09377)). Untouched; this is the provenance. |
| `christian-economy.tei.xml` | The enriched edition: the same transcription with every editorial layer added inline — modern spelling (`choice/orig` + `choice/reg`), macron and superscript abbreviations (`abbr`/`expan`), letters restored where the print is illegible (`supplied`), numbered lists and edition headings. Each decision says who made it: `#auto` (machine) or `#editor` (reviewed). Validates against TEI `tei_all`. |
| `review-report.md` | Every review decision carried from the reviewed Typst chapters into the TEI, grouped by kind, plus a short list of things to check. |

## Getting text out

The modern reading text (what `chapters/typ` contains):

```sh
python3 ../../../../scripts/tei/tei_extract.py christian-economy.tei.xml ../chapters/typ --layer reg
```

The 1609 text as printed (macrons shown, printed headings and numerals):

```sh
python3 ../../../../scripts/tei/tei_extract.py christian-economy.tei.xml out-1609 --layer orig
```

Add `--show-gaps` to show illegible print the way the TCP transcribers
marked it instead of the restored letters, `--expand` to spell out
abbreviations, or `--only-auto` to see the machine pass without the review
(handy for auditing).

## Rebuilding after more review

Keep reviewing in `chapters/typ`, then:

```sh
python3 ../../../../scripts/tei/build_tei.py A09377.tcp.xml christian-economy.tei.xml \
    --review ../chapters/typ --report review-report.md
```

Any word you change becomes an `#editor` decision; the machine's proposal
is kept alongside it.
