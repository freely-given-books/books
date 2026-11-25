"""Crop page-image lines for candidate rows of cand2.tsv (1-based line numbers) and stack them, labelled.
Usage: python3 -I mkbatch.py out.png N N N ...   (N may be 'N:word' to override the search word, or 'page:word' with P prefix e.g. P362:Sihon)"""
import sys, re, subprocess, pathlib, json
D = pathlib.Path(__file__).resolve().parent
W0 = pathlib.Path("/home/courtney/Projects/fgbooks/work/institutes")
rows = (D / "cand2.tsv").read_text().split("\n")
def lines_of(lab):
    if lab.startswith("III."): W = W0 / "vol3"; pg = int(lab[4:]) + 4
    elif lab.startswith("II."): W = W0 / "vol2"; pg = int(lab[3:]) + 10
    else: W = W0; pg = int(lab) + 124
    x = (W / "kraken" / f"p-{pg:04d}.xml").read_text()
    L = []
    for m in re.finditer(r'<TextLine[^>]*HPOS="(\d+)" VPOS="(\d+)" WIDTH="(\d+)" HEIGHT="(\d+)"[^>]*>(.*?)</TextLine>', x, re.S):
        t = " ".join(re.findall(r'<String[^>]*CONTENT="([^"]*)"', m.group(5)))
        L.append((int(m.group(2)), int(m.group(4)), t))
    L.sort(); return W / "pages" / f"p-{pg:04d}.png", L
def norm(s): return re.sub(r"[^a-z0-9æœ]", "", s.lower())
out = []
for k, arg in enumerate(sys.argv[2:]):
    if arg.startswith("P"):
        lab, word = arg[1:].split(":", 1); tag = arg
        ctx = None
    else:
        n, _, word = arg.partition(":")
        f = rows[int(n) - 1].split("\t")
        lab = f[3]; ocr = f[6]; tag = n
        ctx = f[8]
        if not word:
            ws = [w for w in ocr.split() if len(re.sub(r"\W", "", w)) > 1] or ocr.split() or ["?"]
            word = max(ws, key=len)
    img, L = lines_of(lab)
    # neighbours to disambiguate
    hits = [i for i, l in enumerate(L) if norm(word) and norm(word) in norm(l[2])]
    pages = [(img, L)]
    if not hits:
        # try next page (candidate may sit on the following page)
        nl = f"III.{int(lab[4:])+1}" if lab.startswith("III.") else f"II.{int(lab[3:])+1}" if lab.startswith("II.") else str(int(lab) + 1)
        try:
            img2, L2 = lines_of(nl)
            h2 = [i for i, l in enumerate(L2) if norm(word) in norm(l[2])]
            if h2: img, L, hits = img2, L2, h2
        except Exception: pass
    if not hits:
        print("MISS", arg, word); continue
    if ctx and len(hits) > 1:
        cw = set(norm(w) for w in re.sub(r"\[\[|\]\]", " ", ctx).split())
        hits.sort(key=lambda i: -len(cw & set(norm(w) for w in (L[i][2] + " " + (L[i-1][2] if i else "")).split())))
    i = hits[0]
    y0 = L[i][0] - 6; y1 = L[i][0] + L[i][1] + 6
    o = D / "crops" / f"m-{k}.png"
    subprocess.run(["magick", str(img), "-crop", f"x{y1-y0}+0+{y0}", "+repage", "-resize", "55%", "-colorspace", "sRGB", "-background", "white", "-gravity", "east", "-extent", "1000x", "-gravity", "west", "-fill", "red", "-pointsize", "22", "-annotate", "+4+0", tag, str(o)], check=True)
    out.append(str(o))
subprocess.run(["magick", *out, "-append", sys.argv[1]], check=True)
print(len(out), "crops")
