# wording differences between the 1688 transcription (grace-1688.tcp.xml) and the current
# edition's reg text (chapters/typ), after the edition's own modernizations are set aside:
# spelling (compared in modern spelling), compounds ("my self"/"myself"), Scripture references,
# and the kinds the editor's rule of 2026-10-26 keeps modern.
#   wording.py -> wording.json, wording.txt
import json, re, sys
from difflib import SequenceMatcher
from pathlib import Path
from lxml import etree
sys.path.insert(0, str(Path(__file__).parent))
from foundation import modern

W = Path(__file__).parent
ED = Path(__file__).parent / "edition-typ"      # the previous edition (books main, 2026-11-01)
T = "{http://www.tei-c.org/ns/1.0}"
FILES = ["preface", "relation", "call-to-the-ministry", "imprisonment", "conclusion"]
BOOKS = set("""gen exod ex lev num numb deut josh judg ruth sam kgs king kings chr chron ezra neh esth job ps psal
psa prov eccl eccles ecc song isa jer lam ezek dan hos joel amos obad jonah mic nah hab zeph hag zech mal matt mat
mark mar luke luk john joh acts act rom cor gal eph ephes phil col thess thes tim titus tit phlm heb jas jam pet
jude rev chap ch ver vv v cf""".split())
# the edition keeps these modern (the editor's rule of 2026-10-26; pairs as 1688 -> edition)
MODERN = {("an", "a"), ("a", "an"), ("o", "oh"), ("twas", "it was"), ("tis", "it is"), ("betwixt", "between"),
          ("estate", "state"), ("thorow", "through"), ("thorough", "through"), ("tho", "though"),
          ("chuse", "choose"), ("burthen", "burden"), ("learnt", "learned"), ("sate", "sat"),
          ("stroak", "stroke"), ("sieze", "seize"), ("loth", "loath"), ("suddainly", "suddenly"),
          ("then", "than"), ("c", "etc"), ("ake", "ache"), ("holden", "held"), ("mad", "mad")}


def words(s):
    return re.findall(r"[A-Za-z’']+", s)


def key(w):
    return modern(re.sub(r"['’]", "", w.lower()))


def tei_div_words():
    t = etree.parse(str(W / "grace-1688.tcp.xml"))
    for g in t.iter(T + "g"):
        g.text = None
    divs = [d for d in t.iter(T + "div") if d.get("type") != "title_page"]
    out = []
    for d in divs:
        for h in d.findall(T + "head"):
            h.getparent().remove(h)
        s = re.sub(r"<g [^>]*/>", "", etree.tostring(d, encoding=str))
        s = re.sub(r"<pb [^>]*/>", "", s)
        s = re.sub(r"<[^>]+>", "", s)
        out.append(words(s))
    return out


def ed_words(f):
    s = (ED / f"{f}.typ").read_text()
    s = re.sub(r"^=.*$", "", s, flags=re.M)
    s = re.sub(r"#\w+(\([^)]*\))?\[", "", s)
    return words(s)


def main():
    new = tei_div_words()
    rows = []
    for f, nw in zip(FILES, new):
        ew = ed_words(f)
        nk, ek = [key(w) for w in nw], [key(w) for w in ew]
        sm = SequenceMatcher(None, nk, ek, autojunk=False)
        for op, a, b, c, d in sm.get_opcodes():
            if op == "equal": continue
            na, ea = nk[a:b], ek[c:d]
            if "".join(na) == "".join(ea): continue                       # compounds
            if all(x in BOOKS or x.isdigit() for x in na + ea): continue      # references
            if (" ".join(na), " ".join(ea)) in MODERN: continue
            if [x for x in na if x not in BOOKS] == [x for x in ea if x not in BOOKS]: continue
            rows.append({"file": f, "new": " ".join(nw[a:b]), "ed": " ".join(ew[c:d]),
                         "ctx": " ".join(nw[max(0, a - 6):a]) + " [" + " ".join(nw[a:b]) + " | " + " ".join(ew[c:d]) + "] " + " ".join(nw[b:b + 6]),
                         "n": max(b - a, d - c)})
    (W / "wording.json").write_text(json.dumps(rows, indent=1))
    with open(W / "wording.txt", "w") as fh:
        for r in rows: fh.write(f"{r['file']}: {r['ctx']}\n")
    print(len(rows), "wording differences;", sum(r["n"] >= 3 for r in rows), "of 3+ words")


main()
