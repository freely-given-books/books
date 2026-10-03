# Gouge vol. 4 review: progress (branch gouge-review-vol-4)

## Done
- Tools: sweep.py --early (vol-4: 324 hits, mostly period words; "too too" is period),
  refs.py --quotes (1 vol-4 "missing": Philem. v. 2 = verse 2, false positive).
  Own unknown-word list (scratchpad bin/unknown.py) for spellings the machine missed.
- Read for sense: ALL files 01-10 + errata (no edits applied yet at this checkpoint).
- Helpers in scratchpad/bin: o.py CH REGEX (current vs printed), case.py, page.py N (TCP page text).

## Fix list (to apply)
- 01: left->lest; "Servants fear of their masters.." (dropped Greek -> double stop, also 16. 7.., Obseru.].);
  austerit je->austerity; he aven->heaven; receineth->receiveth; "their sure"->suit;
  "( #emph[obey)]"->"(#emph[obey)]"; "IN this verse"->In; "TO the duties"->To; "Marvell not"->marvel not;
  "ôye"->"ô ye"; "God. men must"->Men; u/v misses aduiseth, swerueth, deserueth, adioyneth, inioyneth.
- 02: seruans->servants; ingenerall->in general; "§. 3 "->"§. 3."; Object.] masters->Masters; Answ.] rule->Rule;
  politipue->politic; of fending->offending; 24. 9..; jealously->jealousy; footnote "1\. King."->"1 King.";
  epigraph "servants be obedient"->Servants; inioyneth.
- 03: "One simus"->Onesimus; stray "c" in footnote "c John 4. 53."; "if whey"->when; Tit. 2. 9..; yron?(spelling list)
- 04: footnote "11."->"II."; left->lest; show-of->show of; "2\. King"->"2 King."; be are rule->bear rule;
  1 Tim 6. 20..; sences and gats->fences and gates; see on fire->set on fire; Tit. 2. 10..; Acts 5. 2..;
  strise->strife; Psal]->Psal.]; tht->that; manners.] children->Children; Indas->Judas; Deserueth.
- 05: befor->be for; wch->which; Levire->Levite; Isa. 24 2.->24. 2.; "power Because"->because; family)->family).;
  1 Cor 8. 6..; Ephef.->Ephes.; Lordye->Lord ye; Gen] 39->Gen.]; undesiled->undefiled.
- 06: Philem. vers]->vers.]; 3. 4.. / 5. 14..; relin quishing; aufterity->austerity; childings->chidings;
  Treat. 7. §. 38->38.; obserueth.
- 07: grienous->grievous; Coloss. 4. 1..; margin note run into text in §16 ("amend it, The direction ... Read it. Then blows ... stoutness. Must") -> make footnote, "then blows", "stoutness must"; Jnstit.->Instit.? (Latin, leave).
- 08: Luk. 12. 42..; "4 By"->"4. By"; reapebenefit; Sam]->Sam.]; See. §.->See §.; in humane->inhumane; fouth->fourth; principal-reason.
- 09: Jess->Jesse (machine error!); insect->infect; "themselves, Justice"->". Justice"; "are For"->"are. For";
  Answ.] servants->Servants; conscienc->conscience; "#strong[Object.]" own paragraph x2 -> merge like elsewhere.
- 10: note->Note; "heaven i, higher"->is; "the masters of servants"? (check orig).

## Questions (draft, V4-n)
- point of justice -> injustice (ch3 §11): ERRATUM p.606 l.9 says "Point of injustice" -> apply?
- "the phrase with the Apostle useth" (ch7 §17) -> which?
- foking -> soaking? (ch9 §36)
- TCP false section "=== §. 4. Some of the reasons..." (ch6, Treat. 8 §4): a sentence turned into a heading; structural fix needed.
- ch8 §25 paragraph "The Hebrew word is oft used for scarlet..." is a margin note set as body text -> footnote?
- ch1 §126 verse 7 epigraph set as plain paragraph, unlike verses 5,6,8,9 (TCP <p>).
- Epigraphs ch2 §1 and ch10 §46: inner #emph inside italic block -> renders roman? check PDF.
- Book-wide: Leu.->Lev., Iam.->Jam. citation abbreviations not modernized.
- Old spellings missed by the machine (list with counts) -> modernize?
- Latin misprints (impiun, seruorun, seruabaxtur, Conslit, di'igat, sea quo. libet, fine causa, revs, Deil.) left as printed per README.
- Errata: check each of 8 against the text (p215 dissolution, 218 Have no direct, ibid marg viro, 268 fifth com., 297 fifth reason, 412 And also, 606 injustice, 629 Of one equal).

## Next step
Check errata pages (page.py), then apply fix list per file, sync/check, commit per file.
