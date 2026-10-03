# Gouge Vol. 2 review: progress (branch gouge-review-vol-2)

Helpers (scratchpad, /tmp/claude-1000/-home-courtney-Projects-fgbooks-books/7734942a-5f8c-443c-b192-56f7915e6a6f/scratchpad/v2/):
`orig/` and `auto/` = tei_extract --layer orig --expand / --only-auto (rebuild if gone);
`g.py PRE RX...` searches the printed text; `apply.py EDITS` exact replacements;
`wmap.py words.txt` whole-word spelling map over vol-2.

## Tools
- sweep.py --early: 748 vol-2 hits, mostly -eth verbs / Latin / etc. Real hits taken into the read.
- refs.py --quotes: vol-2 missing: Eccl. l. 1 and Jud. li. 2 (Socrates / Josephus, not Bible: fine);
  Eccles. 20. 7 (ch 3, question); 2 Sam. 25. 31, 37 (ch ?, check: 1 Sam. 25).
- No modern witness; evidence = 1622 printed layer only.
- Key finding: chapters/typ is the raw machine pass (unreviewed). Many 1622 spellings survive
  (aduiseth, cleering, kniteth, joyneth...): fixed by the word map (list below), to be reported
  for spelling.py / SPELLING so all volumes get them.

## Files read
- parallel-of-duties: done
- 01 seeking-marriage: done
- 02 getting-married: done
- 03 marital-unity: done
- NEXT STEP: read 04 living-together-in-love from line 1 (word map already applied to all vol-2 files;
  re-run wmap.py after adding words). Sync after ch 1-3 edits worked (94 new spelling decisions);
  ./fgb check not yet run. Case-check list (case.py) still to handle: 04 'Lord. man and wife', 04 'house. persons at',
  08 'Answ. subjection', 09 'Answ. wives cannot', 12 'subjection. example more', 13 'wife. love covereth',
  15 'entreat it. note how', 17 'Object. mothers in law', 01 '(Mat. 19. 6.) husbands therefore'.
  Also check every 'bruit' (brute) and verb 'loath' (loathe) in vol-2; ch 6 'and well him' -> 'tell him', 'which he good husband' -> 'the'.

## Questions so far (draft "Needs your decision")
- V2-1 ch3 §9: "(Eccles. 20. 7.)" for abstinence in a wife's separation: the verse is Ezek. 18. 6. Print: Eccles. 20. 7. Rec: Ezek. 18. 6.
- (ch3 §6 "for we have direct and strict warrant for it": print same; kept.)
- (ch3 Mal. 2. 16 for v. 15: kept, 2:16 also has the phrase.)

## Fixed (beyond the word map)
See e01.txt..eNN.txt in scratchpad; summary: Latin macron/-un slips (vinculum, inauditum...),
misprints (wise->wife, weight->weigh, beaten own->down, all->will, that me->that time, Solemat->Solemn),
refs (1 Tim. 2.2,10 -> 3.2,12; Joel 2.6 -> 2.16; Heb. 13 4), case (I A. take thee; Child-hood; IN->In),
punctuation.

## Word map applied (1622 spelling the machine missed)
cleering clearing
nearely nearly
aduiseth adviseth
greene green
sowen sown
foureteene fourteen
irkcsome irksome
indefinitly indefinitely
devillish devilish
patheticall pathetical
commiteth committeth
kniteth knitteth
shoo shoe
rendreth rendereth
alleage allege
alleadge allege
striken stricken
tenn ten
Jaacob Jacob
kitchinmaids kitchen-maids
kitchin kitchen
Beniamits Benjamites
catcht catched
journies journeys
fullenness sullenness
setleth settleth
deliberatly deliberately
perfome perform
pitty pity
marvell marvel
Angell Angel
cosen cousin
joyneth joineth
immoderatly immoderately
poysoned poisoned
Galile Galilee
dampt damped
Counseller Counsellor
burthensome burdensome
weyed weighed
hiderance hindrance
stolne stolen
hudled huddled
peruersness perverseness
inioyneth enjoineth
enioyneth enjoineth
enioynes enjoins
obstinatly obstinately
Heretique Heretic
heretique heretic
leasure leisure
ravisht ravished
tenour tenor
hainousness heinousness
hainously heinously
gauling galling
spuing spewing
spue spew
inticements enticements
inticed enticed
intice entice
daliance dalliance
asswaging assuaging
asswage assuage
asswaged assuaged
weakning weakening
paine pain
Canaanits Canaanites
