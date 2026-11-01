# decisions for the places the vote left open (foundation.py): (page:line, Kraken's reading) -> the print's
# reading as tokens, read on the page image (crops/) or plain from the witnesses (see notes)
import json
from pathlib import Path
D = {
 ("11", "Or GRACE"): "OF GRACE",                       # all witnesses but djvu: of
 ("19", "-"): "— “",
 ("19", "A"): "“ A",                                       # image: say—|“A sinner                                    # image: say— “A sinner
 ("22", "I"): "“ I",                                    # three OCRs: opening quote
 ("29", "I BELIEVE"): "“ I BELIEVE",
 ("31", "Friend , do seck it Ar"): "Friend , do seek it AT ONCE .",   # GLM/djvu/Tess; Kraken: "Ar ONCE"
 ("36", "ALL OF GRACE ."): "“",                         # image: running head; “Bear that
 ("45", "I"): "“ I",
 ("47", "THINx"): "THINK",                               # chapter's first word in capitals
 ("50", "WHAT"): "WHAT",
 ("56", "There"): "“ There",
 ("64", "WHY"): "WHY",
 ("65", "."): "",                                       # image: a speck after "absurd."
 ("70", "AFTER"): "AFTER",
 ("72", "W hen ve wvere"): "“ When we were",
 ("72", "« W hen ve wvere"): "“ When we were",
 ("74", "suffici - ently ."): "sufficiently .",         # image: suffici-|ently.”
 ("77", "O"): "“ O",
 ("81", "\" \""): "“",                                  # image: one quote
 ("83", "“ “"): "“",                                    # image: one quote
 ("86", "very"): "very",                                 # chapter heading (structure) + "A very": see heads
 ("96", "CONTINUALLY"): "CONTINUALLY",
 ("97", ". — Acts v . 30"): ". ” — Acts v . 30",          # image: sins.”—Acts v. 30, 31.
 ("99", "Ir"): "IT",
 ("102", "Law"): "“ Law",
 ("106", "BY GRACE ARE YE SAVED ."): "“ BY GRACE ARE YE SAVED .",
 ("111", "“ He"): "“ He",                                 # image: “He came
 ("112", "."): "",                                       # image: no stop after "force"
 ("113", "DARX"): "DARK",
 ("114", "Our"): "“ Our",
 ("120", "saysWho"): "says — Who",
 ("120", "-"): "—",                                        # image: says—|Who: no opening quote                       # image: says—|Who (italic, no opening quote)
 ("121", "and"): "” and",                               # “unstable as water,” and
 ("125", "Bold"): "“ Bold",
 ("126", "THE"): "THE",
 ("126", "God"): "“ God",
 ("131", "Ir"): "” IF",                                    # image: no quote at IF; the mark closes p130's "our Lord?”"
 ("9", "THE"): "THE",
 ("31", "Friend , do seck it Ar ONCE ."): "Friend , do seek it AT ONCE .",   # CCEL lacks the sentence; the OCRs agree
 ("39", "NING ."): "NING .",                               # the heading's second line (assemble.py leaves it out)
 ("99", "NESS . Ir"): "NESS . IT",                          # the same; then the chapter's first word                                    # the book's first word (the rest is title page and plates)
}
KEEP_KRAKEN = ("133",)                                  # the closing paragraph CCEL lost; GLM reads it word for word
# after the vote: words Kraken ran together or broke (every OCR did the same, so the vote
# could not see it) and letters lost in the print; found by wordsweep.py, read on the page
POST = [
 (26, "doneit", "done it"), (30, "Justso", "Just so"), (33, "jusf", "just"),   # p33: a blot after "just"
 (39, "tameit", "tame it"), (41, "xXXVi", "xxxvi"), (48, "Itis", "It is"),
 (50, "understandsit", "understands it"), (72, "Asit", "As it"), (85, "Thisis", "This is"),
 (88, "ventureonit", "venture on it"), (94, "forgetit", "forget it"),
 (110, "isyet spacefor", "is yet space for"), (126, "itis", "it is"),
 (77, "pierce d", "pierced"), (85, "th t", "that"),                             # p85: the a lost in printing
]
votes = json.loads(Path("votes.json").read_text())
out, seen = {}, set()
for r in votes:
    if r["verdict"] != "check": continue
    k = (str(r["page"]), r["kraken"])
    if k in D: out[r["id"]] = D[k]; seen.add(k)
    elif k[0] in KEEP_KRAKEN: out[r["id"]] = r["kraken"]
    else: print("open:", r["id"][:80], "|", r["kraken"][:60])
for k in set(D) - seen: print("unused:", k)
out["__post__"] = POST
Path("decisions.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
