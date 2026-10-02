"""
Rule-based Early Modern English -> Modern English *spelling* normalizer.

Goal: change how a word is spelled, never which word is used. So we do NOT
touch closed-class archaic forms like "hath", "doth", "thou", "thee", "thy",
"thine", "ye", "shalt", "wilt", "art", "wert", "hast", "dost" -- those are
different grammatical forms, not alternate spellings of a modern word.
"""

import re
from spellchecker import SpellChecker

_SPELL = SpellChecker()
# A handful of real modern words the spellchecker's dictionary happens to
# lack, so they don't get wrongly treated as "unknown -> try stripping e".
_SPELL.word_frequency.load_words([
    "oeconomy", "familie", "goodwife", "housewifery", "manservant",
])

# Archaic pronouns / verb-forms that are a different *word* from their
# modern counterpart (has/does/you/your) rather than an alternate spelling
# of the *same* word -- leave these completely alone.
GRAMMAR_EXCEPTIONS = {
    "thou", "thee", "thy", "thine", "thyself", "ye",
    "hath", "doth", "shalt", "wilt", "art", "wert", "hast", "dost",
}

# Latin / non-English fragments quoted in marginal citations -- leave as-is
# (they are not English spelling to modernize).
LATIN_SKIP = {
    "absque", "aequipollent", "iuxta", "patriae", "ciuitate", "civitate",
    "euangelicam", "evangelicam", "sauorem", "savorem", "vxor", "vxorem",
    "uxor", "uxorem", "iunctione", "praesenti", "iure", "de", "sect",
    "libr", "cap", "sess", "decreto", "clandest", "matrim", "sacram",
    "concil", "trident", "can", "diuort", "repud", "beza", "bellarm",
    "aristot", "politic", "xenoph", "oecon", "cic", "nat", "deor", "ibid",
}

# Manual overrides for words the mechanical rules below get wrong or can't
# reach (irregular old spellings). Keys are lowercase old spelling.
MANUAL = {
    "approoue": "approve", "approoued": "approved", "approoueth": "approves",
    "approueth": "approves",
    "oeconomie": "economy", "oeconomicall": "economical",
    "oeconom": "oecon",  # bibliographic abbreviation, leave inert
    "prou": "prov",  # bibliographic abbreviation for Proverbs
    "sonne": "son", "sonnes": "sons",
    "folkes": "folks",
    "childe": "child",
    "kinde": "kind", "mankinde": "mankind",
    "onely": "only",
    "beholde": "behold",
    "vxorem": "uxorem",
    "vpo": "upon",
    "vprightnes": "uprightness",
    "iischa": "iischa",  # OCR noise / unclear fragment, leave inert
    "annaes": "anna's",
    "gouernme": "government",  # truncated OCR fragment
    "trarie": "trarie",  # OCR noise fragment ("con-trarie" split oddly), leave inert
    "niuence": "connivence",  # OCR-split remnant of "conniuence"
    "quetting": "acquitting",  # OCR-split remnant
    "iage": "marriage",  # OCR-split remnant of "marriage"
    "iunction": "conjunction",
    "iunctione": "iunctione",
    "civit": "civit",
    "ciuit": "civit",
    "aboue": "above",
    "eousnesse": "righteousness",  # OCR-split remnant of "righteousnesse"
    "itie": "itie",  # OCR-split remnant
    "seue": "seue",  # OCR-split remnant of "seuen"/"seuenth"
    "questio": "question",
    "iudgeme": "judgement",
    "patie": "patie",
    "civil": "civil",
    # u/v words the vowel-flanked heuristic can't reach (consonant before u)
    "aduance": "advance", "aduertising": "advertising", "aduice": "advice",
    "aduise": "advise", "aduised": "advised", "aduisedly": "advisedly",
    "vnaduisedly": "unadvisedly", "vnaduisedlie": "unadvisedly",
    # i/j mid-word (after a prefix, not word-initial)
    "preiudice": "prejudice", "preiudiced": "prejudiced",
    "preiudiciall": "prejudicial",
    "coniunction": "conjunction", "coniunctions": "conjunctions",
    "coniugall": "conjugal", "coniuction": "conjunction",
    "coniu": "conjunction", "coniuctio": "conjunction",
    # vowel-swap irregulars (not a plain u/v issue)
    "diuell": "devil", "diuels": "devils",
    "euah": "eve",
    # un- prefixed forms needing a final-letter/doubling fix beyond u/v
    "vnfeined": "unfeigned", "vncertaine": "uncertain", "vnchast": "unchaste",
    "vnckle": "uncle", "vncleane": "unclean", "vncleannes": "uncleanness",
    "vncleannesse": "uncleanness", "vncomlie": "uncomely",
    "vndergoe": "undergo", "vnequall": "unequal", "vniuersall": "universal",
    "vniust": "unjust", "vnknowne": "unknown", "vnlawfull": "unlawful",
    "vnmaried": "unmarried", "vnseemely": "unseemly", "vntill": "until",
    "vnfitlie": "unfitly",
    # words dictionaries mark as archaic prefix-variants of a different word
    # (un-/in-) are intentionally left untouched -- see DO_NOT_TOUCH.
    "vsurpe": "usurp", "preuaile": "prevail",
    "gouerne": "govern", "gouernement": "government",
    "gouernements": "governments", "gouernours": "governors",
    "gouerned": "governed",
    "thankesgiuing": "thanksgiving",
    "councell": "council", "cell": "cell",
    "becommeth": "cometh",
    "ministerie": "ministry",
    "controuersie": "controversy",
    "auaileable": "available",
    "autoritie": "authority",
    "beleeuers": "believers", "beleeueth": "believeth", "beleeuing": "believing",
    "beleeue": "believe", "beleeuer": "believer",
    "ciuill": "civil",
    "festiuall": "festival",
    "priuiledge": "privilege", "priuiledges": "privileges",
    "seuerall": "several",
    "soueraigne": "sovereign", "soueraigntie": "sovereignty",
    "vnbeleeuer": "unbeliever", "vnbeleeuing": "unbelieving",
    "vngratious": "ungracious",
    "trauell": "travel",
    "endeuour": "endeavour", "indeuour": "endeavour",
    "ioyfull": "joyful", "ioyne": "join", "ioyned": "joined",
    "iewes": "jews",
    "iesuites": "jesuits",
    "villanie": "villainy",
    "scie": "scie",  # OCR-split remnant, leave inert
    "praier": "prayer", "praiers": "prayers",
    "waightie": "weighty", "waightiest": "weightiest",
    # further "-all"/"-full" suffix strays the oracle rule can't reach
    # (different suffix, or an extra letter elsewhere in the root)
    "domesticall": "domestic", "mosaicall": "mosaic",
    "aristocraticall": "aristocratic",
    "fearefull": "fearful", "fruitefull": "fruitful",
    "behoofefull": "behooful",
    "reprochfull": "reproachful", "reproch": "reproach",
    "reprocheth": "reproacheth",
    # doubled-consonant-before-suffix strays
    "becomming": "becoming", "comming": "coming", "begunne": "begun",
    "buffetted": "buffeted", "ransommed": "ransomed",
    "befals": "befalls",
    # miscellaneous silent-e / vowel / missing-letter strays
    "affoord": "afford", "alleaged": "alleged", "alledged": "alleged",
    "alledgeth": "allegeth", "alwaies": "always", "alway": "always",
    "apparant": "apparent", "apparantly": "apparently",
    "auncient": "ancient", "battell": "battle", "bloud": "blood",
    "boords": "boards", "braule": "brawl", "brethen": "brethren",
    "cariage": "carriage", "cattel": "cattle",
    "busines": "business",
    "throughly": "thoroughly",
    "publike": "public", "publikely": "publicly",
    "wisedome": "wisdom",
    "earely": "early", "hainous": "heinous",
    "harted": "hearted", "haruest": "harvest",
    "instructer": "instructor", "furtherer": "furtherer",
    "cloathed": "clothed", "encreased": "increased",
    "indanger": "endanger",
    "intreated": "entreated", "intised": "enticed", "inticeth": "enticeth",
    "inioyed": "enjoyed", "inlarged": "enlarged",
    "imployment": "employment",
    "intertained": "entertained", "intertainment": "entertainment",
    "intire": "entire", "intrest": "interest",
    "otherside": "otherwise",
    "sute": "suit", "sutable": "suitable",
    "cozin": "cousin", "kinred": "kindred", "kinne": "kin",
    "hinderance": "hindrance",
    "swadled": "swaddled", "swadling": "swaddling",
    "rayment": "raiment",
    "recompence": "recompense", "defence": "defence", "offence": "offence",
    "defloured": "deflowered", "deflowred": "deflowered",
    "extreames": "extremes", "meerely": "merely", "meere": "mere",
    "cleere": "clear", "cleered": "cleared",
    "neere": "near", "neece": "niece", "neeces": "nieces",
    "theefe": "thief", "trueth": "truth",
    "vertuous": "virtuous", "vessell": "vessel",
    "souldier": "soldier", "starres": "stars",
    "stroks": "strokes", "wandring": "wandering",
    "tendring": "tendering", "shal": "shall", "wil": "will",
    "wel": "well", "fal": "fall", "willt": "wilt",
    "wherby": "whereby", "wherfore": "wherefore", "wherin": "wherein",
    "wherof": "whereof", "therfore": "therefore", "therof": "thereof",
    "therunto": "thereunto", "therupon": "thereupon",
    "yee": "ye", "loe": "lo", "hee": "he", "mee": "me", "shee": "she",
    "woma": "woman", "husba": "husband",
    "yeeld": "yield", "yeelded": "yielded", "yeeldeth": "yieldeth",
    "yeelding": "yielding", "yeelds": "yields", "yeeres": "years",
    "yonger": "younger",
    "threatneth": "threateneth",
    "mand": "manned", "manded": "manned", "mandement": "mandment",
    "manchild": "manchild",
    "obiect": "object", "obiected": "objected",
    "reiect": "reject", "reiected": "rejected", "reiecteth": "rejecteth",
    "reiection": "rejection", "reioicing": "rejoicing",
    "reioyce": "rejoice", "reioycing": "rejoicing",
    "enioy": "enjoy", "enioyeth": "enjoyeth", "enioyne": "enjoin",
    "enioyned": "enjoined",
    "coniectures": "conjectures",
    "subiect": "subject", "subiection": "subjection",
    "eies": "eyes", "saies": "says", "waies": "ways", "wayes": "ways",
    "adaies": "adays",
    "moneths": "months", "sixt": "sixth", "fift": "fifth",
    "fiftly": "fifthly",
    "growen": "grown", "setled": "settled", "entred": "entered",
    "entring": "entering", "remembred": "remembered",
    "saken": "shaken",
    "expresly": "expressly", "expressely": "expressly",
    "erroniously": "erroneously", "errour": "error",
    "emperours": "emperors", "inferiour": "inferior",
    "inferiours": "inferiors", "superiour": "superior",
    "superiours": "superiors", "neighbour": "neighbour",
    "infidell": "infidel", "infinitly": "infinitely",
    "franticke": "frantic", "heretike": "heretic",
    "heretikes": "heretics", "politike": "politic",
    "schismatike": "schismatic", "chuse": "choose",
    "choise": "choice", "choyce": "choice", "chast": "chaste",
    "dimme": "dim", "madde": "mad", "bedde": "bed",
    "hebrewesse": "hebrewess",
    "solemnely": "solemnly", "carelessely": "carelessly",
    "cheerefully": "cheerfully", "queene": "queen",
    "rammes": "rams", "sinne": "sin", "sinnest": "sinnest",
    "sinneth": "sinneth", "seemely": "seemly",
    "vncapable": "vncapable", "vncurable": "vncurable",
    "otherwhiles": "otherwhiles", "vnlooked": "unlooked",
    "vnexpedient": "unexpedient",
    "controlement": "controlment",
    "dismission": "dismission",
    "lothsome": "loathsome",
    "menstruous": "menstruous",
    # consonant-preceded u/v the vowel-flanked heuristic can't reach
    "seruant": "servant", "seruants": "servants", "serua": "servant",
    "serue": "serve", "serued": "served", "serueth": "serveth",
    "seruice": "service", "seruitude": "servitude",
    "obserue": "observe", "obserued": "observed",
    "conuenient": "convenient", "conueniently": "conveniently",
    "conuersation": "conversation", "conuerse": "converse",
    "conuerted": "converted", "inconuenience": "inconvenience",
    "preseruation": "preservation", "preserued": "preserved",
    "preseruing": "preserving",
    "resolued": "resolved", "reserued": "reserved",
    "dissolue": "dissolve", "dissolued": "dissolved", "dissolues": "dissolves",
    "inuisible": "invisible", "inuited": "invited", "inuocation": "invocation",
    "renue": "renew", "renued": "renewed", "renuing": "renewing",
    "peruerse": "perverse",
    "perswaded": "persuaded", "perswasion": "persuasion",
    # remaining silent-e / doubled-letter / missing-letter strays
    "harmelesse": "harmless",
    "houshold": "household", "housholder": "householder",
    "eleuenth": "eleventh",
    "wooll": "wool",
    "nearenesse": "nearness", "neerenesse": "nearness",
    "waightie": "weighty", "weightie": "weighty",
    "farre": "far", "foorth": "forth", "fourefold": "fourfold",
    "goe": "go", "doe": "do",
    "euill": "evil",
    "suspition": "suspicion",
    "prophane": "profane", "prophaned": "profaned",
    "schoolemen": "schoolmen",
    "tearme": "term", "tearmes": "terms",
    "warth": "wrath",
    "mariage": "marriage", "mariageable": "marriageable",
    "mariages": "marriages", "maried": "married",
    "themselues": "themselves", "selues": "selves",
    "mixt": "mixed", "queene": "queen", "siluer": "silver",
    "vncapable": "uncapable", "vncurable": "uncurable",
    "al": "all",
    "svrvey": "survey",
    "ordring": "ordering",
    "commandement": "commandment", "commandements": "commandments",
    "incouraged": "encouraged", "incouragement": "encouragement",
    "incourage": "encourage",
    "heer": "here",
    "forme": "form", "formes": "forms",
    "solemne": "solemn", "solemnely": "solemnly",
    "condemne": "condemn", "condemned": "condemned",
    "hymne": "hymn", "colume": "column",
}

# Words the mechanical rules would touch but that are already fine / should
# not be altered (safety net; extend as needed after review).
DO_NOT_TOUCH = {
    "quest", "question", "questions", "queen", "quiet",
    "delinquent", "consequent", "consequently", "frequent", "banqueting",
    "eight", "delight", "flight", "light", "might", "mighty",
    "night", "plight", "right", "sight", "weight",
    "brought", "bought", "sought", "besought", "thought", "wrought",
    "ought", "poet", "poets",
    # archaic prefix-variant of a *different* modern word (un- vs in-):
    # changing the prefix would be replacing a word, not modernizing its
    # spelling, so these are deliberately left alone (spelling of the
    # "un-" part itself is still fixed, via MANUAL, above).
}


def _fix_u_v(word: str) -> str:
    # Initial "v" followed by a consonant is really a vowel "u".
    word = re.sub(r'^v(?=[bcdfghjklmnpqrstwxz])', 'u', word)
    word = re.sub(r'^V(?=[BCDFGHJKLMNPQRSTWXZ])', 'U', word)
    # Medial "u" sitting between two vowels is really a consonant "v".
    # Iterate: fixing one can create a new vowel-u-vowel pattern (vniuersall).
    prev = None
    while prev != word:
        prev = word
        word = re.sub(r'(?<=[aeiouyAEIOUY])u(?=[aeiouyAEIOUY])', 'v', word)
        word = re.sub(r'(?<=[aeiouyAEIOUY])U(?=[AEIOUY])', 'V', word)
    return word


def _fix_i_j(word: str) -> str:
    # Initial "i" followed by a vowel, in a word that has no other vowel
    # before it, is historically the consonant "j" (iustice -> justice).
    word = re.sub(r'^i(?=[aeou])', 'j', word)
    word = re.sub(r'^I(?=[AEOU])', 'J', word)
    return word


def _fix_suffixes(word: str) -> str:
    # "-nesse"/"-lesse" etc: old "-Xsse" -> modern "-Xss" (drop silent e)
    if word.endswith('sse') and len(word) > 4:
        word = word[:-1]
    # "-ie" -> "-y" (familie -> family, dutie -> duty, policie -> policy)
    elif word.endswith('ie') and len(word) > 3:
        word = word[:-2] + 'y'
    return word


# Archaic verb-suffixes that we deliberately keep (giveth, walkest) -- we
# only use these to sanity-check that the *root* is spelled correctly, not
# to strip the suffix itself.
_ARCHAIC_SUFFIXES = ('eth', 'est')


def _dict_known(word: str) -> bool:
    return word in _SPELL


def _fix_silent_e(word: str) -> str:
    """Oracle-driven: old EME spelling often adds a superfluous silent 'e'
    (looke -> look, wisdome -> wisdom, goates -> goats, wherof stays as is),
    doubles a final consonant that modern spelling doesn't (generall ->
    general, beautifull -> beautiful), or drops a needed one (busines ->
    business). Only apply a change when doing so turns an *unrecognized*
    word into a *recognized* one, so real modern words are never touched."""
    if _dict_known(word):
        return word
    candidates = []
    if word.endswith('e') and len(word) > 3:
        candidates.append(word[:-1])
    if word.endswith('es') and len(word) > 4:
        candidates.append(word[:-2] + 's')
    # doubled final consonant that modern single-letters (generall -> general)
    for pair in ('ll', 'ff', 'mm', 'nn', 'pp', 'tt', 'rr'):
        if word.endswith(pair) and len(word) > 4:
            candidates.append(word[:-1])
    # "-nes" -> "-ness" (busines -> business, happines -> happiness)
    if word.endswith('nes') and len(word) > 4:
        candidates.append(word + 's')
    for c in candidates:
        if _dict_known(c):
            return c
    return word


def _fix_archaic_verb_root(word: str) -> str:
    """For words ending in the archaic -eth/-est suffix, run the full
    modernization pipeline on the root and re-attach the suffix, so e.g.
    'yeeldeth' (root yeeld -> yield) becomes 'yieldeth', not left alone."""
    for suf in _ARCHAIC_SUFFIXES:
        if word.endswith(suf) and len(word) > len(suf) + 2:
            root = word[:-len(suf)]
            if root in GRAMMAR_EXCEPTIONS or root in LATIN_SKIP or root in DO_NOT_TOUCH:
                continue
            new_root = MANUAL.get(root)
            if new_root is None:
                r = root
                r = _fix_u_v(r)
                r = _fix_i_j(r)
                r = _fix_silent_e(r)
                new_root = r
            if new_root != root:
                return new_root + suf
    return word


def modernize_word_lower(word: str) -> str:
    """Modernize the spelling of a single lowercase word. Returns the
    (lowercase) modern spelling, or the word unchanged if no rule applies."""
    if word in GRAMMAR_EXCEPTIONS or word in LATIN_SKIP:
        return word
    if word in DO_NOT_TOUCH:
        return word
    if word in MANUAL:
        return MANUAL[word]
    new = word
    new = _fix_u_v(new)
    new = _fix_i_j(new)
    new = _fix_suffixes(new)
    new = _fix_silent_e(new)
    if new == word:
        fixed_verb = _fix_archaic_verb_root(word)
        if fixed_verb != word:
            new = fixed_verb
    return new


def apply_case_pattern(original: str, modern_lower: str) -> str:
    """Re-apply the original word's capitalization pattern to a new
    (lowercase) spelling: ALLCAPS -> ALLCAPS, Titlecase -> Titlecase,
    else lowercase."""
    if original.isupper() and len(original) > 1:
        return modern_lower.upper()
    if original[:1].isupper():
        return modern_lower[:1].upper() + modern_lower[1:]
    return modern_lower
