#!/usr/bin/env python3
"""
Show a TCP file's division structure and whether the TEI scripts support it.

  python3 tcp_structure.py SOURCE.xml

build_tei.py, tei_extract.py and tei_to_html.py only handle
div[@type="dedication"] and div[@type="chapter"] (numbered by @n). Any other
division that holds text is reported, so the scripts can be extended before
the book is started. Divisions the edition leaves out on purpose (a printed
table of contents, a publisher's advertisement) are listed in the book's
source/editorial.py as SKIP_DIVISIONS = {"table_of_contents", ...}; they are
still in the TEI, as printed, but do not fail the check.

A book of any other shape gets a LAYOUT in its editorial.py (see layout.py:
which divisions and blocks go into which chapter file). With one, the check
is instead that the layout covers every piece of text; the tree is printed
the same way, and --layout lists the files it makes.
"""

import sys
from collections import Counter

from lxml import etree

import sources

T = "{http://www.tei-c.org/ns/1.0}"
SUPPORTED = {"dedication", "chapter"}


def words(el):
    return len(" ".join(el.itertext()).split())


def main():
    import runpy
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import layout
    ed = Path(sys.argv[1]).parent / "editorial.py"
    cfg = runpy.run_path(str(ed)) if ed.exists() else {}
    skip = set(cfg.get("SKIP_DIVISIONS", ()))
    root = sources.load(sys.argv[1]).getroot()
    files = layout.book_layout(root, cfg)
    title = root.find(f"{T}teiHeader/{T}fileDesc/{T}titleStmt/{T}title")
    if title is not None:
        print(" ".join("".join(title.itertext()).split())[:120])
    print()

    def show(el, depth):
        for d in el.findall(T + "div"):
            head = d.find(T + "head")
            h = " ".join("".join(head.itertext()).split())[:60] if head is not None else ""
            n = f" n={d.get('n')}" if d.get("n") else ""
            mark = "" if files is not None and d.get("type") not in skip else \
                "" if d.get("type") in SUPPORTED else \
                "  (left out)" if d.get("type") in skip else "  *"
            print(f"{'  ' * depth}{d.get('type')}{n}  ({words(d)} words)  {h}{mark}")
            if d.get("type") not in SUPPORTED or files is not None:
                show(d, depth + 1)

    for part in ("front", "body", "back"):
        el = root.find(f".//{T}text/{T}{part}")
        if el is not None and el.find(T + "div") is not None:
            print(f"[{part}]")
            show(el, 1)

    divs = list(root.iter(T + "div"))
    print()
    print("div types:", dict(Counter(d.get("type") for d in divs)))
    if files is not None:
        missing = layout.check(root, files, cfg)
        if "--layout" in sys.argv:
            for f in files:
                print(f"  {f['file']}  {f['title'] or ''}  ({len(f['parts'])} parts)")
        for el, n in missing:
            print(f"not in any file: <{layout.local(el)}> {n} words: "
                  f"{' '.join(''.join(el.itertext()).split())[:70]}")
        print(f"\nLAYOUT: {len(files)} files" + (
            ", covers all the text" if not missing else
            f"; {len(missing)} text blocks are in no file (add them, or SKIP_DIVISIONS)"))
        sys.exit(0 if not missing else 1)
    missing_n = [d for d in divs if d.get("type") == "chapter" and not d.get("n")]
    # text sitting directly in an unsupported div (not only in supported children)
    stray = [d for d in divs if d.get("type") not in SUPPORTED
             and d.get("type") != "title_page" and d.get("type") not in skip
             and any(c.tag in (T + "p", T + "list", T + "lg") for c in d)]
    ok = not missing_n and not stray
    if missing_n:
        print(f"{len(missing_n)} chapter div(s) without @n")
    for d in stray:
        print(f"text in unsupported div: type={d.get('type')} ({words(d)} words)")
    print("\nfits the supported shape (dedication + chapters)" if ok else
          "\ndoes NOT fit: extend the division handling first (see the eebo-tcp-book skill)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
