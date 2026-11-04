# Grace Abounding 1688: the Kraken foundation (foundation.json) as a TCP-style TEI source,
# so build_tei's TCP mode gives orig = the 1688 spelling, reg = modern.
#   emit_tei.py OUT.tcp.xml
# Structure by hand from the frames (heads, title page, closer); paragraphs from breaks.py;
# italics from italics.json (word slant), smoothed over short words; page breaks with the
# printed page numbers; letters the gutter cut, read from the 1692 copy, as <supplied>.
import json, re, sys
from difflib import SequenceMatcher
from pathlib import Path
from xml.sax.saxutils import escape
sys.path.insert(0, str(Path(__file__).parent))
from alto import lines as alto_lines
from breaks import seq_lines, breaks

W = Path(__file__).parent
SKIP = {62, 63, 87, 88, 106, 107, 120, 121}
NOSPACE_BEFORE = set(".,;:!?)]’”")
NOSPACE_AFTER = set("([“‘")
ITALIC, ROMAN = 0.15, 0.08

# section numbers the OCR lost or misread, read on the frames: (frame, line) -> (old tokens, new tokens)
NUMFIX = {
    (37, 10): (["3"], ["53"]),
    (52, 3): (["."], ["87", "."]),
    (185, 3): (["."], ["."]),              # "330" comes from the catchword line before it
    (189, 28): (["33y"], ["339"]),
    (41, 30): (["."], []),
    (124, 28): (["."], []),
    (193, 7): (["."], ["7", "."]),
    (13, 13): (["N"], ["IN"]),             # the drop capital I
}
NOT_BREAKS = {(30, 14), (50, 22)}        # (50, 22): the number "85" is the line before it
# numbered sections whose number the OCR lost or garbled (". 65.", "3." for 53, "20" printed for 90,
# a second "285"), and the preface paragraph whose first words stand in the catchword
FORCE_BREAKS = {(37, 10), (41, 30), (52, 3), (53, 25), (124, 28), (163, 21), (7, None)}
BREAK_AFTER = {(163, 21): 2}         # "33." ends the Genesis reference of the line before: break after it                    # a gutter-clipped line, not an indent
DROP_LINES = {(12, 15), (193, 21), (193, 22)}   # catchword "GRACE"; shelfmark; FINIS (set by hand)

# The preface is set in italic; its roman words (names, Scripture, references, emphasis), read
# by hand on frames 5-12, are its <hi>; the references, roman too, are left out (set roman in the
# edition as everywhere). Matched in order on the words, punctuation between kept.
PREFACE_ROMAN = [
    "Amen", "c", "Shenir", "Hermon", "the Lions Dens and from the Mountains of the Leopards",
    "THE", "for you are my Glory and Joy",
    "Sampson", "Philistines",
    "The father to the children shall make known the truth of God", "Sinai",
    "that I might fear the Lord all the days of my Life upon Earth and tell of his wondrous Works to my Children",
    "Moses", "Israel", "Egypt", "Canaan",
    "Thou shalt remember all the way which the Lord thy God led thee these forty years in the Wilderness "
    "to humble thee and to prove thee and to know what was in thine heart whether thou wouldest keep his "
    "commandments or no",
    "It is a night to be much observed to the Lord for bringing them out from the Land of Egypt This is that "
    "Night of the Lord to be observed of all the Children of Israel in their Generations",
    "My God", "David",
    "My Soul is cast down within me but I will remember thee from the Land of", "and of the", "from the Hill",
    "Gath", "Paul s", "Israel", "Red Sea",
    "Goliah", "David", "Goliah s",
    "Mizar", "but out of them all the Lord delivered me",
    "the Pangs of Hell caught hold upon me", "Farewel",
]

# the heads, by (frame, first line, last line)
PREFACE_HEAD = (5, 1, 15)
RELATION_HEAD = (13, 2, 12)
CALL_HEAD = (154, 19, 20)
PRISON_HEAD = (178, 20, 21)
CONCLUSION_HEAD = (191, 3, 3)
CLOSER = (12, 9, 14)                       # "My dear Children, ... John Bunyan."

TITLE_PAGE = """<div type="title_page">
<pb facs="f1688:1"/>
<p>Grace Abounding TO THE CHIEF OF SINNERS: OR, A Brief and Faithful Relation of the exceeding Mercy of God in Christ, to His poor Servant <hi>JOHN BUNYAN.</hi> NAMELY, In his Taking of him out of the Dunghil, and Converting of him to the Faith of his Blessed Son, Jesus Christ. HERE Is also particularly shewed, what Sight of, and what Trouble he had for Sin; and also, what various Temptations he hath met with, and how God hath carried him through them.</p>
<p>Corrected, and much Enlarged now by the Author, for the Benefit of the Tempted and Dejected Christian.</p>
<p>The Sixth Edition, Corrected.</p>
<q><hi>Come and hear, all ye that fear God, and I will declare what he hath done for my soul,</hi> <bibl>Psal. 66. 16.</bibl></q>
<p><hi>LONDON,</hi> Printed for <hi>Nath. Ponder,</hi> at the <hi>Pea-cock</hi> in the <hi>Poultry,</hi> over against the <hi>Stocks-Market,</hi> 1688.</p>
</div>"""

HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
<teiHeader>
<fileDesc>
<titleStmt>
<title>Grace abounding to the chief of sinners, or, A brief and faithful relation of the exceeding mercy of God in Christ to his poor servant John Bunyan</title>
<author>Bunyan, John, 1628-1688.</author>
</titleStmt>
<editionStmt><edition>The sixth edition, corrected (London: Nath. Ponder, 1688), transcribed for Freely Given Books</edition></editionStmt>
<publicationStmt>
<publisher>Freely Given Books</publisher>
<availability><licence target="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0: this transcription of a public-domain print is dedicated to the public domain.</licence></availability>
</publicationStmt>
<sourceDesc>
<biblFull>
<titleStmt><title>Grace abounding to the chief of sinners, or, A brief and faithful relation of the exceeding mercy of God in Christ to his poor servant John Bunyan</title><author>Bunyan, John, 1628-1688.</author></titleStmt>
<editionStmt><edition>The sixth edition, corrected.</edition></editionStmt>
<publicationStmt><publisher>Printed for Nath. Ponder</publisher><pubPlace>London</pubPlace><date>1688</date></publicationStmt>
<notesStmt><note>Transcribed from the British Library copy (Early English Books microfilm; archive.org bim_early-english-books-1641-1700_grace-abounding-to-the-c_bunyan-john_1688). Letters the gutter of that copy hides are read from the 1692 Ponder printing (archive.org bunyangraceabounding5ed) and marked &lt;supplied resp="#p1692"&gt;.</note></notesStmt>
</biblFull>
</sourceDesc>
</fileDesc>
<encodingDesc>
<projectDesc><p>Kraken (CATMuS-Print) read of every page, corrected where the witnesses outvote it (Kraken of the 1692 copy, GLM-OCR, Tesseract, archive.org OCR, CCEL, Gutenberg #654), every split read on the page image. The long s is transcribed as s; line-end hyphens as &lt;g ref="char:EOLhyphen"/&gt;; page breaks carry the printed page numbers.</p></projectDesc>
</encodingDesc>
</teiHeader>
<text xml:lang="eng">
"""


def join_toks(toks):
    """[(text, xml)] -> xml with the print's spacing"""
    out, prev = "", None
    for t, x in toks:
        if prev is not None and not (t[0] in NOSPACE_BEFORE or prev[-1] in NOSPACE_AFTER):
            out += " "
        out += x
        prev = t
    return out


def italic_words():
    """{frame:line: [(italic in roman type?, roman in italic type?, confident face)]} per ALTO
    word. Confident: italic = slanted with a clear gain over upright; roman = upright with no
    gain (not a word with y/v/w/k, whose diagonals hide an italic's slant). Short and doubtful
    words are smoothed by their neighbours."""
    raw = json.load(open(W / "italics.json"))
    keys = sorted(raw, key=lambda k: tuple(int(x) for x in k.split(":")))
    flat = [(k, i, w, s, g) for k in keys for i, (w, s, g, *_) in enumerate(raw[k])]
    lab, conf = [], []
    for k, i, w, s, g in flat:
        letters = len(re.sub(r"[^A-Za-z]", "", w))
        if s is None or letters < 3: lab.append(None)
        elif s >= ITALIC and g >= (1.05 if letters > 3 else 1.08): lab.append(True)
        elif s <= ROMAN or g < 1.02: lab.append(False)
        else: lab.append(None)
        if s is not None and letters >= 3 and s >= ITALIC and g >= 1.05: conf.append(1)
        elif s is not None and letters >= 3 and s <= 0.02 and g <= 1.005 and not re.search(r"[yvwkYVWK]", w):
            conf.append(-1)
        else: conf.append(0)

    def around(vals):
        n = len(vals)
        prev, nxt = [None] * n, [None] * n
        last = None
        for j in range(n):
            prev[j] = last
            if vals[j] is not None: last = vals[j]
        last = None
        for j in range(n - 1, -1, -1):
            nxt[j] = last
            if vals[j] is not None: last = vals[j]
        return prev, nxt

    prev_l, next_l = around(lab)
    rlab = [True if c == -1 else (False if c == 1 or lab[j] is True else None) for j, c in enumerate(conf)]
    prev_r, next_r = around(rlab)
    out = {k: [None] * len(raw[k]) for k in keys}
    for j, (k, i, w, s, g) in enumerate(flat):
        letters = len(re.sub(r"[^A-Za-z]", "", w))
        if lab[j] is not None and not (letters <= 3 and prev_l[j] and next_l[j]):
            v = lab[j]
        elif not re.search(r"[A-Za-z]", w):
            v = bool(prev_l[j] and next_l[j])          # a number or mark inside an italic run
        else:
            v = bool(prev_l[j] and next_l[j]) or (s is not None and s >= 0.2 and g >= 1.1 and bool(prev_l[j] or next_l[j]))
        r = rlab[j] if rlab[j] is not None else bool(prev_r[j] and next_r[j])
        out[k][i] = (v, r, conf[j])
    return out


def token_italics(frame, line, toks, ital):
    """(italic in roman, roman in italic, confident face) for each token of an ALTO line, by
    character alignment with Kraken's words"""
    words = alto_lines(frame)[line - 1][2]
    flags = ital.get(f"{frame}:{line}", [])
    a, owner = "", []
    for wi, (w, _) in enumerate(words):
        if a: a += " "; owner.append(None)
        a += w.lower(); owner += [wi] * len(w)
    b, starts = "", []
    for t in toks:
        if b: b += " "
        starts.append(len(b)); b += t["t"].lower()
    sm = SequenceMatcher(None, a, b, autojunk=False)
    b2a = {}
    for x, y, n in sm.get_matching_blocks():
        for d in range(n): b2a[y + d] = x + d
    res = []
    for t, st in zip(toks, starts):
        wi = None
        for c in range(st, st + len(t["t"])):
            if c in b2a and owner[b2a[c]] is not None:
                wi = owner[b2a[c]]; break
        res.append(flags[wi] if wi is not None and wi < len(flags) else None)
    # unaligned tokens follow their neighbours
    for i, v in enumerate(res):
        if v is None:
            l = next((res[j] for j in range(i - 1, -1, -1) if res[j] is not None), (False, False, 0))
            r = next((res[j] for j in range(i + 1, len(res)) if res[j] is not None), (False, False, 0))
            res[i] = (bool(l[0] and r[0]), bool(l[1] and r[1]), 0)
    return res


ROMAN_LEFT = None


def wkeys(t):
    return re.findall(r"[a-z0-9]+", t.replace("\xad", "").replace("’", " ").replace("'", " ").lower())


def preface_roman(items):
    """the hand-read roman spans of the italic preface as the tokens' contrast flag; the list is
    consumed in order across the preface's paragraphs"""
    global ROMAN_LEFT
    if ROMAN_LEFT is None:
        ROMAN_LEFT = [p.lower().split() for p in PREFACE_ROMAN]
    toks = [(i, pl) for i, (k, pl) in enumerate(items) if k == "tok"]
    seq = []                                   # (word key, item index)
    for i, pl in toks:
        for w in wkeys(pl[0]["t"]):
            seq.append((w, i))
    flags = {i: False for i, _ in toks}
    pos = 0
    while ROMAN_LEFT:
        ph = ROMAN_LEFT[0]
        hit = next((j for j in range(pos, len(seq) - len(ph) + 1)
                    if [w for w, _ in seq[j:j + len(ph)]] == ph), None)
        if hit is None:
            break
        a, b = seq[hit][1], seq[hit + len(ph) - 1][1]
        for i, _ in toks:
            if a <= i <= b: flags[i] = True
        pos = hit + len(ph)
        ROMAN_LEFT.pop(0)
    out = []
    for k, (kind, pl) in enumerate(items):
        if kind == "tok":
            t, it, f, l = pl
            out.append(("tok", (t, (it[0], flags[k], it[2]), f, l)))
        else:
            out.append((kind, pl))
    return out


def supplied_split(frame, line, tok):
    """(read, supplied) letters of a gutter-cut word: Kraken read the start (the line's last word)"""
    words = alto_lines(frame)[line - 1][2]
    t = tok["t"]
    if words:
        k = re.sub(r"[^\w]", "", words[-1][0].replace("ſ", "s"))
        if k and t.lower().startswith(k.lower()) and len(k) < len(t):
            return t[:len(k)], t[len(k):]
    return "", t


def word_xml(tok, frame, line):
    t = tok["t"]
    if t == "&c":
        return "&amp;c"
    v = tok.get("voted") or ""
    if v == "gutter":
        return f'<supplied reason="gutter" resp="{tok["resp"]}">{escape(t)}</supplied>'
    if v.startswith("gutter-"):
        sup = f'<supplied reason="gutter" resp="{tok["resp"]}">{escape(tok["sup"])}</supplied>'
        rest = t[len(tok["sup"]):] if v == "gutter-start" else t[:len(t) - len(tok["sup"])]
        return sup + escape(rest) if v == "gutter-start" else escape(rest) + sup
    if v == "supplied" and "\xad" not in t:
        read, sup = supplied_split(frame, line, tok)
        return escape(read) + f'<supplied reason="gutter" resp="#p1692">{escape(sup)}</supplied>'
    return escape(t).replace("\xad", '<g ref="char:EOLhyphen"/>')


def main(out_path):
    seq = seq_lines()
    brk = breaks(seq)
    ital = italic_words()
    # catchword lines: a page's last line, set at the right margin, holding the next page's
    # first word(s): their tokens go after the page break
    last_of = {}
    for i, x in enumerate(seq): last_of[x["frame"]] = i
    catch = set()
    for f, i in last_of.items():
        x = seq[i]
        if x["lind"] > 5 and x["right"] < 1.5 and len(x["toks"]) <= 3 and (f, x["line"]) not in DROP_LINES:
            catch.add(i)
    # page numbers: frame 13 is page 1
    def page_no(f):
        return f - 12 - sum(1 for s in SKIP if s < f) if f >= 13 else None

    # flatten into (kind, payload) events
    ev = []
    cur_frame = None
    held = []
    first_line_of_frame = False
    for i, x in enumerate(seq):
        f, l = x["frame"], x["line"]
        if f != cur_frame:
            n = page_no(f)
            ev.append(("pb", f'<pb{f" n=\"{n}\"" if n else ""} facs="f1688:{f}"/>'))
            cur_frame = f
            first_line_of_frame = True
        if (f, l) in DROP_LINES:
            continue
        toks = [dict(t) for t in x["toks"]]
        if (f, l) in NUMFIX:
            old, new = NUMFIX[(f, l)]
            assert [t["t"] for t in toks[:len(old)]] == old, (f, l, [t["t"] for t in toks[:4]])
            toks = [{"t": s, "p": f, "l": l} for s in new] + toks[len(old):]
        its = token_italics(f, l, x["toks"], ital)
        if (f, l) in NUMFIX:
            old, new = NUMFIX[(f, l)]
            its = [(False, False, 0)] * len(new) + its[len(old):]
        # merge "&" "c" into "&c"
        merged, mits = [], []
        for t, it in zip(toks, its):
            if t["t"] == "c" and merged and merged[-1]["t"] == "&":
                merged[-1] = dict(merged[-1], t="&c"); continue
            merged.append(t); mits.append(it)
        start = ((i in brk) or (f, l) in FORCE_BREAKS or (first_line_of_frame and (f, None) in FORCE_BREAKS)) \
            and (f, l) not in NOT_BREAKS
        items = [("tok", (t, it, f, l)) for t, it in zip(merged, mits)]
        k0 = BREAK_AFTER.get((f, l), 0)
        line_ev = items[:k0] + ([("break", (f, l, brk.get(i)))] if start else []) + items[k0:]
        line_ev = [("line", (f, l))] + line_ev
        if first_line_of_frame and held:         # the catchword's words open the page, after any break
            hb = [e for e in held if e[0] == "break"]
            if hb and not start:                 # a section number in the catchword opens the paragraph
                line_ev = line_ev[:1] + hb + [e for e in held if e[0] == "tok"] + line_ev[1:]
            else:
                k = 2 if start else 1
                line_ev = line_ev[:k] + [e for e in held if e[0] == "tok"] + line_ev[k:]
            held = []
        first_line_of_frame = False
        if i in catch:
            held = line_ev
        else:
            ev += line_ev
    ev += held

    # split the event stream into blocks by the hand-made regions and the breaks
    def in_range(fl, r):
        f, l = fl
        return f == r[0] and r[1] <= l <= r[2]

    blocks = []        # (kind, n, [events])
    cur = None
    region_kind = {PREFACE_HEAD: "head-preface", RELATION_HEAD: "head-relation", CALL_HEAD: "head-call",
                   PRISON_HEAD: "head-prison", CONCLUSION_HEAD: "head-conclusion", CLOSER: "closer"}
    where = None
    for kind, pl in ev:
        if kind == "line":
            r = next((k for k in region_kind if in_range(pl, k)), None)
            if r is not None:
                if cur is None or cur[0] != region_kind[r]:
                    cur = [region_kind[r], None, []]; blocks.append(cur)
            elif cur is None or cur[0] != "p" and cur[0] != "head-relation-first":
                cur = ["p", None, []]; blocks.append(cur)
            where = r
            continue
        if kind == "break" and where is None:
            cur = ["p", pl[2], []]; blocks.append(cur)
            continue
        if kind == "break":
            continue
        if cur is None:
            cur = ["p", None, []]; blocks.append(cur)
        cur[2].append((kind, pl))

    def render(items, face=0):
        """face 0: roman body, <hi> = italic; face 1 (the preface, set in italic): <hi> = roman"""
        out, run, prev = "", [], None
        parts = []          # (text, xml) with italic runs merged
        buf = []

        def flush():
            nonlocal buf
            if buf:
                # trailing punctuation leaves the run
                tail = []
                while buf and not re.search(r"\w", buf[-1][0]): tail.insert(0, buf.pop())
                if buf:
                    parts.append((buf[0][0], "<hi>" + join_toks(buf) + "</hi>", buf[-1][0]))
                for t in tail: parts.append((t[0], t[1], t[0]))
                buf = []
        for kind, pl in items:
            if kind == "pb":
                flush(); parts.append(("\x00", pl, "\x00")); continue
            t, it, f, l = pl
            it = it[face]
            x = word_xml(t, f, l)
            if it and (buf or re.search(r"\w", t["t"])):
                buf.append((t["t"], x))
            else:
                flush(); parts.append((t["t"], x, t["t"]))
        flush()
        s, last = "", None
        for first, x, lastt in parts:
            if first == "\x00":
                s += x; continue
            if last is not None and not (first[0] in NOSPACE_BEFORE or last[-1] in NOSPACE_AFTER):
                s += " "
            s += x
            last = lastt
        return s.replace("> <pb", "><pb").strip()

    # move page breaks that fall between blocks out of the paragraph that ends there
    body = {"front": [], "relation": [], "call": [], "prison": [], "conclusion": []}
    part = "front"
    out_blocks = []
    for kind, n, items in blocks:
        if kind == "head-relation": part = "relation"
        elif kind == "head-call": part = "call"
        elif kind == "head-prison": part = "prison"
        elif kind == "head-conclusion": part = "conclusion"
        lead = []
        while items and items[0][0] == "pb": lead.append(items.pop(0)[1])
        if not items:
            body[part].extend(lead); continue
        body[part].extend(lead)
        if part == "front" and not kind.startswith("head"):
            items = preface_roman(items)
        x = render(items, 1 if part == "front" and not kind.startswith("head") else 0)
        if kind.startswith("head"):
            body[part].append(f"<head>{x}</head>")
        elif kind == "closer":
            body[part].append(("closer", x))
        else:
            if n is None and part != "front":
                m = re.match(r"(\d+)\. ", x)
                n = int(m[1]) if m else None
            body[part].append(f'<p n="{n}">{x}</p>' if n else f"<p>{x}</p>")

    def fix_closer(lst):
        res = []
        for b in lst:
            if isinstance(b, tuple):
                x = b[1]
                tail = re.search(r"(<pb [^>]*/>)+$", x)
                pbs = tail[0] if tail else ""
                x = x[:len(x) - len(pbs)]
                m = re.search(r"\s*(<hi>)?John Bunyan\.?(</hi>)?\s*$", x)
                body_x = x[:m.start()] if m else x
                sig = x[m.start():].strip() if m else ""
                res.append(f"<p>{body_x}</p>")
                if sig: res.append(f"<closer><signed>{sig}</signed></closer>")
                if pbs: res.append(pbs)
            else:
                res.append(b)
        return res

    front = fix_closer(body["front"])
    # the closer, set by hand from frame 12: salute and signature italic, the blessing roman
    ci = next(i for i, b in enumerate(front) if isinstance(b, str) and "Milk and Honey" in b)
    front[ci:ci + 1] = ["<p><hi>My dear Children,</hi></p>",
                        "<p>The Milk and Honey is beyond this Wilderness: God be merciful to you, "
                        "and grant you be not slothful to go in to possess the Land.</p>",
                        "<closer><signed><hi>John Bunyan.</hi></signed></closer>"]
    front = [b for b in front if not (isinstance(b, str) and b.startswith("<closer>") and front.index(b) != ci + 2)]
    # the preface head: the title, then the dedication as its own head
    ph = front.index(next(b for b in front if b.startswith("<head>")))
    m = re.match(r"<head>(.*?WORK\.)\s*(.*)</head>$", front[ph], re.S)
    if m:
        front[ph:ph + 1] = [f"<head>{m[1]}</head>", f'<head type="sub">{m[2]}</head>']
    # the relation's head: "Grace" is on the frame but read as a running head
    rel = body["relation"]
    hi = next(i for i, b in enumerate(rel) if b.startswith("<head>"))
    rel[hi] = ('<head>Grace Abounding TO THE CHIEF OF SINNERS: OR, A brief Relation of the exceeding '
               'Mer<g ref="char:EOLhyphen"/>cy of God in Christ, to his poor Ser<g ref="char:EOLhyphen"/>vant, '
               '<hi>John Bunyan.</hi></head>')
    # the relation's first paragraph is section 1
    pi = next(i for i, b in enumerate(rel) if b.startswith("<p"))
    rel[pi] = rel[pi].replace("<p>", '<p n="1">', 1)
    conc = body["conclusion"]

    xml = HEADER + "<front>\n" + TITLE_PAGE + '\n<div type="preface">\n' + "\n".join(front) + "\n</div>\n</front>\n<body>\n"
    xml += '<div type="text">\n' + "\n".join(rel) + "\n</div>\n"
    xml += '<div type="part">\n' + "\n".join(body["call"]) + "\n</div>\n"
    xml += '<div type="part">\n' + "\n".join(body["prison"]) + "\n</div>\n"
    xml += '<div type="conclusion">\n' + "\n".join(conc) + "\n<trailer>FINIS.</trailer>\n</div>\n"
    xml += "</body>\n</text>\n</TEI>\n"
    if ROMAN_LEFT:
        print("preface roman spans not found:", [" ".join(p) for p in ROMAN_LEFT])
    Path(out_path).write_text(xml)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(W / "grace-1688.tcp.xml"))
