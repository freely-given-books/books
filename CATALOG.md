# Freely Given Books: release 2026.11.24.3

Get it: `git clone --recursive -b stable https://github.com/freely-given-books/books.git`, then `./fgb build`.

Every book here has been signed off by the editor: a signed tag
`<author>/<book>/vN` on the commit it was checked at (a Modern English
edition, its own paperback with its own Lulu revisions, has its own:
`<author>/<book>/modern/vN`), and the book's files are as they were
signed off (a book's two editions are signed off one by one; each tag
covers its edition's own files and the shared ones). Each book was checked again for
this release: its sources match the checksums in its `RELEASE.toml`, the
TEI rebuilds as committed (verify.py), every review edit is applied, the
print PDFs keep Lulu's rules and the EPUBs pass epubcheck. A book changed
since its sign-off and not yet signed off again is carried: its signed
version, built from its tag (it was checked when it was signed off).

Check a sign-off yourself:

```sh
git -c gpg.ssh.allowedSignersFile=allowed_signers tag -v <author>/<book>/vN
git diff --stat <author>/<book>/vN stable -- books/<author>/<book>   # that edition's: nothing
sha256sum -c SHA256SUMS                                         # the downloads
```

Built with colophon 0.65.1.

| Book | Author | Edition | Version | Signed off |
| --- | --- | --- | --- | --- |
| [The 1689 Baptist Confession of Faith: With Catechisms](#the-1689-baptist-confession-of-faith-with-catechisms) | Particular Baptist Churches | Classic | v2 | 2026-11-18 |
| [The Anatomy of Simon Magus](#the-anatomy-of-simon-magus) | Anonymous | Classic | v7 | 2026-11-03 |
| [All of Grace](#all-of-grace) | Charles Spurgeon | Classic | v17 | 2026-11-18 |
| [All of Grace (Modern English)](#all-of-grace-modern-english) | Charles Spurgeon | Modern English | v2 | 2026-11-22 |
| [Grace Abounding to the Chief of Sinners](#grace-abounding-to-the-chief-of-sinners) | John Bunyan | Classic | v3 | 2026-11-18 |
| [Grace Abounding to the Chief of Sinners (Modern English)](#grace-abounding-to-the-chief-of-sinners-modern-english) | John Bunyan | Modern English | v2 | 2026-11-22 |
| [The Pilgrim's Progress](#the-pilgrims-progress) | John Bunyan | Classic | v16 | 2026-11-18 |
| [The Pilgrim's Progress (Modern English)](#the-pilgrims-progress-modern-english) | John Bunyan | Modern English | v1 | 2026-11-22 |
| [Institutes of the Christian Religion](#institutes-of-the-christian-religion) | John Calvin | Classic | v1.1 (between Lulu revisions) | 2026-11-24 |
| [Indwelling Sin](#indwelling-sin) | John Owen | Classic | v3 | 2026-11-22 |
| [Indwelling Sin (Modern English)](#indwelling-sin-modern-english) | John Owen | Modern English | v1 | 2026-11-22 |
| [Of Temptation](#of-temptation) | John Owen | Classic | v3 | 2026-11-18 |
| [Of Temptation (Modern English)](#of-temptation-modern-english) | John Owen | Modern English | v1 | 2026-11-22 |
| [Owen on Sin](#owen-on-sin) | John Owen | Classic | v2 | 2026-11-22 |
| [Owen on Sin (Modern English)](#owen-on-sin-modern-english) | John Owen | Modern English | v1 | 2026-11-22 |
| [The Death of Death in the Death of Christ](#the-death-of-death-in-the-death-of-christ) | John Owen | Classic | v2 | 2026-11-18 |
| [The Mortification of Sin](#the-mortification-of-sin) | John Owen | Classic | v4 | 2026-11-22 |
| [The Mortification of Sin (Modern English)](#the-mortification-of-sin-modern-english) | John Owen | Modern English | v1 | 2026-11-22 |
| [Religious Affections](#religious-affections) | Jonathan Edwards | Classic | v1 | 2026-11-22 |
| [Religious Affections (Modern English)](#religious-affections-modern-english) | Jonathan Edwards | Modern English | v1 | 2026-11-22 |
| [Sinners in the Hands of an Angry God](#sinners-in-the-hands-of-an-angry-god) | Jonathan Edwards | Classic | v10 | 2026-11-18 |
| [Sinners in the Hands of an Angry God (Modern English)](#sinners-in-the-hands-of-an-angry-god-modern-english) | Jonathan Edwards | Modern English | v2 | 2026-11-22 |
| [The Glorious Feast of the Gospel](#the-glorious-feast-of-the-gospel) | Richard Sibbes | Classic | v16 | 2026-11-22 |
| [The Glorious Feast of the Gospel (Modern English)](#the-glorious-feast-of-the-gospel-modern-english) | Richard Sibbes | Modern English | v1 | 2026-11-22 |
| [The Crook in the Lot](#the-crook-in-the-lot) | Thomas Boston | Classic | v2 | 2026-11-18 |
| [The Crook in the Lot (Modern English)](#the-crook-in-the-lot-modern-english) | Thomas Boston | Modern English | v1 | 2026-11-22 |
| [Precious Remedies Against Satan’s Devices](#precious-remedies-against-satans-devices) | Thomas Brooks | Classic | v3 | 2026-11-18 |
| [Precious Remedies Against Satan’s Devices (Modern English)](#precious-remedies-against-satans-devices-modern-english) | Thomas Brooks | Modern English | v1 | 2026-11-22 |
| [The Secret Key of Heaven](#the-secret-key-of-heaven) | Thomas Brooks | Classic | v9 | 2026-11-22 |
| [The Secret Key of Heaven (Modern English)](#the-secret-key-of-heaven-modern-english) | Thomas Brooks | Modern English | v1 | 2026-11-22 |
| [The Surest and Safest Way of Thriving](#the-surest-and-safest-way-of-thriving) | Thomas Gouge | Classic | v2 | 2026-11-22 |
| [The Surest and Safest Way of Thriving (Modern English)](#the-surest-and-safest-way-of-thriving-modern-english) | Thomas Gouge | Modern English | v2 | 2026-11-22 |
| [A Divine Cordial](#a-divine-cordial) | Thomas Watson | Classic | v3 | 2026-11-18 |
| [A Divine Cordial (Modern English)](#a-divine-cordial-modern-english) | Thomas Watson | Modern English | v2 | 2026-11-22 |
| [Of Domestical Duties](#of-domestical-duties) | William Gouge | Classic | v4 | 2026-11-22 |
| [Of Domestical Duties (Modern English)](#of-domestical-duties-modern-english) | William Gouge | Modern English | v1 | 2026-11-22 |
| [Christian Economy](#christian-economy) | William Perkins | Classic | v5 | 2026-11-22 |
| [Christian Economy (Modern English)](#christian-economy-modern-english) | William Perkins | Modern English | v1 | 2026-11-22 |

## The 1689 Baptist Confession of Faith: With Catechisms

The Second London Baptist Confession of Faith (1677, owned in 1689), with the Baptist Catechism (1695) and An Orthodox Catechism (1680), from SVRBC's symbolics-data, with the confession's preface and closing statement transcribed for this edition.

- folder: `books/1689-baptist-confession/1689-baptist-confession`
- version v2: tag `1689-baptist-confession/1689-baptist-confession/v2`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of this paperback
- source: SVRBC symbolics-data (the symbolics-data submodule, commit c6853c8): confessions/lbcf1689, catechisms/bc1695 and catechisms/aoc1680, laid out as ThML by source/make_thml.py with no change of words, with our transcription of the preface and closing (source/transcription/) <https://gitlab.com/svrbc/symbolics-data>, `source/lbcf1689.thml.xml` (sha256 `3037183196dd304f…`)
- files: `1689-baptist-confession-v2.pdf`, `1689-baptist-confession-v2-cover.pdf`, `1689-baptist-confession-v2-cover-front.png`, `1689-baptist-confession-v2-cover-front.png`, `1689-baptist-confession-v2.epub`, `1689-baptist-confession-v2-reader.html`, `1689-baptist-confession-v2-compare.html`, `1689-baptist-confession-v2-cover-back.webp`, `1689-baptist-confession-v2-cover-spine.webp`, `1689-baptist-confession-v2-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 40,321 printed words; 95.8% as printed
- changed in form only (spelling, case, punctuation): 1,671 words (4.1%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 22 words (0.1%); 48 words added, 5 removed
- gaps in the transcription: none
- notes: 0 added by the editor, 1 printed notes left out

## The Anatomy of Simon Magus

The 1700 printing in modern spelling and grammar, with translations of the Latin, a foreword and an abbreviations guide; two slips of the author's corrected (Jehu the Seer, Apollos).

- folder: `books/anonymous/the-anatomy-of-simon-magus`
- version v7: tag `anonymous/the-anatomy-of-simon-magus/v7`, signed off 2026-11-03 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 7 of this paperback
- source: EEBO-TCP A25330: The Anatomy of Simon Magus, or, The Sin of Simony Laid Open (London, Charles Brome, 1700) <https://github.com/textcreationpartnership/A25330>, `source/A25330.tcp.xml` (sha256 `3a437401c8512841…`)
- files: `the-anatomy-of-simon-magus-v7.pdf`, `the-anatomy-of-simon-magus-v7-cover.pdf`, `the-anatomy-of-simon-magus-v7-cover-front.png`, `the-anatomy-of-simon-magus-v7-cover-front.png`, `the-anatomy-of-simon-magus-v7.epub`, `the-anatomy-of-simon-magus-v7-reader.html`, `the-anatomy-of-simon-magus-v7-compare.html`, `the-anatomy-of-simon-magus-v7-cover-back.webp`, `the-anatomy-of-simon-magus-v7-cover-spine.webp`, `the-anatomy-of-simon-magus-v7-cover-front.webp`

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
- version v17: tag `charles-spurgeon/all-of-grace/v17`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 17 of this paperback
- source: Our transcription (CC0) of All of Grace (New York: Robert Carter & Brothers, 1886): Kraken OCR of the archive.org scan corrected by four witnesses and the page images: source/SOURCES.md <https://archive.org/details/allofgraceearnes00spur>, `source/grace.thml.xml` (sha256 `2ca49ee46a82525d…`)
- witness: Monergism's PDF (2015), which follows CCEL's text: source/proofread-report.md <https://www.monergism.com/>
- witness: CCEL ThML of All of Grace, a modernized revision that rewords and drops passages, kept as source/grace.ccel.witness.xml: source/SOURCES.md <https://www.ccel.org/ccel/s/spurgeon/grace.xml>
- witness: GLM-OCR, Tesseract and archive.org's OCR of the 1886 scan, voters in the transcription (2026-11-01): source/SOURCES.md <https://archive.org/details/allofgraceearnes00spur>
- files: `all-of-grace-v17.pdf`, `all-of-grace-v17-cover.pdf`, `all-of-grace-v17-cover-front.png`, `all-of-grace-v17-cover-front.png`, `all-of-grace-v17.epub`, `all-of-grace-v17-reader.html`, `all-of-grace-v17-compare.html`, `all-of-grace-v17-cover-back.webp`, `all-of-grace-v17-cover-spine.webp`, `all-of-grace-v17-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 34,717 printed words; 99.7% as printed
- changed in form only (spelling, case, punctuation): 98 words (0.3%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 17 words (0.0%); 1 words added, 1 removed
- gaps in the transcription: none

## All of Grace (Modern English)

Spurgeon's All of Grace in the words of the 1886 printing (New York, Robert Carter & Brothers), newly transcribed from the page images, in place of CCEL's reworded text.

- folder: `books/charles-spurgeon/all-of-grace`
- version v2: tag `charles-spurgeon/all-of-grace/modern/v2`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v17
- sign-off note: Based on: the Classic v17 (charles-spurgeon/all-of-grace/v17).
- files: `all-of-grace-v2-modern.pdf`, `all-of-grace-v2-cover-modern.pdf`, `all-of-grace-v2-cover-modern-front.png`, `all-of-grace-v2-modern.epub`, `all-of-grace-v2-modern-reader.html`, `all-of-grace-v2-cover-modern-back.webp`, `all-of-grace-v2-cover-modern-spine.webp`, `all-of-grace-v2-cover-modern-front.webp`

## Grace Abounding to the Chief of Sinners

Bunyan's Grace Abounding to the Chief of Sinners in the words and italics of the sixth edition (1688), the last printed in his lifetime, newly transcribed from the page images, in modern spelling, with the passages that edition cut kept from the first (1666).

- folder: `books/john-bunyan/grace-abounding`
- version v3: tag `john-bunyan/grace-abounding/v3`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 3 of this paperback
- source: Our transcription (CC0) of Grace Abounding, the sixth edition (London: Nath. Ponder, 1688): Kraken OCR of the British Library copy (EEBO microfilm, archive.org) corrected by six witnesses and the page images, the words the film lost in the gutter supplied from the 1692 copy, the 1666 first edition or the RTS text: source/transcription-report.md <https://archive.org/details/bim_early-english-books-1641-1700_grace-abounding-to-the-c_bunyan-john_1688>, `source/grace-abounding-1688.tcp.xml` (sha256 `e0d3b26abe8f9df5…`)
- source: EEBO-TCP A30143: Grace Abounding to the Chief of Sinners (London, George Larkin, 1666), the first edition, a witness and the text of the passages 1688 cut: source/witness-report.md <https://github.com/textcreationpartnership/A30143>, `source/A30143.witness.xml` (sha256 `6d927ab6622091da…`)
- witness: CCEL ThML of Grace Abounding (a later printing's text), the previous edition's source, kept as source/grace.ccel.witness.xml: source/witness-report.md <https://www.ccel.org/ccel/b/bunyan/grace.xml>
- witness: Grace Abounding (London, Robert Ponder, 1692), the seventh edition, a photograph of a printed copy (archive.org bunyangraceabounding5ed), read with Kraken: the witness for the words the 1688 film lost in the gutter: source/transcription-report.md <https://archive.org/details/bunyangraceabounding5ed>
- witness: GLM-OCR, Tesseract and archive.org's OCR of the 1688 scan, voters in the transcription (2026-11-01; the GLM and Tesseract texts in source/ocr/): source/transcription-report.md <https://archive.org/details/bim_early-english-books-1641-1700_grace-abounding-to-the-c_bunyan-john_1688>
- witness: The Works of John Bunyan, ed. George Offor (1855), vol. 1, archive.org scan and OCR, the witness for the passages added after 1666 (previous edition): source/proofread-report.md <https://archive.org/details/worksofjohnbunya01buny>
- witness: Grace Abounding, Religious Tract Society edition (1905), 'as nearly as possible' the eighth edition: Project Gutenberg #654, transcribed by David Price; a voter in the transcription: source/transcription-report.md <https://www.gutenberg.org/ebooks/654>
- files: `grace-abounding-v3.pdf`, `grace-abounding-v3-cover.pdf`, `grace-abounding-v3-cover-front.png`, `grace-abounding-v3-cover-front.png`, `grace-abounding-v3.epub`, `grace-abounding-v3-reader.html`, `grace-abounding-v3-compare.html`, `grace-abounding-v3-cover-back.webp`, `grace-abounding-v3-cover-spine.webp`, `grace-abounding-v3-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 44,253 printed words; 88.5% as printed
- changed in form only (spelling, case, punctuation): 3,659 words (8.3%)
- grammar modernized (hath -> has, thou -> you): 22 words (0.0%)
- changed in wording (emendations): 1,413 words (3.2%); 307 words added, 439 removed
- gaps in the transcription: none

## Grace Abounding to the Chief of Sinners (Modern English)

Bunyan's Grace Abounding to the Chief of Sinners in the words and italics of the sixth edition (1688), the last printed in his lifetime, newly transcribed from the page images, in modern spelling, with the passages that edition cut kept from the first (1666).

- folder: `books/john-bunyan/grace-abounding`
- version v2: tag `john-bunyan/grace-abounding/modern/v2`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v3
- sign-off note: Based on: the Classic v3 (john-bunyan/grace-abounding/v3).
- files: `grace-abounding-v2-modern.pdf`, `grace-abounding-v2-cover-modern.pdf`, `grace-abounding-v2-cover-modern-front.png`, `grace-abounding-v2-modern.epub`, `grace-abounding-v2-modern-reader.html`, `grace-abounding-v2-cover-modern-back.webp`, `grace-abounding-v2-cover-modern-spine.webp`, `grace-abounding-v2-cover-modern-front.webp`

## The Pilgrim's Progress

Bunyan's Pilgrim's Progress, both parts, as CCEL gives it (Logos's text of the 1853 Auburn edition), with CCEL's slips and lost words corrected against the first edition of Part I (1678) and a 1732 printing of Part II.

- folder: `books/john-bunyan/the-pilgrims-progress`
- version v16: tag `john-bunyan/the-pilgrims-progress/v16`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 16 of this paperback
- source: CCEL ThML: John Bunyan, The Pilgrim's Progress, Parts I and II (Logos's text of the 1853 Auburn edition) <https://www.ccel.org/ccel/b/bunyan/pilgrim.xml>, `source/pilgrim.thml.xml` (sha256 `1ebdfd4db68990f3…`)
- source: EEBO-TCP A30170: The Pilgrim's Progress (London, Nath. Ponder, 1678), the first edition of Part I, a witness: source/witness-report.md <https://github.com/textcreationpartnership/A30170>, `source/A30170.witness.xml` (sha256 `14c3c96cab3e5a57…`)
- witness: The Pilgrim's Progress, Part II (London, 1732), archive.org scan, checked for Part II: source/proofread-report.md <https://archive.org/details/bim_eighteenth-century_the-pilgrims-progress-_bunyan-john_1732>
- witness: biblebb.com's Pilgrim's Progress Part 2, a modern copy, compared only
- files: `the-pilgrims-progress-v16.pdf`, `the-pilgrims-progress-v16-cover.pdf`, `the-pilgrims-progress-v16-cover-front.png`, `the-pilgrims-progress-v16-cover-front.png`, `the-pilgrims-progress-v16.epub`, `the-pilgrims-progress-v16-reader.html`, `the-pilgrims-progress-v16-compare.html`, `the-pilgrims-progress-v16-cover-back.webp`, `the-pilgrims-progress-v16-cover-spine.webp`, `the-pilgrims-progress-v16-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 110,974 printed words; 99.8% as printed
- changed in form only (spelling, case, punctuation): 158 words (0.1%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 72 words (0.1%); 22 words added, 18 removed
- gaps in the transcription: none

## The Pilgrim's Progress (Modern English)

Bunyan's Pilgrim's Progress, both parts, as CCEL gives it (Logos's text of the 1853 Auburn edition), with CCEL's slips and lost words corrected against the first edition of Part I (1678) and a 1732 printing of Part II.

- folder: `books/john-bunyan/the-pilgrims-progress`
- version v1: tag `john-bunyan/the-pilgrims-progress/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v16
- sign-off note: Based on: the Classic v16 (john-bunyan/the-pilgrims-progress/v16).
- files: `the-pilgrims-progress-v1-modern.pdf`, `the-pilgrims-progress-v1-cover-modern.pdf`, `the-pilgrims-progress-v1-cover-modern-front.png`, `the-pilgrims-progress-v1-modern.epub`, `the-pilgrims-progress-v1-modern-reader.html`, `the-pilgrims-progress-v1-cover-modern-back.webp`, `the-pilgrims-progress-v1-cover-modern-spine.webp`, `the-pilgrims-progress-v1-cover-modern-front.webp`

## Institutes of the Christian Religion

Calvin's Institutes of the Christian Religion in Henry Beveridge's translation (Calvin Translation Society, Edinburgh, 1845), in six volumes: the CCEL text checked word for word against the 1845 printing and restored to it where CCEL departs.

- folder: `books/john-calvin/institutes-of-the-christian-religion`
- version v1.1: tag `john-calvin/institutes-of-the-christian-religion/v1.1`, signed off 2026-11-24 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of this paperback
- a point version: an improved ebook after Lulu revision 1; the print PDFs are that revision's (v1, built from its tag)
- sign-off note: Print: changed since v1 (institutes-vol-5.pdf: 1 page(s) differ: 32); not a Lulu revision.
- source: CCEL ThML: John Calvin, Institutes of the Christian Religion, trans. Henry Beveridge (Edinburgh: Calvin Translation Society, 1845): the text <https://www.ccel.org/ccel/c/calvin/institutes.xml>, `source/institutes.thml.xml` (sha256 `d7995178c1fe1723…`)
- witness: The 1845 printing, vol. 1 (archive.org scan, University of Toronto copy), read with Kraken and Tesseract and collated with the CCEL text: every difference checked on the page image <https://archive.org/details/instituteschrist01calvuoft>
- witness: The 1845 printing, vol. 2 (archive.org scan, University of Toronto copy), collated as vol. 1 <https://archive.org/details/institutesofreli02calvuoft>
- witness: The 1845 printing, vol. 3 (archive.org scan, University of Toronto copy), collated as vol. 1 <https://archive.org/details/institutesofthec03calvuoft>
- files: `institutes-of-the-christian-religion-v1-cover-vol-1-front.png`, `institutes-of-the-christian-religion-v1.1-institutes-vol-1.epub`, `institutes-of-the-christian-religion-v1-cover-vol-2-front.png`, `institutes-of-the-christian-religion-v1.1-institutes-vol-2.epub`, `institutes-of-the-christian-religion-v1-cover-vol-3-front.png`, `institutes-of-the-christian-religion-v1.1-institutes-vol-3.epub`, `institutes-of-the-christian-religion-v1-cover-vol-4-front.png`, `institutes-of-the-christian-religion-v1.1-institutes-vol-4.epub`, `institutes-of-the-christian-religion-v1-cover-vol-5-front.png`, `institutes-of-the-christian-religion-v1.1-institutes-vol-5.epub`, `institutes-of-the-christian-religion-v1-cover-vol-6-front.png`, `institutes-of-the-christian-religion-v1.1-institutes-vol-6.epub`, `institutes-of-the-christian-religion-v1-institutes-vol-1.pdf`, `institutes-of-the-christian-religion-v1-institutes-vol-2.pdf`, `institutes-of-the-christian-religion-v1-institutes-vol-3.pdf`, `institutes-of-the-christian-religion-v1-institutes-vol-4.pdf`, `institutes-of-the-christian-religion-v1-institutes-vol-5.pdf`, `institutes-of-the-christian-religion-v1-institutes-vol-6.pdf`, `institutes-of-the-christian-religion-v1-cover-vol-1.pdf`, `institutes-of-the-christian-religion-v1-cover-vol-2.pdf`, `institutes-of-the-christian-religion-v1-cover-vol-3.pdf`, `institutes-of-the-christian-religion-v1-cover-vol-4.pdf`, `institutes-of-the-christian-religion-v1-cover-vol-5.pdf`, `institutes-of-the-christian-religion-v1-cover-vol-6.pdf`, `institutes-of-the-christian-religion-v1.1-institutes-vol-1-reader.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-1-compare.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-1-parallel.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-2-reader.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-2-compare.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-2-parallel.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-3-reader.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-3-compare.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-3-parallel.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-4-reader.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-4-compare.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-4-parallel.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-5-reader.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-5-compare.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-5-parallel.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-6-reader.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-6-compare.html`, `institutes-of-the-christian-religion-v1.1-institutes-vol-6-parallel.html`, `institutes-of-the-christian-religion-v1-cover-vol-1-back.webp`, `institutes-of-the-christian-religion-v1-cover-vol-1-spine.webp`, `institutes-of-the-christian-religion-v1-cover-vol-1-front.webp`, `institutes-of-the-christian-religion-v1-cover-vol-2-back.webp`, `institutes-of-the-christian-religion-v1-cover-vol-2-spine.webp`, `institutes-of-the-christian-religion-v1-cover-vol-2-front.webp`, `institutes-of-the-christian-religion-v1-cover-vol-3-back.webp`, `institutes-of-the-christian-religion-v1-cover-vol-3-spine.webp`, `institutes-of-the-christian-religion-v1-cover-vol-3-front.webp`, `institutes-of-the-christian-religion-v1-cover-vol-4-back.webp`, `institutes-of-the-christian-religion-v1-cover-vol-4-spine.webp`, `institutes-of-the-christian-religion-v1-cover-vol-4-front.webp`, `institutes-of-the-christian-religion-v1-cover-vol-5-back.webp`, `institutes-of-the-christian-religion-v1-cover-vol-5-spine.webp`, `institutes-of-the-christian-religion-v1-cover-vol-5-front.webp`, `institutes-of-the-christian-religion-v1-cover-vol-6-back.webp`, `institutes-of-the-christian-religion-v1-cover-vol-6-spine.webp`, `institutes-of-the-christian-religion-v1-cover-vol-6-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 691,660 printed words; 99.4% as printed
- changed in form only (spelling, case, punctuation): 3,499 words (0.5%)
- grammar modernized (hath -> has, thou -> you): 10 words (0.0%)
- changed in wording (emendations): 822 words (0.1%); 155 words added, 188 removed
- gaps in the transcription: none
- notes: 4 added by the editor, 35 printed notes left out

## Indwelling Sin

Owen's Indwelling Sin from the second edition (London, 1675), EEBO-TCP A53712, its gaps restored from the page and the transcription's slips corrected, with the first edition (1668) and Goold's text (1850-53) as witnesses.

- folder: `books/john-owen/indwelling-sin`
- version v3: tag `john-owen/indwelling-sin/v3`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 3 of this paperback
- source: EEBO-TCP A53712: John Owen, The Nature, Power, Deceit, and Prevalency of the Remainders of Indwelling-Sin in Believers (London: printed for Thomas Cockerill, 1675), the second edition, the last in Owen's lifetime: the text <https://github.com/textcreationpartnership/A53712>, `source/A53712.tcp.xml` (sha256 `87a10f8feec4f69d…`)
- source: The transcription's keying slips corrected to the 1675 page, each read on the page image (the TCP file untouched) <https://archive.org/details/bim_early-english-books-1641-1700_the-nature-power-decei_owen-john_1675>, `source/A53712.supplied.xml` (sha256 `2260217c597f9f24…`)
- source: CCEL ThML: John Owen, Indwelling Sin, from The Works of John Owen, ed. William H. Goold, vol. 6 (1850-53): a witness, and the guide to the outline levels <https://www.ccel.org/ccel/o/owen/indwellingsin.xml>, `source/indwellingsin.ccel.witness.xml` (sha256 `d96a21545e33e34e…`)
- witness: The 1675 printing (archive.org scan, EEBO microfilm), read with Kraken and Tesseract and collated with the TCP: the gaps restored (Greek and Hebrew from the page) and the keying slips <https://archive.org/details/bim_early-english-books-1641-1700_the-nature-power-decei_owen-john_1675>
- witness: The first edition (London: Elizabeth Calvert, 1668), read with Kraken and Tesseract: Owen's revisions checked (none of substance) and the 1675 printer's slips settled <https://archive.org/details/bim_early-english-books-1641-1700_the-nature-power-decei_owen-john_1668>
- files: `indwelling-sin-v3.pdf`, `indwelling-sin-v3-cover.pdf`, `indwelling-sin-v3-cover-front.png`, `indwelling-sin-v3-cover-front.png`, `indwelling-sin-v3.epub`, `indwelling-sin-v3-reader.html`, `indwelling-sin-v3-compare.html`, `indwelling-sin-v3-cover-back.webp`, `indwelling-sin-v3-cover-spine.webp`, `indwelling-sin-v3-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 88,925 printed words; 97.5% as printed
- changed in form only (spelling, case, punctuation): 1,662 words (1.9%)
- grammar modernized (hath -> has, thou -> you): 32 words (0.0%)
- changed in wording (emendations): 507 words (0.6%); 7 words added, 229 removed
- gaps in the transcription: 214, 214 restored, 0 left open

## Indwelling Sin (Modern English)

Owen's Indwelling Sin from the second edition (London, 1675), EEBO-TCP A53712, its gaps restored from the page and the transcription's slips corrected, with the first edition (1668) and Goold's text (1850-53) as witnesses.

- folder: `books/john-owen/indwelling-sin`
- version v1: tag `john-owen/indwelling-sin/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v3
- sign-off note: Based on: the Classic v3 (john-owen/indwelling-sin/v3).
- files: `indwelling-sin-v1-modern.pdf`, `indwelling-sin-v1-cover-modern.pdf`, `indwelling-sin-v1-cover-modern-front.png`, `indwelling-sin-v1-modern.epub`, `indwelling-sin-v1-modern-reader.html`, `indwelling-sin-v1-cover-modern-back.webp`, `indwelling-sin-v1-cover-modern-spine.webp`, `indwelling-sin-v1-cover-modern-front.webp`

## Of Temptation

Owen's Of Temptation from the first edition (Oxford, 1658), EEBO-TCP A90277, its printer's errata and the transcription's slips corrected, with Goold's text (1850-53) as the guide to modern wording.

- folder: `books/john-owen/of-temptation`
- version v3: tag `john-owen/of-temptation/v3`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 3 of this paperback
- source: EEBO-TCP A90277: John Owen, Of Temptation: the Nature and Power of It (Oxford: Leon. Lichfield for Tho. Robinson, 1658), the first edition: the text <https://github.com/textcreationpartnership/A90277>, `source/A90277.tcp.xml` (sha256 `9270022961e61afb…`)
- source: CCEL ThML: John Owen, Of Temptation, from The Works of John Owen, ed. William H. Goold, vol. 6 (1850-53), a witness and the modernization layer's guide: source/wording-decisions.md <https://www.ccel.org/ccel/o/owen/temptation.xml>, `source/temptation.ccel.witness.xml` (sha256 `6b5231f59965fe7b…`)
- witness: The 1721 printing (archive.org scan, EEBO microfilm), read with Kraken and Tesseract and collated with the TCP (work/of-temptation/collate-3m): the TCP's keying slips, source/errata.md <https://archive.org/details/bim_eighteenth-century_of-temptation-the-natur_owen-john_1721>
- witness: The Works of John Owen, ed. William H. Goold, vol. 6 (Johnstone and Hunter, 1850-53), the printing CCEL follows <https://archive.org/details/worksofjohnowe185006owen>
- files: `of-temptation-v3.pdf`, `of-temptation-v3-cover.pdf`, `of-temptation-v3-cover-front.png`, `of-temptation-v3-cover-front.png`, `of-temptation-v3.epub`, `of-temptation-v3-reader.html`, `of-temptation-v3-compare.html`, `of-temptation-v3-cover-back.webp`, `of-temptation-v3-cover-spine.webp`, `of-temptation-v3-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 33,135 printed words; 72.7% as printed
- changed in form only (spelling, case, punctuation): 7,926 words (23.9%)
- grammar modernized (hath -> has, thou -> you): 71 words (0.2%)
- changed in wording (emendations): 1,046 words (3.2%); 176 words added, 338 removed
- gaps in the transcription: 10, 10 restored, 0 left open
- notes: 0 added by the editor, 5 printed notes left out

## Of Temptation (Modern English)

Owen's Of Temptation from the first edition (Oxford, 1658), EEBO-TCP A90277, its printer's errata and the transcription's slips corrected, with Goold's text (1850-53) as the guide to modern wording.

- folder: `books/john-owen/of-temptation`
- version v1: tag `john-owen/of-temptation/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v3
- sign-off note: Based on: the Classic v3 (john-owen/of-temptation/v3).
- files: `of-temptation-v1-modern.pdf`, `of-temptation-v1-cover-modern.pdf`, `of-temptation-v1-cover-modern-front.png`, `of-temptation-v1-modern.epub`, `of-temptation-v1-modern-reader.html`, `of-temptation-v1-cover-modern-back.webp`, `of-temptation-v1-cover-modern-spine.webp`, `of-temptation-v1-cover-modern-front.webp`

## Owen on Sin

Owen's Of Temptation (1658) and The Mortification of Sin (1656) in one paperback, Of Temptation first: each is the text of its own edition here, unchanged, with its own ebook and record of every change.

- folder: `books/john-owen/owen-on-sin`
- version v2: tag `john-owen/owen-on-sin/v2`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of this paperback
- a print volume, made from: john-owen/of-temptation v3 (`john-owen/of-temptation/v3`), john-owen/the-mortification-of-sin v4 (`john-owen/the-mortification-of-sin/v4`)
- sign-off note: Made from: Of Temptation v3 (john-owen/of-temptation/v3); The Mortification of Sin v4 (john-owen/the-mortification-of-sin/v4).
- files: `owen-on-sin-v2.pdf`, `owen-on-sin-v2-cover.pdf`, `owen-on-sin-v2-cover-front.png`, `owen-on-sin-v2-cover-back.webp`, `owen-on-sin-v2-cover-spine.webp`, `owen-on-sin-v2-cover-front.webp`

## Owen on Sin (Modern English)

Owen's Of Temptation (1658) and The Mortification of Sin (1656) in one paperback in Modern English, Of Temptation first: each is the text of its own Modern English edition, unchanged.

- folder: `books/john-owen/owen-on-sin`
- version v1: tag `john-owen/owen-on-sin/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- a print volume, made from: john-owen/of-temptation v1 (`john-owen/of-temptation/modern/v1`), john-owen/the-mortification-of-sin v1 (`john-owen/the-mortification-of-sin/modern/v1`)
- sign-off note: Made from: Of Temptation (Modern English) v1 (john-owen/of-temptation/modern/v1); The Mortification of Sin (Modern English) v1 (john-owen/the-mortification-of-sin/modern/v1).
- files: `owen-on-sin-v1-modern.pdf`, `owen-on-sin-v1-cover-modern.pdf`, `owen-on-sin-v1-cover-modern-back.webp`, `owen-on-sin-v1-cover-modern-spine.webp`, `owen-on-sin-v1-cover-modern-front.webp`

## The Death of Death in the Death of Christ

Owen's Death of Death in the Death of Christ in William Goold's text, as CCEL gives it, with CCEL's slips corrected against Goold's printing and Owen's own wording, chiefly his quotations of Scripture, restored from the 1648 first edition.

- folder: `books/john-owen/the-death-of-death`
- version v2: tag `john-owen/the-death-of-death/v2`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of this paperback
- source: CCEL ThML: John Owen, The Death of Death in the Death of Christ (Goold's text, The Works of John Owen, vol. 10, 1850-53) <https://www.ccel.org/ccel/o/owen/deathofdeath.xml>, `source/deathofdeath.thml.xml` (sha256 `c76ae424be0caab0…`)
- witness: Salus Electorum, Sanguis Jesu: or, The Death of Death in the Death of Christ (London, 1648), the first edition, archive.org scan, read on the page images and by local OCR: source/collation/*.jsonl <https://archive.org/details/bim_early-english-books-1641-1700_salus-electorum-sanguis_owen-john_1648>
- witness: The Works of John Owen, ed. William H. Goold, vol. 10 (1850), archive.org scan and local OCR, the printing CCEL was keyed from: source/collation/goold-ccel.jsonl <https://archive.org/details/worksofjohnowend0000owen>
- files: `the-death-of-death-v2.pdf`, `the-death-of-death-v2-cover.pdf`, `the-death-of-death-v2-cover-front.png`, `the-death-of-death-v2-cover-front.png`, `the-death-of-death-v2.epub`, `the-death-of-death-v2-reader.html`, `the-death-of-death-v2-compare.html`, `the-death-of-death-v2-cover-back.webp`, `the-death-of-death-v2-cover-spine.webp`, `the-death-of-death-v2-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 191,818 printed words; 98.5% as printed
- changed in form only (spelling, case, punctuation): 1,893 words (1.0%)
- grammar modernized (hath -> has, thou -> you): 45 words (0.0%)
- changed in wording (emendations): 853 words (0.4%); 165 words added, 375 removed
- gaps in the transcription: none

## The Mortification of Sin

Owen's Of the Mortification of Sin in Believers from the second edition (London, 1668), the last in Owen's lifetime, EEBO-TCP A53715, its gaps restored from the page and the transcription's slips corrected, with Goold's text (1850-53) as a witness; and a Modern English edition of it.

- folder: `books/john-owen/the-mortification-of-sin`
- version v4: tag `john-owen/the-mortification-of-sin/v4`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 4 of this paperback
- source: EEBO-TCP A53715: John Owen, Of the Mortification of Sin in Believers (London: printed for Nathanael Ponder, 1668), the second edition: the text <https://github.com/textcreationpartnership/A53715>, `source/A53715.tcp.xml` (sha256 `4603d4fd73838e69…`)
- source: The transcription's keying slips corrected to the 1668 page, each read on the page image (the TCP file untouched) <https://archive.org/details/bim_early-english-books-1641-1700_of-the-mortification-of-_owen-john-dd_1668>, `source/A53715.supplied.xml` (sha256 `ecee4bd05ea2b304…`)
- source: CCEL ThML: John Owen, Of the Mortification of Sin in Believers, from The Works of John Owen, ed. William H. Goold, vol. 6 (1850-53): a witness, and the guide to the outline levels <https://www.ccel.org/ccel/o/owen/mort.xml>, `source/mort.ccel.witness.xml` (sha256 `e3577b8e81583250…`)
- witness: The 1668 printing (archive.org scan, EEBO microfilm), read with Kraken and Tesseract and collated with the TCP: the gaps restored (Greek from the page) and the keying slips <https://archive.org/details/bim_early-english-books-1641-1700_of-the-mortification-of-_owen-john-dd_1668>
- witness: The Works of John Owen, ed. William H. Goold, vol. 6 (Johnstone and Hunter, 1850-53), the edition's base until 2026-11-14: wording and references compared <https://archive.org/details/worksofjohnowe185006owen>
- files: `the-mortification-of-sin-v4.pdf`, `the-mortification-of-sin-v4-cover.pdf`, `the-mortification-of-sin-v4-cover-front.png`, `the-mortification-of-sin-v4-cover-front.png`, `the-mortification-of-sin-v4.epub`, `the-mortification-of-sin-v4-reader.html`, `the-mortification-of-sin-v4-compare.html`, `the-mortification-of-sin-v4-cover-back.webp`, `the-mortification-of-sin-v4-cover-spine.webp`, `the-mortification-of-sin-v4-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 43,857 printed words; 96.1% as printed
- changed in form only (spelling, case, punctuation): 1,309 words (3.0%)
- grammar modernized (hath -> has, thou -> you): 37 words (0.1%)
- changed in wording (emendations): 369 words (0.8%); 10 words added, 116 removed
- gaps in the transcription: 163, 163 restored, 0 left open

## The Mortification of Sin (Modern English)

Owen's Of the Mortification of Sin in Believers from the second edition (London, 1668), the last in Owen's lifetime, EEBO-TCP A53715, its gaps restored from the page and the transcription's slips corrected, with Goold's text (1850-53) as a witness; and a Modern English edition of it.

- folder: `books/john-owen/the-mortification-of-sin`
- version v1: tag `john-owen/the-mortification-of-sin/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v4
- sign-off note: Based on: the Classic v4 (john-owen/the-mortification-of-sin/v4).
- files: `the-mortification-of-sin-v1-modern.pdf`, `the-mortification-of-sin-v1-cover-modern.pdf`, `the-mortification-of-sin-v1-cover-modern-front.png`, `the-mortification-of-sin-v1-modern.epub`, `the-mortification-of-sin-v1-modern-reader.html`, `the-mortification-of-sin-v1-cover-modern-back.webp`, `the-mortification-of-sin-v1-cover-modern-spine.webp`, `the-mortification-of-sin-v1-cover-modern-front.webp`

## Religious Affections

Jonathan Edwards's A Treatise Concerning Religious Affections (Boston, 1746), in modern spelling from the Evans-TCP transcription of the first edition; illegible letters restored and transcription slips corrected from the 1746 page images, with the printed errata applied.

- folder: `books/jonathan-edwards/religious-affections`
- version v1: tag `jonathan-edwards/religious-affections/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.15.0
- print: Lulu revision 1 of this paperback
- source: Evans-TCP N04635: A Treatise Concerning Religious Affections, in Three Parts (Boston, S. Kneeland and T. Green, 1746; Evans 5767) <https://github.com/textcreationpartnership/N04635>, `source/N04635.tcp.xml` (sha256 `238dbbe338902d11…`)
- source: Corrections to the TCP transcription, read on the 1746 page images (dropped and misread words, f for s, among others) <https://archive.org/details/treatiseconcerni1746edwa>, `source/N04635.supplied.xml` (sha256 `2cfb23614e997a11…`)
- witness: The 1746 printing, Princeton Theological Seminary copy, archive.org scan: local OCR (Kraken and Tesseract) collated with the TCP; gaps, slips and the errata page read on its page images <https://archive.org/details/treatiseconcerni1746edwa>
- witness: The 1768 New York edition (J. Parker for G. Noel, set from 1746), archive.org scan, local OCR collated as a second reading <https://archive.org/details/treatiseconcerni00edwa>
- witness: CCEL's modern-spelling text (the Worcester line), a check on case and spelling only <https://www.ccel.org/ccel/edwards/affections.html>
- files: `religious-affections-v1.pdf`, `religious-affections-v1-cover.pdf`, `religious-affections-v1-cover-front.png`, `religious-affections-v1-cover-front.png`, `religious-affections-v1.epub`, `religious-affections-v1-reader.html`, `religious-affections-v1-compare.html`, `religious-affections-v1-cover-back.webp`, `religious-affections-v1-cover-spine.webp`, `religious-affections-v1-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 181,653 printed words; 79.7% as printed
- changed in form only (spelling, case, punctuation): 36,389 words (20.0%)
- grammar modernized (hath -> has, thou -> you): 20 words (0.0%)
- changed in wording (emendations): 429 words (0.2%); 16 words added, 30 removed
- gaps in the transcription: 1377, 1377 restored, 0 left open

## Religious Affections (Modern English)

Jonathan Edwards's A Treatise Concerning Religious Affections (Boston, 1746), in modern spelling from the Evans-TCP transcription of the first edition; illegible letters restored and transcription slips corrected from the 1746 page images, with the printed errata applied.

- folder: `books/jonathan-edwards/religious-affections`
- version v1: tag `jonathan-edwards/religious-affections/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.15.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v1
- sign-off note: Based on: the Classic v1 (jonathan-edwards/religious-affections/v1).
- files: `religious-affections-v1-modern.pdf`, `religious-affections-v1-cover-modern.pdf`, `religious-affections-v1-cover-modern-front.png`, `religious-affections-v1-modern.epub`, `religious-affections-v1-modern-reader.html`, `religious-affections-v1-cover-modern-back.webp`, `religious-affections-v1-cover-modern-spine.webp`, `religious-affections-v1-cover-modern-front.webp`

## Sinners in the Hands of an Angry God

Edwards's Enfield sermon (1741) from its second edition, in modern spelling, a small hand-out book quoting scripture from the Berean Standard Bible (two KJV quotations kept where Edwards builds on their words).

- folder: `books/jonathan-edwards/sinners-in-the-hands-of-an-angry-god`
- version v10: tag `jonathan-edwards/sinners-in-the-hands-of-an-angry-god/v10`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 10 of this paperback
- source: EEBO-TCP (Evans) N05520: Edwards, True Grace (New York, James Parker, 1753), with the second edition of Sinners in the Hands of an Angry God bound after it (pp. 43-62) <https://github.com/textcreationpartnership/N05520>, `source/N05520.tcp.xml` (sha256 `9600c9fdc53098be…`)
- witness: The Berean Standard Bible, for the scripture quotations: source/proofread-report.md <https://berean.bible/>
- files: `sinners-in-the-hands-of-an-angry-god-v10.pdf`, `sinners-in-the-hands-of-an-angry-god-v10-cover.pdf`, `sinners-in-the-hands-of-an-angry-god-v10-cover-front.png`, `sinners-in-the-hands-of-an-angry-god-v10-cover-front.png`, `sinners-in-the-hands-of-an-angry-god-v10.epub`, `sinners-in-the-hands-of-an-angry-god-v10-reader.html`, `sinners-in-the-hands-of-an-angry-god-v10-compare.html`, `sinners-in-the-hands-of-an-angry-god-v10-cover-back.webp`, `sinners-in-the-hands-of-an-angry-god-v10-cover-spine.webp`, `sinners-in-the-hands-of-an-angry-god-v10-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 23,249 printed words; 80.0% as printed
- changed in form only (spelling, case, punctuation): 4,075 words (17.5%)
- grammar modernized (hath -> has, thou -> you): 11 words (0.0%)
- changed in wording (emendations): 565 words (2.4%); 166 words added, 236 removed
- gaps in the transcription: 11, 7 restored, 4 left open

## Sinners in the Hands of an Angry God (Modern English)

Edwards's Enfield sermon (1741) from its second edition, in modern spelling, a small hand-out book quoting scripture from the Berean Standard Bible (two KJV quotations kept where Edwards builds on their words).

- folder: `books/jonathan-edwards/sinners-in-the-hands-of-an-angry-god`
- version v2: tag `jonathan-edwards/sinners-in-the-hands-of-an-angry-god/modern/v2`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v10
- sign-off note: Based on: the Classic v10 (jonathan-edwards/sinners-in-the-hands-of-an-angry-god/v10).
- files: `sinners-in-the-hands-of-an-angry-god-v2-modern.pdf`, `sinners-in-the-hands-of-an-angry-god-v2-cover-modern.pdf`, `sinners-in-the-hands-of-an-angry-god-v2-cover-modern-front.png`, `sinners-in-the-hands-of-an-angry-god-v2-modern.epub`, `sinners-in-the-hands-of-an-angry-god-v2-modern-reader.html`, `sinners-in-the-hands-of-an-angry-god-v2-cover-modern-back.webp`, `sinners-in-the-hands-of-an-angry-god-v2-cover-modern-spine.webp`, `sinners-in-the-hands-of-an-angry-god-v2-cover-modern-front.webp`

## The Glorious Feast of the Gospel

Sibbes's sermons on Isaiah 25:6-9 from the first edition (1650), in modern spelling; an earlier copy's misprints and dropped words corrected against the 1650 text, and its Greek and illegible places restored from the page images.

- folder: `books/richard-sibbes/the-glorious-feast-of-the-gospel`
- version v16: tag `richard-sibbes/the-glorious-feast-of-the-gospel/v16`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 16 of this paperback
- source: EEBO-TCP A93248: The Glorious Feast of the Gospel (London, John Rothwell, 1650) <https://github.com/textcreationpartnership/A93248>, `source/A93248.tcp.xml` (sha256 `d95173b14fc232a3…`)
- witness: Monergism's modernized text (from the SDG reprint; (c) Monergism Books 2017), a check only: source/witness-report.md <https://www.monergism.com/>
- witness: The earlier Freely Given Books copy (a Grosart-type text, 1862), corrected against 1650
- files: `the-glorious-feast-of-the-gospel-v16.pdf`, `the-glorious-feast-of-the-gospel-v16-cover.pdf`, `the-glorious-feast-of-the-gospel-v16-cover-front.png`, `the-glorious-feast-of-the-gospel-v16-cover-front.png`, `the-glorious-feast-of-the-gospel-v16.epub`, `the-glorious-feast-of-the-gospel-v16-reader.html`, `the-glorious-feast-of-the-gospel-v16-compare.html`, `the-glorious-feast-of-the-gospel-v16-cover-back.webp`, `the-glorious-feast-of-the-gospel-v16-cover-spine.webp`, `the-glorious-feast-of-the-gospel-v16-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 56,190 printed words; 74.4% as printed
- changed in form only (spelling, case, punctuation): 13,235 words (23.6%)
- grammar modernized (hath -> has, thou -> you): 53 words (0.1%)
- changed in wording (emendations): 1,121 words (2.0%); 822 words added, 356 removed
- gaps in the transcription: 12, 12 restored, 0 left open
- notes: 0 added by the editor, 385 printed notes left out

## The Glorious Feast of the Gospel (Modern English)

Sibbes's sermons on Isaiah 25:6-9 from the first edition (1650), in modern spelling; an earlier copy's misprints and dropped words corrected against the 1650 text, and its Greek and illegible places restored from the page images.

- folder: `books/richard-sibbes/the-glorious-feast-of-the-gospel`
- version v1: tag `richard-sibbes/the-glorious-feast-of-the-gospel/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v16
- sign-off note: Based on: the Classic v16 (richard-sibbes/the-glorious-feast-of-the-gospel/v16).
- files: `the-glorious-feast-of-the-gospel-v1-modern.pdf`, `the-glorious-feast-of-the-gospel-v1-cover-modern.pdf`, `the-glorious-feast-of-the-gospel-v1-cover-modern-front.png`, `the-glorious-feast-of-the-gospel-v1-modern.epub`, `the-glorious-feast-of-the-gospel-v1-modern-reader.html`, `the-glorious-feast-of-the-gospel-v1-cover-modern-back.webp`, `the-glorious-feast-of-the-gospel-v1-cover-modern-spine.webp`, `the-glorious-feast-of-the-gospel-v1-cover-modern-front.webp`

## The Crook in the Lot

Boston's The Crook in the Lot in full, from Samuel M'Millan's edition of his Whole Works (1848), transcribed for this edition from two scans and checked against the page images; M'Millan's few misprints corrected, the 1811 printing agreeing.

- folder: `books/thomas-boston/the-crook-in-the-lot`
- version v2: tag `thomas-boston/the-crook-in-the-lot/v2`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of this paperback
- source: Our transcription of The Whole Works of Thomas Boston, ed. Samuel M'Millan, vol. 3 (Aberdeen, 1848), pp. 495-590, as ThML: how it was made in source/SOURCES.md <https://archive.org/details/wholeworksoflate03bost>, `source/crook.thml.xml` (sha256 `570af79869826424…`)
- source: CCEL ThML: Thomas Boston, The Crook in the Lot, a modernized revision (Institute of Practical Bible Education etext, 2000), untouched; a witness only, used as a hint in the OCR correction <https://www.ccel.org/ccel/b/boston/crook.xml>, `source/crook.ccel.witness.xml` (sha256 `64cc81b01e511b78…`)
- witness: M'Millan's 1848 volume, the University of Michigan scan: its OCR the second reading in the transcription (source/SOURCES.md) <https://archive.org/details/wholeworkslater06bostgoog>
- witness: The Crook in the Lot, Philadelphia 1811, archive.org scan: M'Millan's misprints corrected where it agrees (source/proofread-report.md) <https://archive.org/details/crookinlotorsove01bost>
- witness: The Crook in the Lot, 1782 and London 1791 printings, archive.org scans, consulted in the transcription; no scan of the 1737 first edition was found <https://archive.org/details/bim_eighteenth-century_crook-in-the-lot-or-the_boston-thomas_1782>
- files: `the-crook-in-the-lot-v2.pdf`, `the-crook-in-the-lot-v2-cover.pdf`, `the-crook-in-the-lot-v2-cover-front.png`, `the-crook-in-the-lot-v2-cover-front.png`, `the-crook-in-the-lot-v2.epub`, `the-crook-in-the-lot-v2-reader.html`, `the-crook-in-the-lot-v2-compare.html`, `the-crook-in-the-lot-v2-cover-back.webp`, `the-crook-in-the-lot-v2-cover-spine.webp`, `the-crook-in-the-lot-v2-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 47,445 printed words; 97.4% as printed
- changed in form only (spelling, case, punctuation): 1,181 words (2.5%)
- grammar modernized (hath -> has, thou -> you): 1 words (0.0%)
- changed in wording (emendations): 65 words (0.1%); 11 words added, 11 removed
- gaps in the transcription: none

## The Crook in the Lot (Modern English)

Boston's The Crook in the Lot in full, from Samuel M'Millan's edition of his Whole Works (1848), transcribed for this edition from two scans and checked against the page images; M'Millan's few misprints corrected, the 1811 printing agreeing.

- folder: `books/thomas-boston/the-crook-in-the-lot`
- version v1: tag `thomas-boston/the-crook-in-the-lot/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v2
- sign-off note: Based on: the Classic v2 (thomas-boston/the-crook-in-the-lot/v2).
- files: `the-crook-in-the-lot-v1-modern.pdf`, `the-crook-in-the-lot-v1-cover-modern.pdf`, `the-crook-in-the-lot-v1-cover-modern-front.png`, `the-crook-in-the-lot-v1-modern.epub`, `the-crook-in-the-lot-v1-modern-reader.html`, `the-crook-in-the-lot-v1-cover-modern-back.webp`, `the-crook-in-the-lot-v1-cover-modern-spine.webp`, `the-crook-in-the-lot-v1-cover-modern-front.webp`

## Precious Remedies Against Satan’s Devices

Brooks's Precious Remedies Against Satan's Devices from the second edition (1653, corrected and enlarged), lightly modernized, its lost Greek and Hebrew restored from the 1652 and 1658 printings and the text proofread twice against Grosart's edition (1866).

- folder: `books/thomas-brooks/precious-remedies-against-satans-devices`
- version v3: tag `thomas-brooks/precious-remedies-against-satans-devices/v3`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 3 of this paperback
- source: EEBO-TCP A77614: Precious Remedies against Satans Devices (London, M. Simmons for John Hancock, 1653), the second edition <https://github.com/textcreationpartnership/A77614>, `source/A77614.tcp.xml` (sha256 `0d7babe825595733…`)
- witness: The Complete Works of Thomas Brooks, ed. A. B. Grosart (1866), vol. 1, archive.org scan and OCR: source/proofread-report.md <https://archive.org/details/completeworksoft01broouoft>
- witness: Precious Remedies (1652), the first edition, archive.org scan of the EEBO microfilm: the Greek and Hebrew the TCP left out, source/gap_fixes.py <https://archive.org/details/bim_early-english-books-1641-1700_precious-remedies_brookes-thomas_1652>
- witness: Precious Remedies (1658), archive.org scan of the EEBO microfilm: gaps, source/gap_fixes.py <https://archive.org/details/bim_early-english-books-1641-1700_precious-remedies-_brookes-thomas_1658>
- witness: Monergism's keyed text of Grosart's edition, compared only
- files: `precious-remedies-against-satans-devices-v3.pdf`, `precious-remedies-against-satans-devices-v3-cover.pdf`, `precious-remedies-against-satans-devices-v3-cover-front.png`, `precious-remedies-against-satans-devices-v3-cover-front.png`, `precious-remedies-against-satans-devices-v3.epub`, `precious-remedies-against-satans-devices-v3-reader.html`, `precious-remedies-against-satans-devices-v3-compare.html`, `precious-remedies-against-satans-devices-v3-cover-back.webp`, `precious-remedies-against-satans-devices-v3-cover-spine.webp`, `precious-remedies-against-satans-devices-v3-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 102,836 printed words; 76.5% as printed
- changed in form only (spelling, case, punctuation): 23,459 words (22.8%)
- grammar modernized (hath -> has, thou -> you): 29 words (0.0%)
- changed in wording (emendations): 693 words (0.7%); 336 words added, 456 removed
- gaps in the transcription: 438, 438 restored, 0 left open
- notes: 0 added by the editor, 222 printed notes left out

## Precious Remedies Against Satan’s Devices (Modern English)

Brooks's Precious Remedies Against Satan's Devices from the second edition (1653, corrected and enlarged), lightly modernized, its lost Greek and Hebrew restored from the 1652 and 1658 printings and the text proofread twice against Grosart's edition (1866).

- folder: `books/thomas-brooks/precious-remedies-against-satans-devices`
- version v1: tag `thomas-brooks/precious-remedies-against-satans-devices/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v3
- sign-off note: Based on: the Classic v3 (thomas-brooks/precious-remedies-against-satans-devices/v3).
- files: `precious-remedies-against-satans-devices-v1-modern.pdf`, `precious-remedies-against-satans-devices-v1-cover-modern.pdf`, `precious-remedies-against-satans-devices-v1-cover-modern-front.png`, `precious-remedies-against-satans-devices-v1-modern.epub`, `precious-remedies-against-satans-devices-v1-modern-reader.html`, `precious-remedies-against-satans-devices-v1-cover-modern-back.webp`, `precious-remedies-against-satans-devices-v1-cover-modern-spine.webp`, `precious-remedies-against-satans-devices-v1-cover-modern-front.webp`

## The Secret Key of Heaven

Brooks's The Privie Key of Heaven (1665) in modern spelling, from an earlier copy corrected against the 1665 printing; its dropped clauses, Latin, Greek and Hebrew restored from the page images.

- folder: `books/thomas-brooks/the-secret-key-of-heaven`
- version v9: tag `thomas-brooks/the-secret-key-of-heaven/v9`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 9 of this paperback
- source: EEBO-TCP A29703: The Privie Key of Heaven (London, John Hancock, 1665) <https://github.com/textcreationpartnership/A29703>, `source/A29703.tcp.xml` (sha256 `b6742bf2f0d59f51…`)
- witness: Chapel Library's edition (Private Key to Heaven, EPUB, text in the public domain), which the earlier copy followed: source/proofread-report.md <https://www.chapellibrary.org/>
- witness: The 1665 printing's page images (archive.org), for the Greek, Hebrew and illegible places <https://archive.org/details/bim_early-english-books-1641-1700_the-privie-key-of-heaven_brookes-thomas_1665>
- witness: The earlier Freely Given Books copy (lightly modernized), folded in as the review
- files: `the-secret-key-of-heaven-v9.pdf`, `the-secret-key-of-heaven-v9-cover.pdf`, `the-secret-key-of-heaven-v9-cover-front.png`, `the-secret-key-of-heaven-v9-cover-front.png`, `the-secret-key-of-heaven-v9.epub`, `the-secret-key-of-heaven-v9-reader.html`, `the-secret-key-of-heaven-v9-compare.html`, `the-secret-key-of-heaven-v9-cover-back.webp`, `the-secret-key-of-heaven-v9-cover-spine.webp`, `the-secret-key-of-heaven-v9-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 102,975 printed words; 75.2% as printed
- changed in form only (spelling, case, punctuation): 20,934 words (20.3%)
- grammar modernized (hath -> has, thou -> you): 76 words (0.1%)
- changed in wording (emendations): 4,569 words (4.4%); 2,521 words added, 2,027 removed
- gaps in the transcription: 72, 66 restored, 6 left open
- notes: 0 added by the editor, 403 printed notes left out

## The Secret Key of Heaven (Modern English)

Brooks's The Privie Key of Heaven (1665) in modern spelling, from an earlier copy corrected against the 1665 printing; its dropped clauses, Latin, Greek and Hebrew restored from the page images.

- folder: `books/thomas-brooks/the-secret-key-of-heaven`
- version v1: tag `thomas-brooks/the-secret-key-of-heaven/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v9
- sign-off note: Based on: the Classic v9 (thomas-brooks/the-secret-key-of-heaven/v9).
- files: `the-secret-key-of-heaven-v1-modern.pdf`, `the-secret-key-of-heaven-v1-cover-modern.pdf`, `the-secret-key-of-heaven-v1-cover-modern-front.png`, `the-secret-key-of-heaven-v1-modern.epub`, `the-secret-key-of-heaven-v1-modern-reader.html`, `the-secret-key-of-heaven-v1-cover-modern-back.webp`, `the-secret-key-of-heaven-v1-cover-modern-spine.webp`, `the-secret-key-of-heaven-v1-cover-modern-front.webp`

## The Surest and Safest Way of Thriving

Thomas Gouge's The Surest and Safest Way of Thriving (1673), on giving to the poor and to ministers, in modern spelling from the EEBO-TCP transcription of the first edition; its Greek restored from the 1676 printing.

- folder: `books/thomas-gouge/the-surest-way-of-thriving`
- version v2: tag `thomas-gouge/the-surest-way-of-thriving/v2`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.15.0
- print: Lulu revision 2 of this paperback
- source: EEBO-TCP A41657: The Surest & Safest Way of Thriving, or, A Conviction of That Grand Mistake in Many, That What Is Given to the Poor Is a Loss to Their Estate (London, for William Rawlins, 1673) <https://github.com/textcreationpartnership/A41657>, `source/A41657.tcp.xml` (sha256 `8e82bc0f604502a0…`)
- witness: The 1676 printing (London, Nevil Simmons), archive.org scan: the Greek the TCP left out, the stops it could not read, and the print's numbering, read on its page images; local OCR collated with the TCP <https://archive.org/details/bim_early-english-books-1641-1700_the-surest-safest-way-_gouge-thomas_1676>
- files: `the-surest-way-of-thriving-v2.pdf`, `the-surest-way-of-thriving-v2-cover.pdf`, `the-surest-way-of-thriving-v2-cover-front.png`, `the-surest-way-of-thriving-v2-cover-front.png`, `the-surest-way-of-thriving-v2.epub`, `the-surest-way-of-thriving-v2-reader.html`, `the-surest-way-of-thriving-v2-compare.html`, `the-surest-way-of-thriving-v2-cover-back.webp`, `the-surest-way-of-thriving-v2-cover-spine.webp`, `the-surest-way-of-thriving-v2-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 30,283 printed words; 93.1% as printed
- changed in form only (spelling, case, punctuation): 1,890 words (6.2%)
- grammar modernized (hath -> has, thou -> you): 13 words (0.0%)
- changed in wording (emendations): 180 words (0.6%); 20 words added, 81 removed
- gaps in the transcription: 23, 23 restored, 0 left open
- notes: 1 added by the editor, 0 printed notes left out

## The Surest and Safest Way of Thriving (Modern English)

Thomas Gouge's The Surest and Safest Way of Thriving (1673), on giving to the poor and to ministers, in modern spelling from the EEBO-TCP transcription of the first edition; its Greek restored from the 1676 printing.

- folder: `books/thomas-gouge/the-surest-way-of-thriving`
- version v2: tag `thomas-gouge/the-surest-way-of-thriving/modern/v2`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.15.0
- print: Lulu revision 2 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v2
- sign-off note: Based on: the Classic v2 (thomas-gouge/the-surest-way-of-thriving/v2).
- files: `the-surest-way-of-thriving-v2-modern.pdf`, `the-surest-way-of-thriving-v2-cover-modern.pdf`, `the-surest-way-of-thriving-v2-cover-modern-front.png`, `the-surest-way-of-thriving-v2-modern.epub`, `the-surest-way-of-thriving-v2-modern-reader.html`, `the-surest-way-of-thriving-v2-cover-modern-back.webp`, `the-surest-way-of-thriving-v2-cover-modern-spine.webp`, `the-surest-way-of-thriving-v2-cover-modern-front.webp`

## A Divine Cordial

Thomas Watson's A Divine Cordial (1663), in modern spelling from the EEBO-TCP transcription of the first edition; Greek, Hebrew and illegible letters restored, and transcription slips corrected, from the 1663 page images, with the 1678 edition where the 1663 film is lost.

- folder: `books/thomas-watson/a-divine-cordial`
- version v3: tag `thomas-watson/a-divine-cordial/v3`, signed off 2026-11-18 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 3 of this paperback
- source: EEBO-TCP A65292: A Divine Cordial, or, The Transcendent Priviledge of Those That Love God and Are Savingly Called (London, for Thomas Parkhurst, 1663) <https://github.com/textcreationpartnership/A65292>, `source/A65292.tcp.xml` (sha256 `b696a71fc48ffedf…`)
- source: Corrections to the TCP transcription from the 1663 page images ("out" for "our", "dejected", Latin misprints in the TCP, among others) <https://archive.org/details/bim_early-english-books-1641-1700_a-divine-cordial-_watson-thomas_1663>, `source/A65292.supplied.xml` (sha256 `1a83a00f4688d4a9…`)
- source: CCEL's text of A Divine Cordial, a reworded later modernization, kept as a check only <https://www.ccel.org/ccel/w/watson/cordial.xml>, `source/cordial.ccel.witness.xml` (sha256 `7b27f46b7deee948…`)
- witness: The 1663 printing, archive.org scan (the copy TCP was keyed from), local OCR (Kraken and Tesseract) collated with the TCP; gaps, Greek and Hebrew, and the proofread's questions read on its page images <https://archive.org/details/bim_early-english-books-1641-1700_a-divine-cordial-_watson-thomas_1663>
- witness: The 1678 edition, archive.org scan: letters and Greek the 1663 film lost (the Chrysostom note on p. 161) <https://archive.org/details/bim_early-english-books-1641-1700_a-divine-cordial-_watson-thomas-d-1689_1678>
- files: `a-divine-cordial-v3.pdf`, `a-divine-cordial-v3-cover.pdf`, `a-divine-cordial-v3-cover-front.png`, `a-divine-cordial-v3-cover-front.png`, `a-divine-cordial-v3.epub`, `a-divine-cordial-v3-reader.html`, `a-divine-cordial-v3-compare.html`, `a-divine-cordial-v3-cover-back.webp`, `a-divine-cordial-v3-cover-spine.webp`, `a-divine-cordial-v3-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 44,881 printed words; 96.0% as printed
- changed in form only (spelling, case, punctuation): 1,538 words (3.4%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 249 words (0.6%); 14 words added, 170 removed
- gaps in the transcription: 561, 561 restored, 0 left open
- notes: 0 added by the editor, 20 printed notes left out

## A Divine Cordial (Modern English)

Thomas Watson's A Divine Cordial (1663), in modern spelling from the EEBO-TCP transcription of the first edition; Greek, Hebrew and illegible letters restored, and transcription slips corrected, from the 1663 page images, with the 1678 edition where the 1663 film is lost.

- folder: `books/thomas-watson/a-divine-cordial`
- version v2: tag `thomas-watson/a-divine-cordial/modern/v2`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 2 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v3
- sign-off note: Based on: the Classic v3 (thomas-watson/a-divine-cordial/v3).
- files: `a-divine-cordial-v2-modern.pdf`, `a-divine-cordial-v2-cover-modern.pdf`, `a-divine-cordial-v2-cover-modern-front.png`, `a-divine-cordial-v2-modern.epub`, `a-divine-cordial-v2-modern-reader.html`, `a-divine-cordial-v2-cover-modern-back.webp`, `a-divine-cordial-v2-cover-modern-spine.webp`, `a-divine-cordial-v2-cover-modern-front.webp`

## Of Domestical Duties

Gouge's Of Domesticall Duties (1622), all eight treatises in four volumes, in modern spelling with his wording kept; the transcription corrected against the 1622 page images, its Greek and Hebrew restored, six missing pages supplied from a second 1622 copy, and the printer's errata applied.

- folder: `books/william-gouge/domestical-duties`
- version v4: tag `william-gouge/domestical-duties/v4`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.15.0
- print: Lulu revision 4 of this paperback
- source: EEBO-TCP A68107: Of Domesticall Duties, Eight Treatises (London, John Haviland for William Bladen, 1622) <https://github.com/textcreationpartnership/A68107>, `source/A68107.tcp.xml` (sha256 `d7404af2ca63812e…`)
- source: Pages 191-196 of the 1622 edition, missing from the copy the TCP transcribed, transcribed from a second 1622 copy (archive.org, n220-n225); and the places where the TCP misreads the print, corrected from the page images <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties_gouge-william_1622>, `source/A68107.supplied.xml` (sha256 `e7541ceaa9342c27…`)
- witness: The 1622 page images of the copy the TCP was made from (archive.org), for the Greek and Hebrew, illegible letters and the proofread: source/proofread-report.md <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622>
- witness: The second edition (1626, in The Workes of William Gouge), consulted for single readings <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-_gouge-william_1626>
- witness: The third edition (1634), consulted for single readings and the errata <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-_gouge-william_1634>
- witness: The earlier Freely Given Books edition (made with the converter before the TEI): source/migration-differences.md
- files: `domestical-duties-v4-vol-1.pdf`, `domestical-duties-v4-vol-2.pdf`, `domestical-duties-v4-vol-3.pdf`, `domestical-duties-v4-vol-4.pdf`, `domestical-duties-v4-cover-vol-1.pdf`, `domestical-duties-v4-cover-vol-2.pdf`, `domestical-duties-v4-cover-vol-3.pdf`, `domestical-duties-v4-cover-vol-4.pdf`, `domestical-duties-v4-cover-vol-1-front.png`, `domestical-duties-v4-cover-vol-2-front.png`, `domestical-duties-v4-cover-vol-3-front.png`, `domestical-duties-v4-cover-vol-4-front.png`, `domestical-duties-v4-cover-vol-1-front.png`, `domestical-duties-v4-vol-1.epub`, `domestical-duties-v4-cover-vol-2-front.png`, `domestical-duties-v4-vol-2.epub`, `domestical-duties-v4-cover-vol-3-front.png`, `domestical-duties-v4-vol-3.epub`, `domestical-duties-v4-cover-vol-4-front.png`, `domestical-duties-v4-vol-4.epub`, `domestical-duties-v4-vol-1-reader.html`, `domestical-duties-v4-vol-1-compare.html`, `domestical-duties-v4-vol-2-reader.html`, `domestical-duties-v4-vol-2-compare.html`, `domestical-duties-v4-vol-3-reader.html`, `domestical-duties-v4-vol-3-compare.html`, `domestical-duties-v4-vol-4-reader.html`, `domestical-duties-v4-vol-4-compare.html`, `domestical-duties-v4-cover-vol-1-back.webp`, `domestical-duties-v4-cover-vol-1-spine.webp`, `domestical-duties-v4-cover-vol-1-front.webp`, `domestical-duties-v4-cover-vol-2-back.webp`, `domestical-duties-v4-cover-vol-2-spine.webp`, `domestical-duties-v4-cover-vol-2-front.webp`, `domestical-duties-v4-cover-vol-3-back.webp`, `domestical-duties-v4-cover-vol-3-spine.webp`, `domestical-duties-v4-cover-vol-3-front.webp`, `domestical-duties-v4-cover-vol-4-back.webp`, `domestical-duties-v4-cover-vol-4-spine.webp`, `domestical-duties-v4-cover-vol-4-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 290,438 printed words; 74.2% as printed
- changed in form only (spelling, case, punctuation): 73,654 words (25.4%)
- grammar modernized (hath -> has, thou -> you): 155 words (0.1%)
- changed in wording (emendations): 1,256 words (0.4%); 476 words added, 884 removed
- gaps in the transcription: 717, 717 restored, 0 left open
- notes: 8 added by the editor, 6 printed notes left out

## Of Domestical Duties (Modern English)

Gouge's Of Domesticall Duties (1622), all eight treatises in four volumes, in modern spelling with his wording kept; the transcription corrected against the 1622 page images, its Greek and Hebrew restored, six missing pages supplied from a second 1622 copy, and the printer's errata applied.

- folder: `books/william-gouge/domestical-duties`
- version v1: tag `william-gouge/domestical-duties/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.15.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v4
- sign-off note: Based on: the Classic v4 (william-gouge/domestical-duties/v4).
- files: `domestical-duties-v1-vol-1-modern.pdf`, `domestical-duties-v1-vol-2-modern.pdf`, `domestical-duties-v1-vol-3-modern.pdf`, `domestical-duties-v1-vol-4-modern.pdf`, `domestical-duties-v1-cover-vol-1-modern.pdf`, `domestical-duties-v1-cover-vol-2-modern.pdf`, `domestical-duties-v1-cover-vol-3-modern.pdf`, `domestical-duties-v1-cover-vol-4-modern.pdf`, `domestical-duties-v1-cover-vol-1-modern-front.png`, `domestical-duties-v1-vol-1-modern.epub`, `domestical-duties-v1-cover-vol-2-modern-front.png`, `domestical-duties-v1-vol-2-modern.epub`, `domestical-duties-v1-cover-vol-3-modern-front.png`, `domestical-duties-v1-vol-3-modern.epub`, `domestical-duties-v1-cover-vol-4-modern-front.png`, `domestical-duties-v1-vol-4-modern.epub`, `domestical-duties-v1-vol-1-modern-reader.html`, `domestical-duties-v1-vol-2-modern-reader.html`, `domestical-duties-v1-vol-3-modern-reader.html`, `domestical-duties-v1-vol-4-modern-reader.html`, `domestical-duties-v1-cover-vol-1-modern-back.webp`, `domestical-duties-v1-cover-vol-1-modern-spine.webp`, `domestical-duties-v1-cover-vol-1-modern-front.webp`, `domestical-duties-v1-cover-vol-2-modern-back.webp`, `domestical-duties-v1-cover-vol-2-modern-spine.webp`, `domestical-duties-v1-cover-vol-2-modern-front.webp`, `domestical-duties-v1-cover-vol-3-modern-back.webp`, `domestical-duties-v1-cover-vol-3-modern-spine.webp`, `domestical-duties-v1-cover-vol-3-modern-front.webp`, `domestical-duties-v1-cover-vol-4-modern-back.webp`, `domestical-duties-v1-cover-vol-4-modern-spine.webp`, `domestical-duties-v1-cover-vol-4-modern-front.webp`

## Christian Economy

Perkins's Christian Oeconomie (1609), translated from the Latin by Thomas Pickering, in modern spelling from the EEBO-TCP transcription; footnotes kept in the original spelling; readings corrected and words the transcription left out restored from the 1609 page images.

- folder: `books/william-perkins/christian-economy`
- version v5: tag `william-perkins/christian-economy/v5`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 5 of this paperback
- source: EEBO-TCP A09377: Christian Oeconomie, or, A Short Survey of the Right Manner of Erecting and Ordering a Family (London, Felix Kyngston for Edmund Weaver, 1609), translated by Thomas Pickering <https://github.com/textcreationpartnership/A09377>, `source/A09377.tcp.xml` (sha256 `83d0f693c303aed4…`)
- source: Corrections to the TCP transcription from the 1609 page images: "Lombard," and "though" restored where it left them out; "or", "continencie", "his", "then", "the" and "bought" where it misread them <https://archive.org/details/bim_early-english-books-1475-1640_christian-oeconomie-or-_perkins-william_1609_0>, `source/A09377.supplied.xml` (sha256 `a43617693cab8cfe…`)
- witness: The 1609 printing, archive.org scan (the copy TCP was keyed from), local OCR (GLM-OCR and Tesseract) in source/ocr/: two readings corrected ("his wife", "he forbiddeth"); the page images also settled the proofread's questions (source/proofread-report.md) <https://archive.org/details/bim_early-english-books-1475-1640_christian-oeconomie-or-_perkins-william_1609_0>
- files: `christian-economy-v5.pdf`, `christian-economy-v5-cover.pdf`, `christian-economy-v5-cover-front.png`, `christian-economy-v5-cover-front.png`, `christian-economy-v5.epub`, `christian-economy-v5-reader.html`, `christian-economy-v5-compare.html`, `christian-economy-v5-cover-back.webp`, `christian-economy-v5-cover-spine.webp`, `christian-economy-v5-cover-front.webp`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 35,568 printed words; 82.9% as printed
- changed in form only (spelling, case, punctuation): 5,951 words (16.7%)
- grammar modernized (hath -> has, thou -> you): 10 words (0.0%)
- changed in wording (emendations): 113 words (0.3%); 49 words added, 48 removed
- gaps in the transcription: 39, 39 restored, 0 left open
- notes: 0 added by the editor, 1 printed notes left out

## Christian Economy (Modern English)

Perkins's Christian Oeconomie (1609), translated from the Latin by Thomas Pickering, in modern spelling from the EEBO-TCP transcription; footnotes kept in the original spelling; readings corrected and words the transcription left out restored from the 1609 page images.

- folder: `books/william-perkins/christian-economy`
- version v1: tag `william-perkins/christian-economy/modern/v1`, signed off 2026-11-22 by Courtney
- template: fgbooks 0.14.0
- print: Lulu revision 1 of the Modern English paperback, a Lulu book of its own
- its text follows the Classic v5
- sign-off note: Based on: the Classic v5 (william-perkins/christian-economy/v5).
- files: `christian-economy-v1-modern.pdf`, `christian-economy-v1-cover-modern.pdf`, `christian-economy-v1-cover-modern-front.png`, `christian-economy-v1-modern.epub`, `christian-economy-v1-modern-reader.html`, `christian-economy-v1-cover-modern-back.webp`, `christian-economy-v1-cover-modern-spine.webp`, `christian-economy-v1-cover-modern-front.webp`
