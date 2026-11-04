#!/usr/bin/env python3
"""
The 1689 Baptist Confession of Faith, with the Baptist Catechism (1695) and
An Orthodox Catechism (1680), as one ThML file: lbcf1689.thml.xml.

The text is SVRBC's symbolics-data (gitlab.com/svrbc/symbolics-data, the
symbolics-data/ submodule beside this folder), exactly as it stands at the
pinned commit, which the ThML header records. Two pieces it does not have
are our own transcriptions, in transcription/: the confession's preface and
its closing statement with the signatories.

colophon reads the ThML as it reads a CCEL text (sources.load ->
thml_to_tei), so the confession goes through the same pipeline as every
other book. This script only lays the data out; it changes no words.

  div1 per part, in the printed order:
    lbcf-preface            the confession's preface
    lbcf-01 ... lbcf-32     its chapters: each paragraph a speech whose
                            speaker is "Paragraph N:"; each segment of the
                            paragraph followed by its proofs as a note
    lbcf-closing            the closing statement and the signatories
    bc1695                  the Baptist Catechism: "Question N:" and
                            "Answer:" speeches, the answer's proofs as notes
    aoc-preface             An Orthodox Catechism's preface (prose/preface.md)
    aoc-01 ... aoc-17       its sections, questions as in bc1695

Small capitals (span.sc) mark the speakers, as CCEL marks dialogue.

  python3 make_thml.py          # from this folder; rewrites lbcf1689.thml.xml
"""

import re
import subprocess
from pathlib import Path
from xml.sax.saxutils import escape

import yaml

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "symbolics-data"
OWN = HERE / "transcription"
OUT = HERE / "lbcf1689.thml.xml"

LBCF = DATA / "confessions" / "lbcf1689"
BC = DATA / "catechisms" / "bc1695"
AOC = DATA / "catechisms" / "aoc1680"


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def text(s):
    """Data text as ThML: XML-escaped, its folded whitespace one space."""
    return escape(" ".join(str(s).split()))


def md_inline(s):
    """A Markdown line's *italics* as <i>."""
    return re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text(s))


def markdown(path):
    """A prose file (front matter, then paragraphs): (title, [paragraph
    ThML]). A block whose lines end in two spaces (the signatories) is a
    paragraph per line."""
    raw = path.read_text(encoding="utf-8")
    title = None
    m = re.match(r"---\n(.*?)\n---\n", raw, re.S)
    if m:
        title = yaml.safe_load(m.group(1)).get("title")
        raw = raw[m.end():]
    paras = []
    for block in re.split(r"\n\s*\n", raw.strip()):
        lines = block.split("\n")
        if any(line.endswith("  ") for line in lines):
            paras += [md_inline(line) for line in lines]
        else:
            paras.append(" ".join(md_inline(line) for line in lines))
    return title, paras


def segments(segs):
    """A paragraph's or answer's segments: each one's text, then its proofs
    as a note."""
    out = []
    for s in segs:
        t = text(s["text"])
        proofs = (s.get("proofs") or "").strip()
        out.append(t + (f"<note>{text(proofs)}</note>" if proofs else ""))
    return " ".join(out)


def speech(speaker, body):
    return f'<p><span class="sc">{escape(speaker)}:</span> {body}</p>'


def div(id_, title, paras, head=True):
    h = f"<h2>{escape(title)}</h2>\n" if head and title else ""
    return (f'<div1 id="{id_}" title="{escape(title)}">\n{h}'
            + "\n".join(paras) + "\n</div1>")


def question(q):
    return [speech(f"Question {q['id']}", text(q["question"])),
            speech("Answer", segments(q["segments"]))]


def numbered(folder, width):
    return sorted(folder.glob("[0-9]" * width + ".yml"))


def body():
    parts = []
    title, paras = markdown(OWN / "lbcf-preface.md")
    parts.append(div("lbcf-preface", title, [f"<p>{p}</p>" for p in paras]))
    for ch_file in numbered(LBCF / "chapters", 2):
        ch = load(ch_file)
        n = int(ch["id"])
        paras = []
        for k in range(1, ch["num_paragraphs"] + 1):
            para = load(LBCF / "paragraphs" / f"{n:02}_{k:02}.yml")
            paras.append(speech(f"Paragraph {para['paragraph']}", segments(para["segments"])))
        parts.append(div(f"lbcf-{n:02}", f"{n}. {ch['title']}", paras))
    title, paras = markdown(OWN / "lbcf-closing.md")
    parts.append(div("lbcf-closing", title, [f"<p>{p}</p>" for p in paras]))

    qs = [p for f in numbered(BC / "questions", 3) for p in question(load(f))]
    parts.append(div("bc1695", "The Baptist Catechism", qs))

    title, paras = markdown(AOC / "prose" / "preface.md")
    parts.append(div("aoc-preface", title, [f"<p>{p}</p>" for p in paras]))
    by_section = {}
    for f in numbered(AOC / "questions", 3):
        q = load(f)
        by_section.setdefault(int(q["parent"]), []).append(q)
    for s_file in numbered(AOC / "sections", 2):
        sec = load(s_file)
        n = int(sec["id"])
        qs = [p for q in by_section.get(n, []) for p in question(q)]
        parts.append(div(f"aoc-{n:02}", f"{n}. {sec['title']}", qs))
    return "\n\n".join(parts)


def head():
    commit = subprocess.run(["git", "-C", str(DATA), "rev-parse", "HEAD"],
                            capture_output=True, text=True, check=True).stdout.strip()
    return f"""<ThML.head>
<generalInfo>
<description>The Second London Baptist Confession of Faith (1677, owned by the
general assembly in 1689), with the Baptist Catechism (1695) and An Orthodox
Catechism (1680).</description>
<pubHistory>Laid out by make_thml.py from SVRBC's symbolics-data.</pubHistory>
<comments>The confession, the catechisms and An Orthodox Catechism's preface
are symbolics-data (gitlab.com/svrbc/symbolics-data) at commit {commit}:
confessions/lbcf1689, catechisms/bc1695, catechisms/aoc1680 (questions,
sections, prose/preface.md), unchanged. The confession's preface, closing
statement and signatories are our own transcription
(transcription/lbcf-preface.md, lbcf-closing.md). Each Scripture proof is a
note after the words it proves.</comments>
</generalInfo>
<printSourceInfo><published>symbolics-data, Silicon Valley Reformed Baptist
Church (SVRBC), commit {commit}</published></printSourceInfo>
<electronicEdInfo>
<publisherID>commonweal</publisherID>
<bookID>lbcf1689</bookID>
<DC>
<DC.Title>The 1689 Baptist Confession of Faith, with Catechisms</DC.Title>
<DC.Creator sub="Author">Particular Baptist Churches</DC.Creator>
<DC.Publisher>symbolics-data (SVRBC)</DC.Publisher>
<DC.Language>en</DC.Language>
<DC.Rights>Public domain.</DC.Rights>
</DC>
</electronicEdInfo>
</ThML.head>"""


def main():
    xml = (f'<?xml version="1.0" encoding="UTF-8"?>\n<ThML>\n{head()}\n'
           f"<ThML.body>\n{body()}\n</ThML.body>\n</ThML>\n")
    OUT.write_text(xml, encoding="utf-8")
    print(f"wrote {OUT.name}")


if __name__ == "__main__":
    main()
