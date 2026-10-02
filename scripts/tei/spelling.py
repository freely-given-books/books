"""
Rule-based Early Modern English -> Modern English *spelling* normalizer.

Goal: change how a word is spelled, never which word is used.  So closed-class
archaic forms -- "hath", "doth", "thou", "thee", "thy", "thine", "ye",
"shalt", "wilt", "art", "wert", "hast", "dost" -- are left completely alone;
those are different grammatical forms, not alternate spellings of a modern
word.

Shared by every book (a book adds its own words with SPELLING in its
editorial.py). The rules: u/v, i/j, -ie -> -y, -nesse -> -ness, a dictionary
oracle for silent e and doubled letters, and THE LETTERFORM ORACLE, which
came from the Gouge edition (merged here in 2026).

Perkins' *Christian Oeconomie* is ~30,000 words and its u/v and i/j irregulars
fitted in a hand-written table of a couple of hundred entries.  Gouge is
~290,000 words and roughly 8,500 distinct ones; hand-listing "seruant",
"aduanced", "saluation", "obiection", "iniurious", "preserue", "peruert" and
their inflections is both endless and error-prone.

But u/v and i/j are not really spelling differences at all -- in 1622 they
were the same letter, chosen by position rather than by sound.  So the modern
form is recoverable by search: try swapping them, and accept the variant the
dictionary recognises.  `_oracle_letterforms` does exactly that, smallest
number of swaps first, and only ever runs on a word the dictionary does not
already know.  That one rule replaces most of what was a manual table, and
generalises to any EEBO-TCP text without retuning.

What still needs a hand-written table, and always will:
  - words whose modern form differs by more than letterform and a silent e
    ("perswade" -> "persuade", "pretious" -> "precious")
  - proper names, where no dictionary helps (see NAMES)
  - words where the oracle would find a real but WRONG modern word: those go
    in DO_NOT_TOUCH.
"""

import re

from spellchecker import SpellChecker

_SPELL = SpellChecker()

# Real modern words the frequency-built dictionary happens to lack.  Without
# these the oracle either leaves an old spelling alone (because it cannot see
# that the modern form exists) or, worse, keeps searching and finds something
# else.  British -our/-ise forms are here on purpose: the editions keep them.
_SPELL.word_frequency.load_words([
    "oeconomy", "familie", "goodwife",
    "honour", "honours", "honourable", "honourably", "dishonour",
    "dishonourable", "labour", "labours", "laboured", "labouring",
    "neighbour", "neighbours", "saviour", "behaviour", "endeavour",
    "endeavours", "favour", "favours", "favoured", "favourable",
    "succour", "rigour", "vigour", "valour", "humour", "colour", "odour",
    "clamour", "armour", "ardour", "fervour", "splendour",
    "baptise", "baptised", "baptising", "baptism", "catechise",
    "catechised", "catechising", "chastise", "chastised",
    "mischiefs", "griefs", "beliefs", "reliefs", "thiefs",
    "housewifery", "manservant", "maidservant", "menservants",
    "unfeigned", "unadvisedly", "unchaste", "uncomely", "unseemly",
    "behoveful", "behovefully", "unbeseeming", "wive", "wived",
    "offence", "offences", "defence", "defences", "pretence", "pretences",
    "honoured", "honouring", "labourer", "labourers", "harbour",
    "harbours", "colours", "favouring", "mould", "moulded", "practise",
    "savour", "savours", "savoury", "demeanour", "succours",
    "practised", "practising", "counsellor", "counsellors", "traveller",
    "travellers", "worshipper", "worshippers", "unfaithfulness",
    "womb", "wombs", "dowry", "dowries", "espousals", "betroth",
    "betrothed", "concubine", "concubines", "helpmeet",
])

# Archaic pronouns and verb-forms that are a different *word* from their
# modern counterpart rather than an alternate spelling of the same one.
GRAMMAR_EXCEPTIONS = {
    "thou", "thee", "thy", "thine", "thyself", "ye",
    "hath", "doth", "shalt", "wilt", "art", "wert", "hast", "dost",
    "saith", "quoth", "canst", "didst", "couldst", "wouldst", "shouldst",
    "hadst", "wast", "mayest", "maist", "mayst", "sayest", "knowest",
    "seest", "wouldest", "shouldest", "couldest",
}

# Latin and Greek fragments quoted in the running text (the marginal notes
# are never modernized at all, so only body-text Latin needs listing).  Left
# as they are: they are not English spelling to modernize, and the oracle
# would happily turn "iuxta" into "juxta" or "vxor" into "uxor" halfway.
LATIN_SKIP = {
    "quippe",
    "absque", "ad", "de", "ex", "in", "non", "per", "pro", "sine", "sub",
    "vt", "et", "est", "sunt", "cum", "quod", "qui", "quae", "quam",
    "vxor", "vxorem", "uxor", "uxorem", "vir", "viri", "virum",
    "pater", "patris", "mater", "matris", "filius", "filia",
    "iuxta", "ibid", "idem", "loc", "cit", "lib", "cap", "tom", "fol",
    "epist", "hom", "serm", "orat", "quaest", "sect", "sess", "can",
    "oeconom", "oecon", "politic", "ethic", "rhet",
    "opere", "operato", "ratum", "praesenti", "futuro", "iure",
    # Latin whose English-looking truncation the silent-e rules would
    # otherwise take ("lege" -> "leg", "ille" -> "ill", "posse" -> "poss",
    # "disces" -> "discs", "homines" -> "hominess").  modernize.py skips
    # whole Latin runs, which handles the quotations; this list catches the
    # short fragments that sit inside an otherwise English note.
    "lege", "leges", "legis", "posse", "potest", "possunt",
    "ille", "illa", "illud", "illi", "illos", "illum",
    "habere", "habet", "habens", "facere", "facit", "faciendam",
    "parere", "parens", "dicere", "dicit", "dicas", "ferre", "fert",
    "inde", "nonne", "homines", "homo", "hominem", "hominis",
    "ecclesia", "ecclesiae", "disces", "discere", "esse", "fuisse",
    "fuit", "sunt", "sit", "sint", "erat", "velle", "nolle",
    "imperare", "obedire", "seruire", "seruus", "seruum", "seruos",
    "causa", "res", "rei", "vita", "vitae", "mors", "mortis",
    "corpus", "corporis", "opus", "operis", "lex", "verbum", "verba",
    "nomen", "nomine", "deus", "dei", "deo", "deum", "dominus",
    "domini", "domino", "dominum", "magis", "minus", "bene", "male",
    "tam", "iam", "nunc", "semper", "ita", "sic", "quare", "unde",
    "ibi", "ubi", "omnis", "omnes", "omnia", "alius", "alii",
    "ipse", "ipsa", "ipsum", "iste", "istum", "quem", "cui", "cuius",
    "hoc", "haec", "hic", "atque", "neque", "sicut", "tanquam",
    # from the shared table
    "aequipollent", "aristot", "bellarm", "beza", "cic", "ciuitate", "civitate", "clandest", "concil", "decreto", "deor", "diuort", "euangelicam", "evangelicam", "iunctione", "libr", "matrim", "nat", "patriae", "repud", "sacram", "sauorem", "savorem", "trident", "xenoph",
}

# Roman numerals and abbreviations that are letter-strings, not words.  The
# oracle must not see them: "vi" and "iii" are made entirely of the letters
# it swaps.
DO_NOT_TOUCH = {
    "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi",
    "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx",
    "answ", "quest", "vers", "viz", "sc", "chap", "pag", "lin",
    "iiii", "luk", "psal", "prou", "eccl", "esa", "ezek", "hos", "mal", "matt",
    "rom", "cor", "gal", "eph", "phil", "col", "thes", "tim", "tit",
    "heb", "pet", "reu", "gen", "exod", "leu", "num", "deut",
    "sam", "king", "chron", "ezr", "neh", "esth",
    "rem", "res", "vsu", "aug", "hier", "chrys", "greg", "ambr",
    # (Ioh., Iudg., Iam. are left to the i/j rule: Joh., Judg., Jam.)
    # words where a swap or a silent-e strip finds a real but wrong word
    "quiet", "quite", "queen", "question", "questions", "quest",
    "consequent", "frequent", "delinquent", "banqueting",
    "eight", "light", "might", "mighty", "night", "right", "sight",
    "weight", "delight", "flight", "plight", "brought", "bought",
    "sought", "besought", "thought", "wrought", "ought", "nought",
    "poet", "poets", "quiver", "liver", "river", "diver", "giver",
    "sliver", "shiver", "silver", "deliver", "delivered",
    # from the shared table
    "consequently",
}

# Proper names, where no dictionary can help.  Restricted to biblical and
# classical names whose modern English form is not in doubt; names the AV
# itself spells as this text does are left alone.
NAMES = {
    "iaakob": "Jacob", "iakob": "Jacob", "iacob": "Jacob",
    "isaak": "Isaac", "abram": "Abram", "salomon": "Solomon", "absolom": "Absalom", "absalom": "Absalom",
    "annah": "Hannah", "iesus": "Jesus", "iesu": "Jesu",
    "iohn": "John", "iames": "James", "ioseph": "Joseph",
    "iosuah": "Joshua", "iosua": "Joshua", "iob": "Job", "ioel": "Joel",
    "ionah": "Jonah", "ionas": "Jonas", "iudah": "Judah", "iudas": "Judas",
    "iude": "Jude", "iudith": "Judith", "ieremie": "Jeremiah",
    "ieremiah": "Jeremiah", "ierusalem": "Jerusalem", "iewes": "Jews",
    "iew": "Jew", "iewish": "Jewish", "iezabel": "Jezebel",
    "iehu": "Jehu", "iephtha": "Jephthah", "iair": "Jair",
    "ionathan": "Jonathan", "iordan": "Jordan", "iosias": "Josiah",
    "iosiah": "Josiah", "israelites": "Israelites", "israel": "Israel",
    "eue": "Eve", "euah": "Eve",
    "bathsheba": "Bathsheba", "bethsheba": "Bathsheba",
    "elkanah": "Elkanah", "michal": "Michal", "mical": "Michal",
    "rebekah": "Rebekah", "sarah": "Sarah", "sara": "Sarah",
    "esaias": "Esaias", "elias": "Elias", "eliseus": "Elisha",
    "iulian": "Julian", "iuno": "Juno", "iupiter": "Jupiter",
    "cain": "Cain", "abel": "Abel", "noah": "Noah",
    "dauid": "David", "iaakobs": "Jacobs",
    "booz": "Boaz", "rahel": "Rachel", "shemei": "Shimei",
    "rebeckah": "Rebekah", "iaakobs": "Jacobs",
}

# Words that are a proper name when capitalized mid-sentence and an ordinary
# word otherwise.  "Mary" the mother of Christ appears throughout, and
# "marie"/"mary" is also this book's spelling of the verb "marry" -- so
# modernizing on spelling alone turns the Virgin into "Marry".  modernize.py
# consults this before anything else for a capitalized, non-sentence-initial
# token.
AMBIGUOUS_NAMES = {
    "mary": "Mary", "marie": "Mary",
}

# Irregulars the rules above cannot reach: the modern form differs by more
# than letterform, a silent e, or a doubled consonant.
MANUAL = {
    # -- letters that simply changed --------------------------------------
    "beleeue": "believe", "beleeues": "believes", "beleeued": "believed",
    "beleeueth": "believeth", "beleeuing": "believing",
    "beleeuer": "believer", "beleeuers": "believers",
    "vnbeleeuer": "unbeliever", "vnbeleeuers": "unbelievers",
    "vnbeleeuing": "unbelieving", "beleefe": "belief",
    "ioyne": "join", "ioyned": "joined", "ioynes": "joins",
    "ioyning": "joining", "ioynt": "joint", "ioyntly": "jointly",
    "conioyned": "conjoined", "adioyned": "adjoined",
    "enioyne": "enjoin", "enioyned": "enjoined", "enioyning": "enjoining",
    "ioyfull": "joyful", "ioyfully": "joyfully",
    "priuiledge": "privilege", "priuiledges": "privileges",
    "behouefull": "behoveful", "behoofefull": "behoveful",
    "cheerefull": "cheerful", "cheerefully": "cheerfully",
    "cheerefulnesse": "cheerfulness",
    "thankesgiuing": "thanksgiving", "thankesgiuings": "thanksgivings",
    "reioyce": "rejoice", "reioyced": "rejoiced", "reioycing": "rejoicing",
    "reioyceth": "rejoiceth", "inioyned": "enjoined",
    "connexion": "connection", "catholike": "catholic",
    "apparrell": "apparel", "pharisies": "Pharisees",
    "gratious": "gracious", "graciously": "graciously",
    "schollers": "scholars", "scholler": "scholar",
    "stroake": "stroke", "stroakes": "strokes", "smoake": "smoke",
    "yoake": "yoke", "yoakes": "yokes", "doat": "dote", "doating": "doting",
    "stomacke": "stomach", "stiled": "styled", "stileth": "styleth",
    "spightfull": "spiteful", "scornefull": "scornful",
    "fearefull": "fearful", "fearefully": "fearfully",
    "seemely": "seemly", "vnseemely": "unseemly",
    "politique": "politic", "heretiques": "heretics",
    "saniour": "saviour", "frolicke": "frolic",
    "forceable": "forcible", "firmely": "firmly",
    "dispence": "dispense", "defloured": "deflowered",
    "disanull": "disannul", "weined": "weaned", "vineger": "vinegar",
    "toies": "toys", "surmizes": "surmises", "stoicks": "Stoics",
    "physitian": "physician", "physitians": "physicians",
    "murther": "murder", "murthered": "murdered",
    "murtherer": "murderer", "murtherers": "murderers",
    "linnen": "linen", "lowring": "louring", "tryall": "trial",
    "traiterous": "traitorous", "alleadged": "alleged",
    "immediatly": "immediately", "destroied": "destroyed",
    "caried": "carried", "carieth": "carrieth", "carying": "carrying",
    "expences": "expenses", "setled": "settled", "setling": "settling",
    # -- -ed/-ing forms that lost a vowel ---------------------------------
    "administring": "administering", "administred": "administered",
    "ministred": "ministered", "ministring": "ministering",
    "numbred": "numbered", "numbring": "numbering",
    "quickning": "quickening", "quickned": "quickened",
    "shortning": "shortening", "shortned": "shortened",
    "comming": "coming", "becomming": "becoming",
    "clearely": "clearly", "chirurgion": "surgeon",
    "araied": "arrayed", "araying": "arraying", "aray": "array",
    "weine": "wean", "weining": "weaning", "valew": "value",
    "therby": "thereby", "tendred": "tendered", "tatling": "tattling",
    "sweetned": "sweetened", "surmize": "surmise", "sleightly": "slightly",
    "sawce": "sauce", "rellish": "relish", "recompenced": "recompensed",
    "raigne": "reign", "raigned": "reigned", "publicke": "public",
    "praied": "prayed", "powting": "pouting",
    "preheminence": "preeminence", "preheminency": "preeminence",
    # "shew" is still in dictionaries as an archaic variant, so the oracle
    # leaves it alone; it is "show" 475 times here and never anything else.
    # The -eth and -est endings stay, as they do on every other verb in the
    # book (giveth, maketh, loveth): they are a verb form, not a spelling.
    # Every form in the source, including "shewes" -- the -es/-s rule would
    # otherwise reduce it to "shews", which is still a dictionary word, so it
    # would stop there and never reach "shows".
    "shew": "show", "shewes": "shows", "shews": "shows",
    "shewed": "showed", "shewing": "showing", "sheweth": "showeth",
    "shewest": "showest", "shewn": "shown", "shewne": "shown",
    "foreshew": "foreshow", "foreshewed": "foreshowed",
    "foresheweth": "foreshoweth", "foreshewing": "foreshowing",
    "compleat": "complete", "compleatly": "completely",
    "curtesie": "courtesy", "curtesies": "courtesies",
    "affaires": "affairs", "privatly": "privately",
    "purloyning": "purloining", "purloyne": "purloin",
    "fained": "feigned", "faining": "feigning",
    "sleight": "slight", "sleightly": "slightly",
    # "forme" and "maine" are real modern words in narrow technical senses,
    # so the dictionary oracle leaves them alone -- but in an Early Modern
    # religious text they are always "form" and "main".
    "forme": "form", "formes": "forms", "maine": "main",
    "commeth": "cometh", "becommeth": "becometh",
    "endeuoured": "endeavoured", "endeuouring": "endeavouring",
    "endeuours": "endeavours", "indeuoured": "endeavoured",
    "prentiships": "apprenticeships",
    "lamitations": "limitations",
    "perswade": "persuade", "perswaded": "persuaded",
    "perswading": "persuading", "perswasion": "persuasion",
    "perswasions": "persuasions", "diswade": "dissuade",
    "pretious": "precious", "pretiously": "preciously",
    "suspition": "suspicion", "suspitions": "suspicions",
    "obeysance": "obeisance", "countrey": "country",
    "countreys": "countries", "countries": "countries",
    "dammage": "damage", "dammages": "damages",
    "orphants": "orphans", "orphant": "orphan",
    "prentise": "prentice", "prentises": "prentices",
    "prentiship": "apprenticeship",
    "physicke": "physic", "physicion": "physician",
    "physicions": "physicians",
    # ("thorow" is "through" or "thorough" by context: left to the review)
    "thorowly": "thoroughly",
    "throughly": "thoroughly", "thorowout": "throughout",
    "releefe": "relief", "releeue": "relieve", "releeued": "relieved",
    "beleefe": "belief", "greefe": "grief", "greeues": "grieves",
    "cheefe": "chief", "cheefely": "chiefly", "breefe": "brief",
    "breefely": "briefly", "theefe": "thief", "theeues": "thieves",
    "eie": "eye", "eies": "eyes", "eied": "eyed",
    "sonne": "son", "sonnes": "sons", "onely": "only",
    "childe": "child", "kinde": "kind", "kindes": "kinds",
    "mankinde": "mankind", "behinde": "behind", "minde": "mind",
    "mindes": "minds", "finde": "find", "findes": "finds",
    "binde": "bind", "bindes": "binds", "blinde": "blind",
    "wilde": "wild", "milde": "mild", "mildely": "mildly",
    "olde": "old", "colde": "cold", "holde": "hold", "beholde": "behold",
    "golde": "gold", "worlde": "world", "woulde": "would",
    "bloud": "blood", "bloudy": "bloody", "bloudie": "bloody",
    "floud": "flood", "wisedome": "wisdom", "kingdome": "kingdom",
    "publike": "public", "publikely": "publicly", "publique": "public",
    "franticke": "frantic", "heretike": "heretic", "heretikes": "heretics",
    "politike": "politic", "schismatike": "schismatic",
    "domesticall": "domestic", "oeconomie": "economy",
    "oeconomicall": "economical",
    # -- in-/en- and im-/em- prefix variants -------------------------------
    "indanger": "endanger", "indangered": "endangered",
    "inforce": "enforce", "inforced": "enforced", "inforceth": "enforceth",
    "incourage": "encourage", "incouraged": "encouraged",
    "incouragement": "encouragement", "increase": "increase",
    "intreat": "entreat", "intreated": "entreated", "intreaty": "entreaty",
    "intise": "entice", "intised": "enticed", "inticeth": "enticeth",
    "inioy": "enjoy", "inioyed": "enjoyed", "inioyne": "enjoin",
    "inlarge": "enlarge", "inlarged": "enlarged",
    "intertain": "entertain", "intertained": "entertained",
    "intertainment": "entertainment", "intire": "entire",
    "intirely": "entirely", "intrest": "interest",
    "imployment": "employment", "imployed": "employed", "imploy": "employ",
    "impaire": "impair", "indeuour": "endeavour", "endeuour": "endeavour",
    # -- doubled/undoubled consonants and stray vowels ---------------------
    "threatning": "threatening", "threatned": "threatened",
    "threatneth": "threateneth", "threatnings": "threatenings",
    "rendred": "rendered", "rendring": "rendering",
    "entred": "entered", "entring": "entering",
    "remembred": "remembered", "remembring": "remembering",
    "gathred": "gathered", "suffred": "suffered", "offred": "offered",
    "ordred": "ordered", "ordring": "ordering", "wandring": "wandering",
    "tendring": "tendering", "hindring": "hindering",
    "considred": "considered", "deliuered": "delivered",
    "neere": "near", "neerer": "nearer", "neerest": "nearest",
    "neerely": "nearly", "neerenesse": "nearness",
    "cleere": "clear", "cleerely": "clearly", "cleered": "cleared",
    "meere": "mere", "meerely": "merely", "yeere": "year",
    "yeeres": "years", "yeerely": "yearly",
    "yeeld": "yield", "yeelded": "yielded", "yeeldeth": "yieldeth",
    "yeelding": "yielding", "yeelds": "yields",
    "seeke": "seek", "seeketh": "seeketh", "sixt": "sixth",
    "fift": "fifth", "fiftly": "fifthly", "moneth": "month",
    "moneths": "months", "yonger": "younger", "yongest": "youngest",
    "yong": "young", "wholsome": "wholesome", "loathsome": "loathsome",
    "carelesly": "carelessly", "expresly": "expressly",
    "expressely": "expressly", "solemnely": "solemnly",
    "infinitly": "infinitely", "erroniously": "erroneously",
    "alwaies": "always", "alway": "always", "adaies": "adays",
    "eies": "eyes", "saies": "says", "waies": "ways", "wayes": "ways",
    "daies": "days", "praier": "prayer", "praiers": "prayers",
    "praying": "praying", "raiment": "raiment",
    "auncient": "ancient", "apparant": "apparent",
    "apparantly": "apparently", "battell": "battle", "cattell": "cattle",
    "cariage": "carriage", "cariages": "carriages",
    "mariage": "marriage", "mariages": "marriages",
    "mariageable": "marriageable", "maried": "married",
    "marie": "marry", "mary": "marry", "marying": "marrying",
    "vnmaried": "unmarried", "housholder": "householder",
    "houshold": "household", "housholds": "households",
    "schoolemaster": "schoolmaster", "schoolemasters": "schoolmasters",
    "schoolemen": "schoolmen", "kinred": "kindred", "kinne": "kin",
    "hinderance": "hindrance", "recompence": "recompense",
    "commandement": "commandment", "commandements": "commandments",
    "acknowledgement": "acknowledgment", "alledge": "allege",
    "alledged": "alleged", "alledgeth": "allegeth", "alleaged": "alleged",
    "affoord": "afford", "boords": "boards", "foorth": "forth",
    "goe": "go", "doe": "do", "loe": "lo", "hee": "he", "mee": "me",
    "shee": "she", "yee": "ye", "wee": "we", "bee": "be",
    "farre": "far", "sute": "suit", "sutable": "suitable",
    "chuse": "choose", "chusing": "choosing", "choise": "choice",
    "choyce": "choice", "chast": "chaste", "hainous": "heinous",
    "haruest": "harvest", "harted": "hearted", "earely": "early",
    "trueth": "truth", "vertue": "virtue", "vertues": "virtues",
    "vertuous": "virtuous", "villanie": "villainy",
    "souldier": "soldier", "souldiers": "soldiers",
    "cloathed": "clothed", "cloathes": "clothes", "swadling": "swaddling",
    "prophane": "profane", "prophaned": "profaned",
    "prophanesse": "profaneness", "tearme": "term", "tearmes": "terms",
    "authoritie": "authority", "autoritie": "authority",
    "controuersie": "controversy", "ministerie": "ministry",
    "councell": "council", "counsell": "counsel",
    "errour": "error", "errours": "errors",
    "inferiour": "inferior", "inferiours": "inferiors",
    "superiour": "superior", "superiours": "superiors",
    "emperour": "emperor", "emperours": "emperors",
    "instructer": "instructor", "gouernour": "governor",
    "gouernours": "governors",
    # -- words a shorter form of which is a real word (oracle traps) -------
    "diuell": "devil", "diuels": "devils", "diuellish": "devilish",
    "euill": "evil", "euils": "evils", "euillest": "evillest",
    # -- truncations the transcription left behind -------------------------
    "shal": "shall", "wil": "will", "wel": "well", "al": "all",
    "ful": "full", "til": "till", "vntill": "until", "vntil": "until",
    "wherby": "whereby", "wherfore": "wherefore", "wherin": "wherein",
    "wherof": "whereof", "wheron": "whereon", "therfore": "therefore",
    "therof": "thereof", "therin": "therein", "therunto": "thereunto",
    "therupon": "thereupon", "heerein": "herein", "heere": "here",
    "heerof": "hereof", "heereafter": "hereafter",

    # -- from the Perkins and Simon Magus reviews (shared table) --------
    "approoue": "approve", "approoued": "approved", "approoueth": "approves",
    "approueth": "approves",
    "oeconom": "oecon",  # bibliographic abbreviation, leave inert
    "folkes": "folks",
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
    # un- prefixed forms needing a final-letter/doubling fix beyond u/v
    "vnfeined": "unfeigned", "vncertaine": "uncertain", "vnchast": "unchaste",
    "vnckle": "uncle", "vncleane": "unclean", "vncleannes": "uncleanness",
    "vncleannesse": "uncleanness", "vncomlie": "uncomely",
    "vndergoe": "undergo", "vnequall": "unequal", "vniuersall": "universal",
    "vniust": "unjust", "vnknowne": "unknown", "vnlawfull": "unlawful",
    "vnfitlie": "unfitly",
    # (un-/in-) are intentionally left untouched -- see DO_NOT_TOUCH.
    "vsurpe": "usurp", "preuaile": "prevail",
    "gouerne": "govern", "gouernement": "government",
    "gouernements": "governments",
    "gouerned": "governed",
    "cell": "cell",
    "auaileable": "available",
    "ciuill": "civil",
    "festiuall": "festival",
    "seuerall": "several",
    "soueraigne": "sovereign", "soueraigntie": "sovereignty",
    "vngratious": "ungracious",
    "trauell": "travel",
    "iesuites": "jesuits",
    "scie": "scie",  # OCR-split remnant, leave inert
    "waightie": "weighty", "waightiest": "weightiest",
    # (different suffix, or an extra letter elsewhere in the root)
    "mosaicall": "mosaic",
    "aristocraticall": "aristocratic",
    "fruitefull": "fruitful",
    "reprochfull": "reproachful", "reproch": "reproach",
    "reprocheth": "reproacheth",
    # doubled-consonant-before-suffix strays
    "begunne": "begun",
    "buffetted": "buffeted", "ransommed": "ransomed",
    "befals": "befalls",
    # miscellaneous silent-e / vowel / missing-letter strays
    "braule": "brawl", "brethen": "brethren",
    "cattel": "cattle",
    "busines": "business",
    "furtherer": "furtherer",
    "encreased": "increased",
    "otherside": "otherwise",
    "cozin": "cousin",
    "swadled": "swaddled",
    "rayment": "raiment",
    "defence": "defence", "offence": "offence",
    "deflowred": "deflowered",
    "extreames": "extremes",
    "neece": "niece", "neeces": "nieces",
    "vessell": "vessel",
    "starres": "stars",
    "stroks": "strokes",
    "fal": "fall", "willt": "wilt",
    "woma": "woman", "husba": "husband",
    "mand": "manned", "manded": "manned", "mandement": "mandment",
    "manchild": "manchild",
    "obiect": "object", "obiected": "objected",
    "reiect": "reject", "reiected": "rejected", "reiecteth": "rejecteth",
    "reiection": "rejection", "reioicing": "rejoicing",
    "enioy": "enjoy", "enioyeth": "enjoyeth",
    "coniectures": "conjectures",
    "subiect": "subject", "subiection": "subjection",
    "growen": "grown",
    "neighbour": "neighbour",
    "infidell": "infidel",
    "dimme": "dim", "madde": "mad", "bedde": "bed",
    "hebrewesse": "hebrewess",
    "carelessely": "carelessly",
    "queene": "queen",
    "rammes": "rams", "sinne": "sin", "sinnest": "sinnest",
    "sinneth": "sinneth",
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
    # remaining silent-e / doubled-letter / missing-letter strays
    "harmelesse": "harmless",
    "eleuenth": "eleventh",
    "wooll": "wool",
    "nearenesse": "nearness",
    "waightie": "weighty", "weightie": "weighty",
    "fourefold": "fourfold",
    "warth": "wrath",
    "themselues": "themselves", "selues": "selves",
    "mixt": "mixed", "queene": "queen", "siluer": "silver",
    "vncapable": "uncapable", "vncurable": "uncurable",
    "svrvey": "survey",
    "heer": "here",
    "solemne": "solemn",
    "condemne": "condemn", "condemned": "condemned",
    "hymne": "hymn", "colume": "column",
    # source/review-report.md): words the rules above missed or mangled.
    "bin": "been",
    "sunne": "sun",
    "lawes": "laws", "reade": "read",
    "maner": "manner", "hindred": "hindered",
    "aule": "awl",  # ("vaile": veil or vail, by context)
    "commaund": "command",
    "concurre": "concur", "incurre": "incur",
    "disswadeth": "dissuadeth", "entise": "entice", "liew": "lieu",
    "mourne": "mourn", "oxe": "ox", "oyle": "oil",
    "paiment": "payment", "premisses": "premises", "rodde": "rod",
    "saluation": "salvation", "soiourne": "sojourn",
    "soiourners": "sojourners", "sundrie": "sundry", "waite": "wait",
    "heards": "herds", "conquerer": "conqueror", "directer": "director",
    # the doubled-consonant rule wrongly strips these; leave them inert
    "abhorreth": "abhorreth", "flitteth": "flitteth",
    # book-name abbreviation in citations
    "prou": "prov",
    # KJV forms of proper names
    "philistims": "philistines", "thare": "terah",
    "sampson": "samson", "abimelek": "abimelech",
    "acsah": "achsah", "ester": "esther", "nachor": "nahor",
    "bethlem": "bethlehem",
    # TCP transcription slips (not period spellings)
    "aud": "and", "chiece": "chief", "childred": "children",
    "contimencie": "continency", "nenessitie": "necessity",
    "rpented": "repented", "thid": "third", "estraineth": "restraineth",
}

_ARCHAIC_SUFFIXES = ("eth", "est")
_VOWELS = "aeiouy"


def _dict_known(word):
    return word in _SPELL


def _freq(word):
    return _SPELL.word_frequency.dictionary.get(word, 0)


# ---------------------------------------------------------------------------
# Mechanical rules
# ---------------------------------------------------------------------------

def _fix_u_v(word):
    """The unambiguous half of the u/v problem: an initial "v" before a
    consonant is the vowel u (vnto -> unto), and a "u" between two vowels is
    the consonant v (loue -> love).  Iterated, because fixing one can create
    the pattern for another (vniuersall)."""
    word = re.sub(r"^v(?=[bcdfghjklmnpqrstwxz])", "u", word)
    prev = None
    while prev != word:
        prev = word
        word = re.sub(r"(?<=[aeiouy])u(?=[aeiouy])", "v", word)
    return word


def _fix_i_j(word):
    """Initial "i" before a vowel is the consonant j (iustice -> justice)."""
    return re.sub(r"^i(?=[aeou])", "j", word)


def _fix_suffixes(word):
    if word.endswith("sse") and len(word) > 4:      # -nesse -> -ness
        return word[:-1]
    if word.endswith("ie") and len(word) > 3:       # familie -> family
        return word[:-2] + "y"
    return word


def _silent_e_candidates(word):
    """Modern forms this word might be an Early Modern spelling of, given the
    usual habits: a superfluous final e, a doubled final consonant, a missing
    one, or -icke for -ic.  Ordered most-likely first; the caller takes the
    first the dictionary recognises, so a real modern word is never touched."""
    out = []
    if word.endswith("e") and len(word) > 3:
        out.append(word[:-1])                       # looke -> look
        if len(word) > 4 and word[-2] == word[-3]:
            out.append(word[:-2])                   # stirre -> stir
    if word.endswith("es") and len(word) > 4:
        out.append(word[:-2] + "s")                 # goates -> goats
        if len(word) > 5 and word[-3] == word[-4]:
            out.append(word[:-3] + "s")             # sinnes -> sins
    for pair in ("ll", "ff", "mm", "nn", "pp", "tt", "rr", "ss"):
        if word.endswith(pair) and len(word) > 4:
            out.append(word[:-1])                   # generall -> general
    if word.endswith("nes") and len(word) > 4:
        out.append(word + "s")                      # busines -> business
    if word.endswith("cke") and len(word) > 4:
        out.append(word[:-2] + "c")                 # physicke -> physic
    # -nesse has already lost its final e by the time we get here, but the
    # stem in front of it is often still Early Modern: "weakenesse" ->
    # "weakeness" needs the linking e dropped, "carelesnesse" ->
    # "carelesness" needs the doubled s restored.
    if word.endswith("eness") and len(word) > 6:
        out.append(word[:-5] + "ness")              # weakeness -> weakness
    if word.endswith("sness") and len(word) > 6:
        out.append(word[:-5] + "ssness")            # carelesness -> carelessness
    return out


def _fix_silent_e(word):
    if _dict_known(word):
        return word
    for c in _silent_e_candidates(word):
        if _dict_known(c):
            return c
    return word


# ---------------------------------------------------------------------------
# The letterform oracle
# ---------------------------------------------------------------------------

# In 1622 u/v were one letter and i/j were one letter, so all four
# substitutions are in play: the transcription's "VVJsdome" is "Wisdom", and
# "iustice" is "justice".
_SWAPS = {"u": "v", "v": "u", "i": "j", "j": "i"}
_MAX_SWAP_POSITIONS = 7


def _oracle_letterforms(word):
    """u/v and i/j were positional variants of one letter in 1622, not
    different letters, so the modern form is recoverable by search rather than
    by rule: swap them and see which variant the dictionary knows.

    Breadth-first by number of swaps, so the smallest change wins; among
    equally small changes the commonest modern word wins.  Each candidate is
    also run through the silent-e rules, since a word usually needs both
    ("obserue" -> "observe", "aduersitie" -> "adversity").

    Returns None if nothing recognisable turns up, which is the common case
    for proper names and Latin -- hence "leave it alone" rather than "guess".
    """
    positions = [i for i, ch in enumerate(word) if ch in _SWAPS]
    if not positions or len(positions) > _MAX_SWAP_POSITIONS:
        return None
    frontier = {word}
    seen = {word}
    for _ in range(len(positions)):
        nxt = set()
        for w in frontier:
            for i in positions:
                if w[i] not in _SWAPS:
                    continue
                cand = w[:i] + _SWAPS[w[i]] + w[i + 1:]
                if cand not in seen:
                    seen.add(cand)
                    nxt.add(cand)
        hits = []
        for cand in nxt:
            for form in (cand, _fix_silent_e(_fix_suffixes(cand))):
                if _dict_known(form):
                    hits.append(form)
        if hits:
            return max(hits, key=_freq)
        frontier = nxt
    return None


# ---------------------------------------------------------------------------

def _fix_archaic_verb_root(word):
    """-eth/-est is kept on purpose (it is a verb form, not a spelling), but
    the root in front of it still needs modernizing: yeeldeth -> yieldeth."""
    for suf in _ARCHAIC_SUFFIXES:
        if word.endswith(suf) and len(word) > len(suf) + 2:
            root = word[:-len(suf)]
            if root in GRAMMAR_EXCEPTIONS or root in LATIN_SKIP or root in DO_NOT_TOUCH:
                continue
            new_root = MANUAL.get(root)
            if new_root is None:
                r = _fix_silent_e(_fix_i_j(_fix_u_v(root)))
                if not _dict_known(r):
                    r = _oracle_letterforms(r) or r
                new_root = r
            if new_root != root:
                return new_root + suf
    return word


def modernize_word_lower(word):
    """Modernize one lowercase word.  Returns the modern spelling, or the
    word unchanged when no rule applies (proper names, Latin, and anything
    the dictionary cannot vouch for are left alone rather than guessed at)."""
    if word in GRAMMAR_EXCEPTIONS or word in LATIN_SKIP:
        return word
    # a table entry is a decision about that exact word, so it wins over
    # DO_NOT_TOUCH, which only guards the rules (Prou -> Prov, Iob -> Job)
    if word in NAMES:
        return NAMES[word]
    if word in MANUAL:
        return MANUAL[word]
    if word in DO_NOT_TOUCH:
        return word

    new = _fix_silent_e(_fix_suffixes(_fix_i_j(_fix_u_v(word))))
    if not _dict_known(new):
        new = _oracle_letterforms(new) or new
    if new == word:
        new = _fix_archaic_verb_root(word)
    return new


def apply_case_pattern(original, modern_lower):
    """Re-apply the original word's capitalization to a new spelling:
    ALLCAPS -> ALLCAPS, Titlecase -> Titlecase, else as given.  NAMES entries
    already carry their own capital, so a name keeps it."""
    if original.isupper() and len(original) > 1:
        return modern_lower.upper()
    if original[:1].isupper():
        return modern_lower[:1].upper() + modern_lower[1:]
    return modern_lower
