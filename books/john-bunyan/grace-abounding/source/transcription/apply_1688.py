# The reading text for the 1688 rebase: the current edition's chapters (its modern spelling, case,
# punctuation and the editor's decisions) with the 1688 wording put back wherever the editor's
# rule of 2026-10-26 says the 1688 wins and the old collation (against GLM OCR) missed it.
# Decided 2026-11-01 from buckets.json (bucket.py): by default the 1688 wins; KEEP lists where the
# edition stays (spelling, the period grammar the rule keeps modern, the reference style, the
# 1666 passages 1688 cut, the rule's "not changed" places, printer's slips); CUSTOM gives the
# reading where neither side fits as it stands.
#   apply_1688.py OUTDIR  -> OUTDIR/*.typ, apply-1688.md (every change)
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from foundation import modern
from wording import ED

W = Path(__file__).parent
KEEP = {
    "A": {1, 3, 10, 12, 15, 20, 21, 22, 23, 36, 43, 48, 54, 57, 65, 72, 77, 78, 79, 85, 86, 87, 89, 90,
          91, 93, 94, 101, 102, 111, 113, 117, 120, 121, 126, 132, 134, 136, 138, 146, 152, 156, 158, 160, 164, 167},
    "B": {0, 1, 3, 6, 9, 14, 15, 16, 19, 20, 23, 30, 31, 33},
    "C": {1, 6, 8, 9, 10, 11, 17, 19, 25, 31, 38, 39, 45, 46, 48, 49, 50, 52, 53, 54, 55, 60, 61, 63, 64, 66, 67, 68, 72, 75, 79, 84, 87, 89, 90, 92, 97, 98, 99},
    "K": set(range(8)),
    "S": {21},                                   # "rent": the old spelling of "rend"
}
CUSTOM = {("A", 7): ("), ever to open", "), even to open"),   # 1688 "even"
          ("A", 12): ("burden upon", "burden on"),
          ("A", 52): ("peace, saith my God, to the wicked", "peace to the wicked, saith my God"),
          ("A", 97): ("blessing’", "blessing also’"),
          ("A", 100): ("He ‘of God is made unto us wisdom, and righteousness, and sanctification, and redemption’",
                       "He ‘is made unto us of God, wisdom, righteousness, sanctification, and redemption’"),
          ("A", 140): ("a gaoler’s", "the gaolers’"),
          ("B", 4): ("there was one, or no", "there was such a one, or no"),
          ("C", 1): ("own heart (", "own hearts ("),
          ("C", 32): ("1600 years", "sixteen hundred years"),
          ("C", 15): ("was a-going to say", "was going to say"),
          ("C", 22): ("was a-going home", "was going home"),
          ("A", 105): ("‘Praise ye the Lord. Praise God in his sanctuary", "‘Praise ye the Lord God in his sanctuary"),
          ("B", 11): ("question all again; which", "question all again; and by times, fell to my old courses again; which"),
          ("B", 13): ("nor depth, nor life", "nor depth, nor death, nor life"),
          ("C", 35): ("born; for those", "born; for, for those"),
          # the edition's Matt 10:37, in no lifetime printing: the whole quotation and its reference
          ("A", 150): (" ‘He that loveth father or mother, son or daughter, more than me, is not worthy "
                       "of me’ (Matt 10:37).", "")}
SPELL = {"rejoyce": "rejoice", "battel": "battle"}
COMPOUND = {"my self": "myself", "thy self": "thyself", "it self": "itself", "him self": "himself",
            "your selves": "yourselves", "our selves": "ourselves", "them selves": "themselves",
            "where ever": "wherever", "what ever": "whatever"}
ALWAYS_CAP = {"I", "God", "Lord", "Christ", "Jesus", "Satan", "Esau", "Peter", "David", "Israel"}


def ed_tokens(text):
    """(start, end) of each word the way wording.ed_words counts them"""
    out = []
    for m in re.finditer(r"(#\w+(?:\([^)]*\))?\[)|([A-Za-z’']+)", text):
        if not m.group(2): continue
        ls = text.rfind("\n", 0, m.start()) + 1
        if text.startswith("=", ls): continue
        out.append((m.start(), m.end()))
    return out


def modern_words(words, capital_first, caps):
    s = " ".join(w.replace("\xad", "") for w in words)
    for a, b in COMPOUND.items():
        s = re.sub(rf"\b{a}\b", b, s, flags=re.I)
    out = []
    for i, w in enumerate(s.split()):
        m = modern(re.sub(r"['’]", "", w.lower())) if not re.search(r"['’]", w) else w.lower()
        m = SPELL.get(m, m)
        if w in ALWAYS_CAP or m.capitalize() in caps or (i == 0 and capital_first):
            m = m[:1].upper() + m[1:]
        out.append(m)
    return " ".join(out)


def main(outdir):
    out = Path(outdir); out.mkdir(parents=True, exist_ok=True)
    b = json.load(open(W / "buckets.json"))
    frozen = json.load(open(W / "buckets-decided.json"))     # the lists KEEP and CUSTOM were decided on
    assert {k: [r["ctx"] for r in v] for k, v in b.items()} == frozen, \
        "buckets.json changed since the decisions: re-decide KEEP/CUSTOM, then refresh buckets-decided.json"
    texts = {f.stem: f.read_text() for f in ED.glob("*.typ")}
    words_all = re.findall(r"(?<=[a-z,;:] )[A-Z][a-z]+", " ".join(texts.values()))
    lower_all = set(re.findall(r"\b[a-z]+\b", " ".join(texts.values())))
    caps = {w for w in set(words_all) if w.lower() not in lower_all}
    edits = {}                                   # file -> [(start, end, new, row)]
    log = []
    for name, rows in b.items():
        for i, r in enumerate(rows):
            if i in KEEP.get(name, ()) and (name, i) not in CUSTOM:
                continue
            f = r["file"]; toks = ed_tokens(texts[f])
            c, d = r["c"], r["d"]
            if c < d:
                st, en = toks[c][0], toks[d - 1][1]
            else:
                st = en = toks[c - 1][1] if c > 0 else 0
            if (name, i) in CUSTOM:
                want, new = CUSTOM[(name, i)]
                k = texts[f].find(want, max(0, st - 300))
                assert 0 <= k < st + 300, ("custom not found", name, i, want)
                st, en, old = k, k + len(want), want
                edits.setdefault(f, []).append((st, en, new, r, old))
                continue
            old = texts[f][st:en]
            first = old.split()[0] if old.split() else ""
            cap = bool(first[:1].isupper()) and first.strip("‘’“”(") not in ALWAYS_CAP
            new = modern_words(r["new"].split(), cap, caps)
            if c == d:                           # an insertion: after the punctuation that ends the word before
                t0 = texts[f]
                while en < len(t0) and t0[en] in ",;:":
                    en += 1
                st = en
                new = " " + new if t0[en:en + 1] == " " or not t0[en:en + 1] else " " + new + " "
                if t0[en:en + 1] == " ":
                    new = " " + new.strip()
            elif not new:                        # a deletion: the space before goes too
                if st > 0 and texts[f][st - 1] == " ": st -= 1
                old = texts[f][st:en]
            else:                                # keep the edition's quotes and stops around the words
                lead = re.match(r"^[‘“(]*", old)[0]; trail = re.search(r"[’”),;:.!?]*$", old)[0]
                new = lead + new + trail
            edits.setdefault(f, []).append((st, en, new, r, old))
    for f, es in edits.items():
        t = texts[f]
        es.sort(key=lambda e: e[0], reverse=True)
        for k in range(1, len(es)):
            assert es[k][1] <= es[k - 1][0], ("overlap", f, es[k][3]["ctx"], es[k - 1][3]["ctx"])
        for st, en, new, r, old in es:
            if not new.strip() and t[st - 1:st] == "‘" and t[en:en + 1] == " ":
                en += 1                          # "‘O my God" -> "‘My God": the quote stays shut on the word
                t = t[:st] + t[en:en + 1].upper() + t[en + 1:]
                log.append(f"- `{f}.typ` …{r['ctx'][:90]}… : “{old.strip()}” → “”")
                continue
            t = t[:st] + new + t[en:]
            if not new and t[st - 1:st] in (":", ";", ",") and t[st:st + 1] in (".", "!", "?"):
                t = t[:st - 1] + t[st:]                  # "circumstances: but, alas! it was all in vain." -> "circumstances."
            log.append(f"- `{f}.typ` …{r['ctx'][:90]}… : “{old.strip()}” → “{new.strip()}”")
        texts[f] = t
    # paragraphs the print sets and the edition ran in: the errors listed in §124 (print §125),
    # and "Secondly" / "Thirdly" in §223
    t = texts["relation"]
    for n in range(1, 9):
        k = t.find(f" {n}. That ", t.find("The errors that this people"))
        assert k > 0, n
        t = t[:k] + f"\n\n{n}\\. That " + t[k + len(f" {n}. That "):]
    for w in ("Secondly, I confessed", "Thirdly, Nor did I find"):
        k = t.find(" " + w); assert k > 0, w
        t = t[:k] + "\n\n" + t[k + 1:]
    texts["relation"] = t
    # CCEL's small capitals on his name in the indictment: not the print's
    texts["call-to-the-ministry"] = texts["call-to-the-ministry"].replace("#smallcaps[John Bunyan]", "John Bunyan")
    texts["preface"] = texts["preface"].replace("#smallcaps[Children]", "Children")   # no opening small capitals
    for f, t in texts.items():
        (out / f"{f}.typ").write_text(t)
    (W / "apply-1688.md").write_text("# The 1688 wording put back into the edition's text\n\n" +
                                     "\n".join(sorted(log)) + "\n")
    print(len(log), "changes")


if __name__ == "__main__":
    main(sys.argv[1])
