# Witnesses: Goold's 1850 printing and the 1668 edition

The edition is CCEL's text of *Of the Mortification of Sin in Believers*
(`mort.thml.xml`), which is William H. Goold's (*The Works of John Owen*,
vol. 6, Johnstone and Hunter, 1850–53). Two witnesses were used to check it:

- **Goold's own printing**, the scan of vol. 6 at archive.org
  ([worksofjohnowe185006owen](https://archive.org/details/worksofjohnowe185006owen)),
  read through its OCR. It is not kept here.
- **The 1668 second edition** (London, Nathanael Ponder), EEBO-TCP A53715,
  kept untouched in `A53715.witness.xml`. The 1656 first edition was not
  compared.

A third copy, William H. Gross's modernized and annotated text (On the Wing,
© 2002, published by Monergism), was read only to confirm passages. It is a
paraphrase under copyright and is not kept here.

## Corrections to CCEL

CCEL's words were compared with the Goold scan and with 1668. Where CCEL
differs from both and they agree, CCEL is wrong. These are editor decisions
in the TEI (`review-report.md`):

| Chapter | CCEL | Corrected (Goold 1850 and 1668) |
| --- | --- | --- |
| II | He who doth not kill sin in *this* way | in *his* way |
| X | that the end of the way may be provoked to fly from it | the end of the way *wherein a man is ought by him to be concluded to be death, that he* may be provoked … (a line dropped) |
| X | the blessed Spirit, who hath undertaken to dwell in them, is continually considering | dwell in them *as temples of God, and to preserve them meet for him who so dwells in them*, is … (a line dropped) |
| X | throw away the *evidence* of his personal interest … he cannot keep them | the *evidences* |
| X | the countenancing *of* a lust | the countenancing a lust |

Also "judgement" (twice, chapter X) is spelled "judgment" as in the rest of
the book. Where CCEL differs from the Goold scan but agrees with 1668
("boast by other men's lives", "the event or thing promised"), CCEL stands.

## The 1668 edition

Compared word by word with `colophon/drift.py` (spelling, case and
punctuation ignored):

```sh
drift.py source/the-mortification-of-sin.tei.xml source/A53715.witness.xml \
    --name "1668 edition" --div to_the_Christian_reader=preface.typ \
    --div chapter=chapter-01.typ,...,chapter-14.typ --min 3
```

What remains is mostly Goold's: references written out ("Rom. vii.; James
iv." for "Jam."), the Greek the TCP transcription left out, "Sixthly" set
as "The sixth direction is", a few words the 1668 printing doubles ("as it
may have (as it may have)"). Differences of fewer than three words are
counted but not listed.

### to_the_Christian_reader (preface.typ)

- edition: 683 words; 1668 edition: 681 words; 96.77% alike
- 19 places differ (23 words of the edition, 21 of the 1668 edition); 1 of them are 3 words or more, listed below

- **different** (3 words), after “…Christ have anew imposed the yoke of a”
  - edition: self wrought out
  - 1668 edition: self-wrought-out

### chapter (chapter-01.typ,chapter-02.typ,chapter-03.typ,chapter-04.typ,chapter-05.typ,chapter-06.typ,chapter-07.typ,chapter-08.typ,chapter-09.typ,chapter-10.typ,chapter-11.typ,chapter-12.typ,chapter-13.typ,chapter-14.typ)

- edition: 41029 words; 1668 edition: 40827 words; 96.61% alike
- 1348 places differ (1489 words of the edition, 1287 of the 1668 edition); 40 of them are 3 words or more, listed below

- **different** (3 words), after “…of devout men ignorant of the gospel Rom”
  - edition: x John xv
  - 1668 edition: Joh
- **only in the edition** (3 words), after “…the performance of this duty is the Spirit”
  - edition: Εἰ δὲ Πνεύματι
- **only in the edition** (3 words), after “…here is the same with παλαιὸς ἄνθρωπος and”
  - edition: σῶμα τῆς ἁμαρτίας
- **only in the edition** (4 words), after “…works of the flesh as they are called”
  - edition: τὰ ἔργα τῆς σαρκός
- **only in the edition** (3 words), after “…name of the effects which it doth produce”
  - edition: Πράξεις τοῦ σώματος
- **only in the edition** (3 words), after “…produce Πράξεις τοῦ σώματος are as much as”
  - edition: φρόνημα τῆς σαρκός
- **different** (3 words), after “…The activity of abiding sin in believers Rom”
  - edition: vii James iv
  - 1668 edition: Jam
- **different** (3 words), after “…will lead me to what I chiefly intend”
  - edition: I
  - 1668 edition: The first is
- **different** (3 words), after “…its course would come to the height of”
  - edition: villany
  - 1668 edition: V ll ny
- **different** (3 words), after “…so to their ruin Heb iii it is”
  - edition: modest
  - 1668 edition: mo e t
- **different** (3 words), after “…victory it breaks the bones of the soul”
  - edition: Ps xxxi li
  - 1668 edition: Psal Psal
- **different** (3 words), after “…a man weak sick and ready to die”
  - edition: Ps xxxviii so
  - 1668 edition: Psal
- **different** (3 words), after “…pray and is a Spirit of supplication Rom”
  - edition: viii Zech xii
  - 1668 edition: Zach
- **different** (3 words), after “…mortification In what sense Not absolutely and necessarily”
  - edition: Ps lxxxviii Heman’s
  - 1668 edition: Psal Heman' s
- **different** (3 words), after “…desirable so expelling the love of the Father”
  - edition: John ii iii
  - 1668 edition: Joh Chap
- **different** (3 words), after “…forth the breaches ruin weakness desolations that one”
  - edition: unmortified
  - 1668 edition: un c tified
- **different** (3 words), after “…entice disquiet as naturally it is apt to”
  - edition: do James i
  - 1668 edition: doe Jam
- **only in the 1668 edition** (3 words), after “…describes as in the whole chapter so especially”
  - 1668 edition: vers of chap
- **different** (3 words), after “…xvi To labour to be acquainted with the”
  - edition: ways wiles
  - 1668 edition: Wayes W les
- **different** (3 words), after “…it is drawn in some of the philosophers”
  - edition: Seneca Tully
  - 1668 edition: Sencca Tu ly
- **different** (3 words), after “…opposition to this or that peculiar lust but”
  - edition: a
  - 1668 edition: it is an
- **only in the edition** (5 words), after “…In grieving the Spirit Wounding the new creature”
  - edition: Taking away a man’s usefulness
- **different** (3 words), after “…out to him So Heb iii to which”
  - edition: add chap x
  - 1668 edition: adde Heb
- **different** (3 words), after “…See if it can stand before this aggravation”
  - edition: of its guilt
  - 1668 edition: o i t
- **only in the edition** (3 words), after “…dangerous Descend to particulars As under the general”
  - edition: head of the
- **different** (4 words), after “…God to the natural root of that distemper”
  - edition: The sixth direction is
  - 1668 edition: Sixthly
- **different** (4 words), after “…treatise about entering into temptations treated of it”
  - edition: The seventh direction is
  - 1668 edition: Seventhly
- **only in the 1668 edition** (4 words), after “…use in our walking with God so far”
  - 1668 edition: as it may have
- **different** (3 words), after “…we see his face now and not his”
  - edition: back parts only
  - 1668 edition: back-parts onely
- **different** (3 words), after “…comprehend that for which we are comprehended Cor”
  - edition: xiii John iii
  - 1668 edition: Joh
- **only in the edition** (6 words), after “…walk by faith and not by sight Cor”
  - edition: v Διὰ πίστεως οὐ διὰ εἴδους
- **different** (4 words), after “…of the face of God in Jesus Christ”
  - edition: To which I answer
  - 1668 edition: A
- **different** (3 words), after “…his promise that the meek he will guide”
  - edition: in judgment
  - 1668 edition: n udg ment
- **only in the edition** (3 words), after “…upon the Lord who hideth his face from”
  - edition: the house of
- **different** (3 words), after “…into a trade of backsliding If upon thy”
  - edition: plastering thyself
  - 1668 edition: plaistering thy self
- **only in the edition** (3 words), after “…because it was not mixed with faith Heb”
  - edition: iv μὴ συγκεκραμένος
- **different** (3 words), after “…cleanse to melt and bind to obedience to”
  - edition: self emptiness etc
  - 1668 edition: self-emptiness c
- **only in the edition** (4 words), after “…relief from Christ which the apostle there calls”
  - edition: χάριν εἰς εὔκαιρον βοήθειαν
- **only in the edition** (4 words), after “…verse which we have translated to obtain is”
  - edition: λαβωμεν Ἵνα λάβωμεν ἔλεον
- **different** (3 words), after “…everywhere ascribed to his blood John i Heb”
  - edition: i Rev i
  - 1668 edition: Revelat

