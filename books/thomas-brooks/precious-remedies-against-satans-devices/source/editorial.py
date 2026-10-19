"""
Editorial tables for Thomas Brooks, Precious Remedies against Satans Devices
(London: M. Simmons for John Hancock, 1653, "The Second Edition Corrected
and Enlarged"; Wing B4954; EEBO-TCP A77614, untouched in A77614.tcp.xml;
the TCP header's edition date, 1658, is not the imprint's). Read by
build_tei.py, tei_extract.py, tcp_structure.py and ./fgb.

Witness: Monergism's PDF (from Grosart's Works of Thomas Brooks, vol. 1;
a check only, its text is not used).
"""

import layout

T = "{http://www.tei-c.org/ns/1.0}"

SIN = ["Presenting the Bait and Hiding the Hook",
       "Painting Sin with Virtue’s Colours",
       "Lessening Sin",
       "The Best Men’s Sins",
       "God as All Mercy",
       "Repentance Made Easy",
       "The Occasions of Sin",
       "The Outward Mercies of Vain Men",
       "The Crosses of the Saints",
       "Comparing Ourselves with Worse Men",
       "Error in the Judgment",
       "Wicked Company"]
DUTIES = ["The World in Its Best Dress",
          "The Dangers of Duty",
          "The Difficulty of Duty",
          "False Inferences from Christ’s Work",
          "The Fewness and Poverty of the Godly",
          "The Example of the World",
          "Vain Thoughts in Duty",
          "Resting in Performances"]
DOUBTING = ["Poring on Sin More than on the Saviour",
            "False Definitions of Grace",
            "Cross Providences",
            "Counterfeit Graces",
            "Conflict as in Hypocrites",
            "Lost Joy",
            "Relapses",
            "Temptations"]
RANKS = ["The Great: Self-Seeking",
         "The Great: Against the Saints",
         "The Learned and the Wise",
         "The Saints: Division",
         "The Ignorant"]
APPENDIX = ["The Greatness of Sin",
            "Unworthiness",
            "Want of Preparation",
            "Christ’s Unwillingness",
            "God’s Secret Decrees"]
PARTS = ["Part I. Devices to Draw the Soul into Sin",
         "Part II. Devices to Keep Souls from Holy Duties",
         "Part III. Devices to Keep Souls Doubting",
         "Part IV. Devices to Destroy All Ranks of Men",
         "Appendix. Five More Devices to Keep Souls from Christ"]


def _printed(el):
    """The printed text of an element: readings of the edition and margin
    notes left out."""
    out = [el.text or ""]
    for c in el:
        if isinstance(c.tag, str) and layout.local(c) not in ("reg", "expan", "note"):
            out.append(_printed(c))
        out.append(c.tail or "")
    return "".join(out)


def _text(el):
    """Printed text, long s as s and lower case, for matching."""
    return " ".join(_printed(el).replace("ſ", "s").split()).lower()


def _flat(div):
    """A division's blocks in reading order, its sub-divisions opened: each
    sub-division's printed head (a part of its own) and then its blocks.
    The division's own head is left to the caller."""
    out = []
    for c in div:
        if not isinstance(c.tag, str) or layout.local(c) in ("pb", "milestone"):
            continue
        if layout.local(c) == "head":
            continue
        if layout.local(c) == "div":
            out += c.findall(T + "head") + _flat(c)
        else:
            out.append(c)
    return out


def _cuts(blocks, starts):
    """Cut `blocks` before the first block (after the previous cut) whose
    printed text starts with each of `starts`: [before, file 1, file 2, ...]
    (cut by text, not position)."""
    out, k = [], 0
    for s in starts:
        j = next(i for i in range(k, len(blocks)) if _text(blocks[i]).startswith(s.lower()))
        out.append(blocks[k:j])
        k = j
    out.append(blocks[k:])
    return out


ORD = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
       "eighth"]


def LAYOUT(root):
    """The epistle dedicatory; To the Reader; the text opened and the point
    proved; the devices of the four parts and of the appendix, one file each
    (the device as printed, then its remedies); the propositions, the reasons
    and the use. In Part I each device is printed at the end of the division
    before it, so files are cut by printed text, the printed heads of the
    divisions ("Now the Remedies against this Device ...") kept as parts."""
    by = {}
    for d in layout.top_divs(root):
        by.setdefault(d.get("type"), []).append(d)
    p1, p2, p3, p4 = by["part"]
    app = by["appendix"][0]
    files = [{"file": "dedication.typ", "title": "The Epistle Dedicatory",
              "parts": layout.sections(by["dedication"][0])},
             {"file": "to-the-reader.typ", "title": "A Word to the Reader",
              "parts": layout.sections(by["to_the_reader"][0])}]

    # Part I: the text opened, then "Now the second thing ... his several
    # Devices"; each device opens "His first Device", "The second Device ...".
    b1 = _flat(p1)
    intro, *rest = _cuts(b1, ["Now the second thing that I am to shew you"])
    files.append({"file": "introduction.typ",
                  "title": "The Text Opened and the Point Proved",
                  "subtitle": p1.find(T + "head"), "parts": intro})
    lead, *sin = _cuts(rest[0], ["His first Device", "The second Device", "The third Device",
                                 "The fourth Device", "The fifth Device", "The sixt Device",
                                 "Now the seventh Device", "The eight Device",
                                 "The ninth Device", "The tenth Device",
                                 "The eleventh Device", "The twel"])
    sin[0] = lead + sin[0]
    for i, parts in enumerate(sin):
        files.append({"file": f"sin-{i + 1:02d}.typ", "title": f"{i + 1}. {SIN[i]}",
                      "parts": parts, "part": PARTS[0] if i == 0 else None})

    def part(div, names, stem, k, starts, subtitle=True):
        lead, *fs = _cuts(_flat(div), starts)
        fs[0] = lead + fs[0]
        out = []
        for i, parts in enumerate(fs):
            out.append({"file": f"{stem}-{i + 1:02d}.typ", "title": f"{i + 1}. {names[i]}",
                        "subtitle": div.find(T + "head") if i == 0 and subtitle else None,
                        "parts": parts, "part": PARTS[k] if i == 0 else None})
        return out

    files += part(p2, DUTIES, "duties", 1,
                  [f"The {ORD[i]} Device" for i in range(8)])
    files += part(p3, DOUBTING, "doubting", 2,
                  [f"The {ORD[i]} Device" for i in range(8)])
    b4 = _flat(p4)
    ranks, closing = _cuts(b4, ["And now to prevent Objections"])
    lead, *rk = _cuts(ranks, ["His first Device", "The second Device", "Secondly, Satan",
                              "Thirdly, Satan", "Lastly, as Satan"])
    rk[0] = lead + rk[0]
    for i, parts in enumerate(rk):
        files.append({"file": f"ranks-{i + 1:02d}.typ", "title": f"{i + 1}. {RANKS[i]}",
                      "subtitle": p4.find(T + "head") if i == 0 else None,
                      "parts": parts, "part": PARTS[3] if i == 0 else None})
    props, reasons, use = _cuts(closing, ["Now I shall come to the Reasons",
                                          "The use of the Point"])
    files += [{"file": "propositions.typ", "title": "Six Propositions Concerning Satan",
               "parts": props},
              {"file": "reasons.typ", "title": "The Reasons of the Point", "parts": reasons},
              {"file": "use.typ", "title": "The Use: Ten Helps Against All His Devices",
               "parts": use}]
    files += part(app, APPENDIX, "appendix", 4,
                  ["Now the first Device"] + [f"The {ORD[i]} Device" for i in range(1, 5)])
    return files


# Not part of this edition (kept in the TEI as printed): the title page, the
# printed table of contents (1653 page numbers), Caryll's imprimatur, the
# bookseller's catalogue and the errata.
SKIP_DIVISIONS = {"title_page", "table_of_contents", "imprimatur",
                  "publishers_advertisement", "errata"}

# A device or remedy head ("Now the Remedies against this Device of Satan
# are these.") is set as a bold paragraph, not a heading.
RUN_IN_DIVS = {"subpart"}

TYPST_ENUM = None

REPORT_NOTES = [
    "The title page, the printed table of contents, the imprimatur, the "
    "bookseller's catalogue and the errata are in the TEI as printed but not "
    "in this edition.",
]

# "IN the fifth Verse" under a decorated initial is set "In the fifth Verse".
DROP_CAP_CASE = True
# "&c." is written "etc.", as on the rest of the shelf.
EXPAND_ETC = True
# A sentence that opens after an italic quotation is capitalized.
ITALIC_SENTENCE_QUIRK = False

# ./fgb epub / pdf / page (paths from the book folder)
EPUB = {"title": "Precious Remedies Against Satan’s Devices", "author": "Thomas Brooks",
        "file": "precious-remedies-against-satans-devices.epub",
        "front": "ebook-front.html", "cover": "cover.typ", "toc_depth": 3,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["precious-remedies-against-satans-devices.typ"]
QUOTE_BLOCK = True

# Salutations and signatures are plain paragraphs, as in The Secret Key of
# Heaven.
CLOSER_PLAIN = True

# The 1653 printing capitalizes many nouns mid-sentence; the edition
# lowercases them, as the other books on the shelf do. Kept capital (not
# listed): God, Christ, Lord, Jesus, Satan, Spirit, Holy Ghost, Scripture,
# Saviour, names, books of the Bible, and words that are sometimes divine or
# part of a name (Father, Son, King, Kings, Judge, Lamb, Word, Majesty, Sea,
# Mount, Book, Supper, Hosts, Paradise, Sabbath, Fathers, Psalmist).
LOWERCASE_COMMON_NOUNS = set("""
    acorns adamant adoption adultery adversary agony altars ambassadors
    amendment ancients angel angell angels anise answers apostle apostles
    appearances appendix apple application arguments ark armies armour arms
    army arrows ascension asp asps atheism attributes axe axiom
    bastard beasts believer believers believing bees bird birds birth
    blasphemy brother
    candle canopy captain captives cardinal castle caution champion chariots
    children church circumcision cities city cock comfort commandments
    commands commission common communion companion companions comrade
    confidences congregation conscience consciences consorts convert
    cornets corruption country countries court courtiers covenant
    covetousness creation creature creatures cross crosses crown crowns
    cummin cup
    deceiver deputy design device devices devil devils disciples disease
    diseases divine doctor doctors doctrine doctrines dragon dragons
    drunkenness duke dukes duties
    earth elephant elephants emperor emperors empire enemies eternity
    evangelical faith family families famine field fishes flag flood
    flower flowers fortitude fountain fowls friend
    gems glass glory goat goats gold gospel gourd grace graceless gun
    hall harbour harlot harlots harp hatchet head heart hearts heathen
    heathens heaven heavenly heavens heir hell hells heritage history
    holiness honey honour horse hypocrite hypocrites
    idiom idol idolatry idols ignorance image impatience ink inn iron
    island jewel jewell jewels joy judgement judgements judgment
    justice justification kingdom kingdoms kingly
    labour labourers labours land lands landmarks law laws learned legacies
    legacy lieutenant life lion lions logic logicians love
    maid manna margent mariner mariners martyr master masters meaning medicine
    merchant mercies mercy messengers metaphor minister monk moon
    nation nations nature natures nightingale nightingales nobles notes
    objections observation ocean oil olive orator orchard ordinance
    ordinances original
    palace pardon parasite parents pastor patient patients peace pearl
    pearls peacock peers penitent persons pestilence philosophers physician
    physicians pill places plots point pole prayer predecessors presence
    presidents pride priest prince princely princes print prison
    proclamation prodigal professors promises prophet prophets proposition
    propositions proverb providence prudence pulpit
    rabbis rain ransom reasons rebel rebellion rebels redemption region
    religion religious remedies remedy repent repentance riders
    righteousness robe robes rock room royal royalty rule ruler rulers
    sacrifice sages saint saints salve sanctification sanctity scepter
    school schools scorpion scorpions scribes seat self senate sermon
    serpent serpents servant services ship sin sinner soldiers soul spider
    spring stars state statutes stone stories strumpet subject subjects
    sun suns surgeon sword
    table tabernacle talents target temperance temple throne thrones thunder
    tomb tongues torments tower towns traitor traveller treatise tree tribe
    triumphs trophies trumpet trumpets tyrant tyrants
    use utterance vengeance verse verses vessel victory viper vipers
    walnut war wasps watch wife wilderness wings wise wolf woman work
    worthies wounds
""".split())

# Old spellings the shared table does not know, and possessives printed
# without an apostrophe (Satans, mens, anothers).
SPELLING = {
    "neer": "near", "injoy": "enjoy", "injoyed": "enjoyed", "injoyest":
    "enjoyest", "injoyment": "enjoyment", "injoyments": "enjoyments",
    "devills": "devils", "evills": "evils", "angells": "angels",
    "beleeve": "believe", "beleeved": "believed", "beleever": "believer",
    "beleevers": "believers", "beleeveth": "believeth", "beleeving":
    "believing", "rejoyce": "rejoice", "rejoyces": "rejoices", "rejoyceth":
    "rejoiceth", "rejoycing": "rejoicing", "poyson": "poison", "poysons":
    "poisons", "poysoned": "poisoned", "poysonous": "poisonous",
    "choisest": "choicest", "choycest": "choicest", "choysest": "choicest",
    "publick": "public", "voyce": "voice", "fixt": "fixed", "logick":
    "logic", "physick": "physic", "collick": "colic", "stomack": "stomach",
    "cloath": "clothe", "cloathing": "clothing", "sackcloath": "sackcloth",
    "terrour": "terror", "terrours": "terrors", "horrour": "horror",
    "horrours": "horrors", "inable": "enable", "inables": "enables",
    "inabled": "enabled", "knowledg": "knowledge", "sinns": "sins", "sinn": "sin",
    "priviledge": "privilege", "priviledges": "privileges", "tast": "taste",
    "tasts": "tastes", "distast": "distaste", "cryed": "cried", "denyed":
    "denied", "mortifyed": "mortified", "hardned": "hardened", "darkned":
    "darkened", "weakned": "weakened", "strengthned": "strengthened",
    "hapned": "happened", "hearkned": "hearkened", "sweetning":
    "sweetening", "lingring": "lingering", "certainely": "certainly",
    "ake": "ache", "dwel": "dwell", "timerous": "timorous", "fals": "falls",
    "aswell": "as well", "assoone": "as soon", "counsells": "counsels",
    "spight": "spite", "jewells": "jewels", "farewel": "farewell",
    "governour": "governor", "seaven": "seven", "crum": "crumb", "crummes":
    "crumbs", "jaylor": "jailer", "plaister": "plaster", "crost": "crossed",
    "sowrly": "sourly", "mistris": "mistress", "mistrisses": "mistresses",
    "marriners": "mariners", "falsly": "falsely", "joyne": "join", "joynes":
    "joins", "joyned": "joined", "joynt": "joint", "joynts": "joints",
    "relapst": "relapsed", "spoyle": "spoil", "spoyling": "spoiling",
    "vildness": "vileness", "leasure": "leisure", "imbrace": "embrace",
    "incouragements": "encouragements", "croud": "crowd", "crouding":
    "crowding", "inriched": "enriched", "intangle": "entangle", "insnared":
    "ensnared", "ingaged": "engaged", "imployments": "employments",
    "stroak": "stroke", "oyntments": "ointments", "controule": "control",
    "controulment": "controlment", "murthering": "murdering", "bewitcht":
    "bewitched", "catcht": "caught", "toucht": "touched", "exprest":
    "expressed", "stept": "stepped", "divelish": "devilish", "vessells":
    "vessels", "bowells": "bowels", "materialls": "materials", "milstones":
    "millstones", "hoast": "host", "theeves": "thieves", "desireable":
    "desirable", "eternaly": "eternally", "compleatness": "completeness",
    "rouling": "rolling", "cruice": "cruse", "mannah": "manna", "traytors":
    "traitors", "reliques": "relics", "wholy": "wholly", "extacy":
    "ecstasy", "toilesome": "toilsome", "winn": "win", "betraies":
    "betrays", "surseited": "surfeited", "feaver": "fever", "extreame":
    "extreme", "begger": "beggar", "ecclipse": "eclipse", "enticeing":
    "enticing", "wormewood": "wormwood", "bryers": "briers", "shipwrack":
    "shipwreck", "unmoveable": "unmovable", "mannor": "manner", "lyer":
    "liar", "scituation": "situation", "dunghil": "dunghill", "seperate":
    "separate", "glimps": "glimpse", "shepheards":
    "shepherds", "emphaticall": "emphatical", "chalenging": "challenging",
    "ballances": "balances", "widdowes": "widows", "annoint": "anoint",
    "loosers": "losers", "layd": "laid", "cordiall": "cordial",
    "joyfullness": "joyfulness", "fowles": "fowls", "cumming": "cummin",
    # names in their KJV form
    "aegypt": "Egypt", "goliah": "Goliath", "zacheus": "Zacchaeus",
    "pharoah": "Pharaoh", "arrians": "Arians", "ninivites": "Ninevites",
    "esay": "Isaiah", "tymothy": "Timothy",
    # possessives printed without an apostrophe
    "satans": "Satan's", "mens": "men's", "anothers": "another's",
    "christs": "Christ's", "abrahams": "Abraham's", "ahabs": "Ahab's",
    "solomons": "Solomon's", "herods": "Herod's", "gideons": "Gideon's",
    "hazaels": "Hazael's", "mahomets": "Mahomet's",
    # an apostrophe opening a word is set as one (Typst would curl a
    # straight one after a space into an opening quote: ‘tis)
    "'tis": "’tis", "'twas": "’twas", "'twill": "’twill", "'twil": "’twill",
    "'twere": "’twere",
}
# ...but the first word of an italic quotation keeps its capital.
QUOTE_START_CASE = True

# Illegible print and the Greek/Hebrew the TCP left out (see gap_fixes.py).
import runpy as _runpy
from pathlib import Path as _Path
GAP_FIXES = _runpy.run_path(str(_Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

# Margin notes are modernized too, as in Gouge: Brooks's margins carry
# English comments and sayings beside the citations, and 1653 spelling there
# next to modern text reads as an accident. Latin (in notes and text) is
# found per run and left as printed.
MODERNIZE_NOTES = True
LATIN_RUNS = True
