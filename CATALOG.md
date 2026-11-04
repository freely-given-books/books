# Freely Given Books: release 2026.11.03

Get it: `git clone --recursive -b stable https://github.com/freely-given-books/books.git`, then `./fgb build`.

Every book here has been signed off by the editor: a signed tag
`<author>/<book>/vN` on the commit it was checked at, and the book's
folder is exactly as it was signed off. Each book was checked again for
this release: its sources match the checksums in its `RELEASE.toml`, the
TEI rebuilds as committed (verify.py), every review edit is applied, the
print PDFs keep Lulu's rules and the EPUBs pass epubcheck. A book changed
since its sign-off and not yet signed off again is carried: its signed
version, built from its tag (it was checked when it was signed off).

Check a sign-off yourself:

```sh
git -c gpg.ssh.allowedSignersFile=allowed_signers tag -v <author>/<book>/vN
git diff --stat <author>/<book>/vN stable -- books/<author>/<book>   # nothing
sha256sum -c SHA256SUMS                                         # the downloads
```

Built with colophon 0.36.0.

| Book | Author | Version | Signed off |
| --- | --- | --- | --- |
| [The 1689 Baptist Confession of Faith: With Catechisms](#the-1689-baptist-confession-of-faith-with-catechisms) | Particular Baptist Churches | v1 | 2026-11-03 |
| [The Anatomy of Simon Magus](#the-anatomy-of-simon-magus) | Anonymous | v7 | 2026-11-03 |
| [All of Grace](#all-of-grace) | Charles Spurgeon | v16 | 2026-11-03 |
| [Grace Abounding to the Chief of Sinners](#grace-abounding-to-the-chief-of-sinners) | John Bunyan | v2 | 2026-11-03 |
| [The Pilgrim's Progress](#the-pilgrims-progress) | John Bunyan | v14 | 2026-11-03 |
| [The Death of Death in the Death of Christ](#the-death-of-death-in-the-death-of-christ) | John Owen | v1 | 2026-11-03 |
| [The Mortification of Sin](#the-mortification-of-sin) | John Owen | v1 | 2026-11-03 |
| [Sinners in the Hands of an Angry God](#sinners-in-the-hands-of-an-angry-god) | Jonathan Edwards | v9 | 2026-11-03 |
| [The Glorious Feast of the Gospel](#the-glorious-feast-of-the-gospel) | Richard Sibbes | v14 | 2026-11-03 |
| [The Crook in the Lot](#the-crook-in-the-lot) | Thomas Boston | v1 | 2026-11-03 |
| [Precious Remedies Against Satan’s Devices](#precious-remedies-against-satans-devices) | Thomas Brooks | v2 | 2026-11-03 |
| [The Secret Key of Heaven](#the-secret-key-of-heaven) | Thomas Brooks | v7 | 2026-11-03 |
| [Of Domestical Duties](#of-domestical-duties) | William Gouge | v2 | 2026-11-03 |
| [Christian Economy](#christian-economy) | William Perkins | v3 | 2026-11-03 |

## The 1689 Baptist Confession of Faith: With Catechisms

The Second London Baptist Confession of Faith (1677, owned in 1689), with the Baptist Catechism (1695) and An Orthodox Catechism (1680), from SVRBC's symbolics-data, with the confession's preface and closing statement transcribed for this edition.

- folder: `books/1689-baptist-confession/1689-baptist-confession`
- version v1: tag `1689-baptist-confession/1689-baptist-confession/v1`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: SVRBC symbolics-data (the symbolics-data submodule, commit c6853c8): confessions/lbcf1689, catechisms/bc1695 and catechisms/aoc1680, laid out as ThML by source/make_thml.py with no change of words, with our transcription of the preface and closing (source/transcription/) <https://gitlab.com/svrbc/symbolics-data>, `source/lbcf1689.thml.xml` (sha256 `3037183196dd304f…`)
- files: `1689-baptist-confession-v1.pdf`, `1689-baptist-confession-v1-cover.pdf`, `1689-baptist-confession-v1-cover-front.png`, `1689-baptist-confession-v1-cover-front.png`, `1689-baptist-confession-v1.epub`, `1689-baptist-confession-v1-reader.html`, `1689-baptist-confession-v1-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 40,321 printed words; 95.8% as printed
- changed in form only (spelling, case, punctuation): 1,670 words (4.1%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 22 words (0.1%); 48 words added, 5 removed
- gaps in the transcription: none
- notes: 0 added by the editor, 1 printed notes left out

## The Anatomy of Simon Magus

The 1700 printing in modern spelling and grammar, with translations of the Latin, a foreword and an abbreviations guide; two slips of the author's corrected (Jehu the Seer, Apollos).

- folder: `books/anonymous/the-anatomy-of-simon-magus`
- version v7: tag `anonymous/the-anatomy-of-simon-magus/v7`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: EEBO-TCP A25330: The Anatomy of Simon Magus, or, The Sin of Simony Laid Open (London, Charles Brome, 1700) <https://github.com/textcreationpartnership/A25330>, `source/A25330.tcp.xml` (sha256 `3a437401c8512841…`)
- files: `the-anatomy-of-simon-magus-v7.pdf`, `the-anatomy-of-simon-magus-v7-cover.pdf`, `the-anatomy-of-simon-magus-v7-cover-front.png`, `the-anatomy-of-simon-magus-v7-cover-front.png`, `the-anatomy-of-simon-magus-v7.epub`, `the-anatomy-of-simon-magus-v7-reader.html`, `the-anatomy-of-simon-magus-v7-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 30,558 printed words; 68.7% as printed
- changed in form only (spelling, case, punctuation): 8,763 words (28.7%)
- grammar modernized (hath -> has, thou -> you): 404 words (1.3%)
- changed in wording (emendations): 383 words (1.3%); 43 words added, 89 removed
- gaps in the transcription: 11, 11 restored, 0 left open
- notes: 4 added by the editor, 1 printed notes left out

## All of Grace

Spurgeon's All of Grace in the words of the 1886 printing (New York, Robert Carter & Brothers), newly transcribed from the page images, in place of CCEL's reworded text.

- folder: `books/charles-spurgeon/all-of-grace`
- version v16: tag `charles-spurgeon/all-of-grace/v16`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: Our transcription (CC0) of All of Grace (New York: Robert Carter & Brothers, 1886): Kraken OCR of the archive.org scan corrected by four witnesses and the page images: source/SOURCES.md <https://archive.org/details/allofgraceearnes00spur>, `source/grace.thml.xml` (sha256 `226534b2eeb7b0aa…`)
- witness: Monergism's PDF (2015), which follows CCEL's text: source/proofread-report.md <https://www.monergism.com/>
- witness: CCEL ThML of All of Grace, a modernized revision that rewords and drops passages, kept as source/grace.ccel.witness.xml: source/SOURCES.md <https://www.ccel.org/ccel/s/spurgeon/grace.xml>
- witness: GLM-OCR, Tesseract and archive.org's OCR of the 1886 scan, voters in the transcription (2026-11-01): source/SOURCES.md <https://archive.org/details/allofgraceearnes00spur>
- files: `all-of-grace-v16.pdf`, `all-of-grace-v16-cover.pdf`, `all-of-grace-v16-cover-front.png`, `all-of-grace-v16-cover-front.png`, `all-of-grace-v16.epub`, `all-of-grace-v16-reader.html`, `all-of-grace-v16-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 34,717 printed words; 99.7% as printed
- changed in form only (spelling, case, punctuation): 95 words (0.3%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 15 words (0.0%); 1 words added, 1 removed
- gaps in the transcription: none

## Grace Abounding to the Chief of Sinners

Bunyan's Grace Abounding to the Chief of Sinners in the words and italics of the sixth edition (1688), the last printed in his lifetime, newly transcribed from the page images, in modern spelling, with the passages that edition cut kept from the first (1666).

- folder: `books/john-bunyan/grace-abounding`
- version v2: tag `john-bunyan/grace-abounding/v2`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: Our transcription (CC0) of Grace Abounding, the sixth edition (London: Nath. Ponder, 1688): Kraken OCR of the British Library copy (EEBO microfilm, archive.org) corrected by six witnesses and the page images, the words the film lost in the gutter supplied from the 1692 copy, the 1666 first edition or the RTS text: source/transcription-report.md <https://archive.org/details/bim_early-english-books-1641-1700_grace-abounding-to-the-c_bunyan-john_1688>, `source/grace-abounding-1688.tcp.xml` (sha256 `e0d3b26abe8f9df5…`)
- source: EEBO-TCP A30143: Grace Abounding to the Chief of Sinners (London, George Larkin, 1666), the first edition, a witness and the text of the passages 1688 cut: source/witness-report.md <https://github.com/textcreationpartnership/A30143>, `source/A30143.witness.xml` (sha256 `6d927ab6622091da…`)
- witness: CCEL ThML of Grace Abounding (a later printing's text), the previous edition's source, kept as source/grace.ccel.witness.xml: source/witness-report.md <https://www.ccel.org/ccel/b/bunyan/grace.xml>
- witness: Grace Abounding (London, Robert Ponder, 1692), the seventh edition, a photograph of a printed copy (archive.org bunyangraceabounding5ed), read with Kraken: the witness for the words the 1688 film lost in the gutter: source/transcription-report.md <https://archive.org/details/bunyangraceabounding5ed>
- witness: GLM-OCR, Tesseract and archive.org's OCR of the 1688 scan, voters in the transcription (2026-11-01; the GLM and Tesseract texts in source/ocr/): source/transcription-report.md <https://archive.org/details/bim_early-english-books-1641-1700_grace-abounding-to-the-c_bunyan-john_1688>
- witness: The Works of John Bunyan, ed. George Offor (1855), vol. 1, archive.org scan and OCR, the witness for the passages added after 1666 (previous edition): source/proofread-report.md <https://archive.org/details/worksofjohnbunya01buny>
- witness: Grace Abounding, Religious Tract Society edition (1905), 'as nearly as possible' the eighth edition: Project Gutenberg #654, transcribed by David Price; a voter in the transcription: source/transcription-report.md <https://www.gutenberg.org/ebooks/654>
- files: `grace-abounding-v2.pdf`, `grace-abounding-v2-cover.pdf`, `grace-abounding-v2-cover-front.png`, `grace-abounding-v2-cover-front.png`, `grace-abounding-v2.epub`, `grace-abounding-v2-reader.html`, `grace-abounding-v2-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 44,253 printed words; 88.5% as printed
- changed in form only (spelling, case, punctuation): 3,659 words (8.3%)
- grammar modernized (hath -> has, thou -> you): 22 words (0.0%)
- changed in wording (emendations): 1,409 words (3.2%); 307 words added, 438 removed
- gaps in the transcription: none

## The Pilgrim's Progress

Bunyan's Pilgrim's Progress, both parts, as CCEL gives it (Logos's text of the 1853 Auburn edition), with CCEL's slips and lost words corrected against the first edition of Part I (1678) and a 1732 printing of Part II.

- folder: `books/john-bunyan/the-pilgrims-progress`
- version v14: tag `john-bunyan/the-pilgrims-progress/v14`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: CCEL ThML: John Bunyan, The Pilgrim's Progress, Parts I and II (Logos's text of the 1853 Auburn edition) <https://www.ccel.org/ccel/b/bunyan/pilgrim.xml>, `source/pilgrim.thml.xml` (sha256 `1ebdfd4db68990f3…`)
- source: EEBO-TCP A30170: The Pilgrim's Progress (London, Nath. Ponder, 1678), the first edition of Part I, a witness: source/witness-report.md <https://github.com/textcreationpartnership/A30170>, `source/A30170.witness.xml` (sha256 `14c3c96cab3e5a57…`)
- witness: The Pilgrim's Progress, Part II (London, 1732), archive.org scan, checked for Part II: source/proofread-report.md <https://archive.org/details/bim_eighteenth-century_the-pilgrims-progress-_bunyan-john_1732>
- witness: biblebb.com's Pilgrim's Progress Part 2, a modern copy, compared only
- files: `the-pilgrims-progress-v14.pdf`, `the-pilgrims-progress-v14-cover.pdf`, `the-pilgrims-progress-v14-cover-front.png`, `the-pilgrims-progress-v14-cover-front.png`, `the-pilgrims-progress-v14.epub`, `the-pilgrims-progress-v14-reader.html`, `the-pilgrims-progress-v14-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 110,974 printed words; 99.8% as printed
- changed in form only (spelling, case, punctuation): 153 words (0.1%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 63 words (0.1%); 20 words added, 13 removed
- gaps in the transcription: none

## The Death of Death in the Death of Christ

Owen's Death of Death in the Death of Christ in William Goold's text, as CCEL gives it, with CCEL's slips corrected against Goold's printing and Owen's own wording, chiefly his quotations of Scripture, restored from the 1648 first edition.

- folder: `books/john-owen/the-death-of-death`
- version v1: tag `john-owen/the-death-of-death/v1`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: CCEL ThML: John Owen, The Death of Death in the Death of Christ (Goold's text, The Works of John Owen, vol. 10, 1850-53) <https://www.ccel.org/ccel/o/owen/deathofdeath.xml>, `source/deathofdeath.thml.xml` (sha256 `c76ae424be0caab0…`)
- witness: Salus Electorum, Sanguis Jesu: or, The Death of Death in the Death of Christ (London, 1648), the first edition, archive.org scan, read on the page images and by local OCR: source/collation/*.jsonl <https://archive.org/details/bim_early-english-books-1641-1700_salus-electorum-sanguis_owen-john_1648>
- witness: The Works of John Owen, ed. William H. Goold, vol. 10 (1850), archive.org scan and local OCR, the printing CCEL was keyed from: source/collation/goold-ccel.jsonl <https://archive.org/details/worksofjohnowend0000owen>
- files: `the-death-of-death-v1.pdf`, `the-death-of-death-v1-cover.pdf`, `the-death-of-death-v1-cover-front.png`, `the-death-of-death-v1-cover-front.png`, `the-death-of-death-v1.epub`, `the-death-of-death-v1-reader.html`, `the-death-of-death-v1-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 191,818 printed words; 98.5% as printed
- changed in form only (spelling, case, punctuation): 1,893 words (1.0%)
- grammar modernized (hath -> has, thou -> you): 45 words (0.0%)
- changed in wording (emendations): 853 words (0.4%); 165 words added, 375 removed
- gaps in the transcription: none

## The Mortification of Sin

Owen's Of the Mortification of Sin in Believers in Goold's text (1850-53), as CCEL gives it, with two lines CCEL dropped and three slips corrected from Goold's printing, the 1668 second edition agreeing.

- folder: `books/john-owen/the-mortification-of-sin`
- version v1: tag `john-owen/the-mortification-of-sin/v1`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: CCEL ThML: John Owen, Of the Mortification of Sin in Believers, from The Works of John Owen, ed. William H. Goold, vol. 6 (1850-53) <https://www.ccel.org/ccel/o/owen/mort.xml>, `source/mort.thml.xml` (sha256 `e3577b8e81583250…`)
- source: EEBO-TCP A53715: Of the Mortification of Sin in Believers, the second edition (London, Nathanael Ponder, 1668), a witness: source/witness-report.md <https://github.com/textcreationpartnership/A53715>, `source/A53715.witness.xml` (sha256 `4603d4fd73838e69…`)
- witness: The Works of John Owen, ed. William H. Goold, vol. 6 (Johnstone and Hunter, 1850-53), archive.org scan and OCR, the printing CCEL follows: source/witness-report.md <https://archive.org/details/worksofjohnowe185006owen>
- witness: William H. Gross's modernized and annotated text (On the Wing, 2002, published by Monergism), read only to confirm passages; under copyright, not kept <https://www.monergism.com/>
- files: `the-mortification-of-sin-v1.pdf`, `the-mortification-of-sin-v1-cover.pdf`, `the-mortification-of-sin-v1-cover-front.png`, `the-mortification-of-sin-v1-cover-front.png`, `the-mortification-of-sin-v1.epub`, `the-mortification-of-sin-v1-reader.html`, `the-mortification-of-sin-v1-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 43,166 printed words; 99.2% as printed
- changed in form only (spelling, case, punctuation): 333 words (0.8%)
- grammar modernized (hath -> has, thou -> you): 1 words (0.0%)
- changed in wording (emendations): 20 words (0.0%); 32 words added, 11 removed
- gaps in the transcription: none

## Sinners in the Hands of an Angry God

Edwards's Enfield sermon (1741) from its second edition, in modern spelling, a small hand-out book quoting scripture from the Berean Standard Bible (two KJV quotations kept where Edwards builds on their words).

- folder: `books/jonathan-edwards/sinners-in-the-hands-of-an-angry-god`
- version v9: tag `jonathan-edwards/sinners-in-the-hands-of-an-angry-god/v9`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: EEBO-TCP (Evans) N05520: Edwards, True Grace (New York, James Parker, 1753), with the second edition of Sinners in the Hands of an Angry God bound after it (pp. 43-62) <https://github.com/textcreationpartnership/N05520>, `source/N05520.tcp.xml` (sha256 `9600c9fdc53098be…`)
- witness: The Berean Standard Bible, for the scripture quotations: source/proofread-report.md <https://berean.bible/>
- files: `sinners-in-the-hands-of-an-angry-god-v9.pdf`, `sinners-in-the-hands-of-an-angry-god-v9-cover.pdf`, `sinners-in-the-hands-of-an-angry-god-v9-cover-front.png`, `sinners-in-the-hands-of-an-angry-god-v9-cover-front.png`, `sinners-in-the-hands-of-an-angry-god-v9.epub`, `sinners-in-the-hands-of-an-angry-god-v9-reader.html`, `sinners-in-the-hands-of-an-angry-god-v9-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 23,249 printed words; 80.0% as printed
- changed in form only (spelling, case, punctuation): 4,074 words (17.5%)
- grammar modernized (hath -> has, thou -> you): 11 words (0.0%)
- changed in wording (emendations): 567 words (2.4%); 166 words added, 238 removed
- gaps in the transcription: 11, 7 restored, 4 left open

## The Glorious Feast of the Gospel

Sibbes's sermons on Isaiah 25:6-9 from the first edition (1650), in modern spelling; an earlier copy's misprints and dropped words corrected against the 1650 text, and its Greek and illegible places restored from the page images.

- folder: `books/richard-sibbes/the-glorious-feast-of-the-gospel`
- version v14: tag `richard-sibbes/the-glorious-feast-of-the-gospel/v14`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: EEBO-TCP A93248: The Glorious Feast of the Gospel (London, John Rothwell, 1650) <https://github.com/textcreationpartnership/A93248>, `source/A93248.tcp.xml` (sha256 `d95173b14fc232a3…`)
- witness: Monergism's modernized text (from the SDG reprint; (c) Monergism Books 2017), a check only: source/witness-report.md <https://www.monergism.com/>
- witness: The earlier Freely Given Books copy (a Grosart-type text, 1862), corrected against 1650
- files: `the-glorious-feast-of-the-gospel-v14.pdf`, `the-glorious-feast-of-the-gospel-v14-cover.pdf`, `the-glorious-feast-of-the-gospel-v14-cover-front.png`, `the-glorious-feast-of-the-gospel-v14-cover-front.png`, `the-glorious-feast-of-the-gospel-v14.epub`, `the-glorious-feast-of-the-gospel-v14-reader.html`, `the-glorious-feast-of-the-gospel-v14-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 56,190 printed words; 74.4% as printed
- changed in form only (spelling, case, punctuation): 13,236 words (23.6%)
- grammar modernized (hath -> has, thou -> you): 53 words (0.1%)
- changed in wording (emendations): 1,117 words (2.0%); 821 words added, 355 removed
- gaps in the transcription: 12, 12 restored, 0 left open
- notes: 0 added by the editor, 385 printed notes left out

## The Crook in the Lot

Boston's The Crook in the Lot in full, from Samuel M'Millan's edition of his Whole Works (1848), transcribed for this edition from two scans and checked against the page images; M'Millan's few misprints corrected, the 1811 printing agreeing.

- folder: `books/thomas-boston/the-crook-in-the-lot`
- version v1: tag `thomas-boston/the-crook-in-the-lot/v1`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: Our transcription of The Whole Works of Thomas Boston, ed. Samuel M'Millan, vol. 3 (Aberdeen, 1848), pp. 495-590, as ThML: how it was made in source/SOURCES.md <https://archive.org/details/wholeworksoflate03bost>, `source/crook.thml.xml` (sha256 `570af79869826424…`)
- source: CCEL ThML: Thomas Boston, The Crook in the Lot, a modernized revision (Institute of Practical Bible Education etext, 2000), untouched; a witness only, used as a hint in the OCR correction <https://www.ccel.org/ccel/b/boston/crook.xml>, `source/crook.ccel.witness.xml` (sha256 `64cc81b01e511b78…`)
- witness: M'Millan's 1848 volume, the University of Michigan scan: its OCR the second reading in the transcription (source/SOURCES.md) <https://archive.org/details/wholeworkslater06bostgoog>
- witness: The Crook in the Lot, Philadelphia 1811, archive.org scan: M'Millan's misprints corrected where it agrees (source/proofread-report.md) <https://archive.org/details/crookinlotorsove01bost>
- witness: The Crook in the Lot, 1782 and London 1791 printings, archive.org scans, consulted in the transcription; no scan of the 1737 first edition was found <https://archive.org/details/bim_eighteenth-century_crook-in-the-lot-or-the_boston-thomas_1782>
- files: `the-crook-in-the-lot-v1.pdf`, `the-crook-in-the-lot-v1-cover.pdf`, `the-crook-in-the-lot-v1-cover-front.png`, `the-crook-in-the-lot-v1-cover-front.png`, `the-crook-in-the-lot-v1.epub`, `the-crook-in-the-lot-v1-reader.html`, `the-crook-in-the-lot-v1-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 47,445 printed words; 97.4% as printed
- changed in form only (spelling, case, punctuation): 1,186 words (2.5%)
- grammar modernized (hath -> has, thou -> you): 1 words (0.0%)
- changed in wording (emendations): 52 words (0.1%); 8 words added, 5 removed
- gaps in the transcription: none

## Precious Remedies Against Satan’s Devices

Brooks's Precious Remedies Against Satan's Devices from the second edition (1653, corrected and enlarged), lightly modernized, its lost Greek and Hebrew restored from the 1652 and 1658 printings and the text proofread twice against Grosart's edition (1866).

- folder: `books/thomas-brooks/precious-remedies-against-satans-devices`
- version v2: tag `thomas-brooks/precious-remedies-against-satans-devices/v2`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: EEBO-TCP A77614: Precious Remedies against Satans Devices (London, M. Simmons for John Hancock, 1653), the second edition <https://github.com/textcreationpartnership/A77614>, `source/A77614.tcp.xml` (sha256 `0d7babe825595733…`)
- witness: The Complete Works of Thomas Brooks, ed. A. B. Grosart (1866), vol. 1, archive.org scan and OCR: source/proofread-report.md <https://archive.org/details/completeworksoft01broouoft>
- witness: Precious Remedies (1652), the first edition, archive.org scan of the EEBO microfilm: the Greek and Hebrew the TCP left out, source/gap_fixes.py <https://archive.org/details/bim_early-english-books-1641-1700_precious-remedies_brookes-thomas_1652>
- witness: Precious Remedies (1658), archive.org scan of the EEBO microfilm: gaps, source/gap_fixes.py <https://archive.org/details/bim_early-english-books-1641-1700_precious-remedies-_brookes-thomas_1658>
- witness: Monergism's keyed text of Grosart's edition, compared only
- files: `precious-remedies-against-satans-devices-v2.pdf`, `precious-remedies-against-satans-devices-v2-cover.pdf`, `precious-remedies-against-satans-devices-v2-cover-front.png`, `precious-remedies-against-satans-devices-v2-cover-front.png`, `precious-remedies-against-satans-devices-v2.epub`, `precious-remedies-against-satans-devices-v2-reader.html`, `precious-remedies-against-satans-devices-v2-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 102,836 printed words; 76.5% as printed
- changed in form only (spelling, case, punctuation): 23,466 words (22.8%)
- grammar modernized (hath -> has, thou -> you): 29 words (0.0%)
- changed in wording (emendations): 666 words (0.6%); 335 words added, 440 removed
- gaps in the transcription: 438, 438 restored, 0 left open
- notes: 0 added by the editor, 222 printed notes left out

## The Secret Key of Heaven

Brooks's The Privie Key of Heaven (1665) in modern spelling, from an earlier copy corrected against the 1665 printing; its dropped clauses, Latin, Greek and Hebrew restored from the page images.

- folder: `books/thomas-brooks/the-secret-key-of-heaven`
- version v7: tag `thomas-brooks/the-secret-key-of-heaven/v7`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: EEBO-TCP A29703: The Privie Key of Heaven (London, John Hancock, 1665) <https://github.com/textcreationpartnership/A29703>, `source/A29703.tcp.xml` (sha256 `b6742bf2f0d59f51…`)
- witness: Chapel Library's edition (Private Key to Heaven, EPUB, text in the public domain), which the earlier copy followed: source/proofread-report.md <https://www.chapellibrary.org/>
- witness: The 1665 printing's page images (archive.org), for the Greek, Hebrew and illegible places <https://archive.org/details/bim_early-english-books-1641-1700_the-privie-key-of-heaven_brookes-thomas_1665>
- witness: The earlier Freely Given Books copy (lightly modernized), folded in as the review
- files: `the-secret-key-of-heaven-v7.pdf`, `the-secret-key-of-heaven-v7-cover.pdf`, `the-secret-key-of-heaven-v7-cover-front.png`, `the-secret-key-of-heaven-v7-cover-front.png`, `the-secret-key-of-heaven-v7.epub`, `the-secret-key-of-heaven-v7-reader.html`, `the-secret-key-of-heaven-v7-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 102,961 printed words; 75.1% as printed
- changed in form only (spelling, case, punctuation): 20,937 words (20.3%)
- grammar modernized (hath -> has, thou -> you): 76 words (0.1%)
- changed in wording (emendations): 4,573 words (4.4%); 2,525 words added, 2,026 removed
- gaps in the transcription: 72, 61 restored, 11 left open
- notes: 0 added by the editor, 403 printed notes left out

## Of Domestical Duties

Gouge's Of Domesticall Duties (1622), all eight treatises in four volumes, in modern spelling with his wording kept; the transcription corrected against the 1622 page images, its Greek and Hebrew restored, six missing pages supplied from a second 1622 copy, and the printer's errata applied.

- folder: `books/william-gouge/domestical-duties`
- version v2: tag `william-gouge/domestical-duties/v2`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.15.0
- source: EEBO-TCP A68107: Of Domesticall Duties, Eight Treatises (London, John Haviland for William Bladen, 1622) <https://github.com/textcreationpartnership/A68107>, `source/A68107.tcp.xml` (sha256 `d7404af2ca63812e…`)
- source: Pages 191-196 of the 1622 edition, missing from the copy the TCP transcribed, transcribed from a second 1622 copy (archive.org, n220-n225); and the places where the TCP misreads the print, corrected from the page images <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties_gouge-william_1622>, `source/A68107.supplied.xml` (sha256 `e7541ceaa9342c27…`)
- witness: The 1622 page images of the copy the TCP was made from (archive.org), for the Greek and Hebrew, illegible letters and the proofread: source/proofread-report.md <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622>
- witness: The second edition (1626, in The Workes of William Gouge), consulted for single readings <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-_gouge-william_1626>
- witness: The third edition (1634), consulted for single readings and the errata <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-_gouge-william_1634>
- witness: The earlier Freely Given Books edition (made with the converter before the TEI): source/migration-differences.md
- files: `domestical-duties-v2-vol-1.pdf`, `domestical-duties-v2-vol-2.pdf`, `domestical-duties-v2-vol-3.pdf`, `domestical-duties-v2-vol-4.pdf`, `domestical-duties-v2-cover-vol-1.pdf`, `domestical-duties-v2-cover-vol-2.pdf`, `domestical-duties-v2-cover-vol-3.pdf`, `domestical-duties-v2-cover-vol-4.pdf`, `domestical-duties-v2-cover-vol-1-front.png`, `domestical-duties-v2-cover-vol-2-front.png`, `domestical-duties-v2-cover-vol-3-front.png`, `domestical-duties-v2-cover-vol-4-front.png`, `domestical-duties-v2-cover-vol-1-front.png`, `domestical-duties-v2-vol-1.epub`, `domestical-duties-v2-cover-vol-2-front.png`, `domestical-duties-v2-vol-2.epub`, `domestical-duties-v2-cover-vol-3-front.png`, `domestical-duties-v2-vol-3.epub`, `domestical-duties-v2-cover-vol-4-front.png`, `domestical-duties-v2-vol-4.epub`, `domestical-duties-v2-vol-1-reader.html`, `domestical-duties-v2-vol-1-compare.html`, `domestical-duties-v2-vol-2-reader.html`, `domestical-duties-v2-vol-2-compare.html`, `domestical-duties-v2-vol-3-reader.html`, `domestical-duties-v2-vol-3-compare.html`, `domestical-duties-v2-vol-4-reader.html`, `domestical-duties-v2-vol-4-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 290,438 printed words; 74.2% as printed
- changed in form only (spelling, case, punctuation): 73,650 words (25.4%)
- grammar modernized (hath -> has, thou -> you): 155 words (0.1%)
- changed in wording (emendations): 1,205 words (0.4%); 459 words added, 856 removed
- gaps in the transcription: 717, 717 restored, 0 left open
- notes: 7 added by the editor, 6 printed notes left out

## Christian Economy

Perkins's Christian Oeconomie (1609), translated from the Latin by Thomas Pickering, in modern spelling from the EEBO-TCP transcription; footnotes kept in the original spelling; readings corrected and words the transcription left out restored from the 1609 page images.

- folder: `books/william-perkins/christian-economy`
- version v3: tag `william-perkins/christian-economy/v3`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- source: EEBO-TCP A09377: Christian Oeconomie, or, A Short Survey of the Right Manner of Erecting and Ordering a Family (London, Felix Kyngston for Edmund Weaver, 1609), translated by Thomas Pickering <https://github.com/textcreationpartnership/A09377>, `source/A09377.tcp.xml` (sha256 `83d0f693c303aed4…`)
- source: Corrections to the TCP transcription from the 1609 page images: "Lombard," and "though" restored where it left them out; "or", "continencie", "his", "then", "the" and "bought" where it misread them <https://archive.org/details/bim_early-english-books-1475-1640_christian-oeconomie-or-_perkins-william_1609_0>, `source/A09377.supplied.xml` (sha256 `a43617693cab8cfe…`)
- witness: The 1609 printing, archive.org scan (the copy TCP was keyed from), local OCR (GLM-OCR and Tesseract) in source/ocr/: two readings corrected ("his wife", "he forbiddeth"); the page images also settled the proofread's questions (source/proofread-report.md) <https://archive.org/details/bim_early-english-books-1475-1640_christian-oeconomie-or-_perkins-william_1609_0>
- files: `christian-economy-v3.pdf`, `christian-economy-v3-cover.pdf`, `christian-economy-v3-cover-front.png`, `christian-economy-v3-cover-front.png`, `christian-economy-v3.epub`, `christian-economy-v3-reader.html`, `christian-economy-v3-compare.html`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 35,568 printed words; 83.6% as printed
- changed in form only (spelling, case, punctuation): 5,739 words (16.1%)
- grammar modernized (hath -> has, thou -> you): 10 words (0.0%)
- changed in wording (emendations): 86 words (0.2%); 44 words added, 45 removed
- gaps in the transcription: 39, 39 restored, 0 left open
- notes: 0 added by the editor, 1 printed notes left out
