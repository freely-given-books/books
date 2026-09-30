# Legacy converters (superseded)

The first pass at this book went straight from the TCP XML to Typst, without
TEI in between. Kept for reference only; use `../build_tei.py` +
`../tei_extract.py` (or `../tei.typ`) instead.

- `tcp_to_typst.py` — TCP XML → original-spelling Typst, one file per
  top-level div. Still handy for `--list` (shows what quod.lib's `1:N` means).
- `modernize_render.py` — TCP XML → modernized Typst. Its tables
  (macrons, gaps) now live in `../build_tei.py`.
