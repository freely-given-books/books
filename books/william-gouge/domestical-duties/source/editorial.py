"""Editorial tables for William Gouge, Of Domesticall Duties (1622),
EEBO-TCP A68107. Read by scripts/tei/build_tei.py, tei_extract.py and the
other TEI tools (see the eebo-tcp-book skill)."""

import json
import re
from pathlib import Path

import layout

# Printed divisions the edition leaves out: the title page, and the table
# of contents, which indexes the 1622 pagination this edition does not share.
SKIP_DIVISIONS = {"title_page", "table_of_contents"}

# Gouge writes in numbered sections (heading level 3 under the edition's
# chapters); a question or objection inside a section has a run-in head.
DIV_LEVELS = {"section": 3, "dedication": 2, "errata": 2}
RUN_IN_DIVS = {"question"}

EDITION = json.loads((Path(__file__).parent / "edition.json").read_text(encoding="utf-8"))


def slugify(title):
    s = title.lower().replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def LAYOUT(root):
    """edition.json: four volumes of chapters, each chapter a run of one
    treatise's sections cut by ordinal position (Gouge's own numbering
    repeats), plus the front and back matter each volume claims."""
    divs = layout.top_divs(root)
    files = []
    for vol in EDITION["volumes"]:
        d = f"vol-{vol['number']}"

        def matter(name):
            spec = EDITION["front"][name]
            files.append({"file": f"{d}/{name}.typ", "title": spec.get("title"),
                          "parts": [divs[spec["div"] - 1]]})
        for name in vol.get("front", []):
            matter(name)
        for i, ch in enumerate(vol["chapters"], start=1):
            first, last = ch["sections"]
            files.append({"file": f"{d}/{i:02d}-{slugify(ch['title'])}.typ",
                          "title": ch["title"],
                          "parts": layout.sections(divs[ch["div"] - 1], first, last)})
        for name in vol.get("back", []):
            matter(name)
    return files
