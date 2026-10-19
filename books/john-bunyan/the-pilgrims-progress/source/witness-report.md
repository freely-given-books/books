# Witnesses to the CCEL text

The edition is CCEL's text (`pilgrim.thml.xml`, Logos's text of the 1853
Auburn edition), with 38 editor decisions (`review-report.md`). Two
witnesses were compared with it, word by word, by `colophon/drift.py`;
neither is followed where it differs.

## What the editor changed in CCEL

- Typos: "sufferet do go on" → "suffered to go on" (Part II, stage 2),
  "scouged" → "scourged" (Part I, stage 9), "similtudes" → "similitudes"
  (Part II title page; KJV Hos. 12:10).
- Elisions keyed with an opening quote (‘Tis, ‘t is, ‘T was, ‘cause) set
  with an apostrophe: ’Tis, ’tis, ’Twas, ’cause, ’twould (31 places). The
  Conclusion's last line, "‘t will", is "’twill", as the 1678 edition prints it.
- Part II's subtitle, keyed lowercase in small capitals, capitalized
  (Wherein, Christian’s); it is set bold, like CCEL's other small capitals,
  because the book's font has none.
- Part II, stage 7: "Then he writ under it upon a marble stone these verses
  following:" is prose; CCEL keyed it as the first line of the verse.

## The earlier Freely Given Books copy

The copy published before this edition (`part1/`, `part2/`, `apology.typ`,
now removed; in git history) was CCEL's text, nearly word for word. Besides
the differences below, its book file left out **the whole Tenth Stage** of
Part I (chapter10.typ was never included), set the Apology as running prose
(its line breaks were lost), and set verse two ways (Part I plain, Part II
as quotations). Compared as printed (Typst's quote curling applied; `--`
printed an en dash):



### apology.typ

- edition: 2361 words; earlier copy: 2361 words; 99.96% alike
- 1 places differ (1 words of the edition, 1 of the earlier copy); 1 of them are 1 words or more

- **different** (1 words), after “…therefore , to conclude That I want solidness”
  - edition: —
  - earlier copy: –

### part-1/conclusion.typ

- edition: 208 words; earlier copy: 209 words; 99.28% alike
- 1 places differ (1 words of the edition, 2 of the earlier copy); 1 of them are 1 words or more

- **different** (2 words), after “…away as vain , I know not but”
  - edition: ’twill
  - earlier copy: it will

### part-1/stage-01.typ

- edition: 7033 words; earlier copy: 7033 words; 99.99% alike
- 1 places differ (1 words of the edition, 1 of the earlier copy); 1 of them are 1 words or more

- **different** (1 words), after “…town - talk in some other places )”
  - edition: —
  - earlier copy: –

### part-1/stage-05.typ

- edition: 8642 words; earlier copy: 8638 words; 99.95% alike
- 4 places differ (6 words of the edition, 2 of the earlier copy); 4 of them are 1 words or more

- **different** (1 words), after “…time that he has met with me .”
  - edition: ’Twas
  - earlier copy: Twas
- **different** (1 words), after “…of the Shadow of Death . Christian :”
  - edition: ’Twas
  - earlier copy: Twas
- **only in the edition** (2 words), after “…. To others it is thus discovered :”
  - edition: 1 .
- **only in the edition** (2 words), after “…an experimental confession of his faith in Christ”
  - edition: . 2

### part-1/stage-06.typ

- edition: 5169 words; earlier copy: 5169 words; 99.98% alike
- 1 places differ (1 words of the edition, 1 of the earlier copy); 1 of them are 1 words or more

- **different** (1 words), after “…good friend too , said Faithful , for”
  - edition: ’twas
  - earlier copy: twas

### part-1/stage-07.typ

- edition: 8943 words; earlier copy: 8919 words; 99.84% alike
- 14 places differ (26 words of the edition, 2 of the earlier copy); 14 of them are 1 words or more

- **different** (1 words), after “…all , even to prince and peasant .”
  - edition: ’Tis
  - earlier copy: Tis
- **only in the edition** (2 words), after “…be an honest man . For why ?”
  - edition: 1 .
- **only in the edition** (2 words), after “…can , making no question for conscience’ sake”
  - edition: . 2
- **only in the edition** (2 words), after “…which is according to the mind of God”
  - edition: . 3
- **only in the edition** (2 words), after “…. So more fit for the ministerial function”
  - edition: . 4
- **only in the edition** (2 words), after “…may be lawfully done . For why ?”
  - edition: 1 .
- **only in the edition** (2 words), after “…by what means soever a man becomes so”
  - edition: . 2
- **only in the edition** (2 words), after “…wife , or more custom to my shop”
  - edition: . 3
- **only in the edition** (2 words), after “…wizards , that are of this opinion .”
  - edition: 1 .
- **only in the edition** (2 words), after “…Gen . 34 : 20 - 24 .”
  - edition: 2 .
- **only in the edition** (2 words), after “…judgment . Luke 20 : 46 , 47”
  - edition: . 3
- **only in the edition** (2 words), after “…, and the very son of perdition .”
  - edition: 4 .
- **only in the edition** (2 words), after “…according . Acts 8 : 19 - 22”
  - edition: . 5
- **different** (1 words), after “…we went , and then we found What”
  - edition: ’twas
  - earlier copy: twas

### part-1/stage-08.typ

- edition: 1645 words; earlier copy: 1645 words; 99.94% alike
- 1 places differ (1 words of the edition, 1 of the earlier copy); 1 of them are 1 words or more

- **different** (1 words), after “…, “ Thus by the shepherds secrets are”
  - edition: reveal’d
  - earlier copy: revealed

### part-1/stage-09.typ

- edition: 11428 words; earlier copy: 11429 words; 99.98% alike
- 2 places differ (2 words of the edition, 3 of the earlier copy); 2 of them are 1 words or more

- **different** (2 words), after “…Cause they good counsel lightly did forget :”
  - edition: ’Tis
  - earlier copy: ‘ Tis
- **different** (1 words), after “…; but yet , you see , They’re”
  - edition: scourged
  - earlier copy: scouged

### part-2/authors-way.typ

- edition: 2389 words; earlier copy: 2396 words; 99.44% alike
- 11 places differ (10 words of the edition, 17 of the earlier copy); 11 of them are 1 words or more

- **only in the earlier copy** (1 words), after “…OF SENDING FORTH HIS SECOND PART”
  - earlier copy: 1
- **different** (1 words), after “…of me That I am truly thine ?”
  - edition: ’cause
  - earlier copy: cause
- **different** (2 words), after “…houses of I know not who . answer”
  - edition: ’Tis
  - earlier copy: ‘ Tis
- **different** (1 words), after “…a brother . In Holland , too ,”
  - edition: ’tis
  - earlier copy: tis
- **different** (2 words), after “…My Pilgrim should familiar with them be .”
  - edition: ’Tis
  - earlier copy: ‘ Tis
- **different** (2 words), after “…and their hearts , My Pilgrim has ;”
  - edition: ’cause
  - earlier copy: ‘ cause
- **different** (2 words), after “…but well to him that went before ;”
  - edition: ’Cause
  - earlier copy: ‘ Cause
- **different** (1 words), after “…show his wisdom’s covered With its own mantles”
  - edition: —
  - earlier copy: –
- **different** (1 words), after “…, I prithee on them smile : Perhaps”
  - edition: ’tis
  - earlier copy: tis
- **different** (2 words), after “…her in her virgin face , and learn”
  - edition: ’Twixt
  - earlier copy: ‘ Twixt
- **different** (2 words), after “…leave old doting sinners to his rod ,”
  - edition: ’Tis
  - earlier copy: ‘ Tis

### part-2/stage-02.typ

- edition: 6510 words; earlier copy: 6514 words; 99.88% alike
- 6 places differ (6 words of the edition, 10 of the earlier copy); 6 of them are 1 words or more

- **different** (2 words), after “…be the man That thereto moved me .”
  - edition: ’Tis
  - earlier copy: ‘ Tis
- **different** (2 words), after “…That thereto moved me . ’Tis true ,”
  - edition: ’twas
  - earlier copy: t was
- **different** (1 words), after “…now I run fast as I can :”
  - edition: ’Tis
  - earlier copy: Tis
- **different** (1 words), after “…. Ezek . 36 : 37 . And”
  - edition: ’tis
  - earlier copy: tis
- **different** (2 words), after “…in God’s sight is of great price .”
  - edition: ’Tis
  - earlier copy: T is
- **different** (2 words), after “…sit up a whole year together : so”
  - edition: ’tis
  - earlier copy: t is

### part-2/stage-03.typ

- edition: 3879 words; earlier copy: 3879 words; 99.95% alike
- 2 places differ (2 words of the edition, 2 of the earlier copy); 2 of them are 1 words or more

- **different** (1 words), after “…have spoken to you . Remember , that”
  - edition: ’twas
  - earlier copy: twas
- **different** (1 words), after “…hill will be the hardest of all .”
  - edition: ’Tis
  - earlier copy: Tis

### part-2/stage-05.typ

- edition: 4644 words; earlier copy: 4644 words; 99.96% alike
- 2 places differ (2 words of the edition, 2 of the earlier copy); 2 of them are 1 words or more

- **different** (1 words), after “…15 . Mr . Great - Heart :”
  - edition: ’Tis
  - earlier copy: Tis
- **different** (1 words), after “…what is it like ? said he .”
  - edition: ’Tis
  - earlier copy: Tis

### part-2/stage-06.typ

- edition: 15088 words; earlier copy: 15090 words; 99.94% alike
- 8 places differ (8 words of the edition, 10 of the earlier copy); 8 of them are 1 words or more

- **different** (1 words), after “…the happiness to have a habitation there !”
  - edition: ’Tis
  - earlier copy: Tis
- **different** (1 words), after “…in the world . Mr . Honest :”
  - edition: ’Tis
  - earlier copy: Tis
- **different** (1 words), after “…. Luke 8 : 2 , 3 .”
  - edition: ’Twas
  - earlier copy: Twas
- **different** (1 words), after “…“ Apples were they with which we were”
  - edition: beguil’d
  - earlier copy: beguiled
- **different** (1 words), after “…sin , not apples , hath our souls”
  - edition: defil’d
  - earlier copy: defiled
- **different** (2 words), after “…is master of a number of thieves :”
  - edition: ’twould
  - earlier copy: t would
- **different** (2 words), after “…full of hurry in fair - time .”
  - edition: ’Tis
  - earlier copy: T is
- **different** (1 words), after “…Mr . Dare - not - lie ,”
  - edition: ’Tis
  - earlier copy: Tis

### part-2/stage-07.typ

- edition: 4455 words; earlier copy: 4455 words; 99.98% alike
- 1 places differ (1 words of the edition, 1 of the earlier copy); 1 of them are 1 words or more

- **different** (1 words), after “…bestow , That show we pilgrims are ,”
  - edition: where’er
  - earlier copy: wherever

### part-2/stage-08.typ

- edition: 10288 words; earlier copy: 10292 words; 99.92% alike
- 7 places differ (6 words of the edition, 10 of the earlier copy); 7 of them are 1 words or more

- **different** (1 words), after “…one . Valiant - for - Truth :”
  - edition: ’Tis
  - earlier copy: Tis
- **only in the earlier copy** (1 words), after “…night and day To be a pilgrim .”
  - earlier copy: ”
- **different** (1 words), after “…: when heedless ones go on pilgrimage ,”
  - edition: ’tis
  - earlier copy: tis
- **different** (2 words), after “…if I be not as I should ,”
  - edition: ’tis
  - earlier copy: t is
- **different** (1 words), after “…that was her heart’s delight . Standfast :”
  - edition: ’Tis
  - earlier copy: Tis
- **different** (2 words), after “…. 1 Tim . 6 : 9 .”
  - edition: ’Twas
  - earlier copy: T was
- **different** (2 words), after “…father , and Jeroboam against his master .”
  - edition: ’Twas
  - earlier copy: T was

### part-2/to-the-reader.typ

- edition: 5030 words; earlier copy: 5030 words; 99.96% alike
- 2 places differ (2 words of the edition, 2 of the earlier copy); 2 of them are 1 words or more

- **different** (1 words), after “…”
  - edition: courteous
  - earlier copy: Courteous
- **different** (1 words), after “…he is highly commended of all . For”
  - edition: ’tis
  - earlier copy: tis


## The first edition of Part I (1678), EEBO-TCP A30170

`A30170.witness.xml`, the untouched TCP transcription. It is the first
edition: Bunyan added to the book in the second and third (1679)
editions, and CCEL's text has those additions, the best known of them
Mr. Worldly Wiseman, the Charity conversation, By-ends' friends, Lot's wife
and Diffidence. Compared loosely (spelling, case and punctuation ignored;
scripture references, which 1678 prints in the margin, left out), passages
of 8 words or more. The transcription also has 1,313 illegible gaps, which
count as differences here. There is no TCP transcription of Part II (1684);
the "Second part" in the TCP catalogue, A58733 (1683), is an imitation by
T. S.


### apology (apology.typ)

- edition: 1969 words; 1678 first edition: 1977 words; 93.72% alike
- 102 places differ (120 words of the edition, 128 of the 1678 first edition); 0 of them are 8 words or more


### text (part-1/stage-01.typ,part-1/stage-02.typ,part-1/stage-03.typ,part-1/stage-04.typ,part-1/stage-05.typ,part-1/stage-06.typ,part-1/stage-07.typ,part-1/stage-08.typ,part-1/stage-09.typ,part-1/stage-10.typ)

- edition: 54223 words; 1678 first edition: 44805 words; 83.90% alike
- 2918 places differ (12682 words of the edition, 3264 of the 1678 first edition); 22 of them are 8 words or more, listed below

- **only in the edition** (377 words), after “…a lamentable cry saying What shall I do”
  - edition: In this plight therefore he went home and restrained himself as long as he could that his wife and children … done before crying What shall I do to be saved
- **different** (10 words), after “…time appointed on them that diligently seek it”
  - edition: Read it so if you will in my book Obstinate
  - 1678 first edition: Ob
- **only in the edition** (2839 words), after “…thus much concerning Pliable Now as Christian was”
  - edition: walking solitary by himself he espied one afar off come crossing over the field to meet him and their hap … Mr Worldly Wiseman’s counsel So in process of time Christian
- **only in the edition** (160 words), after “…hazard of a few difficulties to obtain it”
  - edition: Christian Truly said Christian I have said the truth of Pliable and if I should also say all the truth … and will be the death of many more it is
- **only in the edition** (125 words), after “…the death of many more it is well”
  - edition: you escaped being by it dashed in pieces Christian Why truly I do not know what had become of me … hither they in no wise are cast out And therefore
- **only in the 1678 first edition** (10 words), after “…Every tub must stand upon its own bottom”
  - 1678 first edition: what is the answer else that I should give thee
- **only in the edition** (478 words), after “…company that shall continually cry Holy holy holy”
  - edition: Then said Charity to Christian Have you a family Are you a married man Christian I have a wife and … to good thou hast delivered thy soul from their blood
- **only in the edition** (33 words), after “…raisins and then he went on his way”
  - edition: Whilst Christian is among his godly friends Their golden mouths make him sufficient mends For all his griefs and when they let him go He’s clad with northern steel from top to toe
- **only in the edition** (12 words), after “…at last I got past this importunate one”
  - edition: And when I had shaken him off then I began to sing
- **only in the edition** (769 words), after “…them for now they went through a wilderness”
  - edition: Now when they were got almost quite out of this wilderness Faithful chanced to cast his eye back and espied … to God in well doing as unto a faithful Creator
- **only in the edition** (100 words), after “…and made their feet fast in the stocks”
  - edition: Here also they called again to mind what they had heard from their faithful friend Evangelist and were the more … which they were until they should be otherwise disposed of
- **different** (59 words), after “…there if a man may be so bold”
  - edition: By Ends Almost the whole town and in particular my Lord Turn about my Lord Time server my Lord Fair … tongues was my mother’s own brother by father’s side and
  - 1678 first edition: By-ends
- **only in the edition** (1897 words), after “…me that will be glad of my company”
  - edition: Now I saw in my dream that Christian and Hopeful forsook him and kept their distance before him but one … shall be rebuked by the flames of a devouring fire
- **only in the edition** (742 words), after “…up in this world and no farther go”
  - edition: Now I saw that just on the other side of this plain the pilgrims came to a place where stood … to fear before him and always to remember Lot’s wife
- **only in the 1678 first edition** (13 words), after “…with all manner of fruit and the leaves”
  - 1678 first edition: of the Trees were good for Medicine with the Fruit of these Trees
- **different** (9 words), after “…all manner of fruit and the leaves they”
  - edition: ate
  - 1678 first edition: were also much delighted and the leaves they eat
- **only in the edition** (1392 words), after “…counsel that they were brought into this distress”
  - edition: Now Giant Despair had a wife and her name was Diffidence so when he was gone to bed he told … the giant I will therefore search them in the morning
- **only in the edition** (8 words), after “…us But do you begin if you please”
  - edition: Christian I will sing you first this song
- **different** (10 words), after “…thou wilt be The loser Ignorance I’ll warrant”
  - edition: thee Then Christian addressed himself thus to his fellow Christian
  - 1678 first edition: Chr
- **only in the edition** (12 words), after “…go now but all of a sudden he”
  - edition: grew acquainted with one Save self and then he became a stranger
- **only in the edition** (18 words), after “…called to the marriage supper of the Lamb”
  - edition: There came out also at this time to meet them several of the King’s trumpeters clothed in white
- **different** (254 words), after “…of the King’s trumpeters clothed in white and”
  - edition: shining raiment who with melodious noises and loud made even the heavens to echo with their sound These trumpeters saluted … tongue or pen can their glorious joy be expressed Thus
  - 1678 first edition: th s

### conclusion (part-1/conclusion.typ)

- edition: 174 words; 1678 first edition: 164 words; 88.76% alike
- 20 places differ (24 words of the edition, 14 of the 1678 first edition); 0 of them are 8 words or more


