#!/usr/bin/env python3
"""
slips.py: likely slips in an edition, found with a second modern witness.

  python3 slips.py BOOK.tei.xml WITNESS [--files a.typ,b.typ,...] [--min-context 6]

The edition (the TEI's reading text) is compared with two other texts of
the same work:

  the early printing   the TEI's machine pass alone (tei_extract --only-auto:
                       the printed text, spelling modernized, nothing else)
  the witness          a modern text of the same early printing (Monergism's
                       PDF, Chapel Library's EPUB, a .txt, or a folder of
                       .typ files)

A place where the edition departs from the early printing *and* the witness
agrees with the early printing is listed: a scanning slip in the edition
(Gentles for Gentiles, "the church lied into the wilderness"), a dropped or
added word, a changed word. Where the witness differs too, the change is
shared editing and is not listed. Scripture references are left out. Words
are compared loosely (drift.loose: case, punctuation, u/v, i/j, doubled
letters and a final e ignored), so spelling modernization is mostly not
listed either; read the list, it still holds some.

The witness is only compared, never copied: a witness may be under copyright.

Markdown goes to stdout: one line per place, "file  …context [early/witness:
X] [edition: Y] following…".
"""

import argparse
import difflib
import html
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import drift  # noqa: E402
import layout  # noqa: E402


def witness_words(path):
    """The words of a witness file or folder, in reading order."""
    p = Path(path)
    if p.is_dir():
        return drift.typ_words(sorted(p.glob("*.typ")), False)
    if p.suffix == ".pdf":
        text = subprocess.run(["pdftotext", str(p), "-"], capture_output=True,
                              text=True, check=True).stdout
    elif p.suffix == ".epub":
        z = zipfile.ZipFile(p)
        opf = next(n for n in z.namelist() if n.endswith(".opf"))
        o = z.read(opf).decode("utf-8")
        base = str(Path(opf).parent)
        man = {i: h for i, h in re.findall(r'<item[^>]*?id="([^"]*)"[^>]*?href="([^"]*)"', o)}
        man.update({i: h for h, i in re.findall(r'<item[^>]*?href="([^"]*)"[^>]*?id="([^"]*)"', o)})
        parts = []
        for i in re.findall(r'idref="([^"]*)"', o):
            h = man.get(i, "")
            if not h.endswith(("html", "htm")):
                continue
            name = h if base in ("", ".") else f"{base}/{h}"
            t = z.read(name).decode("utf-8", "replace")
            t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", t, flags=re.S)
            parts.append(html.unescape(re.sub(r"<[^>]+>", " ", t)))
        text = "\n".join(parts)
    else:
        text = p.read_text(encoding="utf-8")
    return [w for w in re.findall(r"[\w’'-]+", text) if re.search(r"\w", w)]


def edition_words(tei, files, only_auto):
    """(words, file of each word) of the TEI's reading text."""
    with tempfile.TemporaryDirectory() as d:
        args = [sys.executable, str(HERE / "tei_extract.py"), str(tei), d, "--layer", "reg"]
        if only_auto:
            args.append("--only-auto")
        subprocess.run(args, check=True, capture_output=True)
        out, of = [], []
        for f in files:
            ws = drift.without_refs(drift.typ_words([Path(d) / f], False))
            out += ws
            of += [f] * len(ws)
        return out, of


def book_files(tei):
    """The chapter files in reading order (the LAYOUT's, else the extraction's)."""
    cfg = layout.settings(tei)
    if cfg.get("LAYOUT"):
        from lxml import etree
        root = etree.parse(str(tei)).getroot()
        return [f["file"] for f in layout.book_layout(root, cfg)]
    with tempfile.TemporaryDirectory() as d:
        subprocess.run([sys.executable, str(HERE / "tei_extract.py"), str(tei), d,
                        "--layer", "reg"], check=True, capture_output=True)
        return sorted(str(p.relative_to(d)) for p in Path(d).rglob("*.typ"))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tei")
    ap.add_argument("witness")
    ap.add_argument("--files", help="chapter files in reading order (comma-separated)")
    ap.add_argument("--min-context", type=int, default=6)
    a = ap.parse_args()
    files = a.files.split(",") if a.files else book_files(a.tei)
    L = drift.loose
    ed, of = edition_words(a.tei, files, False)
    au, _ = edition_words(a.tei, files, True)
    wi = drift.without_refs(witness_words(a.witness))
    le, la, lw = [L(w) for w in ed], [L(w) for w in au], [L(w) for w in wi]
    # early printing -> witness positions, where they agree
    a2w = {}
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lw, autojunk=False).get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                a2w[i1 + k] = j1 + k
    n = 0
    c = a.min_context
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, le, la, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        a0, a1 = j1 - 1, j2
        if a0 in a2w and a1 in a2w:
            span = [L(w) for w in wi[a2w[a0] + 1:a2w[a1]]]
            if span == la[j1:j2]:
                n += 1
                f = of[min(i1, len(of) - 1)]
                print(f"{f}\t…{' '.join(ed[max(0, i1 - c):i1])} "
                      f"[early/witness: {' '.join(au[j1:j2]) or '(nothing)'}] "
                      f"[edition: {' '.join(ed[i1:i2]) or '(nothing)'}] "
                      f"{' '.join(ed[i2:i2 + 4])}…")
    print(f"{n} places", file=sys.stderr)


if __name__ == "__main__":
    main()
