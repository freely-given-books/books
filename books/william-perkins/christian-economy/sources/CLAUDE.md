# Working with EEBO-TCP texts (quod.lib.umich.edu source)

> **First-pass notes.** This file and the scripts beside it are the first
> converter, kept as provenance. The book is now built from the TEI by
> `scripts/tei/` (see the repository's `CLAUDE.md` and the `eebo-tcp-book`
> skill); the lessons below were carried into that pipeline.

This documents what was learned converting William Perkins' *Christian
Oeconomie* (TCP id `A09377`) from quod.lib.umich.edu into Typst files, both
in original spelling and modernized spelling. The scripts here are
generic and should work on any other EEBO-TCP text with little or no
modification.

## The source

`https://quod.lib.umich.edu/e/eebo/<ID>.0001.001/1:N?rgn=div1;view=fulltext`
is a web front-end over the **Text Creation Partnership (TCP)** corpus.
**The site itself blocks bot/programmatic access** (`web_fetch` gets a bot-
detection error) — don't fight this. Every EEBO-TCP text has a matching
GitHub repo with a plain TEI-XML file:

```
https://github.com/textcreationpartnership/<ID>
```

containing a single `<ID>.xml`. Just `git clone --depth 1` it. This is the
same underlying data quod.lib.umich.edu renders, so it's a strictly better
source: full text, no bot-blocking, no HTML-scraping mess.

The `<ID>` is the code visible in the quod.lib URL path (e.g. `A09377`).

## The "1:N" numbering

The `1:2`, `1:3` ... in the quod.lib URL corresponds to **top-level `<div>`
elements, in document order, across `<front>`, `<body>`, `<back>`**
(i.e. what old TEI called "div1"). `tcp_to_typst.py --list` prints exactly
this mapping:

```
python3 tcp_to_typst.py A09377 --list
1:1    title_page
1:2    dedication -- TO THE RIGHT HONORABLE ROBERT Lord RICH...
1:3    treatise -- A SHORT SVRVEY OF THE RIGHT MANNER...
```

`view=fulltext` on one of these URLs shows the **entire contents** of that
div, including all nested chapters/sections — for a "treatise" div this
can be the whole book in one fetch.

## Files in this project

- **`tcp_to_typst.py`** — generic, reusable converter. Give it a TCP id (it
  clones the repo) or a local XML path; it writes one `.typ` file per
  top-level div, preserving original spelling exactly. Use `--list` first,
  `--sections N N ...` to pick specific ones, `--pdf` to also compile.
  This is the tool to reach for on a **new** book.
- **`spelling.py`** — the Early-Modern-English → Modern-English spelling
  rule engine (mechanical rules + dictionary-oracle + a large manual
  dictionary of irregulars). Book-specific vocabulary (proper names, the
  manual dictionary) was tuned for *Christian Oeconomie* — see "Reusing
  the spelling modernizer" below before pointing it at a different text.
- **`modernize_render.py`** — like `tcp_to_typst.py`, but also runs
  everything through `spelling.py` and does capitalization cleanup. This
  one is currently hard-coded to `A09377.xml` and its two divs
  (dedication + treatise) and its macron-resolution table — treat it as a
  worked example / starting point to copy and adapt, not a drop-in tool.

## Hard-won lessons (read before modifying the renderers)

**1. A "word" in the XML is often split across inline markup.**
Justified line-wrapping means a single word is frequently split like
`ci<g ref="char:EOLhyphen"/>uill`. If you modernize/transform text
fragment-by-fragment as you walk the tree, you will silently process each
half of a split word independently and get it wrong (`ciuill` → the two
halves `ci` and `uill` never became `civil`). **Fix: linearize the whole
paragraph into one string first (with footnotes pulled into placeholder
tokens), do ALL text transformation in a single pass over that string,
then splice the footnotes back in.** This is the `linearize()` /
`render_paragraph_like()` pattern in `modernize_render.py`.

**2. Placeholder tokens must survive being tokenized as "words".**
Once you're doing whole-paragraph text processing, any inline markup you
insert (footnote refs, `#emph[...]`, etc.) needs to not get mangled by
your own word-level logic (capitalization, spelling rules). E.g. literally
inserting `#emph[` into the stream means the word-tokenizer will see
`emph` as a real word and may capitalize it. Use an unambiguous, clearly-
non-English placeholder (`ZZEMSTARTZZ`, `ZZFNAAZZ`, ...) wrapped in a
non-alphabetic separator (e.g. `\x00`) so it can't fuse with adjacent real
words, guard against it in the tokenizer loop, and substitute the real
markup back in as the very last step.

**3. Escape source text *before* inserting your own Typst markup, not
after.** If you escape the whole combined string at the end, you'll
escape the `#`, `[`, `]` you deliberately inserted for `#emph[...]` /
`#footnote[...]`, corrupting the output. Escape only literal text pulled
from the XML, at the point you pull it.

**4. The "combining macron abbreviation" (`char:cmbAbbrStroke`, e.g.
"whē" for "when") is genuinely ambiguous** — it can expand to a suppressed
`n` (the vast majority of cases) or `m` (com-/com- assimilation, "them",
"whom", "chamber", ...). There's no way to tell which from the character
alone; **you have to inspect the surrounding text for every occurrence**
in a new book and build an index-based override table (see
`MACRON_M_OVERRIDE` in `modernize_render.py` — one index per occurrence in
document order, default `n`, override to `m` for the specific ones you've
manually confirmed). Do this once per book; don't assume the same indices
apply to a different text.

**5. A rare double-whammy: a macron-abbreviated word that *also* gets
split by a line-wrap hyphen** (e.g. `co<macron>` + `<EOLhyphen/>` +
`sent`). The whitespace between those two adjacent `<g>` tags is pure
XML-pretty-print indentation, not a real space — but naively collapsing
whitespace turns it into `" "`, producing `"con sent"`. Fix: when the
tail between two sibling `<g>` elements is whitespace-only *and* contains
a newline, drop it instead of collapsing it to a space (see the
`next_el.getnext()` check in both `tcp_to_typst.py` and
`modernize_render.py`). **This same whitespace-collapse bug also hits
`<gap>` elements** (illegible-text placeholders) sitting next to a `<g>`
tag or another `<gap>` — and also hits an element's own *leading* text
(its `.text`, not a sibling's `.tail`) when the element's first child is
a `<g>`/`<gap>`. Both scripts guard against all of these now (see
`_leading_text_is_joinable_whitespace()` and the `joinable = ("g", "gap")`
checks) — if you copy this pattern for a new book, make sure you didn't
narrow the check back down to just `"g"`.

**5b. Illegible-text `<gap>` elements can often be reconstructed from
context**, and it's worth doing — EEBO-TCP represents illegible print as
`<gap reason="illegible"><desc>•</desc></gap>` (bullet count is a rough
guide to how many characters are missing, not exact), which otherwise
renders as a literal "•" in the output. For *Christian Oeconomie* every
non-`duplicate`, non-`foreign`-script gap in the treatise was resolved by:
tracing direct Bible quotations (KJV/Geneva wording), recognizing known
Latin legal/canon-law maxims ("diu deliberandum quod semel statuendum",
"de praesenti" vs "de futuro" marriage contracts, "cousin-german" as a
period technical term), and just reading the surrounding sentence. The
reconstruction is done via an index-based override table exactly like the
macron table — `GAP_FIXES = {0-indexed-gap-number: "letters to insert"}`
in both `convert.py` and `modernize_render.py` — with a `next_gap_text()`
helper mirroring `next_macron_letter()`. **Important:** the letters you
insert must match *this document's own* old-spelling conventions, not
modern spelling or your assumption — e.g. this text spells "every" as
"euery" (18 occurrences, 0 as "every") and "marriage" as "mariage" (92 vs
10), so a gap bridging "pray _ ery where" needs the filler "eu", not "ev",
even though either produces the same *modernized* result downstream.
Check the actual word-frequency balance in `wordlist.txt` before assuming
which spelling variant is dominant. Leave gaps unresolved (fall through to
the original bullet/bracket) rather than guess when: the script is
non-Latin (Greek/Hebrew — unrecoverable without a page image; see 5b-bis),
the span is many words long, or it's an ambiguous citation digit/number
with no other clue.

**5b-bis. Before guessing at a gap, look for a second witness.** A text that
was later gathered into a collected *Workes* was usually reset from the same
copy, and the reset margins are often perfectly legible where the quarto's are
not. For *Christian Oeconomie* that witness is the 1609 folio *Workes of that
famous and worthie minister of Christ, M. W. Perkins*, vol. 3, scanned on
archive.org as `bim_early-english-books-1475-1640_the-workes-of-that-famou_\
perkins-william_1609_3`; it resolved all eight gaps context could not, including
the Greek and Hebrew ones that 5b says to leave alone. Finding a passage in a
scan without a working "search inside" endpoint:

```
# per-leaf text: the search text has no page breaks, but the page index gives
# the character range of each leaf
curl -sL -o st.txt.gz  ".../<ID>/<ID>_hocr_searchtext.txt.gz"
curl -sL -o pi.json.gz ".../<ID>/<ID>_hocr_pageindex.json.gz"
# idx[leaf] == [char_start, char_end, ...]; slice st by it, grep the slices
# then pull that leaf's image and crop the margin:
curl -sL -o p.jpg "https://archive.org/download/<ID>/page/n<LEAF>_w2000.jpg"
magick p.jpg -crop WxH+X+Y +repage -resize 700% -normalize -sharpen 0x1 out.png
```

Search the OCR on short, odd words ("Paternus", "glue"), not on phrases —
early-modern OCR mangles long-s, u/v and word spacing, so a four-word query
usually misses. And read the *image*, never the OCR, for the answer: the OCR of
the note that turned out to be `Aristot. Politic. 1.` was `AY tot.Pe, - facet.`

**5c. An EOL-hyphen join can produce a non-word when the compositor
abbreviated the first half.** `par<g ref="char:EOLhyphen"/>factis` joins to
"parfactis", which is not Latin: the printed "par-" carried a suspension mark
for "parentum" that the transcription did not record (Beza's section heading is
*de sponsalibus absque consensu parentum factis*). The join itself is correct
behaviour — the loss happened upstream — so the repair belongs in a lookup
table, not in the joining logic: `NOTE_TEXT_FIXES` in `modernize_render.py`,
keyed by the rendered post-join text and applied to note bodies. Only add an
entry you have checked against the work being cited. Note that
`tcp_to_typst.py` is deliberately kept generic and carries no such table, so
the original-spelling render (`treatise.typ`) needs this fix reapplied by hand
after a regeneration.

**6. The drop-cap artifact.** `<seg rend="decorInit">C</seg>Hristian`
renders as literal "CHristian" (decorative first letter + the next
letter, which the original typesetting also capitalized). If you're
modernizing capitalization, lowercase that second letter before your
normal sentence-initial-capitalization logic runs on it.

**7. Footnote/marginal-note content was deliberately left in *original*
spelling in the modernized output.** It's almost entirely bibliographic
abbreviations and Latin, not modernizable English prose, and the risk of
mangling a Latin citation is not worth it. If a future text has footnotes
containing substantial English commentary, reconsider this.

**8. A `#footnote[...]` body is re-parsed as Typst markup, so a note that
opens with an enum or list marker becomes a list *inside the note*.** In this
text nine notes are Scripture citations beginning `1. Cor.`, `1. Sam.`,
`2. Sam.` ... — Typst read the `1. ` as an enumeration and rendered the note as
an empty numbered item, swallowing the note that followed it into the same
list. Both renderers now run note bodies (and `<item>` text) through
`escape_leading_marker()`, which turns `1. Cor.` into `1\. Cor.` and a leading
`- `/`+ `/`/ ` into `\- ` etc. Watch for this in any content block built from
source text, not just footnotes.

**9. List nesting is carried entirely by leading spaces, so never run a
whitespace-collapsing pass over the rendered `.typ`.** `render_list()` indents
two spaces per level and Typst nests on that indent alone. A cleanup pass doing
`re.sub(r"[ \t]{2,}", " ", text)` — an easy thing to add when stripping
artifacts — silently flattens every genealogy diagram in chapter 5 to one
level, and the result still compiles and still looks like a list, so nothing
warns you. In this book the *only* runs of 2+ spaces in the renderers' output
are list indentation; if you need such a pass, exclude lines matching
`^\s*- `.

## Reusing the spelling modernizer (`spelling.py`) on a different book

The **mechanical rules** (u/v, i/j, doubled-final-consonant, `-ie`→`-y`,
`-nes`→`-ness`, oracle-driven silent-e removal) are generic and should
carry over directly. The **`MANUAL` dictionary and `DO_NOT_TOUCH`/
`LATIN_SKIP` sets are specific to this book's vocabulary** (proper names,
the exact irregular spellings that appear in *Christian Oeconomie*) and
should be rebuilt for a new text. Process for a new book:

1. Extract the word list (see the `wordlist.txt` approach: strip Typst
   markup, tokenize, count frequencies).
2. Run `modernize_word_lower()` over it and diff against the input to
   sanity-check the mechanical rules aren't misfiring (test known real
   double-letter words like "small", "well", "hill" stay untouched — the
   dictionary-oracle guard should protect these already).
3. Cross-check the *unchanged* words against a spellchecker
   (`pyspellchecker`) to surface words the mechanical rules missed
   entirely (filter out proper nouns, Latin, and archaic `-eth`/`-est`
   verb forms whose *root* is already fine — those are expected to show
   as "unknown" and aren't bugs).
4. Build the new `MANUAL` dict from what's left. Watch for: dictionaries
   containing real-but-obscure words that happen to match an old spelling
   (`forme` is valid modern English in some technical senses, so the
   oracle leaves it — but in an EME religious text it's always old
   spelling for "form" and needs a manual override).
5. Do NOT touch closed-class grammatical archaisms (`hath`, `doth`,
   `thou`, `thee`, `thy`, `thine`, `ye`, `shalt`, `wilt`, `art`, `wert`,
   `hast`, `dost`) — these are different word-forms from their modern
   equivalents, not alternate spellings, and changing them would be
   replacing words, which was explicitly out of scope here.
6. Capitalization: keep the "lowercase a short, explicit list of
   unambiguous common nouns when not sentence-initial" approach rather
   than trying to lowercase everything capitalized. Titles and religious
   terms (God, Lord, Church, King, Bishop, Scripture...) are safer left
   alone than guessed at word-by-word.

## Quick start for a new EEBO-TCP book

```bash
# See what's in it
python3 tcp_to_typst.py <ID> --list

# Convert everything, compile to PDF
python3 tcp_to_typst.py <ID> --outdir out/ --pdf

# Or just specific top-level divs
python3 tcp_to_typst.py <ID> --sections 2 3 --outdir out/ --pdf
```

For a modernized-spelling version, copy `modernize_render.py` and adapt:
replace the hard-coded XML filename/div types, rebuild the
`MACRON_M_OVERRIDE` table by inspecting that book's macron occurrences,
and rebuild `spelling.py`'s `MANUAL` dictionary per the process above.
