# check_sheet.py BUCKET OUTDIR: each case of buckets.json[BUCKET] shown on its 1688 frame lines
import json, re, sys
from PIL import Image, ImageDraw
sys.path.insert(0, ".")
from alto import lines
from assemble import page_lines
from gutter import key
SKIP = re.compile(r"^(John Bunyan|Ecclus|Jer|ver|Josh|Col II|Chap II|Act amp amp|FINIS)$")
pages = page_lines()
seq = []
for p in sorted(pages):
    for x in pages[p]:
        for t in x["toks"]:
            if re.match(r"[A-Za-z]", t["t"]): seq.append((key(t["t"]), p, x["line"]))
keys = [k for k, _, _ in seq]
cases = [r for r in json.load(open("buckets.json"))[sys.argv[1]] if not SKIP.match(r["new"])]
rows = []
for r in cases:
    m = re.match(r"(.*?)\[(.*?) \| (.*?)\](.*)", r["ctx"])
    left = [key(w) for w in m[1].split()][-3:]; mid = [key(w) for w in m[2].split()]
    pat = left + mid if mid else left + [key(w) for w in m[4].split()][:2]
    hit = next((i for i in range(len(keys)) if keys[i:i + len(pat)] == pat), None)
    if hit is None:
        print("not found:", r["ctx"][:80]); continue
    _, f, l = seq[hit + len(left)] if mid else seq[hit + len(left) - 1]
    ls = lines(f); a = max(0, l - 2); b = min(len(ls), l + 1)
    im = Image.open(f"f1688/p-{f:03d}.png").convert("L")
    st = im.crop((0, ls[a][1][1], im.size[0], ls[b - 1][1][3]))
    st = st.resize((900, int(900 * st.size[1] / st.size[0])))
    rows.append((f"{len(rows) + 1}. f{f}:{l}  {m[1][-40:]}[{m[2]} | {m[3]}]{m[4][:30]}", st))
out = sys.argv[2]
for s in range(0, len(rows), 8):
    part = rows[s:s + 8]
    H = sum(p[1].size[1] + 30 for p in part)
    sh = Image.new("L", (900, H), 255); d = ImageDraw.Draw(sh); y = 0
    for lab, st in part:
        d.text((4, y + 6), lab, fill=0); y += 28; sh.paste(st, (0, y)); y += st.size[1] + 2
    sh.save(f"{out}/{sys.argv[1]}{s // 8}.png")
print(len(rows), "cases")
