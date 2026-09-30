"""
Check an EPUB with Calibre's own checker (the editor's "Check book"), for
when epubcheck (Java) isn't available. Run it through Calibre's Python:

  calibre-debug scripts/tei/check_epub.py BOOK.epub

Prints one line per problem and exits non-zero if there are any.
"""

import sys

from calibre.ebooks.oeb.polish.check.main import run_checks
from calibre.ebooks.oeb.polish.container import get_container
from calibre.utils.logging import default_log

errors = run_checks(get_container(sys.argv[1], tweak_mode=True, log=default_log))
for e in errors:
    where = f"{e.name}:{e.line}" if getattr(e, "line", None) else e.name
    print(f"{type(e).__name__}: {e.msg} ({where})")
print(f"{len(errors)} issue(s)")
sys.exit(1 if errors else 0)
