"""Whole-book mechanical checks of a Modern English edition against its Classic (read only), from the 2026-11-16
assessment checks + the review-of-reviews lessons (2026-11-17). python3 lint.py PAIRS.jsonl > lint.txt
Sections: markup counts (footnote, emph, smallcaps, list items); straight quotes; Scripture references per
paragraph (Classic vs Modern: added, dropped, changed); unbalanced brackets/parentheses/quotes; headings (level,
number, archaic word left, identical to an archaic Classic head); paragraph-opening outline marks; length ratio;
archaic forms; you⁺ against the Classic's ye/you-all; ellipsis seams (a quotation cut so the grammar breaks);
notes or Latin changed beyond an added [translation]. Every line is a place to look, not yet an error."""
import json, re, sys, collections
pairs = [json.loads(l) for l in open(sys.argv[1])]
out = collections.defaultdict(list)
REF = re.compile(r"\b(?:[1-3] )?[A-Z][a-z]{1,6}\.? \d+:\d+(?:[–\-, ]+\d+)*")
ARCH = re.compile(r"\b(thou|thee|thy|thine|ye|hath|doth|art|wast|wert|wilt|shalt|canst|dost|didst|hast|hadst|couldst|"
                  r"wouldst|shouldst|’tis|’twas|unto|spake|whither|whence|thither|hither|wherefore|ere|anon|fain|"
                  r"peradventure|withal|betwixt|asunder|nigh|methinks|verily|yea|nay|hereby|thereof|therein|thereby|"
                  r"whereby|whereof|wherein|whilst|amongst|saith|[a-z]{3,}eth)\b", re.I)
OK_ETH = {"teeth", "beneath", "death", "breath", "seventh", "eighth", "twentieth", "thirtieth", "fortieth", "fiftieth",
          "sixtieth", "hundredth", "thousandth", "elizabeth", "nazareth", "japheth", "shibboleth", "sabaoth", "ashtaroth",
          "kenneth", "macbeth", "bethseth", "seth"}
MARK = re.compile(r"\s*(#emph\[)?(First|Secondly|Thirdly|Fourthly|Fifthly|Sixthly|Seventhly|Eighthly|Ninthly|Tenthly|"
                  r"Lastly|\d+\\?\.|\(\d+\.?\)|\\\[\d+\.?\\\]|[IVXL]+\.)")
NOTE = re.compile(r"#footnote\[((?:[^\[\]]|\[[^\[\]]*\])*)\]")
EN = re.compile(r"\b(the|and|of|to|is|that|in|he|it|for|with|as|his|which|this|be|not)\b", re.I)
for r in pairs:
    f, i, a, b = r["file"], r["n"], r["classic"], r["modern"]
    w = f"{f} ¶{i}"
    for tag in ["#footnote[", "#emph[", "#smallcaps[", "#quote", "#stanza"]:
        if tag == "#smallcaps[" and b.count(tag) - b.count("#smallcaps[Lord]") == a.count(tag): continue
        if a.count(tag) != b.count(tag): out["markup"].append(f"{w}: {tag} {a.count(tag)} vs {b.count(tag)}")
    for tag in ("+ ", "- "):
        ca, cb = (len(re.findall(r"^\s*" + re.escape(tag), x, re.M)) for x in (a, b))
        if ca != cb: out["markup"].append(f"{w}: list item {tag!r} {ca} vs {cb}")
    bb = re.sub(r"#(set|text|block|align|v|pad|image)\b[^\n]*", "", b)
    for m in re.finditer(r"[\"']", bb): out["straight quote"].append(f"{w}: …{bb[max(0, m.start() - 30):m.end() + 10]}…")
    ra, rb = REF.findall(a), REF.findall(b)
    if collections.Counter(ra) != collections.Counter(rb):
        out["references"].append(f"{w}: Classic {sorted(set(ra) - set(rb))} / Modern {sorted(set(rb) - set(ra))}")
    for o, c, name in (("(", ")", "parentheses"), ("“", "”", "double quotes")):
        if b.count(o) != b.count(c) and a.count(o) == a.count(c): out["balance"].append(f"{w}: {name} {b.count(o)}/{b.count(c)}")
    if b.count("[") - b.count("\\[") != b.count("]") - b.count("\\]"): out["balance"].append(f"{w}: brackets")
    if a.startswith("="):
        la, lb = re.match(r"=+", a).group(0), (re.match(r"=+", b) or [""])[0] if b.startswith("=") else ""
        if la != lb: out["headings"].append(f"{w}: level {la!r} -> {lb!r}")
        bad = [x for x in ARCH.findall(b) if x.lower() not in OK_ETH]
        if bad: out["headings"].append(f"{w}: archaic {bad}: {b[:120]}")
    ma, mb = MARK.match(a), MARK.match(b)
    if (ma and ma.group(0).strip()) != (mb and mb.group(0).strip()):
        out["outline marks"].append(f"{w}: {ma and ma.group(0).strip()!r} -> {mb and mb.group(0).strip()!r}")
    wa, wb = len(a.split()), len(b.split())
    if wa > 25 and not 0.8 <= wb / wa <= 1.35: out["length ratio"].append(f"{w}: {wa} -> {wb} ({wb / wa:.2f})")
    for m in ARCH.finditer(re.sub(NOTE, "", b)):
        if m.group(0).lower() not in OK_ETH: out["archaic"].append(f"{w}: {m.group(0)} …{b[max(0, m.start() - 40):m.end() + 30]}…")
    if re.search(r"\b(ye|yourselves)\b", a, re.I) and "#super[+]" not in b:
        out["you+ (Classic ye/yourselves, Modern unmarked)"].append(w)
    for m in re.finditer(r"…\s*([a-z]+)", b):
        pre = b[max(0, m.start() - 25):m.start()]
        if re.search(r"\b(the|a|an|of|to|and|his|their|our|your|my)\s*$", pre):
            out["ellipsis seams"].append(f"{w}: …{b[max(0, m.start() - 50):m.end() + 30]}…")
    for m in re.finditer(r"#super\[\+\][;(\[]", b):
        out["swallowed after a mark (escape it: \\;)"].append(f"{w}: …{b[max(0, m.start() - 30):m.end() + 20]}…")
    na, nb = NOTE.findall(a), NOTE.findall(b)
    for x, y in zip(na, nb):
        if len(EN.findall(x)) < 2 and x.strip() != re.sub(r"\s*\[[^\]]*\]", "", y).strip():
            out["notes (non-English) changed"].append(f"{w}: {x[:80]!r} -> {y[:80]!r}")
for k, v in out.items():
    print(f"\n### {k} ({len(v)})"); print("\n".join(v))
print(f"\n{len(pairs)} pairs; " + ", ".join(f"{k} {len(v)}" for k, v in out.items()), file=sys.stderr)
