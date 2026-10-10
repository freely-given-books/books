# Proofread report

The machine pass of the 1653 text (TCP A77614), read in full against the
1653 printing and Grosart's edition (Monergism), in four parts. Fixes were
applied to `chapters/typ` and folded into the TEI as `#editor` decisions.

## Fixed

| kind | count |
| --- | --- |
| modernize | 332 |
| possessive | 227 |
| then-than | 220 |
| misprint | 192 |
| other | 107 |
| punctuation | 76 |
| reference | 49 |
| latin | 45 |
| spacing | 40 |
| words | 18 |
| greek | 13 |
| hebrew | 3 |

Also by machine rule (colophon): sentence-initial ’Tis/’Twas, lowercase
ver./v./chap. after a verse number, and lowercase after an interjection's
"!" as printed (153).

The stray "v." in the note "Prov. 13. 20. v." (sin-12) is removed: colophon
now records deleting it (it took "v." for a roman list label).

## Open questions

Not applied. Each with the proposed reading and why; the editor decides.

- **dedication.typ**: `Matth. 16. ver. 22. 26. ch. 69. ult.` → `Matth. 16. ver. 22. ch. 26. 69. ult.`. 1653 as printed is garbled; the denial is Matt. 26:69 to the end; Grosart 'Mat. 16:22, chap. 26:69-75'
- **to-the-reader.typ**: `not #emph[quaristas,]` → `not #emph[quaeristas,]`. Luther's play 'curristas, non quaeristas' (runners, not askers, from quaerere); 1653 'quariſtas' may be a misprint
- **to-the-reader.typ**: `the runner not the questioner #emph[Pacunius] hath` → `the runner not the questioner. #emph[Pacuvius] hath`. a sentence ends with no stop (1653 the same); the saying 'Odi homines ignava opera, philosopha sententia' is Pacuvius (Gellius 13.8), 1653 'Pacunius' u/n; Grosart drops the note
- **introduction.typ**: `old subtile serpent` → `old subtle serpent`. 'subtile' is an old spelling of subtle; Grosart 'subtle'; a book-wide choice (see note)
- **sin-01.typ**: `#emph[Heliogobalus]` → `#emph[Heliogabalus]`. name form; the emperor is Heliogabalus (Elagabalus)
- **sin-01.typ**: `at the loss of #emph[Callice,] when a proud French-man scornfully demanded, when will you fetch #emph[Callice] again?` → `at the loss of #emph[Calais,] when a proud French-man scornfully demanded, when will you fetch #emph[Calais] again?`. name form: 'Callice' is the old English spelling of Calais; Grosart 'Calais'
- **sin-01.typ**: `#emph[Appium Sardis]` → `#emph[Apium Sardoum]`. the herb of 'sardonic' laughter is apium Sardoum (Sardinian), not Sardis; 1653 'Appium Sardis' may be Brooks's own
- **sin-01.typ**: `it will with #emph[Dalilah] smile` → `it will with #emph[Delilah] smile`. name form: KJV and Grosart 'Delilah'
- **sin-01.typ**: `#emph[Philistimes;]` → `#emph[Philistines;]`. name form: Grosart 'Philistines'
- **sin-02.typ**: `a pestilent Sect in #emph[Arragon,]` → `a pestilent Sect in #emph[Aragon,]`. name form: Aragon (the Spanish alumbrados)
- **sin-02.typ**: `ready with #emph[Achitophel,] and` → `ready with #emph[Ahithophel,] and`. name form: KJV and Grosart 'Ahithophel'
- **sin-03.typ**: `who let all the vials of his fiercest wrath upon him` → `who let out all the vials of his fiercest wrath upon him`. 'let all the vials ... upon him' seems to lack a verb particle (let out/let fall); 1653 and Grosart both 'let all'
- **sin-04.typ**: `#footnote[Theodorit. hist. l. 4. c. 17.]` → `#footnote[Theodorit. hist. l. 5. c. 17.]`. Ambrose and Theodosius is Theodoret, Eccl. Hist. book 5, ch. 17 (18 in some editions); 1653 'l. 4.'
- **sin-04.typ**: `Pro. 3. 12, 13. ch. 6. 23. 26. Isaiah 9.` → `Pro. 3. 12, 13. ch. 6. 23. Isaiah 26. 9.`. 'Isaiah 9.' after a stray '26.' reads as Isa. 26:9 ('the inhabitants of the world will learn righteousness'), which fits chastening as teaching; 1653 the same
- **sin-04.typ**: `#emph[Job (Chap. 33. 16. 19)` → `#emph[Job (Chap. 33. 14-18)`. the quotation runs from Job 33:14 ('God speaketh once, yea twice') to 33:18; Grosart 'chap. 33:14-18'; 1653 '16. 19'
- **sin-05.typ**: `for 30 pence 8. #emph[Andr. cat.]` → `for 30 pence. #emph[Andr. cat.]`. a stray '8.' after '30 pence' (perhaps a page or chapter of the source); 1653 the same
- **sin-06.typ**: `thou art as well melt adamant` → `thou art as well able to melt adamant`. 1653 'thou art as well melt Adamant' has lost words; Grosart 'Thou art as well able to melt adamant'
- **sin-07.typ**: `play and toy with #emph[Daliloh,]` → `play and toy with #emph[Delilah,]`. 1653 'Daliloh' is a misprint at least (sin-01 has 'Dalilah'); KJV and Grosart 'Delilah'
- **sin-07.typ**: `God will not remove the tentation` → `God will not remove the temptation`. 'tentation' is an old word for temptation; the parallel sentence below has 'God will not remove the temptation'
- **sin-08.typ**: `to render good for good, is humane` → `to render good for good, is human`. 'humane' was the period spelling of human; the series divine / human / brutish / devilish wants 'human'
- **sin-08.typ**: `for all the sins they have committed, would make their hearts` → `for all the sins they have committed, it would make their hearts`. the main clause lacks its subject (1653 the same); Grosart 'it would make their hearts'
- **sin-09.typ**: `#emph[Benedicta Medicamentum,]` → `#emph[Benedicta Medicamenta,]`. 1653 'Benedicta Medicamentum' does not agree (neuter plural adjective with singular noun); 'medicamenta' fits 'call them'; not in Grosart
- **sin-09.typ**: `Vedib bartignal-libbab.` → `Vedibbartignal-libbah.`. transliteration of ודברתי על־לבה: 1653 'Vedib bartignal-libbab' splits the word and ends in b for h (the TCP note in gap_fixes reads 'Vedibbartignal libbah'); transliterations otherwise stay as printed
- **sin-11.typ**: `#emph[Judge] 8. 13. one turn` → `#emph[Judg.] 8. 30, 31. & 9. 5. One turn`. Gideon's seventy sons and the bastard Abimelech are Judg. 8:30-31, the slaughter 9:5; 8:13 does not fit (1653 'Judge 8. 13.'); 'one turn' opens a new sentence
- **sin-11.typ**: `saith #emph[Melancton,]` → `saith #emph[Melanchthon,]`. name form: 1653 'Melancton', Grosart 'Melancthon'; standard 'Melanchthon'
- **duties-01.typ**: `#emph[Gilimex] King of #emph[Vandalls,] led in triumph, by #emph[Bellisarius,]` → `#emph[Gelimer] King of #emph[Vandals,] led in triumph, by #emph[Belisarius,]`. name forms: 1653 'Gilimex', 'Vandalls', 'Bellisarius'; Gelimer, the Vandal king led in Belisarius' triumph ('Vandals' at least is a plain modernization)
- **duties-01.typ**: `#emph[when Jesurum waxed fat,` → `#emph[when Jeshurun waxed fat,`. name form: 1653 'Jeſurum'; KJV Deut. 32:15 and Grosart 'Jeshurun'
- **duties-02.typ**: `So #emph[Santus] being under` → `So #emph[Sanctus] being under`. name form: 1653 'Santus'; Sanctus of Vienne, the martyr of Lyons who answered every question 'Christianus sum' (Eusebius 5.1)
- **duties-02.typ**: `for momentany afflictions` → `for momentary afflictions`. 'momentany' is an obsolete form of momentary (the book has 'momentary' in sin-09)
- **duties-03.typ**: `and the keeping under of weak graces` → `and the strengthening of weak graces`. 1653 repeats 'keeping under' from 'keeping under of sin', which inverts the sense; Grosart 'the strengthening of weak graces'
- **duties-04.typ**: `#footnote[Gal. 6. 9. 2.]` → `#footnote[Gal. 6. 9. 1 Thess. 5. 16, 17.]`. 1653 'Gal. 6. 9. 2.': the stray '2.' looks like the start of a lost reference; the next quotation 'rejoice always, and pray without ceasing' (no note of its own) is 1 Thess. 5:16-17
- **duties-05.typ**: `and who have counted their lives dear unto them` → `and who have not counted their lives dear unto them`. 1653 lacks 'not', which the sense needs (Acts 20:24 'neither count I my life dear unto myself'); Grosart 'who have not counted their lives dear unto them'
- **duties-06.typ**: `with chains of adamant of sin; we may say as #emph[Isidor] doth` → `with chains of adamant; of sin we may say as #emph[Isidore] doth`. 1653 'chains of adamant of ſinn; we may say': the semicolon reads better before 'of sin' (Isidore's saying is about sin); 1653 prints 'Iſidore', the edition's 'Isidor' is a machine-pass slip (fix that part regardless)
- **duties-07.typ**: `saith #emph[Augustin.]]` → `saith #emph[Augustine.]]`. name form: 1653 'Auguſtin'; the book writes 'Augustine' elsewhere (sin-09, duties-01)
- **duties-07.typ**: `and his#footnote[Simile.] law;` → `and his law;`. margin keyword 'Simile.' (marking the comparison that follows), like the 'Remedy' labels
- **duties-08.typ**: `Mat 6. 2. Rom. 17.]` → `Mat. 6. 2. Rom. 2. 17.]`. Romans has 16 chapters; 1653 'Rom. 17.' probably lost the chapter: Rom. 2:17 'thou ... restest in the law' fits 'rest in their performances'; stop missing after 'Mat'
- **doubting-02.typ**: `Heb. 7. 25. 26. Isa. 3. 4, etc.]` → `Heb. 7. 25, 26. Isa. 26. 3, 4, etc.]`. 1653 'Heb. 7. 25. 26. Isa. 3. 4'; Isa. 3. 4 ('I will give children to be their princes') does not fit; Isa. 26. 3, 4 ('whose mind is stayed on thee ... trust ye in the Lord') fits 'resting, and staying'. Grosart drops the refs
- **doubting-02.typ**: `#footnote[Gal. 4 6.]` → `#footnote[Gal. 3. 26.]`. 1653 'Gal. 4 6.' (Grosart copies 'Gal. 4:6'); the words quoted, 'sons by faith in Christ Jesus', are Gal. 3. 26; Gal. 4. 6 (the Spirit in sons) fits the sentence before. At least 'Gal. 4. 6.'
- **doubting-03.typ**: `all the rugged promises that #emph[Daniel,]` → `all the rugged providences that #emph[Daniel,]`. 1653 'rugged promises'; Grosart 'rugged providences', as in the clauses before and after
- **doubting-04.typ**: `#emph[2 Cor. 4. 18. chap. 11. Hebr. 15. Prov.] 14.` → `#emph[2 Cor. 4. 18. Hebr. 11. Prov.] 15. 24.`. 1653 'chap. 11. Hebr. 15. Prov. 14.' looks scrambled (numbers set before the next book's name): Heb. 11 (the worthies' heavenly objects) and Prov. 15. 24 ('the way of life is above to the wise', which the note 'a saint hath his feet where other men's heads are' glosses). Grosart drops the refs
- **doubting-04.typ**: `Fourthly, True grace makes` → `4\. True grace makes`. 1653 'Fourthly, True grace' among numbered heads 1.-10.; at least lowercase 'true' if 'Fourthly,' stays
- **doubting-05.typ**: `#footnote[Rom. 7. 19. 17.]` → `#footnote[Rom. 7. 19. 15.]`. 1653 'Rom. 7. 19. 17.'; 'what I hate, that do I' is Rom. 7. 15 (v. 17 is 'it is no more I that do it')
- **doubting-05.typ**: `against the #emph[Nauratines,]` → `against the #emph[Narentines,]`. 1653 and Grosart 'Nauratines'; Doge Pietro Candiano I fell (887) fighting the Narentines (Narentani)
- **doubting-05.typ**: `The conflict that is in the saints, is in the same faculties;` → `5\. The conflict that is in the saints, is in the same faculties;`. the 5th head lacks its number in 1653 (4. before, 6. after); Grosart supplies '[5.]'
- **doubting-05.typ**: `#emph[crucified the world with the affections, and lusts.]` → `#emph[crucified the flesh with the affections, and lusts.]`. 1653 and Grosart 'the world'; Gal. 5. 24 'crucified the flesh'. Brooks may have misquoted
- **doubting-08.typ**: `no temptations don't hurt nor harm the saints, so long as they are not resisted by them` → `no temptations do hurt nor harm the saints, so long as they are resisted by them`. 1653 'so long as they are not resisted' reverses the sense (the paragraph says resisted temptations are no sin); Grosart 'no temptations do hurt or harm the saints, so long as they are resisted by them'
- **ranks-02.typ**: `quoniam eo plures superabimus` → `quanto plures superabimus`. 1653 'quoniam eo plures'; the construction is 'tanto plus ... quanto plures' (the more ... the more), 'quoniam eo' is not good Latin; apply after the 'plas' fix
- **ranks-04.typ**: `is in #emph[Pihil,] and` → `is in #emph[Piel,] and`. 1653 'Pihil' (Brooks's name for the Hebrew stem); Grosart 'Piel'
- **ranks-04.typ**: `I press toward the mark for the price of the]` → `I press toward the mark for the prize of the]`. 1653 'price', an old spelling of prize (KJV Phil. 3:14 'prize')
- **ranks-04.typ**: `with what measures ye meet, it]` → `with what measures ye mete, it]`. 1653 'meet' = mete (KJV Matt. 7:2 'mete'); a different word
- **ranks-05.typ**: `Prov. 22. 29.] despise` → `Prov. 19. 2.] despise`. Prov. 22:29 (a man diligent in business) does not fit ignorance; Prov. 19:2 ('without knowledge the mind is not good') is cited below. 1653 prints 22. 29, perhaps caught from the next note (Mat. 22. 29)
- **propositions.typ**: `φλὸξ τοῦ πνεύματα.` → `φλὸξ τοῦ πνεύματος.`. gap 377: the 1652 prints 'πνεύματα' (unverified saying); genitive πνεύματος after τοῦ ('the flame of the Spirit')
- **use.typ**: `#emph[seorsim a me separat,]` → `#emph[seorsim a me,]`. 1653 'ſeorſim a me ſeparat': 'separat' (separates) is odd in the gloss 'from me, or apart from me'; perhaps a stray word, or 'separatim'
- **appendix-01.typ**: `’tis not simply the greatest of thy sins, but` → `’tis not simply the greatness of thy sins, but`. 1653 and Grosart 'greatest'; the sense (and 'thy great transgressions' just before) wants 'greatness'
- **appendix-03.typ**: `filled with horror and terror, if they may come to Christ,` → `filled with horror and terror, yet they may come to Christ,`. 1653 'though men are not thus and thus burdened ... if they may come'; Grosart drops 'not' and keeps 'if'. 'yet' gives the plain sense
- **appendix-04.typ**: `but is he willing surely? Though he be able,` → `but is he willing? surely though he be able,`. 1653 'is he willing ſurely? though'; Grosart ends the question at 'willing?'; 'surely' reads as the start of Satan's answer

## Spelling variants noted (for a consistency pass)

- sin-06.typ: verb 'loath'/'loaths' (= loathe) 8 times in the 'loathing' passage of the second remedy (KJV Ezek. 20:43 now 'lothe'/'loathe'); a book-wide choice whether to modernize to loathe/loathes
- sin-11.typ: 'I' for 'ay' (yes) kept in sin-11 twice ('open fields, I, and'; 'relations, I, your very lives'); book-wide decision whether to write 'ay'
- sin-11.typ: 'thorough' for 'through' kept 3 times in sin-11 ('swimming thorough the waters', 'pass thorough these/them'); Grosart 'through'
- duties-03.typ: Melanchthon spelled two ways in g2 files: 'Melancton' 2 (sin-11, duties-01), 'Melancthon' 1 (duties-03)
- duties-07.typ: Augustine named three ways in g2 files: 'Augustine' 3, 'Austin' 1 (sin-09), 'Augustin' 1 (duties-07)
- duties-04.typ: Psalms abbreviated 'Psal.' 10 times and 'Psa.' 3 times in g2 files; Matthew 'Mat.' 7 and 'Matth.' 1
- duties-06.typ: the machine pass changed 1653 Latin and names: 'quot colores' became 'quot colors', 'Iſidore' became 'Isidor' (duties-06); worth a book-wide check of Latin words the spelling table may have touched
- sin-11.typ: 'lye' for lie (verb) left unmodernized in sin-11 (4) and duties-08 (2), all proposed; may recur elsewhere in the book
- doubting-01.typ: Machine capitalizes after '!' mid-sentence: 'oh! But remember', 'oh! Then let no believer', 'Ah! You lamenting souls' (doubting-01); 1653 lowercase. Likely book-wide, for the same pass as 'tis.
- doubting-02.typ: Name forms: 'Mica' (doubting-01 x1, doubting-02 x1, in references) and 'Micha' (doubting-02 x1, in text); KJV Micah
- doubting-07.typ: 'tentation' (doubting-07 x1) beside 'temptation(s)' (doubting-07 x2, doubting-08 x45): book-wide choice
- ranks-01.typ: 'Wo'/'wo' (ranks-01 x3) beside 'Woe' (ranks-01 x4) in the woes quoted; KJV 'Woe'
- ranks-02.typ: Name forms: 'Sion' (ranks-02 x1, doubting-08 x1) beside 'Zion' (ranks-01 x1, ranks-02 x2, doubting-07 x1); 'Zach.' (ranks-02) for Zechariah
- ranks-03.typ: Spelling pairs in g3 files: 'burthen' (doubting-01 x1) / 'burden' (doubting-01 x2, -02 x1, -04 x2, -07 x2, ranks-02 x2); 'honor' (doubting-05 x1) / 'honour' (many); 'judgement' (doubting-04 x1, -05 x2, ranks-01 x1, ranks-02 x1) / 'judgment' (doubting-04 x1, ranks-01 x1, ranks-02 x1); 'Austin' (doubting-04, -05, ranks-03, x1 each) / 'Augustine' (doubting-03 x1) / 'Augustin' (doubting-01 x1); 'Sonship'/'son-ship' (doubting-06)
- use.typ: Samson/Sampson: 'Samson' 1, 'Sampsons' 1 in use.typ
- appendix-01.typ: "I'le" (= I'll) 4 times in appendix-01, once in appendix-03; the only form in the book; modern "I'll" if the book modernizes it
- appendix-01.typ: burthen/burden: 'burthen' 1, 'burden' 1 in the same paragraph of appendix-01
- appendix-03.typ: burthen/burden in appendix-03: 'burthened' 1, 'burden'/'burdened' 2

## Recommendations (2026-10-09)

1. **Restore the sense, Grosart agrees: yes.** able to melt (sin-06); it would
   make (sin-08); strengthening (duties-03); have not counted (duties-05);
   are resisted (doubting-08); rugged providences (doubting-03); "is he
   willing? surely though" (appendix-04).
2. **Restore the sense, no witness.** Yes: "yet they may come" (appendix-03),
   "human" (sin-08). Keep as printed: "let all the vials" (sin-03), "the
   greatest of thy sins" (appendix-01), "seorsim a me separat" (use).
3. **References: yes to all.** For duties-04, just drop the stray "2." rather
   than add 1 Thess. 5. 16, 17.
4. **Names to their KJV or standard forms: yes.** Delilah, Philistines,
   Ahithophel, Jeshurun, Calais, Aragon, Heliogabalus, Melanchthon,
   Gelimer/Vandals/Belisarius, Sanctus, Pacuvius (and its stop), Narentines,
   Augustine, Isidore, Piel.
5. **Latin, Greek and Hebrew: yes** (quaeristas, Medicamenta,
   Vedibbartignal-libbah, quanto plures, πνεύματος). Keep "Appium Sardis",
   modernized only to "Apium Sardis".
6. **Words and form.**
   - Yes: subtle (book-wide), temptation, momentary, prize, mete, drop
     "Simile.", the semicolon before "of sin" (duties-06), add the "5." head
     (doubting-05).
   - Keep: "Fourthly, true grace" (lowercase "true"); "crucified the world"
     (Brooks's misquotation of Gal. 5. 24).

## Settled (2026-10-10)

All 56 questions are decided. Where Grosart's edition made a decision, it
was followed (20, including "Melancthon" in his spelling). Where Grosart
keeps the 1653 reading, the text stays as printed: Nauratines, "crucified
the world", "the greatest of thy sins", "let all the vials", Gal. 4. 6. The
other 31 were settled as recommended above, with three kept as printed:
"Apium Sardis" (spelling only), "Fourthly, true grace" (case only) and
"seorsim a me separat".

## Spelling consistency (2026-10-10)

Each made one form through the book: burden/burdened (from burthen),
Augustine (from Austin/Augustin), fulness (as the KJV), Jerome (from
Hierome), I'll (from I'le), savour, and loathe/loathes for the verb ("you
are loath to come" keeps the adjective). Samson was already uniform.
