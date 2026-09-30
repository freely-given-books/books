"""
Parse the reviewed Typst chapters from the freely-given-books repo into a
flat token stream comparable with the TEI reading text, plus structure
markers:

    "¶"   start of an ordinary paragraph / block
    "+"   start of a numbered-list item (#set enum ... / "+ ")
    "-"   start of a bullet-list item ("- " or nested "  - ")

Headings (lines starting with "=") are pulled out separately per file.
Lines starting with "//" are review comments and are ignored. Typst markup
(#emph[, #footnote[, #super[, #align(..)[, #linebreak(), closing ]) is
stripped; backslash escapes are undone.
"""

import re

# Word characters include combining marks (Hebrew points, the TCP macron),
# so a pointed Hebrew word or "spo̅salibus" stays one token.
MARKS = "̀-֑ͯ-ׇ᷀-᷿⃐-⃿︠-︯"
TOKEN_RE = re.compile(r"[\w'’" + MARKS + r"]+|[^\w\s" + MARKS + r"]", re.S)


def strip_markup(line):
    s = line
    s = re.sub(r"#linebreak\(\)", " ", s)
    s = re.sub(r"#align\([^)]*\)\[", "", s)
    s = re.sub(r"#footnote\[", " ", s)
    s = re.sub(r"#(emph|super|strong|smallcaps)\[", "", s)
    # closing brackets of Typst content blocks (escaped \] stays literal)
    s = re.sub(r"(?<!\\)\]", "", s)
    s = re.sub(r"\\(.)", r"\1", s)
    return s


def parse_typ(text):
    """Return (headings, tokens). tokens is a list of (tok, kind) where
    kind is 'w' (word/punct) or 'm' (structure marker)."""
    headings = []
    toks = []
    blocks = re.split(r"\n\s*\n", text)
    for block in blocks:
        lines = [l for l in block.split("\n")
                 if not l.lstrip().startswith("//") and l.strip()]
        lines = [l for l in lines if not l.lstrip().startswith("#set ")]
        if not lines:
            continue
        cur_marker = None
        for line in lines:
            st = line.lstrip()
            if st.startswith("="):
                headings.append(st.lstrip("=").strip())
                continue
            m = re.match(r"^(\s*)([+-]) (.*)$", line)
            if m:
                toks.append(("+" if m.group(2) == "+" else "-", "m"))
                body = m.group(3)
                cur_marker = "item"
            else:
                if cur_marker is None:
                    toks.append(("¶", "m"))
                    cur_marker = "p"
                body = line
            for t in TOKEN_RE.findall(strip_markup(body)):
                toks.append((t, "w"))
    return headings, toks
