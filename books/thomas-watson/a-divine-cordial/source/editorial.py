# Editorial settings for Thomas Watson, A Divine Cordial, from the first edition (London: for
# Thomas Parkhurst, 1663), EEBO-TCP A65292, kept untouched in A65292.tcp.xml. Read by
# build_tei.py, tei_extract.py and ./fgb.
#
# The orig layer is the 1663 print as the TCP keys it, corrected where the page shows a keying
# slip. Witnesses: the 1663 scan the TCP was keyed from (archive.org
# bim_early-english-books-1641-1700_a-divine-cordial-_watson-thomas_1663, Kraken and Tesseract,
# work/a-divine-cordial/ocr-1663), the 1678 edition and the 1815 Philadelphia reprint (A Pious
# Selection) for letters the 1663 film lost; CCEL's text (cordial.ccel.witness.xml), a
# reworded 20th-century modernization, only as a check.

import layout
import runpy as _runpy
from pathlib import Path

T = "{http://www.tei-c.org/ns/1.0}"

QUOTE_BLOCK = True
SMALLCAPS = "smallcaps"
OPENING_SMALLCAPS = True
DROP_CAP_CASE = True
EXPAND_ETC = True
# The short lists the print sets out as tables (1. The best things. 2. The worst things.)
# number as the template does, 1. 2. 3.
TYPST_ENUM = None

# The title page is the print's, not the edition's; the contents index the 1663 pages and the
# edition's own contents replace it.
SKIP_DIVISIONS = {"title_page", "table_of_contents"}

# Watson's sections (chapters 4 and 11) under their chapter.
DIV_LEVELS = {"section": 3}

# Headings this edition adds over the parts of chapters 3, 7, 10, 13, 14 and 16, in the words
# of the 1663 contents page (the parts Watson lists under each chapter there).
EDITION_HEADINGS = True

ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
         "XI", "XII", "XIII", "XIV", "XV", "XVI"]

# The book prints four parts, each opening with its title over its first chapter.
PARTS = {1: "A Divine Cordial", 7: "The Breathings of Love", 11: "Effectual Calling",
         15: "God’s Eternal Purpose"}


def LAYOUT(root):
    """Watson's epistle to the reader, then the sixteen chapters, one file each, the printed
    chapter head ("CHAP. III. Shewing that ...") set under the edition's title."""
    divs = layout.top_divs(root)
    files = [{"file": "to-the-reader.typ", "title": "To the Reader",
              "parts": layout.sections(next(d for d in divs if d.get("type") == "to_the_reader"))}]
    chapters = [d for d in divs if d.get("type") == "chapter"]
    assert [d.get("n") for d in chapters] == [str(k) for k in range(1, 17)]
    for k, div in enumerate(chapters, 1):
        sub = div.findall(f"{T}head")[-1]
        files.append({"file": f"chapter-{k:02d}.typ", "title": f"Chapter {ROMAN[k - 1]}",
                      "subtitle": sub, "part": PARTS.get(k),
                      "parts": layout.sections(div)})
    return files


# Macron abbreviations default to a suppressed "n"; these document-order indices expand to "m"
# ("bonū hominem", a Latin note). Index 1, "free-gracē" (p. 153), is no abbreviation: the 1663
# page (scan 161) has "free-grace:", the colon's upper dot set high; the reading text has "grace".
MACRON_M = {0}

# Gaps (build_tei.py --list): every illegible letter, the Greek and Hebrew the TCP could not
# key and the words lost to blots, read from the 1663 page images or the 1678 edition; see
# gap_fixes.py. Gap 496 (p. 161, an eight-line Greek margin note, stained) is read with the 1678.
GAP_FIXES = _runpy.run_path(str(Path(__file__).parent / "gap_fixes.py"))["GAP_FIXES"]

# Watson's 1663 spellings the shared tables leave (spelling.py): letters only, the word stays his
# (-eth, doth, hath kept; honour, labour as printed). Also the possessives printed without an
# apostrophe where the word can be nothing else (Gods, Christs; Devils, Lords and the like are
# set in chapters/typ by their noun), the names in their KJV form, and the words the machine
# pass turns into other words (lovest -> louest, Bee -> Be, unkindnesses -> unkindness, Latin
# animae -> anima). Keyed by the printed form; made from work/a-divine-cordial/spelling/table.py.
SPELLING = {
    "abrahams": "Abraham's", "advantagious": "advantageous", "ake": "ache",
    "alchymy": "alchemy", "amore": "amore", "animae": "animae", "anothers": "another's",
    "apostacy": "apostasy", "assoon": "as soon", "asswageth": "assuageth",
    "austins": "Austin's", "auxillary": "auxiliary", "avoyding": "avoiding",
    "bartimeus": "Bartimaeus", "battel": "battle", "battels": "battles", "bee": "bee",
    "bellyes": "bellies", "bezar": "bezoar", "boggs": "bogs", "boyls": "boils",
    "bruit": "brute", "burdensom": "burdensome", "caelestial": "celestial",
    "carkass": "carcass", "centinel": "sentinel", "charet": "chariot", "chastned": "chastened",
    "chastneth": "chasteneth", "chastning": "chastening", "chearful": "cheerful",
    "chearfully": "cheerfully", "chearfulness": "cheerfulness", "childs": "Child's",
    "chilness": "chillness", "christs": "Christ's", "chymical": "chemical",
    "chymistry": "chemistry", "cleer": "clear", "cloaths": "clothes",
    "cognitione": "cognitione", "comandments": "commandments", "conquerour": "conqueror",
    "conquerours": "conquerors", "copyed": "copied", "cowardise": "cowardice",
    "cryed": "cried", "cryes": "cries", "cryest": "criest", "cryeth": "crieth",
    "cyrces": "Circe's", "darkned": "darkened", "davids": "David's", "denyal": "denial",
    "devillish": "devilish", "dilicious": "delicious", "diocess": "diocese",
    "disponding": "desponding", "disswades": "dissuades", "doated": "doted", "dwel": "dwell",
    "dye": "die", "dyed": "died", "dyes": "dies", "dyest": "diest", "eccho": "echo",
    "eliah": "Elijah", "elies": "Eli's", "elixar": "elixir", "emboldned": "emboldened",
    "enameld": "enamelled", "encrease": "increase", "encreaseth": "increaseth",
    "encreasing": "increasing", "enflame": "inflame", "evill": "evil",
    "exellencies": "excellencies", "farewel": "farewell", "fastned": "fastened",
    "feaver": "fever", "flyes": "flies", "foyl": "foil", "foyle": "foil", "foyling": "foiling",
    "frantique": "frantic", "freinds": "friends", "garlick": "garlic", "gods": "God's",
    "goliah": "Goliath", "grandure": "grandeur", "hacknying": "hackneying",
    "hamans": "Haman's", "hardning": "hardening", "hieroglyphicks": "hieroglyphics",
    "hierusalem": "Jerusalem", "horrour": "horror", "imbitter": "embitter",
    "implyes": "implies", "indeared": "endeared", "ingulphed": "engulfed",
    "intrinsecal": "intrinsical", "inveloped": "enveloped", "israels": "Israel's",
    "jacobs": "Jacob's", "jaylor": "jailer", "josephs": "Joseph's", "joyn": "join",
    "joyned": "joined", "joynt": "joint", "judg": "judge", "julip": "julep",
    "landskip": "landscape", "livelyhood": "livelihood", "logick": "logic", "louest": "lovest",
    "loueth": "loveth", "lovest": "lovest", "loveth": "loveth", "lye": "lie", "lyed": "lied",
    "lyes": "lies", "lymbecks": "limbecks", "manassah": "Manasseh", "mans": "man's",
    "marriner": "mariner", "medly": "medley", "mens": "men's", "mettal": "metal",
    "mettals": "metals", "milstones": "millstones", "mishapen": "misshapen",
    "mistriss": "mistress", "moistned": "moistened", "musick": "music", "myrth": "mirth",
    "neer": "near", "oratour": "orator", "oyl": "oil", "oyles": "oils", "oyls": "oils",
    "oyntment": "ointment", "oyntments": "ointments", "pallat": "palate",
    "paradice": "paradise", "parlying": "parleying", "pauls": "Paul's", "pennance": "penance",
    "pensil": "pencil", "pensill": "pencil", "peters": "Peter's", "phansy": "fancy",
    "physick": "physic", "pinacle": "pinnacle", "plurisy": "pleurisy", "plyed": "plied",
    "pomgranate": "pomegranate", "powred": "poured", "poyson": "poison",
    "poysoned": "poisoned", "poysonful": "poisonful", "priviledge": "privilege",
    "priviledges": "privileges", "prophaness": "profaneness", "provinder": "provender",
    "publick": "public", "puzling": "puzzling", "rejoyce": "rejoice", "rejoyced": "rejoiced",
    "rejoycest": "rejoicest", "rejoyceth": "rejoiceth", "sacriledge": "sacrilege",
    "satans": "Satan's", "sauls": "Saul's", "scepticisme": "scepticism", "scrued": "screwed",
    "seaven": "seven", "sence": "sense", "showres": "showers", "sleighted": "slighted",
    "sloath": "sloth", "sluce": "sluice", "smel": "smell", "softned": "softened",
    "soveraign": "sovereign", "sowrest": "sourest", "sowrness": "sourness", "soyl": "soil",
    "sphear": "sphere", "spight": "spite", "spoyling": "spoiling", "spyes": "spies",
    "squemish": "squeamish", "stept": "stepped", "stomack": "stomach",
    "stupendious": "stupendous", "subtil": "subtle", "subtilties": "subtleties",
    "subtilty": "subtlety", "supplyes": "supplies", "supream": "supreme", "tast": "taste",
    "tasts": "tastes", "terrours": "terrors", "themselvs": "themselves", "traytor": "traitor",
    "tryal": "trial", "tryals": "trials", "tryed": "tried", "tyde": "tide", "tye": "tie",
    "unkindnesses": "unkindnesses", "valourous": "valorous", "venemous": "venomous",
    "vollies": "volleys", "voyce": "voice", "vse": "use", "waggons": "wagons",
    "wholsom": "wholesome", "wondring": "wondering", "yeild": "yield", "yeilds": "yields",
    "yoak": "yoke", "zacheus": "Zacchaeus",
}

# ./fgb epub / pdf / build (paths from the book folder)
EPUB = {"title": "A Divine Cordial", "author": "Thomas Watson",
        "file": "a-divine-cordial.epub", "front": "ebook-front.html",
        "cover": "cover.typ", "toc_depth": 3,
        "css": ["../../resources/css/ebook.css", "ebook-override.css"]}
PRINT = ["a-divine-cordial.typ"]
