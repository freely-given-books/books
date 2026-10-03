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
- [x] part-1/stage-10, conclusion
- [x] part-2 title, authors-way, to-the-reader
- [ ] part-2 stage-01..08
- [x] part-2 stage-01, stage-02

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

- s10: "such conviction as tend" -> "convictions" (1678); "the sight of at it first" ->
  "of it at first" (1678 "of it first"); "answered, they" -> "They"; "be: And" ->
  "and"; "would; But" -> "but"; "1 John, 3:2"; CCEL small-caps lines lowercased ->
  "Blessed", "Enter ye into the joy of your Lord", "Blessing ... unto the Lamb";
  stray paragraph "Isa. 26:2." joined to the paragraph it belongs to.

- II authors-way: "answer" labels -> "Answer"; "objection iv" -> "Objection iv"; "His Head" -> "head".
- II to-the-reader: "courteous companions" -> "Courteous"; "Jude, 14,15"; comma after "as she thought";
  missing open/close quotes on Christiana's speech para "The thoughts ... that land."; "I am sure," ;
  "within herself, If".
- II s1: "stand; For" -> "for"; "Christiana, had I" -> "Had". II s2: "doing, But" -> "; but"; "said, stand back" -> "Stand"; "pilgrim’s life." -> "?"; "God made it a true saying upon me, and grant" -> "make" (sense, parallel to grant); "he, said" -> "he said"; "neat and find" -> "neat and fine".

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

5. Author's Way verse lines short by a word in CCEL (no Part II witness in repo; from
   memory of the 1684 text): l.82 "Are nothing else but groundless fears" (1684: "but ground for
   groundless fears"); l.111 "Things of greater bulk" ("Things of a greater bulk"); l.131 "love him at
   first" ("at the first"). Recommend restoring.
6. "wholsome" (Author's Way) vs "wholesome" elsewhere.

## Next step

Continue Part II at part-2/stage-03.typ through stage-08 (whole files; helpers in scratchpad pp/: rep.py FILE PAIRS, prog.py NOTE --done --next --msg, w.py). Part I + front matter synced/checked OK; Part II stage fixes not yet synced: run ./fgb sync pilgrim and ./fgb check pilgrim after next batches. Then global to-do, build, PDF checks, report.
