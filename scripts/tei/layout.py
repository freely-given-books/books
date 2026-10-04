"""
Which parts of the TEI go into which chapter file.

A book with only a dedication and numbered chapters needs nothing here: each
of those divisions is one file (dedication.typ, chapter-NN.typ), as before.

Any other book defines LAYOUT in its source/editorial.py: a function taking
the TEI root element and returning a list of files, in reading order:

    {"file": "vol-1/01-serving.typ",      # path under chapters/typ
     "title": "Serving Each Other",        # the edition's heading for the file
     "short": None,                        # optional short (running-head) title
     "subtitle": el,                       # optional: a printed head set under
                                           # the title, as a centred line
     "part": None,                         # optional: a part heading before this
                                           # file (ebook only; print sets its own)
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
        f.setdefault("subtitle", None)
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
    # SKIP_BLOCKS(root): loose blocks this edition leaves out (kept in the
    # TEI as printed), e.g. most of a long dedication
    skip_blocks = set(cfg["SKIP_BLOCKS"](root)) if cfg.get("SKIP_BLOCKS") else set()
    covered = set()
    for f in files:
        for p in f["parts"] + ([f["subtitle"]] if f.get("subtitle") is not None else []):
            covered.add(p)
    missing = []

    def walk(el):
        for c in el:
            if not isinstance(c.tag, str):
                continue
            n = local(c)
            if c in covered or c in skip_blocks:
                continue
            if n in skip:
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


_VERSE = {}


def verse_division(el):
    """Is el's division (el itself, if it is a div) a section made of verse,
    such as a verse preface? Its stanzas are then the text itself, set as
    plain stanzas, not as quotations standing out from prose."""
    div = el if local(el) == "div" else next(el.iterancestors(T + "div"), None)
    if div is None:
        return False
    if div not in _VERSE:
        total = words(div) - sum(words(h) for h in div.findall(T + "head"))
        verse = sum(words(x) for x in div.iter(T + "l"))
        _VERSE[div] = bool(total) and verse / total >= 0.8
    return _VERSE[div]


def closer_lines(closer, layer="reg"):
    """A closer with a place and date (dateline) or several signatories (a
    list in signed), as one block per line: in the edition the signatories,
    one to a line, then the dateline; in the orig layer as printed. None for
    any other closer (a single signature is set as before)."""
    signed = closer.find(T + "signed")
    lst = signed.find(T + "list") if signed is not None else None
    dates = closer.findall(T + "dateline")
    if lst is None and not dates or \
            any(local(c) not in ("dateline", "signed") for c in closer if local(c)) or \
            (lst is not None and any(local(c) not in ("list",) for c in signed if local(c))):
        return None
    names = lst.findall(T + "item") if lst is not None else \
        ([signed] if signed is not None else [])
    if layer == "reg":
        return names + dates
    return [c for c in closer.iter(T + "dateline", T + "item", T + "signed")
            if c in names or c in dates]


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


# ---------------------------------------------------------------------------
# Tables: early printed "tables" are brace diagrams, not grids
# ---------------------------------------------------------------------------

def _cell_span(cell):
    return int(cell.get("rows") or 1), int(cell.get("cols") or 1)


def table_grid(table):
    """[(cell, row, col, rowspan, colspan)] in document order, honouring
    rowspan and colspan; empty unspanned cells (the compositor's spacers)
    are dropped so each branch stays under its own head."""
    placements, occupied = [], {}
    for row_i, row in enumerate(table.findall(T + "row")):
        cells = [c for c in row.findall(T + "cell")
                 if "".join(c.itertext()).strip() or _cell_span(c) != (1, 1)]
        col = 0
        for cell in cells:
            rowspan, colspan = _cell_span(cell)
            while occupied.get(col, 0) > 0:
                col += 1
            placements.append((cell, row_i, col, rowspan, colspan))
            for c in range(col, col + colspan):
                occupied[c] = rowspan
            col += colspan
        occupied = {c: n - 1 for c, n in occupied.items() if n > 1}
    return placements


def text_follows(p, node):
    """Is there text after `node` inside `p` (the block interrupts a sentence)?"""
    seen = False
    for child in p:
        if child is node:
            seen = True
            continue
        if seen and ((child.tail or "").strip() or "".join(child.itertext()).strip()):
            return True
    return bool((node.tail or "").strip())


BLOCK_IN_P = ("table", "list")


def edition_empty(el):
    """Whether the edition (the reg layer) leaves nothing of el: every word
    of it is a reading the review emptied (margin matter moved to a note)."""
    found = []

    def walk(e):
        if not isinstance(e.tag, str):
            return
        n = local(e)
        if n in ("note", "pb", "lb", "orig", "abbr", "sic"):
            return
        if n == "choice":
            r = next((c for c in e if isinstance(c.tag, str) and local(c) in
                      ("reg", "expan", "corr")), None)
            if r is not None:
                found.append(r.get("resp") == "#editor" and not "".join(r.itertext()).strip())
                if "".join(r.itertext()).strip():
                    found.append(False)
            return
        if (e.text or "").strip():
            found.append(False)
        for c in e:
            walk(c)
            if (c.tail or "").strip():
                found.append(False)
    walk(el)
    return bool(found) and all(found)


def p_blocks(p, edition=True):
    """The block children (tables, lists) a paragraph is split around, or []
    when it is set whole: no blocks, or a table interrupting its sentence
    (that one is read inline, column by column). In the edition a list the
    review emptied is no block: the paragraph runs on past it."""
    blocks = [c for c in p if isinstance(c.tag, str) and local(c) in BLOCK_IN_P
              and not (edition and c.get("rend") == "inline")    # in the sentence
              and not (edition and local(c) == "list" and edition_empty(c))]
    if any(local(b) == "table" and text_follows(p, b) for b in blocks):
        return []
    return blocks


NUMBER_CELL = r"\d{1,2}[.)]?"


def table_reading(table):
    """How the edition reads a table: (mode, [(marker, [cells])]).

    "brace" (a cell spans rows): column by column, as a brace groups; a
    column of one cell is a label (marker "¶"), a column of several is the
    branches (one "+" item each). "rows": row by row; a row of one cell is a
    heading line ("¶"), any other row is one "+" item (its leading number
    cell is left out by the machine pass). "inline" (the table interrupts a
    sentence): all cells column by column, no markers."""
    import re
    grid = table_grid(table)
    if not grid:
        return "rows", []
    p = table.getparent()
    if p is not None and local(p) == "p" and text_follows(p, table):
        cells = [c for c, *_ in sorted(grid, key=lambda g: (g[2], g[1]))]
        return "inline", [("", cells)]
    if any(g[3] > 1 for g in grid):
        cols = {}
        for cell, row, col, _rs, _cs in grid:
            cols.setdefault(col, []).append((row, cell))
        out = []
        for col in sorted(cols):
            cells = [c for _r, c in sorted(cols[col]) if "".join(c.itertext()).strip()]
            if len(cells) == 1:
                out.append(("¶", cells))
            else:
                out += [("+", [c]) for c in cells]
        return "brace", out
    rows = {}
    for cell, row, col, _rs, _cs in grid:
        rows.setdefault(row, []).append((col, cell))
    out = []
    for row in sorted(rows):
        cells = [c for _col, c in sorted(rows[row])]
        if not any("".join(c.itertext()).strip() for c in cells):
            continue
        out.append(("¶" if len(cells) == 1 else "+", cells))
    return "rows", out
