# Words the 1688 film lost at the cropped page edge (the gutter): a whole short word at a line's
# start or end ("[I] stood there"), or a word's first letters at a line start ("[s]wearing").
# Kraken never saw them, and the vote is anchored on Kraken's tokens, so nothing put them back.
# Found where the current edition has words the 1688 text lacks at a line boundary; supplied
# only where the 1692 copy (Kraken, kp1692/) has the same words in the same context.
#   gutter.py -> gutter.json [{"after"|"before": token index, "t": word, "p", "l", "kind"}]
import json, re, sys
from difflib import SequenceMatcher
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from foundation import modern
from assemble import line_fix
from alto import lines as alto_lines
from wording import ED, FILES

W = Path(__file__).parent


def key(w):
    return modern(re.sub(r"['’\-­]", "", w.lower()))


def k1692_keys():
    text = []
    for f in sorted((W / "kp1692").glob("p-*.txt")):
        text.append(f.read_text())
    s = "\n".join(text).replace("ſ", "s")
    s = re.sub(r"[-¬]\s*\n\s*", "", s)
    return " " + " ".join(key(w) for w in re.findall(r"[A-Za-z’']+", s)) + " "


def text_keys(s):
    s = s.replace("ſ", "s")
    s = re.sub(r"[-¬]\s*\n\s*", "", s)
    return " " + " ".join(key(w) for w in re.findall(r"[A-Za-z’']+", s)) + " "


def witnesses():
    """the other texts, as modern-spelling key strings: the 1692 copy (Kraken), the 1666 first
    edition (TCP; its gaps left as gaps), the 1905 RTS text (Gutenberg #654)"""
    tcp = (Path.home() / "Projects/fgbooks/books/books/john-bunyan/grace-abounding/source/A30143.witness.xml").read_text()
    tcp = re.sub(r'<g ref="char:EOLhyphen"/>', "", tcp[tcp.find("<text"):])
    tcp = re.sub(r"<gap.*?</gap>", " ~ ", tcp, flags=re.S)
    tcp = re.sub(r"<[^>]+>", " ", tcp)
    pg = (W / "scans/pg654.txt").read_text()
    return {"1692": k1692_keys(), "1666": text_keys(tcp), "RTS": text_keys(pg)}


def left_cut(frame):
    ls = alto_lines(frame)
    return sum(1 for _, b, _ in ls if b[0] < 25) > len(ls) / 3


def main():
    toks = json.load(open(W / "foundation.json"))
    fix = line_fix()
    for t in toks:
        if t["p"] in fix: t["l"] = fix[t["p"]][t["l"]]
    widx = [i for i, t in enumerate(toks) if re.match(r"[A-Za-z]", t["t"])]
    nk = [key(toks[i]["t"]) for i in widx]
    ew = []
    for f in FILES:
        s = (ED / f"{f}.typ").read_text()
        s = re.sub(r"^=.*$", "", s, flags=re.M)
        s = re.sub(r"#\w+(\([^)]*\))?\[", "", s)
        ew += re.findall(r"[A-Za-z’']+", s)
    ek = [key(w) for w in ew]
    wit = witnesses()

    def confirmed(ctx):
        pat = " " + " ".join(ctx) + " "
        return [k for k, v in wit.items() if pat in v]
    sm = SequenceMatcher(None, nk, ek, autojunk=False)
    out, rejected = [], []
    for op, a, b, c, d in sm.get_opcodes():
        if op == "equal" or d - c > 3 or b - a > 1 or a == 0 or a >= len(nk): continue
        ins = ek[c:d]
        if op == "insert":
            ti_prev, ti_next = widx[a - 1], widx[a]
            tp, tn = toks[ti_prev], toks[ti_next]
            if (tp["p"], tp["l"]) == (tn["p"], tn["l"]): continue          # not at a line boundary
            # the tokens between them (punctuation) must all sit on the earlier line
            hit = confirmed(nk[a - 1:a] + ins + nk[a:a + 1])
            row = {"t": " ".join(ew[c:d]), "kind": "word", "ctx": " ".join(toks[i]["t"] for i in widx[max(0, a - 4):a]) + " [" + " ".join(ew[c:d]) + "] " + " ".join(toks[i]["t"] for i in widx[a:a + 4])}
            if tn["p"] != tp["p"]:
                row.update({"before": ti_next, "p": tn["p"], "l": tn["l"]})
            elif left_cut(tn["p"]):
                row.update({"before": ti_next, "p": tn["p"], "l": tn["l"]})
            else:
                row.update({"after": ti_prev, "p": tp["p"], "l": tp["l"]})
            row["by"] = hit
            (out if hit else rejected).append(row)
        elif op == "replace" and d - c == 1:
            ti = widx[a]; t = toks[ti]; e = ew[c]
            first = ti == 0 or (toks[ti - 1]["p"], toks[ti - 1]["l"]) != (t["p"], t["l"])
            last = ti + 1 >= len(toks) or (toks[ti + 1]["p"], toks[ti + 1]["l"]) != (t["p"], t["l"])
            w = t["t"]
            if first and len(e) > len(w) and e.lower().endswith(w.lower()) and left_cut(t["p"]):
                kind, sup = "start", e[:len(e) - len(w)]
            elif last and len(e) > len(w) and e.lower().startswith(w.lower()) and not left_cut(t["p"]):
                kind, sup = "end", e[len(w):]
            else:
                continue
            hit = confirmed(nk[a - 1:a] + [key(e)] + nk[a + 1:a + 2])
            row = {"at": ti, "kind": kind, "t": sup, "word": e, "p": t["p"], "l": t["l"],
                   "ctx": " ".join(toks[i]["t"] for i in widx[max(0, a - 4):a]) + " [" + w + "→" + e + "] " + " ".join(toks[i]["t"] for i in widx[a + 1:a + 4])}
            row["by"] = hit
            (out if hit else rejected).append(row)
    (W / "gutter.json").write_text(json.dumps(out, indent=1))
    print(len(out), "supplied from the 1692 copy;", len(rejected), "not confirmed by it")
    for r in out: print("  +", r["p"], r["l"], r["kind"], r["ctx"], r["by"])
    print("not confirmed:")
    for r in rejected: print("  ?", r["p"], r["l"], r["kind"], r["ctx"])


if __name__ == "__main__":
    main()
