"""Align vol-6 Classic .typ (Book IV ch. 14-20, main text + footnotes) with Kraken OCR of 1845 vol. 3 pp. 299-554 (images 303-558).
Writes cand.tsv (one candidate difference per line) and cand.json.
Usage: python3 -I align.py"""
import difflib, re, json, pathlib, unicodedata

T = pathlib.Path("/home/courtney/Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion/chapters/typ/vol-6")
W = pathlib.Path("/home/courtney/Projects/fgbooks/work/institutes")
OUT = pathlib.Path(__file__).resolve().parent
# (scan dir, first image, last image, offset printed = image - off, label prefix)
SCANS = [(W / "vol3", 303, 558, 4, "III.")]
def plabel(sp):
    sc, p = sp
    d, _, _, off, pre = SCANS[sc]
    return f"{pre}{p - off}"
def pimgname(sp):
    sc, p = sp
    return "vol3/" + f"p-{p:04d}"

HEAD = re.compile(r"^([A-Z]{2,}\w* OF THE\.?|INSTITUTES,? (RC|&C|ETC)\.?|INST\w* OF THE,? ETC\.?|VOL\.? ?II\.?|\d{1,3}|[ivxlc]+\.?|INSTITUTES OF THE\.?|CHRISTIAN RELIGION\.?|BOOK ?[IV1l]+\.?|CHAP\.? ?[IVXLC1l]+\.?|PREFATORY ADDRESS.*|EPISTLE.*|SUBJECT OF THE.*|METHOD AND.*|GENERAL INDEX.*|VOL\.? ?I\.?|[A-Z]{1,2}\d?|[A-Z] ?\d)$")

def ocr_stream(kind):
    toks = []
    for sc, (D0, P0, P1, _o, _pre) in enumerate(SCANS):
     for p in range(P0, P1 + 1):
         f = D0 / kind / f"p-{p:04d}.txt"
         if not f.exists():
             continue
         lines = f.read_text().split("\n")
         keep = []
         for k, ln in enumerate(lines):
             s = ln.strip()
             if (k < 4 or k >= len(lines) - 3) and HEAD.match(s):
                 continue
             keep.append(s)
         txt = "\n".join(keep)
         txt = re.sub(r"¬\s*\n\s*", "", txt)
         txt = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", txt)
         for li, ln in enumerate(txt.split("\n")):
             for w in re.split(r"[\s\u2014\u2013-]+", ln):
                 if w: toks.append((w, (sc, p)))
    return toks

def parse_typ(src):
    """Return (main, notes): lists of (char, offset) visible text."""
    main, notes = [], []
    stack = []  # 'fn' or 'x'
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        if c == "\\" and i + 1 < n:
            (notes if "fn" in stack else main).append((src[i + 1], i + 1)); i += 2; continue
        m = re.match(r"#(\w+)(\([^()]*(?:\([^()]*\)[^()]*)*\))?\[", src[i:])
        if m:
            stack.append("fn" if m.group(1) == "footnote" else "x")
            if m.group(1) == "footnote":
                main.append((" ", i))
                notes.append(("‖", i))  # note separator
            i += m.end(); continue
        m = re.match(r"#\w+(\([^()]*\))?", src[i:])
        if m:
            i += m.end(); continue
        if c == "]" and stack:
            stack.pop(); i += 1; continue
        if c == "=" and (i == 0 or src[i - 1] == "\n"):
            while i < n and src[i] == "=": i += 1
            continue
        (notes if "fn" in stack else main).append((c, i))
        i += 1
    return main, notes

def tokens(chars):
    out, cur, st = [], [], None
    for ch, o in chars:
        if ch.isspace() or ch in "\u2014\u2013-\u2016":
            if cur: out.append(("".join(cur), st, o)); cur = []
            if ch == "‖": out.append(("‖", o, o + 1))
            continue
        if not cur: st = o
        cur.append(ch); end = o + 1
        last = o
    if cur: out.append(("".join(cur), st, last + 1))
    return out

def fold(w):
    w = unicodedata.normalize("NFKD", w)
    w = "".join(c for c in w if not unicodedata.combining(c)).lower()
    w = re.sub(r"[^a-z0-9Ͱ-Ͽ֐-׿]", "", w)
    w = w.replace("our", "or").replace("ise", "ize").replace("yse", "yze").replace("ae", "e")
    w = re.sub(r"([a-z])\1+", r"\1", w)
    w = re.sub(r"tre(s|d)?$", r"ter\1", w); w = re.sub(r"ence(s)?$", r"ense\1", w)
    w = w.replace("ence", "ense").replace("gement", "gment").replace("ou", "o").replace("ph", "f")
    return w

def sfold(w):
    w = unicodedata.normalize("NFKD", w)
    w = "".join(c for c in w if not unicodedata.combining(c)).lower()
    w = re.sub(r"[^a-z0-9\u0370-\u03ff]", "", w)
    if len(w) < 5: return w
    w = w.replace("our", "or").replace("ise", "ize").replace("yse", "yze").replace("ae", "e").replace("oe", "e")
    w = re.sub(r"([a-z])\1+", r"\1", w)
    w = re.sub(r"tre(s|d)?$", r"ter\1", w)
    w = w.replace("ence", "ense").replace("gement", "gment")
    return w

CASES = []
def main():
    K = ocr_stream("kraken")
    files = sorted(T.glob("*.typ"))
    MT, NT = [], []  # (word, file, start, end)
    for f in files:
        src = f.read_text()
        m, nt = parse_typ(src)
        MT += [(w, f.name, s, e) for w, s, e in tokens(m)]
        NT += [(w, f.name, s, e) for w, s, e in tokens(nt) if w != "‖"] + [("‖", f.name, 0, 0)]
    a = [fold(t[0]) for t in MT]; b = [fold(t[0]) for t in K]
    cands = []
    def run(A, Atok, Bidx, tag):
        bb = [b[j] for j in Bidx]
        sm = difflib.SequenceMatcher(None, A, bb, autojunk=False)
        used = set()
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                used.update(Bidx[j] for j in range(j1, j2))
                for k in range(i2 - i1):
                    t = Atok[i1 + k]; ow = K[Bidx[j1 + k]][0]
                    ca = re.sub(r"[^A-Za-z]", "", t[0]); co = re.sub(r"[^A-Za-z]", "", ow)
                    if ca and co and ca != co and ca.lower() == co.lower() and ca[0] != co[0]:
                        CASES.append(f"{t[1]}\t{plabel(K[Bidx[j1 + k]][1])}\t{t[0]}\t{ow}\t" + " ".join(x[0] for x in Atok[max(0, i1 + k - 5):i1 + k + 5]))
                    if sfold(t[0]) != sfold(ow) and re.sub(r"\W", "", ow) and not re.fullmatch(r"\W*\d+\W*", ow):
                        cands.append(dict(tag=tag + "-eq", file=t[1], ccel=t[0], ocr=ow, ctx=" ".join(x[0] for x in Atok[max(0, i1 + k - 4):i1 + k]) + " [[" + t[0] + "]] " + " ".join(x[0] for x in Atok[i1 + k + 1:i1 + k + 5]), page=plabel(K[Bidx[j1 + k]][1]), pimg=pimgname(K[Bidx[j1 + k]][1]), off=t[2]))
                continue
            if op == "insert" and j2 - j1 > 6: continue  # unmatched OCR runs (notes / main)
            if op == "delete" and i2 - i1 > 40:
                print("BIGDEL", tag, Atok[i1][1], " ".join(t[0] for t in Atok[i1:i2])[:400]); continue
            if (i2 - i1) > 12 or (j2 - j1) > 12:
                cands.append(dict(tag=tag, big=True, file=Atok[min(i1, len(Atok)-1)][1], ccel=" ".join(t[0] for t in Atok[i1:i2])[:300], ocr=" ".join(K[Bidx[j]][0] for j in range(j1, j2))[:300], page=plabel(K[Bidx[min(j1, len(Bidx)-1)]][1]))); continue
            ctx0 = max(0, i1 - 4); ctx1 = min(len(Atok), i2 + 4)
            jj = Bidx[min(j1, len(Bidx) - 1)]
            cands.append(dict(tag=tag, file=Atok[min(i1, len(Atok)-1)][1],
                              ccel=" ".join(t[0] for t in Atok[i1:i2]),
                              ocr=" ".join(K[Bidx[j]][0] for j in range(j1, j2)),
                              ctx=" ".join(t[0] for t in Atok[ctx0:i1]) + " [[" + " ".join(t[0] for t in Atok[i1:i2]) + "]] " + " ".join(t[0] for t in Atok[i2:ctx1]),
                              octx=" ".join(K[Bidx[j]][0] for j in range(max(0, j1 - 4), min(len(Bidx), j2 + 4))),
                              page=plabel(K[jj][1]), pimg=pimgname(K[jj][1]), off=Atok[min(i1, len(Atok)-1)][2]))
        return used
    used = run(a, MT, list(range(len(b))), "main")
    rest = [j for j in range(len(b)) if j not in used]
    na = [fold(t[0]) for t in NT]
    used2 = run(na, NT, rest, "note")
    left = [j for j in rest if j not in used2]
    runs = []; cur = []
    for j in left:
        if cur and j != cur[-1] + 1:
            runs.append(cur); cur = []
        cur.append(j)
    if cur: runs.append(cur)
    with open(OUT / "residual.txt", "w") as fr:
        for r in runs:
            if len(r) >= 1:
                fr.write(f"p{plabel(K[r[0]][1])}\t{len(r)}\t" + " ".join(K[j][0] for j in r) + "\n")
    open(OUT / "cases.tsv", "w").write("\n".join(CASES) + "\n")
    json.dump(cands, open(OUT / "cand.json", "w"), ensure_ascii=False, indent=0)
    with open(OUT / "cand.tsv", "w") as fo:
        for c in cands:
            fo.write(f"{c['tag']}\t{c['file']}\t{c['page']}\t{c['ccel']}\t||\t{c['ocr']}\t||\t{c.get('ctx','BIG')}\n")
    print(len(cands))

main()
