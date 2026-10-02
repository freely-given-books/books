#!/usr/bin/env python3
"""
fgb: one command for the TEI book pipeline. Run it through ./fgb at the
repository root (which sets up the Python environment the first time); it
works from any folder.

  ./fgb list                      books with a TEI edition
  ./fgb sync   [BOOK]             after editing chapters/typ: fold the edits
                                  into the TEI, show what changed, refresh the
                                  side-by-side page
  ./fgb find   [BOOK] WORD        every place WORD is, in chapters/typ and as
                                  printed, with what the machine and you chose
  ./fgb page   [BOOK] [--open]    rebuild the side-by-side page(s)
  ./fgb check  [BOOK]             full verification (verify.py)
  ./fgb epub   [BOOK]             build the EPUB and run epubcheck
  ./fgb pdf    [BOOK]             compile the print edition(s) with Typst
  ./fgb build  [BOOK ...]         PDFs (print editions, then covers) and the
                                  checked EPUB into dist/<author>/<book>/;
                                  no BOOK = every book on the TEI pipeline.
                                  --pdf / --epub for one kind, --out DIR

BOOK is any part of the book's folder name ("gouge", "perkins", "simon");
leave it out when you are inside the book's folder.

A book's source/editorial.py can hold what these commands need, so nobody
has to remember options:

  EPUB = {"title": ..., "author": ..., "front": "ebook-front.html",
          "cover": "cover_front.jpg", "css": [...], "before": [...],
          "after": [...], "toc_depth": 4}          # paths from the book folder
  PRINT = ["book.typ"]                             # Typst files to compile
  COVERS = ["cover.typ"]       # covers, compiled after PRINT (default cover*.typ)
  SIDE_BY_SIDE = {"before": [...], "after": [...],
                  "split": ["vol-1/", ...]}        # one page per prefix
"""

import argparse
import os
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PY = sys.executable


# -- finding the book --------------------------------------------------------

def books():
    return sorted(p.parent.parent for p in REPO.glob("books/*/*/source/*.tcp.xml"))


def find_book(name):
    if name is None:
        cwd = Path.cwd().resolve()
        for b in books():
            if cwd == b or b in cwd.parents:
                return b
        sys.exit("which book? give part of its name (./fgb list), "
                 "or run this inside the book's folder")
    hits = [b for b in books() if name.lower() in str(b.relative_to(REPO)).lower()]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        sys.exit(f"no book matches '{name}' (./fgb list)")
    sys.exit(f"'{name}' matches several books: " +
             ", ".join(str(b.relative_to(REPO / "books")) for b in hits))


class Book:
    def __init__(self, path):
        self.dir = path
        self.src = path / "source"
        self.tcp = next(self.src.glob("*.tcp.xml"))
        self.tei = next(self.src.glob("*.tei.xml"), self.src / (path.name + ".tei.xml"))
        self.chapters = path / "chapters" / "typ"
        self.report = self.src / "review-report.md"
        ed = self.src / "editorial.py"
        sys.path.insert(0, str(HERE))
        self.cfg = runpy.run_path(str(ed)) if ed.exists() else {}

    @property
    def name(self):
        return str(self.dir.relative_to(REPO / "books"))


def run(*args, cwd=None, quiet=False):
    r = subprocess.run([str(a) for a in args], cwd=cwd, capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(r.stdout + r.stderr)
        sys.exit(f"failed: {' '.join(str(a) for a in args[:3])} ...")
    if not quiet and r.stdout.strip():
        print(r.stdout.strip())
    return r.stdout


# -- reports -----------------------------------------------------------------

def report_entries(path):
    """{section: [entry lines]} and the counts table of a review report."""
    if not path.exists():
        return {}, {}
    sec, out, counts = None, {}, {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| (\S[^|]*?) \| (\d+) \|$", line)
        if m:
            counts[m.group(1)] = int(m.group(2))
        if line.startswith("## "):
            sec = line[3:].strip()
            out.setdefault(sec, [])
        elif sec and line.startswith("- "):
            out[sec].append(line[2:])
    return out, counts


def show_changes(before, after):
    (b_ent, b_cnt), (a_ent, a_cnt) = before, after
    moved = False
    for sec in sorted(set(b_ent) | set(a_ent)):
        if sec in ("Please check",):
            continue
        old, new = b_ent.get(sec, []), a_ent.get(sec, [])
        added = [e for e in new if e not in old]
        gone = [e for e in old if e not in new]
        if not (added or gone):
            continue
        moved = True
        print(f"  {sec}:")
        for e in added[:15]:
            print(f"    + {e}")
        for e in gone[:15]:
            print(f"    - {e}")
        if len(added) > 15 or len(gone) > 15:
            print(f"    ... ({len(added)} new, {len(gone)} gone; see {sec} in the report)")
    if not moved:
        print("  no decisions changed")


# -- commands ----------------------------------------------------------------

def cmd_list(a):
    for b in books():
        bk = Book(b)
        state = "TEI" if bk.tei.exists() else "no TEI yet"
        print(f"  {bk.name:55} {state}")


def cmd_sync(a):
    bk = Book(find_book(a.book))
    before = report_entries(bk.report)
    print(f"{bk.name}: folding chapters/typ into the TEI ...")
    out = run(PY, HERE / "build_tei.py", bk.tcp.name, bk.tei.name,
              "--review", bk.chapters, "--report", bk.report.name, cwd=bk.src, quiet=True)
    print("  " + out.strip().splitlines()[-1].split(": ", 1)[-1])
    after = report_entries(bk.report)
    print("changes since the last sync:")
    show_changes(before, after)
    unresolved = after[0].get("not applied", []) + after[0].get("unresolved", [])
    if unresolved:
        print(f"\n{len(unresolved)} edit(s) could NOT be applied (they are missing from the TEI):")
        for e in unresolved[:20]:
            print("  ! " + e)
    cmd_page(a, bk, quiet=True)
    print("\nnext: ./fgb check to verify, then commit")


def cmd_find(a):
    bk = Book(find_book(a.book))
    word = a.word
    rx = re.compile(r"(?<![\w'])" + re.escape(word) + r"(?![\w'])", re.I)
    # search the TEI's own reading text (a fresh extraction), then point at
    # the same line in chapters/typ, where the edit is made
    tmp = Path(tempfile.mkdtemp(prefix="fgb-find-"))
    run(PY, HERE / "tei_extract.py", bk.tei, tmp, "--layer", "reg", quiet=True)
    orig = Path(tempfile.mkdtemp(prefix="fgb-find-orig-"))
    run(PY, HERE / "tei_extract.py", bk.tei, orig, "--layer", "orig", quiet=True)
    print(f"{bk.name}: '{word}' in the edition")
    n, stale = 0, 0
    for f in sorted(tmp.rglob("*.typ")):
        rel = f.relative_to(tmp)
        mine = bk.chapters / rel
        mine_lines = mine.read_text(encoding="utf-8").splitlines() if mine.exists() else []
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for m in rx.finditer(line):
                n += 1
                s_ = line[max(0, m.start() - 70):m.end() + 50]
                s_ = re.sub(r"#(emph|footnote|strong|super)\[", "", s_).replace("]", "")
                at = next((k for k, l in enumerate(mine_lines, 1) if l == line), None)
                if at is None:
                    stale += 1
                where = f"chapters/typ/{rel}:{at}" if at else f"chapters/typ/{rel} (not synced)"
                print(f"  {where}\n      ...{s_.strip()}...")
    if not n:
        print("  (not in the edition's text)")
    if stale:
        print(f"\n  {stale} of these are not in chapters/typ as the TEI has them: "
              "chapters/typ is out of step with the TEI (run ./fgb sync first, "
              "or the chapters have not been replaced with the extraction yet)")
    printed = sum(len(rx.findall(f.read_text(encoding="utf-8").replace("ſ", "s")))
                  for f in orig.rglob("*.typ"))
    print(f"\nas printed: {printed} time(s)")
    shutil.rmtree(tmp, ignore_errors=True)
    shutil.rmtree(orig, ignore_errors=True)
    # the TEI: every choice whose printed or modern form is the word
    from lxml import etree
    T = "{http://www.tei-c.org/ns/1.0}"
    txt = lambda el: "".join(el.itertext()).replace("ſ", "s") if el is not None else ""
    rows = {}
    for ch in etree.parse(str(bk.tei)).getroot().iter(T + "choice"):
        orig = ch.find(T + "orig")
        regs = ch.findall(T + "reg")
        if orig is None or not regs:
            continue
        forms = [txt(orig)] + [txt(r) for r in regs]
        if not any(rx.fullmatch(f.strip()) for f in forms):
            continue
        ed = next((txt(r) for r in regs if r.get("resp") == "#editor"), None)
        au = next((txt(r) for r in regs if r.get("resp") == "#auto"), None)
        key = (txt(orig), au, ed)
        rows[key] = rows.get(key, 0) + 1
    if rows:
        print("recorded choices (printed -> machine -> your text):")
        for (o, au, ed), k in sorted(rows.items(), key=lambda kv: -kv[1]):
            print(f"  {o} -> {au or o} -> {ed or '(the machine’s)'}   x{k}")
    print("\nto change one: edit the line above, then ./fgb sync")


def side_pages(bk):
    cfg = bk.cfg.get("SIDE_BY_SIDE", {})
    extra = [x for f in cfg.get("before", []) for x in ("--before", bk.dir / f)] + \
            [x for f in cfg.get("after", []) for x in ("--after", bk.dir / f)]
    split = cfg.get("split")
    if not split:
        return [(bk.dir / "side-by-side.html", extra)]
    return [(bk.dir / f"side-by-side-{p.strip('/')}.html", ["--only", p])
            for p in split]


def cmd_page(a, bk=None, quiet=False):
    bk = bk or Book(find_book(a.book))
    for out, extra in side_pages(bk):
        run(PY, HERE / "tei_review.py", bk.tei, out, *extra, cwd=bk.dir, quiet=True)
        print(f"side-by-side: {out.relative_to(REPO)}")
        if getattr(a, "open", False):
            subprocess.Popen(["xdg-open", str(out)], stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)


def cmd_check(a):
    bk = Book(find_book(a.book))
    r = subprocess.run([PY, str(HERE / "verify.py"), str(bk.dir)])
    sys.exit(r.returncode)


def build_epub(bk, outdir):
    e = bk.cfg.get("EPUB")
    if not e:
        sys.exit(f"{bk.name}: no EPUB settings in source/editorial.py (see ./fgb --help)")
    out = outdir / e.get("file", bk.dir.name + ".epub")
    args = [PY, HERE / "tei_epub.py", bk.tei, out, "--title", e["title"],
            "--author", e["author"]]
    for k in ("front", "cover"):
        if e.get(k):
            args += [f"--{k}", bk.dir / e[k]]
    for k in ("css", "before", "after"):
        for f in e.get(k, []):
            args += [f"--{k}", f]
    if e.get("toc_depth"):
        args += ["--toc-depth", e["toc_depth"]]
    run(*args, cwd=bk.dir)
    if shutil.which("epubcheck"):
        r = subprocess.run(["epubcheck", str(out)], capture_output=True, text=True)
        line = next((l for l in (r.stdout + r.stderr).splitlines() if l.startswith("Messages")), "")
        print("epubcheck: " + (line or "failed to run"))
        if r.returncode:
            print(r.stdout[-2000:] + r.stderr[-2000:])
            sys.exit(f"{bk.name}: epubcheck failed")
    else:
        print("epubcheck: not installed, EPUB not checked")
    return [out]


def build_pdf(bk, outdir, covers=False):
    files = bk.cfg.get("PRINT") or [bk.dir.name + ".typ"]
    if covers:
        files = files + (bk.cfg.get("COVERS") or
                         sorted(p.name for p in bk.dir.glob("cover*.typ")))
    outs = []
    for f in files:
        src = bk.dir / f
        out = outdir / Path(f).with_suffix(".pdf").name
        print(f"typst: {src.relative_to(REPO)}")
        # --root: covers import the shared design from scripts/
        run("typst", "compile", "--root", REPO, src, out, cwd=bk.dir)
        outs.append(out)
    return outs


def cmd_epub(a):
    bk = Book(find_book(a.book))
    build_epub(bk, bk.dir)


def cmd_pdf(a):
    bk = Book(find_book(a.book))
    build_pdf(bk, bk.dir)


# -- build: everything for some or all books, into dist/ -----------------------

def book_dirs():
    """Every book folder under books/ (books/<author>/<book>), on the TEI
    pipeline or not."""
    return sorted(p for p in REPO.glob("books/*/*") if p.is_dir()
                  and p.parent.name != "resources" and not p.name.startswith("."))


def incompatible(path):
    """Why a book folder cannot be built by the TEI pipeline ([] if it can)."""
    src = path / "source"
    why = []
    if not any(src.glob("*.tcp.xml")):
        why.append("no source/*.tcp.xml")
    if not any(src.glob("*.tei.xml")):
        why.append("no enriched TEI (source/*.tei.xml)")
    ed = src / "editorial.py"
    if not ed.exists():
        why.append("no source/editorial.py")
    else:
        text = ed.read_text(encoding="utf-8")
        for k in ("EPUB", "PRINT"):
            if not re.search(rf"^{k}\s*=", text, re.M):
                why.append(f"no {k} settings in source/editorial.py")
    return why


def git_state():
    r = subprocess.run(["git", "-C", str(REPO), "describe", "--always", "--dirty"],
                       capture_output=True, text=True)
    return r.stdout.strip() or "unknown"


def cmd_build(a):
    all_dirs = book_dirs()
    if a.books:
        chosen = []
        for name in a.books:
            hits = [d for d in all_dirs if name.lower() in str(d.relative_to(REPO)).lower()]
            if not hits:
                sys.exit(f"no book matches '{name}'")
            if len(hits) > 1:
                sys.exit(f"'{name}' matches several books: " +
                         ", ".join(str(d.relative_to(REPO / "books")) for d in hits))
            why = incompatible(hits[0])
            if why:
                sys.exit(f"{hits[0].relative_to(REPO / 'books')} is not compatible with the "
                         f"TEI pipeline ({'; '.join(why)}); nothing was built")
            if hits[0] not in chosen:
                chosen.append(hits[0])
    else:
        chosen = [d for d in all_dirs if not incompatible(d)]
        skipped = [d for d in all_dirs if incompatible(d)]
        if skipped:
            print("not on the TEI pipeline yet, skipped: " +
                  ", ".join(str(d.relative_to(REPO / "books")) for d in skipped))
    kinds = {"pdf", "epub"} if a.pdf == a.epub else ({"pdf"} if a.pdf else {"epub"})
    out_root = Path(a.out).resolve() if a.out else REPO / "dist"
    state = git_state()
    built, failed = [], []
    for d in chosen:
        bk = Book(d)
        outdir = out_root / bk.name
        outdir.mkdir(parents=True, exist_ok=True)
        print(f"\n== {bk.name} -> {outdir}")
        try:
            files = []
            if "pdf" in kinds:
                files += build_pdf(bk, outdir, covers=True)
            if "epub" in kinds:
                files += build_epub(bk, outdir)
        except SystemExit as e:
            print(f"FAILED: {e}" if e.code not in (None, 0, 1) else "FAILED")
            failed.append(bk.name)
            continue
        (outdir / "build-info.txt").write_text(
            f"{bk.name}\nbuilt from commit {state}\n" +
            "".join(f"{f.name}\n" for f in files), encoding="utf-8")
        built.append((bk.name, files))
    print()
    for name, files in built:
        size = sum(f.stat().st_size for f in files) / 1e6
        print(f"  built  {name:50} {len(files)} file(s), {size:.1f} MB")
    for name in failed:
        print(f"  FAILED {name}")
    if state.endswith("-dirty"):
        print(f"note: the working tree has uncommitted changes ({state})")
    sys.exit(1 if failed else 0)


def main():
    ap = argparse.ArgumentParser(prog="fgb", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    for name, fn in (("sync", cmd_sync), ("check", cmd_check), ("epub", cmd_epub),
                     ("pdf", cmd_pdf)):
        p = sub.add_parser(name)
        p.add_argument("book", nargs="?")
        p.set_defaults(fn=fn)
    p = sub.add_parser("build", help="PDFs and EPUB into dist/")
    p.add_argument("books", nargs="*", metavar="BOOK")
    p.add_argument("--pdf", action="store_true", help="only the PDFs")
    p.add_argument("--epub", action="store_true", help="only the EPUB")
    p.add_argument("--out", help="output folder (default: dist/ at the repo root)")
    p.set_defaults(fn=cmd_build)
    p = sub.add_parser("page")
    p.add_argument("book", nargs="?")
    p.add_argument("--open", action="store_true", help="open it in the browser")
    p.set_defaults(fn=cmd_page)
    p = sub.add_parser("find")
    p.add_argument("args", nargs="+", metavar="[BOOK] WORD")
    p.set_defaults(fn=cmd_find)
    a = ap.parse_args()
    if a.cmd == "find":
        a.book, a.word = (a.args[0], a.args[1]) if len(a.args) > 1 else (None, a.args[0])
    a.fn(a)


if __name__ == "__main__":
    main()
