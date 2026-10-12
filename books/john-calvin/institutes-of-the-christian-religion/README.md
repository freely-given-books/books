# Institutes of the Christian Religion — John Calvin

Henry Beveridge's translation (Edinburgh, 1845) of Calvin's final Latin
edition (1559), from CCEL, in six volumes: Book I (vol. 1, with Calvin's
prefaces), Book II (vol. 2), Book III (vols 3-4, chapters 1-10 and 11-25),
Book IV (vols 5-6, chapters 1-13 and 14-20). Sources: `source/SOURCES.md`.

- `source/editorial.py`: the layout (files, volumes, short titles), what is left out.
- `source/make_volumes.py`: writes `institutes-vol-N.typ`, `cover-vol-N.typ` and
  `ebook-front-vol-N.html` from the layout; run it after changing either.
- `chapters/typ/vol-N/`: the text to review, one file per chapter.

```sh
./fgb build calvin     # six print volumes, covers, six EPUBs into dist/
./fgb page calvin      # side-by-side pages, one per volume
./fgb check calvin
```
