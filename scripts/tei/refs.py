#!/usr/bin/env python3
"""
refs.py: the scripture references in a book, checked against the Bible.

  python3 refs.py BOOK_DIR [--bible kjv|bsb] [--quotes] [--all]

Reads chapters/typ/*.typ and finds every reference ("Romans 11:20, 21",
"Rom. 11.21", "(Psa 55:17)", "1Co 3:22-23", "John xiv. 1-4"), then lists:

  missing   no such chapter or verse (Romans 11:42, Psalm 151)
  quote     (--quotes) the words quoted next to the reference share little
            with the verse(s) it names: perhaps the wrong verse (1 Corinthians
            5:13 for 2 Corinthians 5:13), perhaps a paraphrase; read it

--all prints every reference found, for a count by style (a book should
write its references one way). The Bibles are public domain: the KJV
(github.com/thiagobodruk/bible) and the Berean Standard Bible
(bereanbible.com), fetched once into ~/.cache/fgb-bible. Quotes are compared
with the version the book uses (--bible; KJV by default, BSB for a book that
says so); a book quoting from memory, as the Puritans did, gives many weak
matches: the strongest mismatches are the ones to read.
"""

import argparse
import difflib
import json
import re
import sys
import urllib.request
from pathlib import Path

CACHE = Path.home() / ".cache" / "fgb-bible"
SOURCES = {"kjv": "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_kjv.json",
           "bsb": "https://bereanbible.com/bsb.txt"}

BOOKS = """Genesis Exodus Leviticus Numbers Deuteronomy Joshua Judges Ruth 1_Samuel 2_Samuel
1_Kings 2_Kings 1_Chronicles 2_Chronicles Ezra Nehemiah Esther Job Psalms Proverbs
Ecclesiastes Song_of_Solomon Isaiah Jeremiah Lamentations Ezekiel Daniel Hosea Joel Amos
Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah Malachi Matthew Mark Luke John
Acts Romans 1_Corinthians 2_Corinthians Galatians Ephesians Philippians Colossians
1_Thessalonians 2_Thessalonians 1_Timothy 2_Timothy Titus Philemon Hebrews James 1_Peter
2_Peter 1_John 2_John 3_John Jude Revelation""".split()
BOOKS = [b.replace("_", " ") for b in BOOKS]

# names and abbreviations as books print them -> canonical name
ALIASES = {
    "Genesis": "Gen Gn Ge", "Exodus": "Exo Ex Exod", "Leviticus": "Lev Le",
    "Numbers": "Num Nu Numb", "Deuteronomy": "Deu Deut Dt", "Joshua": "Jos Josh",
    "Judges": "Jdg Judg Jud", "Ruth": "Rut Ru", "1 Samuel": "1Sa 1Sam", "2 Samuel": "2Sa 2Sam",
    "1 Kings": "1Ki 1Kgs 1King", "2 Kings": "2Ki 2Kgs 2King", "1 Chronicles": "1Ch 1Chr 1Chron",
    "2 Chronicles": "2Ch 2Chr 2Chron", "Ezra": "Ezr", "Nehemiah": "Neh", "Esther": "Est Esth Hester",
    "Job": "", "Psalms": "Psa Ps Psal Psalm Pss", "Proverbs": "Pro Prov Pr",
    "Ecclesiastes": "Ecc Eccl Eccles Ecclus", "Song of Solomon": "Song Sol Cant Canticles SS",
    "Isaiah": "Isa Isai Is", "Jeremiah": "Jer Jerem", "Lamentations": "Lam",
    "Ezekiel": "Eze Ezek Ezech", "Daniel": "Dan Da", "Hosea": "Hos Ho", "Joel": "Joe",
    "Amos": "Amo Am", "Obadiah": "Oba Obad", "Jonah": "Jon Jonas", "Micah": "Mic", "Nahum": "Nah",
    "Habakkuk": "Hab Habak", "Zephaniah": "Zep Zeph", "Haggai": "Hag", "Zechariah": "Zec Zech",
    "Malachi": "Mal", "Matthew": "Mat Matt Mt", "Mark": "Mar Mk", "Luke": "Luk Lk Lu",
    "John": "Joh Jn", "Acts": "Act", "Romans": "Rom Ro", "1 Corinthians": "1Co 1Cor",
    "2 Corinthians": "2Co 2Cor", "Galatians": "Gal", "Ephesians": "Eph Ephes",
    "Philippians": "Phi Phil Philip Php", "Colossians": "Col Coloss",
    "1 Thessalonians": "1Th 1Thes 1Thess", "2 Thessalonians": "2Th 2Thes 2Thess",
    "1 Timothy": "1Ti 1Tim", "2 Timothy": "2Ti 2Tim", "Titus": "Tit", "Philemon": "Phm Philem",
    "Hebrews": "Heb", "James": "Jas Jam", "1 Peter": "1Pe 1Pet", "2 Peter": "2Pe 2Pet",
    "1 John": "1Jo 1Jn 1Joh", "2 John": "2Jo 2Jn", "3 John": "3Jo 3Jn", "Jude": "",
    "Revelation": "Rev Revel Apoc",
}
NAMES = {}
for canon in BOOKS:
    forms = {canon, canon.replace(" ", "")} | set(ALIASES.get(canon, "").split())
    if canon == "Song of Solomon":
        forms |= {"Song of Songs", "Song of Sol"}
    if canon == "Psalms":
        forms.add("Psalm")
    if canon == "Revelation":
        forms.add("Revelations")
    for f in list(forms):
        m = re.match(r"([123])\s*(\D.*)", f)
        if m:      # "1Co", "1 Co", "I Cor", "1 Corinthians", "II Tim"
            n, rest = m.groups()
            forms |= {f"{n} {rest}", f"{'I' * int(n)} {rest}", f"{'I' * int(n)}{rest}"}
    for f in forms:
        NAMES[f.lower()] = canon

ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100}


def roman(s):
    s, total = s.lower(), 0
    for i, ch in enumerate(s):
        v = ROMAN[ch]
        total += -v if i + 1 < len(s) and ROMAN[s[i + 1]] > v else v
    return total


def load(version):
    """{book: [[verse text, ...] per chapter]}."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / Path(SOURCES[version]).name
    if not path.exists():
        print(f"fetching the {version.upper()} into {path} ...", file=sys.stderr)
        urllib.request.urlretrieve(SOURCES[version], path)
    if version == "kjv":
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        return {BOOKS[i]: b["chapters"] for i, b in enumerate(data)}
    out = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        m = re.match(r"(.+?) (\d+):(\d+)\t(.*)", line)
        if not m:
            continue
        book, c, v, t = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        book = {"Psalm": "Psalms", "Song of Songs": "Song of Solomon"}.get(book, book)
        chs = out.setdefault(book, [])
        while len(chs) < c:
            chs.append([])
        while len(chs[c - 1]) < v:
            chs[c - 1].append("")
        chs[c - 1][v - 1] = t
    return out


NAME_RE = "|".join(sorted((re.escape(n) for n in NAMES), key=len, reverse=True))
REF_RE = re.compile(
    r"(?<![\w])(?P<book>" + NAME_RE + r")\.?\s+(?P<ch>\d{1,3}|[ivxlc]{1,7})[.:]\s?"
    r"(?P<vs>\d{1,3}(?:\s?[-–]\s?\d{1,3})?(?:\s?,\s?\d{1,3}(?:\s?[-–]\s?\d{1,3})?)*)"
    r"(?:ff)?", re.I)


def verses(vs):
    out = []
    for part in re.split(r"\s?,\s?", vs):
        a, _, b = part.partition("-") if "-" in part else part.partition("–")
        a, b = int(a), int(b) if b else int(a)
        out += list(range(a, max(a, b) + 1))
    return out


def prose(text):
    text = re.sub(r"#(?:emph|strong|smallcaps|super)\[", "", text)
    text = re.sub(r"#footnote\[", " ", text)
    text = re.sub(r"\\(.)", r"\1", text).replace("]", "")
    return re.sub(r"\s+", " ", text)


def quoted_before(text, pos):
    """The quotation closing just before a reference ("…" (Ref) or '…,' Ref):
    from the closing mark back to its opening one. A straight quote opens
    after a space or an opening bracket and before a letter; a straight
    apostrophe inside a word ("God's") is neither."""
    seg = text[max(0, pos - 800):pos].rstrip(" (")
    seg = re.sub(r"[,.;:!?]+$", "", seg).rstrip()
    m = re.search(r"[”’\"']\W*$", seg)
    if not m:
        return None
    close = m.start()
    body = seg[:close]
    k = len(body) - 1
    while k >= 0:
        ch = body[k]
        if ch in "“‘":
            break
        if ch in "\"'" and (k == 0 or body[k - 1] in " (—[") and k + 1 < len(body) and \
                body[k + 1].isalnum():
            break
        k -= 1
    if k < 0 or close - k > 600:
        return None
    return body[k + 1:]


def words(s):
    return [w for w in re.findall(r"[a-z]+", s.lower().replace("’", "'"))]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("book")
    ap.add_argument("--bible", choices=["kjv", "bsb"], default="kjv")
    ap.add_argument("--quotes", action="store_true")
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    bible = load(a.bible)
    files = sorted((Path(a.book) / "chapters" / "typ").rglob("*.typ"))
    n = bad = weak = 0
    styles = {}
    for f in files:
        text = prose(f.read_text(encoding="utf-8"))
        for m in REF_RE.finditer(text):
            name = m.group("book")
            canon = NAMES[name.lower().rstrip(".")]
            ch = m.group("ch")
            c = int(ch) if ch.isdigit() else roman(ch)
            try:
                vs = verses(m.group("vs"))
            except ValueError:
                continue
            n += 1
            styles[name] = styles.get(name, 0) + 1
            ref = m.group(0)
            where = f"{f.relative_to(a.book)}\t{ref}\t…{text[max(0, m.start() - 50):m.start()]}"
            chs = bible.get(canon, [])
            if c < 1 or c > len(chs) or any(v < 1 or v > len(chs[c - 1]) for v in vs):
                bad += 1
                have = f"{canon} has {len(chs)} chapters" if c > len(chs) or c < 1 else \
                    f"{canon} {c} has {len(chs[c - 1])} verses"
                print(f"missing\t{where}\t({have})")
                continue
            if a.all:
                print(f"ok\t{where}")
            if a.quotes:
                q = quoted_before(text, m.start())
                if q and len(words(q)) >= 4:
                    verse = " ".join(chs[c - 1][v - 1] for v in vs)
                    qw, vw = words(q), set(words(verse))
                    share = sum(w in vw for w in qw) / len(qw)
                    if share < 0.5:
                        weak += 1
                        print(f"quote {share:.0%}\t{where}\n\tquoted: {q[:160]}\n"
                              f"\t{a.bible.upper()} {canon} {c}:{m.group('vs')}: {verse[:200]}")
    print(f"{n} references, {bad} missing, {weak} weak quote matches; styles: " +
          ", ".join(f"{k} {v}" for k, v in sorted(styles.items(), key=lambda x: -x[1])[:25]),
          file=sys.stderr)


if __name__ == "__main__":
    main()
