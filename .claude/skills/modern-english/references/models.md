# Models and effort for each job

The Agent tool takes `model` (haiku, sonnet, opus, fable) and `effort` (low, medium, high, xhigh, max). This file
is the skill's instruction to set them, so pass them on every spawn as below. The rule of thumb: **scripts find,
cheap models sort, strong models judge.** Never ask a strong model to scan 80,000 words for a list of words, and
never let a cheap model decide a meaning.

## The table

| Job | Model | Effort | Size of one task | Why |
|---|---|---|---|---|
| Coordinator (one per book, background) | opus | default | the whole book | Holds the plan, settles findings, writes edit scripts |
| Drafter | opus | high | about 7,500 Classic words (`slice.py`) | Voice, meaning and the false-friend choice all start here; mistakes made here are the expensive ones |
| False-friend classifier (`ff-scan.py` hits) | haiku | low | about 60 hits | Yes/no per hit: "does this word mislead a modern reader here?" High recall, so "doubtful" counts as yes |
| False-friend decider (the hits haiku kept) | sonnet | medium | about 40 hits | Picks the rendering in context, consistent with the glossary |
| Sentence check (`split-points.py` rows) | haiku | low | about 40 paragraphs | Does each new sentence parse? Is any sentence a fragment? |
| Referent check (the same rows) | opus | high | about 40 paragraphs | Does every pronoun and subject still point where the author's did? Was speech made indirect without changing the speaker? |
| Scripture lean check (`audit-scripture.py` + each quotation) | sonnet | medium | about 60 quotations | Does the next sentence lean on a word the BSB dropped? |
| Meaning readers, pass A | opus | high | at most 10,000 Classic words | Sentence by sentence, every paragraph, one verdict per paragraph (`coverage.py`) |
| Meaning readers, pass B | sonnet | high | at most 10,000 words, **cut at different places from pass A** | A second model reads differently; overlapping slices put every seam in the middle of somebody's read |
| Review of the edits (diff of every audit and assessment edit) | sonnet | high | all the edits of one pass | Edits made by the audit have introduced errors ("nothing will be effectual"; humors → infection); nobody checked them |
| Independent assessment | fable, or opus | xhigh | coordinator only; its readers as pass A | The final judgment and score; its readers' coverage is proven like the audit's |
| Classic suspects against page images | opus | high | one TSV of suspects | Reading the scans and deciding printer's error vs author's slip |

Use effort `max` only when the editor asks for it.

## Coverage is proven, not promised

Every reader (audit or assessment) returns two files:
- **verdicts:** one line per paragraph of its assignment, `file  n  ok`, or a finding row;
- **a clause ledger:** one row per Classic sentence or clause it compared,
  `file  n  classic clause (first words, copied)  modern words carrying it  = or ≠`.

`coverage.py PAIRS ASSIGNMENT READER.tsv LEDGER.tsv` must pass before the reader's findings are accepted. It
checks that every paragraph has a verdict, that ledger rows cover at least 80% of each paragraph's sentences,
and that each row's Classic words are really in that paragraph. A run that fails is redone. A brief may never
invite sampling. If a reader must stop, it says which paragraphs it did not read, and they go to a new reader.

**Not a clock.** A timing gate of 10 minutes per 10,000 words was tried on the first four re-checks
(2026-11-17) and dropped. Honest opus and sonnet readers read 2,000–3,500 words a minute and failed it on every
run, and small runs passed it only because of start-up overhead. Keeping the ledger is what made readers
compare clause by clause, and unlike a time, a ledger can be checked. The other check on reading is
agreement: the same finding reached independently by readers of both passes.

## Calibration: choosing the drafter and reader models

Model quality changes with each release, so the table above is the current best guess, not a law. Re-check it
when a new model arrives, or once every few books:

1. Take two passages of about 1,200 Classic words each from the next book: one hard periodic passage (Owen, Perkins)
   and one plain or narrative passage.
2. Draft each with three or four candidate settings (for example sonnet/high, opus/high, fable/high, opus/medium),
   with the same brief.
3. Strip the labels. Have one strong reader (fable or opus, xhigh), which drafted none of them, score each draft
   on the assessment rubric. It also counts meaning errors, false friends left, voice lost and lines that need an
   edit, per 1,000 words.
4. Record the result in `references/calibration.md` (date, models, scores, errors per 1,000 words, tokens used).
   Choose the cheapest setting within half a point of the best score with no more meaning errors. Change the
   table only on that evidence.

The same test works for the readers: plant ten known errors (a dropped "not", a pronoun shifted, a false friend
put back, a BSB word removed) in a copy of 3,000 audited words, and count how many each candidate reader finds.
