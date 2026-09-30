#!/usr/bin/env python3
"""
End-to-end check of a TEI edition. Run from the repository root:

  python3 scripts/tei/verify.py books/william-perkins/christian-economy \
      --tcp A09377.tcp.xml --tei christian-economy.tei.xml

What it checks
  1. Rebuilding the enriched TEI from the TCP file + chapters/typ gives the
     committed TEI (so the TEI and the reviewed chapters agree).
  2. Extracting the reg layer reproduces chapters/typ (ignoring // comment
     lines); lists any chapter that differs.
  3. The orig layer, with gaps shown, has exactly the words of the TCP file.
  4. The TEI validates against tei_all (only if --schema and java + jing
     are available: --jing path/to/jing.jar --schema path/to/tei_all.rng).
  5. The extracted chapters compile with Typst (if the `typst` Python
     package or CLI is installed).

Exit code is 0 when 1, 3 (and 4/5 when run) pass; chapter differences in
step 2 are reported but do not fail, since they may be intentional.
"""

import argparse
import difflib
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import reviewparse  # noqa: E402


def run(*args):
    r = subprocess.run([str(a) for a in args], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"command failed: {' '.join(map(str, args))}\n{r.stdout}{r.stderr}")
    return r.stdout + r.stderr


def chapter_files(d):
    return ["dedication.typ"] + sorted(p.name for p in Path(d).glob("chapter-*.typ"))


def strip_comments(s):
    return "\n".join(l for l in s.split("\n") if not l.lstrip().startswith("//"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book", help="book folder, e.g. books/william-perkins/christian-economy")
    ap.add_argument("--tcp", default=None, help="TCP file name inside source/")
    ap.add_argument("--tei", default=None, help="enriched TEI file name inside source/")
    ap.add_argument("--jing")
    ap.add_argument("--schema")
    a = ap.parse_args()

    book = Path(a.book)
    src = book / "source"
    tcp = src / (a.tcp or next(p.name for p in src.glob("*.tcp.xml")))
    tei = src / (a.tei or next(p.name for p in src.glob("*.tei.xml")))
    chapters = book / "chapters" / "typ"
    ok = True
    tmp = Path(tempfile.mkdtemp(prefix="tei-verify-"))

    # 1. rebuild
    rebuilt = tmp / "rebuilt.tei.xml"
    print(run(sys.executable, HERE / "build_tei.py", tcp, rebuilt,
              "--review", chapters, "--report", tmp / "report.md").strip())
    a_txt = tei.read_text(encoding="utf-8")
    b_txt = rebuilt.read_text(encoding="utf-8")
    # the revisionDesc date differs between runs; ignore that line
    norm = lambda s: "\n".join(l for l in s.split("\n") if 'xml:id="review"' not in l)
    same = norm(a_txt) == norm(b_txt)
    print(f"[1] rebuild matches committed TEI: {same}")
    ok &= same

    # 2. reg layer vs chapters/typ
    reg = tmp / "reg"
    run(sys.executable, HERE / "tei_extract.py", tei, reg, "--layer", "reg")
    differ = []
    for f in chapter_files(chapters):
        mine = strip_comments((chapters / f).read_text()).replace("\n\n\n", "\n\n")
        got = (reg / f).read_text().replace("\n\n\n", "\n\n")
        if mine != got:
            differ.append(f)
    print(f"[2] reg extraction identical to chapters/typ: "
          f"{len(chapter_files(chapters)) - len(differ)}/{len(chapter_files(chapters))}"
          + (f" (differs: {', '.join(differ)})" if differ else ""))

    # 3. orig layer vs TCP words
    o1, o2 = tmp / "orig", tmp / "tcp"
    run(sys.executable, HERE / "tei_extract.py", tei, o1, "--layer", "orig", "--show-gaps")
    run(sys.executable, HERE / "tei_extract.py", tcp, o2, "--layer", "orig")
    words = lambda d: [w for f in chapter_files(d) for w in
                       reviewparse.TOKEN_RE.findall((d / f).read_text())
                       if w not in ("#", "emph", "[", "]")]
    wa, wb = words(o2), words(o1)
    ops = [o for o in difflib.SequenceMatcher(None, wa, wb, autojunk=False).get_opcodes()
           if o[0] != "equal"]
    print(f"[3] orig layer has the TCP words exactly: {not ops}"
          + (f" ({len(ops)} differences)" if ops else ""))
    ok &= not ops

    # 4. schema
    if a.jing and a.schema and shutil.which("java"):
        out = run("java", "-jar", a.jing, a.schema, tei)
        errs = [l for l in out.splitlines() if "error" in l]
        print(f"[4] valid against {Path(a.schema).name}: {not errs}")
        for e in errs[:10]:
            print("    ", e)
        ok &= not errs
    else:
        print("[4] schema validation skipped (pass --jing and --schema)")

    # 5. typst
    book_typ = reg / "book.typ"
    book_typ.write_text("#set page(width: 6in, height: 9in, margin: 1in)\n"
                        + "".join(f'#include "{f}"\n' for f in chapter_files(reg)))
    try:
        import typst
        typst.compile(str(book_typ), output=str(reg / "book.pdf"))
        print("[5] extracted chapters compile with Typst: True")
    except ImportError:
        if shutil.which("typst"):
            run("typst", "compile", book_typ, reg / "book.pdf")
            print("[5] extracted chapters compile with Typst: True")
        else:
            print("[5] Typst not installed; compile check skipped")
    except Exception as e:  # compile error
        print(f"[5] Typst compile FAILED: {e}")
        ok = False

    shutil.rmtree(tmp, ignore_errors=True)
    print("OK" if ok else "FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
