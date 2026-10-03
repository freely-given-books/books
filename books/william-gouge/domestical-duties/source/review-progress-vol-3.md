# Gouge vol. 3 review: progress (branch gouge-review-vol-3)

Helper: scratchpad `o.py NN pat...` greps the printed layer (orig extraction in
scratchpad/orig; machine-only in scratchpad/auto; regenerate with tei_extract.py
if the scratchpad is gone).

## Tools
- sweep.py --early: 533 vol-3 hits; apostrophe hits are italic names + 's (book
  style, kept); the rarer "words" hits were used as a suspect list (all checked
  as files are read).
- refs.py --quotes: 2 missing in vol-3 (02 Num. 30. 17; 06 Psal. 1. 12) -> questions.
- slips.py: no modern witness for Gouge.

## Files
- 01 done, fixed
- 02 done, fixed
- 03 done, fixed
- 04 done, fixed
- 05 done, fixed
- 06 read to line 319 (of ~450); its fixes NOT yet applied (list below)
- 07-10 not yet read

## Fix kinds so far (for the report)
- misprints (print or TCP): siliall->filial, fullenness->sullenness, cavear->caveat,
  revererend->reverend, continuali->continual, fathfull->faithful, beggd->begged,
  "children are must bound"->most, "was to careful"->so, Godhath->God hath,
  "therefore at parents"->that, "thy another"->mother, acomely->a comely,
  "and impious conceit"->an, biosterous->boisterous, "In in different"->indifferent,
  "out to ascend"->but, "in his kind"->this, poverry, farrc->far,
  "his showeth"->This, seareheth, requirety, revetence, "to then children"->their,
  "God ever lieth"->liveth (05 §64, print has lieth; sense), "Moses bear"->bare.
- capitals lost by the machine: epigraph "Children obey"/"Honour" (01, 03 §35 also
  IN ALL THINGS), "Object./Answ. children|servants" (02 x4, 05), "OF their", Subjection (05).
- references: Job 29 "Vers. 25"->21 (01 §4, quote is 29:21); "Luk. 2. 5 1."; "½ Kin."->1 Kin.;
  missing/doubled stops (19 4, 12 17, Tit 1. 6.., Eph. 6. 1.., Heb. 12. 9.., 1 Tim. 5. 4.. x2,
  Gen 27, Iam 1, Col. 3. 20), "3. 4, 6,", "Gen. 34, 3", "Ruth 1, 16", "1. Tim."->1 Tim.
- margin notes: numbers without stop ("2 Necessity", "3 By", "4 By", "2 In sincerity", "4 With");
  05 §53 margin notes 3/4 (Rudely/Grudgingly) swapped back to match the text; stray "\*"
  print reference marks removed (03 §31, 04 §48); "See. §. 6."; "-against"; "§" restored in "[. 37.]".
- Latin (TCP/print slips): siliorum->filiorum, mirati sant->sunt, vx eres->vxores,
  Di est->Digest., quast->quaest., "Parent is imprecation"->Parentis imprecatione (machine had
  modernized Latin), patren eger->patrem egere, parentus fata propera uerit->parentis fata
  properauerit, vicinun->vicinum, praestitiss->praestitisse, subiect siue->subiectisque (Aen. 11.185).
- spelling the machine missed: deserueth, conueniency x3, conueigh, heighnous, nurtered, erronious,
  Hereticke, tenn x2, townes, idolls, busibodies, Wastfully, deerely, paine x3, lyeth x4, leaud,
  overweining conceipt, conceipt, fearefulness x2, swagerers, Isaakes->Isaacs, uncleaness, dispise,
  disdainefully/scornefully, releeving, shuteth, poorely, adiudgeth, cryeth, carkase, imbalmed,
  funeralls, coverousness, neast, meated->meted, greene, linage, stile->style, Stubborness,
  Unsetledly, backt, marieth, steed->stead x3, dissention, brooke x2, cosen, refractary,
  alleageance, ex emption, after wards, straitned, for borne->forborne.
- names to KJV form: Absoloms->Absaloms x2, Stevens->Stephens, Jehosaphat->Jehoshaphat, Phineas->Phinehas.
- layout: 03 §36 and 05 §62 Quest./Answ. set like the rest (split "Quest." paragraph joined).

## Needs your decision (draft)
- V3-1 01 §6 "when children pout, lour, swell, and give to answer at all" (print same): a word
  lost; recommend "give no answer at all".
- V3-2 01 §5 "making known to them me needful matter" (print "me"): recommend "some".
- V3-3 02 §14 the one illegible word ("4. For the loving of father and mother more then Christ, ….
  It doth not"): the answer goes on "2. If they be forsaken", so the lost word is almost certainly
  the number "1."; recommend "1.".
- V3-4 references that do not exist: 02 §12 Num. 30. 17 (KJV 30:16 is the verse meant);
  06 Psal. 1. 12 (check when read).
- V3-5 "Levies speech" (02 §14 x2) = Levi's; book style without apostrophe -> "Levis"? recommend "Levi's"? (decide with book's possessive style)
- V3-6 04 §45 "It is the duty of children to bring the bodies of their parents deceased, with such
  decency" (print "bring"): recommend "bury"? or keep (bring = carry to the grave).

## For the coordinator (cross-volume)
- machine lowercases a common noun after an italic "Object."/"Answ." (Children, Servants):
  7 more in vols 1, 2, 4 (grep "#emph\[(Object|Answ|Quest)\.\]( \d\.)? [a-z]").
- "Iam." (James) not modernized to "Jam." though Ioh->Joh, Iob->Job were.
- variant spellings: collect at the end.

## 06 fixes identified, not yet applied (lines 1-319)
enioyneth->enjoineth; item "3. To instruct" (l.37) into the "- 1\. / - 2\." list as "- 3\.";
Isaacks->Isaacs; paine->pain (l.86 x2, l.94, l.314-318 x3); Savadges in Virginea->Savages in Virginia;
"1 Thes 5. 17.."->"1 Thes. 5. 17."; "Treat 5."->"Treat. 5."; "Hier. ad] 1 #emph[aet.]]"->"Hier. ad Laet.]]";
"Psal. 1. 12. 2."->"Psal. 112. 2." (settles V3-4 second half); degenerat->degenerate;
join "#strong[3. #emph[Object.]]" with the next paragraph (as 03 §36); Ammon->Amnon (2 Sam 13);
toile->toil; saulation->salvation; "Tro. 10. 22."->"Pro."; nutriend->nutriendi; coveteous; affoorded;
Philosophen->Philosophers; Angell->Angel x3; miscariage->miscarriage x3;
"vindie abitur si iniusle"->"vindicabitur si iniuste" (accented e); hardned->hardened x2;
"Iniquiffima ... quiae"->"Iniquissima ... quia"; "Digest. l, 25." (comma inside the emph) -> "l.";
"a kind of further."->"murder." (print "further"; the Latin beside it: necare videtur); bestfood->best food;
add "(" before "As new-borne babes desire" (closing ")" is there); brest-milk; "ablactaueris cam"->eam;
"1. The consequences" -> "I." (II., III. follow); "1\. #emph[Tim.] 5. 10."->"1 #emph[Tim.]"; "As his is"->this;
"virgin #emph[man]"->Mary (print "Man"); diddest->didst; "taketh if also"->it; "womb bear him"->bare;
Idoirco->Idcirco, "praebuit" + odd mark -> "praebuit."; "Plut. de Justit."->Instit.; seamonsters->sea-monsters;
Cucco->Cuckoo x2; dugges->dugs; "up. And stilling them;"->"up, and stilling them:" (print "vp. and");
"Or when ... he had one"->she; Pharohs->Pharaohs; "Reu.] 15. 16."->"16. 15." (Rev 16:15, thief).
Coordinator note: "Reu." (Revelation) is not modernized to "Rev." anywhere in the book.

## Next step
Apply the 06 list above (python exact replacements, assert each count), then read 06 from line 319
to the end, then 07-10; then variants table, sync/check/pdf, report proofread-report-vol-3.md.
