#!/usr/bin/env python3
"""
Compare two versions of a book, to prove that output built from the TEI
matches a finished edition.

  python3 compare.py chapters DIR_A DIR_B      parsed Typst chapters
  python3 compare.py pdf A.pdf B.pdf           rendered text of two PDFs
  python3 compare.py epub A.epub B.epub        text and notes of two EPUBs

chapters  parses every .typ file (subfolders too) in both folders with reviewparse and
          compares words, paragraph breaks, italics, notes (text, italics
          and position) and headings. Blind to spacing and line wrapping.
pdf       word-by-word diff of pdftotext output (pdftotext must be
          installed). A "word" is a run of non-space characters, so it
          catches spacing ("natura(" vs "natura ("). Run it on the print PDF
          compiled from the old and the new chapters. For the strictest check
          also `cmp` the `pdftotext -layout` output, which compares every line
          and page break.
epub      body text of all pages in spine order (spacing-sensitive) and the
          notes, in order, whatever their markup (Typst/Calibre endnotes or
          EPUB 3 asides).

Exit code 0 when nothing differs.
"""

import difflib
import html
import re
import subprocess
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import reviewparse  # noqa: E402


def show(ops, a, b, n=15, width=5):
    for op, i1, i2, j1, j2 in ops[:n]:
        print(f"   {op}: {' '.join(a[max(0, i1 - width):i2 + width])}  |||  "
              f"{' '.join(b[max(0, j1 - width):j2 + width])}")


def diff(a, b):
    return [o for o in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
            if o[0] != "equal"]


def chapters(da, db):
    bad = 0
    for fa in sorted(Path(da).rglob("*.typ")):
        fb = Path(db) / fa.relative_to(da)
        ra = reviewparse.parse_review(fa.read_text())
        rb = reviewparse.parse_review(fb.read_text())
        wa = [(t, k) for t, k, _ in ra.body]
        wb = [(t, k) for t, k, _ in rb.body]
        res = {
            "words": wa == wb,
            "italic": [i for *_, i in ra.body] == [i for *_, i in rb.body],
            "notes": [(n["anchor"], [t for t, _ in n["toks"]]) for n in ra.notes] ==
                     [(n["anchor"], [t for t, _ in n["toks"]]) for n in rb.notes],
            "note italic": [[i for _, i in n["toks"]] for n in ra.notes] ==
                           [[i for _, i in n["toks"]] for n in rb.notes],
            "headings": (ra.headings, ra.short) == (rb.headings, rb.short),
        }
        bad += not all(res.values())
        print(fa.relative_to(da), " ".join(f"{k}={'ok' if v else 'DIFF'}" for k, v in res.items()))
        if not res["words"]:
            show(diff([t for t, _ in wa], [t for t, _ in wb]),
                 [t for t, _ in wa], [t for t, _ in wb], 5)
    return bad == 0


def pdf_words(p):
    t = subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True,
                       check=True).stdout.replace("\f", " ")
    return re.sub(r"-\n(?=[a-z])", "", t).split()     # undo typeset hyphenation


def pdf(a, b):
    wa, wb = pdf_words(a), pdf_words(b)
    ops = diff(wa, wb)
    print(f"words {len(wa)} / {len(wb)}, differences: {len(ops)}")
    show(ops, wa, wb)
    return not ops


def epub_text(p):
    z = zipfile.ZipFile(p)
    opf = next(n for n in z.namelist() if n.endswith(".opf"))
    base = opf.rsplit("/", 1)[0] + "/" if "/" in opf else ""
    o = z.read(opf).decode()
    hrefs = {}
    for tag in re.findall(r"<item\b[^>]*>", o):
        i, h = re.search(r'\bid="([^"]+)"', tag), re.search(r'\bhref="([^"]+)"', tag)
        if i and h:
            hrefs[i.group(1)] = h.group(1)
    s = "".join(re.sub(r".*?<body[^>]*>", "", z.read(base + hrefs[i]).decode(), count=1,
                       flags=re.S)
                for i in re.findall(r'<itemref[^>]*idref="([^"]+)"', o))
    notes = re.findall(r'<span id="loc-\d+">(.*?)</span></li>', s, flags=re.S) + \
        re.findall(r'<li id="loc-\d+"[^>]*>(.*?)</li>', s, flags=re.S) + \
        re.findall(r'<aside id="fn-[^"]+"[^>]*>(.*?)</aside>', s, flags=re.S)
    notes = [" ".join(html.unescape(re.sub(r"<[^>]+>", "", re.sub(
        r'<(a|sup)\b[^>]*role="doc-backlink"[^>]*>.*?</\1>', "", n, flags=re.S))).split())
        for n in notes]
    s = re.sub(r'<section[^>]*role="doc-endnotes"[^>]*>.*?</section>', " ", s, flags=re.S)
    s = re.sub(r'<(ol|section)[^>]*>\s*<li[^>]*>\s*<span id="loc-.*?</\1>', " ", s, flags=re.S)
    s = re.sub(r'<section class="notes">.*?</section>', " ", s, flags=re.S)
    s = re.sub(r'<(a|sup)\b[^>]*role="doc-noteref"[^>]*>.*?</\1>', "", s, flags=re.S)
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"</(p|h\d|dt|dd|li|section|div)>", " ", s)
    return html.unescape(re.sub(r"<[^>]+>", "", s)).split(), notes


def epub(a, b):
    (wa, na), (wb, nb) = epub_text(a), epub_text(b)
    ops = diff(wa, wb)
    print(f"body words {len(wa)} / {len(wb)}, differences: {len(ops)}")
    show(ops, wa, wb)
    same_notes = na == nb
    print(f"notes {len(na)} / {len(nb)}, identical: {same_notes}")
    shown = 0
    for k, (x, y) in enumerate(zip(na, nb)):
        if x != y and shown < 8:
            shown += 1
            print(f"   note {k + 1}: {x[:80]!r}  |||  {y[:80]!r}")
    return not ops and same_notes


def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ("chapters", "pdf", "epub"):
        sys.exit(__doc__)
    ok = {"chapters": chapters, "pdf": pdf, "epub": epub}[sys.argv[1]](sys.argv[2], sys.argv[3])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
