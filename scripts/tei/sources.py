"""
A book's source transcription, whatever form it came in, as TEI.

  source/<ID>.tcp.xml     EEBO-TCP transcription (TEI already)
  source/<id>.thml.xml    CCEL ThML, converted in memory (thml_to_tei.py)

The untouched file is the provenance; every tool that reads the source
(build_tei.py, tei_extract.py on the source, tcp_structure.py, verify.py)
goes through load(), so no converted copy has to be kept.
"""

from pathlib import Path

from lxml import etree

PATTERNS = ("*.tcp.xml", "*.thml.xml")


def is_source(path):
    return any(Path(path).match(p) for p in PATTERNS)


def find(src_dir):
    """The source file in a book's source/ folder, or None."""
    for pat in PATTERNS:
        hit = next(iter(sorted(Path(src_dir).glob(pat))), None)
        if hit is not None:
            return hit
    return None


def kind(path):
    return "thml" if str(path).endswith(".thml.xml") else "tcp"


def load(path):
    """An lxml ElementTree of the source as TEI, with any supplement
    (<stem>.supplied.xml beside it) spliced in."""
    if kind(path) == "thml":
        import thml_to_tei
        tree = thml_to_tei.convert(path)
    else:
        tree = etree.parse(str(path))
    sup = supplement(path)
    if sup is not None:
        splice(tree, etree.parse(str(sup)))
    return tree


# ---------------------------------------------------------------------------
# Supplements: text the transcription lacks (pages missing from the copy it
# was made from), transcribed from another copy and kept in its own file, so
# the source file stays untouched.  See Gouge's A68107.supplied.xml.
# ---------------------------------------------------------------------------

T = "{http://www.tei-c.org/ns/1.0}"
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


def supplement(path):
    p = Path(path)
    hit = p.with_name(p.name.split(".")[0] + ".supplied.xml")
    return hit if hit.exists() else None


def _page_after(el):
    """pb/@n of the first page break after el"""
    hit = el.xpath("following::t:pb[1]/@n", namespaces={"t": T[1:-1]})
    return hit[0] if hit else None


def _append_text(parent, text):
    if not text:
        return
    if len(parent):
        parent[-1].tail = (parent[-1].tail or "") + text
    else:
        parent.text = (parent.text or "") + text


def splice(tree, sup):
    """Put each supplement fill in at its gap (see the supplement's header):
    the gap's paragraph is split after the gap; a leading <seg> runs on in
    it, blocks follow it, divisions follow its division, and <rest/> takes
    the rest of the paragraph and the blocks after it.  Everything brought in
    carries @change pointing at a revisionDesc entry made from fill/desc."""
    root = tree.getroot()
    for fill in sup.getroot().iter(T + "fill"):
        cid = fill.get(XML_ID)
        gap = next((g for g in root.iter(T + "gap") if g.get("reason") == fill.get("gap")
                    and _page_after(g) == fill.get("pb")), None)
        if gap is None:
            raise SystemExit(f"supplement: no {fill.get('gap')} gap before page {fill.get('pb')}")
        para = gap.getparent()
        div = para.getparent()
        # the rest of the paragraph after the gap, and the blocks after it
        rest_text, gap.tail = gap.tail, None
        rest_nodes = []
        while gap.getnext() is not None:
            rest_nodes.append(gap.getnext())
            para.remove(gap.getnext())
        later = []
        while para.getnext() is not None:
            later.append(para.getnext())
            div.remove(para.getnext())
        rest = fill.find(".//" + T + "rest")
        block_at, div_at = para, div
        for el in [c for c in fill if isinstance(c.tag, str) and c.tag != T + "desc"]:
            el.set("change", "#" + cid)
            if el.tag == T + "seg":                  # runs on in the gap's paragraph
                gap.addnext(el)
            elif el.tag == T + "div":
                div_at.addnext(el)
                div_at = el
            else:
                block_at.addnext(el)
                block_at = el
        if rest is None:
            raise SystemExit("supplement: a fill needs <rest/>")
        holder = rest.getparent()
        before = rest.getprevious()
        tail = rest.tail
        holder.remove(rest)
        if before is not None:
            before.tail = (before.tail or "") + (rest_text or "")
        else:
            holder.text = (holder.text or "") + (rest_text or "")
        for n in rest_nodes:
            holder.append(n)
        _append_text(holder, tail)
        at = holder
        for b in later:
            at.addnext(b)
            at = b
        # the revision entry the @change attributes point at
        hdr = root.find(T + "teiHeader")
        rd = hdr.find(T + "revisionDesc")
        if rd is None:
            rd = etree.SubElement(hdr, T + "revisionDesc")
        ch = etree.SubElement(rd, T + "change")
        ch.set(XML_ID, cid)
        ch.set("who", "#editor")
        ch.text = " ".join((fill.findtext(T + "desc") or "").split())
        ch.tail = "\n"
    return tree
