#!/usr/bin/env python3
"""
Show a TCP file's division structure and whether the TEI scripts support it.

  python3 tcp_structure.py SOURCE.xml

build_tei.py, tei_extract.py and tei_to_html.py only handle
div[@type="dedication"] and div[@type="chapter"] (numbered by @n). Any other
division that holds text is reported, so the scripts can be extended before
the book is started.
"""

import sys
from collections import Counter

from lxml import etree

T = "{http://www.tei-c.org/ns/1.0}"
SUPPORTED = {"dedication", "chapter"}


def words(el):
    return len(" ".join(el.itertext()).split())


def main():
    root = etree.parse(sys.argv[1]).getroot()
    title = root.find(f"{T}teiHeader/{T}fileDesc/{T}titleStmt/{T}title")
    if title is not None:
        print(" ".join("".join(title.itertext()).split())[:120])
    print()

    def show(el, depth):
        for d in el.findall(T + "div"):
            head = d.find(T + "head")
            h = " ".join("".join(head.itertext()).split())[:60] if head is not None else ""
            n = f" n={d.get('n')}" if d.get("n") else ""
            mark = "" if d.get("type") in SUPPORTED else "  *"
            print(f"{'  ' * depth}{d.get('type')}{n}  ({words(d)} words)  {h}{mark}")
            if d.get("type") not in SUPPORTED:
                show(d, depth + 1)

    for part in ("front", "body", "back"):
        el = root.find(f".//{T}text/{T}{part}")
        if el is not None and el.find(T + "div") is not None:
            print(f"[{part}]")
            show(el, 1)

    divs = list(root.iter(T + "div"))
    print()
    print("div types:", dict(Counter(d.get("type") for d in divs)))
    missing_n = [d for d in divs if d.get("type") == "chapter" and not d.get("n")]
    # text sitting directly in an unsupported div (not only in supported children)
    stray = [d for d in divs if d.get("type") not in SUPPORTED
             and d.get("type") != "title_page"
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
