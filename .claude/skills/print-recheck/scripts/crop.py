"""Crop the line(s) of a page image containing a word: python3 -I crop.py PRINTED_PAGE word [n_lines_context] [out]
Uses Kraken ALTO line boxes. Page "279" = 1845 vol. 1 (image page+124); "II.5" = 1845 vol. 2 (vol2/ image page+10); "III.5" = 1845 vol. 3 (vol3/ image page+4)."""
import re, sys, subprocess, pathlib
W = pathlib.Path("/home/courtney/Projects/fgbooks/work/institutes")
lab = sys.argv[1]
if lab.startswith("III."):
    W = W / "vol3"; pg = int(lab[4:]) + 4
elif lab.startswith("II."):
    W = W / "vol2"; pg = int(lab[3:]) + 10
else:
    pg = int(lab) + 124
word = sys.argv[2]; ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 1
out = sys.argv[4] if len(sys.argv) > 4 else str(pathlib.Path(__file__).resolve().parent / "crops" / f"c-{sys.argv[1]}-{re.sub(r'[^A-Za-z0-9]', '_', word)[:20]}.png")
pathlib.Path(out).parent.mkdir(exist_ok=True)
x = (W / "kraken" / f"p-{pg:04d}.xml").read_text()
lines = []
for m in re.finditer(r'<TextLine[^>]*HPOS="(\d+)" VPOS="(\d+)" WIDTH="(\d+)" HEIGHT="(\d+)"[^>]*>(.*?)</TextLine>', x, re.S):
    t = " ".join(re.findall(r'<String[^>]*CONTENT="([^"]*)"', m.group(5)))
    lines.append((int(m.group(2)), int(m.group(4)), t))
lines.sort()
hits = [k for k, l in enumerate(lines) if word.lower() in l[2].lower()]
if not hits:
    print("not found; lines:"); [print(l[2]) for l in lines]; sys.exit(1)
k = hits[0]
a = max(0, k - ctx); b = min(len(lines) - 1, k + ctx)
y0 = lines[a][0] - 8; y1 = lines[b][0] + lines[b][1] + 8
subprocess.run(["magick", str(W / "pages" / f"p-{pg:04d}.png"), "-crop", f"x{y1 - y0}+0+{y0}", "+repage", out], check=True)
print(out, "hits", len(hits)); [print(" ", lines[j][2]) for j in range(a, b + 1)]
