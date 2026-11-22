---
name: modern-english
description: Make, audit or fix a book's Modern English edition, the second edition beside the Classic for readers who find 17th–19th-century English hard going (ESL readers included). Every point is kept and nothing is abridged; the author stays recognizable ("ahh, this is John Owen"). Scripture is quoted from the BSB lightly adjusted, plural you is marked you⁺, and false friends are replaced in the text. Use it whenever the user says to modernize a book or "do the Modern English" of one, to continue or finish a modernization, to audit or re-check a Modern English text (meaning audit, false friends, referents, Scripture wording, plural marks, headings), to apply the editor's or an outside reviewer's (GPT's) points to one, to run an independent assessment, or to choose models and effort for this work. Also use it for sermons or other texts made into modern books the same way. For the Classic text's own proofreading use book-review; for building a new book's TEI use eebo-tcp-book.
---

# Modern English editions

The Modern English edition puts a book into today's English **without abridging and without losing the
author's voice**. The editor's test: a reader should think "ahh, this is John Owen", never "this is a total
rewording of Owen" (as Updated Works does it). The Classic is the critical edition; the Modern sits beside
it, paragraph for paragraph.

**The rules are `MODERN-ENGLISH-RULES.md` at the repo root.** They are binding and grow with each book; read
all of them before anything else. This skill is the method. When the editor settles a new question, it
becomes a rule there.

## What a finished book has

In `books/<author>/<book>/`:

- `chapters/modern/` with the same files and paragraphs as `chapters/typ`;
- `<book>-modern.typ` (print), `cover-modern.typ` (the Classic cover labelled MODERN ENGLISH, with a BSB verse
  on the back), `ebook-front-modern.html` (with the front note on Scripture and you⁺);
- `editorial.py` EPUB/PRINT entries for the modern edition, made by `scripts/scaffold.py`;
- `source/modern-glossary.md`, the book's binding renderings: kept terms, recurring words, the key verses as
  adjusted, its false friends.

Plus a books PR (the editor merges), drafts in Nextcloud, the side-by-side page with the editor's questions
at the top, and one Vikunja task per question.

## How to run a book

Run each book as **one background coordinator subagent** (general-purpose, opus). It spawns its own
drafters and readers, and the main session stays small. Brief it with this skill, the paths, and anything
the editor has said about this book. A book of 80,000 to 100,000 words takes about 2 to 3 hours of agents.
Everything below is the coordinator's job, in order. Each stage has a **gate**: do not go on until it passes.

Work files go in `~/Projects/fgbooks/work/<book>-modern/`, never in /tmp. Use a worktree from the newest
branch that carries the latest rules (`git worktree add ../wt-<book>-modern -b <book>-modern origin/<base>`,
then `git submodule update --init`). Scripts are in `scripts/`, run with `python3`. `side_by_side.py` needs
colophon's venv: `colophon/.venv/bin/python`.

### 1. Prepare

1. Read the rules, the book's README, `source/editorial.py`, and the Classic's notes on its base text.
2. **Settle the shared decisions before drafting**, in `source/modern-glossary.md`:
   - the key verses the author expounds, rendered once (check particles: "that" as outcome vs "so that"
     as purpose; "and" vs "but"; the word his exposition leans on);
   - his central terms (kept, as "closet" in Brooks, or rendered one way);
   - the labels (Obj. → Objection; Answ. → Answer);
   - the false friends of this author.

   Start from the same author's earlier glossary, if one exists. Put to the editor (Vikunja) any choice that
   shapes the whole book. Draft with your recommendation meanwhile.
3. `slice.py BOOK_DIR WORK_DIR` cuts slices of about 7,500 words, as mini book folders, and writes
   `plan.json`.
4. Write the drafter brief from `references/drafter-brief-example.md` (Secret Key's, the most complete). Keep
   all of these:
   - headings modernized too;
   - the false-friend list up front, replace, never gloss;
   - the BSB lean check;
   - the you⁺ rule (every plural you/your/yours/yourselves, rules §4.2);
   - gendered language kept;
   - no fresh images;
   - a reply that lists suspected Classic slips and recurring terms the glossary lacks.

   **Never write "keep the word X" for a word whose sense has shifted.** One brief did that ("enthusiasm")
   and the book carried 418 false friends.

### 2. Draft (opus, high)

Run all slices at once, or in waves of 6 to 8. After each drafter finishes, run `check.py WORK_DIR/<L>`
(paragraph counts, opening marks, references, notes, length ratio, archaic forms) and send its slice back
until the result is clean.

**Gate:** every slice is clean in check.py. Collect each drafter's suspected Classic slips into one
`classic-suspects.tsv`.

### 3. Join and lint

1. `join.py WORK_DIR`. Then `harmonize.py BOOK_DIR` (LORD → `#smallcaps[Lord]`, Holy Ghost → Holy Spirit,
   straight quotes, archaic or unchanged headings).
2. `audit-pairs.py BOOK_DIR AUDIT_DIR`, then on its `pairs.jsonl`:
   - `lint.py` (markup, references per paragraph, balance, headings, outline marks, length, archaic forms,
     you⁺ against ye, ellipsis seams, notes or Latin changed);
   - `renderings.py` (one verse quoted two ways; openers);
   - `audit-negation.py`;
   - `audit-terms.py`;
   - `audit-scripture.py BOOK_DIR`.
3. Settle every lint and rendering line, and fix them in `<book>-coordinator-edits.py`.

**Gate:** lint is clean or every remaining line is explained; renderings are settled.

### 4. Classic suspects

Check every suspect against the print's page images (`work/<book>/scan-*`; fetch and cache them if missing).
Settle each as a printer's error or wrong reference (fixed in **both** editions: the Classic through
`chapters/typ`, then `./fgb sync`, `./fgb check`), or as the author's own slip (kept, and listed for the
editor).

Also grep the Classic for references our restyling mangled. The print may name the chapter first ("the 12.
Rom. 9. v."), and the restyling read the verse as a chapter. Earlier editions (Grosart, Monergism) often copy
a misprint; when one is fixed, say so.

### 5. Targeted checks (`references/check-prompts.md`; models in `references/models.md`)

1. **False friends:** `ff-scan.py PAIRS references/false-friends.tsv <kept,words>`. haiku classifies the hits
   in batches of about 60, sonnet decides the ones it flags, and the coordinator applies them. Add every new
   rendering to the glossary.
2. **Split points:** `split-points.py PAIRS`. haiku checks every row for grammar; opus checks referents.
3. **Scripture lean:** sonnet, on every quotation from `audit-scripture.py`.

**Gate:** every row answered; fixes applied.

### 6. Meaning audit: two passes, coverage proven

1. `assign.py PAIRS AUDIT_DIR/readers` writes pass A; `assign.py ... --pass B` writes pass B, offset by
   half a run.
2. Pass A readers are opus/high and pass B readers sonnet/high, each at most 10,000 words, all with
   `references/reader-brief.md`.
3. For each reader run `coverage.py PAIRS <reader>.ids <reader>.tsv <reader>-ledger.tsv`: a verdict for every
   paragraph and a clause ledger that covers it. **A reader that fails is redone.** Time is not the test.
4. Settle every finding: accept, adjust, or reject with a reason. Put the corrections in
   `<book>-audit-edits.py`, each edit with a comment saying why. Where two readers disagree, read the Classic
   yourself.
5. **Review the edits:** sonnet/high on the edit script's diff (`check-prompts.md` §6).
6. Plural marks: `plurals.py BOOK_DIR` lists every unmarked you/your in a paragraph that carries a you⁺;
   settle each against the Classic (ye / you to a group, or thou / a polite singular you) and mark the plurals
   (`--write` marks them all, only for a book whose plural-address paragraphs speak to the group throughout).
   Run it again after any edit script.

### 7. Independent assessment (fable or opus, xhigh)

Use a fresh agent from `references/assessment-prompt-example.md`, which must not open the audit. Its readers
work as in stage 6, with `coverage.py`, so the coverage is proven. It writes `assessment.md` (coverage, a
score out of 10, a verdict, findings) and `corrections.tsv`.

Apply its corrections in the wording closest to the author, not the reviewer's paraphrase, and run the
review of edits on them. The order matters when re-running: audit edits first, then the assessment's.

### 8. Build, page, hand over

1. `scaffold.py BOOK_DIR SLUG EPIGRAPH_RE EPIGRAPH_MODERN` (first time only). Fix the duplicate subtitle it
   writes, and set the ebook epigraph by hand. Check that the MODERN ENGLISH label clears the cover art.
2. `./fgb build <book>`. Check:
   - both EPUBs pass epubcheck;
   - the Modern EPUB's note count equals `chapters/modern`'s;
   - page fit: no chapter ends on 1 to 4 lines, and no note is set off its page. `pagefit.py` tightens
     tracking on a chapter.
3. Make the side-by-side page: `side_by_side.py BOOK_DIR TITLE OUT.html NOTES.html`. NOTES has the editor's
   questions at the top, each with the passage. Copy it and the drafts to Nextcloud (see the
   `review-locations` memory).
4. Commit with explicit paths. **Never `git add -A books` after a build**: it picks up regenerated
   `.cover-ground.png` files. Push and open the PR, with a body like
   `work/precious-remedies-modern/pr-body.md`.
5. Vikunja: one stand-alone task per editor question, made with `card()`. It gives where, the texts, the
   question, numbered options, your recommendation and what happens next. Add a note on the book's queue
   task.

### 9. After the editor

- **Answers** come as "task N option M": apply each, rebuild, push, and tick the task with a done-note.
- **An outside review** (GPT) comes back as a ledger. Judge each point against the Classic and apply it in
  the author's own wording. Show the editor the before and after. Points the editor settled (rules §7b) are
  not reopened.
- **A lesson that applies to every book** goes into `MODERN-ENGLISH-RULES.md` (and the false-friend lexicon
  or these prompts) in the same PR.

## What the stages catch

From a 2026-11-17 study of every review so far (about 1,000 audit findings, 240 assessment edits, the GPT
ledgers, and a 1,285-word false-friend sweep):

| Error | Where it hides | Caught by |
|---|---|---|
| False friend left (professors, discover, convenient, "to this day") | everywhere; the commonest by far | lexicon scan + classifier, drafter list |
| Pronoun or speaker shifted at a new sentence boundary | rebuilt sentences, speech made indirect | split-points + opus referent check |
| Fragment or broken grammar | new sentence boundaries | split-points + haiku |
| Lost negation or limiter ("only", "all") | rebuilt clauses | audit-negation (one strong limiter is enough) + readers |
| BSB lost the word the author leans on | quotations he expounds | Scripture lean check |
| Wrong or added reference; a quotation cut badly | quotations | lint (references, ellipsis seams) |
| One verse or term rendered two ways | across slices | renderings.py |
| An audit edit that made things worse | correction scripts | review of the edits |
| Voice thinned (an image flattened, a pun lost) | anywhere | assessment, editor |

The residual after all our stages, on the books an outside reviewer read in full: about one real fix per 50
to 150 rows, mostly false friends. The scan in stage 5 targets exactly that.

## Models and effort

See `references/models.md`: which model and effort for each job, why, how big each task is, and how to
calibrate when a new model arrives. In short, scripts find, haiku sorts, sonnet decides narrow questions and
gives the second reading, and opus or fable drafts and judges. Pass `model` and `effort` on every spawn.

## Scripts

| Script | Does |
|---|---|
| `slice.py`, `join.py` | slices in book order (long chapters cut at headings) and back, by `plan.json` |
| `check.py` | one slice or book: paragraph and mark counts, references, notes, length, archaic forms (VERSE=1 for verse) |
| `harmonize.py` | LORD, Holy Spirit, quotes, headings after the join |
| `audit-pairs.py` | `pairs.jsonl` + `pairs-<file>.md`, in book order |
| `lint.py` | whole-book mechanical checks |
| `renderings.py` | one verse or opener rendered several ways (within one book, or across books with several PAIRS) |
| `ff-scan.py` | false-friend hits with the Classic paragraph (`references/false-friends.tsv`) |
| `split-points.py` | rebuilt paragraphs for the grammar and referent checks |
| `audit-negation.py`, `audit-negflag.py`, `audit-negshow.py` | negation and limiter differences, and showing them |
| `audit-terms.py`, `audit-show.py` | technical terms that must survive (not false friends) |
| `audit-scripture.py`, `bsb.py` | quotations against the BSB; verse lookup |
| `audit-grep.py`, `audit-match.py` | look a phrase up in the pairs |
| `plurals.py` | unmarked you/your in plural-address paragraphs (every plural is marked) |
| `assign.py`, `coverage.py` | reader runs for two offset passes; proof (verdicts + clause ledger) that each read everything |
| `scaffold.py`, `pagefit.py`, `side_by_side.py` | edition files, page fit, the editor's review page |
