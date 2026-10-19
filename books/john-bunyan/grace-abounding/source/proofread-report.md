# Grace Abounding: proofreading report

A full read of `chapters/typ`. The preface, the Relation (§1–264), the Call
to the Ministry, the Imprisonment and the Conclusion were read for sense.
They were checked against the 1666 first edition (`A30143.witness.xml`) and
the KJV. The base text is CCEL's enlarged edition. Where the 1666 printing
has the passage, its reading settled each fix; passages added after 1666
were fixed on sense alone (marked *sense*).

## Fixed

### Misprints (scanning slips in the CCEL text)

| § | was | now | evidence |
| --- | --- | --- | --- |
| 24 | what sin was *set* to be committed | *yet* | 1666 |
| 117 | He pressed *up* to take special heed that we | *us* | sense |
| 173 | that scripture, in these flying *sins*, would call | *fits* | 1666 |
| 183 | *brought forth* the villainy of my sin, and my loss by it to mind | *brought both* | 1666 |
| 191 | keep my heart upon this *world* | *word* | 1666 |
| 212 | I *would* which of them would get the better of me | *wonder* | 1666 |
| 231 | For by this scripture, *l* saw | *I* | |
| 330 | as spurs *into my flaw* | *unto my flesh* | 1666 |
| 335 | that oft *1* was as if I was on the ladder | *I* | 1666 |
| 338 | Is *lie* a godly man | *he* | 1666 |

### Doubled or stray words

- §104: "There is no peace, saith my God, to the wicked, *saith my God*". The 1666 printing and Isa. 57:21 have the phrase once.
- §25: "this temptation … is *more than usual* amongst poor creatures *than* many are aware of" is now "more usual … than", as in 1666.
- §337: "wherefore thought I, *save* the point being thus" is now "the point being thus", as in 1666.
- §263: "that twelfth of the author *of (Hebrews 12:22-4)*" is now "the author to the Hebrews (Heb. 12.22-24)", as in 1666.
- Preface: "grace;*4* for he found" was a stray footnote digit; it is now "grace; for he found".

### Punctuation and numbering

- §24/25: §25 ran on inside §24. It is now its own paragraph, as in 1666.
- §97: "97 The tempter" is now "97\. The tempter".
- §27: "hanging down my head*.* I wished" now has a comma, as in 1666.
- §71: "fore fit" is now "fore-fit", as in 1666.
- §213: "vanish and this" is now "vanish, and this".
- §221: "ground of hope*.* and so" now has a comma.
- §230: "redemption’ by this word" is now "redemption’; by this word".
- §338: "hast thou not made an hedge about him*.*" now ends with "?".
- §329: a stray hyphen was removed from "here -I will name".
- §337: "‘twas" had its apostrophe curled the wrong way; it is now "’twas".
- §200: "eighteeneth" is now "eighteenth".

### Scripture references

- Abbreviations missing their full stop are fixed: Rom 8.39, Heb 10.26, Heb 4.16, Esth 4.16, Col iii. 3,4 and Col. i 11.
- "Act. 8.4" is now "Acts 8.4".
- Roman references missing their full stop are fixed: 2 Pet. i 16, Heb. xii 22-24 and Eccles. vii 14.
- Shortened ranges are written out: Matt. 15.21-8 is now 15.21-28, and (ver. 22-4) is now (ver. 22-24).
- Spacing is fixed in "(S.of Sol. 4.8)", "(Num.14.25)", "(Mark 5. 2-5)", "(Heb. 12.16, 17) ." and "(I Cor. 16.15, 16) .".

## Checked and kept

- §107 "nay, thought I have felt him": the 1666 printing reads the same.
- "Rom. 8.38" for "shall separate us from the love of God" is Bunyan's own reference in 1666, so it is kept.
- "Jer. xlix. 11; xv. 11" cites two verses for two quotations, and both are right.
- Period words and forms are kept: forasmuch, overstood, strengthlessness, revengement, holloa, baulks, groaningly, -eth and -est verbs, "an hedge", "a-going", "began" as a participle.
- Zion (Joel 3.21) and Sion (Heb. 12.22) follow the KJV in each quotation.

## Changed after asking (the user agreed, 2026-10-02)

1. **§324, a clause restored from 1666.** It now reads: "the first was, how to be able to endure, should my imprisonment be long and tedious; the second was, how to be able to encounter death, should that be my portion." CCEL had lost the clause, which left "the first of these" and §325's "the second consideration" with nothing to refer to.
2. **The Imprisonment section now follows the book's style.** It uses single quotation marks for scripture and references in parentheses with Arabic chapters ("(John 14.1-4; 16.33; Col. 3.3, 4; Heb. 12.22-24)", "(Ps. 109.6-20)"). He/Him/His for God and Christ are capitalized in Bunyan's own sentences; quotations keep the KJV's lowercase.
3. **Book numbers are Arabic throughout.** The 9 references with I Sam., I Cor., II Cor., II Pet. and II Tim. are now 1 Sam., 1 Cor., 2 Cor., 2 Pet. and 2 Tim.
4. **One-off spellings modernized:** befal → befall, intreat/intreated → entreat/entreated, "for ought" → "for aught", bye-respects → by-respects, "every thing" → "everything", shewn → shown.

Kept on purpose: the double quotation marks for spoken words in the Relation (the voice in §22, Harry's swearing in §43). The book uses double marks for speech and single for scripture.

## Checklist

- `sweep.py --early`: the 64 words it lists are all period or British forms (forasmuch, overstood, -eth, colour) or "etc".
- `refs.py --quotes`: 168 references, 0 missing ("16.33" after "John 14.1-4;" is no longer counted separately). The 2 weak matches were read and kept.
- `./fgb check`: OK. The rebuild matches, the extraction matches, the TEI is valid and the book compiles.
- `./fgb build`: 144 pages and Lulu margins OK. epubcheck reports 0 errors and 0 warnings.
- PDF text: no wrongly curled quotes and no stray markup.

# Second proofread (2026-10-18)

A second full read, in two parts, against the 1666 first edition and a new
witness: George Offor's text (*Works*, 1855, vol. 1; archive.org OCR,
`~/.cache/fgb-scans/bunyan/offor-1855-vol-01.djvu.txt`). Offor printed the
enlarged text, so it is the only witness for the passages Bunyan added
after 1666.

## Fixed (67)

Where both witnesses agree unless marked:

- **Words and clauses CCEL lost**: §126 "and cause them to dwell with me,
  talk with me,"; §173 "it would cry aloud with a very great voice" (Offor);
  §234 "died by Him"; §22 "other my ungodly practices"; §23 "too too late";
  §41 "a very great softness"; §250 "that blessed sixth of John"; §261 "I
  was also"; §324 "all patience"; §332 "poor forlorn"; §335 "very last
  words"; §337 "or no, or save me"; and other short words (also, now, all,
  it, of, before, indeed).
- **Misprints**: §117 "faults and unsound rests" → false; §165 "continued
  fear" → continual; §91 "as I came in" → they; §222 "nigh into" → unto;
  §229 "is my righteousness" → as; §252 "to draw" → do draw; §253
  "leadings" → dealings; §301 "power to have the soul" → save (Offor); §330
  "forsook Him in His ways" → and; §334 "in such a case" → for such a cause;
  §157 dispensations (Offor); §243 word.
- **Word order**: §54 "then was I"; §140 "down fell I".
- **Quotations to the KJV**: §122 "upon his shoulder"; §179 "Pray not
  thou"; §238 "and I shall be innocent"; §326 "Look not at".
- **Punctuation**: §163 a paragraph split mid-sentence rejoined; §173,
  §206, §284, §315, §319 ("At the sessions after, I was indicted"), §325,
  §333; §109 "deceived! It is".
- **References**: §80 "(Luke 9.42; Mark 9.20)", §141 "12.16, 17", §164
  "Acts 1.18".
- **He/Him for God in Bunyan's sentences** (§72, §148, §155, §156, §192);
  §112 "thou" in a Jer. 3.4 quotation lowercase, as the KJV.

## Print layout

- The contents page and running heads were off by one: the template pairs
  short titles with chapters by position, and the Relation and the
  Conclusion had none (the Relation's 95 pages ran under "A Preface").
  Keach's *Gospel Minister's Maintenance* had the same fault; fixed too.
- The preface's dedication now stands apart from the first paragraph, as in
  the ebook.

## Questions (2026-10-18)

The readers' questions, grouped. Most are places where CCEL's wording
differs from what both 1666 and Offor print: an older editor's smoothing
rather than a keying slip.

### Bunyan’s own prayers: thou → Thou (4)

- `relation.typ`: “O Lord, thou knowest my life” → “O Lord, Thou knowest my life”. §10; Bunyan's own address to God: 'thou' lowercase but 'Thee' capitalized in the same sentence (book style capitalizes); or keep as an echo of scripture?
- `relation.typ`: “O Lord, I beseech thee, show me that thou hast loved me” → “O Lord, I beseech Thee, show me that Thou hast loved me”. §190; Bunyan's own prayer, lowercase here but capitalized elsewhere ('how couldest Thou' §188, 'shall I honour Thee' §200); book style capitalizes in Bunyan's sentences
- `relation.typ`: “Lord, if thou wilt now remove this sad affliction” → “Lord, if Thou wilt now remove this sad affliction”. §240; Bunyan's own prayer: 'thou wilt ... thou canst discern' lowercase here, capitalized in his prayers in §188, §200, §216 (same question as §190); if yes, also 'then I shall know that thou canst' → 'Thou canst'
- `imprisonment.typ`: “Lord Jesus, if thou wilt catch me, do; if not, I will venture for thy name.” → “Lord Jesus, if Thou wilt catch me, do; if not, I will venture for Thy name.”. §337; Bunyan's own prayer in lowercase; same question as §190/§240 (Relation prayers in §188, §200, §216 capitalize Thou/Thee)

### CCEL differs from both 1666 and Offor (34)

- `relation.typ`: “He should speak those words on purpose” → “He should speak them words on purpose”. §69; 1666 'speak them words'; Offor 'them words'; CCEL modernized period grammar (cf. §68 'especially them, ...' kept)
- `relation.typ`: “while in a natural state, committed” → “while in a natural estate, committed”. §147; 1666 and Offor 'natural estate'; CCEL modernized? (state/estate same sense)
- `relation.typ`: “many days are not for ever, many days” → “many days are not, not for ever, many days”. §199; 1666 'many days are not not for ever'; Offor 'many days are not, not for ever' (both witnesses repeat 'not', as emphasis); CCEL dropped one
- `relation.typ`: “and save me for all of them?” → “and save me for all them?”. §208; 1666 'save me for all them?'; Offor 'for all them?'; CCEL adds 'of'
- `relation.typ`: “now how I might be comforted?” → “now how might I be comforted?”. §208; 1666 'now how might I be comforted!'; Offor 'now how might I be comforted?'; CCEL's word order differs from both
- `relation.typ`: “found it exceedingly hard to trust Him” → “found it exceeding hard to trust Him”. §217; 1666 'exceedin[g] hard'; Offor 'exceeding hard' (and 'exceeding glad' just after in all three); CCEL modernized one of the pair
- `relation.typ`: “with more ease and freedom in abundance, have leaned” → “with more ease and freedom abundance, have leaned”. §217; 1666 'with more ease and freedom abundance'; Offor 'freedom abundance'; CCEL inserted 'in' (an editor's smoothing; 'abundance' = abundantly)
- `relation.typ`: “and should also be looked on by us” → “and should also be looked upon by us”. §234; 1666 and Offor 'looked on of God, and should also be looked upon by us'
- `relation.typ`: “with many others of a like nature” → “with many other of a like nature”. §235; 1666 'with many other of a like nature'; Offor same; CCEL modernized to 'others'
- `call-to-the-ministry.typ`: “a more ordinary and public preaching of the Word” → “a more ordinary and public preaching the Word”. §268; 1666 'publick preaching the Word'; Offor 'public preaching the word'; CCEL added 'of'
- `call-to-the-ministry.typ`: “yet those who were thus touched” → “yet those who thus were touched”. §273; 1666 'those who thus were touched'; Offor same; CCEL word order
- `call-to-the-ministry.typ`: “the sin and the person guilty” → “the sin and person guilty”. §280; 1666 'the sin and person guilty'; Offor same; CCEL added 'the'
- `imprisonment.typ`: “did sentence me to a perpetual banishment” → “did sentence me to perpetual banishment”. §319; 1666 'sentenced to perpetual banishment'; Offor 'did sentence me to perpetual banishment'
- `imprisonment.typ`: “delivered up to a gaoler’s hands, I was had home to prison, and there have lain now complete twelve years, waiting to see what God would suffer those men” → “delivered up to the gaoler’s hands, I was had home to prison again, and there have lain now complete twelve years, waiting to see what God would suffer these men”. §319; 1666 'to the Goalers hands, I was had home to Prison again ... these men'; Offor 'the jailer's hands ... prison again ... these men'; CCEL 'a', no 'again', 'those'
- `imprisonment.typ`: “and my own corruption; by all which” → “and my own corruptions; by all which”. §320; 1666 'my own corruptions'; Offor same
- `imprisonment.typ`: “only to give you a hint or two” → “only give you, in a hint or two,”. §320; 1666 'onely give you, in a hint or two, a word that may'; Offor 'only give you in a hint or two, a word'; CCEL's 'to give you a hint or two, a word' makes 'a word' dangle
- `imprisonment.typ`: “Those scriptures that I saw nothing in before, were made in this place” → “those scriptures that I saw nothing in before, are made in this place”. §321; 1666 'them Scriptures ... are made in this place'; Offor 'those Scriptures ... are made'; capital after semicolon is a CCEL keying quirk
- `imprisonment.typ`: “here I have seen and felt Him indeed” → “here I have seen Him and felt Him indeed”. §321; 1666 'here I have seen him, and felt him indeed'; Offor same
- `imprisonment.typ`: “have been great refreshments in this condition to me” → “have been great refreshment in this condition to me”. §322; 1666 'great refreshment'; Offor same
- `imprisonment.typ`: “Oh! the Mount Sion, the heavenly Jerusalem” → “Oh! the mount Zion, the heavenly Jerusalem”. §322; 1666 'the Mount Zion'; Offor 'the mount Zion'; Bunyan's own words, not the KJV quotation ('mount Sion' in Heb. 12.22, §264, stays). Capital 'Mount' differs from 'the mount Sion' in §262/§264
- `imprisonment.typ`: “I have seen a truth in this scripture” → “I have seen a truth in that scripture”. §322; 1666 'in that Scripture'; Offor same
- `imprisonment.typ`: “as being very tender to me” → “as being very tender of me”. §323; 1666 'very tender of me'; Offor same
- `imprisonment.typ`: “with one scripture or another” → “with one scripture and another”. §323; 1666 'with one Scripture and another'; Offor same
- `imprisonment.typ`: “I saw what was coming” → “I saw what was a-coming”. §324; 1666 'what was a coming'; Offor 'a-coming'; the book keeps 'a-going', 'a-doing'
- `imprisonment.typ`: “Again, if I only provide for these” → “Again, if I provide only for these”. §326; 1666 'if I provide onely for these'; Offor same (parallel to 'If I provide only for a prison')
- `imprisonment.typ`: “I found myself a man encompassed with infirmities; the parting with my wife and poor children hath often been to me in this place as the pulling the flesh from the bones, and that not only because I am somewhat too fond” → “I found myself a man, and compassed with infirmities; the parting with my wife and poor children hath oft been to me in this place as the pulling the flesh from my bones, and that not only because I am somewhat too too fond”. §327; 1666 'a man, and compassed with infirmities ... hath oft been ... from my bones ... somewhat too too fond'; Offor same throughout. 'too too' is the period intensive; CCEL modernized it away
- `imprisonment.typ`: “than all beside” → “than all I had besides”. §327; 1666 'than all I had besides'; Offor same
- `imprisonment.typ`: “if I should venture all for God” → “if I should now venture all for God”. §330; 1666 'if I should now venture all'; Offor same
- `imprisonment.typ`: “and as spurs unto my flesh” → “and was as spurs unto my flesh”. §330; 1666 'and was as spurs unto my flesh'; Offor same
- `imprisonment.typ`: “I had this lying much upon my spirits” → “had this lay much upon my spirit”. §333; 1666 'had this lay much upon my spirit'; Offor same; CCEL adds 'I', 'lying', 'spirits'
- `imprisonment.typ`: “for indeed at this time all the things” → “for indeed at that time all the things”. §333; 1666 'at that time'; Offor same
- `imprisonment.typ`: “make a scrambling shift” → “make a scrabbling shift”. §334; 1666 'scrabling'; Offor 'scrabbling' (Offor glosses it); the book keeps 'scrabble' in §198
- `imprisonment.typ`: “fixed with this resolution” → “fixed upon this resolution”. §338; 1666 'fixed upon this resolution'; Offor same
- `imprisonment.typ`: “though I had nothing at all for my pains” → “though I have nothing at all for my pains”. §338; 1666 'though I have nothing'; Offor same

### Passages added after 1666: CCEL differs from Offor (21)

- `relation.typ`: “had not God been merciful, I might” → “had not God been merciful unto me, I might”. §12; Offor 'had not God been merciful unto me'; passage not in 1666; CCEL seems to have dropped 'unto me'
- `relation.typ`: “to whom my heart was knit more than” → “to whom my heart before was knit more than”. §43; Offor 'to whom my heart before was knit'; not in 1666
- `relation.typ`: “in a little time we should see all professors” → “in a little time I should see all professors”. §44; Offor 'in a little time I should see'; not in 1666
- `relation.typ`: “pretending that they had only attained” → “pretending that they only had attained”. §45; Offor 'they only had attained'; not in 1666
- `relation.typ`: “but God, who had, I hope, designed me” → “but God, who had, as I hope, designed me”. §45; Offor 'who had, as I hope, designed me'; not in 1666
- `relation.typ`: “to accept of such principles” → “to accept of such cursed principles”. §45; Offor 'such cursed principles'; not in 1666
- `relation.typ`: “Yet, I thought, if this great man” → “Yet, thought I, if this great man”. §70; Offor 'Yet, thought I, if'; not in 1666
- `relation.typ`: “oh! how rich I should esteem myself” → “ah! how rich should I esteem myself”. §85; Offor 'ah! how rich should I esteem myself'; not in 1666
- `relation.typ`: “but by sin he has made himself” → “but by sin he had made himself”. §88; Offor 'by sin he had made himself'; not in 1666
- `relation.typ`: “they were not obnoxious in the sight of God” → “they were not obnoxious to the wrath of God”. §88; Offor 'not obnoxious to the wrath of God' ('obnoxious to' = liable to); not in 1666
- `relation.typ`: “when such thoughts have led through my heart” → “when such thoughts have fled through my heart”. §162; 'led through my heart' reads oddly; 'fled' (a led/fled slip) would fit, but Offor also reads 'led'; not in 1666. Keep unless the editor prefers 'fled'
- `relation.typ`: “These, I thought, are great sins” → “These, thought I, are great sins”. §171; Offor 'These, thought I, are great sins'; not in 1666
- `relation.typ`: “greatly fearing I would not be pardoned” → “greatly fearing I should not be pardoned”. §174; Offor 'should not be pardoned' (passage added after 1666, so Offor is the only witness); CCEL 'would' may be a modernizing slip
- `relation.typ`: “yea, this was a kind of chide for” → “yea, this was a kind of a chide for”. §174; Offor 'a kind of a chide ... a kind of a threatening' (parallel phrasing); CCEL dropped 'a'? Not in 1666
- `relation.typ`: “what it was I knew not; from whence it came I knew not.” → “what it was I knew not; or from whence it came I know not.”. §174; Offor 'what it was I knew not; or from whence it came I know not' (present: he still does not know, cf. 'I have not yet ... been able to make a judgment of it'); not in 1666
- `relation.typ`: “the blessed privilege to flee to Jesus for mercy” → “the blessed privilege to flee to Jesus Christ for mercy”. §174; Offor 'to flee to Jesus Christ for mercy'; not in 1666
- `relation.typ`: “you have put Him away from you” → “you have put Him from you”. §183; Offor 'you have put him from you' (sentence added after 1666); CCEL's 'away' looks editorial
- `relation.typ`: “but you yourself be no partaker of it” → “but yourself to be no partaker of it”. §183; Offor 'Behold, then, his goodness, but yourself to be no partaker of it' (not in 1666); CCEL reads as a smoothing
- `relation.typ`: “glory that came with it, was marvellous” → “glory that came with it, also, was marvellous”. §188; Offor 'the power, and sweetness, and light, and glory that came with it, also, was marvellous' (Bunyan's addition; 1666 ends the paragraph at 'sentence')
- `call-to-the-ministry.typ`: “My great desire in fulfilling my ministry” → “My great desire in my fulfilling my ministry”. §289; Offor 'My great desire in my fulfilling my ministry' (not in 1666); CCEL may have smoothed it
- `call-to-the-ministry.typ`: “and that he must give at last an account” → “and he must give at last an account”. §304; Offor 'and he must give at last an account'; CCEL added 'that' (not in 1666)

### References CCEL left out or cut short (6)

- `relation.typ`: “and in very truth and faithfulness.” → “and in very truth and faithfulness (2 Sam. 3.28).”. §249; 1666 ends 'and in very truth and faithfulness, 2 Sam. 3.28.'; Offor has a reference there too ('2 Sa. iii. 2[8]', OCR garbled); CCEL dropped it. Ask because the verse fits poorly
- `call-to-the-ministry.typ`: “for my sake; rejoice, and be exceeding glad, for great is your reward in heaven; for so persecuted they the prophets which were before you’ (Matt. 5.11)” → “for my sake; rejoice, and be exceeding glad, for great is your reward in heaven; for so persecuted they the prophets which were before you’ (Matt. 5.11, 12)”. §309; the quotation runs through Matt. 5.12 ('Rejoice, and be exceeding glad ...'); Offor and CCEL cite 5.11 only
- `imprisonment.typ`: “that your faith and hope might be in God, were the blessed words” → “that your faith and hope might be in God (1 Pet. 1.21), were blessed words”. §321; 1666 '1 Pet. 1.20. were blessed words'; Offor '1 Pe. i. 2[1], were blessed words'; KJV verse is 1 Pet. 1.21; CCEL dropped the reference and added 'the'
- `imprisonment.typ`: “to fear neither the horse nor his rider.” → “to fear neither the horse nor his rider (Job 39.18).”. §322; Offor 'fear neither the horse nor his rider. Job xxxix. 18.' (1666 has no reference)
- `imprisonment.typ`: “as dead to me and myself, as dead to them.” → “as dead to me, and myself as dead to them. ‘He that loveth father or mother, son or daughter, more than me, is not worthy of me’ (Matt. 10.37).”. §325; Offor ends the paragraph with 'He that loveth father or mother ... is not worthy of me. Matt. x. 37.' (a later addition, not in 1666); CCEL lacks it. If accepted, this supersedes the punctuation fix just above
- `imprisonment.typ`: “(1 Sam. 6.10)” → “(1 Sam. 6.10-12)”. §328; 1666 '1 Sam. 6.10, 11, 12'; Offor '1 Sa. vi. 10-12'

### Other (1)

- `relation.typ`: “He hath received gifts for the rebellious (Ps. 68.18)” → “‘He hath received gifts for the rebellious’ (Ps. 68.18)”. §166; scripture with reference but not in quotation marks, while the next words quote it ('The rebellious,'); though a paraphrase of KJV 'Thou hast received gifts for men; yea, for the rebellious also'

## Answers (the user, 2026-10-18)

1. **CCEL against both 1666 and Offor (34): restore only words CCEL lost.**
   Restored: §199 "not, not for ever"; §319 "home to prison again"; §320
   "to give you, in a hint or two, a word"; §321 "seen Him and felt Him";
   §327 "too too fond", "all I had besides"; §330 "now venture", "and was
   as spurs". Kept as CCEL: its word order and forms (those/them words,
   state/estate, others/other, Sion/Zion, a-coming, scrambling, this/that,
   tender to/of, refreshments, corruption, and the rest).
2. **Passages added after 1666 (21): follow Offor.** All 20 applied (§12,
   §43, §44, §45 ×3, §70, §85, §88 ×2, §171, §174 ×4, §183 ×2, §188, §289,
   §304). §162 "thoughts have led through my heart" stays: Offor reads
   "led" too.
3. **References: add all, Matt. 10.37 too.** 2 Sam. 3.28 (§249), Matt.
   5.11, 12 (§309), 1 Pet. 1.21 (§321), Job 39.18 (§322), 1 Sam. 6.10-12
   (§328), and Offor's closing quotation of Matt. 10.37 in §325.
4. **Style: all four.** Thou/Thee/Thy capitalized in Bunyan's own prayers
   (§10, §190, §240 ×2, §337); the Imprisonment's capitals after ; and :
   lowered (§321, §323, §326 ×2, §327); the ebook indents paragraphs, as
   Pilgrim's Progress and the print book do; the preface's "CHILDREN" in
   small caps (`OPENING_SMALLCAPS`).

Kept without asking: §166 "He hath received gifts for the rebellious" is a
paraphrase of Ps. 68.18, not set as a quotation.

Colors: the cover uses the `ochre` palette and ruled spine, as *The
Pilgrim's Progress* does; the ebook CSS now differs from Pilgrim's only in
the dedication's `.subtitle` rule.

## Checklist (2026-10-18)

- [x] `sweep.py`: 2 hits, both Bunyan's "too too" (kept).
- [x] `refs.py --quotes`: 172 references, 0 missing; the 2 weak matches are
  the two kept in the first proofread.
- [x] `./fgb check`: OK.
- [x] `./fgb build`: 122 pages, Lulu margins OK, no footnotes; epubcheck 0
  errors, 0 warnings.
- [x] PDF text: no wrongly curled quotes, no stray markup; contents and
  running heads right.
