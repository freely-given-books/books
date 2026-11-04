#!/usr/bin/env python3
"""
tcp_to_typst.py
================

Convert an EEBO-TCP (Text Creation Partnership) TEI-XML transcription
into one Typst (.typ) file per top-level division ("div1"), preserving
the original early-modern spelling/wording exactly, and turning every
marginal/footnote <note> into a paired Typst #footnote[...] at its
original anchor point in the text.

This is the same backend that powers the "fulltext" pages on
https://quod.lib.umich.edu/e/eebo/... -- e.g. a URL like

    https://quod.lib.umich.edu/e/eebo/A09377.0001.001/1:2?rgn=div1;view=fulltext

is showing the *second* top-level div of the TEI file for TCP id
A09377, and .../1:3 is the third, and so on. Every EEBO-TCP text has a
matching GitHub repo at:

    https://github.com/textcreationpartnership/<ID>

containing a single <ID>.xml file. This script will auto-clone that
repo if you just give it the ID.

USAGE
-----
    # List the top-level divisions in a text (to see what 1:1, 1:2, ... are)
    python3 tcp_to_typst.py A09377 --list

    # Convert specific sections (1-based, matching the quod.lib "1:N" numbering)
    python3 tcp_to_typst.py A09377 --sections 2 3 --outdir out/

    # Convert the whole text, one file per top-level div
    python3 tcp_to_typst.py A09377 --outdir out/

    # Also compile each .typ straight to PDF (requires `pip install typst`)
    python3 tcp_to_typst.py A09377 --outdir out/ --pdf

    # Point it at an XML file you already have, instead of an ID
    python3 tcp_to_typst.py path/to/some_other_text.xml --outdir out/

NOTES ON WHAT GETS PRESERVED / HOW IT'S RENDERED
-------------------------------------------------
- Spelling and wording are never modernized.
- <hi> -> #emph[...] (rend="sup" -> #super[...])
- <note place="margin"> (or any <note>) -> #footnote[...] inserted at the
  exact point it occurs in the running text (this is the "pairing").
- <g ref="char:EOLhyphen"/> / EOLunhyphen (soft line-break markers) are
  dropped so words rejoin correctly; <g ref="char:cmbAbbrStroke"> (the
  combining macron used for abbreviations like "wh~e" -> when) is kept
  literally.
- <gap> (illegible/foreign-script passages) becomes the bracketed
  placeholder TCP already supplies (e.g. "<...>"), except
  reason="duplicate" gaps (misprinted duplicate pages), which are
  dropped since they carry no text.
- <expan>/<am>/<ex> (abbreviation + editorial expansion) renders the
  <ex> expansion text.
- <list>/<item> (incl. nested genealogy-style lists) become nested
  Typst bullet lists.
- Headings: a top-level div gets a level-1 `=` heading from its first
  <head>; any *further* <head> elements at that same level (e.g. a
  chapter's "CHAP. I." + descriptive subtitle) are rendered as one
  more heading level down. Nested <div>s recurse with heading level+1.

This script is deliberately generic across EEBO-TCP texts -- div
@type values (chapter, section, part, dialogue, sermon, ...) and
nesting depth vary a lot from book to book, so it doesn't hard-code
any of that; it just walks whatever structure is actually in the XML.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

from lxml import etree

NS = {"t": "http://www.tei-c.org/ns/1.0"}
WS_RE = re.compile(r"\s+")
ESCAPE_RE = re.compile(r"([\\#\$\*_`<>@\[\]])")


def local(tag):
    return etree.QName(tag).localname


def collapse(s):
    if s is None:
        return ""
    return WS_RE.sub(" ", s)


def esc(s):
    """Escape characters meaningful to Typst markup in plain source text."""
    return ESCAPE_RE.sub(r"\\\1", s)


# ---------------------------------------------------------------------------
# Inline rendering (handles running text inside <p>, <head>, <item>, etc.)
# ---------------------------------------------------------------------------

def _leading_text_is_joinable_whitespace(el):
    """True if el.text is pure whitespace containing a newline (just XML
    pretty-print indentation) AND el's first child is a glyph-splice <g>
    or an illegible-text <gap> -- meaning this "whitespace" isn't a real
    space, it's noise before a mid-word continuation."""
    if not el.text or el.text.strip() or "\n" not in el.text:
        return False
    if len(el) == 0:
        return False
    return local(el[0].tag) in ("g", "gap")


def render_inline(el):
    parts = []
    if el.text and not _leading_text_is_joinable_whitespace(el):
        parts.append(esc(collapse(el.text)))
    for child in el:
        tag = local(child.tag)
        if tag == "hi":
            inner = render_inline(child)
            if child.get("rend") == "sup":
                parts.append(f"#super[{inner}]")
            else:
                parts.append(f"#emph[{inner}]")
        elif tag == "g":
            # EOLhyphen / EOLunhyphen: empty, just drop (rejoins the word).
            # cmbAbbrStroke etc: literal combining character, keep as-is.
            if child.text:
                parts.append(child.text)
        elif tag == "note":
            note_body = render_inline(child).strip()
            if note_body:
                parts.append(f"#footnote[{escape_leading_marker(note_body)}]")
        elif tag == "gap":
            if child.get("reason") != "duplicate":
                desc = child.find(".//t:desc", namespaces=NS)
                if desc is not None and desc.text:
                    parts.append(esc(desc.text))
        elif tag == "expan":
            ex = child.find(".//t:ex", namespaces=NS)
            if ex is not None and ex.text:
                parts.append(esc(ex.text))
        elif tag in ("seg", "bibl", "q", "abbr", "corr", "sic", "unclear", "term"):
            parts.append(render_inline(child))
        elif tag in ("pb", "fw", "milestone"):
            pass
        else:
            # Unknown inline element: recurse so we never silently lose text.
            parts.append(render_inline(child))
        if child.tail:
            # Whitespace-only tail that's purely XML pretty-print
            # indentation (contains a newline) adjacent to a glyph-splice
            # <g> tag or an illegible-text <gap> is not a real space in
            # the source -- collapsing it to " " would wrongly split a
            # word (e.g. "co" + macron + <newline-indent> + "sent" ->
            # "consent", not "con sent").
            next_el = child.getnext()
            joinable = ("g", "gap")
            if (tag in joinable and next_el is not None and local(next_el.tag) in joinable
                    and not child.tail.strip() and "\n" in child.tail):
                pass
            else:
                parts.append(esc(collapse(child.tail)))
    return "".join(parts)


def render_inline_element(child):
    """Render a single element exactly as render_inline's dispatch would,
    without needing a real parent (used when skipping sibling <list>s)."""
    saved_tail = child.tail
    child.tail = None
    wrapper = etree.Element("wrap")
    wrapper.append(child)
    try:
        return render_inline(wrapper)
    finally:
        child.tail = saved_tail


# ---------------------------------------------------------------------------
# Block-level rendering
# ---------------------------------------------------------------------------

# A Typst content block re-parses its own body as markup, so a footnote whose
# text opens with "1. " (very common here -- "1. Cor. 7.") or with "- " becomes
# a list *inside* the note, swallowing the notes that follow it. Escape the
# marker so it stays literal. Same hazard for the text of a list <item>.
def escape_leading_marker(text):
    # "1. Cor." / "2) x"  -> escape the punctuation after the number
    m = re.match(r"(\s*\d+)([.)])(\s)", text)
    if m:
        return text[:m.end(1)] + "\\" + text[m.start(2):]
    # "- x" / "+ x" / "/ x" -> escape the marker itself
    m = re.match(r"(\s*)([-+/])(\s)", text)
    if m:
        return text[:m.end(1)] + "\\" + text[m.start(2):]
    return text

def render_list(list_el, depth=0):
    lines = []
    indent = "  " * depth
    head = list_el.find("t:head", namespaces=NS)
    if head is not None:
        text = render_inline(head).strip()
        if text:
            lines.append(f"{indent}#strong[{text}]")
            lines.append("")
    for item in list_el.findall("t:item", namespaces=NS):
        sub_lists = item.findall("t:list", namespaces=NS)
        parts = []
        if item.text and not _leading_text_is_joinable_whitespace(item):
            parts.append(esc(collapse(item.text)))
        for child in item:
            if local(child.tag) == "list":
                continue
            parts.append(render_inline_element(child))
            if child.tail:
                next_el = child.getnext()
                joinable = ("g", "gap")
                if (local(child.tag) in joinable and next_el is not None
                        and local(next_el.tag) in joinable
                        and not child.tail.strip() and "\n" in child.tail):
                    pass
                else:
                    parts.append(esc(collapse(child.tail)))
        text = escape_leading_marker("".join(parts).strip())
        if text:
            lines.append(f"{indent}- {text}")
        for sub in sub_lists:
            lines.extend(render_list(sub, depth + 1))
    return lines


def render_closer(closer_el):
    signed = closer_el.find("t:signed", namespaces=NS)
    out = []
    if signed is not None:
        txt = render_inline(signed).strip()
        txt = re.sub(r"\s+", " ", txt)
        out.append("#align(right)[" + txt + "]")
        out.append("")
    return out


def render_block(el):
    tag = local(el.tag)
    if tag == "p":
        txt = render_inline(el).strip()
        txt = re.sub(r" +", " ", txt)
        return [txt, ""] if txt else []
    if tag == "list":
        return render_list(el) + [""]
    if tag == "closer":
        return render_closer(el)
    if tag in ("q",):
        txt = render_inline(el).strip()
        return [f"#quote(block: true)[{txt}]", ""] if txt else []
    if tag in ("pb", "head", "fw", "trailer"):
        return []
    # Fallback: try to render as a paragraph so we never drop content.
    txt = render_inline(el).strip()
    return [txt, ""] if txt else []


def render_heads(div_el, level):
    """Render every direct <head> child of a div. The first becomes the
    heading at `level`; subsequent ones (e.g. a chapter's descriptive
    subtitle) are emphasized lines just under it."""
    out = []
    heads = div_el.findall("t:head", namespaces=NS)
    for i, head in enumerate(heads):
        text = render_inline(head).strip()
        text = re.sub(r"\s+", " ", text)
        if not text:
            continue
        if i == 0:
            out.append(f"{'=' * level} {text}")
        else:
            out.append(f"#emph[{text}]")
            out.append("")
    if len(heads) == 1:
        out.append("")
    return out


def render_div(div_el, level):
    out = []
    out.extend(render_heads(div_el, level))
    for child in div_el:
        tag = local(child.tag)
        if tag == "head":
            continue
        if tag == "div":
            out.extend(render_div(child, level + 1))
        else:
            out.extend(render_block(child))
    return out


PREAMBLE = '''#set page(width: 6in, height: 9in, margin: 1in)
#set par(justify: true)
#set text(font: "New Computer Modern", size: 11pt)

'''


def render_top_div(div_el):
    lines = [PREAMBLE.rstrip("\n")]
    lines.append("")
    lines.extend(render_div(div_el, 1))
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Top-level division discovery (the quod.lib.umich.edu "1:N" numbering)
# ---------------------------------------------------------------------------

def get_top_divs(root):
    """Return the flattened, in-document-order list of div1-equivalent
    elements: the direct <div> children of <front>, <body>, <back>.
    This matches the 1:1, 1:2, 1:3... numbering used by the
    quod.lib.umich.edu ".../1:N?rgn=div1" fulltext URLs."""
    divs = []
    text_el = root.find(".//t:text", namespaces=NS)
    for section_name in ("front", "body", "back"):
        section = text_el.find(f"t:{section_name}", namespaces=NS)
        if section is not None:
            divs.extend(section.findall("t:div", namespaces=NS))
    return divs


def div_label(div_el, index):
    dtype = div_el.get("type")
    head = div_el.find("t:head", namespaces=NS)
    title = ""
    if head is not None:
        title = render_inline(head).strip()
        title = re.sub(r"\s+", " ", title)[:60]
    return dtype or f"section{index}", title


def slugify(s):
    s = re.sub(r"[^a-zA-Z0-9]+", "_", s).strip("_").lower()
    return s or "section"


# ---------------------------------------------------------------------------
# Fetching a text by TCP id
# ---------------------------------------------------------------------------

def resolve_xml_path(source, cache_dir):
    p = Path(source)
    if p.suffix.lower() == ".xml" and p.exists():
        return p
    # Treat as a TCP id, e.g. "A09377"
    tcp_id = source.upper()
    repo_dir = cache_dir / tcp_id
    xml_path = repo_dir / f"{tcp_id}.xml"
    if xml_path.exists():
        return xml_path
    cache_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://github.com/textcreationpartnership/{tcp_id}.git"
    print(f"Cloning {url} ...", file=sys.stderr)
    subprocess.run(
        ["git", "clone", "--depth", "1", url, str(repo_dir)],
        check=True,
    )
    if not xml_path.exists():
        raise FileNotFoundError(f"Expected {xml_path} after cloning {url}")
    return xml_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="A TCP id (e.g. A09377) or a path to a local TEI XML file")
    ap.add_argument("--sections", nargs="*", type=int, default=None,
                     help="1-based indices of top-level divs to convert (matches quod.lib's 1:N). Default: all.")
    ap.add_argument("--outdir", default="out", help="Output directory for .typ (and .pdf) files")
    ap.add_argument("--cache-dir", default=".tcp_cache", help="Where to clone TCP repos when given an id")
    ap.add_argument("--list", action="store_true", help="Just list the top-level divs (index, type, heading) and exit")
    ap.add_argument("--pdf", action="store_true", help="Also compile each .typ to .pdf (requires the `typst` python package)")
    args = ap.parse_args()

    xml_path = resolve_xml_path(args.source, Path(args.cache_dir))
    tree = etree.parse(str(xml_path))
    root = tree.getroot()
    top_divs = get_top_divs(root)

    if not top_divs:
        print("No top-level <div> elements found under front/body/back.", file=sys.stderr)
        sys.exit(1)

    if args.list:
        for i, div_el in enumerate(top_divs, start=1):
            dtype, title = div_label(div_el, i)
            suffix = f" -- {title}" if title else ""
            print(f"1:{i}\t{dtype}{suffix}")
        return

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    wanted = set(args.sections) if args.sections else set(range(1, len(top_divs) + 1))

    for i, div_el in enumerate(top_divs, start=1):
        if i not in wanted:
            continue
        dtype, title = div_label(div_el, i)
        fname = f"{i:02d}_{slugify(dtype)}.typ"
        out_text = render_top_div(div_el)
        out_path = outdir / fname
        out_path.write_text(out_text, encoding="utf-8")
        print(f"Wrote {out_path} (1:{i}, type={dtype})")
        if args.pdf:
            import typst
            pdf_path = out_path.with_suffix(".pdf")
            typst.compile(str(out_path), output=str(pdf_path))
            print(f"Compiled {pdf_path}")


if __name__ == "__main__":
    main()
