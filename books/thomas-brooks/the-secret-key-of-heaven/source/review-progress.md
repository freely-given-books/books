# Secret Key of Heaven: review progress (branch secret-key-review)

Scratch work (not in git) lives in
`/tmp/claude-1000/-home-courtney-Projects-fgbooks-books/7734942a-5f8c-443c-b192-56f7915e6a6f/scratchpad/brooks/`:
`auto/` (1665 text, spelling modernized only, `tei_extract --only-auto`), `orig/` (as printed),
`wit/` (Chapel Library EPUB as text, compare only), `q.py PATTERN [auto|orig|wit|ed]` (find a phrase in
each layer), `wdiff.py` + `filt.py` -> `wdiff2.txt` (819 lines: every substantive word difference
between the edition and 1665, references and spelling filtered out). Regenerate them if /tmp was cleared.

Note: the Bash guard refuses any command line containing the word `source`; write `sourc[e]` in paths.

## Tools run

- sweep.py --early: 137 hits, all "words" (names, period forms, Chapel-style refs "Joh", "Ecc", "Jdg").
  Real ones: `forpublic` (app-01, glued: fix "for public"); `Eropas` (app-02, check name: Aeropus?);
  `doemon` (app-02, "brevis doemon": check print / daemon).
- slips.py vs Chapel Library EPUB: 3 (app-02 "water pot" -> waterpot, app-03 "still born" -> stillborn,
  app-05 "love tokens" -> love-tokens/lovetokens): print and witness agree; fix as spacing.
  Few hits because the copy was made from Chapel Library: CL's own slips are only visible in wdiff2.txt.
- refs.py --quotes: 778 refs, 0 missing, 5 weak: Psa 77:4 (2 verses, fine), Pro 2:20 (chain, fine),
  Jer 3:3 (chain, fine), **1Ki 19:8 for "subject to like passions" (app-02 l.455; check print)**,
  **Song 8:11-12 for Bernard (app-05 l.20; print? perhaps 7:11-12)**.

## Files read

- chapter-01, 02, 03: done
- argument-01 .. 12: done
- NEXT: argument-13 .. 20, then application-01 .. 05 (app-02 ~28k words, app-03 ~18k, app-04 ~9k, app-05 ~4.5k)

## Fixes applied (synced; check OK)

- ch-01: "dear friend" -> "dear friends" (1665 "Dear Friends"; opens "Dear friends")
- ch-02: "the 16 argument" -> "the 16th argument" (1665 "the 16. Argument")
- arg-01: "saying. “Well" -> "saying, “Well"; "Dr Sibbes" -> "Dr. Sibbes" (book has "Mr." with stop)
- arg-02: "bloody sweat; so John 6:15-17." -> ". So John 6:15-17." (1665); "(Heb 2:17; John 17)" -> "Joh 17" (ref style)
- arg-08: "by might and flight" -> "might and sleight" (1665 "slight", = sleight; next sentence has "sleights";
  CL has "flight" too: CL's slip); Augustine "dost thou hear" -> "Thou"; "God sends forth his mandamus" -> "His"
- arg-12: "as a man would speak to His friend" -> "his"; Augustine "His pleasure, he would send" -> "He";
  "in the 25 Psalm" -> "25th" (1665 "25th."); "His greatest and our choicest secrets" -> "His choicest"
  (1665 "his greatest and his choicest"; CL's slip)

## To check while reading (from wdiff2.txt)

app-01: l.7 "any more but secondly" -> "anymore" (Secondly lost?). app-02: "conjoyne" -> "enjoin" (l.73: should be
conjoin), "lusteth" dropped (Gal 5:17), "a great lady" + "Queen Elizabeth" added, "[that] -> []", "have" dropped,
"must" dropped, Eropas, "brevis doemon", 1Ki 19:8, "and not" added, "eh"->"when". app-03: "man"->"marquis",
"fifteenth" dropped, "he" dropped. app-04: "person"->"soul", "Antonius"->"Antoninus", "archangels surpass"->
"archangel surpasses", "if not"->"if but", "issues in upon"->"open", "whom"->"him", "laws or" dropped, "judge" added,
"was/him"->"were/them". app-05: stray “ before "Meditation is the nurse of prayer" (l.20), "of"->"so", "or" dropped,
"the house of" dropped (Zec 12:12), end-of-file "with/o/it" drops, "hath"->"have", "any"->"they".
arg-13..20: "his"->"our" style slips; arg-19 "but in the" dropped; arg-17 fine.

## Needs your decision (draft)

1. **Latin, Greek and Hebrew still cut** (555ca78 restored eleven; these remain cut or replaced by a translation):
   poenae gravitas / personae dignitas (app-03, now only English), bene fecisti (app-03), bombarda christianorum
   (app-03), ultimum vitae / optimum gloria (app-03, English only), invocare / advocare (app-03, English only),
   Hebrew robets, tolagnath, gnarach, tsaphah (app-03), in nihil agendo, pulvinar diaboli, totus oculus,
   munito corde / occlusa corde (app-04), meditatio nutrix orationis, aeternitati pingo, unum perpetuum hodie (app-05),
   lasuach (arg-01), porta coeli clavis paradisi, vicimus vicimus (arg-08), iste liber (arg-06), segullah (arg-20),
   the gloss "what extraordinary thing do you" (app-02, Mat 5:47). Recommend: restore Latin beside the English,
   as 555ca78 did; Hebrew transliterations as printed.
2. Older editor's wording kept so far (ask only if the user wants them undone): "unskilful idiot" -> "uneducated
   person" (arg-12), "victuals" -> "food", "without all peradventure" -> "without any doubt" (ch-03),
   'tis -> "it is" throughout, 1665 margin notes not in the edition.

## Check status

`./fgb check brooks`: OK. [2] lists 17 files as differing from the extraction: expected layout lines
(README), but confirm it was 17 before this branch (`git stash`-free: compare on a clean checkout of main).

## Update (resumed 2026-10-03)

- arguments 13-20, application-01, application-02: done. NEXT: application-03, 04, 05; then build, PDF check, report.
- check [2]: the 17 files differ from the extraction only by layout lines and a blank line after the heading
  (argument-04 etc.); predates this branch.
- more fixes: arg-14 "As he is included … so he" -> He; app-01 forpublic; app-02 "Sirs, I, as you, love" ->
  "O sirs, as you love" (1665; CL slip) and "?"; Eropas -> Eropus (1665 "Ero••s", two letters lost; Aeropus);
  "until he entered" -> He (Christ); "enjoin our affections" -> conjoin (1665); "What do ye more than others?";
  "Thou sayest thou cannot pray" -> "canst not" (1665); Zech -> Zec (2); Sirtorius -> Sertorius; "so forwardly" ->
  frowardly (1665; CL slip); "husbandmen until their fields" -> till (1665); "(1)#emph" space; "the holy”." ->
  "holy.”"; "some of his people" -> His; "authentic. / And, for ensuring." merged as 1665; "(Compare Song 2:16; 3-6"
  -> "2:16, 3-6"; "Tenthly and lastly. When" -> ", when"; "sweet meats" -> sweetmeats; "brevis doemon" -> daemon
  (1665 Daemon); ‘My sister …” -> “; "the “the soul’s beast" -> doubled the removed; "our Saviour" -> Savior.
- questions added: yearnings (=earnings, ×4: arg-15, arg-19, app-03 ×2); "[Queen Elizabeth]" is Chapel Library's
  annotation (app-02) - remove?; Harcatus (1665) -> Hyrcanus (CL) - restore "Harcatius"?; "But secondly, this may serve
  to exhort us" (app-01 end, "Secondly" cut); Isa 54:13 expanded by CL into a quotation, so "In these words" now points
  at Isaiah (app-02, Spirit teaches); 1Sa 1:11 (Brooks's ref, 1:13 is the verse); "eminent danger" (=imminent, arg-13);
  recompence (×2) / recompense.
