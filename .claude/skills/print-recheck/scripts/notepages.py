"""Footnotes per printed page: 1845 (indented lines after the gap at the foot of the page, ALTO) vs CCEL
(#footnote positions mapped to pages through the main-text alignment). Prints pages where the counts differ.
Usage: python3 -I notepages.py"""
import re, pathlib, difflib, collections, bisect
D = pathlib.Path(__file__).resolve().parent
src = (D / "align.py").read_text().replace("\nmain()\n", "\n")
ns = {"__file__": str(D / "align.py")}; exec(compile(src, "align", "exec"), ns)
K = ns["ocr_stream"]("kraken"); fold = ns["fold"]; T = ns["T"]
W = pathlib.Path("/home/courtney/Projects/fgbooks/work/institutes/vol3")
def notes1845(img):
    x = (W / "kraken" / f"p-{img:04d}.xml").read_text()
    L = []
    for m in re.finditer(r'<TextLine[^>]*HPOS="(\d+)" VPOS="(\d+)" WIDTH="(\d+)" HEIGHT="(\d+)"[^>]*>(.*?)</TextLine>', x, re.S):
        t = " ".join(re.findall(r'<String[^>]*CONTENT="([^"]*)"', m.group(5)))
        L.append((int(m.group(2)), int(m.group(1)), int(m.group(3)), t))
    L.sort()
    body = [l for l in L if l[2] > 600]
    if not body: return []
    left = sorted(l[1] for l in body)[len(body) // 2]
    # the note zone: after the largest vertical gap in the lower half
    best = None
    for a, b in zip(body, body[1:]):
        g = b[0] - a[0]
        if b[0] > 1000 and g > 75 and (best is None or g > best[0]): best = (g, b[0])
    if not best: return []
    return [l[3] for l in L if l[0] >= best[1] and l[1] > left + 25 and re.match(r"^\S*\d", l[3]) and not re.match(r"^\d+\. [A-Z]", l[3]) and l[2] > 150]
files = sorted(T.glob("*.typ"))
MT = []; FN = []
for f in files:
    s = f.read_text()
    m, nt = ns["parse_typ"](s)
    toks = ns["tokens"](m)
    MT += [(w, f.name, a) for w, a, e in toks]
    for mm in re.finditer(r"#footnote\[", s):
        FN.append((f.name, mm.start(), s[mm.end():mm.end() + 50]))
a = [fold(t[0]) for t in MT]; b = [fold(t[0]) for t in K]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
pg = {}
for op, i1, i2, j1, j2 in sm.get_opcodes():
    if op == "equal":
        for k in range(i2 - i1): pg[i1 + k] = K[j1 + k][1][1]
keys = [(MT[i][1], MT[i][2], i) for i in range(len(MT))]
cc = collections.defaultdict(list)
for fn, off, txt in FN:
    j = bisect.bisect_right(keys, (fn, off, 10**9)) - 1
    while j >= 0 and j not in pg: j -= 1
    cc[pg[j]].append(txt)
for img in range(303, 559):
    n45 = notes1845(img)
    if len(n45) != len(cc[img]):
        print(f"III.{img-4}: 1845 {len(n45)} CCEL {len(cc[img])}")
        for t in n45: print("   1845:", t[:90])
        for t in cc[img]: print("   CCEL:", t)
