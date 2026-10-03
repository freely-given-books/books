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
