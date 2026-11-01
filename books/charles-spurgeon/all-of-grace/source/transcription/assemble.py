# All of Grace: our own ThML transcription of the 1886 R. Carter print, from foundation.json
# (Kraken's text corrected by the witness vote). Layout from the print: Tesseract's line boxes
# matched to Kraken's lines give paragraph indents and the small-type quotations and verse;
# CCEL's ThML gives only the chapter divisions (its titles, checked against the print's headings).
#   assemble.py OUT.thml.xml
import csv, json, re, sys
from collections import Counter
from difflib import SequenceMatcher
from html import escape
from pathlib import Path
from statistics import median

W = Path(__file__).parent
X = Path.home() / "temp_codex/books/charles-spurgeon/all-of-grace/source/ocr-witnesses/spurgeon-all-of-grace-1886"
CCEL = Path.home() / "Projects/fgbooks/books/books/charles-spurgeon/all-of-grace/source/grace.ccel.witness.xml"
OFFSET = 6                                     # printed page = scan page - 6
sys.path.insert(0, str(W))
from foundation import key, is_head, TOK, pages_from_export, ccel_text

T = json.loads((W / "foundation.json").read_text())


# --- geometry: Kraken line -> (left, right, height) from Tesseract's TSV ---------------------
def tess_lines(page):
    f = X / f"tesseract/pages/{page:06d}.tsv"
    rows = [r for r in csv.DictReader(open(f), delimiter="\t", quoting=csv.QUOTE_NONE)
            if r["level"] == "5" and (r.get("text") or "").strip()]
    by = {}
    for r in rows:
        by.setdefault((int(r["block_num"]), int(r["par_num"]), int(r["line_num"])), []).append(r)
    out = []
    for ws in by.values():
        l = min(int(w["left"]) for w in ws); r = max(int(w["left"]) + int(w["width"]) for w in ws)
        t = min(int(w["top"]) for w in ws)
        h = median(int(w["height"]) for w in ws if re.search(r"[a-z]", w["text"]) or True)
        out.append(dict(top=t, left=l, right=r, h=h, text=" ".join(w["text"] for w in ws)))
    return sorted(out, key=lambda x: x["top"])


def geometry():
    geo = {}
    for page in sorted({t["p"] for t in T}):
        raw = (W / f"kraken/p-{page:03d}.txt").read_text().splitlines()
        tl = tess_lines(page)
        if not tl: continue
        body = [x for x in tl if len(x["text"]) > 30]
        H = median(x["h"] for x in body) if body else 32
        left = Counter(round(x["left"] / 4) for x in body).most_common(1)[0][0] * 4 if body else 0
        right = median(x["right"] for x in body) if body else 0
        # monotone match: each Kraken line to the most similar Tesseract line at or after the last
        j = 0
        for i, line in enumerate(raw, 1):
            best, bj = 0, None
            for k in range(j, min(j + 4, len(tl))):
                r = SequenceMatcher(None, line.lower(), tl[k]["text"].lower()).ratio()
                if r > best: best, bj = r, k
            if bj is not None and best > 0.5:
                x = tl[bj]; j = bj + 1
                geo[(page, i)] = dict(indent=(x["left"] - left) / H, short=(right - x["right"]) / H,
                                      small=x["h"] / H, text=line, tl=bj)
    return geo


# --- chapters from CCEL ---------------------------------------------------------------------
def ccel_chapters():
    s = CCEL.read_text()
    out = []
    for m in re.finditer(r'<div1 title="([^"]*)"[^>]*>(.*?)</div1>', s, re.S):
        title, body = m[1].replace("&quot;", '"'), m[2]
        if title == "Title Page": continue
        body = re.sub(r"<h\d[^>]*>.*?</h\d>", " ", body, count=1, flags=re.S)
        body = re.sub(r"<scripRef[^>]*>.*?</scripRef>", " ", body, flags=re.S)
        words = [key(t) for t in TOK.findall(re.sub(r"<[^>]+>", " ", body)) if t[0].isalnum()]
        out.append((title, words))
    return out


def find_starts(chapters, T):
    """each chapter's first token: CCEL's first words placed by aligning all of CCEL with the
    text, then snapped to the top of the page (chapters open a page in this print)"""
    keys = [key(t["t"].replace(SC_ON, "").replace(SC_OFF, "").split()[0]) for t in T]
    widx = [i for i, k in enumerate(keys) if k[0].isalnum()]
    wkeys = [keys[i] for i in widx]
    cwords, cstart = [], []
    for title, words in chapters:
        cstart.append(len(cwords)); cwords += words
    sm = SequenceMatcher(None, cwords, wkeys, autojunk=False)
    blocks = sm.get_matching_blocks()
    starts = []
    for n, c in enumerate(cstart):
        if n == 0: starts.append(0); continue
        mb = next(b for b in blocks if b.a + b.size > c and b.size >= 3)
        w = mb.b + (c - mb.a)
        i = widx[max(0, min(w, len(widx) - 1))]
        page = T[i]["p"]
        first = next(j for j in range(len(T)) if T[j]["p"] == page)
        lines_before = len({T[j]["l"] for j in range(first, i)})
        if lines_before <= 4: i = first
        else: print(f"chapter {chapters[n][0]!r} starts inside p{page} (line {T[i]['l']})", file=sys.stderr)
        starts.append(i)
    return starts


# the chapters: (scan page, heading as printed, its second line in Kraken's file when it runs
# over). Read from Kraken's page tops (a title in capitals, no page number, the text's first
# word in capitals); the running heads that repeat or shorten a title are left out.
CHAPTERS = [
    (9, "TO YOU!", None), (11, "WHAT ARE WE AT?", None), (13, "GOD JUSTIFIETH THE UNGODLY.", None),
    (24, "“IT IS GOD THAT JUSTIFIETH.”", None), (32, "JUST AND THE JUSTIFIER.", None),
    (39, "CONCERNING DELIVERANCE FROM SINNING.", "NING."), (47, "BY GRACE THROUGH FAITH.", None),
    (50, "FAITH, WHAT IS IT?", None), (56, "HOW MAY FAITH BE ILLUSTRATED?", None),
    (64, "WHY ARE WE SAVED BY FAITH?", None), (70, "ALAS! I CAN DO NOTHING!", None),
    (86, "THE INCREASE OF FAITH.", None), (92, "REGENERATION AND THE HOLY SPIRIT.", None),
    (96, "“MY REDEEMER LIVETH.”", None), (99, "REPENTANCE MUST GO WITH FORGIVENESS.", "NESS."),
    (107, "HOW REPENTANCE IS GIVEN.", None), (113, "THE FEAR OF FINAL FALLING.", None),
    (120, "CONFIRMATION.", None), (126, "WHY SAINTS PERSEVERE.", None), (131, "CLOSE.", None),
]


def kraken_chapters(T):
    first_tok = {}
    for i, t in enumerate(T):
        first_tok.setdefault(t["p"], i)
    return [(title, first_tok[page]) for page, title, _ in CHAPTERS]


def title_runover(T, RAW):
    """token indexes of a heading's second line"""
    out = set()
    for page, _, second in CHAPTERS:
        if not second: continue
        for i, t in enumerate(T):
            if t["p"] == page and RAW.get((page, t["l"]), "").strip() == second \
                    and key(t["t"]) in [key(w) for w in TOK.findall(second)]: out.add(i)
    return out


# --- text -------------------------------------------------------------------------------------
NOSPACE_BEFORE = set(".,;:!?)’”»")
NOSPACE_AFTER = set("(“‘«")


# small capitals as the print sets them: (scan page, Kraken's run in capitals) -> text, a capital
# letter where the print has a full capital (chapter openings, I, proper names)
SC = {
    (9, "THE"): "The", (11, "HEARD"): "heard", (11, "ALL OF GRACE"): "all of grace",
    (13, "LISTEN"): "Listen", (16, "UNGODLY"): "ungodly",
    (29, "BELIEVE IN THE FORGIVENESS OF SINS"): "believe in the forgiveness of sins", (29, "YOU"): "you",
    (31, "AT ONCE"): "at once", (32, "WE"): "We", (47, "THINK"): "think", (49, "HIM"): "him",
    (50, "WHAT"): "What", (55, "HE THAT BELIEVETH IN HIM HATH EVERLASTING LIFE"): "He that believeth in him hath everlasting life",
    (64, "WHY"): "Why", (70, "AFTER"): "After", (96, "CONTINUALLY"): "Continually", (99, "IT"): "It",
    (106, "BY GRACE ARE YE SAVED"): "By grace are ye saved", (112, "CHRIST IS ALL"): "Christ is all",
    (113, "DARK"): "dark", (120, "WANT"): "want",
    (120, "SECURITY WHICH PAUL CONFIDENTLY EXPECTED"): "security which Paul confidently expected",
    (86, "HOW CAN WE OBTAIN AN INCREASE OF FAITH"): "How can we obtain an increase of faith", (126, "THE"): "The", (127, "ALL OF GRACE"): "all of grace", (131, "IF"): "If",
    (132, "BESEECH YOU"): "beseech you", (132, "DO NOT TURN AWAY FROM YOUR REDEEMER"): "Do not turn away from your Redeemer",
    (134, "READER"): "Reader", (134, "MEET ME IN HEAVEN"): "meet me in heaven", (134, "NOW OR NEVER"): "now or never",
}
SC_ON, SC_OFF = "\x01", "\x02"
IT_ON, IT_OFF = "\x03", "\x04"


def mark_italics(toks, geo):
    """t["it"] for words the slant measure (italics.json) finds italic"""
    f = W / "italics.json"
    if not f.exists(): return
    ital = json.loads(f.read_text())
    # a word's own roman slant: its median over the book (letters like v, w, y, A lean)
    from statistics import median as med
    allw = {}
    for v in ital.values():
        for w, sl in v:
            if sl is not None: allw.setdefault(re.sub(r"\W", "", w).lower(), []).append(sl)
    base = {w: med(v) for w, v in allw.items() if len(v) >= 3}
    diag = lambda w: sum(c in "vwyxkAVWXYK" for c in w) / max(1, len(w))

    def is_it(w, sl):
        """2: clearly italic (0.15-0.36, above the word's own baseline); 1: at the measure's
        edge, italic only beside a clear one; 0: roman"""
        k = re.sub(r"\W", "", w)
        if k.lower() in base and sl - base[k.lower()] <= 0.12: return 0
        if 0.15 <= sl <= 0.36: return 2 if diag(k) < 0.25 or sl >= 0.2 else 1
        return 1 if sl > 0.36 else 0
    lines = {}
    for i, t in enumerate(toks):
        lines.setdefault((t["p"], t["l"]), []).append(i)
    for ln, idx in lines.items():
        g = geo.get(ln)
        if not g: continue
        tw = ital.get(f"{ln[0]}:{g['tl']}", [])
        tk = [key(TOK.findall(w)[0]) if TOK.findall(w) else "" for w, _ in tw]
        sl = [s if s is not None else 0 for _, s in tw]
        raw_it = [is_it(tw[n][0], x) for n, x in enumerate(sl)]
        flag = []
        for n, x in enumerate(raw_it):
            w = re.sub(r"\W", "", tw[n][0])
            near = (n and raw_it[n - 1] == 2) or (n + 1 < len(raw_it) and raw_it[n + 1] == 2)
            flag.append(x == 2 and (len(w) > 3 or near) or x == 1 and near)
        for n in range(1, len(flag) - 1):              # "a Prince and a Saviour": a short word inside
            if not flag[n] and flag[n - 1] and flag[n + 1] and len(re.sub(r"\W", "", tw[n][0])) <= 2:
                flag[n] = True
        words = [i for i in idx if toks[i]["t"][0].isalnum()]
        sm = SequenceMatcher(None, [key(toks[i]["t"]) for i in words], tk, autojunk=False)
        for a, b, size in sm.get_matching_blocks():
            for d in range(size):
                if flag[b + d]: toks[words[a + d]]["it"] = True


def small_caps(toks):
    """runs of capitals -> one token wrapped in SC_ON/SC_OFF, as SC gives them"""
    out, i = [], 0
    caps = lambda w: re.fullmatch(r"[A-Z][A-Z’'-]*", w) is not None
    while i < len(toks):
        j = i
        while j < len(toks) and caps(toks[j]["t"]) and toks[j]["p"] == toks[i]["p"]: j += 1
        run = " ".join(t["t"] for t in toks[i:j])
        hit = SC.get((toks[i]["p"], run)) if j > i else None
        if hit is None and j > i + 1:                  # "I BESEECH YOU": a leading I stays a capital
            hit2 = SC.get((toks[i]["p"], " ".join(t["t"] for t in toks[i + 1:j])))
            if hit2 is not None:
                out.append(toks[i]); i += 1; continue
        if hit is not None:
            out.append(dict(toks[i], t=SC_ON + hit + SC_OFF)); i = j
        else:
            out.append(toks[i]); i += 1
    return out


QUOTES = ('"', "«", "»", "„", "'", "‘", "’", "“", "”")


def curl(tokens):
    """quote marks: Kraken's curly ones kept; straight ones and guillemets by alternation
    (a paragraph starts with no quotation open); « » are double"""
    out, open_d, open_s = [], False, False
    for i, t in enumerate(tokens):
        if t in QUOTES:
            single = t in ("'", "‘", "’")
            prev = out[-1] if out else ""
            nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
            if not nxt or nxt[0] in ".,;:!?)—": opening = False          # at the end: closing
            elif not prev or prev in "—(": opening = True              # at the start: opening
            elif not single:
                opening = not open_d                                   # double quotes alternate
            elif t in ("‘",): opening = True
            elif t in ("’",): opening = False
            else:
                opening = not (open_s if single else open_d)
                prev = out[-1] if out else ""
                if not prev or prev in "—(": opening = True
            if single: open_s = opening
            else: open_d = opening
            t = ("‘" if opening else "’") if single else ("“" if opening else "”")
        out.append(t)
    return out


def join(tokens):
    s = ""
    for t in tokens:
        if t == "-" or t == "–" or t.startswith("--"): t = "—"
        t = re.sub(r"(?<=\w)'(?=\w)", "’", t)
        if not s: s = t; continue
        if t[0] in NOSPACE_BEFORE or s[-1] in NOSPACE_AFTER or t == "—" or s[-1] == "—" \
                or t == IT_OFF or s[-1] == IT_ON or (t[0] in NOSPACE_BEFORE) \
                or (s[-1] == IT_OFF and t[0] in NOSPACE_BEFORE):
            s += t
        else:
            s += " " + t
    return s


def hyphens(text_witnesses):
    """for each word joined at a line end: keep a hyphen where GLM or CCEL hyphenate it"""
    hy = set()
    for text in text_witnesses:
        for w in re.findall(r"[^\W_]+(?:-[^\W_]+)+", text.lower()):
            hy.add(w)
    return hy


def raw_lines():
    return {(n, i): line for n in sorted({t["p"] for t in T})
            for i, line in enumerate((W / f"kraken/p-{n:03d}.txt").read_text().splitlines(), 1)}


def main(out_path):
    geo = geometry()
    RAW = raw_lines()
    # a word broken at a line end: a hyphen where CCEL hyphenates it, or where the joined form
    # is no word but both halves are ("Book-reading"); else joined ("commendation"). GLM is
    # no guide: it keeps the print's line-end hyphens.
    HY = hyphens([ccel_text()])
    vocab = set(w.strip().lower() for w in open("/usr/share/dict/cracklib-small"))
    vocab |= set(w.lower() for w in re.findall(r"[^\W\d_]+", ccel_text()))
    known = lambda w: w in vocab or re.sub(r"(s|es|ed|d|ing|ly|'s)$", "", w) in vocab
    toks = []
    for t in T:
        s = t["t"]
        if "\u00ad" in s:
            a, b = s.split("\u00ad", 1)
            whole = (a + b).lower()
            hy = f"{a}-{b}".lower() in HY or (not known(whole) and known(a.lower()) and known(b.lower()))
            s = f"{a}-{b}" if hy else a + b
        toks.append(dict(t, t=s))
    mark_italics(toks, geo)
    toks = small_caps(toks)
    found = kraken_chapters(toks)
    chapters = [(t, None) for t, _ in found]
    starts = [i for _, i in found]
    G0 = dict(indent=0, short=0, small=1, text="")

    def small(ln):
        return geo.get(ln, G0)["small"] < 0.8

    # before each chapter's first word, on its page: heading lines are left out, an epigraph
    # (small type between heading and text) opens the chapter
    drop = title_runover(toks, RAW)
    for ci, st in enumerate(starts):
        j, new_st, seen_head, cand = st - 1, st, False, set()
        while j >= 0 and toks[j]["p"] == toks[st]["p"] and toks[j]["l"] < toks[st]["l"]:
            ln = (toks[j]["p"], toks[j]["l"])
            if is_head(RAW.get(ln, "")): drop.add(j); seen_head = True
            elif seen_head: break
            else: cand.add(ln); new_st = j
            j -= 1
        top = j < 0 or toks[j]["p"] != toks[st]["p"]
        if not (seen_head or top) or len(cand) > 3:
            new_st = st                                # no heading found: the text starts where CCEL's does
        starts[ci] = new_st if ci else 0
    # blocks: [kind, [token idx], [verse break positions]], kind p / quote / verse
    body = []
    for ci, st in enumerate(starts):
        end = starts[ci + 1] if ci + 1 < len(starts) else len(toks)
        blocks, cur, last_line = [], None, None
        for i in range(st, end):
            if i in drop: continue
            ln = (toks[i]["p"], toks[i]["l"])
            if ln != last_line:
                g = geo.get(ln, G0)
                frag = len(RAW.get(ln, "").split()) < 3 and g["indent"] > 4      # a piece Kraken split off a line
                if frag and cur is not None:
                    last_line = ln; cur[1].append(i); continue
                raw = RAW.get(ln, "")
                if is_head(raw) and g["indent"] > 1.5 and len(raw.split()) <= 8:
                    cur = ["center", [], []]; blocks.append(cur); last_line = ln
                    cur[1].append(i); continue
                if cur and cur[0] == "center":
                    cur = None
                sm = g["small"] < 0.8
                nxt = (ln[0], ln[1] + 1); prv = (ln[0], ln[1] - 1)
                run = sm and (small(nxt) or small(prv) or g["indent"] > 1.5)
                kind = ("verse" if g["indent"] > 1.5 or (cur and cur[0] == "verse") else "quote") if run else "p"
                new = cur is None or kind != cur[0] or kind == "p" and g["indent"] > 0.8 \
                    or kind == "quote" and g["indent"] > 0.8
                if new:
                    cur = [kind, [], []]; blocks.append(cur)
                elif kind == "verse":
                    cur[2].append(len(cur[1]))         # a verse line break
                last_line = ln
            cur[1].append(i)
        body.append((chapters[ci][0], blocks))
    # emit
    lines = [HEAD]
    lastp = None
    for n, (title, blocks) in enumerate(body, 1):
        lines.append(f'<div1 title="{escape(title, quote=True)}" id="ch{n}">')
        lines.append(f"<h2>{escape(title, quote=False)}</h2>")
        for kind, idx, breaks in blocks:
            seq, flags = [], []                         # tokens, "\n" verse breaks, ("pb", n)
            for k, i in enumerate(idx):
                if k in breaks: seq.append("\n"); flags.append(None)
                if toks[i]["p"] != lastp:
                    seq.append(("pb", toks[i]["p"] - OFFSET)); flags.append(None); lastp = toks[i]["p"]
                seq.append(toks[i]["t"]); flags.append(toks[i].get("it", False))
            words = curl([x for x in seq if isinstance(x, str) and x != "\n"])
            it = iter(words)
            seq = [next(it) if isinstance(x, str) and x != "\n" else x for x in seq]
            # italic runs: from an italic word to the last italic word before a roman one
            tok_pos = [n for n, x in enumerate(seq) if isinstance(x, str) and x != "\n"]
            on = None; out_seq = list(seq); ins = []
            wordpos = [n for n in tok_pos if seq[n][0].isalnum()]
            for wi, n in enumerate(wordpos):
                if flags[n] and on is None: on = n
                nxt_it = wi + 1 < len(wordpos) and flags[wordpos[wi + 1]]
                if on is not None and not nxt_it:
                    ins.append((on, n)); on = None
            for a, b in reversed(ins):
                out_seq.insert(b + 1, IT_OFF); out_seq.insert(a, IT_ON)
            seq = out_seq
            pre = ""
            while seq and isinstance(seq[0], tuple):
                pre += f'<pb n="{seq[0][1]}"/>'; seq.pop(0)
            text, run = "", []
            def flush():
                nonlocal text, run
                if run:
                    segs, cur_s = [], []
                    for x in run:
                        if x == "\n": segs.append(cur_s); cur_s = []
                        else: cur_s.append(x)
                    segs.append(cur_s)
                    piece = "<br />\n".join(escape(join(sg), quote=False) for sg in segs)
                    first = re.sub(r"^[\x01-\x04<]+|^<[^>]*>", "", piece)[:1]
                    text += (" " if text and not (first and first in NOSPACE_BEFORE)
                             and not re.search(r"[“‘(\x01\x03]$", re.sub(r"<pb[^>]*/>$", "", text)) else "") + piece
                    run = []
            for x in seq:
                if isinstance(x, tuple):
                    flush(); text += f'<pb n="{x[1]}"/>'
                else:
                    run.append(x)
            flush()
            text = text.replace(SC_ON, '<span class="sc">').replace(SC_OFF, "</span>")
            text = text.replace(IT_ON + " ", IT_ON).replace(" " + IT_OFF, IT_OFF)
            text = text.replace(IT_ON, "<i>").replace(IT_OFF, "</i>")
            if kind == "p":
                lines.append(f"{pre}<p>{text}</p>")
            elif kind == "center":
                lines.append(f'{pre}<p class="Centered">{text}</p>')
            elif kind == "quote":
                lines.append(f"{pre}<blockquote><p>{text}</p></blockquote>")
            else:
                lines.append(f'{pre}<blockquote><p class="left">{text}</p></blockquote>')
        lines.append("</div1>")
    lines.append("</ThML.body>\n</ThML>\n")
    Path(out_path).write_text("\n".join(lines))
    print(len(body), "chapters;", sum(len(b) for _, b in body), "blocks;", len(drop), "heading tokens left out", file=sys.stderr)


HEAD = """<?xml version="1.0" encoding="UTF-8"?>
<ThML>
<ThML.head>
<generalInfo>
  <description>C. H. Spurgeon's All of Grace, transcribed from the 1886 New York printing (Robert Carter &amp; Brothers) for Freely Given Books.</description>
  <pubHistory>First published London, 1886 (Passmore &amp; Alabaster); the same year in New York by Robert Carter &amp; Brothers.</pubHistory>
  <comments>Transcribed from the archive.org scan of the Robert Carter &amp; Brothers printing (Princeton Theological Seminary Library, allofgraceearnes00spur): the Kraken OCR (CATMuS-Print model) of every page, corrected where GLM-OCR, Tesseract, archive.org's OCR and CCEL's text outvote it, and read on the page image where they split. Page breaks are the printed pages, kept as pb; paragraphs and the small-type quotations and verse follow the print's layout. Running heads, page numbers and the library's plates and date slip are left out.</comments>
</generalInfo>
<printSourceInfo>
  <published>All of Grace: An Earnest Word with Those Who Are Seeking Salvation by the Lord Jesus Christ, by C. H. Spurgeon (New York: Robert Carter &amp; Brothers, 530 Broadway, 1886).</published>
</printSourceInfo>
<electronicEdInfo>
  <publisherID>fgb</publisherID>
  <authorID>spurgeon</authorID>
  <bookID>grace</bookID>
  <DC>
    <DC.Title>All of Grace</DC.Title>
    <DC.Creator sub="Author">C. H. Spurgeon</DC.Creator>
    <DC.Creator sub="Author" scheme="file-as">Spurgeon, Charles Haddon (1834-1892)</DC.Creator>
    <DC.Publisher>Freely Given Books</DC.Publisher>
    <DC.Date sub="Created">2026-11-01</DC.Date>
    <DC.Source>All of Grace (New York: Robert Carter &amp; Brothers, 1886), archive.org allofgraceearnes00spur.</DC.Source>
    <DC.Language scheme="ISO639-3">eng</DC.Language>
    <DC.Rights>Public Domain (CC0 1.0 for this transcription)</DC.Rights>
  </DC>
</electronicEdInfo>
</ThML.head>
<ThML.body>
<div1 title="Title Page" id="i">
<h1>All of Grace.</h1>
<p class="Centered">An Earnest Word with Those Who Are Seeking Salvation by the Lord Jesus Christ.</p>
<h2>By C. H. Spurgeon.</h2>
<p class="Centered">“Where sin abounded, grace did much more abound.” Romans v. 20.</p>
<p class="Centered">New York: Robert Carter &amp; Brothers, 530 Broadway, 1886.</p>
</div1>"""

if __name__ == "__main__":
    main(sys.argv[1])
