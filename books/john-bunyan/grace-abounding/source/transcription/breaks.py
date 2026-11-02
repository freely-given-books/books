# paragraph breaks of the 1688 print: a line that opens with the next section number, or an
# indented line (local margin, 0.6-3 em) after a line that stops short
import re, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from assemble import page_lines, join


def seq_lines():
    pages = page_lines()
    seq = []
    for p in sorted(pages):
        ls = pages[p]
        for i, x in enumerate(ls):
            win = sorted(y["box"][0] for y in ls[max(0, i - 4):i + 5])
            margin = win[1] if len(win) > 2 else win[0]
            em = x["box"][3] - x["box"][1]
            x["lind"] = (x["box"][0] - margin) / max(em, 1)
            x["txt"] = join([t["t"] for t in x["toks"]])
            seq.append(x)
    return seq


def breaks(seq):
    expect, out = 2, {}
    for i, x in enumerate(seq):
        prev = seq[i - 1] if i else None
        m = re.match(r"(\d{1,3})\s*[.,(]?", x["txt"])
        num = None
        if m and x["lind"] > -0.5:
            n = int(m[1])
            if expect <= n <= expect + 3 or (n == 1 and x["frame"] == 191): num = n
        geo = 0.6 <= x["lind"] <= 3.0 and prev is not None and prev["right"] >= 1.0
        if num: expect = num + 1
        if num or geo:
            out[i] = num
    return out


if __name__ == "__main__":
    seq = seq_lines()
    b = breaks(seq)
    got = sorted(n for n in b.values() if n)
    print(len(b), "breaks,", len(got), "numbered")
    print("numbers not found:", sorted(set(range(2, 341)) - set(got)))
    for i, n in b.items():
        x = seq[i]
        if not n and not re.match(r"\d", x["txt"]): print(x["frame"], x["line"], round(x["lind"], 2), x["txt"][:50])
