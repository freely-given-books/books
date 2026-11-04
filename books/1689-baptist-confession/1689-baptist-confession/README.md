# The 1689 Baptist Confession of Faith — With Catechisms

The Second London Baptist Confession of Faith (1677, owned by the general
assembly in 1689), bound with the Baptist Catechism (1695) and An Orthodox
Catechism (1680).

The text is SVRBC's [symbolics-data](https://gitlab.com/svrbc/symbolics-data)
(the `symbolics-data/` submodule), on its own: no other copy is compared
with it. It goes through colophon like every TEI book: `source/make_thml.py`
lays the YAML out as one ThML file, which colophon reads as it reads a CCEL
text.

## Layout

| Path | What it is |
| --- | --- |
| `symbolics-data/` | submodule: `confessions/lbcf1689`, `catechisms/bc1695`, `catechisms/aoc1680` (the provenance, at the pinned commit) |
| `source/transcription/` | our own transcription of what symbolics-data lacks: the confession's preface, its closing statement and signatories |
| `source/make_thml.py` | lays both out as `source/lbcf1689.thml.xml`; it changes no words |
| `source/lbcf1689.thml.xml` | the source colophon reads (regenerate it, never edit it) |
| `source/1689-baptist-confession.tei.xml` | the enriched TEI |
| `source/editorial.py` | the book's settings: the layout (42 files), speeches, modern text |
| `chapters/typ/` | extracted from the TEI: `confession/`, `baptist-catechism/`, `orthodox-catechism/` |
| `proofs.typ` | how print sets the speeches and Scripture proofs (see below) |
| `1689-baptist-confession.typ` | print edition (`@local/fgbooksLBCF` template) |
| `cover.typ` | the full wrap and, with `--input front-only=true`, the ebook front |
| `art/corner.svg` | the frame's corner (from the engraved cover design) |
| `ebook-front.html`, `ebook-override.css` | the ebook's front matter and styling |

## How the text is encoded

Each confession paragraph and each catechism question and answer is a
speech, its label the speaker: "Paragraph 1:", "Question 1:", "Answer:"
(`SPEECH_BLOCKS`). Each Scripture proof is a note after the words it proves.
In print, `proofs.typ` (imported by every chapter file) sets them as the
book always has: the label bold, a bold number after each proved clause,
the proofs as a numbered list under the paragraph or answer, kept on one
page when it fits, and a thin rule after each catechism answer. The ebook
and the web pages give the proofs as pop-up notes.

## Everyday commands

```sh
git submodule update --init books/1689-baptist-confession/1689-baptist-confession/symbolics-data
./fgb build 1689          # PDF, cover, EPUB, reader and comparison pages into dist/
./fgb check 1689          # verify
```

After symbolics-data changes (a new pinned commit) or an edit in
`source/transcription/`:

```sh
cd books/1689-baptist-confession/1689-baptist-confession/source
python3 make_thml.py
../../../../colophon/.venv/bin/python ../../../../colophon/build_tei.py \
    lbcf1689.thml.xml 1689-baptist-confession.tei.xml
../../../../colophon/.venv/bin/python ../../../../colophon/tei_extract.py \
    1689-baptist-confession.tei.xml ../chapters/typ --layer reg
```

The print template is still the book's own `fgbooksLBCF` 0.1.0, whose
running head and inside margin fall short of Lulu's rules (`./fgb build`
warns: the head 0.28in from the top edge where Lulu asks 0.5in, an inside
margin of 0.875in where Lulu asks 1in for 206 pages), as they did before the
book moved to colophon; moving to the current `fgbooks` template would
settle both.
