#!/usr/bin/env python3
"""
gap_resolver.py
===============

Reconstruct EEBO-TCP <gap reason="illegible"> spans from the book's own
vocabulary.

TCP marks text it could not read as `<gap extent="1 letter"><desc>•</desc></gap>`,
which otherwise renders as a literal bullet in the middle of a word:

    Of a wiues inward f<gap extent="1 letter"/>are of her husband.

Perkins' *Christian Oeconomie* had 39 of these and they were resolved by hand
into an index-keyed override table.  This book has 478, which is too many to
read one at a time -- but it is also a 290,000-word book, and almost every
damaged word occurs undamaged somewhere else in it.  So: build a frequency
list of every word in the text, then for each gap look for words that match
`<letters before><n unknown><letters after>` and take the answer when it is
unambiguous.

That resolves the great majority mechanically and, crucially, resolves them
into *this document's own* spelling conventions rather than modern ones or a
guess ("euery" not "every", "mariage" not "marriage") -- which matters because
the old-spelling render is a published artifact in its own right and because
the modernizer downstream expects old spelling as its input.

What it deliberately will not do:
  - resolve a gap with no surviving letters on either side (extent="1 word",
    or a whole illegible note): there is nothing to match on
  - pick between candidates that are close in frequency ("m?n" is both "man"
    and "men"): those fall through to the bullet placeholder and are listed in
    the gap report for a human to settle in GAP_FIXES
  - trust the bullet count exactly.  TCP's own guidelines call it approximate,
    so an exact-length match is preferred but a length off by one is accepted
    when nothing exact fits.

Anything settled by hand goes in GAP_FIXES below, keyed by the gap's index in
the report (`--gap-report`), which is stable for a given input and renderer.
"""

import re
from collections import Counter, defaultdict

NS = {"t": "http://www.tei-c.org/ns/1.0"}

# Manual overrides, keyed by the index in the --gap-report TSV (which is the
# order gaps are resolved in, and is stable as long as the renderer walks the
# document the same way).  Entries here beat anything the frequency matcher
# comes up with.
#
# Everything below was read off the surrounding sentence, or -- for the Latin
# and Greek marginalia -- off the work being cited.  Two kinds of entry appear:
#   * gaps the matcher could not settle (ambiguous / no-match / no-context)
#   * gaps the matcher settled WRONGLY.  These are worth listing explicitly:
#     a one-letter gap with only one letter of surviving context is decided by
#     raw word frequency, and frequency is often just wrong ("f" + gap: "for"
#     beats "faune on", "of" beats "on").  The matcher is right about ~4 in 5
#     of those, which is why the report exists and why this table is long.
#
# An empty string means "there was no missing letter": a blot, a broken space,
# or a mark the transcriber read as a character.
GAP_FIXES = {
    36: "e",         # O wretched m[e]n that we are
    39: "n",         # L.L. Pipi[n]i (the Frankish Leges Pipini), Carol. M.
    40: "t",         # Qui diem obij[t] antequam baptisaretur
    41: "",          # "Ex opere operato, B[?]em. loc. citat." is Bellarmine:
                    # the note two sentences earlier in the same section
                    # (Treatise I, s. 45, on baptism) is "Bellarm. de Bapt.
                    # lib. 1. cap. 4", which is the place "loc. citat."
                    # points back to.  TEXT_FIXES completes the repair.
    55: "",          # a lost section number in a marginal cross-reference
    58: "u",         # nam a[u]arus (Aug. de doctr. Chr. 1. 25)
    76: "a",         # itaque duceb[a]tur in domum sponsi (Erasmus, Adagia)
    77: "c",         # nes[c]iret redeundi viam ad aedes parentum
    100: "s",        # such mischiefes a[s] children may fall into
    113: "ap",       # Vide [ap]ud Viu[es]. ibid.
    147: "ta",       # secundas nuptias [ta]nquam supra damnare
    154: "S",        # [S]uch as the virgin Mary will be a good example
    158: "i",        # the precedency [i]s giuen to the younger
    159: "r",        # excellently deciphe[r]ed in Solomons Song
    169: "b",        # the bridegroome and [b]ride goe out of their chamber
    170: "b",        # in the time of a Fast it must [b]e forborne
    172: "I",        # [I] will haue mercy, and not sacrifice (Hos. 6. 6)
    173: "sacrifice", # shall not mans or womans [sacrifice]?
    174: "or",       # continue so long sicke, [or] otherwise weake
    177: "fro",      # what can be expected [fro]m such polluted copulation
    191: "be",       # may sundry other wayes [be] applied
    192: "b",        # by way of comparison to [b]e taken
    198: "l",        # to carry away the goods and [l]ands
    202: "b",        # two that were in one [b]ed together
    206: "h",        # when [h]e obserued her to be with childe
    209: "s",        # The [s]ame respect moued Bathsheba
    211: "ou",       # man and wife ought (the transcription reads "aght")
    212: "gr",       # and that on good [gr]ounds
    213: "c",        # better then pre[c]ious ointment (Eccl. 7. 1)
    221: "o",        # Ios. 4. 15
    223: "d",        # haue no helpe from you, [d]o not in those things
    227: "t",        # iustum est vt eum gubernatorem assuma[t] (Ambr. Hexaem.)
    243: "i",        # so is [i]t a cause of many other vices
    247: "e",        # contracted thus, Iack[e], Tom, Will, Hall
    249: "f",        # to a very naturall, or a [f]renzy man
    250: "v",        # some rent, annuity, fees, [v]ailes, or the like
    254: "sh",       # to dispose as [sh]e please
    255: "g",        # to order his [g]ift as he please
    256: "fe",       # She is herein but as a [fe]offee in trust
    257: "st",       # other he reserueth for a [st]ocke
    262: "",         # a lost folio number in "Coke Rep. 4. 3 [?] 3."
    263: "a",        # Non excus[a]bit bona intentio vxoris (Greg. Sayr.)
    272: "s",        # componitur ex diuersis vocibu[s]
    276: "hi",       # Hebraei docent Vast[hi]am natam fuisse (Feuardent)
    280: "t",        # about the mee[t]nesse of it
    281: "c",        # quid censeas di[c]as, minime prohibeo (Greg. Naz.)
    282: "o",        # minime prohibe[o]: sed viri tui sententiam...
    288: "b",        # no greater ingratitude can [b]e shewed
    291: "n",        # to carry away the [n]ame of gratefulnesse
    295: "b",        # not the example of one only, [b]ut of many
    304: "t",        # gubernatorem [t]e Deus voluit esse sexus inferioris
    310: "n",        # namely, to be a[n] helpe
    312: "d",        # commend and reward what she hath well [d]one
    314: "fr",       # Giue her of the [fr]uit of her hands (Prov. 31. 31)
    316: "If",       # [If] there be no delight in ones person
    322: "c",        # as of a discontented [c]reditor ouer a desperate debtor
    324: "e",        # n[e]que quicquam tale exprobrauit (Chrysostom)
    325: "",         # C[or]nelius -- the transcription reads "C•raelius";
                   # Acts 10. 2, 30 in the margin identifies him
    326: "l",        # the lawes vnder which they [l]iue
    327: "f",        # vse all the [f]raudulent meanes they can
    334: "d",        # affected with a wrong [d]one to the bodie
    337: "h",        # for [h]e hath more power ouer them in his house
    343: "p",        # the most [p]eeuish, and peruerse wiues
    344: "i",        # they are very deuils [i]ncarnate
    345: "sh",       # in their place [sh]ew themselues so vnlike to Christ
    348: "s",        # they may haue [s]ome bait to allure their affections
    352: "lo",       # This cannot be a true sound [lo]ue
    354: "lo",       # an holy, pure, chaste, [lo]ue
    355: "ef",       # as is euident by the [ef]fect thereof
    356: "to",       # I am euen ashamed [to] mention
    357: "at",       # let such know, th[at] they shall be accounted
    361: "p",        # a pit of needlesse [p]erill
    362: "st",       # to bring vs to this [st]raite of parting with our life
    364: "e",        # cannot any other way be [e]ffected
    365: "to",       # no other way [to] redeeme the Church
    368: "ca",       # which minde men must much more [ca]rie towards their wiues
    369: "ga",       # It was for our saluation that Christ [ga]ue himselfe
    373: "be",       # if any extraordinary charge must [be] laid out
    374: "wi",       # little loue [wi]ll then appeare
    376: "g",        # As [g]old and other like mettals are tryed by the fire
    377: "affl",     # so loue by [affl]ictions and crosses
    378: "t",        # now [t]ender-hearted, then againe hard-hearted
    379: "l",        # now smiling, then [l]owring
    382: "a",        # proue in their loue as cold [a]s ice
    385: "w",        # [w]e haue on the one side a good direction
    386: "lo",       # a good direction to teach vs how to [lo]ue our wiues
    388: "far",      # it sheweth vs how [far]re short we come
    390: "w",        # a Subiection [w]hereunto by nature we are all loath to yeeld
    392: "m",        # and [m]uch more easie it is to performe the part of a wife
    394: "wiu",      # So ought men to loue their [wiu]es as their owne bodies
    395: "n",        # see they neither faune o[n] them, nor flatter them
    396: "t",        # as great as possibly i[t] can be
    403: "in",       # as the history [in] many particulars sheweth
    406: "ou",       # with goodnes he [ou]ght to ouercome euill
    408: "lo",       # for [lo]ue hopeth all things (1 Cor. 13. 7)
    409: "sa",       # as he may iustly [sa]y
    414: "",         # more abomi[]nable -- the bullet is a blot, not a letter
    427: "to",       # children haue euer vsed [to] giue those titles
    439: "t",        # much offended and grieued [t]hereat
    442: "be",       # must [be] so framed both for matter and manner
    448: "ll",       # they doe not so generally disa[ll]ow this dutie
    452: "",         # as some will haue it -- the bullet is a blot
    456: "b",        # It is collected [b]oth by ancient and later Diuines
    457: "in",       # our Lord Iesus Christ [in] his younger yeeres
    461: "bo",       # an hand in placing [bo]th their children
    464: "sh",       # that they [sh]ould see their children well trained vp
    465: "ent",      # children may [ent]er into religious orders
    467: "doe",      # Whereby they [doe] not only patronize apparent disobedience
    474: "d",        # while the [d]ate of their couenant lasteth
    475: "t",        # greater [t]hen of a childe
    484: "",         # My sonne, saith he -- the bullet is a blot
    495: "b",        # [b]ut it hardly ascendeth from children to parents
    499: "p",        # More tulere [p]atrum (Virgil, Aen. 11. 185-6)
    500: "t",        # More tulere pa[t]rum
    505: "S",        # [S]ome by the needlesse solemnitie of their parents funerall
    506: "so",       # are [so] farre cast into debt
    515: "a",        # such measure to be meated out to them, [a]s they mete
    518: "o",        # apud Di[o]g. Laert. l. 1.
    533: "ce",       # the law of God maketh it plaine in[ce]st
    535: "",         # a lost book number in a marginal cross-reference
    536: "i",        # that dutie [i]s due to them
    547: "in",       # though he truly [in]tend what he promiseth
    549: "h",        # but thought when [h]e made the promise
    551: "str",      # Gods power cannot be so [str]aitned
    552: "th",       # men may be taken away before [th]e time
    553: "li",       # but God euer [li]ueth, and changeth not
    554: "sa",       # Gods, who euer remaineth the [sa]me
    556: "b",        # no dutie so holy and necessarie, [b]ut may be peruerted
    557: "si",       # the catalogue of notorious [si]nnes
    558: "lu",       # through couetousnesse, [lu]st, vaine-glory
    559: "sh",       # in stead of the good which they [sh]ould doe
    561: "re",       # Is not this mee[re] apish kindnesse?
    563: "c",        # Basil. loc. [c]it.
    567: "w",        # the sincere milke of the [w]ord (1 Pet. 2. 2)
    569: "pr",       # the abilitie, and [pr]omptnesse which is in them to sucke
    570: "ca",       # Gods prouidence in [ca]using a womans breasts to yeeld milke
    577: "lo",       # mothers [lo]ue those children best
    578: "sh",       # and we [sh]all finde the dutie in question
    579: "p",        # that the [p]aps of that woman gaue him sucke
    582: "fo",       # to lay them [fo]rth for ostentation?
    583: "w",        # no warrant for that in all Gods [w]ord
    584: "n",        # there is [n]o milke in the breasts
    592: "d",        # She was therefore a [d]rie nurse
    594: "d",        # those nurses might be [d]ead
    595: "n",        # for want of milke, [n]ipple, or some other like defect
    596: "to",       # the childe which she [to]oke for her owne to nurse
    606: "se",       # a faithfull and constant ob[se]ruance of this ordinance
    610: "r",        # heathenish, idolatrous, [r]idiculous names
    614: "it",       # or to the childe [it] selfe
    617: "f",        # till it be [f]it to be placed forth
    620: "b",        # tagged and ragged like beggars [b]rats
    621: "o",        # but [o]uer-strictly hold them in
    622: "b",        # [b]ut plaine vnnaturalnesse in such parents
    628: "",         # (in the way that he should go) -- the bullet is a blot
    631: "",         # Parents are bour[]d -- see TEXT_FIXES: printed "bound"
    634: "o",        # workes of mercy [o]r of iudgement
    637: "lik",      # so [lik]ewise other masters (see TEXT_FIXES for the space)
    639: "If",       # [If] masters themselues be religious
    640: "",         # (same lacuna, second of three adjacent gaps)
    641: "",         # (same lacuna, third of three adjacent gaps)
    643: "th",       # very profitable to [th]e children
    648: "e",        # Quo sem[e]l est imbuta (Horace, Ep. 1. 2. 69)
    649: "o",        # seruabit od[o]rem testa diu
    650: "t",        # [t]hen be suffered to runne on in euill
    651: "t",        # till they get an habit [t]herein
    655: "m",        # they learne them [m]eerely by rote
    656: "bu",       # [bu]t afterwards come to make very good vse of them
    657: "fore",     # Where[fore] children are to be instructed betimes
    658: "cr",       # as corne is sowne in winter to receiue [cr]op
    659: "the",      # against [the]ir minde
    660: "n",        # his father taught him eue[n] while he was tender
    661: "s",        # the smart of neglecting hi[s] other children
    666: "n",        # more peruersenesse and vntowardnesse i[n] such parents
    667: "u",        # illos & seipsum [u]na perdidit (Chrys. in 1 Tim. hom. 9)
    668: "",         # therein, he brought destruction -- the bullet is a blot
    669: "l",        # who are [l]oth to giue them a foule word
    673: "e",        # semetipsos in furorem iudicij dem[e]rgunt (Orig. in Iob)
    676: "v",        # to be of little [v]se
    677: "fit",      # though children be neuer so [fit] for these callings
    678: "n",        # God hath placed such a[n] one in his place
    680: "t",        # Ma[t]. 6. 19. expounded
    691: "in",       # [in] case God take them away
    693: "ll",       # as a[ll] their care is to aduance their eldest sonne
    694: "n",        # and i[n] the meane while neglect their younger children
    698: "x",        # ...phrontisteria... constru[x]it (Niceph. eccl. hist.)
    703: "l",        # the seruants of Lidia, and of the Iay[l]er
    717: "t",        # vt fra[t]rem propter fidei societatem (Constit. Apost.)
    719: "tuum",     # istum quem seruum [tuum] vocas (Seneca, Ep. 47)
    720: "r",        # the errata list: "ibid. in ma[r]g. l. 8." (in the margin)
}

WORD_RE = re.compile(r"[A-Za-z']+")
# A word that had a gap in it is not evidence about spelling, so mask any
# token touching the gap marker before counting.
MASKED_WORD_RE = re.compile(r"[A-Za-z']*\x01[A-Za-z']*")


def _local(tag):
    return tag.rsplit("}", 1)[-1]


# Attribute stamped on every <gap> so a manual fix can name it.  The key has
# to be a property of the gap itself, not of when it happens to be resolved:
# keying on resolution order means rendering a subset of the book, or moving
# a gap type out of the pipeline, silently renumbers every fix after it.
INDEX_ATTR = "gapidx"


class GapResolver:
    def __init__(self, root, normalize):
        self.normalize = normalize
        self.vocab = self._build_vocab(root)
        self.log = []
        self.counts = Counter()
        self._context = ("", "")
        self._stamp_indices(root)

    @staticmethod
    def _stamp_indices(root):
        """Number every <gap> by its position in the document -- all of them,
        including the foreign-script and duplicate-page ones the renderer
        drops, so the numbering does not depend on renderer policy either.
        The attribute survives the deepcopy that paragraph and list rendering
        does, which an object identity would not."""
        tag = "{http://www.tei-c.org/ns/1.0}gap"
        for i, el in enumerate(root.iter(tag)):
            el.set(INDEX_ATTR, str(i))

    # -- vocabulary ---------------------------------------------------------

    def _build_vocab(self, root):
        """Word frequencies over the whole document, in original spelling,
        with end-of-line hyphens joined and every gap-damaged word excluded."""
        out = []
        text_el = root.find(".//t:text", namespaces=NS)
        self._plain(text_el, out)
        text = MASKED_WORD_RE.sub(" ", "".join(out))
        return Counter(w.lower() for w in WORD_RE.findall(text) if len(w) > 1)

    def _plain(self, el, out):
        if el.text and not self._leading_joinable(el):
            out.append(self.normalize(el.text))
        for ch in el:
            tag = _local(ch.tag)
            if tag == "gap":
                out.append("\x01")
            elif tag == "g":
                ref = ch.get("ref", "")
                if ref in ("char:EOLhyphen", "char:EOLunhyphen"):
                    pass          # soft line break: the word rejoins
                elif ref == "char:cmbAbbrStroke":
                    out.append("\x01")   # an abbreviated word, not a spelling
                elif ch.text:
                    out.append(self.normalize(ch.text))
            elif tag in ("pb", "fw", "milestone"):
                pass
            elif tag == "expan":
                ex = ch.find(".//t:ex", namespaces=NS)
                out.append(self.normalize(ex.text) if ex is not None and ex.text else "")
            else:
                self._plain(ch, out)
            if ch.tail and not self._tail_joinable(ch, tag):
                out.append(self.normalize(ch.tail))

    @staticmethod
    def _leading_joinable(el):
        if not el.text or el.text.strip() or "\n" not in el.text:
            return False
        return len(el) > 0 and _local(el[0].tag) in ("g", "gap")

    @staticmethod
    def _tail_joinable(ch, tag):
        nxt = ch.getnext()
        return (tag in ("g", "gap") and nxt is not None
                and _local(nxt.tag) in ("g", "gap")
                and not ch.tail.strip() and "\n" in ch.tail)

    # -- resolution ---------------------------------------------------------

    @staticmethod
    def _extent_letters(extent):
        m = re.match(r"(\d+)\s+letter", extent or "")
        return int(m.group(1)) if m else None

    def resolve(self, idx, left, right, extent, default):
        """Return the letters to splice in, or None to fall back to the
        placeholder.  `idx` is the gap's document-order number (see
        _stamp_indices), `left` is everything rendered before it and `right`
        everything after, with any gap tokens still ahead masked out."""
        prefix = self._trailing_word(left)
        suffix = self._leading_word(right)
        n = self._extent_letters(extent)
        self._context = (self._snip(left[-90:]), self._snip(right[:90]))

        forced = GAP_FIXES.get(idx)
        if forced is not None:
            self._record(idx, prefix, suffix, extent, forced, "manual")
            return forced

        # One letter of surviving context is enough to work with -- a great
        # many of these gaps are a lost letter of a two-letter function word
        # ("a" + gap -> "as", gap + "f" -> "of").  With none at all there is
        # nothing to match, and extents measured in words or pages are whole
        # lost passages, not spellings.
        if n is None or not (prefix or suffix):
            self._record(idx, prefix, suffix, extent, None, "no-context")
            return None

        # Bullet counts are approximate, so try the stated length first and
        # widen only if it yields nothing.
        ambiguous = None
        for k in (n, n + 1, n - 1):
            if k < 1:
                continue
            ranked = self._ranked(prefix, suffix, k)
            if not ranked:
                continue
            best, best_n = ranked[0]
            if len(ranked) > 1 and not (best_n >= 3 and best_n >= 5 * ranked[1][1]):
                ambiguous = ranked
                break
            fill = self._match_case(best, prefix, suffix)
            self._record(idx, prefix, suffix, extent, fill,
                         "auto" if k == n else f"auto({k} letters)", ranked[:4])
            return fill

        # Candidates that exist but do not agree are a genuinely ambiguous
        # missing letter ("m?n" is man and men); leave those for a human.
        # Only when NO word in the book fits the shape at all is it worth
        # asking whether a letter is missing in the first place.
        if ambiguous is not None:
            self._record(idx, prefix, suffix, extent, None, "ambiguous",
                         ambiguous[:4])
            return None

        # A one-letter "illegible" is often not a letter at all but a blot,
        # a broken space, or an inked-over word division: the letters on
        # either side already spell whole words.  Bridge those rather than
        # inventing a letter.
        blot = self._blot(prefix, suffix, left, right)
        if blot is not None:
            self._record(idx, prefix, suffix, extent, blot,
                         "blot" if blot == "" else "word-break")
            return blot

        # Last resort: the bullet count can be badly short when a whole
        # syllable was lost ("•ictions" for "afflictions").  Widen a long way,
        # but insist on a single well-attested candidate.
        for k in range(n + 2, n + 6):
            ranked = self._ranked(prefix, suffix, k)
            if len(ranked) == 1 and ranked[0][1] >= 3:
                fill = self._match_case(ranked[0][0], prefix, suffix)
                self._record(idx, prefix, suffix, extent, fill,
                             f"auto({k} letters)", ranked)
                return fill

        self._record(idx, prefix, suffix, extent, None, "no-match")
        return None

    def _ranked(self, prefix, suffix, k):
        return sorted(self._candidates(prefix, suffix, k).items(),
                      key=lambda kv: -kv[1])

    def _blot(self, prefix, suffix, left, right):
        """Return "" if the gap sits beside a space and the word next to it is
        already complete, " " if it sits between two complete words with no
        space of its own, or None if it really does look like a lost letter."""
        def whole(w):
            # "a" and "O" are the only one-letter words here; the vocabulary
            # is built with a length-2 floor, so spell them out.
            if len(w) == 1:
                return w.lower() in ("a", "o")
            return len(w) > 1 and self.vocab.get(w.lower(), 0) >= 3
        left_spaced = not left or left[-1].isspace()
        right_spaced = not right or right[0].isspace()
        if left_spaced and right_spaced:
            return None                      # standalone: nothing to bridge
        if left_spaced and whole(suffix):
            return ""
        if right_spaced and whole(prefix):
            return ""
        if whole(prefix) and whole(suffix):
            return " "
        return None

    def _candidates(self, prefix, suffix, k):
        """Middles (summed frequency) of vocabulary words shaped
        prefix + k unknown letters + suffix."""
        p, s = prefix.lower(), suffix.lower()
        want = len(p) + k + len(s)
        groups = defaultdict(int)
        for word, freq in self.vocab.items():
            if len(word) != want or not word.startswith(p) or not word.endswith(s):
                continue
            groups[word[len(p):len(word) - len(s)] if s else word[len(p):]] += freq
        return groups

    @staticmethod
    def _snip(text):
        """Strip the placeholder tokens out of a context excerpt so the
        report reads as prose."""
        text = re.sub(r"\x00ZZ(?:EM|SU)(?:START|END)ZZ\x00", "", text)
        text = re.sub(r"\x00ZZFN\d{4}ZZ\x00", "", text)
        return re.sub(r"[\x00\x01]", "", text)

    @staticmethod
    def _trailing_word(text):
        m = re.search(r"[A-Za-z']+$", text)
        return m.group(0) if m else ""

    @staticmethod
    def _leading_word(text):
        m = re.match(r"[A-Za-z']+", text)
        return m.group(0) if m else ""

    @staticmethod
    def _match_case(middle, prefix, suffix):
        """The vocabulary is folded to lowercase, so re-case the fill from its
        surroundings: all-caps neighbours give an all-caps fill, and a fill at
        the very start of a word is left lowercase (nothing in the source says
        whether the lost letter was capital)."""
        context = prefix + suffix
        if context and context.isupper():
            return middle.upper()
        return middle

    # -- reporting ----------------------------------------------------------

    def _record(self, idx, prefix, suffix, extent, fill, how, ranked=None):
        self.counts[how.split("(")[0]] += 1
        self.log.append({
            "idx": idx, "prefix": prefix, "suffix": suffix, "extent": extent,
            "fill": fill, "how": how,
            "candidates": ", ".join(f"{m}:{n}" for m, n in (ranked or [])),
            "before": self._context[0], "after": self._context[1],
        })

    def summarize(self, stream):
        total = len(self.log)
        filled = sum(1 for r in self.log if r["fill"] is not None)
        print(f"Illegible gaps: {total}, filled {filled} "
              f"({filled * 100 // total if total else 0}%) -- "
              + ", ".join(f"{k}={v}" for k, v in sorted(self.counts.items())),
              file=stream)

    def write_report(self, path):
        self.log.sort(key=lambda r: r["idx"])
        with open(path, "w", encoding="utf-8") as f:
            f.write("idx\thow\textent\tword\tcandidates\tbefore\tafter\n")
            for r in self.log:
                word = r["prefix"] + (r["fill"] if r["fill"] is not None else "?") + r["suffix"]
                f.write("\t".join([
                    str(r["idx"]), r["how"], r["extent"], word, r["candidates"],
                    r["before"], r["after"],
                ]) + "\n")
