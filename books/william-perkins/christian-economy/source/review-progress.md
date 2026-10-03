# Christian Economy review: progress

Branch `christian-economy-review`. No modern witness (README names none), so slips.py was not run.

## Tools
- sweep.py --early: 186 hits; all -eth verbs, Latin, period words, and the "great great" doubles that belong in the kinship lists. Nothing to fix from it except "commiteth" (now "committeth").
- refs.py --quotes: 209 refs, 1 missing (Coloss. 5. 11, printed in 1609; see the questions).

## Read
All files read for sense: dedication, chapters 1-18 (done).

## Fixes applied (batch 1, 64 replacements)
Listed in the scratch apply.py; they go into proofread-report.md by kind.

## Open questions (draft)
1. Coloss. 5. 11 (ch16): Colossians has 4 chapters. Col. 3. 11 or Gal. 5. 1?
2. commeth x3 vs cometh: an earlier review choice; restore "cometh"?
3. Remaining non-KJV biblical names: Anna (Hannah) x3, Thamar x2, Ruben, Vashi, Iischa, Ahashuerosh, Cham x2, Adoniah, Izreelite.
4. honor/honour, labour/labor: normalize?
5. ch5 "issue from out, & the same" -> "one"?
6. ch5 "whole sisters by the same father or mother" -> "and"?
7. ch7 "where he may conveniently from company" (a word lost)?
8. ch8 "Those that are at liberty, are tied necessarily" -> "are not tied"?
9. ch15 "intercession & rest" -> "intermission"?
10. ch3 Gen 1:28 "Bring forth fruit multiply" -> add "and"?
11. ch4 footnote "Jn sauorem Matrimony" (TCP misreading of "In fauorem Matrimonij")?
12. ch5 affinity trees (Isaac/Samuel): the TCP encoding is garbled; page image needed.
13. dedication footnote "1. King. 5. 6." (Adonijah is 1 Kings 1:5-6).

Not applied (the TEI cannot hold them): Laban nested under Bethuel in the ch5 tree (list nesting is not stored); a full stop after item VII in ch5's affinity list (the aligner read it as deleting the numeral VIII). Both go in the report.

## Status
Batch 1 synced; ./fgb check OK (chapter-05 differs only by the known #linebreak()). WIP committed.

## Next step
./fgb build perkins; check PDF text for quotes and markup; write proofread-report.md; final commit.
