"""Institutes: per-volume review pages (Latin | French | Beveridge | corrected) and the corrected text.

Usage: python3 -I build_review.py VOL OUT_DIR
  VOL      e.g. vol1 (folder under work/institutes/latin/ with la/, fr/, compare/verified-*.json)
  OUT_DIR  where index.html and one page per chapter go
Writes VOL/corrected/<file>.typ: Beveridge's Classic (books worktree) with every accepted,
adjusted or new fix applied in order. Downgraded and rejected fixes are shown but not applied.
Book I ch. 1-5 come from the pilot (pilot/latin-1559-ch1-5.md, french-1560-ch1-5.md,
pilot/fixes-verified.json).
"""
import difflib, html, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
BOOK = pathlib.Path.home() / "Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion"
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "IIII": 4, "V": 5}
# French section -> Latin section(s) where Calvin's French numbers differently (Book I)
FR_MAP = {"book-1-chapter-05": {11: [11, 12], 12: [13], 13: [14], 14: [15]},
          "book-1-chapter-08": {5: [5, 6], **{n: [n + 1] for n in range(6, 13)}}}
APPLY = {"accept", "adjust", "new", None}


def clean(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"\s*\[[A-Z0-9]+-\d+\]", "", t)
    return t


def body(text):
    """Drop the header comment, the Apparatus / Notes sections and trailing notes."""
    text = re.sub(r"<!--(?!\s*col).*?-->", "", text, flags=re.S)
    return re.split(r"\n###? (?:Apparatus|Notes|Unsettled)|\n## Notes on the transcription", text)[0]


def read_parts(folder, name):
    p = folder / f"{name}.md"
    if p.exists():
        return p.read_text()
    parts = sorted(folder.glob(f"{name}.part-*.md"))
    if not parts:
        return None
    out = body(parts[0].read_text())
    for q in parts[1:]:
        b = body(q.read_text()).strip()
        # a word split across the two transcribers: "facul-" + "tas"
        if out.rstrip().endswith("-"):
            out = out.rstrip()[:-1] + b
        else:
            out = out.rstrip() + " " + b
    return out


def sections_md(text):
    """(heading text, {n: text}) of one chapter file (or ("", {0: all}) for a preface)."""
    text = body(text)
    head, secs, cur = "", {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = "head"
            continue
        if line.startswith("#"):
            continue
        m = re.match(r"^(\d+)\.\s+(.*)", line)
        if m:
            cur = int(m.group(1))
            secs[cur] = m.group(2)
        elif cur == "head" and line.strip():
            head += line.strip().strip("*_") + " "
        elif isinstance(cur, int) and line.strip():
            secs[cur] += "\n" + line.strip()
        elif cur in (None, "head") and line.strip() and not secs:
            secs.setdefault(0, "")
            secs[0] += line.strip() + "\n"
    if not any(k for k in secs):        # a preface: no numbered sections
        return head, {0: clean((head + "\n" + secs.get(0, "")).strip())}
    return head, {k: clean(v) for k, v in secs.items()}


def pilot_chapter(path, ch, heading):
    text = path.read_text()
    parts = re.split(rf"^## {heading} ", text, flags=re.M)
    for p in parts[1:]:
        num = p.split()[0].strip(".[]")
        if ROMAN.get(num) == ch:
            return f"## {heading} " + p
    return None


def sections_typ(text):
    m = re.search(r"#align\(center\)\[(.*?)\]\n", text)
    head = m.group(1) if m else ""
    secs, cur = {}, None
    for para in re.split(r"\n\s*\n", text):
        m = re.match(r"^(\d+)\\\.\s*(.*)", para, re.S)
        if m:
            cur = int(m.group(1))
            secs[cur] = m.group(2)
        elif cur is not None and para.strip():
            secs[cur] += "\n\n" + para
    if not secs:
        secs = {0: "\n\n".join(p for p in re.split(r"\n\s*\n", text) if p.strip() and not p.startswith("=="))}
    return head, secs


def typ2txt(s):
    s = re.sub(r"#footnote\[((?:[^\[\]]|\[[^\]]*\])*)\]", r" ⟨note: \1⟩", s)
    s = re.sub(r"#(?:emph|smallcaps|strong)\[([^\]]*)\]", r"\1", s)
    s = re.sub(r"#[a-z]+\([^)]*\)\[([^\]]*)\]", r"\1", s)
    s = re.sub(r"#block\([^)]*\)\[", "", s)
    return s.replace("\\", "")


def worddiff(a, b):
    aw, bw = re.findall(r"\S+|\s+", a), re.findall(r"\S+|\s+", b)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes():
        if op == "equal":
            out.append(html.escape("".join(aw[i1:i2])))
        else:
            if i2 > i1:
                out.append(f"<del>{html.escape(''.join(aw[i1:i2]))}</del>")
            if j2 > j1:
                out.append(f"<ins>{html.escape(''.join(bw[j1:j2]))}</ins>")
    return "".join(out).replace("\n\n", "<br><br>")


def para(s):
    return "".join(f"<p>{html.escape(x)}</p>" for x in s.split("\n") if x.strip())


def fixes_for(vol, name):
    out = []
    files = sorted((HERE / vol / "compare").glob("verified-*.json"))
    if vol == "vol1":
        files = [HERE / "pilot" / "fixes-verified.json"] + files
    key = {"01-prefatory-address": "P1", "04-epistle-1559": "P4"}.get(name)
    ch = int(name.rsplit("-", 1)[1]) if name.startswith("book-") and "chapter" in name else None
    for f in files:
        for x in json.loads(f.read_text()):
            c = str(x.get("chapter"))
            if (key and (c == key or x["id"].startswith(key + "."))) or (ch and c == str(ch)):
                out.append(x)
    return out


def section_of(x):
    s = str(x.get("section", "0")).split(".")[-1]
    s = re.sub(r"\D", "", s)
    return int(s) if s else 0


def build(vol, out):
    out.mkdir(parents=True, exist_ok=True)
    (HERE / vol / "corrected").mkdir(exist_ok=True)
    typdir = BOOK / "chapters/typ" / f"vol-{vol[3:]}"
    pages, totals = [], {"A": 0, "B": 0, "skip": 0, "miss": 0}
    for typ in sorted(typdir.glob("*.typ")):
        name = typ.stem
        src = typ.read_text()
        fixed, notes = src, []
        for x in fixes_for(vol, name):
            v = x.get("verdict")
            if v not in APPLY:
                notes.append((x, f"not applied ({v})"))
                totals["skip"] += 1
                continue
            if x["old"] == x["new"]:
                notes.append((x, "kept as is"))
                continue
            if fixed.count(x["old"]) == 1:
                fixed = fixed.replace(x["old"], x["new"])
                notes.append((x, ""))
                totals[x["severity"]] = totals.get(x["severity"], 0) + 1
            else:
                notes.append((x, "NOT APPLIED: text not found once"))
                totals["miss"] += 1
        (HERE / vol / "corrected" / typ.name).write_text(fixed)
        # Latin and French
        if vol == "vol1" and re.match(r"book-1-chapter-0[1-5]$", name):
            ch = int(name[-1])
            la = pilot_chapter(HERE / "pilot/latin-1559-ch1-5.md", ch, "Caput")
            fr = pilot_chapter(HERE / "pilot/french-1560-ch1-5.md", ch, "Chapitre")
        else:
            la, fr = read_parts(HERE / vol / "la", name), read_parts(HERE / vol / "fr", name)
        lh, ls = sections_md(la) if la else ("", {})
        fh, fs = sections_md(fr) if fr else ("", {})
        bh, bs = sections_typ(src)
        ch_, cs = sections_typ(fixed)
        frmap = {}
        for fn in fs:
            for ln in FR_MAP.get(name, {}).get(fn, [fn]):
                frmap.setdefault(ln, []).append(fn)
        rows, shown = [], set()
        keys = sorted(set(ls) | set(bs)) or [0]
        if len(keys) > 1 and 0 in keys and not bs.get(0) and not ls.get(0, "").strip():
            keys.remove(0)
        for n in keys:
            frs = [x for x in frmap.get(n, []) if x not in shown]
            shown.update(frs)
            frtxt = "".join(f"<p><b>{x}.</b> {html.escape(clean(fs[x]))}</p>" if x else para(clean(fs[x])) for x in frs) \
                or ('<p class="dim">(not in the 1560 French)</p>' if not fs else '<p class="dim">(see the French above)</p>')
            bt, ct = typ2txt(bs.get(n, "")), typ2txt(cs.get(n, ""))
            items = [(x, why) for x, why in notes if (section_of(x) == n) or (n == keys[0] and section_of(x) not in keys)]
            ih = "".join(
                f'<li class="sev{x["severity"]}{" off" if why else ""}"><b>{html.escape(x["id"])}</b> '
                f'<span class="tag">{x["severity"]} · {html.escape(x["kind"])}{" · " + html.escape(why) if why else ""}</span> '
                f'{html.escape(x.get("why", ""))}'
                + (f' <i>Second reader ({html.escape(str(x.get("verdict")))}): {html.escape(x.get("note", ""))}</i>' if x.get("note") else "")
                + "</li>" for x, why in items)
            label = f"§{n}" if n else ""
            rows.append(
                (f'<div class="secno">{label}</div>' if label else "")
                + '<div class="row">'
                f'<div class="la"><h4>Latin 1559</h4>{para(ls.get(n, "")) or "<p class=dim>(no Latin)</p>"}</div>'
                f'<div class="fr"><h4>{"French 1560" if vol in ("vol1", "vol2") else "French 1560 (1859 Paris ed.)"}</h4>{frtxt}</div>'
                f'<div class="bev"><h4>Beveridge 1845</h4><p>{html.escape(bt).replace(chr(10) * 2, "<br><br>")}</p></div>'
                f'<div class="cor"><h4>Corrected</h4><p>{worddiff(bt, ct)}</p></div></div>'
                + (f'<ul class="items">{ih}</ul>' if items else ""))
        title = src.splitlines()[0].lstrip("= ").strip()
        nA = sum(1 for x, w in notes if not w and x["severity"] == "A")
        nB = sum(1 for x, w in notes if not w and x["severity"] == "B")
        head = (f'<div class="row head"><div class="la"><i>{html.escape(clean(lh))}</i></div>'
                f'<div class="fr"><i>{html.escape(clean(fh))}</i></div>'
                f'<div class="bev">{html.escape(bh)}</div><div class="cor">{worddiff(bh, ch_)}</div></div>') if (lh or bh) else ""
        page = TEMPLATE.replace("%TITLE%", html.escape(title)).replace(
            "%BODY%", f'<p class="nav"><a href="index.html">← Volume {vol[3:]}</a></p><h2>{html.escape(title)}</h2>'
            f'<p class="sum">{nA} A and {nB} B fixes applied.</p>' + head + "\n".join(rows))
        (out / f"{name}.html").write_text(page)
        pages.append((name, title, nA, nB, sum(1 for _, w in notes if w)))
    idx = "".join(f'<tr><td><a href="{n}.html">{html.escape(t)}</a></td><td>{a}</td><td>{b}</td><td>{s or ""}</td></tr>'
                  for n, t, a, b, s in pages)
    page = TEMPLATE.replace("%TITLE%", f"Volume {vol[3:]}").replace(
        "%BODY%", f"<h2>Institutes, volume {vol[3:]}: Beveridge checked against Calvin's Latin</h2>{INTRO}{INTRO_1859 if vol not in ("vol1", "vol2") else ""}"
        f'<table class="idx"><tr><th>Part</th><th>A</th><th>B</th><th>shown, not applied</th></tr>{idx}</table>'
        f'<p class="sum">Total: {totals["A"]} A and {totals["B"]} B fixes applied; {totals["skip"]} downgraded or rejected by the second reader; '
        f'{totals["miss"]} could not be placed.</p>')
    (out / "index.html").write_text(page)
    print(out, totals)


INTRO = """<p>Each page shows, section by section: Calvin's 1559 Latin (Baum–Cunitz–Reuss 1869), Calvin's own
French of 1560, Beveridge 1845 as in our Classic (now checked against the 1845 print), and the corrected Beveridge
(green added, red removed). Under each section are the findings: <b>A</b> = Calvin's meaning changed or lost,
<b>B</b> = a smaller loss or tilt. Each was proposed by one reader and judged by a second; harmless paraphrase (C) is left
alone. The corrected text is the base for the Modern English edition.</p>"""

INTRO_1859 = """<p>From Book III the French comes from the Paris edition of 1859 (Meyrueis), because the critical text
(Calvini Opera vol. 4) can't be had. That edition is the 1560 French with modern accents, and its editor silently corrected
the Scripture references, so the Latin alone decides a reference. The corrected Beveridge gives Calvin's own reference,
even where a later editor changed it. The one exception is a plain slip, where the words Calvin quotes prove which verse
he meant.</p>"""

TEMPLATE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>%TITLE%</title>
<style>
:root{--bg:#fbfaf7;--fg:#222;--dim:#777;--line:#ddd;--ins:#d8f0d8;--del:#f6d6d6;--a:#b3261e;--b:#a36a00}
@media (prefers-color-scheme:dark){:root{--bg:#1b1b1b;--fg:#e6e6e6;--dim:#999;--line:#333;--ins:#1f4a25;--del:#5a2323;--a:#ff8a80;--b:#ffcc66}}
body{background:var(--bg);color:var(--fg);font:15px/1.5 Georgia,serif;margin:0 auto;padding:16px;max-width:1700px}
a{color:inherit}.nav{font:13px system-ui}.sum{font:14px system-ui}
.row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;border-top:1px solid var(--line);padding:8px 0}
.row.head{font-size:.9em}
h4{margin:0 0 4px;font:600 11px system-ui;text-transform:uppercase;color:var(--dim)}
.secno{font:700 13px system-ui;margin-top:14px}
.la{font-size:.93em}.fr{font-size:.9em;color:var(--dim)}
.la p,.fr p,.bev p,.cor p{margin:0 0 .5em}
ins{background:var(--ins);text-decoration:none}del{background:var(--del)}
.items{font:13px/1.45 system-ui;margin:4px 0 10px}.items li{margin:3px 0}.items li.off{opacity:.6}
.tag{font-weight:600}.sevA .tag{color:var(--a)}.sevB .tag{color:var(--b)}.dim{color:var(--dim)}
table.idx{border-collapse:collapse;font:14px system-ui}table.idx td,table.idx th{padding:4px 10px;border-bottom:1px solid var(--line);text-align:left}
@media (max-width:900px){.row{grid-template-columns:1fr}}
</style></head><body>
%BODY%
</body></html>"""

if __name__ == "__main__":
    build(sys.argv[1], pathlib.Path(sys.argv[2]))
