"""Copy the finished Latin and French into the book folder (2026-11-24):
books/.../parallel/{la,fr}/vol-N/<english file stem>.md, one file per chapter (split parts joined, Book I ch. 1-5
taken from the pilot files). Usage: python3 -I export.py BOOK_DIR"""
import importlib.util, pathlib, re, sys
L = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("br", L / "build_review.py"); br = importlib.util.module_from_spec(spec); spec.loader.exec_module(br)
book = pathlib.Path(sys.argv[1])

def joined(folder, name):
    p = folder / f"{name}.md"
    if p.exists():
        return p.read_text()
    parts = sorted(folder.glob(f"{name}.part-*.md"))
    if not parts:
        return None
    # the body text runs on across parts; each part's apparatus and notes follow at the end
    bodies, tails = [], []
    for k, q in enumerate(parts):
        t = q.read_text()
        b = _body_raw(t)
        tails.append(f"<!-- notes of {q.name} -->\n" + t[len(b):].strip())
        if k:  # drop a later part's descriptive header comment, keep page/column markers
            b = re.sub(r"^\s*<!--(?!\s*(?:p\.|col))(.*?)-->", "", b, count=1, flags=re.S)
        bodies.append(b.strip())
    out = bodies[0]
    for b in bodies[1:]:
        lead = re.sub(r"^(?:\s*<!--.*?-->)*\s*", "", b, flags=re.S)
        if out.endswith("-"):
            out = out[:-1] + b
        elif re.match(r"(\d+\.|#)", lead):
            out += "\n\n" + b
        else:
            out += " " + b
    out += "\n\n" + "\n\n".join(x for x in tails if x.split("\n", 1)[1:] and x.split("\n", 1)[1].strip())
    return out

def _body_raw(t):
    return re.split(r"\n###? (?:Apparatus|Notes|Unsettled)|\n## Notes on the transcription", t)[0]

def _body_keep_head(t):
    return _body_raw(t)

n = 0
for v in range(1, 7):
    for typ in sorted((book / "chapters/typ" / f"vol-{v}").glob("*.typ")):
        name = typ.stem
        for lang, head in (("la", "Caput"), ("fr", "Chapitre")):
            m = re.match(r"book-1-chapter-0([1-5])$", name)
            if v == 1 and m:
                src = "pilot/latin-1559-ch1-5.md" if lang == "la" else "pilot/french-1560-ch1-5.md"
                t = br.pilot_chapter(L / src, int(m.group(1)), head)
            else:
                t = joined(L / f"vol{v}" / lang, name)
            if t is None:
                continue
            out = book / "parallel" / lang / f"vol-{v}" / f"{name}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(t.rstrip() + "\n")
            n += 1
print(n, "files")
