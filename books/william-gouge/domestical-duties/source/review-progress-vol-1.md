# Gouge vol. 1 review: progress (branch gouge-review-vol-1)

Brief: scratchpad brief.md, with the vol-1 changes (edit only chapters/typ/vol-1;
commit only those files + this file + source/proofread-report-vol-1.md; restore
the TEI / review-report.md / volume files / covers before committing).

## Tools run

- sweep.py --early: 506 vol-1 hits (491 "words", mostly -eth/etc./Latin). Useful
  hits: machine spelling misses (begineth, kniteth, submiteth, stireth, refereth,
  prefereth, infereth, acquiteth, tyrany, therto, suerty, unfainedly, unbeleefe,
  sowreness, raigneth, neerness, mispent, hainousness, enlightned, darkned,
  wordlings?, Welbeloved, genetive, beinto, Godman, couragement, backparts);
  doubled "Tit. 3 3", "Psal. 37 37"; Latin "Pascit a & Pentecosle" (ch05).
- refs.py --quotes: vol-1 missing refs: 03 Psal. 116. 136 (FIXED -> 119. 136);
  04 Mat. 16. 32, 23 (FIXED -> 16. 22, 23); 07 "eccl. l. 1" (Latin, ignore);
  07 "I John 4. 34" (probably John 4. 34 - check); 08 "EPHES. 6. 29" (epigraph
  heading? check); 11 "Job. 7. 30" (check).
- Helpers in scratchpad (not committed): og.py NN 'pattern' searches the
  as-printed text (orig layer extraction in scratchpad/orig, regenerate with
  tei_extract.py --layer orig --expand if missing); apply.py EDITS.tsv applies
  exact replacements (FILEPREFIX<TAB>OLD<TAB>NEW). `./fgb find gouge WORD`
  shows printed / machine readings.

## Files read and fixed

- dedication: DONE
- 01: DONE
- 02: DONE
- 03: DONE (user had reviewed only its lists/layout)
- 04: DONE
- word map (vol-2's 72 entries + mine, helper v1/wmap-applied.txt in scratchpad/v1) applied to all vol-1 files
- 05: DONE (Pascha & Pentecoste, still-born, 1 Joh. 1. 8, ad elementum, Object. merged)
- 06: DONE (Reu. -> Rev. and Iam. -> Jam. done volume-wide)
- 07: DONE
- 08-12: NOT YET READ
- Round-trip check: extract reg from worktree TEI to scratchpad/v1/rt and diff with chapters/typ/vol-1 (only the 2 pre-existing layout lines in 03 differ). A run-in '#strong[Object.]' head cannot be merged into its paragraph (reverted in 05); nested '+' sub-items do not round-trip (reverted in 07).
- NOTE: scratchpad is shared with other agents; my helpers now live in scratchpad/v1/ (og.py, apply.py, orig/)

## Fixes so far (for the report)

- Print misprints: "which be giveth" -> he (ded.); "seruiee" -> service; "Euscb."
  -> Euseb.; "nothing a consequence" -> noting (04); "instification" ->
  justification (04); §31 heading "value of the prince of our redemption" ->
  price (04, a misprint in Gouge's own head; report it prominently).
- Machine spelling misses: Midsommer, wier, praieth, waightier, inioyneth,
  Angell, alleaging, hearkned, swel, accurat, Be-hive -> Bee-hive (bee->be
  rule), Wherupon, Privat, likwise, mistris, mispend, goshipping, Jaacobs ->
  Jacobs, borne -> born (birth; x6), horne -> horn x2, begineth x2, obserueth,
  vertuously, preserueth, infereth, First-borne, allegeance, Soveraignes,
  pole/peele -> poll/peel, emphaticall, seazed, woful x2, tyrany, rendreth,
  stireth x2, climing, attonement, purchaesing, suerty, deserueth, paralleld,
  therto, Nazaret -> Nazareth, Uers. -> Vers., Exhòrtation, back ward, ô -> O.
- Citations: Iam. -> Jam. x2, Reu. -> Rev., "2. Sam."/"1. Tim."/"1. Cor." ->
  "2 Sam." etc., "Gen. 3 10" / "2 Chro. 19 9" / "Tit. 3 3" dots, "2 Chro. 24 7"
  -> 24. 17 (Joash and the princes, KJV), Psal. 116. 136 -> 119. 136, Mat. 16.
  32, 23 -> 22, 23, doubled full stops (Heb. 7. 25.., Acts 3. 15.., 1 Cor. 7.
  2.., Phil. 2. 9.., etc..).
- Spacing / glued: "( #emph[own)]" etc. -> "(#emph[own)]"; samething,
  somethings, therebe, Churchwith, whethe -> whether, Godman -> God-man,
  Methodusintelligentiae.
- Latin: TCP line-end splits joined (faci enda, praete rire, cast us, Ec l.,
  instrip tum -> inscriptum); misprints secit -> fecit, blaspliemies (Eng.);
  machine modernized Latin "vocatione" -> "vocation" (restored); macron
  expansions tuun -> tuum, Nazarenun -> Nazarenum, expani -> expavi, lesum ->
  Iesum, "nullase necessita e" -> "nulla se necessitate".
- Epigraphs: inner #emph inside the italic epigraph block made the verse print
  upright (Typst emph toggles); removed in 02 §7, 03 §17, 04 §26 ("husbands" ->
  "Husbands" there too). CHECK this rendering in the PDF and look for the same
  in 05-12 and other volumes (tell coordinator: likely book-wide).
- 01 footnote "submitting., submit." -> "submitting. submit." (Greek dropped).

## Draft "Needs your decision"

- V1-1: 02 §13 "Thus the Apostle himself expoundeth this phrase, chap. 5. Vers.
  5, 6." (1622 the same). Eph. 5:5-6 does not expound "as unto the Lord"; Eph.
  6:5-6 ("as unto Christ ... as the servants of Christ") does. Recommend chap. 6.
- V1-2: 03 §16 heading "Of the resemblance betwixt The Church to Christ. A wife
  to her husband." (a brace in the print). Recommend "Of the resemblance betwixt
  the Church to Christ, and a wife to her husband."
- V1-3: "humane" for "human" (humane nature, humane laws, humane traditions) vs
  "human nature" once in 04: modernize to "human"? (count across vol.)
- V1-4: "in deed" (3 in 03 = indeed; 04 "in deed and truth" is right) vs
  "indeed" 10: normalize the three in 03?
- Possessives: SPELLING table gives "Adam's", "David's", "Abraham's",
  "Solomon's" while the book writes "Aarons, Sauls, Josephs, Jacobs": "The issue
  of Adam's, Aarons, Sauls" (01). Ask: drop the apostrophes from the table
  names, or leave.
- V1-5: 06 heading "§. 44. Of the fruition of Christs presence in heaven" sits between §48 and §50 (1622 prints 44). Recommend §. 49.
- V1-6: 07 §56 brace list '1. Negatively 2. Affirmatively, and that in two branches 3. Nourisheth 4. Cherisheth it.' prints as one 4-item list; Nourisheth/Cherisheth are branches of item 2. Nested items do not survive sync (pipeline). Recommend: '+ Affirmatively, and that in two branches, #emph[Nourisheth] and #emph[Cherisheth] it.' or a pipeline fix.
- Kept: "It is then unlawful to fear any but God?" (01, as printed).

## Variants to count at the end (vol-1)

in deed/indeed, humane/human, Black-friers/Black-Fryers, Isay/Isaiah,
dependance, every thing, your selves / it self, -eth doubled consonants.

## Next step

Read 08 from the top, then 09-12; after each file: apply edits, ./fgb sync gouge, restore regenerated
files, commit WIP. Then sweep re-run, refs, ./fgb check, ./fgb pdf (check
epigraph italics), pdftotext checks, write source/proofread-report-vol-1.md,
final commit.
