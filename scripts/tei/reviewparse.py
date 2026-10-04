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


# ---------------------------------------------------------------------------
# Markup-aware parser: keeps footnotes apart from the body, and records which
# words are italic, so notes can be matched and moved and emphasis compared.
# ---------------------------------------------------------------------------

class Review:
    """A reviewed chapter.

    body       [(text, kind, italic)]  kind 'w' word/punct, 'm' block marker
               ('¶' paragraph, '+'/'-' list item, '>' block quotation)
    notes      [{"anchor": i, "toks": [(text, italic)]}]  i = len(body) at
               the point the #footnote[ stood
    headings   heading texts ('=' lines, or the long title of #chapter[..][..])
    short      short titles from #chapter[long][short], else None
    """

    def __init__(self):
        self.body, self.notes, self.headings, self.short = [], [], [], []
        self.body_sp = []        # parallel to body: whitespace before the token?
        self._last = " "         # last character seen in the body text


def _bracket_arg(s, i):
    """s[i] == '['; return (content, index after the matching ']')."""
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced [ in: " + s[i:i + 60])


def _scan(s, out_body, notes, italic=False, in_note=None, buf=None, sp_state=None):
    """Walk inline Typst markup, appending words to out_body (or the current
    note's toks). Handles \\escapes, _italic_, #emph[ #strong[ #super[
    #smallcaps[ #align(..)[ #quote[ #footnote[ and #linebreak(). Emphasis
    does not split a word (#emph[Simon]'s is one word): characters are
    collected with their italic flag and tokenized together. A token's
    italic flag is True/False, or a string mask ("111100") when mixed."""
    top = buf is None
    if top:
        buf = []                            # [(char, italic)]
    if sp_state is None:
        sp_state = {"last": " ", "sp": []}

    def flush():
        text = "".join(c for c, _ in buf)
        flags = [f for _, f in buf]
        buf.clear()
        # whitespace before each token (review.body_sp / note["sp"])
        holder = in_note if in_note is not None else sp_state
        for m in TOKEN_RE.finditer(text):
            fl = flags[m.start():m.end()]
            it = all(fl) if (all(fl) or not any(fl)) else "".join("1" if x else "0" for x in fl)
            prev = text[m.start() - 1] if m.start() else holder["last"]
            sp = prev.isspace()
            if in_note is not None:
                in_note["toks"].append((m.group(0), it))
                in_note["sp"].append(sp)
            else:
                out_body.append((m.group(0), "w", it))
                sp_state["sp"].append((len(out_body) - 1, sp))
        if text:
            holder["last"] = text[-1]

    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            nxt = s[i + 1:i + 2]
            buf.append((" " if nxt in ("", "\n", " ") else nxt, italic))
            i += 2
            continue
        if c == "_":
            italic = not italic
            i += 1
            continue
        if c == "#":
            m = re.match(r"#linebreak\(\)", s[i:])
            if m:
                buf.append((" ", italic))
                i += m.end()
                continue
            m = re.match(r"#(emph|strong|super|smallcaps|quote|footnote)\[", s[i:]) or \
                re.match(r"#(align)\([^)]*\)\[", s[i:])
            if m:
                inner, j = _bracket_arg(s, i + m.end() - 1)
                name = m.group(1)
                if name == "footnote":
                    flush()
                    note = {"anchor": len(out_body), "toks": [], "sp": [], "last": " "}
                    notes.append(note)
                    _scan(inner, out_body, notes, False, note, None, sp_state)
                elif name == "align":
                    flush()
                    _scan(inner, out_body, notes, italic, in_note, None, sp_state)
                    buf.append((" ", italic))
                else:
                    _scan(inner, out_body, notes, italic or name == "emph", in_note, buf,
                          sp_state)
                i = j
                continue
            # any other call with content, e.g. #par(first-line-indent: 0em)[..]
            # or a book macro #epigraph[..][..]: its content is text
            m = re.match(r"#[A-Za-z][\w-]*(\((?:[^()]|\([^()]*\))*\))?(?=\[)", s[i:])
            if m:
                j = i + m.end()
                first = True
                while s[j:j + 1] == "[":
                    inner, j = _bracket_arg(s, j)
                    if not first:
                        buf.append((" ", italic))
                    _scan(inner, out_body, notes, italic, in_note, buf, sp_state)
                    first = False
                i = j
                continue
            # a call without content (#v(1em), #pagebreak()) is layout
            m = re.match(r"#[A-Za-z][\w.-]*\((?:[^()]|\([^()]*\))*\)", s[i:])
            if m:
                buf.append((" ", italic))
                i += m.end()
                continue
        buf.append((c, italic))
        i += 1
    if top:
        flush()
    return italic


def _scan_block(r, text, italic=False):
    st = {"last": " ", "sp": []}
    _scan(text, r.body, r.notes, italic, None, None, st)
    for i, sp in st["sp"]:
        r.body_sp_map[i] = sp


def join_brackets(text):
    """Blank lines inside an open [ ... ] (a multi-line call such as an
    epigraph block) do not end the block: turn them into single newlines."""
    out, depth, i = [], 0, 0
    while i < len(text):
        c = text[i]
        if c == "\\":
            out.append(text[i:i + 2])
            i += 2
            continue
        if c == "[":
            depth += 1
        elif c == "]":
            depth = max(0, depth - 1)
        if depth and text.startswith("\n\n", i):
            out.append("\n")
            i += 2
            while i < len(text) and text[i] == "\n":
                i += 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


ENUM_RE = re.compile(r"^\s*#set enum\((.*)\)\s*$")


def unwrap_lists(text):
    """A "#[" line opens a scope that its own "]" line closes (the review's
    way of numbering one list differently: #[ #set enum(numbering: "a)",
    start: 2) + ... ]). The two lines are layout and become "//@scope" and
    "//@scope-end" lines for parse_review, and a #set enum inside such a
    scope a "//@enum numbering|start" line."""
    out, opens, depth = [], [], 0
    for line in text.split("\n"):
        st = line.strip()
        if st == "#[":
            opens.append(depth)
            depth += 1
            out += ["", "//@scope"]
            continue
        if st == "]" and opens and depth - 1 == opens[-1]:
            opens.pop()
            depth -= 1
            out.append("//@scope-end")
            continue
        m = ENUM_RE.match(line)
        if m and opens:
            args = dict(re.findall(r'(\w+):\s*("[^"]*"|\d+)', m.group(1)))
            out.append("//@enum " + args.get("numbering", "").strip('"') + "|" +
                       args.get("start", ""))
            continue
        depth += len(re.findall(r"(?<!\\)\[", line)) - len(re.findall(r"(?<!\\)\]", line))
        out.append(line)
    return "\n".join(out)


def parse_review(text, inline_headings=False, titled=True, edition_heads=False):
    """inline_headings (a book with a LAYOUT): heading lines are text of the
    file, marked "H", except the first when the file has a title of the
    edition's own (titled), which goes to headings.

    r.list_info: body index of a "+" marker -> {"depth", "numbering",
    "start"}, and of a "¶" marker of a paragraph indented under a list item
    (Typst sets it inside the item) -> {"depth"}: how many items enclose it,
    and the numbering a #[ #set enum(...) ] scope gives its list."""
    r = Review()
    r.titled = titled
    r.list_info = {}
    r.epigraphs = []           # body indices of blocks set as an epigraph
    # edition_heads (EDITION_HEADINGS): headings below the file title are
    # the edition's own, not printed text: (body index they stand before,
    # level, text), kept out of the body
    r.edition_heads = []
    text = unwrap_lists(text)
    if inline_headings:
        text = join_brackets(text)
    scopes = []                # #[ ] scopes: [numbering, start pending, items open]
    items = []                 # columns of the list items open at this point

    def enclosing(col):
        while items and items[-1] >= col:
            items.pop()
        return len(items)

    def item_mark(col, kind="+"):
        depth = enclosing(col)
        items.append(col)
        info = {"kind": kind, "depth": depth, "numbering": None, "start": None}
        if scopes:              # set rules reach into inner scopes
            info["numbering"] = next((sc[0] for sc in reversed(scopes) if sc[0]), None)
            info["start"], scopes[-1][1] = scopes[-1][1], None
        r.list_info[len(r.body)] = info
    r.body_sp_map = {}
    ends = 0                   # scopes closed by the block before
    for block in re.split(r"\n\s*\n", text):
        for _ in range(ends):      # items opened inside a scope end with it
            del items[scopes.pop()[2]:]
        ends = 0
        for l in block.split("\n"):
            if l.startswith("//@scope-end"):
                ends += 1
            elif l.startswith("//@scope"):
                scopes.append([None, None, len(items)])
            elif l.startswith("//@enum ") and scopes:
                num, start = l[len("//@enum "):].split("|")
                scopes[-1][:2] = [num or None, int(start) if start else None]
        lines = [l for l in block.split("\n")
                 if l.strip() and not l.lstrip().startswith(("//", "#set ", "#import "))]
        if not lines:
            continue
        indent = len(lines[0]) - len(lines[0].lstrip())
        joined = "\n".join(lines)
        st = joined.lstrip()
        if st.startswith("#chapter["):
            long_, j = _bracket_arg(st, len("#chapter"))
            short = None
            if st[j:j + 1] == "[":
                short, j = _bracket_arg(st, j)
            r.headings.append(" ".join(long_.split()))
            r.short.append(" ".join(short.split()) if short is not None else None)
            continue
        if st.startswith(("#quote[", "#quote()[")):
            enclosing(indent)
            inner, _ = _bracket_arg(st, len("#quote()") if st.startswith("#quote()[")
                                    else len("#quote"))
            r.body.append((">", "m", False))
            _scan_block(r, inner)
            continue
        if not any(l.lstrip().startswith("=") or re.match(r"^\s*[+-] ", l) for l in lines):
            # an ordinary paragraph: scan it whole, since a #footnote[...]
            # may run over several lines
            depth = enclosing(indent)
            if depth:
                r.list_info[len(r.body)] = {"kind": "¶", "depth": depth}
            if st.startswith("#align(center)[") and "#text(size: 0.9em, weight: 600)[" in st:
                r.epigraphs.append(len(r.body))     # a scripture epigraph
            r.body.append(("¶", "m", False))
            n = len(r.body)
            _scan_block(r, joined + "\n")
            if inline_headings and len(r.body) == n:
                r.body.pop()             # a layout-only block, e.g. #v(1em)
                r.list_info.pop(n - 1, None)
            continue
        cur = None
        for line in lines:
            s = line.lstrip()
            if s.startswith("="):
                items.clear()
                if edition_heads and (r.headings or not r.titled):
                    level = len(s) - len(s.lstrip("="))
                    r.edition_heads.append((len(r.body), level, s.lstrip("=").strip()))
                    cur = None
                    continue
                if inline_headings and (r.headings or not r.titled):
                    r.body.append(("H", "m", False))
                    _scan_block(r, s.lstrip("=").strip() + "\n")
                    cur = None
                    continue
                r.headings.append(s.lstrip("=").strip())
                r.short.append(None)
                continue
            m = re.match(r"^(\s*)([+-]) (.*)$", line)
            if m:
                item_mark(len(m.group(1)), m.group(2))
                r.body.append(("+" if m.group(2) == "+" else "-", "m", False))
                body, cur = m.group(3), "item"
            else:
                if cur is None:
                    depth = enclosing(len(line) - len(line.lstrip()))
                    if depth:
                        r.list_info[len(r.body)] = {"kind": "¶", "depth": depth}
                    r.body.append(("¶", "m", False))
                    cur = "p"
                body = line
            _scan_block(r, body + "\n")
    r.body_sp = [r.body_sp_map.get(i, False) for i in range(len(r.body))]
    return r


def flatten(review):
    """The old flat stream: note words inline at their anchors."""
    out, k = [], 0
    notes = sorted(review.notes, key=lambda n: n["anchor"])
    for i, e in enumerate(review.body + [None]):
        while k < len(notes) and notes[k]["anchor"] == i:
            out += [(t, "w") for t, _ in notes[k]["toks"]]
            k += 1
        if e is not None:
            out.append((e[0], e[1]))
    return out
