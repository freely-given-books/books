# Edition rules

The press's standing editorial decisions, in one place, so a book can be made from start to
finish without asking about anything settled here. Each rule names where it came from. When a
book needs something these rules do not cover, ask the editor once, then add the answer here.

Three layers, never mixed (the editor, 2026-11-05):

| Layer | What it is | Example |
| --- | --- | --- |
| **as printed** (`orig`) | the base printing, letter for letter | approueth |
| **spelling** (`reg[@type=spelling]`) | the same words in modern letters | approveth |
| **modernized** (`reg[@type=grammar\|emendation]`) | a different word or form | approves |

The reading edition is spelling-modernized; grammar and wording change only where a rule below
says so.

## 1. Choosing the base

Case by case, with the evidence shown to the editor (2026-11-08):

1. **An EEBO-TCP or Evans text exists → it is the base**, untouched, as `source/<ID>.tcp.xml`.
2. **No TCP →** decide per book: our own Kraken + Tesseract reading of a scanned printing
   (the full pipeline), with CCEL, Gutenberg, Goold and other texts as witnesses.
3. **Either way, look for a later edition by the author himself** (a lifetime revision). If it
   adds real clarifications, bring the differences to the editor; basing on it is their call
   (Grace Abounding: the 1688 edition, a book Bunyan kept revising).
4. Every other printing is a witness. Get its scan (archive.org `bim_early-english-books-*`
   first), cache it under `work/<book>/scan-<year>/` with a README, never delete it, and run
   Kraken + Tesseract on it.

## 2. The as-printed layer: verbatim

As close to the printed page as we can get ("what it looks like if you pick up the original book
in the library"). Only real errors change it, each recorded with its evidence:

- **Gaps:** every illegible letter and word, and every Greek, Hebrew or other non-Latin passage
  the transcription could not key, read from the page images (`GAP_FIXES`). No
  "in non-Latin alphabet" placeholder ever reaches a draft.
- **Keying slips:** where two OCR readings of the same printing agree against the TCP, read on
  the page image, recorded as supplement `<corrections>`.
- **Nothing else:** not the printer's own misprints (those are corrected in the reading text), not
  spelling, not a model's reading. OCR and vision models only flag; the page image decides.

## 3. The reading edition

The editor keeps this deliberately loose rather than a formula (2026-11-08): **updated spelling
and punctuation always; wording only where it is really needed.** Goold (or a book's standard
later editor) is a good frame for wording but not binding; we have overruled him.

What the finished books show (counted from their TEIs, 2026-11-08):

**Always changed**

| | Example | Note |
| --- | --- | --- |
| letter forms | ſ → s, vv → w, u/v, i/j, Ʋ → U | machine |
| spelling | approueth → approveth, shew → show, choyce → choice | machine + book's `SPELLING` |
| compounds | my self → myself, our selves → ourselves, any thing → anything | |
| elided past forms | fill'd → filled, lay'n → lain, blest → blessed | 2026-11-08 |
| capitals | mid-sentence nouns lowercased (Grace → grace); drop-cap words (HAving → Having) | |
| God | always capitalized when it means God | 2026-11-01 |
| Scripture references | Heb. xii. 5 → Heb 12:5; spelled out where the sentence reads it ("in Romans 8:28"); v., vv., ch. | 2026-10-27 |
| printer's misprints | be → he where the sense needs it, a wrong verse number fixed from the page | with evidence |
| &c. | → etc. where the book sets `EXPAND_ETC` | per book |

**Kept as printed**

| | Example | Note |
| --- | --- | --- |
| period grammar | hath, doth, thou, thee, ye, unto, -eth, -est | every book but Simon Magus |
| pronouns for God | lowercase or capital as the book prints them | 2026-11-01 |
| italics | the print's italics (Scripture, emphasis, names) | 2026-11-01 |
| contractions | 'tis, 'twas | |
| Latin and other works' citations | Aug. de Civ. Dei l. 1 | |
| margin labels | Doct., Answ., Use, Quest. stay footnotes at their line | 2026-11-08 |
| Scripture wording | the author's, not forced to the KJV | |

**Wording, only where really needed** (each a decision, listed for the editor in one batch):
a word that now means something else or misleads ("let" = hinder), a construction that reads as a
mistake today, a word lost to the page. Look at Goold's reading first; take whichever reads
better and stays closer to the author. Of Temptation's looser rule (whichever reads better in
modern English) stays that book's.

**Grammar modernization** (hath → has, thou → you, -eth → -s) is a per-book decision, off by
default. Simon Magus has it; ask before giving it to another book.

## 4. Typesetting

One house way for every book, so no book needs layout choices. Gathered from the books'
revision history (2026-11-08); colophon makes these the defaults.

**Follow the print's structure.** Its paragraph breaks stay (Gouge's "teacheth us, that" doctrine
paragraphs); its numerals stay as printed labels (1., I., First), never regenerated.

**Numbered outlines** (points, sub-points, reasons):
- each level set in 2em further than the one above, clearly more than the 12pt first-line
  indent; a set-in paragraph keeps its first-line indent;
- the level comes from the numbering (I. › 1. › (1.) › [1] › a.), settled by sense where the
  numbering is ambiguous; a run-in series ("…: 1. The Word preached. 2. …") is split onto its
  own lines;
- a list sits one step in, under the point it belongs to, never left of it; half a line above and
  below;
- a deep outline (three levels or more) also gets edition headings over its main parts, in the
  author's or the contents page's words (Divine Cordial, mock-up "B").

**Braces:** with a closing term, read as a sentence; a small two-item brace runs into its
sentence; otherwise its branches are a list, with no bullets when the print has no numbers. A
genealogy or tree is a diagram, drawn in print, EPUB and reader alike.

**Margin matter:** labels (Doct., Answ., Use) and references are footnotes, placed after the
clause or name they gloss, not on a point's number; a note that only repeats the point's number
is dropped.

**Chapter summaries** (Owen's arguments): inset, a size smaller, ragged right. A printed chapter
title (Watson): bold, centred under "Chapter N", never doubled with the printed "CHAP. II.".

**Pages (print):** every footnote on its marker's page; no heading at a page's foot; no chapter
ending on 2-4 lines; no widow lines.

**Every output alike:** print, EPUB, reader and the site's Then & Now show every feature before
a book goes to the editor.

## 5. Front and back matter

- Publisher page: the printed edition, "spelling modernized", and the transcription used (e.g.
  EEBO-TCP A53712). No method detail (2026-11-02).
- The print's title page and contents are not reproduced; the edition makes its own.

## 6. What still goes to the editor

Only these stop a book:

1. The base, when rule 1 leaves a real choice.
2. The batch of wording changes (rule 3).
3. Grammar modernization, if a book seems to want it.
4. The cover colour.
5. Sign-off.

Everything else follows these rules. A new question, once answered, becomes a rule here.
