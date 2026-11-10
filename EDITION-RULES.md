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
| spelling | approueth → approveth, shew → show, choyce → choice, weakned → weakened, terrour → terror; American: labour → labor, defence → defense, centre → center, Saviour → Savior | machine + book's `SPELLING`; any old spelling with a plain modern form is modernized by default, in American spelling (2026-11-08; All of Grace and Indwelling Sin; released British-spelled books change at their next revision) |
| compounds | it self → itself, our selves → ourselves, what ever → whatever, to day → today | "any thing", "every one" kept as printed (Owen's books, 2026-11-09) |
| elided past forms | fill'd → filled, lay'n → lain, blest → blessed | 2026-11-08 |
| capitals | mid-sentence nouns lowercased (Grace → grace); drop-cap words (HAving → Having) | |
| God | always capitalized when it means God | 2026-11-01 |
| Scripture references | Heb. xii. 5 → Heb 12:5; spelled out where the sentence reads it ("in Romans 8:28"); v., vv., ch. | 2026-10-27 |
| printer's misprints | be → he where the sense needs it, a wrong verse number fixed from the page | with evidence; a reference whose verse is not the one quoted is corrected to it (check every quotation against its verse, italic ones too: Indwelling Sin had 12) |
| & | → and | Indwelling Sin, Of Temptation (2026-11-09) |
| &c. | → etc. where the book sets `EXPAND_ETC` | per book |

A spelling review page lists the book's remaining old spellings with these defaults already standing
(modern American form taken; the author's own words, Latin, names and contractions kept); the editor
only overrides. Claude settles the unclear ones; nothing is left waiting on the editor by default.

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
better and stays closer to the author. Where the base printing slips in sense and the author's
own earlier edition (or Goold) has the word that makes sense, take it, listed for the editor
(Indwelling Sin: Saviours or *Believers* → *Deliverers*, 2026-11-09). Of Temptation's looser rule (whichever reads better in
modern English) stays that book's.

**Grammar modernization** (hath → has, thou → you, -eth → -s) is a per-book decision, off by
default. Simon Magus has it; ask before giving it to another book.

## 4. Typesetting

One house way for every book, so no book needs layout choices. Gathered from the books'
revision history (2026-11-08); colophon makes these the defaults.

**Follow the print's structure.** Its paragraph breaks stay (Gouge's "teacheth us, that" doctrine
paragraphs); its numerals stay as printed labels (1., I., First), never regenerated.

**Numbered outlines** (points, sub-points, reasons), the outline marks layout (the editor's
choice, 2026-11-09, over indents, first-line steps, margin rules and styled ordinals):
- every level full width, no set-in columns; each numbered point opens with a mark naming its
  level, `1.` / `(1.)` / `[1.]` / `1st.` as Goold marked Owen, and a little space before it
  (6pt at the top level, 3pt, then 2pt); the top level's ordinal word in small capitals;
- the author's ordinal words ("First,") keep their words and get the mark in grey before them;
  printed figures the same at every depth (Watson's "1.") are restyled to the level's shape;
  a text that already prints distinct marks (Goold's) keeps them and gains the spacing;
- print: `#show: outline-marks` (`scripts/outline_marks.typ`); ebook: `OUTLINE_MARKS = True`;
  chapters/typ and the TEI keep the levels as `./fgb outline` sets them;
- the level comes from the numbering (I. › 1. › (1.) › [1] › a.), settled by sense where the
  numbering is ambiguous; a run-in series ("…: 1. The Word preached. 2. …") is split onto its
  own lines;
- a list sits one step in, under the point it belongs to, never left of it; half a line above and
  below;
- levels are assigned by `./fgb outline` (colophon), with a later edition's distinct marks
  (Goold's 1. (1.) [1.] 1st.) as evidence where one exists; only its "?" places are judged;
- a deep outline (three levels or more) also gets edition headings over its main parts, in the
  author's or the contents page's words (Divine Cordial, mock-up "B").

**Braces:** with a closing term, read as a sentence; a small two-item brace runs into its
sentence; otherwise its branches are a list, with no bullets when the print has no numbers. A
genealogy or tree is a diagram, drawn in print, EPUB and reader alike.

**Margin matter:** labels (Doct., Answ., Use) and references are footnotes, placed after the
clause or name they gloss, not on a point's number; a note that only repeats the point's number
is dropped.

**Chapter summaries** (Owen's arguments): inset, a size smaller, ragged right, a line's space
before the chapter's first paragraph (2026-11-09). A printed chapter
title (Watson): bold, centred under "Chapter N", never doubled with the printed "CHAP. II.".

**Pages (print):** every footnote on its marker's page; no heading at a page's foot; no chapter
ending on 2-4 lines; no widow lines. `./fgb build` lists the first two as `page:` warnings;
clear them before a draft goes to the editor.

**Sign-offs:** each part on its own line set right; a valediction that ends in the name in
capitals ("… Devotion. THOMAS WATSON.") sets the name a line of its own (`SIGNATURE_NAME_LINE`).

**Every output alike:** print, EPUB, reader and the site's Then & Now show every feature before
a book goes to the editor.

## 5. Proofread

The house routine (`proof/`): Qwen flags small-word slips, the gap marker scores every word;
every flag is settled against the base printing and its witnesses; the top 15% of sentences by
score and a random 5% are read. The paragraphs Qwen cannot answer (long ones) are read in full,
and every reference's quotation is checked against its verse. A second random 5% is the
confidence check before the editor's reading.

## 6. Front and back matter

- Publisher page: the printed edition, "spelling modernized", and the transcription used (e.g.
  EEBO-TCP A53712). No method detail (2026-11-02).
- The print's title page and contents are not reproduced; the edition makes its own.

## 7. What still goes to the editor

Only these stop a book:

1. The base, when rule 1 leaves a real choice.
2. The batch of wording changes (rule 3).
3. Grammar modernization, if a book seems to want it.
4. The cover colour.
5. Sign-off.

Everything else follows these rules. A new question, once answered, becomes a rule here.
