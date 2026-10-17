# Freely Given Books: release 2026.10.17.2

Get it: `git clone --recursive -b stable https://github.com/freely-given-books/books.git`, then `./fgb build`.

Every book here has been signed off by the editor: a signed tag
`<author>/<book>/vN` on the commit it was checked at, and the book's
folder is exactly as it was signed off. Each book was checked again for
this release: its sources match the checksums in its `RELEASE.toml`, the
TEI rebuilds as committed (verify.py), every review edit is applied, the
print PDFs keep Lulu's rules and the EPUBs pass epubcheck.

Check a sign-off yourself:

```sh
git -c gpg.ssh.allowedSignersFile=allowed_signers tag -v <author>/<book>/vN
git diff --stat <author>/<book>/vN stable -- books/<author>/<book>   # nothing
sha256sum -c SHA256SUMS                                         # the downloads
```

Built with colophon 0.20.0.

| Book | Author | Version | Signed off |
| --- | --- | --- | --- |
| [The Anatomy of Simon Magus](#the-anatomy-of-simon-magus) | Anonymous | v6.1 (between Lulu revisions) | 2026-10-17 |
| [All of Grace](#all-of-grace) | Charles Spurgeon | v15.1 (between Lulu revisions) | 2026-10-17 |
| [The Pilgrim's Progress](#the-pilgrims-progress) | John Bunyan | v13.1 (between Lulu revisions) | 2026-10-17 |
| [Sinners in the Hands of an Angry God](#sinners-in-the-hands-of-an-angry-god) | Jonathan Edwards | v8.1 (between Lulu revisions) | 2026-10-17 |
| [The Glorious Feast of the Gospel](#the-glorious-feast-of-the-gospel) | Richard Sibbes | v13.1 (between Lulu revisions) | 2026-10-17 |
| [The Secret Key of Heaven](#the-secret-key-of-heaven) | Thomas Brooks | v6.1 (between Lulu revisions) | 2026-10-17 |
| [Of Domestical Duties](#of-domestical-duties) | William Gouge | v1 | 2026-10-17 |

## The Anatomy of Simon Magus

The 1700 printing in modern spelling and grammar, with translations of the Latin, a foreword and an abbreviations guide; two slips of the author's corrected (Jehu the Seer, Apollos).

- folder: `books/anonymous/the-anatomy-of-simon-magus`
- version v6.1: tag `anonymous/the-anatomy-of-simon-magus/v6.1`, signed off 2026-10-17 by Courtney Hicks
- template: fgbooks 0.12.0
- a point version: an improved edition after Lulu revision 6 (the sign-off note says whether its print is still that revision's)
- sign-off note: Print: changed since v6 (the-anatomy-of-simon-magus.pdf: 2 page(s) differ: 17, 62); not a Lulu revision.
- source: EEBO-TCP A25330: The Anatomy of Simon Magus, or, The Sin of Simony Laid Open (London, Charles Brome, 1700) <https://github.com/textcreationpartnership/A25330>, `source/A25330.tcp.xml` (sha256 `3a437401c8512841…`)
- files: `the-anatomy-of-simon-magus-v6.1.pdf`, `the-anatomy-of-simon-magus-v6.1.epub`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 30,558 printed words; 68.8% as printed
- changed in form only (spelling, case, punctuation): 8,731 words (28.6%)
- grammar modernized (hath -> has, thou -> you): 404 words (1.3%)
- changed in wording (emendations): 396 words (1.3%); 42 words added, 92 removed
- gaps in the transcription: 11, 11 restored, 0 left open
- notes: 4 added by the editor, 1 printed notes left out

## All of Grace

Spurgeon's All of Grace (1886) as CCEL gives it, with clear CCEL errors fixed.

- folder: `books/charles-spurgeon/all-of-grace`
- version v15.1: tag `charles-spurgeon/all-of-grace/v15.1`, signed off 2026-10-17 by Courtney Hicks
- template: fgbooks 0.12.0
- a point version: an improved edition after Lulu revision 15 (the sign-off note says whether its print is still that revision's)
- sign-off note: Print: the same as v15, page for page (Lulu revision 15).
- source: CCEL ThML: C. H. Spurgeon, All of Grace (1886) <https://www.ccel.org/ccel/s/spurgeon/grace.xml>, `source/grace.thml.xml` (sha256 `7980c795972bb279…`)
- witness: Monergism's PDF (2015), which follows CCEL's text: source/proofread-report.md <https://www.monergism.com/>
- files: `all-of-grace-v15.1.pdf`, `all-of-grace-v15.1.epub`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 34,491 printed words; 99.4% as printed
- changed in form only (spelling, case, punctuation): 209 words (0.6%)
- grammar modernized (hath -> has, thou -> you): 1 words (0.0%)
- changed in wording (emendations): 8 words (0.0%); 1 words added, 1 removed
- gaps in the transcription: none

## The Pilgrim's Progress

Bunyan's Pilgrim's Progress, both parts, as CCEL gives it (Logos's text of the 1853 Auburn edition), with CCEL's slips and lost words corrected against the first edition of Part I (1678) and a 1732 printing of Part II.

- folder: `books/john-bunyan/the-pilgrims-progress`
- version v13.1: tag `john-bunyan/the-pilgrims-progress/v13.1`, signed off 2026-10-17 by Courtney Hicks
- template: fgbooks 0.12.0
- a point version: an improved edition after Lulu revision 13 (the sign-off note says whether its print is still that revision's)
- sign-off note: Print: changed since v13 (the-pilgrims-progress.pdf: 1 page(s) differ: 99); not a Lulu revision.
- source: CCEL ThML: John Bunyan, The Pilgrim's Progress, Parts I and II (Logos's text of the 1853 Auburn edition) <https://www.ccel.org/ccel/b/bunyan/pilgrim.xml>, `source/pilgrim.thml.xml` (sha256 `1ebdfd4db68990f3…`)
- source: EEBO-TCP A30170: The Pilgrim's Progress (London, Nath. Ponder, 1678), the first edition of Part I, a witness: source/witness-report.md <https://github.com/textcreationpartnership/A30170>, `source/A30170.witness.xml` (sha256 `14c3c96cab3e5a57…`)
- witness: The Pilgrim's Progress, Part II (London, 1732), archive.org scan, checked for Part II: source/proofread-report.md <https://archive.org/details/bim_eighteenth-century_the-pilgrims-progress-_bunyan-john_1732>
- witness: biblebb.com's Pilgrim's Progress Part 2, a modern copy, compared only
- files: `the-pilgrims-progress-v13.1.pdf`, `the-pilgrims-progress-v13.1-cover.pdf`, `the-pilgrims-progress-v13.1-cover-front.png`, `the-pilgrims-progress-v13.1-cover-front.png`, `the-pilgrims-progress-v13.1.epub`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 110,974 printed words; 99.9% as printed
- changed in form only (spelling, case, punctuation): 87 words (0.1%)
- grammar modernized (hath -> has, thou -> you): 0 words (0.0%)
- changed in wording (emendations): 58 words (0.1%); 20 words added, 11 removed
- gaps in the transcription: none

## Sinners in the Hands of an Angry God

Edwards's Enfield sermon (1741) from its second edition, in modern spelling, a small hand-out book quoting scripture from the Berean Standard Bible (two KJV quotations kept where Edwards builds on their words).

- folder: `books/jonathan-edwards/sinners-in-the-hands-of-an-angry-god`
- version v8.1: tag `jonathan-edwards/sinners-in-the-hands-of-an-angry-god/v8.1`, signed off 2026-10-17 by Courtney Hicks
- template: fgbooks 0.12.0
- a point version: an improved edition after Lulu revision 8 (the sign-off note says whether its print is still that revision's)
- sign-off note: Print: changed since v8 (sinners-in-the-hands-of-an-angry-god.pdf: 10 page(s) differ: 7, 17, 19, 26, 33, 34, 35, 36, 37, 38); not a Lulu revision.
- source: EEBO-TCP (Evans) N05520: Edwards, True Grace (New York, James Parker, 1753), with the second edition of Sinners in the Hands of an Angry God bound after it (pp. 43-62) <https://github.com/textcreationpartnership/N05520>, `source/N05520.tcp.xml` (sha256 `9600c9fdc53098be…`)
- witness: The Berean Standard Bible, for the scripture quotations: source/proofread-report.md <https://berean.bible/>
- files: `sinners-in-the-hands-of-an-angry-god-v8.1.pdf`, `sinners-in-the-hands-of-an-angry-god-v8.1.epub`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 23,249 printed words; 80.0% as printed
- changed in form only (spelling, case, punctuation): 4,059 words (17.5%)
- grammar modernized (hath -> has, thou -> you): 11 words (0.0%)
- changed in wording (emendations): 586 words (2.5%); 166 words added, 241 removed
- gaps in the transcription: 11, 7 restored, 4 left open

## The Glorious Feast of the Gospel

Sibbes's sermons on Isaiah 25:6-9 from the first edition (1650), in modern spelling; an earlier copy's misprints and dropped words corrected against the 1650 text, and its Greek and illegible places restored from the page images.

- folder: `books/richard-sibbes/the-glorious-feast-of-the-gospel`
- version v13.1: tag `richard-sibbes/the-glorious-feast-of-the-gospel/v13.1`, signed off 2026-10-17 by Courtney Hicks
- template: fgbooks 0.12.0
- a point version: an improved edition after Lulu revision 13 (the sign-off note says whether its print is still that revision's)
- sign-off note: Print: changed since v13 (the-glorious-feast-of-the-gospel.pdf: 26 page(s) differ: 11, 13, 28, 31, 51, 58, 65, 66, 67, 68, 69, 70 ...); not a Lulu revision.
- source: EEBO-TCP A93248: The Glorious Feast of the Gospel (London, John Rothwell, 1650) <https://github.com/textcreationpartnership/A93248>, `source/A93248.tcp.xml` (sha256 `d95173b14fc232a3…`)
- witness: Monergism's modernized text (from the SDG reprint; (c) Monergism Books 2017), a check only: source/witness-report.md <https://www.monergism.com/>
- witness: The earlier Freely Given Books copy (a Grosart-type text, 1862), corrected against 1650
- files: `the-glorious-feast-of-the-gospel-v13.1.pdf`, `the-glorious-feast-of-the-gospel-v13.1-cover.pdf`, `the-glorious-feast-of-the-gospel-v13.1-cover-front.png`, `the-glorious-feast-of-the-gospel-v13.1-cover-front.png`, `the-glorious-feast-of-the-gospel-v13.1.epub`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 56,190 printed words; 74.3% as printed
- changed in form only (spelling, case, punctuation): 13,233 words (23.6%)
- grammar modernized (hath -> has, thou -> you): 53 words (0.1%)
- changed in wording (emendations): 1,127 words (2.0%); 830 words added, 356 removed
- gaps in the transcription: 12, 12 restored, 0 left open
- notes: 0 added by the editor, 385 printed notes left out

## The Secret Key of Heaven

Brooks's The Privie Key of Heaven (1665) in modern spelling, from an earlier copy corrected against the 1665 printing; its dropped clauses, Latin, Greek and Hebrew restored from the page images.

- folder: `books/thomas-brooks/the-secret-key-of-heaven`
- version v6.1: tag `thomas-brooks/the-secret-key-of-heaven/v6.1`, signed off 2026-10-17 by Courtney Hicks
- template: fgbooks 0.12.0
- a point version: an improved edition after Lulu revision 6 (the sign-off note says whether its print is still that revision's)
- sign-off note: Print: changed since v6 (the-secret-key-of-heaven.pdf: 9 page(s) differ: 51, 68, 86, 149, 156, 167, 171, 223, 281); not a Lulu revision.
- source: EEBO-TCP A29703: The Privie Key of Heaven (London, John Hancock, 1665) <https://github.com/textcreationpartnership/A29703>, `source/A29703.tcp.xml` (sha256 `b6742bf2f0d59f51…`)
- witness: Chapel Library's edition (Private Key to Heaven, EPUB, text in the public domain), which the earlier copy followed: source/proofread-report.md <https://www.chapellibrary.org/>
- witness: The 1665 printing's page images (archive.org), for the Greek, Hebrew and illegible places <https://archive.org/details/bim_early-english-books-1641-1700_the-privie-key-of-heaven_brookes-thomas_1665>
- witness: The earlier Freely Given Books copy (lightly modernized), folded in as the review
- files: `the-secret-key-of-heaven-v6.1.pdf`, `the-secret-key-of-heaven-v6.1-cover.pdf`, `the-secret-key-of-heaven-v6.1-cover-front.png`, `the-secret-key-of-heaven-v6.1-cover-front.png`, `the-secret-key-of-heaven-v6.1.epub`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 102,961 printed words; 75.1% as printed
- changed in form only (spelling, case, punctuation): 20,915 words (20.3%)
- grammar modernized (hath -> has, thou -> you): 76 words (0.1%)
- changed in wording (emendations): 4,660 words (4.5%); 2,431 words added, 2,074 removed
- gaps in the transcription: 72, 61 restored, 11 left open
- notes: 0 added by the editor, 403 printed notes left out

## Of Domestical Duties

Gouge's Of Domesticall Duties (1622), all eight treatises in four volumes, in modern spelling with his wording kept; the transcription corrected against the 1622 page images, its Greek and Hebrew restored, six missing pages supplied from a second 1622 copy, and the printer's errata applied.

- folder: `books/william-gouge/domestical-duties`
- version v1: tag `william-gouge/domestical-duties/v1`, signed off 2026-10-17 by Courtney Hicks
- template: fgbooks 0.12.0
- source: EEBO-TCP A68107: Of Domesticall Duties, Eight Treatises (London, John Haviland for William Bladen, 1622) <https://github.com/textcreationpartnership/A68107>, `source/A68107.tcp.xml` (sha256 `d7404af2ca63812e…`)
- source: Pages 191-196 of the 1622 edition, missing from the copy the TCP transcribed, transcribed from a second 1622 copy (archive.org, n220-n225) <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties_gouge-william_1622>, `source/A68107.supplied.xml` (sha256 `a5620c2d6f858778…`)
- witness: The 1622 page images of the copy the TCP was made from (archive.org), for the Greek and Hebrew, illegible letters and the proofread: source/proofread-report.md <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622>
- witness: The second edition (1626, in The Workes of William Gouge), consulted for single readings <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-_gouge-william_1626>
- witness: The third edition (1634), consulted for single readings and the errata <https://archive.org/details/bim_early-english-books-1475-1640_of-domesticall-duties-_gouge-william_1634>
- witness: The earlier Freely Given Books edition (made with the converter before the TEI): source/migration-differences.md
- files: `domestical-duties-v1-vol-1.pdf`, `domestical-duties-v1-vol-2.pdf`, `domestical-duties-v1-vol-3.pdf`, `domestical-duties-v1-vol-4.pdf`, `domestical-duties-v1-cover-vol-1.pdf`, `domestical-duties-v1-cover-vol-2.pdf`, `domestical-duties-v1-cover-vol-3.pdf`, `domestical-duties-v1-cover-vol-4.pdf`, `domestical-duties-v1-cover-vol-1-front.png`, `domestical-duties-v1-cover-vol-2-front.png`, `domestical-duties-v1-cover-vol-3-front.png`, `domestical-duties-v1-cover-vol-4-front.png`, `domestical-duties-v1-cover-vol-1-front.png`, `domestical-duties-v1-vol-1.epub`, `domestical-duties-v1-cover-vol-2-front.png`, `domestical-duties-v1-vol-2.epub`, `domestical-duties-v1-cover-vol-3-front.png`, `domestical-duties-v1-vol-3.epub`, `domestical-duties-v1-cover-vol-4-front.png`, `domestical-duties-v1-vol-4.epub`

Fidelity to the source (counted from the TEI's record of every decision; ./fgb coverage):

- 290,439 printed words; 74.5% as printed
- changed in form only (spelling, case, punctuation): 72,878 words (25.1%)
- grammar modernized (hath -> has, thou -> you): 155 words (0.1%)
- changed in wording (emendations): 1,019 words (0.4%); 383 words added, 728 removed
- gaps in the transcription: 717, 717 restored, 0 left open
- notes: 5 added by the editor, 2 printed notes left out
