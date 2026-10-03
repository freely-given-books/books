# Pilgrim's Progress review — progress (WIP checkpoint file)

Branch `pilgrims-progress-review`, worktree
`/home/courtney/Projects/fgbooks/books/.claude/worktrees/agent-a944362ba96a35ee3`.

## Tools run

- `sweep.py --early`: 514 candidates; all "words" are period forms/names except
  candidates to check: `Christana` (typo, Part II), `Satans`, `Romanus`,
  `Cyprusian`, `Abra`, `lillies`, `wholsome`, `befal`; spacing hits stage-08
  "before you ." (fixed), part-2 stage-08 "three against one ."; glued
  part-2 stage-06 "throne.Rev. 5:8".
- `slips.py` vs A30170: 0 places (no edits yet at the time; CCEL = printed layer).
- `drift.py --min 1` vs 1678 (scratchpad pp-drift.md): too noisy; used per-suspect
  via scratchpad `pp/w.py PHRASE` (searches the 1678 witness; `-c` CCEL).
- `refs.py --quotes`: 477 refs, 0 missing, 7 weak matches (all refs attached to
  non-quotations; 1 Cor 4:10 was wrong -> 5:10, fixed).

## Files read

- [x] apology.typ
- [x] part-1/stage-01 .. stage-09
- [ ] part-1/stage-10, conclusion
- [ ] part-2: title, authors-way, to-the-reader, stage-01..08

## Fixes applied so far (all in chapters/typ; not yet synced)

- apology: "set down" + ";" (1678); "in toad's head" -> "in a toad's head" (1678,
  metre); "My end-thy good" -> em dash; "understand" + ":" (1678).
- s1: "straight gate" -> "strait gate" (KJV Luke 13:24).
- s2: "God speed; So" -> ". So" ; "the picture a very grave person" -> "the
  picture of a" (1678); "said Christian may we" -> ", May" (1678); Matt. 18:30 ->
  13:30 (1678 margin, tares).
- s3: "cried, you are" -> "You" (1678); "1 John, 3:12" -> "1 John 3:12".
- s4: "traitor." -> "?" (1678); "land Num.13:32," -> "land, Num. 13:32,"; "His
  Candle" -> "candle".
- s5: "; So I spake" -> "; so" (1678); "1 John, 2:16"; "live with him; And" ->
  "? And" (1678); "tender Conscience" -> lowercase; "slander-a lot",
  "Secondly-", "holiness-heart-holiness" -> em dashes.
- s6: 1 Cor. 4:10 -> 5:10 (1678 margin); "Phil. 3: 20,21"; "he is-" -> em dash.
- s7: "saying, it runs" -> "It"; "said Hopeful, let us" -> "Let"; "Matt.26:14";
  "Job. 7:15"; "King of’ the" stray apostrophe.
- s8: "before you ." spacing.
- s9: missing close quote after Eccles. 10:3 quotation; "fleshy" -> "fleshly"
  (1678); "thieves; They" -> "they"; "thousand-else", "I am-and" -> em dashes;
  "the God of this world" -> "god" (1678, 2 Cor 4:4); "1 John, 5:21" -> "1 John
  2:21" (1678 margin; 5:21 is about idols); "Rom.10:4"; "action’s sake" ->
  "actions’ sake" (1678).

## To do globally (after reading)

- Ref spacing "Job 10: 21,22", "Heb. 9: 17-21", "John 10: 27-29", "John 5: 28,29";
  missing stops "Isa 64:6", "Rev 7:16", "Habak 1:2,3".
- Scan for hyphen-as-dash, "; [A-Z]" capitals, wrong curled quotes.
- Variant table: Emmanuel/Immanuel, shew/show, aught/ought, Saviour/Savior,
  labour/labor (CCEL American), Psa./Psalm/Ps., Zion/Sion.

## Needs your decision (draft)

1. Part I s3 l.119: "Formality and Hypocrisy" — the character is Formalist; 1678
   reads "Formalist". Recommend "Formalist".
2. Part I s8: "Emmanuel's land" vs s3 "Immanuel's land"; 1678 has Immanuel both.
   Recommend Immanuel (check Part II usage).
3. Part I s8: "Hymenius" (1678 "Hymeneus", KJV "Hymenaeus"). Recommend
   "Hymenaeus" (KJV) or keep.
4. Part I s6: "they that had ought to say" (1678 same; book has "aught"
   elsewhere). Recommend "aught".

## Next step

Read part-1/stage-10.typ, then conclusion, then Part II in order.
