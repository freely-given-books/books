# All of Grace: the reg layer's modernizations, applied to chapters/typ freshly extracted from
# the TEI (then ./fgb sync records each as a reg decision; the orig layer keeps the 1886 print).
#   modernize.py BOOK_DIR
# 1. headings in title case (the edition's style)
# 2. American spelling (the editor, 2026-11-01), the pairs the edition used before (CCEL's
#    American text, ready 2026-10-30) where the 1886 print spells the British way
# 3. the 1886 printer's misprints, read on the page images
# 4. dashes spaced, the edition's style (editorial.py DASH = " — "), where the print closes them up
# Scripture references are restyled after this by colophon's refstyle.py.
import re, sys
from pathlib import Path

HEADINGS = ["To You!", "What Are We At?", "God Justifieth The Ungodly", "“It Is God That Justifieth”",
            "Just And The Justifier", "Concerning Deliverance From Sinning", "By Grace Through Faith",
            "Faith, What Is It?", "How May Faith Be Illustrated?", "Why Are We Saved By Faith?",
            "Alas! I Can Do Nothing!", "The Increase Of Faith", "Regeneration And The Holy Spirit",
            "“My Redeemer Liveth”", "Repentance Must Go With Forgiveness", "How Repentance Is Given",
            "The Fear Of Final Falling", "Confirmation", "Why Saints Persevere", "Close"]

# British -> American, whole words, any case (Saviour's, Saviourship follow)
SPELLING = {
    "saviour": "savior", "saviours": "saviors", "saviourship": "saviorship",
    "honour": "honor", "honours": "honors", "honoured": "honored", "honourable": "honorable",
    "favour": "favor", "favours": "favors", "favoured": "favored", "favourable": "favorable",
    "labour": "labor", "labours": "labors", "laboured": "labored", "labouring": "laboring",
    "colour": "color", "coloured": "colored", "neighbour": "neighbor", "neighbours": "neighbors",
    "behaviour": "behavior", "rumour": "rumor", "vigour": "vigor", "ardour": "ardor",
    "offence": "offense", "offences": "offenses", "defence": "defense", "pretence": "pretense",
    "marvellous": "marvelous", "marvellously": "marvelously", "marvelled": "marveled",
    "labelled": "labeled", "travelled": "traveled", "traveller": "traveler", "travellers": "travelers",
    "travelling": "traveling", "parcelled": "parceled", "counsellor": "counselor",
    "counsellors": "counselors", "jewelled": "jeweled", "quarrelled": "quarreled",
    "fulfil": "fulfill", "fulfils": "fulfills", "fulfilment": "fulfillment", "fulness": "fullness",
    "sceptre": "scepter", "sepulchre": "sepulcher", "centre": "center", "theatre": "theater",
    "almanack": "almanac", "axe": "ax", "towards": "toward", "upwards": "upward",
    "afterwards": "afterward", "downwards": "downward", "cheque": "check", "grey": "gray",
}

# the printer's misprints (orig keeps them as printed); each read on the page image
MISPRINTS = {"sarpe": "spare", "godness": "goodness", "scarely": "scarcely",
             "trangression": "transgression", "Spirt": "Spirit", "checque": "check"}


# the printer's slips that are real words, so only in their context (orig keeps them)
PHRASES = {"their evils ways": "their evil ways", "when be yielded": "when he yielded",
           "better that merely": "better than merely"}


def respell(text):
    for a, b in PHRASES.items():
        text = text.replace(a, b)
    def one(m):
        w = m.group(0)
        if w in MISPRINTS: return MISPRINTS[w]
        new = SPELLING.get(w.lower())
        if new is None: return w
        if w.isupper(): return new.upper()
        if w[0].isupper(): return new[0].upper() + new[1:]
        return new
    return re.sub(r"(?<![\w#])[A-Za-z]+(?![\w(\[])", one, text)


def space_dashes(text):
    """word—word -> word — word; not at a line's start or end, nor before closing punctuation"""
    return re.sub(r"(?<=[^\s\n—])—(?=[^\s\n—.,;:!?”’)\]])", " — ", text)


def main(book):
    files = sorted((Path(book) / "chapters/typ").glob("chapter-*.typ"))
    n = 0
    for f, head in zip(files, HEADINGS):
        first, rest = f.read_text().split("\n", 1)
        new = space_dashes(respell(rest))
        n += sum(a != b for a, b in zip(re.findall(r"\w+", rest), re.findall(r"\w+", new)))
        f.write_text(f"== {head}\n" + new)
    print(f"{len(files)} headings, {n} words respelled or corrected")


if __name__ == "__main__":
    main(sys.argv[1])
