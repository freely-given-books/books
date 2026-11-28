import importlib.util, pathlib
L=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("br",L/"build_review.py"); br=importlib.util.module_from_spec(spec); spec.loader.exec_module(br)
B=pathlib.Path.home()/"Projects/fgbooks/wt-institutes/books/john-calvin/institutes-of-the-christian-religion"
bad=0
for v in range(1,7):
    for p in sorted((B/"parallel/la"/f"vol-{v}").glob("*.md")):
        la=p.read_text(); fr=(B/"parallel/fr"/f"vol-{v}"/p.name).read_text()
        en=(B/"chapters/typ"/f"vol-{v}"/(p.stem+".typ")).read_text()
        _,ls=br.sections_md(la); _,fs=br.sections_md(fr); _,es=br.sections_typ(en)
        k=lambda d: sorted(x for x in d if x)
        if not (k(ls)==k(es)==k(fs)):
            bad+=1; print(v,p.stem,"la",len(k(ls)),"fr",len(k(fs)),"en",len(k(es)), "la^en",sorted(set(k(ls))^set(k(es)))[:8],"fr^en",sorted(set(k(fs))^set(k(es)))[:8])
print("mismatched files:",bad)
