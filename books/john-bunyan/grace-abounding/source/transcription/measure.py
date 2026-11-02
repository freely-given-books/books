# The before/after quality measure: 32 random passages of 8 printed lines (seed 1688), each shown
# as the 1688 page image with the previous edition's text and the new reading text beside it,
# for counting wording errors (a word missing, added or changed against the print, or put in the
# wrong order; spelling, case, punctuation and the editor's rule of 2026-10-26 left aside).
#   measure.py OUTDIR -> OUTDIR/m*.png (4 passages each), OUTDIR/measure-texts.md
import random, re, sys
from difflib import SequenceMatcher
from pathlib import Path
from PIL import Image, ImageDraw
sys.path.insert(0, str(Path(__file__).parent))
from alto import lines
from assemble import page_lines
from gutter import key

W = Path(__file__).parent
NEW = Path.home() / "Projects/fgbooks/books/books/john-bunyan/grace-abounding/chapters/typ"
OLD = W / "edition-typ"
FILES = ["preface", "relation", "call-to-the-ministry", "imprisonment", "conclusion"]


def typ_words(d):
    out = []
    for f in FILES:
        s = (d / f"{f}.typ").read_text()
        s = re.sub(r"^=.*$", "", s, flags=re.M)
        s = re.sub(r"#\w+(\([^)]*\))?\[", "", s).replace("]", "").replace("\\", "")
        out += re.findall(r"[A-Za-z’'\d]+(?:[.:–][\d]+)*|[^\sA-Za-z\d]", s)
    return out


def mapping(pk, other):
    ok = [key(w) if re.match(r"[A-Za-z]", w) else None for w in other]
    idx = [i for i, k in enumerate(ok) if k]
    sm = SequenceMatcher(None, pk, [ok[i] for i in idx], autojunk=False)
    m = {}
    for a, b, n in sm.get_matching_blocks():
        for d in range(n): m[a + d] = idx[b + d]
    return m


def span(m, i, j, words):
    hits = [m[k] for k in range(i, j) if k in m]
    if not hits: return "(nothing aligned)"
    return " ".join(words[min(hits):max(hits) + 1])


def main(out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    pages = page_lines()
    pw = []                                     # (key, frame, line)
    for p in sorted(pages):
        if p < 5: continue
        for x in pages[p]:
            for t in x["toks"]:
                if re.match(r"[A-Za-z]", t["t"]): pw.append((key(t["t"]), p, x["line"]))
    pk = [k for k, _, _ in pw]
    nw, ow = typ_words(NEW), typ_words(OLD)
    mn, mo = mapping(pk, nw), mapping(pk, ow)
    rnd = random.Random(1688)
    frames = sorted(rnd.sample([p for p in sorted(pages) if p >= 13], 32))
    rows, texts = [], []
    for n, f in enumerate(frames, 1):
        ls = [x["line"] for x in pages[f]]
        start = rnd.randrange(0, max(1, len(ls) - 8))
        sel = ls[start:start + 8]
        idx = [i for i, (_, p, l) in enumerate(pw) if p == f and l in sel]
        i, j = idx[0], idx[-1] + 1
        texts.append(f"## {n}. frame {f}, lines {sel[0]}-{sel[-1]} ({j - i} words)\n\n"
                     f"- previous: {span(mo, i, j, ow)}\n- new: {span(mn, i, j, nw)}\n")
        al = lines(f)
        y0, y1 = al[sel[0] - 1][1][1], al[sel[-1] - 1][1][3]
        im = Image.open(W / f"f1688/p-{f:03d}.png").convert("L").crop((0, y0, 10 ** 5, y1))
        im = im.crop((0, 0, Image.open(W / f"f1688/p-{f:03d}.png").size[0], im.size[1]))
        im.thumbnail((900, 700)); rows.append((f"{n}. frame {f}", im))
    for s in range(0, len(rows), 4):
        part = rows[s:s + 4]
        sh = Image.new("L", (900, sum(r[1].size[1] + 28 for r in part)), 255); d = ImageDraw.Draw(sh); y = 0
        for lab, im in part:
            d.text((4, y + 6), lab, fill=0); y += 26; sh.paste(im, (0, y)); y += im.size[1] + 2
        sh.save(out / f"m{s // 4}.png")
    (W / "measure-texts.md").write_text("\n".join(texts))
    print(sum(len(t.split()) for t in texts), "chars-ish;", len(rows), "passages")


if __name__ == "__main__":
    main(sys.argv[1])
