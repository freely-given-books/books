#!/usr/bin/env python3
"""
Before and after: a book's earlier published EPUB next to the one the TEI
pipeline builds now, paragraph by paragraph, every change marked.

  python3 before_after.py OLD.epub NEW.epub OUT.html [--title T]
                          [--old-label L] [--new-label L]

Both EPUBs are read the same way (body text in spine order, footnotes set
inline where their markers are), so the page shows what a reader of each
got, whatever built it (Typst + pandoc + Calibre before, tei_epub.py now).
Paragraphs are paired by the words they share, so a paragraph split, joined
or moved shows as one row. Each change is classed (wording, spelling,
capitals, punctuation, quotation marks, spacing, paragraphs) and the page
can show or hide each class, show only the rows that changed, and step from
change to change (n / p). It is for reading only.

./fgb changes BOOK finds the old EPUB in git (the last version before the
book's TEI was added) and builds the new one.
"""

import argparse
import collections
import difflib
import html
import re
import zipfile
from pathlib import PurePosixPath

from lxml import etree

XHTML = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
BLOCKS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "dt", "dd", "td", "th",
          "figcaption", "pre", "blockquote", "div", "section", "aside", "header",
          "footer", "nav", "figure", "ol", "ul", "dl", "table", "tr", "tbody",
          "thead", "body", "hr"}
SKIP = {"script", "style", "head"}
ITALIC = {"i", "em", "cite"}
TOKEN_RE = re.compile(r"\w+(?:[’'‐-]\w+)*|[^\w\s]", re.U)

KINDS = [  # (class, label, shown by default)
    ("wording", "wording", True),
    ("grammar", "grammar (thereof, unto, hath, thou)", True),
    ("spelling", "spelling", True),
    ("case", "capitals", True),
    ("punct", "punctuation", True),
    ("quotes", "quotation marks and dashes", False),
    ("spacing", "spacing", False),
    ("para", "paragraph breaks", True),
]


def local(el):
    return etree.QName(el).localname if isinstance(el.tag, str) else ""


# -- reading an EPUB -----------------------------------------------------------

def spine(z):
    opf = next(n for n in z.namelist() if n.endswith(".opf"))
    base = PurePosixPath(opf).parent
    o = etree.fromstring(z.read(opf))
    ns = {"o": "http://www.idpf.org/2007/opf"}
    items = {i.get("id"): i.get("href") for i in o.iterfind(".//o:manifest/o:item", ns)}
    out = []
    for r in o.iterfind(".//o:spine/o:itemref", ns):
        href = items.get(r.get("idref"))
        if href:
            out.append(str(base / href) if str(base) != "." else href)
    return out


def parse(z, name):
    data = z.read(name)
    try:
        return etree.fromstring(data)
    except etree.XMLSyntaxError:
        return etree.fromstring(data, etree.HTMLParser())


def is_noteref(a):
    return local(a) == "a" and (
        "noteref" in (a.get("role") or "") or
        "noteref" in (a.get(f"{{{EPUB_NS}}}type") or "") or
        "noteref" in (a.get("class") or "") or
        "footnote-ref" in (a.get("class") or ""))


def is_backlink(a):
    return local(a) == "a" and (
        "backlink" in (a.get("role") or "") or "footnote-back" in (a.get("class") or ""))


class Book:
    """Blocks of an EPUB: lists of (token, italic, space_before) with the
    block's tag; footnotes set inline as a ⟦ … ⟧ run where their marker is."""

    def __init__(self, path):
        z = zipfile.ZipFile(path)
        self.docs = [(n, parse(z, n)) for n in spine(z) if n in z.namelist()]
        self.ids = {}
        for n, root in self.docs:
            for el in root.iter():
                if isinstance(el.tag, str) and el.get("id"):
                    self.ids[(n, el.get("id"))] = el
        self.note_els = set()
        self.refs = {}
        for n, root in self.docs:
            for a in root.iter():
                if is_noteref(a):
                    tgt = self.target(n, a.get("href") or "")
                    if tgt is not None:
                        box = self.note_box(tgt)
                        self.refs[a] = box
                        self.note_els.add(box)
        self.blocks = []
        for n, root in self.docs:
            body = next((e for e in root.iter() if local(e) == "body"), root)
            self.walk_blocks(body, n)

    def target(self, doc, href):
        f, _, frag = href.partition("#")
        if not frag:
            return None
        name = str(PurePosixPath(doc).parent / f) if f else doc
        name = re.sub(r"(^|/)\./", r"\1", name)
        el = self.ids.get((name, frag))
        return el if el is not None else self.ids.get((doc, frag))

    @staticmethod
    def note_box(el):
        """The element that holds a footnote: the aside / li around the target."""
        e = el
        while e is not None:
            if local(e) in ("aside", "li") or (local(e) in ("div", "section") and
                                               "note" in (e.get("class") or "") +
                                               (e.get(f"{{{EPUB_NS}}}type") or "")):
                return e
            e = e.getparent()
        return el.getparent() if local(el) in ("a", "span") and el.getparent() is not None else el

    def walk_blocks(self, el, doc):
        if el in self.note_els or local(el) in SKIP or local(el) == "nav":
            return
        kids = [c for c in el if isinstance(c.tag, str)]
        has_block_kids = any(local(c) in BLOCKS and c not in self.note_els for c in kids)
        direct_text = (el.text or "").strip() or any((c.tail or "").strip() for c in kids)
        if local(el) in BLOCKS and local(el) not in ("body",) and \
                (not has_block_kids or direct_text) and local(el) != "hr":
            toks = []
            self.inline(el, toks, False, doc, top=True)
            if any(t[0] for t in toks):
                tag = local(el)
                self.blocks.append({"tag": tag, "toks": toks, "doc": doc})
            return
        for c in kids:
            self.walk_blocks(c, doc)

    def text(self, s, toks, ital):
        pos = 0
        for m in TOKEN_RE.finditer(s):
            sp = bool(re.search(r"\s", s[pos:m.start()])) or (pos == 0 and m.start() > 0 and
                                                             s[:m.start()].isspace())
            toks.append([m.group(0), ital, sp])
            pos = m.end()
        if s and s[-1:].isspace():
            toks.append(["", ital, True])        # a space before what follows

    def inline(self, el, toks, ital, doc, top=False):
        if not top:
            if el in self.note_els or local(el) in SKIP or is_backlink(el):
                self.tail(el, toks, ital)
                return
            if el in self.refs:
                box = self.refs[el]
                toks.append(["⟦", False, False])
                sub = []
                self.inline(box, sub, False, doc, top=True)
                # drop a leading note number ("12." / "12")
                while sub and (not sub[0][0] or re.fullmatch(r"\d+", sub[0][0])):
                    sub.pop(0)
                    if sub and sub[0][0] == "." and not sub[0][2]:
                        sub.pop(0)
                if sub:
                    sub[0][2] = True
                toks += sub
                toks.append(["⟧", False, True])
                self.tail(el, toks, ital)
                return
            if local(el) == "br":
                toks.append(["", ital, True])
                self.tail(el, toks, ital)
                return
        it = ital or local(el) in ITALIC or "italic" in (el.get("class") or "")
        if el.text:
            self.text(el.text, toks, it)
        for c in el:
            if isinstance(c.tag, str):
                if local(c) in BLOCKS and not top and c not in self.note_els:
                    toks.append(["", it, True])
                self.inline(c, toks, it, doc)
            elif c.tail:
                self.text(c.tail, toks, it)
        if not top:
            self.tail(el, toks, ital)

    def tail(self, el, toks, ital):
        if el.tail:
            self.text(el.tail, toks, ital)


def clean(toks):
    """Join the space markers into the next token's space-before flag."""
    out, pending = [], False
    for t, it, sp in toks:
        if not t:
            pending = pending or sp
            continue
        out.append((t, it, (sp or pending) and bool(out)))
        pending = False
    return out


# -- comparing -----------------------------------------------------------------

QUOTE_FOLD = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "—": "-", "–": "-",
                            "‐": "-", "ʼ": "'"})


def key(t):
    return t.translate(QUOTE_FOLD)


def is_word(t):
    return bool(re.match(r"\w", t))


ARCHAIC = re.compile(r"^(?:(?:there|here|where)(?:of|in|by|unto|with|to|upon|from|after|fore)|"
                     r"unto|hath|doth|thou|thee|thy|thine|ye|art|hast|dost|shalt|wilt|"
                     r"wherefore|whither|whence|thence|hence|whilst|amongst|"
                     r"\w+eth)$", re.I)


def classify(a, b):
    """The kind of one change: old tokens a, new tokens b."""
    ka, kb = [key(x) for x in a], [key(x) for x in b]
    if ka == kb:
        return "quotes"
    if "".join(ka) == "".join(kb):
        return "spacing"
    wa, wb = [x for x in ka if is_word(x)], [x for x in kb if is_word(x)]
    if not wa and not wb:
        return "punct"
    if [x.lower() for x in wa] == [x.lower() for x in wb]:
        if wa == wb:
            return "punct"
        return "case"
    sa, sb = collections.Counter(x.lower() for x in wa), collections.Counter(x.lower() for x in wb)
    gone, came = list((sa - sb).elements()), list((sb - sa).elements())
    if any(ARCHAIC.match(x) for x in gone + came) and \
            all(ARCHAIC.match(x) or x in ("of", "in", "by", "to", "with", "upon", "that", "which",
                                          "it", "them", "those", "this", "these", "you", "your",
                                          "has", "does", "are", "therefore", "is", "s")
                for x in gone + came):
        return "grammar"
    if len(wa) == len(wb) and all(
            x.lower() == y.lower() or (min(len(x), len(y)) >= 4 and difflib.SequenceMatcher(
                None, x.lower(), y.lower()).ratio() >= 0.6)
            for x, y in zip(wa, wb)):
        return "spelling"
    if "".join(wa).lower() == "".join(wb).lower():
        return "spelling"                     # any thing / anything
    return "wording"


def group_blocks(old, new):
    """Pair the blocks: rows of (old block indices, new block indices)."""
    a, b, ab, bb = [], [], [], []
    for i, blk in enumerate(old):
        for t in blk["toks"]:
            a.append(key(t[0]).lower())
            ab.append(i)
    for j, blk in enumerate(new):
        for t in blk["toks"]:
            b.append(key(t[0]).lower())
            bb.append(j)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    shared = collections.Counter()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                shared[(ab[i1 + k], bb[j1 + k])] += 1
    parent = {}

    def find(x):
        while parent.get(x, x) != x:
            x = parent[x]
        return x

    def union(x, y):
        parent[find(x)] = find(y)

    la = collections.Counter(ab)
    lb = collections.Counter(bb)
    for (i, j), n in shared.items():
        if n >= max(1, 0.3 * min(la[i], lb[j])) or n >= 12:
            union(("o", i), ("n", j))
    groups = collections.defaultdict(lambda: ([], []))
    for i in range(len(old)):
        groups[find(("o", i))][0].append(i)
    for j in range(len(new)):
        groups[find(("n", j))][1].append(j)
    rows = list(groups.values())
    # order: by the new side; old-only rows after the row of the old block before
    pos_new = {}
    for r in rows:
        for j in r[1]:
            pos_new[j] = r
    keyed = []
    last = -1.0
    old_row = {}
    for r in rows:
        for i in r[0]:
            old_row[i] = r
    for r in rows:
        if r[1]:
            keyed.append((min(r[1]), 0, r))
    for i in range(len(old)):
        r = old_row[i]
        if r[1]:
            last = min(r[1])
        elif r[0][0] == i:
            keyed.append((last + 0.5, i, r))
    keyed.sort(key=lambda x: (x[0], x[1]))
    return [r for _, _, r in keyed]


def joined(blocks, idx):
    toks = []
    for n, i in enumerate(idx):
        if n:
            toks.append(("¶", False, True))
        toks += blocks[i]["toks"]
    return toks


def render(toks, marks):
    """marks: index -> (class, title). Consecutive marked tokens share a span."""
    out, k = [], 0
    in_note = 0
    while k < len(toks):
        t, it, sp = toks[k]
        if sp and k:
            out.append(" ")
        if t == "¶":
            cls = marks.get(k)
            out.append(f'<span class="pb{" ch " + cls[0] if cls else ""}"'
                       f'{" title=" + chr(34) + html.escape(cls[1]) + chr(34) if cls else ""}>¶</span>'
                       '<br class="pbr">')
            k += 1
            continue
        if t == "⟦":
            in_note += 1
            out.append('<span class="note">')
            k += 1
            continue
        if t == "⟧":
            in_note -= 1
            out.append('</span>')
            k += 1
            continue
        if k in marks:
            cls, title = marks[k]
            run = []
            j = k
            while j < len(toks) and marks.get(j) == (cls, title) and toks[j][0] not in "⟦⟧¶":
                run.append(toks[j])
                j += 1
            inner = ""
            for n, (w, i2, s2) in enumerate(run):
                if n and s2:
                    inner += " "
                w = html.escape(w)
                inner += f"<i>{w}</i>" if i2 else w
            out.append(f'<span class="ch {cls}" title="{html.escape(title)}">{inner}</span>')
            k = j
            continue
        w = html.escape(t)
        out.append(f"<i>{w}</i>" if it else w)
        k += 1
    out.append("</span>" * max(0, in_note))
    return "".join(out)


def show_text(toks):
    s = ""
    for n, (t, _, sp) in enumerate(toks):
        if n and sp:
            s += " "
        s += t
    return s


def compare_row(ot, nt):
    """Marks for both sides and the kinds found."""
    a = [key(t[0]) for t in ot]
    b = [key(t[0]) for t in nt]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    om, nm, kinds = {}, {}, collections.Counter()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                x, y = ot[i1 + k], nt[j1 + k]
                if x[0] != y[0]:
                    kind = "quotes"
                elif x[2] != y[2] and i1 + k and j1 + k:
                    kind = "spacing"
                else:
                    continue
                t = f"{kind}: {x[0]!s} → {y[0]!s}" if kind == "quotes" else \
                    f"spacing: {'space' if x[2] else 'no space'} → {'space' if y[2] else 'no space'}"
                om[i1 + k] = (kind, t)
                nm[j1 + k] = (kind, t)
                kinds[kind] += 1
            continue
        A, B = [t[0] for t in ot[i1:i2]], [t[0] for t in nt[j1:j2]]
        if "¶" in A or "¶" in B:
            Aw = [x for x in A if x != "¶"]
            Bw = [x for x in B if x != "¶"]
            if A.count("¶") != B.count("¶"):
                kinds["para"] += 1
                for k in range(i1, i2):
                    if ot[k][0] == "¶":
                        om[k] = ("para", "paragraph break removed")
                for k in range(j1, j2):
                    if nt[k][0] == "¶":
                        nm[k] = ("para", "paragraph break added")
            if not Aw and not Bw:
                continue
            kind = classify(Aw, Bw) if Aw or Bw else "para"
        else:
            kind = classify(A, B)
        title = f"{kind}: {show_text(ot[i1:i2]) or '(nothing)'} → {show_text(nt[j1:j2]) or '(nothing)'}"
        kinds[kind] += 1
        for k in range(i1, i2):
            if ot[k][0] != "¶" or k not in om:
                om.setdefault(k, (kind, title))
        for k in range(j1, j2):
            if nt[k][0] != "¶" or k not in nm:
                nm.setdefault(k, (kind, title))
        if i1 == i2 and j1 < j2:     # a pure insertion: a caret on the old side
            om.setdefault(("at", i1), (kind, title))
        if j1 == j2 and i1 < i2:
            nm.setdefault(("at", j1), (kind, title))
    return om, nm, kinds


def with_carets(toks, marks):
    """Insert an empty marker token where the other side has text this one lacks."""
    at = {k[1]: v for k, v in marks.items() if isinstance(k, tuple)}
    if not at:
        return toks, {k: v for k, v in marks.items() if not isinstance(k, tuple)}
    out, m2 = [], {}
    for k in range(len(toks) + 1):
        if k in at:
            m2[len(out)] = at[k]
            out.append(("‸", False, True))
        if k < len(toks):
            if k in marks:
                m2[len(out)] = marks[k]
            out.append(toks[k])
    return out, m2


# -- the page ------------------------------------------------------------------

CSS = """
:root{--bg:#fbfaf7;--fg:#1f1d1a;--muted:#6b665e;--line:#e3dfd6;--panel:#f2efe8;
--del:#f6d5cf;--ins:#d3ecd2;--wording:#c0392b;--spelling:#8e5bb5;--case:#2b7bb9;
--punct:#b7791f;--quotes:#7a7a7a;--spacing:#7a7a7a;--para:#16876b;--hl:#ffe9a8}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#1b1a18;--fg:#e8e4dc;
--muted:#a39d92;--line:#3a3732;--panel:#25231f;--del:#5a2b26;--ins:#21452a;--wording:#ff8a7a;
--spelling:#c9a2ea;--case:#7cc0f0;--punct:#e9b45c;--quotes:#a8a8a8;--spacing:#a8a8a8;
--para:#5fd0b0;--hl:#5c4c16}}
:root[data-theme="dark"]{--bg:#1b1a18;--fg:#e8e4dc;--muted:#a39d92;--line:#3a3732;--panel:#25231f;
--del:#5a2b26;--ins:#21452a;--wording:#ff8a7a;--spelling:#c9a2ea;--case:#7cc0f0;--punct:#e9b45c;
--quotes:#a8a8a8;--spacing:#a8a8a8;--para:#5fd0b0;--hl:#5c4c16}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 Georgia,"Libertinus Serif",serif}
header.top{position:sticky;top:0;z-index:5;background:var(--panel);border-bottom:1px solid var(--line);
padding:.6rem 16px}
header.top h1{font-size:1.1rem;margin:0 0 .3rem}
.controls{display:flex;flex-wrap:wrap;gap:.3rem 1rem;font:13px/1.4 system-ui,sans-serif;align-items:center}
.controls label{white-space:nowrap}
.controls button{font:inherit;padding:.1rem .6rem;border:1px solid var(--line);background:var(--bg);
color:var(--fg);border-radius:4px;cursor:pointer}
.sw{display:inline-block;width:.8em;height:.8em;border-radius:2px;vertical-align:-.05em;margin-right:.2em}
.counts{font:12px system-ui,sans-serif;color:var(--muted);margin-top:.25rem}
nav.toc{font:13px/1.6 system-ui,sans-serif;padding:.5rem 16px;border-bottom:1px solid var(--line)}
nav.toc a{color:var(--fg);margin-right:.9rem;white-space:nowrap}
nav.toc a .n{color:var(--muted)}
main{padding:0 16px 4rem}
.row{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;padding:.45rem 0;border-bottom:1px solid var(--line)}
.row>div{min-width:0;overflow-wrap:anywhere}
.row.colhead{position:sticky;top:var(--hh,6.5rem);z-index:4;background:var(--bg);
font:600 12px system-ui,sans-serif;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.row.h>div{font-weight:700;font-size:1.08rem}
.row.focus{background:var(--hl)}
.empty{color:var(--muted);font-style:italic;font-size:.9em}
.note{font-size:.85em;color:var(--muted)}
.note::before{content:"[note: "}.note::after{content:"]"}
.pb{color:var(--muted);font-size:.8em}
.ch{border-radius:2px;cursor:help}
.old .ch{background:var(--del)}
.new .ch{background:var(--ins)}
.ch.wording{box-shadow:inset 0 -2px var(--wording)}
.ch.spelling{box-shadow:inset 0 -2px var(--spelling)}
.ch.case{box-shadow:inset 0 -2px var(--case)}
.ch.punct{box-shadow:inset 0 -2px var(--punct)}
.ch.quotes,.ch.spacing{box-shadow:inset 0 -2px var(--quotes)}
.ch.para{box-shadow:inset 0 -2px var(--para)}
body.only .row.same{display:none}
@media (max-width:700px){.row{grid-template-columns:1fr;gap:.2rem}
.row>div.old::before{content:"before: ";font:600 11px system-ui;color:var(--muted)}
.row>div.new::before{content:"now: ";font:600 11px system-ui;color:var(--muted)}
.row.colhead{display:none}}
"""

JS = """
const kinds = KINDS_JSON;
const b = document.body;
function apply(){
  for (const [k] of kinds){
    const on = document.querySelector('input[data-k="'+k+'"]').checked;
    b.classList.toggle('hide-'+k, !on);
  }
  // a row counts as changed when it has a visible change
  document.querySelectorAll('.row.data').forEach(r=>{
    const ks = (r.dataset.k||'').split(' ').filter(Boolean);
    const vis = ks.some(k => !b.classList.contains('hide-'+k));
    r.classList.toggle('same', !vis);
  });
  b.classList.toggle('only', document.getElementById('only').checked);
  try{localStorage.setItem('ba-prefs', JSON.stringify({
    k: kinds.map(([k])=>[k, document.querySelector('input[data-k="'+k+'"]').checked]),
    only: document.getElementById('only').checked}));}catch(e){}
}
try{const p = JSON.parse(localStorage.getItem('ba-prefs')||'null');
  if (p){ for (const [k,v] of p.k){const i=document.querySelector('input[data-k="'+k+'"]'); if(i) i.checked=v;}
          document.getElementById('only').checked = p.only; }}catch(e){}
document.querySelectorAll('.controls input').forEach(i=>i.addEventListener('change', apply));
apply();
let cur = -1;
function step(d){
  const rows = [...document.querySelectorAll('.row.data:not(.same)')];
  if (!rows.length) return;
  const y = window.scrollY + (document.querySelector('header.top').offsetHeight + 40);
  if (cur < 0 || !rows[cur] || !rows[cur].classList.contains('focus')){
    cur = rows.findIndex(r => r.offsetTop > y) ; if (cur < 0) cur = rows.length-1; if (d<0) cur = Math.max(0,cur-1); else cur = Math.max(0,cur-1);
  }
  document.querySelectorAll('.row.focus').forEach(r=>r.classList.remove('focus'));
  cur = Math.min(rows.length-1, Math.max(0, cur + d));
  rows[cur].classList.add('focus');
  window.scrollTo({top: rows[cur].offsetTop - document.querySelector('header.top').offsetHeight - 50, behavior:'smooth'});
}
document.getElementById('next').onclick = ()=>step(1);
document.getElementById('prev').onclick = ()=>step(-1);
document.addEventListener('keydown', e=>{
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
  if (e.key === 'n' || e.key === 'j') step(1);
  if (e.key === 'p' || e.key === 'k') step(-1);
});
const hh = ()=>document.documentElement.style.setProperty('--hh', document.querySelector('header.top').offsetHeight+'px');
hh(); addEventListener('resize', hh);
"""


def page(title, old_label, new_label, rows_html, toc, totals):
    hide = "".join(
        f"body.hide-{k} .ch.{k}{{background:none!important;box-shadow:none!important}}"
        for k, _, _ in KINDS)
    boxes = "".join(
        f'<label><input type="checkbox" data-k="{k}"{" checked" if on else ""}>'
        f'<span class="sw" style="background:var(--{k})"></span>{lab}'
        f' <span class="n">({totals.get(k, 0)})</span></label>'
        for k, lab, on in KINDS)
    kinds_json = "[" + ",".join(f'["{k}"]' for k, _, _ in KINDS) + "]"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}: before and after</title>
<style>{CSS}{hide}</style></head>
<body>
<header class="top"><h1>{html.escape(title)}: {html.escape(old_label)} and {html.escape(new_label)}</h1>
<div class="controls"><span>Mark:</span>{boxes}
<label><input type="checkbox" id="only"> only rows that changed</label>
<button id="prev" title="previous change (p)">◀ prev</button>
<button id="next" title="next change (n)">next ▶</button></div>
<div class="counts">{sum(v for k, v in totals.items() if not k.startswith("_"))} changes in {totals.get('_rows', 0)} of {totals.get('_all', 0)} paragraphs.
Hover a marked word for before → after. Keys: n / p step through the changes shown.</div>
</header>
<nav class="toc">{toc}</nav>
<main>
<div class="row colhead"><div>{html.escape(old_label)}</div><div>{html.escape(new_label)}</div></div>
{rows_html}
</main>
<script>{JS.replace("KINDS_JSON", kinds_json)}</script>
</body></html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("out")
    ap.add_argument("--title", default="Book")
    ap.add_argument("--old-label", default="Before")
    ap.add_argument("--new-label", default="Now")
    a = ap.parse_args()
    old, new = Book(a.old), Book(a.new)
    for bk in (old, new):
        for blk in bk.blocks:
            blk["toks"] = clean(blk["toks"])
    rows = group_blocks(old.blocks, new.blocks)
    out, toc = [], []
    totals = collections.Counter()
    changed_rows = 0
    sect_changes = None
    for n, (oi, ni) in enumerate(rows):
        ot, nt = joined(old.blocks, oi), joined(new.blocks, ni)
        heading = any(new.blocks[j]["tag"] in ("h1", "h2") for j in ni) or \
            (not ni and any(old.blocks[i]["tag"] in ("h1", "h2") for i in oi))
        if not oi or not ni:
            kind = "wording"
            title = "only before" if oi else "only now"
            om = {k: (kind, title) for k in range(len(ot))}
            nm = {k: (kind, title) for k in range(len(nt))}
            kinds = collections.Counter({kind: 1})
        else:
            om, nm, kinds = compare_row(ot, nt)
        ot2, om2 = with_carets(ot, om)
        nt2, nm2 = with_carets(nt, nm)
        totals.update(kinds)
        if kinds:
            changed_rows += 1
        if heading:
            ident = f"s{n}"
            label = show_text(nt or ot)[:60]
            toc.append([ident, label, 0])
            sect_changes = toc[-1]
        else:
            ident = None
        if sect_changes is not None:
            sect_changes[2] += sum(kinds.values())
        left = render(ot2, om2) if ot else '<span class="empty">(not in this version)</span>'
        right = render(nt2, nm2) if nt else '<span class="empty">(not in this version)</span>'
        cls = "row data" + (" h" if heading else "") + ("" if kinds else " same")
        out.append(f'<div class="{cls}"{f" id={chr(34)}{ident}{chr(34)}" if ident else ""}'
                   f' data-k="{" ".join(sorted(kinds))}">'
                   f'<div class="old">{left}</div><div class="new">{right}</div></div>')
    totals["_rows"], totals["_all"] = changed_rows, len(rows)
    toc_html = "".join(f'<a href="#{i}">{html.escape(l)} <span class="n">{c}</span></a>'
                       for i, l, c in toc)
    shown = {k: v for k, v in totals.items()}
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(page(a.title, a.old_label, a.new_label, "\n".join(out), toc_html, shown))
    real = {k: v for k, v in totals.items() if not k.startswith("_")}
    print(f"{a.out}: {len(rows)} rows, {changed_rows} changed; " +
          ", ".join(f"{k} {v}" for k, v in sorted(real.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
