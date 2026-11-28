"""Filter cand.json: drop OCR noise, note marks, reference-style and spelling differences.
Writes cand2.tsv. Usage: python3 -I filter.py"""
import json, re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
D = pathlib.Path(__file__).resolve().parent
import importlib.util
spec = importlib.util.spec_from_file_location("al", D / "align.py")
src = (D / "align.py").read_text().replace("\nmain()\n", "\n")
ns = {"__file__": str(D / "align.py")}; exec(compile(src, "align", "exec"), ns)
fold = ns["sfold"]

BOOKS = set("""gen genesis exod ex exodus lev levit leviticus num numb numbers deut deuteronomy josh joshua judg judges ruth sam samuel kgs kings chr chron chronicles ezra neh nehemiah esth job ps psa psal psalm psalms prov proverbs eccl eccles ecclesiastes song cant isa isaiah is jer jeremiah lam ezek ezekiel dan daniel hos hosea joel amos obad jonah mic micah nah hab habakkuk zeph hag haggai zech zechariah mal malachi matt matth matthew mark luke john acts rom romans cor corinthians gal galatians eph ephes ephesians phil philippians col colossians thess thessalonians tim timothy tit titus philem heb hebrews jas james pet peter jude rev revelation ver chap ch cap lib c v ibid see also comp""".split())
ROMAN = re.compile(r"^[ivxlcdmïüîíIVXLCDM]+$")

def roman(s):
    s = s.lower().replace("ï", "i").replace("î", "i").replace("í", "i").replace("ü", "ii")
    v = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    if not s or any(c not in v for c in s): return None
    t = 0
    for k, c in enumerate(s):
        if k + 1 < len(s) and v[c] < v[s[k + 1]]: t -= v[c]
        else: t += v[c]
    return t

def isref(w):
    x = re.sub(r"[^\wïüîí]", "", w)
    if not x: return True
    if x.isdigit(): return True
    if x.lower() in BOOKS: return True
    if ROMAN.match(x): return True
    if re.match(r"^\d+[a-z]?$", x): return True
    return False

def nums_c(s): return [int(x) for x in re.findall(r"\d+", s)]
def nums_o(s):
    out = []
    for w in re.split(r"[\s,;.:()\-–]+", s):
        w = re.sub(r"[^\wïüîí]", "", w)
        if not w: continue
        if w.isdigit(): out.append(int(w))
        elif ROMAN.match(w) and w.lower() not in ("i",) or w in ("i",):
            r = roman(w)
            if r: out.append(r)
    return out

def alnum(s): return re.search(r"[A-Za-zͰ-Ͽἀ-῿]", s) is not None

C = json.load(open(D / "cand.json"))
keep = []
for c in C:
    if c.get("big"):
        keep.append(("BIG", c)); continue
    a, o = c["ccel"], c["ocr"]
    if not alnum(a) and not alnum(o): continue
    if not a.strip() and not alnum(re.sub(r"\b[l1t]\b", "", o)): continue
    fa = fold(a.replace(" ", "")); fo = fold(o.replace(" ", ""))
    if fa == fo: continue
    fo2 = re.sub(r"(\d+|[lit])$", "", fold(re.sub(r"[\d]+", "", o.replace(" ", ""))))
    if fa == fo2 or fa == fold(re.sub(r"\d", "", o.replace(" ", ""))): continue
    toks = (a + " " + o).split()
    if all(isref(t) for t in toks):
        if nums_c(a) == nums_o(o): continue
        keep.append(("REF", c)); continue
    keep.append(("W", c))

with open(D / "cand2.tsv", "w") as f:
    for k, c in keep:
        f.write(f"{k}\t{c['tag']}\t{c['file']}\t{c['page']}\t{c['ccel']}\t||\t{c['ocr']}\t||\t{c.get('ctx','')}\n")
import collections
print(collections.Counter(k for k, _ in keep))
