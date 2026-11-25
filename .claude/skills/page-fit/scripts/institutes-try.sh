#!/bin/bash
# institutes-try.sh 'PYTHON-DICT-LITERAL' VOLS  (run from the books repository's root)
# Sets the Institutes' PAGEFIT table in source/make_volumes.py, regenerates the print files,
# builds those volumes (e.g. 1,2) and prints the page counts and every page-fit warning.
set -e
R=$(git rev-parse --show-toplevel)
B=$R/books/john-calvin/institutes-of-the-christian-religion
python3 - "$1" "$B/source/make_volumes.py" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[2]); s = p.read_text(); i = s.index("PAGEFIT = {"); j = s.index("\n\n", i) + 1
p.write_text(s[:i] + "PAGEFIT = " + sys.argv[1].strip() + "\n" + s[j:])
PY
(cd "$B" && "$R/colophon/.venv/bin/python" source/make_volumes.py >/dev/null)
cd "$R" && ./fgb pdf calvin --volume "$2" 2>&1 | grep -E "^typst|^lulu: [0-9]|^page:|WARNING"
