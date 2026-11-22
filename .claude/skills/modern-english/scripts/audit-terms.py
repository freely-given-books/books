"""Theological-term audit: for each term (a stem regex), paragraphs where the Modern text has
fewer occurrences than the Classic. python3 audit-terms.py PAIRS.jsonl > terms.tsv
Only terms that must survive (rules §3.3). Words whose sense has shifted (convince, legal, quicken, humiliation,
formal, sincere, discover, communicate ...) are NOT here: dropping them is the false-friend rule (§3.6) at work;
ff-scan.py checks them the other way round (2026-11-17: this list once flagged correct replacements).""" 
import json, re, sys
TERMS = """effectual effectually efficien efficac efficacy merit impute imputation justif sanctif regenerat
regenera adopt election elect reprobat covenant grace gracious mortif vivif habit habitual principle
frame assurance assure convict lust concupiscen flesh fleshly carnal old.man new.man
indwelling corrupt depravit ordinance means duty duties evangelical hypocri
material materially physical moral morally repent penitent contrition faith believ unbelie
peace consolation comfort conscience guilt pardon forgive remission atone satisfaction sacrifice blood
cross death union communion fellowship spirit holy holiness godly godliness saint righteous
righteousness wrath curse law gospel promise threatening sovereign providence predestin
heart soul will affections understanding mind temptation tempt deceit deceitful backslid apostas
perseverance persever glory glorif worship prayer meditat watch abhor hatred hate love fear
dread terror chastise afflict discipline sin sinful iniquit transgress offen evil wicked""".split()
rows = [json.loads(l) for l in open(sys.argv[1])]
strip = lambda s: re.sub(r"#[a-z]+(\.[a-z]+)*|[\[\]]", " ", s).lower()
print("file\tn\tterm\tclassic\tmodern")
for r in rows:
    c, m = strip(r["classic"]), strip(r["modern"])
    for t in TERMS:
        p = re.compile(r"\b" + t.replace(".", r"\W+"))
        a, b = len(p.findall(c)), len(p.findall(m))
        if a > b:
            print(f"{r['file']}\t{r['n']}\t{t}\t{a}\t{b}")
