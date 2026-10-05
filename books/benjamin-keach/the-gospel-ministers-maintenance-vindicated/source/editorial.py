"""
Editorial tables for The Gospel Minister's Maintenance Vindicated (London:
John Harris, 1689; Wing K711A; EEBO-TCP A47561, untouched in
A47561.tcp.xml). Read by build_tei.py, tei_extract.py, tcp_structure.py and
./fgb.

Catalogued (Wing, TCP) under Hanserd Knollys, whose name heads the eleven
elders signing the recommendation; the treatise is Benjamin Keach's, and
this edition gives it to him (the foreword says why). Page images: the
same microfilm on archive.org,
bim_early-english-books-1641-1700_the-gospel-ministers-ma_knollys-hanserd_1689
(scan index = printed page + 13).
"""

import runpy
from pathlib import Path

import layout

T = "{http://www.tei-c.org/ns/1.0}"

AUTHOR = ("Keach, Benjamin, 1640-1704.",
          "This edition attributes the treatise to Benjamin Keach. Wing and "
          "EEBO-TCP catalogue it under Hanserd Knollys, the first of the eleven "
          "elders who signed its recommendation (Keach among them).")

FILES = [("chapter-01.typ", "A Regular Ministry in the Church Asserted"),
         ("chapter-02.typ", "The Gospel Minister’s Maintenance Vindicated"),
         ("chapter-03.typ", "Motives to Press the Duty of the Minister’s Maintenance, "
                            "with an Answer to Other Objections"),
         ("chapter-04.typ", "The Great and Weighty Work of a True Gospel Minister Opened")]
SHORT = [None, "The Minister’s Maintenance Vindicated", "Motives to Press the Duty",
         "The Work of a Gospel Minister"]


def LAYOUT(root):
    """The elders' recommendation (its printed address and greeting set under
    the title), then the four sections of the treatise, one file each."""
    by = {}
    for d in layout.top_divs(root):
        by.setdefault(d.get("type"), []).append(d)
    rec = by["to_the_reader"][0]
    files = [{"file": "recommendation.typ", "title": "Recommendation",
              "subtitle": rec.find(f"{T}head"), "parts": layout.sections(rec)}]
    for (f, t), s, d in zip(FILES, SHORT, by["section"]):
        parts = [x for x in layout.sections(d) if x not in _duplicates(root)]
        files.append({"file": f, "title": t, "short": s, "parts": parts})
    return files


def _duplicates(root):
    return root.findall(f".//{T}body//{T}gap[@reason='duplicate']")


def SKIP_BLOCKS(root):
    """Pages 110-111 were photographed twice on the microfilm; the TCP marks
    the second copy as a gap. Nothing is missing."""
    return _duplicates(root)


# The title page, the errata (applied in the text as editor emendations), the
# printed contents (1689 page numbers) and the Advertisement on the 38th
# Article are not part of this edition; they stay in the TEI as printed.
SKIP_DIVISIONS = {"title_page", "errata", "table_of_contents", "notice"}

# Illegible print: every gap in the edition's text filled (see gap_fixes.py).
GAP_FIXES = runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

TYPST_ENUM = None

REPORT_NOTES = [
    "The recommendation is dated 'July, 30. 1681.' as printed, eight years "
    "before the book (1689); left as printed.",
]

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "The Gospel Minister’s Maintenance Vindicated", "author": "Benjamin Keach",
        "file": "the-gospel-ministers-maintenance-vindicated.epub",
        "front": "ebook-front.html", "cover": "cover.typ",
        "before": ["chapters/typ/foreword.typ"],
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["the-gospel-ministers-maintenance-vindicated.typ"]
COVERS = ["cover.typ"]
SIDE_BY_SIDE = {"before": ["chapters/typ/foreword.typ"]}
QUOTE_BLOCK = True


# "WE have read" under a decorated initial is set "We have read".
DROP_CAP_CASE = True


# The 1689 printing capitalizes most nouns, many adjectives and some other
# words mid-sentence; the edition lowercases them, as the other books on the
# shelf do. Kept capital (not listed): God, Christ, Lord, Jesus, Spirit,
# Scripture, Saviour, names, books of the Bible, and words that are sometimes
# divine or a name (Father, Son, King, Mark, New, Lamb, Acts), settled by hand.
LOWERCASE_COMMON_NOUNS = set("""
    abilities ability able abrogated accomplishment accomplishments
    according account accountable accounts act administer adorn
    adorning advantages affairs affection afflicting afflictions after age
    agent ages aid alas all allowance altar alter ambassador ambassadors an
    ancient and angel angels annotators annum answer answered apostle
    apostles apparel appeal application applications appointed appointment
    archers are argument arguments armour army art artist as ascension ashes
    assert assistance author authorities authority bag baptized bargain
    battle be beasts beautify because beds being believe believers benefit
    besides bishop bishops blamelessly bless blessed blessing blessings
    blind blood blots bodies bodily body boldness bonds book books bountiful
    brass bread brethren brethren's bring builders buildings burden burdens
    burthens business but by call calling callings calls can canons capacity
    captain carcass care careful careless cares carnal case cats cause
    ceiled certainly chains charge chargeable charges charity children
    choice church churches circumstance circumstances city clothes clouds
    coats coherence comfort comfortable comforts coming command commanded
    commandment commandments commands commendable commerce commission common
    communicate communicating communication communion compensation conceit
    concerns conclusions condition confess confirm confirmation congregation
    congregations connection conscience consciences consequences consider
    consideration considered considering continuation contradictions
    controversy conversion copper corn cost counsel country course covenant
    covenanted covetous covetousness creature credit crown cry curious curse
    damnation danger dangers daughter daughters day deacons death debt
    debtors defect defence delights deliverance demonstration dependence
    design desire desires destruction detriment devoted did die difficulty
    dignity diligence diligent direction disappointments discharge disciples
    discouragements discourse discovered dishonour dispensation disputings
    disquieting distress distribute divine do doctrine doings door doors
    doth dread drink dross due dues duties duty ear earn ears earth earthly
    eat eats edification edifying effects either elder elders election
    embodied employed employeth employment employments empowered encourage
    encouragement encumbrances end endowments ends enemy enlightened
    ensnarements epistles equitableness equity error especially essence
    estates esteem eternal even evil evils evince exactness example excuse
    excuses exercise exhortation exhortations expectation expediment expense
    experience experiences eyes face faces faith faithful faithfulness false
    families family farmers fastings fathers fault favour fear fears fed
    feed feedeth fellow fellowship field fields fifth first flax fled flesh
    flock flocks flood flourishing fold food fool foolishness for form
    foundation frailties freedom friends fruit fruits function further
    garnish gift gifts glass glorified glorious glory go godliness godly
    gold goldsmith good goodness goods gospel govern grace graces gracious
    graciously grand graves great greatness grief grievous ground grounds
    grudge guides guilt hand hands happiness harvest hath have he heads
    health heart hearts hearty heathen heathens heave heaven heavenly
    heavens her heretics high him himself hire his holes holiness holy
    honest honorable honorur honour honourable honourableness hope
    hospitality hosts hour hours house houses how humane hundred hunger
    husband hypocrites idle idolatry idols if ignorance ignorant immortal
    implacable import improve improvement improving in incarnation
    inconveniences increase indispensable industry infamy infidel infinite
    infirmities influence inhabitants inherit inheritance iniquity instances
    institute institution institutions instruction instruments insufficiency
    intention interest interests intrusted inventions investiture invocation
    is it its jingling journey joy jubilee judge judgment judgments just
    justice justification justly justness kindom kindred kingdom know
    knowledge labor laborious laboriousness labour laboured labourer
    labourers labours lamentable land lands law laws lay laying learning
    left legacies less let liberal liberty life light likewise line lists
    live livelihood lively lives living loss losses lot love lovely lucre's
    lust lusts maim maintenance majesty man management manifest mans many
    marry master masters matchless materials matter matters may meat
    mediation mediator meditation meet meeting members men men's mercies
    mercy merits messengers metaphors miles militant military milk mind
    minds minister ministered ministerial ministering ministers ministration
    ministry miracles miseries mission mistake money moral moreover most
    mother motives mountain mourning mouth mouths muzzle mysteries
    mysterious mystery mystical nakedness name named names nation national
    nations nativity natural nature nay necessary necessities necessity
    needy negative neglect negligent neighbouring night no none nor nostrils
    noteth nourishment now obedience obediential object objection objections
    oblation obligation obligations obstructions occasion offender offering
    offerings office officers offices oil old omission omissions one ones
    opinion opposers opposition oppositions oppression or ordain ordained
    order ordered ordinance ordinances ordination organical ornaments ought
    our ox oxen painful pains parents part parts party passion pastor
    pastoral pastors pattern pay peace pearl peculiar people people's
    perfection persecution persecutors person persons persuasion physician
    pillar piously place places plant planters planteth planting plants plea
    plead pleasure plow ploweth point poor portion portions positive
    possessions pounds poverty power powers practice praise pray prayer
    prayers preach preached preacher preachers preaches preaching precept
    precepts precious prejudice presbytery prevention priest priesthood
    priests prince principles prisoners privileges profession professors
    profit promulgation proof property prophet propriety prove proverb
    provide providence providences provision prudence public pulpit pure
    pureness purses qualifications quarterly question raiment read reading
    reap reaped reason reasons rebellious rebuke reference reformation
    regular relations release religion religious remember remiss remissness
    repent repentance report reproach reproaches reputation requirement
    requires respect resurrection revenues reverence reverend reward rich
    riches right righteousness rite room ruin rule rulers rules run sabbaths
    sacraments sacred sacrifice sacrilege safety saint saints sake salvation
    sanction sanctuary savour scandal scope scrip season second secondly
    secular see seek seers self selves send sense senses sentences serious
    sermon sermons servant servants serve service seventy shall shame she
    sheep shepherd shepherds shoes silver sin since sincerity singers
    sinners sins sister sitting skill sleeps slothful snare snares so
    societies soldier soldiers solemnity solicitous sons sorrow soul souls
    sovereign sow soweth sown speech spent sphere spirits spiritual
    spirituals spoils spring stains stars state station statutes staves
    steps stewards stones store stores storm storms strange strength
    strengthen studies study sublime subsistence substance success such
    suffering sufferings suffrages sumptuous superfluities support sure
    surely take teach teacher teachers teacheth tears temper temple temporal
    temporals temptation temptations ten tenderness tenth tenths term terms
    testimony text that the then there therefore they thing things this tho
    thorny thou thoughts thousand threats three thresheth throne time times
    tithe tithes to tongue tongues town towns tract trade trades tradesman
    trading traditions treadeth treasure treasuries treatise trembling trial
    tribe true trust truth truths turst twelve twentieth two unbelieving
    understanding understandings undertaking unfitness ungodly universal
    unlawful unless unspeakable unworthiness use useful uses vain vengeance
    verse villages vineyard virtue virtues visible visiting voice wages walk
    war warfare warrant warreth watch watchings watchman watchmen water way
    ways we weak weakness weaknesses wealthy weather week weigh weightiness
    well what when where wherefore which whilst who why wife will
    willfulness willing windows wine wisdom with without witness wives wolf
    women wool word wordly words work workers working workman works world
    worldly worlds worm worship worth worthy would wrath write writer
    written year yearly years yeomen yet you young zeal zealous
""".split()) | {"minister's", "man's", "men's", "watchman's", "liv'd", "consider'd",
                  "baptiz'd"}
# ...but the first word of an italic quotation keeps its capital.
QUOTE_START_CASE = True

# Old spellings the shared table does not know, and possessives printed
# without an apostrophe (Mens, Christs, Lords, Peoples).
SPELLING = {
    "abilitys": "abilities", "abillities": "abilities", "allways": "always",
    "ambassadours": "ambassadors", "ascention": "ascension", "carryed":
    "carried", "carcase": "carcass", "comparitively": "comparatively",
    "connextion": "connection", "cumbred": "cumbered", "denyed": "denied",
    "dilligence": "diligence", "dilligent": "diligent", "discribed":
    "described", "dispenced": "dispensed", "divest": "divest", "dutys":
    "duties", "expence": "expense", "extreamly": "extremely", "grudg":
    "grudge", "hardning": "hardening", "hereticks": "heretics", "holyness":
    "holiness", "idlely": "idly", "imbodied": "embodied", "imbrace":
    "embrace", "imploying": "employing", "imployments": "employments",
    "impowered": "empowered", "inconveniencies": "inconveniences",
    "incouragment": "encouragement", "incumbrances": "encumbrances",
    "incumbred": "encumbered", "indeavour": "endeavour", "indeavoured":
    "endeavoured", "indispencible": "indispensable", "indispensible":
    "indispensable", "indowed": "endowed", "indowments": "endowments",
    "indure": "endure", "ingaged": "engaged", "injoyn": "enjoin",
    "injoyned": "enjoined", "inlightened": "enlightened", "inrich":
    "enrich", "inriching": "enriching", "insnarements": "ensnarements",
    "intangle": "entangle", "intangled": "entangled", "intangleth":
    "entangleth", "joyn": "join", "knowledg": "knowledge", "labouriousness":
    "laboriousness", "labourous": "laborious", "livelyhood": "livelihood",
    "loosers": "losers", "lyable": "liable", "lyes": "lies", "lyeth":
    "lieth", "lye": "lie", "dye": "die", "meer": "mere", "meerly": "merely",
    "millitant": "militant", "oftner": "oftener", "ommission": "omission",
    "ordaination": "ordination", "ordaine": "ordain", "oyl": "oil",
    "patern": "pattern", "persue": "pursue", "preceeds": "precedes",
    "priviledges": "privileges", "prophanely": "profanely", "publick":
    "public", "publickly": "publicly", "recal": "recall", "rejoyce":
    "rejoice", "sacriledg": "sacrilege", "sence": "sense", "sensured":
    "censured", "sequestred": "sequestered", "sollicitous": "solicitous",
    "soveraign": "sovereign", "strangly": "strangely", "subjoyned":
    "subjoined", "subsistance": "subsistence", "supplyed": "supplied",
    "tryal": "trial", "tythes": "tithes", "uncapable": "incapable",
    "unsensible": "insensible", "wellfare": "welfare", "niggerly":
    "niggardly", "thrasheth": "thresheth", "dependance": "dependence",
    "brethrens": "brethren's", "mens": "men's", "christs": "Christ's",
    # an apostrophe opening a word is set as one (Typst would curl a
    # straight one after a space into an opening quote: ‘tis)
    "'tis": "’tis", "'twas": "’twas", "'twill": "’twill",
    "obj": "obj",  # the letterform search made these "Obi", "diuest"
    "lords": "Lord's", "peoples": "people's", "lucres": "lucre's",
}

# "&c." is written "etc.", as on the rest of the shelf.
EXPAND_ETC = True
# A sentence that opens after an italic quotation is capitalized
# ("... elders in every church.] So the apostle").
ITALIC_SENTENCE_QUIRK = False
