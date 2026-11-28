"""Reference rows that filter.py drops because the numbers agree: list those whose book names differ
(e.g. CCEL Mark for 1845 Matth.). Usage: python3 -I bookcheck.py"""
import json, re, pathlib
D = pathlib.Path(__file__).resolve().parent
B = {"gen":"gen","exod":"exod","ex":"exod","lev":"lev","levit":"lev","num":"num","numb":"num","deut":"deut","josh":"josh","judg":"judg","judges":"judg",
     "sam":"sam","kgs":"kgs","kings":"kgs","chr":"chr","chron":"chr","neh":"neh","job":"job","ps":"ps","psa":"ps","psal":"ps","psalm":"ps","psalms":"ps",
     "prov":"prov","eccl":"eccl","eccles":"eccl","isa":"isa","isaiah":"isa","jer":"jer","lam":"lam","ezek":"ezek","dan":"dan","hos":"hos","hosea":"hos","joel":"joel","amos":"amos",
     "mic":"mic","micah":"mic","mal":"mal","malachi":"mal","zech":"zech","hag":"hag","matt":"matt","matth":"matt","mark":"mark","luke":"luke","john":"john","acts":"acts",
     "rom":"rom","cor":"cor","gal":"gal","eph":"eph","ephes":"eph","phil":"phil","col":"col","thess":"thess","tim":"tim","tit":"tit","titus":"tit","heb":"heb",
     "jas":"jas","james":"jas","pet":"pet","peter":"pet","jude":"jude","rev":"rev"}
def books(s): return [B[w] for w in re.findall(r"[a-z]+", s.lower()) if w in B]
for c in json.load(open(D / "cand.json")):
    if c.get("big"): continue
    a, o = books(c["ccel"]), books(c["ocr"])
    if a != o and a and o: print(c["file"], c["page"], c["ccel"], "||", c["ocr"])
