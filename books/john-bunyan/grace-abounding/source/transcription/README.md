# How the 1688 transcription was made

The scripts ran in `~/Projects/fgbooks/work/grace-abounding/` (the film frames,
Kraken's output and the OCR witnesses are not in git; see
`../transcription-report.md`). In order:

| script | does |
| --- | --- |
| `crop.py` | each film frame cut to its page |
| `foundation.py` | Kraken's text voted on by six witnesses → `foundation.json`; `decisions.json` the readings settled on the page images |
| `alto.py`, `assemble.py`, `breaks.py`, `italics.py` | lines with Kraken's boxes, paragraphs, italics by slant |
| `gutter.py` | words the film lost at the gutter, supplied → `gutter.json` |
| `emit_tei.py` | the TEI source (`../grace-abounding-1688.tcp.xml`); heads, title page, preface italics and transcription fixes by hand |
| `wording.py`, `triage.py`, `bucket.py` | the 1688 wording against the previous edition, sorted by the witnesses |
| `apply_1688.py` | the reading text: the previous edition with the 1688 wording put back (decisions in KEEP/CUSTOM, on `buckets-decided.json`; every change in `apply-1688.md`) |
| `transfer_italics.py` | the 1688 italics into the reading text |
| `paradiff.py`, `check_sheet.py`, `measure.py` | checks: paragraphs, page-image sheets, the before/after measure |
| `rebuild.sh` | the whole chain, into the book, with `refstyle.py`, `./fgb sync` and `./fgb check` |
