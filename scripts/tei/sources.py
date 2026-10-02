"""
A book's source transcription, whatever form it came in, as TEI.

  source/<ID>.tcp.xml     EEBO-TCP transcription (TEI already)
  source/<id>.thml.xml    CCEL ThML, converted in memory (thml_to_tei.py)

The untouched file is the provenance; every tool that reads the source
(build_tei.py, tei_extract.py on the source, tcp_structure.py, verify.py)
goes through load(), so no converted copy has to be kept.
"""

from pathlib import Path

from lxml import etree

PATTERNS = ("*.tcp.xml", "*.thml.xml")


def is_source(path):
    return any(Path(path).match(p) for p in PATTERNS)


def find(src_dir):
    """The source file in a book's source/ folder, or None."""
    for pat in PATTERNS:
        hit = next(iter(sorted(Path(src_dir).glob(pat))), None)
        if hit is not None:
            return hit
    return None


def kind(path):
    return "thml" if str(path).endswith(".thml.xml") else "tcp"


def load(path):
    """An lxml ElementTree of the source as TEI."""
    if kind(path) == "thml":
        import thml_to_tei
        return thml_to_tei.convert(path)
    return etree.parse(str(path))
