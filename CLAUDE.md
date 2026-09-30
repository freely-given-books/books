# Freely Given Books — working notes for early printed sources

How books from early printed sources are prepared in this repo, and what
was learned doing it for William Perkins' *Christian Oeconomie* (1609,
EEBO-TCP `A09377`). Read this before starting a new book from the same
kind of source.

## Architecture: TEI is the master, Typst is a view

```
TCP transcription (untouched)          books/<author>/<book>/source/<ID>.tcp.xml
        │  scripts/tei/build_tei.py  (+ reviewed Typst chapters, optional)
        ▼
enriched TEI edition                   books/<author>/<book>/source/<book>.tei.xml
        │  scripts/tei/tei_extract.py   or   scripts/tei/tei.typ (Typst reads the XML)
        ▼
Typst chapters / PDF                   chapters/typ/*.typ, <book>.typ

enriched TEI edition
        │  scripts/tei/tei_epub.py (+ ebook-front.html, cover, CSS)
        ▼
EPUB 3                                 <book>.epub
```

`tei_epub.py` gets its XHTML from `tei_to_html.py`, which reuses
`tei_extract.py`'s renderer (the `R` class; its
output methods `esc`/`emph`/`sup`/`footnote` are what the HTML subclass
overrides), so the ebook and the Typst chapters cannot drift apart.

- The **untouched TCP file** is provenance. Never edit it.
- The **enriched TEI** holds the 1609 text *and* every editorial decision
  inline, so one file yields either reading:
  - `<choice><orig>mariage</orig><reg resp="#auto">marriage</reg></choice>` spelling
  - `<choice><orig>Heere</orig><reg resp="#editor">Here</reg><reg resp="#auto">Heer</reg></choice>`
    an editor overriding the machine (editor's reg first, machine's kept)
  - `<choice><abbr>fro̅</abbr><expan>from</expan></choice>` macron abbreviations,
    `y<hi rend="sup">e</hi>` → `the`
  - `<supplied reason="illegible" cert="high" resp="#auto">eu</supplied>`
    letters lost to bad print, with an XML comment giving the evidence and
    the TCP `<gap>` kept inside
  - `<list type="numbered" change="#review">` run-in "I. … II. …" set out as
    lists, printed numerals kept in `<label>`
  - `<head type="edition">` this edition's section title, printed head kept
  - `reg/@type`: spelling, case, punctuation, emendation
- The header (`editorialDecl`, `respStmt`, `revisionDesc`) documents the
  rules and who `#auto` / `#editor` are. It validates against `tei_all`.
- **Typst is replaceable.** Anything that reads XML can produce LaTeX, HTML
  or EPUB from the same file.

## Getting sources

**EEBO-TCP (quod.lib.umich.edu).** The site blocks programmatic access;
don't fight it. Every text is on GitHub as plain TEI:
`git clone --depth 1 https://github.com/textcreationpartnership/<ID>` →
`<ID>.xml`. `<ID>` is the `A#####` in the quod.lib URL. The `1:N` in a
quod.lib URL is the Nth top-level `<div>` across front/body/back.
`<pb n="90" facs="tcp:2719:61"/>` gives the printed page and page image.

**CCEL** (not done yet). CCEL offers ThML (an old HTML-based format) or
plain text. Plan: write a converter to the same TEI subset used here, with
`<pb>`/line information optional and the header saying the text is
paragraph-faithful rather than line-faithful. Then everything downstream
works unchanged.

## Commands

```sh
# enriched TEI from the TCP file, folding in reviewed Typst chapters
python3 scripts/tei/build_tei.py source/A09377.tcp.xml source/christian-economy.tei.xml \
    --review chapters/typ --report source/review-report.md

# Typst chapters (dedication.typ, chapter-NN.typ) from either layer
python3 scripts/tei/tei_extract.py source/christian-economy.tei.xml chapters/typ --layer reg
python3 scripts/tei/tei_extract.py source/christian-economy.tei.xml out/orig --layer orig
#   --expand          orig layer: fro̅ -> from
#   --show-gaps       orig layer: show illegible print as transcribed (•)
#   --mark-supplied   wrap reconstructed letters in ⟨ ⟩
#   --only-auto       reg layer: machine pass only (audit what the review changed)

# EPUB 3 straight from the TEI (no Calibre); full command in the book's README
python3 scripts/tei/tei_epub.py source/christian-economy.tei.xml christian-economy.epub \
    --title "Christian Economy" --author "William Perkins" \
    --front ebook-front.html --cover cover_front.jpg --css ebook.css
# or the whole book as one XHTML file, to preview in a browser
python3 scripts/tei/tei_to_html.py source/christian-economy.tei.xml preview.html

# end-to-end check: rebuild matches committed TEI, round trips, compile
python3 scripts/tei/verify.py books/william-perkins/christian-economy
```

Or straight from Typst (compile with `--root` at the repo root, like the cover):

```typst
#import "../../../scripts/tei/tei.typ": tei-division, tei-book
#let ed = xml("source/christian-economy.tei.xml")   // load in *this* file
#tei-division(ed, "dedication")
#tei-division(ed, 1)                    // layer: "reg" is the default
#tei-book(ed, layer: "orig")
```

`tei.typ` and `tei_extract.py` produce text-identical output (checked by
comparing compiled PDFs).

## Review workflow

The reviewed Typst chapters remain a fine place to edit. Re-run
`build_tei.py --review chapters/typ`: it aligns the reviewed text against
the machine pass token by token and records every difference as an
`#editor` decision (macron n/m fixes and filled-in gaps are recognized as
such). Structural edits it understands: a printed "I." turned into a `+ `
enum item, and a paragraph split. Pure layout (`#linebreak()`,
`#align(...)`) is not text and is not stored. `//` comment lines are
ignored. The report lists every decision and anything it could not apply.

For *Christian Oeconomie* the reg extraction reproduces the reviewed
chapters byte for byte, except the `#linebreak()` in chapter 5 (layout). A
damaged list in the review copy of chapter 5 was rebuilt from the source
and copied back into `chapters/typ`.

## Hard-won lessons

1. **Words span inline markup.** `ci<g ref="char:EOLhyphen"/>uill`,
   `fro<g ref="char:cmbAbbrStroke">̄</g>`, `cu<gap/>ome`,
   `<seg rend="decorInit">C</seg>Hristian`, `y<hi rend="sup">e</hi>`.
   `teitok.py` tokenizes a TEI element losslessly into words that can
   contain such elements (tested: rebuild without changes is byte-identical
   to the source), so a `<choice>` can wrap the whole word.
2. **Pretty-print whitespace is not a space** when it sits between two
   `g`/`gap` siblings or is an element's leading text before a `g`/`gap`.
   Treating it as a space gives "con sent", "cu stome". The enriched file
   drops it inside words so consumers need no heuristics; `tei_extract.py`
   still guards against it for raw TCP input.
3. **Macron abbreviations are ambiguous** (n or m). `MACRON_M` in
   `build_tei.py` lists, by document order, the ones that are m; everything
   else is n. Build it per book by reading each occurrence. The review
   caught 9 wrong ones here (fron→from, conmonly→commonly); those are now
   `<expan resp="#editor">`.
4. **Illegible gaps can mostly be reconstructed** from Bible quotations,
   Latin legal maxims and context (`GAP_FIXES`, with certainty and
   evidence). Use the document's *own* spelling for the letters ("euery",
   not "every"; check word frequencies). Greek/Hebrew and citation digits
   need the page image — the editor filled 8 of those by hand.
5. **Keep grammatical archaisms** (hath, doth, thou, thee, thy, ye, shalt,
   wilt, art, hast, dost): different words, not spellings. Footnotes stay
   in original spelling (abbreviations expanded only).
6. **Sentence case rules are legacy-compatible on purpose**: first word of
   a paragraph or after . ! ? is capitalized; an italic boundary right
   after a full stop does *not* start a sentence (so "…do.] vers. 26." stays
   lowercase); a short list of common nouns is lowercased mid-sentence;
   roman numerals are left alone. Changing these rules would make an
   unreviewed rebuild differ from what was reviewed.
7. **spelling.py misses** found by the review (bee→be ×78, lawes→laws,
   Prou→Prov, Heere→Here, bin→been, dais→days, yong→young, reade→read,
   shew→show, KJV name forms like Isaak→Isaac, Thar→Terah…) are
   now in `spelling.py`'s `MANUAL` (so this book's TEI credits them to
   `#auto`; its report is down to 8 spelling decisions, mostly in notes,
   which stay in original spelling). Context-dependent ones were left out
   (harts/hearts, Tigres, Corinthes). `bee`→`be` is a known risk: it
   mangles "Bee-hive", which the editor layer here overrides.
8. **Typst `xml()` gotchas** (for `tei.typ`): paths resolve relative to the
   file that calls `xml()`, so load the XML in the book file and pass it
   in; `while` loops hit an iteration limit on a whole book, use recursion;
   adjacent string pieces keep double spaces (collapse them yourself);
   markup drops the space before `#footnote[...]` but strings don't; smart
   apostrophes are applied to markup, not strings.
9. **TEI validation**: `tei_all.rng` is on GitHub
   (`TEIC/TEI-Simple`), tei-c.org is often unreachable; validate with jing
   (`relaxng/jing-trang` releases). lxml's RelaxNG is too slow for
   `tei_all`. `@resp` is not allowed on `list`/`head` in that schema, hence
   `@change="#review"`.
10. **EPUB checking**: epubcheck needs Java. Without it, Calibre's own
   checker (the editor's "Check book") runs headless:
   `calibre-debug scripts/tei/check_epub.py book.epub` (ignore the Qt/GPU
   noise it prints). The Perkins EPUB passes with 0 issues.

## Starting a new TCP book

1. Clone the TCP repo; copy `<ID>.xml` to `source/<ID>.tcp.xml`.
2. Copy `build_tei.py` and replace the book tables at the top:
   `MACRON_M`, `GAP_FIXES`, `REPORT_NOTES`, `repair_review`, and the
   file-name mapping in `main()` (dedication + chapter-NN).
3. Run `build_tei.py` without `--review` for the machine-only edition,
   extract the reg layer, review in Typst, then rebuild with `--review`.
