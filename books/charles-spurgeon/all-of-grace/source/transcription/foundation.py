# All of Grace, 1886 R. Carter print: the foundation text.
# Kraken (CATMuS-Print) read of every page is the base; GLM-OCR, Tesseract, archive.org's
# djvu OCR and CCEL's ThML are witnesses. Words and punctuation marks are voted on (5 voters;
# word division and case are not votes):
#   keep    Kraken's reading has 3+ voters
#   fix     3+ of the 4 witnesses agree on another reading: it replaces Kraken's
#   check   neither: read on the page image (decisions.json, then rerun)
# writes foundation.json (tokens with page and line) and check.md
import json, re, sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

W = Path(__file__).parent
X = Path.home() / "temp_codex/books/charles-spurgeon/all-of-grace/source/ocr-witnesses/spurgeon-all-of-grace-1886"
CCEL = Path.home() / "Projects/fgbooks/books/books/charles-spurgeon/all-of-grace/source/grace.thml.xml"
FIRST, LAST = 9, 134

DASHES = "—–―"
TOK = re.compile(r"[^\W_]+(?:['’\-\u00ad][^\W_]+)*|[.,;:!?()\[\]“”\"‘’'«»„" + DASHES + "]|-{2,}|-")


def clean(text):
    text = text.replace("ſ", "s").replace("¬", "-").replace("­", "-")
    text = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)           # line-end hyphen: join
    return text


def key(t):
    """what a token votes as"""
    if t[0].isalnum():
        return re.sub(r"['’\-\u00ad]", "", t.lower())
    if t in "“”\"‘’'«»„": return '"'                 # a quote mark (single or double: not a vote)
    if t in DASHES or t.startswith("-"): return "—"              # a hyphen standing alone is a dash
    return t


def is_head(line):
    """a running head ("ALL OF GRACE.", "IT IS GOD THAT JUSTIFIETH. 21") or a page number"""
    t = line.strip()
    letters = [c for c in t if c.isalpha()]
    if not letters: return bool(t) and len(t) <= 6
    up = sum(c.isupper() for c in letters) / len(letters)
    return len(t) <= 60 and len(letters) >= 4 and up >= 0.7


def strip_heads(page):
    """drop the running head or chapter title (one line in capitals) and page numbers at the
    top, a page number at the foot; a chapter's opening words in capitals stay"""
    lines = page.strip().splitlines()
    title = False
    for _ in range(4):
        if not lines: break
        t = lines[0].strip()
        if not t or re.fullmatch(r"\W*(\d+|[ivxlc]+)\W*", t) or re.fullmatch(r"\W*\d*\W*ALL OF GRACE\W*\d*\W*", t):
            lines.pop(0)                                 # blank, page number, the verso head
        elif is_head(t) and not title:
            lines.pop(0); title = True
        else:
            break
    while lines and (not lines[-1].strip() or re.fullmatch(r"\W*\d+\W*", lines[-1].strip())):
        lines.pop()
    return "\n".join(lines)


def pages_from_export(path):
    out, cur = {}, None
    for line in Path(path).read_text().splitlines():
        m = re.match(r"--- (?:Source )?PDF page (\d+) ---", line)
        if m: cur = int(m[1]); out[cur] = []
        elif cur: out[cur].append(line)
    return {k: "\n".join(v) for k, v in out.items()}


def seq(text):
    """(keys, surface tokens)"""
    out, surf = [], []
    for t in TOK.findall(clean(text)):
        k = key(t)
        if out and k in "'\"" and out[-1] in "'\"" and out[-1] != k or out and k == out[-1] == "'":
            out[-1] = surf[-1] = '"'                      # '' or "' read for one double quote
        elif out and k == out[-1] == '"':
            continue
        else:
            out.append(k); surf.append(t)
    return out, surf


def kraken():
    """Kraken tokens: (surface, page, line), line = the line's number in Kraken's file"""
    out = []
    for n in range(FIRST, LAST + 1):
        f = W / f"kraken/p-{n:03d}.txt"
        if not f.exists(): continue
        raw = f.read_text().splitlines()
        kept = strip_heads("\n".join(raw)).splitlines()
        first = next((i for i in range(len(raw)) if raw[i:i + len(kept)] == kept), 0)
        carry = ""
        for ln, line in enumerate(kept, first + 1):
            line = (carry + line).replace("ſ", "s")
            carry = ""
            m = re.search(r"([^\W\d_]+)[-¬\u00ad]\s*$", line)
            if m and ln - first < len(kept) and re.match(r"[a-z]", kept[ln - first]):   # a word broken at the line end
                carry, line = m[1], line[:m.start()]
                nxt = kept[ln - first]
                w = re.match(r"\S*", nxt)[0]
                kept[ln - first] = nxt[len(w):]
                line += carry + "\u00ad" + w; carry = ""      # soft hyphen marks the join
            for t in TOK.findall(line.replace("¬", "-")):
                if out and key(t) == '"' and key(out[-1][0]) == '"' and out[-1][1:] == (n, ln):
                    continue                                  # « « or ‘‘ read for one quote mark
                out.append((t, n, ln))
    return out


def ccel_text():
    s = CCEL.read_text()
    s = s[s.find("<ThML.body"):]
    s = re.sub(r"<scripRef[^>]*>.*?</scripRef>", " ", s, flags=re.S)   # CCEL's added references
    s = re.sub(r"<[^>]+>", " ", s)
    return s.replace("&amp;", "&")


def edits(a, b, bs):
    sm = SequenceMatcher(None, a, b, autojunk=False)
    return {(i1, i2): (tuple(b[j1:j2]), tuple(bs[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"}


def quote_open(tokens, reach=400):
    """is a double quotation open at the end of tokens? (curly marks say so; a straight one
    toggles)"""
    state = False
    for t in tokens[-reach:]:
        c = t["t"]
        if c == "“": state = True
        elif c == "”": state = False
        elif c in ('"', "«", "»", "„"): state = not state
    return state


def main():
    K = kraken()
    a = [key(t) for t, _, _ in K]
    wit = {
        "glm": "\n".join(strip_heads(v) for k, v in sorted(pages_from_export(X / "glm/full-text.txt").items()) if FIRST <= k <= LAST),
        "tess": "\n".join(strip_heads(v) for k, v in sorted(pages_from_export(X / "tesseract/full-text.txt").items()) if FIRST <= k <= LAST),
        "djvu": "\n\n".join(p for p in re.split(r"\n\s*\n", (W / "1886.djvu.txt").read_text()) if not is_head(p.replace("\n", " "))),
        "ccel": ccel_text(),
    }
    E = {}
    for name, text in wit.items():
        E[name] = edits(a, *seq(text))
        print(name, len(E[name]), "edit spans", file=sys.stderr)
    spans = sorted({s for e in E.values() for s in e})
    groups, cur = [], None
    for i1, i2 in spans:
        hi = max(i2, i1 + 1)
        if cur and i1 < cur[1]: cur[1] = max(cur[1], hi)
        else: cur = [i1, hi]; groups.append(cur)
    decisions = json.loads((W / "decisions.json").read_text()) if (W / "decisions.json").exists() else {}
    out_tokens, rows, i = [], [], 0
    for g1, g2 in groups:
        out_tokens += [dict(t=K[j][0], p=K[j][1], l=K[j][2]) for j in range(i, g1)]
        reads, surfs = {}, {}
        ks = [t for t, _, _ in K]
        for name in wit:
            r, rs, j = [], [], g1
            for (i1, i2), (w, ws) in sorted(E[name].items()):
                if not g1 <= i1 < g2: continue
                r += a[j:i1]; rs += ks[j:i1]; r += list(w); rs += list(ws); j = max(j, i2)
            r += a[j:g2]; rs += ks[j:g2]
            reads[name], surfs[name] = r, rs
        mine = a[g1:g2]
        jk = lambda r: "".join(x for x in r)
        votes = Counter(jk(r) for r in reads.values())
        votes[jk(mine)] += 1
        best, n = max(votes.items(), key=lambda kv: (kv[1], kv[0] == jk(mine)))
        p, l = K[min(g1, len(K) - 1)][1], K[min(g1, len(K) - 1)][2]
        ident = f"{p}:{l}:{' '.join(t for t, _, _ in K[max(0, g1 - 4):g2 + 3])}"
        if votes[jk(mine)] >= 3:
            verdict, chosen = "keep", None
            # same words, but 3+ witnesses divide them otherwise ("Fa ther", "W ho"): theirs
            div = Counter(tuple(r) for r in reads.values() if jk(r) == jk(mine))
            if div:
                d, dn = div.most_common(1)[0]
                if dn >= 3 and d != tuple(mine):
                    verdict = "divide"
                    chosen = next(surfs[k] for k in ("glm", "ccel", "tess", "djvu") if tuple(reads[k]) == d)
        elif n >= 3:
            verdict = "fix"
            # in the words of the first witness that has it (GLM keeps case and quotes best)
            chosen = next(surfs[k] for k in ("glm", "ccel", "tess", "djvu") if jk(reads[k]) == best)
        else:
            verdict = "check"
            chosen = decisions.get(ident)
            chosen = chosen.split() if chosen is not None else None
        if chosen is None:
            out_tokens += [dict(t=K[j][0], p=K[j][1], l=K[j][2]) for j in range(g1, g2)]
        else:
            # punctuation ahead of the reading's first word closes what came before and stays on
            # the line of the token before the group; a quote mark there closes if a quotation
            # is open at that point, else it opens the words after it
            pp, pl = (K[g1 - 1][1], K[g1 - 1][2]) if g1 else (p, l)
            # each word of the reading on the line of the Kraken word it lines up with
            kw = [j for j in range(g1, g2) if K[j][0][0].isalnum()]
            cw = [n for n, c in enumerate(chosen) if c[0].isalnum()]
            at = {}
            for n, j in zip(cw, kw): at[n] = (K[j][1], K[j][2])
            cur = (p, l)
            lead = True
            for n, c in enumerate(chosen):
                if c[0].isalnum(): lead = False
                cur = at.get(n, cur)
                back = lead
                if lead and key(c) == '"' and c not in "‘’'":
                    closing = quote_open(out_tokens)
                    c = "”" if closing else "“"
                    back = closing
                pos = (pp, pl) if back else cur
                out_tokens.append(dict(t=c, p=pos[0], l=pos[1], voted=verdict))
        if verdict not in ("keep", "divide"):
            rows.append(dict(id=ident, page=p, line=l, verdict=verdict, kraken=" ".join(t for t, _, _ in K[g1:g2]),
                             reads={k: " ".join(v) for k, v in reads.items()},
                             before=" ".join(t for t, _, _ in K[max(0, g1 - 8):g1]),
                             after=" ".join(t for t, _, _ in K[g2:g2 + 6]),
                             decided=ident in decisions))
        i = g2
    out_tokens += [dict(t=K[j][0], p=K[j][1], l=K[j][2]) for j in range(i, len(K))]
    (W / "foundation.json").write_text(json.dumps(out_tokens))
    (W / "votes.json").write_text(json.dumps(rows, indent=1))
    c = Counter(r["verdict"] for r in rows)
    und = [r for r in rows if r["verdict"] == "check" and not r["decided"]]
    print(len(K), "kraken tokens;", dict(c), ";", len(und), "undecided", file=sys.stderr)
    md = [f"# Undecided ({len(und)})\n"]
    for r in und:
        md.append(f"- p{r['page']}:{r['line']} …{r['before']} **[{r['kraken'] or '∅'}]** {r['after']}…  " +
                  " | ".join(f"{k}: {t or '∅'}" for k, t in r["reads"].items()))
    (W / "check.md").write_text("\n".join(md) + "\n")


if __name__ == "__main__":
    main()
