"""A book's Classic and Modern English text side by side, paragraph by paragraph, for the editor:
python3 side_by_side.py BOOK_DIR TITLE OUT.html [NOTES.html]"""
import html, re, runpy, sys
from pathlib import Path

# colophon's outline marks (the ebook's: tei_to_html.mark_point), from the books checkout given by
# FGB_COLOPHON (default: the colophon of the checkout holding this script)
import os
sys.path.insert(0, os.environ.get("FGB_COLOPHON", str(Path(__file__).resolve().parents[4] / "colophon")))
from layout import em_level  # noqa: E402
from tei_to_html import POINT_MARKS, mark_point  # noqa: E402

B, TITLE, OUT = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
NOTES = Path(sys.argv[4]).read_text() if len(sys.argv) > 4 else ""
# what every page says about its two columns
ABOUT = ("<p><b>Classic</b>: the author's own words from the printing named in the edition, with spelling and "
         "punctuation brought up to date and the author's grammar kept. <b>Modern English</b>: the whole book in "
         "today's English, nothing abridged, Scripture from the Berean Standard Bible. "
         "In the Modern English, “you<sup>+</sup>” marks a plural “you” (the older “ye”, or the author speaking to "
         "all his readers); a plain “you” is singular or general. Notes appear in grey where they stand in the "
         "text.</p>")


INLINE = {"emph": ("<i>", "</i>"), "strong": ("<b>", "</b>"), "smallcaps": ("<span class='sc'>", "</span>"),
          "super": ("<sup>", "</sup>"), "sub": ("<sub>", "</sub>"),
          "footnote": ("<span class='fn'>Note: ", "</span>")}
CALL = re.compile(r"#([a-z.]+)(\((?:[^()]|\((?:[^()]|\([^()]*\))*\))*\))?(\[)?")


PAD = re.compile(r"\s*#pad\(left: ([\d.]+)em\)")


def typ(t, counts=None):
    """A Typst block as HTML for reading: italics, small capitals, notes inline, layout wrappers
    (#pad, #par, #align, #block, #text …) dropped but their text kept, #v / comments dropped."""
    t = re.sub(r"^//.*$", "", t, flags=re.M)
    t = re.sub(r"#(?:set|show|let|import)\b[^\n]*", "", t)       # settings: not text
    t = re.sub(r"\s*<[a-z-]+>\s*$", "", t, flags=re.M)              # a Typst label (Perkins's <diagram>)
    t = re.sub(r"^(=+) (.*)$", lambda m: "\x00h" + m.group(2) + "\x00/h", t, flags=re.M)
    summary = t.lstrip().startswith("#block(inset:")
    pad = PAD.match(t)
    lvl = em_level(float(pad.group(1))) if pad else 0
    # a paragraph of text (not a heading, list, centred or set-off block, quotation, spacing)
    plain = not t.lstrip().startswith(("=", "+ ", "- ", "#align", "#block", "#quote", "#v(", "#[", "#set",
                                       "#figure", "#image", "#table", "#pagebreak", "#line"))
    out, stack, i = [], [], 0
    while i < len(t):
        c = t[i]
        if c == "#" and t.startswith("#[", i):                     # a bare content block
            stack.append("")
            i += 2
            continue
        if c == "#" and (m := CALL.match(t, i)):
            name, bracket = m.group(1), m.group(3)
            if bracket:
                o, cl = INLINE.get(name, ("", ""))
                if name == "linebreak":
                    o, cl = "<br>", ""
                stack.append(cl)
                out.append(o)
            elif name == "linebreak":
                out.append("<br>")
            i = m.end()
            continue
        if c == "\\" and i + 1 < len(t):
            nxt = t[i + 1]
            out.append("<br>" if nxt in " \n" else html.escape(nxt))
            i += 2
            continue
        if c == "[":
            # a bare [ in markup is text (our gloss: "Pater patriae [the father of the country]"); its ]
            # is text too, not the end of the #footnote or #emph around it (GPT review 2026-11-16)
            out.append("[")
            stack.append("]")
            i += 1
            continue
        if c == "]":
            # a wrapper opened in an earlier blank-line block (an #align around a verse) closes here: drop it
            out.append(stack.pop() if stack else "")
            i += 1
            continue
        out.append(html.escape(c, quote=False))
        i += 1
    h = "".join(out)
    h = h.replace("\x00h", "<b class='h'>").replace("\x00/h", "</b>")
    h = re.sub(r"^\s*[+-] ", "• ", h, flags=re.M)
    h = re.sub(r"\n(?=• )", "<br>", h)
    h = re.sub(r"\s*\n\s*", " ", h).strip()
    if summary:
        return f"<span class='sum'>{h}</span>"
    if counts is not None and plain:
        # OUTLINE_MARKS: the point's mark by its level, as the ebook sets it, and the level shown
        # by a small step in (a review aid; the ebook and print keep every level full width)
        cls, h = mark_point(lvl, h, counts)
        h = h.replace('<span class="smallcaps">', "<span class='sc'>")
        return f"<div class='lv' style='margin-left:{lvl * 0.9:g}em'>{h}</div>" if lvl else h
    return h


def paras(p):
    return [x.strip() for x in re.split(r"\n\s*\n", p.read_text()) if x.strip()]


FRONT = {"preface.typ": "Preface", "to-the-reader.typ": "To the Reader"}
def label(f):
    """A file's name for the contents: "part-2/sign-03.typ" -> "Part II, Sign 3";
    "part-1/02-what-the-affections-are.typ" -> "Part I: What the Affections Are"."""
    parts = Path(f).with_suffix("").parts
    words = lambda t: re.sub(r"^\d+-", "", t).replace("-", " ").title()
    if len(parts) == 2 and (m := re.fullmatch(r"part-(\d+)", parts[0])):
        roman = ["", "I", "II", "III", "IV", "V"][int(m.group(1))]
        if (n := re.fullmatch(r"sign-(\d+)", parts[1])):
            return f"Part {roman}, Sign {int(n.group(1))}"
        return f"Part {roman}: {words(parts[1])}"
    return words(parts[-1])


# front matter, then chapter-NN.typ in order, then any other file (a sermon.typ; a book in
# sub-folders, part-1/... ) in its path's order
found = sorted(str(p.relative_to(B / "chapters/modern")) for p in (B / "chapters/modern").rglob("*.typ"))
order = list(FRONT) + [f"chapter-{k:02d}.typ" for k in range(1, 40)]
files = [f for f in order if f in found] + [f for f in found if f not in order]
ed = B / "source/editorial.py"
marks = ed.exists() and bool(runpy.run_path(str(ed)).get("OUTLINE_MARKS"))
counts = ([0] * len(POINT_MARKS), [0] * len(POINT_MARKS)) if marks else (None, None)
nav, body = [], []
for f in files:
    a, m = paras(B / "chapters/typ" / f), paras(B / "chapters/modern" / f)
    name = FRONT.get(f) or ("Chapter " + str(int(f[8:10])) if re.fullmatch(r"chapter-\d\d\.typ", f)
                            else label(f))
    nav.append(f"<a href='#{f[:-4]}'>{name}</a>")
    rows = "".join(f"<div class='row'><div class='n'>{k}</div><div>{typ(x, counts[0])}</div><div>{typ(y, counts[1])}</div></div>"
                   for k, (x, y) in enumerate(zip(a, m), 1))
    body.append(f"<section id='{f[:-4]}'><h2>{name}</h2>"
                f"<div class='row head'><div></div><div>Classic</div><div>Modern English</div></div>{rows}</section>")
OUT.write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>{TITLE}: Classic and Modern English</title>
<style>
:root {{ --bg:#faf8f3; --fg:#222; --muted:#666; --rule:#e3ddd0; --mark:#7a4b00; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#1b1b1b; --fg:#e8e6e1; --muted:#999; --rule:#333; --mark:#e0b060; }} }}
body {{ background:var(--bg); color:var(--fg); font:16px/1.55 Georgia, serif; margin:0 auto; max-width:1250px; padding:16px; }}
nav {{ position:sticky; top:0; background:var(--bg); padding:6px 0; border-bottom:1px solid var(--rule); font:13px system-ui, sans-serif; }}
nav a {{ margin-right:10px; color:var(--mark); }}
h2 {{ font-weight:normal; margin-top:2em; }}
.row {{ display:grid; grid-template-columns:2.2em 1fr 1fr; gap:22px; padding:10px 0; border-top:1px solid var(--rule); }}
.row.head {{ font:600 12px system-ui, sans-serif; text-transform:uppercase; letter-spacing:.06em; color:var(--muted); }}
.n {{ color:var(--muted); font:12px system-ui, sans-serif; padding-top:4px; }}
.h {{ font-size:1.1em; }} .sum {{ font-style:italic; color:var(--muted); }} .sc {{ font-variant:small-caps; }}
sup {{ color:var(--mark); }} .fn {{ font-size:0.82em; color:var(--muted); }} .fn::before {{ content:''; }}
.notes {{ font-size:15px; max-width:60em; }}
.omark {{ color:var(--muted); }} .lv {{ border-left:2px solid var(--rule); padding-left:.5em; }}
@media (max-width: 800px) {{ .row {{ grid-template-columns:1fr; gap:6px; }} .n {{ display:none; }} }}
</style></head><body>
<h1>{TITLE}: Classic and Modern English</h1>
<div class="notes">{ABOUT}{NOTES}</div>
<nav>{" ".join(nav)}</nav>
{"".join(body)}
</body></html>""")
print("wrote", OUT, len(files), "files")
