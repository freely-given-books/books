"""Look up the BSB: python3 bsb.py "Rom 8:13" "Gal 5:17-18" "Ps 123:2" -> each verse's text.
Book names as the editions write them (John, 1 Cor, Ps, Isa, Jas, Song ...)."""
import json, re, sys
from pathlib import Path

D = json.load(open(Path(__file__).resolve().parents[4] / "books/1689-baptist-confession/1689-baptist-confession/symbolics-data/.bible/bsb.json"))
NAMES = {"gen": "GEN", "exod": "EXO", "exo": "EXO", "lev": "LEV", "num": "NUM", "deut": "DEU", "josh": "JOS",
         "judg": "JDG", "ruth": "RUT", "1 sam": "1SA", "2 sam": "2SA", "1 kgs": "1KI", "2 kgs": "2KI",
         "1 kings": "1KI", "2 kings": "2KI", "1 chr": "1CH", "2 chr": "2CH", "ezra": "EZR", "neh": "NEH",
         "esth": "EST", "job": "JOB", "ps": "PSA", "psa": "PSA", "psalm": "PSA", "prov": "PRO", "eccl": "ECC",
         "song": "SNG", "isa": "ISA", "jer": "JER", "lam": "LAM", "ezek": "EZK", "dan": "DAN", "hos": "HOS",
         "joel": "JOL", "amos": "AMO", "obad": "OBA", "jonah": "JON", "mic": "MIC", "nah": "NAM", "hab": "HAB",
         "zeph": "ZEP", "hag": "HAG", "zech": "ZEC", "mal": "MAL", "matt": "MAT", "mark": "MAR", "luke": "LUK",
         "john": "JHN", "acts": "ACT", "rom": "ROM", "1 cor": "1CO", "2 cor": "2CO", "gal": "GAL", "eph": "EPH",
         "phil": "PHP", "col": "COL", "1 thess": "1TH", "2 thess": "2TH", "1 tim": "1TI", "2 tim": "2TI",
         "titus": "TIT", "phlm": "PHL", "heb": "HEB", "jas": "JAS", "1 pet": "1PE", "2 pet": "2PE",
         "1 john": "1JN", "2 john": "2JN", "3 john": "3JN", "jude": "JUD", "rev": "REV"}
for ref in sys.argv[1:]:
    m = re.fullmatch(r"\s*(\d?\s?[A-Za-z]+)\.?\s+(\d+):(\d+)(?:[-–](\d+))?\s*", ref)
    if not m:
        print(ref, "?"); continue
    b = NAMES.get(m.group(1).lower().strip())
    if not b:
        print(ref, "? book"); continue
    c, v1 = int(m.group(2)), int(m.group(3)); v2 = int(m.group(4) or v1)
    try:
        print(f"{ref}: " + " ".join(f"[{v}] {D[b][c - 1][v - 1]}" for v in range(v1, v2 + 1)))
    except IndexError:
        print(ref, "? verse")
