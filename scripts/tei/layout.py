"""
Which parts of the TEI go into which chapter file.

A book with only a dedication and numbered chapters needs nothing here: each
of those divisions is one file (dedication.typ, chapter-NN.typ), as before.

Any other book defines LAYOUT in its source/editorial.py: a function taking
the TEI root element and returning a list of files, in reading order:

    {"file": "vol-1/01-serving.typ",      # path under chapters/typ
     "title": "Serving Each Other",        # the edition's heading for the file
     "short": None,                        # optional short (running-head) title
     "parts": [el, el, ...]}               # TEI elements, in order

A part that is a <div> is set with its own heading (DIV_LEVELS gives the
heading level by div type; RUN_IN_DIVS are set as a bold run-in paragraph
instead) and everything in it, nested divisions included. Any other element
(a paragraph, an epigraph) is a loose block of a division, set as it stands.
The file title is the edition's, so it lives in the layout, not in the TEI;
a printed head of a division that is not itself a part (a treatise's title,
when its sections are cut into chapters) is left out of the edition.

check() lists text that no part covers, so nothing vanishes silently.
"""

import runpy
from pathlib import Path

from lxml import etree

NS = "http://www.tei-c.org/ns/1.0"
T = "{%s}" % NS


def local(el):
    return etree.QName(el).localname if isinstance(el.tag, str) else None


def settings(src_path):
    """The book's editorial.py (next to the TCP or TEI file), as a dict."""
    ed = Path(src_path).parent / "editorial.py"
    return runpy.run_path(str(ed)) if ed.exists() else {}


def book_layout(root, cfg):
    """The book's files, or None for the classic dedication/chapter layout."""
    fn = cfg.get("LAYOUT")
    if fn is None:
        return None
    files = fn(root)
    for f in files:
        f.setdefault("short", None)
        f.setdefault("title", None)
    return files


def div_levels(cfg):
    return dict(cfg.get("DIV_LEVELS", {})), set(cfg.get("RUN_IN_DIVS", ()))


def words(el):
    return len("".join(el.itertext()).split())


def check(root, files, cfg):
    """Text-bearing elements of <text> outside every part (and outside
    SKIP_DIVISIONS): [(element, words)]. Heads of divisions that contain
    parts are the edition's to replace, and are not counted."""
    skip = set(cfg.get("SKIP_DIVISIONS", ()))
    covered = set()
    for f in files:
        for p in f["parts"]:
            covered.add(p)
    missing = []

    def walk(el):
        for c in el:
            if not isinstance(c.tag, str):
                continue
            n = local(c)
            if c in covered:
                continue
            if n == "div":
                if c.get("type") in skip:
                    continue
                walk(c)
            elif n in ("head", "pb", "milestone", "fw", "lb"):
                continue
            elif n in ("front", "body", "back", "group", "text"):
                walk(c)
            elif words(c):
                missing.append((c, words(c)))
    text = root.find(f".//{T}text")
    walk(text)
    return missing


def parts_of(f):
    """(element, is_div) for each part of a file."""
    return [(p, local(p) == "div") for p in f["parts"]]


def top_divs(root):
    """Direct <div> children of front, body and back, in order: the numbering
    quod.lib.umich.edu uses in its 1:N URLs (1-based)."""
    text = root.find(f".//{T}text")
    out = []
    for part in ("front", "body", "back"):
        el = text.find(T + part)
        if el is not None:
            out += el.findall(T + "div")
    return out


def sections(div, first=1, last=None):
    """Parts for a run of a division's sub-divisions, cut by ordinal position
    (1-based, inclusive): the sub-divisions, any loose blocks between them,
    and, when the run starts at the first one, whatever stands before it
    (e.g. a scripture epigraph). The division's own head is not included."""
    out, seen = [], 0
    for c in div:
        if not isinstance(c.tag, str):
            continue
        n = local(c)
        if n in ("head", "pb"):
            continue
        if n == "div":
            seen += 1
            if first <= seen and (last is None or seen <= last):
                out.append(c)
        elif seen == 0:
            if first == 1:
                out.append(c)
        elif first <= seen and (last is None or seen <= last):
            out.append(c)
    return out
