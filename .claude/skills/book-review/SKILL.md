---
name: book-review
description: A thorough editorial review of a Freely Given Books edition's text, to make it shelf ready — proofreading chapters/typ against the early printed text and any modern witness, fixing OCR and scanning slips (he/be, b/h, "Gentles", "the church lied into the wilderness"), dropped or doubled words, broken quotations and punctuation, swallowed Typst semicolons, wrong scripture references, inconsistent spellings and headings, while understanding 16th–19th century English (hath, -eth, 'tis, shew, "prevent" meaning go before) and keeping it. Use this whenever the user asks to review, proofread, edit, check, clean up or "make shelf ready" a book, asks whether a book has errors or is ready to print, wants OCR errors fixed, or wants a book's text, headings, nested numbered outlines (Owen's I. › 1. › (1.) › [1.]), scripture references or consistency checked — even for one chapter, and even if the book is not yet on the TEI pipeline.
---

# Book review: making the text shelf ready

You are the edition's copy editor and proofreader. The goal is a text a
reader can trust: no scanning slips, no lost words, no broken quotations,
no wrong references, no inconsistencies a careful reader would notice — and
none of the period English damaged in the process. When you finish, the
user should be confident the book can go to print.

The books are early-modern and later Christian works (1600s Puritans,
Bunyan, Edwards, Spurgeon), edited *lightly*: modern spelling and
punctuation, the author's words and grammar kept. A more modern edition may
come later from the same TEI, so this review does not modernize grammar.

## What you work on

A book is `books/<author>/<book>/`. The text is `chapters/typ/*.typ`
(Typst); for TEI books, `source/<book>.tei.xml` holds the early printed text
and every editorial decision, and `./fgb sync <book>` folds edits in
`chapters/typ` back into it. **Edit only `chapters/typ`**, never the TEI or
the untouched source files. Read the book's `README.md`,
`source/editorial.py` (`REPORT_NOTES`), `source/review-report.md` and any
`source/witness-report.md` first: they record deliberate choices (Edwards
quotes the BSB; Brooks keeps Latin beside its translation; passages left
out on purpose) that a review must respect, not "fix".

Your sources of evidence, best first:

1. **The early printing**: the TEI's printed layer. `tei_extract.py
   <tei> OUT --layer reg --only-auto` gives it with spelling modernized and
   nothing else changed; `--layer orig` gives it as printed. `./fgb find
   <book> WORD` shows a word as printed and as decided; `./fgb page <book>`
   opens the side-by-side page.
   For a CCEL base, the early printing is the edition CCEL keyed (Goold's
   Owen, Beveridge's 1845 Calvin): its archive.org OCR and page images. Check
   CCEL against it volume by volume with a comparison agent; the method,
   CCEL's typical defects and the scripts are in the eebo-tcp-book skill's
   `references/ccel-books.md` (worked example: Calvin's
   `source/witness-check/`).
2. **A modern witness** of the same text (CCEL, Monergism PDF, Chapel
   Library EPUB, an old copy): compared, never copied — some are under
   copyright and none is committed.
3. **The Bible** the book quotes (KJV unless the book says otherwise).
4. Your own reading, and `references/period-english.md` for what looks
   wrong but is not.

## The review, in order

### 1. Run the tools (minutes, finds the mechanical errors)

```sh
PY=$PWD/colophon/.venv/bin/python                    # at the repo root (uv; ./fgb makes it)
$PY colophon/sweep.py books/<author>/<book> --early   # spacing, punctuation, quotes, \; , words
$PY colophon/slips.py <tei> WITNESS                   # if there is a witness
$PY colophon/refs.py books/<author>/<book> --quotes [--bible bsb]
./fgb check <book> && ./fgb build <book>                 # verify, Lulu checks, epubcheck
```

`slips.py` lists where the edition departs from the early printing while
the witness agrees with it — the likeliest slips. `refs.py` lists references
to verses that do not exist and quotations that do not match the verse they
cite. Every hit is a candidate to read in context, not a fix to apply.

**Thin spaces (any text keyed from an 1800s edition).** Victorian printers
set a thin space before : ; ? ! and inside quotation marks, and OCR or
keying turns it into a full space ("Cicero : Qui deos", "“ Prince of
Peace.”", "others ; see"). `sweep.py`'s spacing hits catch them; in a CCEL,
Goold, Beveridge, Grosart or M'Millan text clear every one (a French or
Latin quotation's spacing included: the edition is English). The 1600s TCP
texts do not have this.

### 2. Read the book (the part the tools cannot do)

Read every file, start to finish, in passes of a few thousand words. Read
for sense, as a careful reader would. For each sentence ask: does it say
something? A sentence that does not parse usually hides a slip. Look for:

- **Scanning and OCR slips**: real words in the wrong place (`he` for
  `be`, `lied` for `fled`, `sold` for `soul`, `bead` for `head`, `title`
  for `little`, `form` for `for me`); the confusions are listed in
  `references/period-english.md`. Check each suspect against the early
  printing before changing it.
- **Lost and doubled words**: a sentence missing its verb or object, "the
  the", a list missing a member ("believe … plead … hope" in the print,
  two of three in the copy).
- **Quotations**: every opening mark closed, in the right direction, at the
  right place; a quotation's wording matching its source; nested quotes
  consistent. Typst curls straight quotes; a straight apostrophe inside a
  single-quoted passage closes it, so the book writes `’` there.
- **Punctuation**: doubled marks, a full stop mid-sentence ("lastly.
  didst"), a lost comma that changes the sense.
- **Latin, Greek and Hebrew**: misprints (`Sapieus miner` for `Sapiens
  miser`, `harebit` for `haerebit`), accents and breathings, and that a
  translation beside them says what they say.
- **Names**: the book's own form, consistently (Zion or Sion, not both;
  KJV forms for biblical names unless the book chose otherwise).

**A whole book (tens of thousands of words) is read by subagents**, the way
Brooks's *Precious Remedies* was (2026-10). Token use matters to the user,
so:

- Split the book into parts of about 20,000–25,000 words. Give each reader
  the same written brief: what to fix, what to ask, what never to change,
  and the evidence files (the edition, the `--layer orig` extraction, the
  witness). Brooks's brief is `references/reader-brief-example.md` and its
  applier `references/apply-proposals-example.py`; adapt the paths.
- Run the readers at **medium effort** (the Agent tool's `effort`), **one
  at a time**. Two Opus readers at once hit the session limit. At medium, a
  reader found as much as one at high (about 13–15 proposals per 1,000
  words, scrambled margins and mangled Latin included) for about 25% fewer
  tokens.
- Tell readers to keep lean: read each edition file once, Grep the 1653
  text and the witness only where they doubt, and write commands that need
  no permission (one plain command per call, no `cd &&` or shell variables).
- Readers **propose; they don't edit.** Each writes JSON lines (`file`,
  exact unique `old`, `new`, `class` fix/ask/note, `kind`, `why`), appending
  after every file so a usage cutoff loses little. Apply the `fix` lines
  with a script that refuses any `old` not found exactly once, then
  `./fgb sync` and `./fgb check`.
- A slip that repeats across the book (sentence case, a spelling the
  machine got wrong) is a machine rule in colophon or `editorial.py`, not
  hundreds of hand edits. Tell later readers not to propose it.
- Settle the `ask` items yourself at **high effort**, in one batch, and put
  them to the user grouped with recommendations. Record them in
  `source/proofread-report.md` so they survive the session. Group by the
  evidence, one AskUserQuestion question per group with the recommended
  option first (Grace Abounding: CCEL against both witnesses / later
  witness only / missing references / small style points): four questions
  settled 66 items. Apply the answers with the same applier, taking the
  chosen proposal ids, plus hand edits for the ones the answer reshapes.
- **A second pass pays when there is a new witness.** Grace Abounding,
  proofread once already, gave 67 fixes and 66 questions in 43,000 words
  once Offor's 1855 text was added (2026-10-18). The brief for a CCEL book
  with two witnesses is `references/reader-brief-ccel-example.md`.
  Precious Remedies, proofread once against Monergism's keyed Grosart,
  gave 141 fixes and 43 questions in 98,000 words against Grosart's
  *printed* edition (archive.org OCR): the footnotes the keyed copy drops
  are where he corrects references, names and Latin, and he records the
  first edition's readings. Prefer a printed scholarly edition's scan over
  a keyed copy of it, and tell readers to check every footnote there.
- **Apply a settled spelling everywhere, by grep, the day it is settled.**
  The first pass settled Ahithophel, Jerome, temptation and others, but
  applied them only where a reader had proposed them; the second pass
  found them still printed the old way in other files.
- A rule like "hyphenate the a- prefix" (a-crying) needs reading each hit:
  most "a turning" are the article ("repentance is a turning from sin");
  only progressives after be/day ("they are every day a-crying out") take
  the hyphen. Expanding "&" likewise keeps it in Latin ("ille hodie & ego
  cras"): list every hit with its words around, then keep a short list.
- Don't apply one reader's fixes while another is reading the same file:
  merged paragraphs shift its line ranges. Apply after the last reader.

**Keep the main session lean** (the readers' tokens stay in their own
context; yours don't). Print proposals one line each (`old => new | why`,
cut to ~150 characters), never the JSONL whole; spot-check a few fixes per
reader with one Grep in the witness rather than all of them; read a book
file by offset or with a Python slice around the passage, not whole; look
at PDF pages as low-resolution montages (`pdftoppm -r 40`, `montage -tile
8x2`), and only the pages in doubt at 70 dpi.

### 3. Check what spans the book

- **Scripture references**: one style through the book (`Romans 11:20` or
  `Rom 11:20`, colon or period); each points at the verse it quotes; ranges
  and lists well formed (`11:20, 21`, `3:22-23`).
- **Consistency**: the same word spelled the same way throughout (every
  one/everyone, Saviour/Savior, shew/show, labour/labor, today/to-day),
  numbering styles, quotation-mark style, dashes, `etc.`. Build a table of
  variants with counts; propose the book's majority form.
- **Printed lists and braces in the PDF**: look for bullets carrying typed
  numbers (`- 1\. …`). Write them as `+ …` without the numeral, and the sync
  numbers the list, keeping the printed numeral as a label. Also look for a
  brace whose closing term (`{1. In the necessity / 2. In the efficacy} Of
  Baptism.`) is left on a line of its own after the list. Read that brace
  into its sentence ("In two things do Papists exceed: in the necessity and
  in the efficacy of Baptism."); the sync marks the table
  `@rend="inline"` (colophon 0.12.2+). A brace can only be read inline
  whole, not in part, and two braces can't be nested into one list. In
  those cases use a paragraph or numbered paragraphs (Gouge §49, §56).
  In a brace read inline, type a comma outside the italics
  (`the #emph[soul], the #emph[body]`, not `#emph[soul,]`), or the comma
  lands in the next cell's reading and comes back as "soul ,". After every
  sync, diff `tei_extract --layer reg` against `chapters/typ`: a reading
  the TEI cannot hold (a list item split into a paragraph, a sub-list
  moved under a printed "4." paragraph) comes back in another shape, so
  put it back and note it rather than forcing it.
- **Typesetting sweep of the PDF** (Gouge, all four volumes 2026-10-14):
  one agent per volume at medium effort, one at a time, each writing JSONL
  (page, file:line, excerpt, proposal, small|template). Give it the known
  kinds so it only counts them: an epigraph verse opening "23." set as a
  list item; footnote markers in "(¹word", at a paragraph's start, straight
  after an item number, or two side by side ("223224"); a margin note
  split into two notes mid-phrase; two lists separated by a blank line that
  keep counting (restart with `#[ #set enum(start: 1) ... ]`); a sub-list
  not indented; a bold "Object./Quest." label alone or a roman one among
  bold ones; stray "]"; runs of one-line paragraphs. Markers move by a
  bracket-aware script (marker before the "(", or after the first word);
  side-by-side markers and label styling are template/structure work.
  Printed tables "laid one against another" are PARALLEL_TABLES (two
  columns, fgbooks 0.10.0).
- **Nested outlines** (Owen: I. › 1. › (1.) › [1.] › 1st.): readers lose
  their place when a series runs over several chapters, when an editor's
  numerals stack ("I. 1. (1.)") or clash ("2." for a second reason under
  Rule 1 and "2." for Rule 2), and when ordinals hide in mid-paragraph. Map
  the whole tree first (one agent: every marker with file, paragraph and
  gist, against the first edition and the later editor's scan). Then fix
  what is wrong (a CCEL slip like "[4.]" for "4.", a level the first edition
  contradicts, paragraphs an editor ran together), and offer the user
  edition headings for the top levels (`EDITION_HEADINGS`, as Brooks and
  both Owens have: "=== I. What It Is to Mortify a Sin", "==== First
  Direction: …"). Where a heading carries a number, the paragraph drops the
  *editor's* added numeral; the author's own numerals and ordinals stay.
  Number an implicit "1." when a series starts at "2." (ask first).
- **Headings and titles**: chapter titles, the headings the edition adds,
  running-head short titles — consistent title case (lowercase articles,
  short prepositions and conjunctions), parallel wording within a series
  ("1. The Most Eminent Saints…", "2. Christ Much Exercised…"), no typos,
  short titles that fit one line (`./fgb pdf` warns when a running head
  breaks the top margin).
  Read the PDF's contents page against the chapters: the template pairs
  `#metadata[...] <short>` lines with chapters *by position*, so a book
  `.typ` with fewer short titles than chapters lists every later chapter
  under the wrong name and runs pages under the previous chapter's head
  (Grace Abounding and Keach, 2026-10-18). Every `#include` gets one.
- **Look at the print, not just its text.** A montage of the first 16
  pages and each chapter's opening page shows what `pdftotext` cannot: a
  subtitle run into the first paragraph, a heading's lone last word, the
  wrong running head. A print-only spacing fix may go in the book's `.typ`
  as a show rule (Grace's dedication: `#show align: it => if it.alignment
  == center { it + v(0.8em) } else { it }`; a `.where(alignment: ...)`
  selector does not match under the template). Text, never there.
- **An opening word in capitals** ("CHILDREN, grace be with you") set as
  small caps: `OPENING_SMALLCAPS = True` in `editorial.py`, then type
  `#smallcaps[Children]` in `chapters/typ` and sync. The review alone cannot
  add small caps (check [2] fails); CCEL books take the setting too.
- **An author's books are a set.** Same cover palette and spine style, and
  the same ebook CSS bar the book's own needs: diff `cover.typ` and
  `ebook-override.css` against the author's other books (Grace Abounding's
  ebook set paragraphs flush while Pilgrim's indents; fixed).
- **A CCEL text against two witnesses** (Grace Abounding, 1666 and Offor
  1855): CCEL's keyed text often smooths the author (word order, "them
  words" → "those words", "a-coming" → "coming") and drops short words. The
  user's rule there: restore only words CCEL *lost* where both witnesses
  agree; keep CCEL's order and forms; in passages only the later witness
  has, follow it. Offor's *Works* (OCR in `~/.cache/fgb-scans/bunyan/`) is
  the witness for Bunyan's enlarged texts.

### 4. Fix and ask

**Fix yourself** what is unambiguous, and list it afterwards: misprints with
the early printing (or the witness) on your side, stray spaces, broken
quotation marks, swallowed semicolons, glued or doubled words, a
reference that is plainly mistyped (`1 Kings 17:4, G` → `17:4, 6`).

**Ask first**, with a recommendation, for anything that changes the
wording on purpose: restoring text the copy lost or cut, undoing an older
editor's change, a reading where the evidence is split, normalizing
variant spellings across the book, rewording a sentence that reads as a
mistake today ("other men, good wit" → "other men of good wit"), changing
a heading. Group the questions; show each with its context and the early
printing's reading.

Applying proposals from an agent's report, mind what went wrong before:
an `old` that stops inside `#emph[` gets mangled ("(ransom)[ransom])"), so
skip any change touching markup and do it by hand; Greek may be decomposed
(letter + combining accent) in the file and composed in the report, and
quotes curly in the file and straight in the report, so match tolerantly
and write the file's own form back; a fix taken from an older printing can
bring that printing's punctuation along ("magic, (Exod. 9:11)") where the
book has its own style. `./fgb check` [2] catches broken markup. A proposal
that moves a footnote marker can double the word it moves past ("34. But¹
But as Paul") and drop an escape ("34\." written "34."): read every such
proposal before applying it (Calvin, 2026-10-16).

**A big CCEL book already compared word by word with its printed edition**
(Calvin: 1845, 999 corrections) does not need a sentence-by-sentence read
(670,000 words, ~30 readers). The user chose a targeted review instead: the
tools; `refs.py --quotes` weak matches compared with the printed edition's
reference after each quotation (roman *l* read as 1, *lv* as 4: Jer. 50:25,
Isa. 55:3); consistency tables (spelling, reference abbreviations, ranges);
headings and running heads (generated files can bypass the corrected text);
and a typesetting sweep per volume from `pdftotext -layout`, rendering a page
only when the text cannot tell, every wording proposal checked against the
printed edition's OCR. It found about 130 real problems in six volumes:
unclosed quotations, stray parentheses and note numbers, wrong words,
Greek/Latin/French misprints (some the printed edition's own: fix plain
misprints, keep period spellings such as 16th-century French).

Edit `chapters/typ` with exact, unique replacements (match across line
breaks; keep the file's wrapping). Mind Typst: `#`, `[`, `]`, `\` are
markup; write `\;` after a call like `#emph[..]`; keep `#footnote[..]`
anchors where they were. After each batch: `./fgb sync <book>` (it lists
the decisions that changed), then `./fgb check <book>`.

### 5. Prove it and report

Before calling a book shelf ready, all of these hold:

- `sweep.py` hits are fixed or explained; `slips.py` items resolved or
  listed as kept on purpose; `refs.py` shows no missing verses and every
  weak quote match read.
- `./fgb check` is OK; `./fgb build` passes the Lulu checks (footnote
  warnings explained) and epubcheck.
- The compiled PDF's text has no quotes curled the wrong way (`,‘ word`,
  `‘ `, `’’`) and no stray markup (`#emph`, `\[`).

Report to the user in plain words: what you fixed, by kind, with a few
examples each; the questions, with your recommendation; anything left as is
on purpose and why; and the checklist above. For a long list, write it to
`source/proofread-report.md` and summarize. When the user settles the
questions, record the answers in the report and tick its checklist (stale
"questions are open" boxes outlived their answers in three books). Commit
and push without asking (the user's standing instruction).
