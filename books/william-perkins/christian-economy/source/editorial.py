"""
Editorial tables for Christian Oeconomie (EEBO-TCP A09377), loaded by
scripts/tei/build_tei.py (it looks for editorial.py next to the TCP file).
Every name is optional; a book without this file gets a machine-only pass.
"""

# Macron abbreviations default to a suppressed "n"; these document-order
# indices expand to "m" instead (checked by hand against context).
MACRON_M = {4, 29, 31, 35, 51, 53, 62, 72, 75, 78, 79, 81, 87, 88, 93,
            109, 113, 115, 132, 141, 144, 146, 151}

# Illegible <gap>s reconstructed from context, keyed by document-order
# index of non-duplicate gaps: (letters, certainty, evidence note).
GAP_FIXES = {
    3: ("eu", "high", "1 Tim. 2:8, 'pray every where'"),
    4: ("w", "high", "1 Tim. 2:8, 'without wrath'"),
    5: ("st", "high", "custome"),
    6: ("ti", "high", "times"),
    7: ("t", "high", "Gen. 18:19, 'that they keep'"),
    8: ("t", "high", "Gen. 18:19, 'righteousness'"),
    9: ("G", "high", "citation Gen. 18. 19."),
    11: ("i", "high", "it is"),
    12: ("e", "high", "maxim: diu deliberandum quod semel statuendum"),
    13: ("t", "high", "maxim: diu deliberandum quod semel statuendum"),
    14: ("b", "high", "canon-law formula: in verbis de praesenti"),
    15: ("praesenti", "medium", "canon-law formula: in verbis de praesenti"),
    16: ("i", "high", "de iure, glossed 'in regard of right'"),
    17: ("u", "high", "lawfull"),
    19: ("5", "low", "Augustine, De Civ. Dei lib. 15 cap. 16 (digit uncertain)"),
    20: ("a", "high", "in stead"),
    21: ("o", "high", "blood"),
    22: ("o", "high", "Epistol."),
    24: ("e", "high", "cousin-german"),
    25: ("it", "medium", "it forbiddeth"),
    26: ("en", "high", "children"),
    27: ("e", "high", "the mother"),
    28: ("i", "high", "Marie"),
    29: ("i", "high", "maxim: cuius nuptias inire non licet"),
    30: ("g", "high", "maxim: eius nec coniugis licet"),
    31: ("r", "high", "formerly"),
    32: ("nta", "high", "maintaining"),
    34: ("r", "high", "mariage (this text's spelling)"),
    36: ("su", "high", "succeeding"),
    37: ("r", "high", "seueritie"),
    38: ("8", "medium", "Matt. 18:15, on rebuking a brother"),
}

# Capitalized common nouns lowercased mid-sentence (the 1609 printing
# capitalized many).
LOWERCASE_COMMON_NOUNS = {
    "family", "familie", "contract", "marriage", "mariage", "society",
    "societie", "societies", "common", "line", "case", "nature", "rules",
    "rule", "argument", "author", "education", "sacrament", "baptisme",
    "baptism", "concubine", "bride", "wife", "wiues", "wives", "children",
    "husbands", "husband", "master", "masters", "servant", "servants",
    "seruant", "seruants", "goodwife", "mother", "image", "signe", "sign",
    "generall", "general", "proper", "honour", "honor", "mistresse",
    "mistress", "state", "states", "commonwealth", "parent", "parents",
}

# Shown under "Please check" at the top of review-report.md.
REPORT_NOTES = [
    "chapter-05.typ: the #linebreak() before 'Concerning affinity' is layout, "
    "not text, so it is not stored in the TEI; keep it in chapters/typ.",
    "chapter-10 heading: your title drops ', and of due benevolence'. The "
    "printed heading is kept in orig; the shortened title is your reg.",
    "In the orig layer, the run-in lists you set out (I. ... II. ...) come out "
    "as separate paragraphs with their printed numerals. Extract the "
    "untouched TCP file itself for the exact 1609 paragraphing.",
]
