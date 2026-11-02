# Grace Abounding, 1688 sixth edition (Nath. Ponder; EEBO microfilm): the foundation text.
# Kraken (CATMuS-Print) read of every cropped frame is the base. Witnesses (6):
#   k1692  Kraken's read of the 1692 Ponder copy (Google photograph, nearly line for line)
#   glm    GLM-OCR of the 1688 scan            tess  Tesseract of the 1688 scan
#   djvu   archive.org's OCR of the 1688 scan   ccel  CCEL's text (a later printing, modern spelling)
#   pg     Gutenberg #654 (the 1905 RTS text, modern spelling)
# Words are compared in modern spelling (colophon's spelling.py), so "suddainly" and "suddenly"
# agree; punctuation marks vote as themselves. With Kraken, 7 voters:
#   keep    Kraken's reading is the most voted, with 3+
#   fix     another reading has 4+ and more votes than Kraken's (Tesseract and archive.org both
#           read the long s as f, so "fin" against "sin" is 3 against 4)
#   check   neither: read on the page image (decisions.json, then rerun)
# A fixed word is spelled from the 1688 witnesses where they have it (Kraken's own letters if
# only its long s was misread, else Tesseract/archive.org/1692), else the 1692 copy's. A word cut
# short at the gutter (Kraken's is the start of the reading, at a line's end) is "supplied".
# writes foundation.json (tokens with frame and line), votes.json, check.md
import json, re, sys
from collections import Counter
from pathlib import Path

try:
    from cydifflib import SequenceMatcher
except ImportError:
    from difflib import SequenceMatcher

sys.path.insert(0, str(Path.home() / "Projects/fgbooks/books/colophon"))
from spelling import modernize_word_lower  # noqa: E402

W = Path(__file__).parent
BOOK = Path.home() / "Projects/fgbooks/books/books/john-bunyan/grace-abounding/source"
X = BOOK / "ocr/ocr-witnesses/bunyan-grace-abounding-1688"
FIRST, LAST = 5, 193
SKIP = {62, 63, 87, 88, 106, 107, 120, 121}   # spreads filmed twice: the cleaner shot of each page kept

DASHES = "—–―"
TOK = re.compile(r"[^\W_]+(?:['’\-­][^\W_]+)*|[.,;:!?()\[\]“”\"‘’'«»„&" + DASHES + "]|-{2,}|-")
HEAD = re.compile(r"^\W*\d*\W*(?:[gjc]\s*r\s*a\s*c\s*e\s+a\s*b\w*|to\s+t\w{1,2}\s+\S{3,7}\s+\S{1,3}\s+s\S*|the\s+preface\w*)\W*\d*\W*$", re.I)
SIGNATURE = re.compile(r"^\W*[A-Z]{1,2}\s*\d?\W*$")
_mod = {}


def modern(w):
    if w not in _mod:
        _mod[w] = modernize_word_lower(w)
    return _mod[w]


def clean(text):
    text = text.replace("ſ", "s").replace("¬", "-").replace("­", "-")
    return re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", text)            # line-end hyphen: join


def key(t):
    """what a token votes as"""
    if t[0].isalnum():
        w = re.sub(r"['’\-­]", "", t.lower())
        return modern(w)
    if t in "“”\"‘’'«»„": return '"'
    if t in DASHES or t.startswith("-"): return "—"
    return t


def is_head(line):
    t = line.strip()
    return bool(not t or HEAD.match(t) or re.fullmatch(r"\W*\d{1,3}\W*", t))


def strip_page(lines, nxt_first=None):
    """drop the running head and page number at the top; the catchword (the next page's first
    word, repeated alone at the foot) and the signature mark ("B 2") at the bottom"""
    lines = [ln for ln in lines if not HEAD.match(ln.strip())]   # Kraken sometimes reads the head out of order
    for _ in range(3):
        if lines and is_head(lines[0]): lines.pop(0)
    while lines and (not lines[-1].strip() or SIGNATURE.match(lines[-1]) or re.fullmatch(r"\W*\d{1,3}\W*", lines[-1].strip())):
        lines.pop()
    for k in (-1, -2):                                    # a signature mark Kraken read into a text line
        if len(lines) >= -k:
            lines[k] = re.sub(r"(^|\s)[A-H]\s?\d(?=\s|$)", " ", lines[k]).strip() if \
                re.search(r"(^|\s)[A-H]\s?\d(\s|$)", lines[k]) and not re.search(r"[A-Z][a-z]+\.?\s*[A-H]\s?\d", lines[k]) else lines[k]
    lines = [ln for ln in lines if ln.strip()]
    if lines and nxt_first:
        last = lines[-1].split()
        words = [t for t in TOK.findall(" ".join(last)) if t[0].isalpha()]
        if len(last) <= 4 and words:
            w = key(words[0])
            if w == nxt_first or (len(w) >= 2 and nxt_first.startswith(w.rstrip("-"))) or \
                    (len(w) >= 2 and SequenceMatcher(None, w, nxt_first, autojunk=False).ratio() >= 0.75):
                lines.pop()                               # the catchword (with a section number)
    return lines


def first_word(lines):
    for ln in lines:
        if is_head(ln): continue
        toks = [t for t in TOK.findall(clean(ln)) if t[0].isalpha()]
        if toks: return key(toks[0])
    return None


def frames(read):
    """{frame: lines} for the book's frames"""
    return {n: read(n) for n in range(FIRST, LAST + 1) if n not in SKIP}


def stripped(pages):
    ns = sorted(pages)
    out = {}
    for i, n in enumerate(ns):
        nxt = first_word(pages[ns[i + 1]]) if i + 1 < len(ns) else None
        out[n] = strip_page(pages[n], nxt)
    return out


def kraken_lines(d, n):
    f = W / d / f"p-{n:03d}.txt"
    return f.read_text().splitlines() if f.exists() else []


def kraken():
    """Kraken tokens: (surface, frame, line), line = the line's number in Kraken's file"""
    raw = frames(lambda n: kraken_lines("kf1688", n))
    pages = stripped(raw)
    out = []
    for n in sorted(pages):
        kept = pages[n]
        first = next((i for i in range(len(raw[n])) if raw[n][i:i + len(kept)] == kept), 0)
        for ln, line in enumerate(kept, first + 1):
            line = line.replace("ſ", "s")
            m = re.search(r"([^\W\d_]+)[-¬­]\s*$", line)
            nxt_i = ln - first
            if m and nxt_i < len(kept) and re.match(r"\s*[a-z]", kept[nxt_i]):   # a word broken at the line end
                w = re.match(r"\s*\S*", kept[nxt_i])[0]
                kept[nxt_i] = kept[nxt_i][len(w):]
                line = line[:m.start()] + m[1] + "­" + w.strip()            # soft hyphen marks the join
            for t in TOK.findall(line.replace("¬", "-")):
                if out and key(t) == '"' and key(out[-1][0]) == '"' and out[-1][1:] == (n, ln):
                    continue
                out.append((t, n, ln))
    return out


def export_pages(path):
    out, cur = {}, None
    for line in Path(path).read_text().splitlines():
        m = re.match(r"--- (?:Source )?PDF page (\d+) ---", line)
        if m: cur = int(m[1]); out[cur] = []
        elif cur: out[cur].append(line)
    return out


def text_of(pages):
    return "\n".join("\n".join(v) for k, v in sorted(stripped(pages).items()))


def plain(path, start, end=None):
    s = Path(path).read_text()
    s = s[s.find(start):]
    if end: s = s[:s.find(end)]
    return "\n".join(ln for ln in s.splitlines() if not is_head(ln) or not ln.strip())


def ccel_text():
    s = (BOOK / "grace.thml.xml").read_text()
    i = s.find("Children, Grace be with you")
    if i < 0: i = s.find("<ThML.body")
    s = s[s.rfind("<", 0, i):]
    s = re.sub(r"<scripRef[^>]*>(.*?)</scripRef>", r" \1 ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return s.replace("&amp;", "&")


def seq(text):
    out, surf = [], []
    for t in TOK.findall(clean(text)):
        k = key(t)
        if out and k == out[-1] == '"':
            continue
        out.append(k); surf.append(t)
    return out, surf


def edits(a, b, bs):
    sm = SequenceMatcher(None, a, b, autojunk=False)
    return {(i1, i2): (tuple(b[j1:j2]), tuple(bs[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"}


SPELL_ORDER = ("tess", "djvu", "k1692", "glm", "ccel", "pg")
MODERN = ("ccel", "pg")


def close(x, y):
    """near-identical words (an OCR's misread letter or two), not a different word"""
    if x == y: return False
    sm = SequenceMatcher(None, x, y, autojunk=False)
    return sm.ratio() >= 0.6 and max(len(x), len(y)) - sum(b.size for b in sm.get_matching_blocks()) <= 2


def spell(kraken_t, cands):
    """the letters of a fixed word: Kraken's own with a misread long s put right, else the first
    1688 witness's, else the 1692 copy's"""
    for c in cands:
        if c and len(c) == len(kraken_t) and all(x == y or (x == "f" and y == "s") for x, y in zip(kraken_t, c)):
            return kraken_t[:0] + "".join(y if x == "f" else x for x, y in zip(kraken_t, c))
    return next((c for c in cands if c), None)


def main():
    K = kraken()
    a = [key(t) for t, _, _ in K]
    ks = [t for t, _, _ in K]
    wit = {
        "k1692": text_of({n: kraken_lines("kp1692", n) for n in range(1, 211)}),
        "glm": text_of({k: v for k, v in export_pages(X / "glm/full-text.txt").items() if FIRST <= k <= LAST and k not in SKIP}),
        "tess": text_of({k: v for k, v in export_pages(X / "tesseract/full-text.txt").items() if FIRST <= k <= LAST and k not in SKIP}),
        "djvu": plain(W / "scans/1688_djvu.txt", "Children"),
        "ccel": ccel_text(),
        "pg": plain(W / "scans/pg654.txt", "CHILDREN, Grace be with you", "*** END OF"),
    }
    E = {}
    for name, text in wit.items():
        E[name] = edits(a, *seq(text))
        print(name, len(E[name]), "edit spans", file=sys.stderr)
    # a witness that lacks (or adds) a long passage abstains over it, so its gap does not swallow the
    # other witnesses' readings into one group too long to vote on
    BIG = 15
    absent = {name: [(i1, i2) for (i1, i2), (w, _) in e.items() if max(i2 - i1, len(w)) > BIG] for name, e in E.items()}
    for name in E:
        E[name] = {k: v for k, v in E[name].items() if max(k[1] - k[0], len(v[0])) <= BIG}
    spans = sorted({s for e in E.values() for s in e})
    groups, cur = [], None
    for i1, i2 in spans:
        hi = min(max(i2, i1 + 1), len(K))
        if i1 >= len(K): continue
        if cur and i1 < cur[1]: cur[1] = max(cur[1], hi)
        else: cur = [i1, hi]; groups.append(cur)
    decisions = json.loads((W / "decisions.json").read_text()) if (W / "decisions.json").exists() else {}
    out_tokens, rows, i = [], [], 0
    tok = lambda j, **kw: dict(t=K[j][0], p=K[j][1], l=K[j][2], **kw)
    def emit(c1, c2, rd):
        """decide Kraken's tokens c1:c2 against the witnesses' readings rd {name: (keys, surfaces)}"""
        mine = a[c1:c2]
        jk = lambda r: " ".join(r)
        numeric = any(ch.isdigit() for x in ks[c1:c2] for ch in x)
        votes = Counter()
        votes[jk(mine)] += 1
        words = lambda r: [x for x in r if x[:1].isalnum()]
        modern_reads = []
        for k, (r, _) in rd.items():
            if k in MODERN:
                if not (numeric or any(ch.isdigit() for x in r for ch in x)):   # their references are restyled
                    modern_reads.append(words(r))
                continue
            votes[jk(r)] += 1
        for w in modern_reads:              # the later texts repunctuate: they vote on the words only
            hit = [c for c in votes if words(c.split()) == w]
            for c in hit: votes[c] += 1      # (a reading only they have is no candidate: they only support)
        best, n = max(votes.items(), key=lambda kv: (kv[1], kv[0] == jk(mine)))
        nm = votes[jk(mine)]
        second = max([v for r, v in votes.items() if r != best] or [0])
        p, l = K[min(c1, len(K) - 1)][1], K[min(c1, len(K) - 1)][2]
        ident = f"{p}:{l}:{' '.join(ks[max(0, c1 - 4):c1])} [{' '.join(ks[c1:c2])}] {' '.join(ks[c2:c2 + 3])}"
        chosen = None
        if best == jk(mine) and (nm >= 3 or nm >= 2 and second <= 1):
            verdict = "keep"
            joined = Counter(tuple(r) for r, _ in rd.values() if "".join(r) == "".join(mine))
            if joined:
                d, dn = joined.most_common(1)[0]
                if dn >= 3 and d != tuple(mine):          # "debauch ed" -> "debauched"
                    verdict = "divide"
                    chosen = next(rd[k][1] for k in SPELL_ORDER if k in rd and tuple(rd[k][0]) == d)
            mod = [jk(rd[k][0]) for k in MODERN if k in rd]
            if verdict == "keep" and len(mod) == 2 and mod[0] == mod[1] != jk(mine) and c2 - c1 == 1 \
                    and mine[0][:1].isalpha() and close(mod[0], mine[0]):
                verdict = "doubt"                         # both later texts read a near-identical word
                if ident in decisions:                    # settled on the page image (or by the models' agreement)
                    chosen = decisions[ident].split()
        elif best != jk(mine) and n >= 3 and n > nm or best != jk(mine) and n >= 2 and nm == 1 and n > second:
            verdict = "fix"
            names = [k for k in SPELL_ORDER if k in rd and jk(rd[k][0]) == best]
            chosen = list(rd[names[0]][1])
            joined_b = "".join(w for w in best.split() if w[:1].isalnum())
            joined_m = "".join(w for w in mine if w[:1].isalnum())
            if sum(c[0].isalnum() for c in chosen) < sum(x[0].isalnum() for x in ks[c1:c2]) and \
                    SequenceMatcher(None, joined_b, joined_m, autojunk=False).ratio() < 0.8:
                verdict, chosen = "check", None           # never drop words Kraken read: a repeated phrase misaligns
                d = decisions.get(ident)
                chosen = d.split() if d is not None else None
            kw = [x for x in ks[c1:c2] if x[0].isalnum()]
            if verdict == "fix" and len([w for w in chosen if w[0].isalnum()]) == len(kw):
                alts = [[w for w in rd[k][1] if w[0].isalnum()] for k in names]
                fixed = []
                for wi, kt in enumerate(kw):
                    cands = [al[wi] for al in alts if wi < len(al)]
                    fixed.append(spell(kt, cands) if key(kt) != key(cands[0]) else kt)
                it = iter(fixed)
                chosen = [next(it) if c[0].isalnum() else c for c in chosen]
            if verdict == "fix":
                # a mark brought in with the reading needs a 1688 witness (or 1692) with it after the same
                # word: GLM and the later texts modernize punctuation
                pairs = set()
                for k in ("tess", "djvu", "k1692"):
                    if k in rd:
                        r = rd[k][0]
                        pairs |= {(r[x - 1], r[x]) for x in range(1, len(r)) if not r[x][:1].isalnum()}
                r = mine
                pairs |= {(r[x - 1], r[x]) for x in range(1, len(r)) if not r[x][:1].isalnum()}
                if c1 and not ks[c1][:1].isalnum(): pairs.add((a[c1 - 1], a[c1]))
                kept = []
                for c in chosen:
                    if not c[:1].isalnum() and key(c) != '"':
                        prev = key(kept[-1]) if kept else (a[c1 - 1] if c1 else "")
                        if (prev, key(c)) not in pairs: continue
                    kept.append(c)
                chosen = kept
        else:
            verdict = "check"
            d = decisions.get(ident)
            chosen = d.split() if d is not None else None
        if chosen is None:
            out_tokens.extend(tok(j, **({"voted": verdict} if verdict == "doubt" else {})) for j in range(c1, c2))
        else:
            kwj = [j for j in range(c1, c2) if K[j][0][0].isalnum()]
            cw = [m for m, c in enumerate(chosen) if c[0].isalnum()]
            at = {m: (K[j][1], K[j][2]) for m, j in zip(cw, kwj)}
            cur = (p, l)
            for m, c in enumerate(chosen):
                cur = at.get(m, cur)
                v = verdict
                if verdict == "fix" and m in at:
                    j = kwj[cw.index(m)]
                    kt = K[j][0].replace("\u00ad", "")
                    line_end = j + 1 >= len(K) or K[j + 1][1:] != K[j][1:]
                    if line_end and len(kt) < len(c) and c.lower().startswith(kt.lower()):
                        v = "supplied"
                out_tokens.append(dict(t=c, p=cur[0], l=cur[1], voted=v))
        if verdict not in ("keep", "divide"):
            rows.append(dict(id=ident, page=p, line=l, verdict=verdict, kraken=" ".join(ks[c1:c2]),
                             reads={k: " ".join(v[1]) for k, v in rd.items()},
                             before=" ".join(ks[max(0, c1 - 8):c1]), after=" ".join(ks[c2:c2 + 6]),
                             decided=ident in decisions))

    for g1, g2 in groups:
        out_tokens += [tok(j) for j in range(i, g1)]
        if g2 - g1 > 40:                       # a long passage one witness lacks or adds: Kraken's
            out_tokens += [tok(j) for j in range(g1, g2)]; i = g2; continue
        reads, surfs = {}, {}
        for name in wit:
            if any(i1 <= g1 and g2 <= i2 + 1 for i1, i2 in absent[name]): continue
            r, rs, j = [], [], g1
            for (i1, i2), (w, ws) in sorted(E[name].items()):
                if not g1 <= i1 < g2: continue
                r += a[j:i1]; rs += ks[j:i1]; r += list(w); rs += list(ws); j = max(j, i2)
            r += a[j:g2]; rs += ks[j:g2]
            reads[name], surfs[name] = r, rs
        mine = a[g1:g2]
        same = [k for k in reads if len(reads[k]) == len(mine)]
        if mine and len(same) >= 3:
            cols = [(g1 + c, g1 + c + 1, {k: ([reads[k][c]], [surfs[k][c]]) for k in same}) for c in range(len(mine))]
        else:
            cols = [(g1, g2, {k: (reads[k], surfs[k]) for k in reads})]
        for c1, c2, rd in cols:
            emit(c1, c2, rd)
        i = g2
    out_tokens += [tok(j) for j in range(i, len(K))]
    for page, old, new in decisions.get("__post__", []):
        old, new = old.split(), new.split()
        hits = [i for i in range(len(out_tokens) - len(old) + 1) if page in (0, out_tokens[i]["p"])
                and [x["t"].replace("­", "") for x in out_tokens[i:i + len(old)]] == old]
        if len(hits) != 1:
            print(f"POST NOT APPLIED p{page} {' '.join(old)}: found {len(hits)} times", file=sys.stderr); continue
        i = hits[0]
        pos = [(x["p"], x["l"]) for x in out_tokens[i:i + len(old)]]
        out_tokens[i:i + len(old)] = [dict(t=w, p=pos[min(n, len(pos) - 1)][0], l=pos[min(n, len(pos) - 1)][1],
                                           voted="post") for n, w in enumerate(new)]
    (W / "foundation.json").write_text(json.dumps(out_tokens))
    (W / "votes.json").write_text(json.dumps(rows, indent=1))
    c = Counter(r["verdict"] for r in rows)
    sup = sum(1 for t in out_tokens if t.get("voted") == "supplied")
    und = [r for r in rows if r["verdict"] == "check" and not r["decided"]]
    print(len(K), "kraken tokens;", dict(c), ";", sup, "supplied;", len(und), "undecided", file=sys.stderr)
    md = [f"# Undecided ({len(und)})\n"]
    for r in und:
        md.append(f"- f{r['page']}:{r['line']} …{r['before']} **[{r['kraken'] or '∅'}]** {r['after']}…  " +
                  " | ".join(f"{k}: {t or '∅'}" for k, t in r["reads"].items()))
    (W / "check.md").write_text("\n".join(md) + "\n")


if __name__ == "__main__":
    main()
