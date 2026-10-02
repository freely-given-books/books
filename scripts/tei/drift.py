#!/usr/bin/env python3
"""
drift.py: how far a witness's text is from a TEI edition's reading text.

  python3 drift.py EDITION.tei.xml WITNESS [--min N] [--title T] [--strict]

The edition's reading text is extracted (tei_extract.py, reg layer) and
compared word by word with the witness, which is one of:

  a TEI file (an EEBO-TCP transcription)   its text without margin notes;
                                           "--div TYPE=FILE[,FILE]" pairs a
                                           division with the edition's files
  a folder of Typst files (an older copy)  every .typ file, in name order

Words are compared loosely by default (case, punctuation, u/v, i/j, y/i,
doubled letters and a final e ignored), which suits an early printing:
what is left is a different, added or missing word. Scripture references
(inline in a modern text, in the margin of a printing) are left out there. --strict compares the
words exactly, punctuation included, for two modern copies. Passages of
fewer than --min words that differ are counted but not listed.

Markdown goes to stdout.
"""

import argparse
import difflib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from lxml import etree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reviewparse  # noqa: E402

T = "{http://www.tei-c.org/ns/1.0}"


def loose(w):
    w = w.lower().replace("ſ", "s")
    w = re.sub(r"[^a-z]", "", w).replace("v", "u").replace("j", "i").replace("y", "i")
    w = re.sub(r"(.)\1", r"\1", w)
    return w[:-1] if len(w) > 3 and w.endswith("e") else w


BOOKS = set("""Gen Genesis Exod Exo Ex Lev Num Deut Deu Josh Judg Ruth Sam Kings Kgs Chron
Chr Ezra Neh Esth Job Psa Psalm Psalms Ps Prov Pro Eccl Eccles Ecc Song Cant Isa Isaiah Jer
Lam Ezek Eze Dan Hos Joel Amos Obad Jonah Jon Mic Micah Nah Hab Habak Zeph Hag Zech Mal Matt
Mat Mark Luke John Acts Act Rom Cor Gal Eph Phil Col Thess Thes Tim Titus Tit Philem Heb
James Jas Pet Jude Rev""".split())


def without_refs(ws):
    """Scripture references left out (a modern text's inline "Isa. 64:6", a
    printing's margin note): a book name followed by a number, and numbers."""
    out = []
    for k, w in enumerate(ws):
        nxt = next((x for x in ws[k + 1:k + 3] if re.search(r"\w", x)), "")
        if w.isdigit() or (w in BOOKS and nxt.isdigit()):
            continue
        out.append(w)
    return out


def typ_words(files, strict):
    out = []
    for f in files:
        text = Path(f).read_text(encoding="utf-8")
        try:
            r = reviewparse.parse_review(text, inline_headings=True)
        except ValueError:
            # a #quote[...] across blank lines (an older copy): its markup is
            # not words, so read the text without it
            text = re.sub(r"(?<!\\)\](?=\s*$)", "", text.replace("#quote[", ""), flags=re.M)
            r = reviewparse.parse_review(text, inline_headings=True)
        for t, kind, _it in r.body:
            if kind != "w" or t in ("\\",):
                continue
            if strict or re.search(r"\w", t):
                out.append(t)
    return out


def tei_words(path, div_types):
    root = etree.parse(str(path)).getroot()
    divs = [d for d in root.iter(T + "div") if d.get("type") in div_types]
    out = []
    for d in divs:
        d = etree.fromstring(etree.tostring(d))
        for n in list(d.iter(T + "note")) + list(d.iter(T + "g")) + list(d.iter(T + "desc")):
            p, prev = n.getparent(), n.getprevious()
            tail = n.tail or ""
            if prev is not None:
                prev.tail = (prev.tail or "") + tail
            else:
                p.text = (p.text or "") + tail
            p.remove(n)
        for h in list(d.iter(T + "head")):
            h.getparent().remove(h) if h.getparent() is d else None
        out += [w for w in re.findall(r"[\w’'ſ-]+", " ".join(d.itertext())) if loose(w)]
    return out


def report(a, b, an, bn, strict, min_words, width=8):
    key = (lambda w: w) if strict else loose
    ka, kb = [key(w) for w in a], [key(w) for w in b]
    if not strict:
        ka = [k or "\0" for k in ka]
    sm = difflib.SequenceMatcher(None, ka, kb, autojunk=False)
    ops = [o for o in sm.get_opcodes() if o[0] != "equal"]
    big = [o for o in ops if max(o[2] - o[1], o[4] - o[3]) >= min_words]
    only_a = sum(i2 - i1 for op, i1, i2, j1, j2 in ops if op in ("delete", "replace"))
    only_b = sum(j2 - j1 for op, i1, i2, j1, j2 in ops if op in ("insert", "replace"))
    lines = [f"- {an}: {len(a)} words; {bn}: {len(b)} words; "
             f"{sm.ratio() * 100:.2f}% alike",
             f"- {len(ops)} places differ ({only_a} words of the {an}, "
             f"{only_b} of the {bn}); {len(big)} of them are {min_words} words or more"
             + (", listed below" if big and min_words > 1 else ""), ""]
    for op, i1, i2, j1, j2 in big:
        ctx = " ".join(a[max(0, i1 - width):i1])
        what = {"insert": f"only in the {bn}", "delete": f"only in the {an}",
                "replace": "different"}[op]
        lines.append(f"- **{what}** ({max(i2 - i1, j2 - j1)} words), after "
                     f"“…{ctx}”")
        if i2 > i1:
            lines.append(f"  - {an}: {short(a[i1:i2])}")
        if j2 > j1:
            lines.append(f"  - {bn}: {short(b[j1:j2])}")
    return lines


def short(ws, n=40):
    s = " ".join(ws)
    return s if len(ws) <= n else " ".join(ws[:n // 2]) + " … " + " ".join(ws[-n // 4:])


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edition")
    ap.add_argument("witness")
    ap.add_argument("--div", action="append", default=[],
                    help="TYPE=FILE[,FILE...]: a witness division and the edition files it "
                    "matches (TEI witness)")
    ap.add_argument("--min", type=int, default=1)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--name", default="witness")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, str(HERE / "tei_extract.py"), a.edition, tmp,
                        "--layer", "reg"], check=True, capture_output=True)
        ed = Path(tmp)
        w = Path(a.witness)
        if w.is_dir():
            files = sorted(p.relative_to(w) for p in w.rglob("*.typ"))
            print(f"## The edition and {a.name}\n")
            for f in files:
                if not (ed / f).exists():
                    print(f"- {f}: not in the edition\n")
                    continue
                aw = typ_words([ed / f], a.strict)
                bw = typ_words([w / f], a.strict)
                if aw == bw:
                    continue
                print(f"### {f}\n")
                print("\n".join(report(aw, bw, "edition", a.name, a.strict, a.min)) + "\n")
        else:
            print(f"## The edition and {a.name}\n")
            for spec in a.div:
                typ, fs = spec.split("=", 1)
                aw = without_refs(typ_words([ed / f for f in fs.split(",")], False))
                bw = without_refs(tei_words(w, {typ}))
                print(f"### {typ} ({fs})\n")
                print("\n".join(report(aw, bw, "edition", a.name, False, a.min)) + "\n")


if __name__ == "__main__":
    main()
