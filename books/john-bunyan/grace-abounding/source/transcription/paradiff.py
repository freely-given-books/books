# paragraph boundaries: the 1688 TEI (grace-1688.tcp.xml) against a reading text (DIR/*.typ)
import re, sys
from difflib import SequenceMatcher
from lxml import etree
from foundation import modern
T = "{http://www.tei-c.org/ns/1.0}"
t = etree.parse("grace-1688.tcp.xml")
for g in t.iter(T + "g"): g.text = None
k = lambda w: modern(re.sub(r"['’]", "", w.lower()))
ow, os_ = [], set()
for p in t.iter(T + "p", T + "head"):
    if p.getparent().get("type") == "title_page": continue
    s = re.sub(r"<pb[^>]*/>|<g [^>]*/>", "", etree.tostring(p, encoding=str)); s = re.sub(r"<[^>]+>", " ", s)
    ws = [k(w) for w in re.findall(r"[A-Za-z’']+", s)]
    if ws: os_.add(len(ow)); ow += ws
rw, rs = [], set()
for f in ["preface", "relation", "call-to-the-ministry", "imprisonment", "conclusion"]:
    for para in open(f"{sys.argv[1]}/{f}.typ").read().split("\n\n"):
        para = re.sub(r"#\w+(\([^)]*\))?\[", "", para)
        ws = [k(w) for w in re.findall(r"[A-Za-z’']+", para)]
        if ws: rs.add(len(rw)); rw += ws
sm = SequenceMatcher(None, ow, rw, autojunk=False)
o2r = {a + i: b + i for a, b, n in sm.get_matching_blocks() for i in range(n)}; r2o = {v: x for x, v in o2r.items()}
near = lambda S, x: any(x + d in S for d in (-2, -1, 0, 1, 2))
for i in sorted(os_):
    if i in o2r and not near(rs, o2r[i]): print("PRINT-ONLY ¶", " ".join(ow[i - 5:i]), "|", " ".join(ow[i:i + 7]))
for j in sorted(rs):
    if j in r2o and not near(os_, r2o[j]): print("EDITION-ONLY ¶", " ".join(rw[j - 5:j]), "|", " ".join(rw[j:j + 7]))
