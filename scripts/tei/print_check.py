#!/usr/bin/env python3
"""
print_check.py: a print PDF against Lulu's interior rules.

  python3 print_check.py BOOK.pdf [...]

Lulu (help.lulu.com, "Interior Formatting: The Basics"): text, page numbers
and running heads at least 0.5in from the trimmed edge; the inside (binding)
margin by page count:

  under 60 pages 0.5in, 61-150 0.625in, 151-400 1in, 401-600 1.125in,
  over 600 1.25in

Both are measured on the rendered pages (pdftotext -bbox-layout), not read
from the Typst source, so they hold whatever the template or the book set.
The inside margin is the median, over the pages, of each page's text edge
nearest the spine (rectos: page 1, 3, ...; the left edge), which a line of
hanging punctuation does not move. It also warns when a footnote's text is
set on another page than its marker (Typst's widow control can carry the
marker's line over after the note is placed). Exit code 1 when a rule is
broken.
"""

import re
import statistics
import subprocess
import sys

SAFETY = 0.5
TOLERANCE = 0.02                 # inches: rounding of glyph boxes
GUTTER = [(60, 0.5), (150, 0.625), (400, 1.0), (600, 1.125), (10 ** 9, 1.25)]


def lulu_inside(pages):
    return next(m for limit, m in GUTTER if pages <= limit)


def pages_of(pdf):
    """[(width, height, [(x0, y0, x1, y1)...])] in inches, one per page."""
    xml = subprocess.run(["pdftotext", "-bbox-layout", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    out = []
    for m in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S):
        w, h = float(m.group(1)) / 72, float(m.group(2)) / 72
        lines = [tuple(float(v) / 72 for v in g) for g in re.findall(
            r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)"',
            m.group(3))]
        out.append((w, h, lines))
    return out


def words_of(pdf):
    """[[[(text, x0, y0, x1, y1), ...] per line] per page], in points."""
    xml = subprocess.run(["pdftotext", "-bbox-layout", str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    out = []
    for m in re.finditer(r"<page [^>]*>(.*?)</page>", xml, re.S):
        page = []
        for ln in re.findall(r"<line [^>]*>(.*?)</line>", m.group(1), re.S):
            page.append([(t, float(a), float(b), float(c), float(d)) for a, b, c, d, t in
                         re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" '
                                    r'yMax="([\d.]+)">([^<]*)</word>', ln)])
        out.append(page)
    return out


def stray_footnotes(pdf):
    """Footnotes whose text is set on another page than their marker: [(n,
    note page, marker page)]. A note is a small number opening a line at the
    foot of the page; its marker, the same number set small after a word
    on its line ("Suffield¹")."""
    pages = words_of(pdf)
    heights = [w[4] - w[2] for pg in pages for ln in pg for w in ln if w[0].isalpha()]
    if not heights:
        return []
    body = statistics.median(heights)
    out = []
    for i, pg in enumerate(pages):
        for ln in pg:
            first = ln[0] if ln else None
            if not first or not first[0].isdigit() or first[4] - first[2] > 0.8 * body:
                continue
            if first[2] < 0.6 * max(w[4] for l in pg for w in l):
                continue                        # not at the foot of the page
            n = first[0]

            def has_marker(k):
                # the number set small after a word on its line
                return 0 <= k < len(pages) and any(
                    w[0] == n and j > 0 and w[4] - w[2] <= 0.8 * body
                    for l in pages[k] for j, w in enumerate(l))
            if has_marker(i):
                continue
            for k in (i + 1, i - 1):
                if has_marker(k):
                    out.append((n, i + 1, k + 1))
                    break
    return out


def check(pdf):
    """(problems, summary) for one PDF."""
    pages = pages_of(pdf)
    n = len(pages)
    problems, edges = [], {"top": [], "bottom": [], "outside": []}
    inside = []
    for i, (w, h, lines) in enumerate(pages, start=1):
        if not lines:
            continue
        x0 = min(l[0] for l in lines)
        x1 = max(l[2] for l in lines)
        y0 = min(l[1] for l in lines)
        y1 = max(l[3] for l in lines)
        recto = i % 2 == 1
        inside.append(x0 if recto else w - x1)
        near = {"top": y0, "bottom": h - y1, "outside": (w - x1) if recto else x0}
        for k, v in near.items():
            edges[k].append((v, i))
    for k, vals in edges.items():
        bad = [(v, i) for v, i in vals if v < SAFETY - TOLERANCE]
        if bad:
            v, i = min(bad)
            problems.append(f"{len(bad)} page(s) print within {SAFETY}in of the {k} "
                            f"edge (closest {v:.2f}in, page {i})")
    got = statistics.median(inside) if inside else 0
    want = lulu_inside(n)
    if abs(got - want) > TOLERANCE:
        problems.append(f"inside margin {got:.3f}in; Lulu's for {n} pages is {want}in")
    for num, at, mark in stray_footnotes(pdf):
        problems.append(f"footnote {num} is set on page {at}, its marker on page {mark}")
    closest = {k: min(v for v, _ in vals) for k, vals in edges.items() if vals}
    summary = (f"{n} pages, inside {got:.3f}in (Lulu {want}in); closest to the trim: " +
               ", ".join(f"{k} {v:.2f}in" for k, v in closest.items()))
    return problems, summary


def main():
    bad = False
    for pdf in sys.argv[1:]:
        problems, summary = check(pdf)
        print(f"{pdf}: {summary}")
        for p in problems:
            print(f"  ! {p}")
        bad |= bool(problems)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
