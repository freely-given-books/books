"""Align Calvin Institutes vol-1 edition (CCEL) against 1845 OCR; list candidate differences."""
import re, sys, json, difflib, unicodedata, collections, os, pickle

BOOK = "/home/courtney/Projects/fgbooks/books/books/john-calvin/institutes-of-the-christian-religion"
ED = BOOK + "/chapters/typ/vol-2"
OCR = BOOK + "/source/instituteschrist01calvuoft.djvu.txt"
OUT = os.path.dirname(os.path.abspath(__file__))

OCR2 = BOOK + "/source/institutesofreli02calvuoft.djvu.txt"
# (file, first OCR line, last OCR line, ocr file), 1-based inclusive
RANGES = [
    ("book-2-argument", 16766, 16827, 1),
    ("book-2-chapter-01", 16828, 17539, 1),
    ("book-2-chapter-02", 17540, 19237, 1),
    ("book-2-chapter-03", 19238, 20298, 1),
    ("book-2-chapter-04", 20299, 20710, 1),
    ("book-2-chapter-05", 20711, 21969, 1),
    ("book-2-chapter-06", 21970, 22373, 1),
    ("book-2-chapter-07", 22374, 23328, 1),
    ("book-2-chapter-08", 23329, 26417, 1),
    ("book-2-chapter-09", 26418, 26723, 1),
    ("book-2-chapter-10", 26724, 27901, 1),
    ("book-2-chapter-11", 27902, 28700, 1),
    ("book-2-chapter-12", 83, 613, 2),
    ("book-2-chapter-13", 614, 979, 2),
    ("book-2-chapter-14", 980, 1552, 2),
    ("book-2-chapter-15", 1553, 2023, 2),
    ("book-2-chapter-16", 2024, 3312, 2),
    ("book-2-chapter-17", 3313, 3706, 2),
]

GREEK = re.compile(r"[Ͱ-Ͽἀ-῿֐-׿]")


def norm_word(w):
    w = unicodedata.normalize("NFKD", w)
    w = "".join(c for c in w if not unicodedata.combining(c))
    w = w.lower().replace("æ", "ae").replace("œ", "oe")
    return w


def tokens_with_spans(text):
    """Return list of (normalized token, start, end) over text."""
    out = []
    t = text.replace("’", "").replace("'", "").replace("‘", "")
    # keep char offsets aligned: we replaced apostrophes -> shifts offsets; so work on text directly
    for m in re.finditer(r"[^\W_]+(?:['’][^\W_]+)*", text):
        w = m.group(0)
        w = re.sub(r"['’]", "", w)
        n = norm_word(w)
        if GREEK.search(m.group(0)):
            n = "§grk"
        out.append((n, m.start(), m.end()))
    return out


def match_bracket(s, k):
    depth = 1
    while depth and k < len(s):
        c = s[k]
        if c == "\\":
            k += 2
            continue
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        k += 1
    return k


def strip_typst(src):
    notes = []
    out = []
    i = 0
    while True:
        j = src.find("#footnote[", i)
        if j < 0:
            out.append(src[i:])
            break
        out.append(src[i:j])
        k = match_bracket(src, j + 10)
        notes.append(clean(src[j + 10:k - 1]))
        out.append("⁣")  # invisible marker for note position
        i = k
    body = "".join(out)
    body = "\n".join(l for l in body.split("\n") if not l.startswith("== ") and not l.startswith("//"))
    return clean(body), notes


def clean(s):
    s = re.sub(r"#block\(inset: \(x: 1em\)\)\[", "", s)
    s = re.sub(r"#align\(center\)\[", "", s)
    s = re.sub(r"#(emph|smallcaps|strong|underline|super|sub)\[", "", s)
    s = re.sub(r"(?<!\\)\]", "", s)
    s = re.sub(r"\\(.)", r"\1", s)
    s = s.replace("_", "")
    return s


HEADER_RES = [
    re.compile(r"^\s*(\d{1,3})\s+[A-Z][A-Z .,'’—\-]{3,}\.?\s*$"),
    re.compile(r"^\s*[A-Z][A-Z .,'’—\-]{3,}\.?\s+(\d{1,3})\s*$"),
    re.compile(r"^\s*(?:CHAP|OHAP|CHAP\.)\.?\s+[A-Z]+\.?\s+[A-Z .,]+?(\d{1,3})\s*$"),
    re.compile(r"^\s*(\d{1,3})\s+INSTITUTES.*$"),
]
SIG_RE = re.compile(r"^\s*VOL\.\s*[I1lT]{1,3}\.?\s*\S{0,3}\s*$")


def ocr_lines(lines, a, b):
    """Return list of (line_no, text, page) for content lines; headers removed."""
    out = []
    heads = []
    for ln in range(a, b + 1):
        t = lines[ln - 1].rstrip("\n")
        if SIG_RE.match(t):
            continue
        pg = None
        for r in HEADER_RES:
            m = r.match(t)
            if m:
                pg = int(m.group(1))
                break
        if pg is not None:
            heads.append((ln, pg))
            continue
        out.append([ln, t, None])
    return out, heads


def assign_pages(content, heads, prev_page):
    # heads: sorted (ln, pg). Lines before first head: page = first head - 1 (or prev)
    hs = heads
    for c in content:
        ln = c[0]
        before = [h for h in hs if h[0] < ln]
        after = [h for h in hs if h[0] > ln]
        if before:
            p = before[-1][1]
            if after and after[0][1] - p > 1:
                # missed header(s) in between: interpolate
                frac = (ln - before[-1][0]) / (after[0][0] - before[-1][0])
                p = p + int(frac * (after[0][1] - p))
            c[2] = p
        elif after:
            c[2] = after[0][1] - 1
        else:
            c[2] = prev_page
    return content


def ocr_tokens(content, vocab):
    """Tokenize OCR lines, joining line-end splits. Returns list of (tok, raw, line_no, page)."""
    toks = []
    for ln, t, pg in content:
        raw = t.split()
        for r in raw:
            # strip footnote marker digits glued to words: wisdom.3 / be2 / ages1
            r2 = re.sub(r"(?<=[A-Za-z][.,;:!?\"')])\d{1,2}$", "", r)
            r2 = re.sub(r"(?<=[a-z])\d{1,2}(?=[.,;:!?\"')]*$)", "", r2)
            for m in re.finditer(r"[^\W_]+(?:['’][^\W_]+)*", r2):
                w = re.sub(r"['’]", "", m.group(0))
                toks.append([norm_word(w), r, ln, pg, False])
        if toks:
            toks[-1][4] = True  # line end
    # join splits across line ends (and explicit hyphen)
    out = []
    i = 0
    while i < len(toks):
        tk = toks[i]
        if tk[4] and i + 1 < len(toks):
            nx = toks[i + 1]
            joined = tk[0] + nx[0]
            if joined in vocab and (tk[0] not in vocab or nx[0] not in vocab or vocab[joined] > min(vocab.get(tk[0], 0), vocab.get(nx[0], 0))):
                out.append([joined, tk[1] + "|" + nx[1], tk[2], tk[3], nx[4]])
                i += 2
                continue
        out.append(tk)
        i += 1
    return out


def main():
    L = {1: open(OCR, encoding="utf-8", errors="replace").readlines(), 2: open(OCR2, encoding="utf-8", errors="replace").readlines()}
    # vocab from CCEL ThML (whole work) for joins & real-word test
    thml = open(BOOK + "/source/institutes.thml.xml", encoding="utf-8").read()
    thml = re.sub(r"<[^>]+>", " ", thml)
    vocab = collections.Counter(norm_word(re.sub(r"['’]", "", w)) for w in re.findall(r"[^\W_]+(?:['’][^\W_]+)*", thml))
    data = {}
    prev_page = 280
    for name, a, b, v in RANGES:
        lines = L[v]
        if v == 2 and prev_page > 100: prev_page = 1
        src = open(f"{ED}/{name}.typ", encoding="utf-8").read()
        body, notes = strip_typst(src)
        content, heads = ocr_lines(lines, a, b)
        content = assign_pages(content, heads, prev_page)
        if heads:
            prev_page = heads[-1][1]
        otoks = ocr_tokens(content, vocab)
        etoks = tokens_with_spans(body)
        ntoks = [tokens_with_spans(n) for n in notes]
        data[name] = dict(vol=v, body=body, notes=notes, etoks=etoks, ntoks=ntoks, otoks=otoks, heads=heads)
    pickle.dump(dict(data=data, vocab=vocab), open(OUT + "/prep.pkl", "wb"))
    for k, v in data.items():
        print(k, len(v["etoks"]), len(v["otoks"]), len(v["notes"]), v["heads"][:1], v["heads"][-1:] if v["heads"] else None)


if __name__ == "__main__":
    main()
