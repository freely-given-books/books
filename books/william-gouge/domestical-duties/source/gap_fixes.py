"""Illegible gaps filled for this edition, keyed by the TEI pipeline's gap
index (build_tei.py --list). Carried over from the earlier Gouge converter
(sources/gap_resolver.py): "#editor" entries were read by hand from context
or from the work cited; "#auto" ones were matched against the book's own
vocabulary (its most frequent word of that shape). An empty fill means there
was no missing letter: a blot or a broken space."""

GAP_FIXES = {
    4: ('e', 'high', "the book's own vocabulary: f_are -> e:298", '#auto'),  # f[e]are
    5: ('t', 'medium', "the book's own vocabulary: s_ealing -> t:4", '#auto'),  # s[t]ealing
    34: ('e', 'high', 'by hand: O wretched m[e]n that we are', '#editor'),  # m[e]n
    35: ('i', 'medium', "the book's own vocabulary: d_ebus -> i:1", '#auto'),  # d[i]ebus
    36: ('it', 'medium', "the book's own vocabulary: Pasc_ -> it:1 (auto(2 letters))", '#auto'),  # Pasc[it]
    37: ('n', 'high', 'by hand: L.L. Pipi[n]i (the Frankish Leges Pipini), Carol. M.', '#editor'),  # Pipi[n]
    38: ('t', 'high', 'by hand: Qui diem obij[t] antequam baptisaretur', '#editor'),  # obij[t]
    39: ('', 'medium', 'by hand: "Ex opere operato, B[?]em. loc. citat." is Bellarmine: the note two sentences earlier in the same section (Treatise I, s. 45, on baptism) is "Bellarm. de Bapt. lib. 1. cap. 4", which is the place "loc. citat." points back to.  TEXT_FIXES completes the repair.', '#editor'),  # B[]
    52: ('e', 'medium', "the book's own vocabulary: Summ_ -> e:15, o:1, a:1", '#auto'),  # Summ[e]
    53: ('', 'high', 'by hand: a lost section number in a marginal cross-reference', '#editor'),  # []
    56: ('u', 'high', 'by hand: nam a[u]arus (Aug. de doctr. Chr. 1. 25)', '#editor'),  # a[u]arus
    64: ('e', 'medium', "the book's own vocabulary: ar_ -> e:2300, t:12, s:1", '#auto'),  # ar[e]
    74: ('a', 'high', 'by hand: itaque duceb[a]tur in domum sponsi (Erasmus, Adagia)', '#editor'),  # duceb[a]tur
    75: ('c', 'high', 'by hand: nes[c]iret redeundi viam ad aedes parentum', '#editor'),  # nes[c]iret
    98: ('s', 'high', 'by hand: such mischiefes a[s] children may fall into', '#editor'),  # a[s]
    111: ('ap', 'high', 'by hand: Vide [ap]ud Viu[es]. ibid.', '#editor'),  # [ap]ud
    143: ('c', 'medium', "the book's own vocabulary: _ler -> c:2", '#auto'),  # [c]ler
    144: ('c', 'high', "the book's own vocabulary: _itat -> c:12", '#auto'),  # [c]itat
    145: ('ta', 'high', 'by hand: secundas nuptias [ta]nquam supra damnare', '#editor'),  # [ta]nquam
    146: ('s', 'medium', "the book's own vocabulary: _upra -> s:1", '#auto'),  # [s]upra
    148: ('e', 'high', "the book's own vocabulary: estat_ -> e:175", '#auto'),  # estat[e]
    149: ('i', 'high', "the book's own vocabulary: _nsult -> i:8", '#auto'),  # [i]nsult
    151: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    152: ('S', 'high', 'by hand: [S]uch as the virgin Mary will be a good example', '#editor'),  # [S]uch
    153: ('so', 'medium', "the book's own vocabulary: _brietie -> so:4 (auto(2 letters))", '#auto'),  # [so]brietie
    154: ('g', 'medium', "the book's own vocabulary: _ood -> g:1027, f:55, w:6, h:5", '#auto'),  # [g]ood
    155: ('an', 'medium', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232", '#auto'),  # [an]d
    156: ('i', 'high', 'by hand: the precedency [i]s giuen to the younger', '#editor'),  # [i]s
    157: ('r', 'high', 'by hand: excellently deciphe[r]ed in Solomons Song', '#editor'),  # deciphe[r]ed
    162: ('e', 'medium', "the book's own vocabulary: H_b -> e:62, a:2", '#auto'),  # H[e]b
    166: ('e', 'medium', "the book's own vocabulary: Io_l -> e:2", '#auto'),  # Io[e]l
    167: ('b', 'high', 'by hand: the bridegroome and [b]ride goe out of their chamber', '#editor'),  # [b]ride
    168: ('b', 'high', 'by hand: in the time of a Fast it must [b]e forborne', '#editor'),  # [b]e
    169: ('m', 'high', "the book's own vocabulary: _eanes -> m:331", '#auto'),  # [m]eanes
    170: ('I', 'high', 'by hand: [I] will haue mercy, and not sacrifice (Hos. 6. 6)', '#editor'),  # [I]
    171: ('sacrifice', 'medium', 'by hand: shall not mans or womans [sacrifice]?', '#editor'),  # [sacrifice]
    172: ('or', 'high', 'by hand: continue so long sicke, [or] otherwise weake', '#editor'),  # [or]
    173: ('o', 'high', "the book's own vocabulary: _wne -> o:496", '#auto'),  # [o]wne
    174: ('assu', 'high', "the book's own vocabulary: _redly -> assu:23 (auto(4 letters))", '#auto'),  # [assu]redly
    175: ('fro', 'high', 'by hand: what can be expected [fro]m such polluted copulation', '#editor'),  # [fro]m
    181: ('a', 'medium', "the book's own vocabulary: _re -> a:2300, e:2", '#auto'),  # [a]re
    182: ('c', 'medium', "the book's own vocabulary: Soli_iting -> c:1", '#auto'),  # Soli[c]iting
    183: ('m', 'medium', "the book's own vocabulary: _ust -> m:767, i:131, l:13, d:4", '#auto'),  # [m]ust
    184: ('u', 'high', "the book's own vocabulary: di_orce -> u:10", '#auto'),  # di[u]orce
    185: ('p', 'high', "the book's own vocabulary: com_laine -> p:15", '#auto'),  # com[p]laine
    186: ('t', 'medium', "the book's own vocabulary: _he -> t:12236, s:713", '#auto'),  # [t]he
    187: ('n', 'high', "the book's own vocabulary: ma_age -> n:8", '#auto'),  # ma[n]age
    188: ('ke', 'medium', "the book's own vocabulary: pluc_d -> ke:1 (auto(2 letters))", '#auto'),  # pluc[ke]d
    189: ('be', 'high', 'by hand: may sundry other wayes [be] applied', '#editor'),  # [be]
    190: ('b', 'high', 'by hand: by way of comparison to [b]e taken', '#editor'),  # [b]e
    191: ('m', 'high', "the book's own vocabulary: _any -> m:635", '#auto'),  # [m]any
    194: ('e', 'medium', "the book's own vocabulary: _ither -> e:109, w:1, h:1", '#auto'),  # [e]ither
    195: ('', 'medium', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words', '#auto'),  # []rotten
    196: ('l', 'high', 'by hand: to carry away the goods and [l]ands', '#editor'),  # [l]ands
    198: ('', 'medium', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words', '#auto'),  # []edifie
    200: ('b', 'high', 'by hand: two that were in one [b]ed together', '#editor'),  # [b]ed
    201: ('o', 'high', "the book's own vocabulary: _ne -> o:990", '#auto'),  # [o]ne
    202: ('c', 'high', "the book's own vocabulary: _ouple -> c:14", '#auto'),  # [c]ouple
    204: ('h', 'high', 'by hand: when [h]e obserued her to be with childe', '#editor'),  # [h]e
    205: ('f', 'medium', "the book's own vocabulary: _or -> f:2960, n:228, c:196, h:2", '#auto'),  # [f]or
    207: ('s', 'high', 'by hand: The [s]ame respect moued Bathsheba', '#editor'),  # [s]ame
    208: ('w', 'medium', "the book's own vocabulary: _ell -> w:475, t:26, h:25, f:11", '#auto'),  # [w]ell
    209: ('ou', 'high', 'by hand: man and wife ought (the transcription reads "aght")', '#editor'),  # [ou]aght
    210: ('gr', 'high', 'by hand: and that on good [gr]ounds', '#editor'),  # [gr]ounds
    211: ('c', 'high', 'by hand: better then pre[c]ious ointment (Eccl. 7. 1)', '#editor'),  # pre[c]ious
    212: ('l', 'medium', "the book's own vocabulary: _oue -> l:633, m:78, i:2, d:1", '#auto'),  # [l]oue
    213: ('t', 'medium', "the book's own vocabulary: pra_e -> t:3", '#auto'),  # pra[t]e
    214: ('r', 'medium', "the book's own vocabulary: tho_owly -> r:4", '#auto'),  # tho[r]owly
    215: ('t', 'medium', "the book's own vocabulary: _he -> t:12236, s:713", '#auto'),  # [t]he
    216: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    217: ('s', 'high', "the book's own vocabulary: mea_ure -> s:48", '#auto'),  # mea[s]ure
    218: ('d', 'medium', "the book's own vocabulary: _icing -> d:2", '#auto'),  # [d]icing
    219: ('o', 'high', 'by hand: Ios. 4. 15', '#editor'),  # J[o]s
    220: ('', 'medium', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words', '#auto'),  # Jos[]
    221: ('d', 'high', 'by hand: haue no helpe from you, [d]o not in those things', '#editor'),  # [d]o
    225: ('t', 'high', 'by hand: iustum est vt eum gubernatorem assuma[t] (Ambr. Hexaem.)', '#editor'),  # assuma[t]
    233: ('i', 'high', "the book's own vocabulary: _mage -> i:58", '#auto'),  # [i]mage
    234: ('n', 'medium', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3", '#auto'),  # [n]ot
    235: ('v', 'medium', "the book's own vocabulary: _assals -> v:2", '#auto'),  # [v]assals
    236: ('a', 'medium', "the book's own vocabulary: _rrogancy -> a:3", '#auto'),  # [a]rrogancy
    237: ('m', 'medium', "the book's own vocabulary: _ore -> m:914, s:10, f:4", '#auto'),  # [m]ore
    238: ('m', 'medium', "the book's own vocabulary: _ary -> m:38, c:1", '#auto'),  # [m]ary
    241: ('i', 'high', 'by hand: so is [i]t a cause of many other vices', '#editor'),  # [i]t
    245: ('e', 'high', 'by hand: contracted thus, Iack[e], Tom, Will, Hall', '#editor'),  # Iack[e]
    247: ('f', 'high', 'by hand: to a very naturall, or a [f]renzy man', '#editor'),  # [f]renzy
    248: ('v', 'high', 'by hand: some rent, annuity, fees, [v]ailes, or the like', '#editor'),  # [v]ailes
    251: ('h', 'medium', "the book's own vocabulary: _ard -> h:26, w:1, b:1", '#auto'),  # [h]ard
    252: ('sh', 'high', 'by hand: to dispose as [sh]e please', '#editor'),  # [sh]e
    253: ('g', 'high', 'by hand: to order his [g]ift as he please', '#editor'),  # [g]ift
    254: ('fe', 'high', 'by hand: She is herein but as a [fe]offee in trust', '#editor'),  # [fe]offee
    255: ('st', 'high', 'by hand: other he reserueth for a [st]ocke', '#editor'),  # [st]ocke
    256: ('n', 'medium', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3", '#auto'),  # [n]ot
    257: ('b', 'medium', "the book's own vocabulary: _ound -> b:105, f:19, s:18, w:8", '#auto'),  # [b]ound
    259: ('g', 'medium', "the book's own vocabulary: Gre_ -> g:21, w:1", '#auto'),  # Gre[g]
    260: ('', 'medium', 'by hand: a lost folio number in "Coke Rep. 4. 3 [?] 3."', '#editor'),  # []
    261: ('a', 'high', 'by hand: Non excus[a]bit bona intentio vxoris (Greg. Sayr.)', '#editor'),  # excus[a]bit
    263: ('o', 'medium', "the book's own vocabulary: _r -> o:1440, f:1, t:1", '#auto'),  # [o]r
    264: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    267: ('d', 'medium', "the book's own vocabulary: si_e -> d:64, n:7, u:2", '#auto'),  # si[d]e
    268: ('s', 'medium', "the book's own vocabulary: commi_it -> s:1 (auto(1 letters))", '#auto'),  # commi[s]it
    270: ('s', 'high', 'by hand: componitur ex diuersis vocibu[s]', '#editor'),  # vocibu[s]
    272: ('s', 'medium', "the book's own vocabulary: _ought -> s:13, n:1, b:1", '#auto'),  # [s]ought
    273: ('t', 'high', "the book's own vocabulary: Es_h -> t:7", '#auto'),  # Es[t]h
    274: ('hi', 'high', 'by hand: Hebraei docent Vast[hi]am natam fuisse (Feuardent)', '#editor'),  # Vast[hi]am
    275: ('d', 'medium', "the book's own vocabulary: kindle_ -> d:1", '#auto'),  # kindle[d]
    278: ('t', 'high', 'by hand: about the mee[t]nesse of it', '#editor'),  # mee[t]nesse
    279: ('c', 'high', 'by hand: quid censeas di[c]as, minime prohibeo (Greg. Naz.)', '#editor'),  # di[c]
    280: ('o', 'high', 'by hand: minime prohibe[o]: sed viri tui sententiam...', '#editor'),  # prohibe[o]
    281: ('g', 'medium', "the book's own vocabulary: Gre_ -> g:21, w:1", '#auto'),  # Gre[g]
    282: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    283: ('s', 'high', "the book's own vocabulary: de_pise -> s:27", '#auto'),  # de[s]pise
    284: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    285: ('c', 'high', "the book's own vocabulary: _heerefull -> c:14", '#auto'),  # [c]heerefull
    286: ('b', 'high', 'by hand: no greater ingratitude can [b]e shewed', '#editor'),  # [b]e
    287: ('g', 'high', "the book's own vocabulary: in_ratitude -> g:9", '#auto'),  # in[g]ratitude
    288: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    289: ('n', 'high', 'by hand: to carry away the [n]ame of gratefulnesse', '#editor'),  # [n]ame
    290: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    291: ('p', 'medium', "the book's own vocabulary: _reuailes -> p:1", '#auto'),  # [p]reuailes
    292: ('f', 'high', "the book's own vocabulary: _orce -> f:42", '#auto'),  # [f]orce
    293: ('b', 'high', 'by hand: not the example of one only, [b]ut of many', '#editor'),  # [b]ut
    294: ('s', 'high', "the book's own vocabulary: _aints -> s:137", '#auto'),  # [s]aints
    295: ('al', 'medium', "the book's own vocabulary: _l -> al:1504, il:62, co:31, ga:28", '#auto'),  # [al]l
    297: ('e', 'medium', "the book's own vocabulary: foemina_ -> e:3", '#auto'),  # foemina[e]
    302: ('t', 'high', 'by hand: gubernatorem [t]e Deus voluit esse sexus inferioris', '#editor'),  # [t]e
    308: ('n', 'high', 'by hand: namely, to be a[n] helpe', '#editor'),  # a[n]
    309: ('q', 'high', "the book's own vocabulary: re_uireth -> q:101", '#auto'),  # re[q]uireth
    310: ('d', 'high', 'by hand: commend and reward what she hath well [d]one', '#editor'),  # [d]one
    311: ('t', 'medium', "the book's own vocabulary: _hat -> t:4575, w:636", '#auto'),  # [t]hat
    312: ('fr', 'high', 'by hand: Giue her of the [fr]uit of her hands (Prov. 31. 31)', '#editor'),  # [fr]uit
    313: ('h', 'medium', "the book's own vocabulary: _er -> h:1661, i:23, p:10, v:6", '#auto'),  # [h]er
    314: ('If', 'high', 'by hand: [If] there be no delight in ones person', '#editor'),  # [If]
    316: ('a', 'high', "the book's own vocabulary: _dde -> a:42", '#auto'),  # [a]dde
    317: ('s', 'high', "the book's own vocabulary: _mall -> s:34", '#auto'),  # [s]mall
    318: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    319: ('t', 'medium', "the book's own vocabulary: _hat -> t:4575, w:636", '#auto'),  # [t]hat
    320: ('c', 'high', 'by hand: as of a discontented [c]reditor ouer a desperate debtor', '#editor'),  # [c]reditor
    321: ('o', 'medium', "the book's own vocabulary: _biect -> o:185, a:3", '#auto'),  # [o]biect
    322: ('e', 'high', 'by hand: n[e]que quicquam tale exprobrauit (Chrysostom)', '#editor'),  # n[e]
    323: ('', 'high', 'by hand: C[or]nelius -- the transcription reads "C•raelius"; Acts 10. 2, 30 in the margin identifies him', '#editor'),  # C[]raelius
    324: ('l', 'high', 'by hand: the lawes vnder which they [l]iue', '#editor'),  # [l]iue
    325: ('f', 'high', 'by hand: vse all the [f]raudulent meanes they can', '#editor'),  # [f]raudulent
    326: ('n', 'medium', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3", '#auto'),  # [n]ot
    327: ('b', 'high', "the book's own vocabulary: dou_le -> b:32", '#auto'),  # dou[b]le
    328: ('k', 'high', "the book's own vocabulary: vn_indnesse -> k:9", '#auto'),  # vn[k]indnesse
    329: ('t', 'high', "the book's own vocabulary: _hinking -> t:20", '#auto'),  # [t]hinking
    330: ('w', 'medium', "the book's own vocabulary: _iues -> w:1085, l:13, g:4, v:1", '#auto'),  # [w]iues
    331: ('l', 'medium', "the book's own vocabulary: _esse -> l:66, n:1, m:1, b:1", '#auto'),  # [l]esse
    332: ('d', 'high', 'by hand: affected with a wrong [d]one to the bodie', '#editor'),  # [d]one
    333: ('i', 'medium', "the book's own vocabulary: _n -> i:5378, a:1059, o:506, v:1", '#auto'),  # [i]n
    334: ('s', 'high', "the book's own vocabulary: _trangers -> s:27", '#auto'),  # [s]trangers
    335: ('h', 'high', 'by hand: for [h]e hath more power ouer them in his house', '#editor'),  # [h]e
    336: ('o', 'medium', "the book's own vocabulary: _r -> o:1440, f:1, t:1", '#auto'),  # [o]r
    337: ('u', 'high', "the book's own vocabulary: ser_ants -> u:1096", '#auto'),  # ser[u]ants
    338: ('an', 'medium', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232", '#auto'),  # [an]d
    339: ('n', 'medium', "the book's own vocabulary: _eeds -> n:48, d:9, s:1, w:1", '#auto'),  # [n]eeds
    341: ('p', 'high', 'by hand: the most [p]eeuish, and peruerse wiues', '#editor'),  # [p]eeuish
    342: ('i', 'high', 'by hand: they are very deuils [i]ncarnate', '#editor'),  # [i]ncarnate
    343: ('sh', 'high', 'by hand: in their place [sh]ew themselues so vnlike to Christ', '#editor'),  # [sh]ew
    344: ('l', 'medium', "the book's own vocabulary: _oue -> l:633, m:78, i:2, d:1", '#auto'),  # [l]oue
    345: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    346: ('s', 'high', 'by hand: they may haue [s]ome bait to allure their affections', '#editor'),  # [s]ome
    347: ('o', 'medium', "the book's own vocabulary: _r -> o:1440, f:1, t:1", '#auto'),  # [o]r
    348: ('p', 'high', "the book's own vocabulary: _ortion -> p:48", '#auto'),  # [p]ortion
    349: ('e', 'high', "the book's own vocabulary: _xpect -> e:16", '#auto'),  # [e]xpect
    350: ('lo', 'high', 'by hand: This cannot be a true sound [lo]ue', '#editor'),  # [lo]ue
    351: ('in', 'high', "the book's own vocabulary: _heritance -> in:48", '#auto'),  # [in]heritance
    352: ('lo', 'high', 'by hand: an holy, pure, chaste, [lo]ue', '#editor'),  # [lo]ue
    353: ('ef', 'high', 'by hand: as is euident by the [ef]fect thereof', '#editor'),  # [ef]fect
    354: ('to', 'high', 'by hand: I am euen ashamed [to] mention', '#editor'),  # [to]
    355: ('at', 'high', 'by hand: let such know, th[at] they shall be accounted', '#editor'),  # th[at]
    356: ('te', 'medium', "the book's own vocabulary: adul_rers -> te:3 (auto(2 letters))", '#auto'),  # adul[te]rers
    357: ('l', 'high', "the book's own vocabulary: _eaue -> l:80", '#auto'),  # [l]eaue
    358: ('m', 'medium', "the book's own vocabulary: _ust -> m:767, i:131, l:13, d:4", '#auto'),  # [m]ust
    359: ('p', 'high', 'by hand: a pit of needlesse [p]erill', '#editor'),  # [p]erill
    360: ('st', 'high', 'by hand: to bring vs to this [st]raite of parting with our life', '#editor'),  # [st]raite
    361: ('t', 'medium', "the book's own vocabulary: _ime -> t:340, a:21", '#auto'),  # [t]ime
    362: ('e', 'high', 'by hand: cannot any other way be [e]ffected', '#editor'),  # [e]ffected
    363: ('to', 'high', 'by hand: no other way [to] redeeme the Church', '#editor'),  # [to]
    364: ('g', 'high', "the book's own vocabulary: _reater -> g:116", '#auto'),  # [g]reater
    365: ('r', 'high', "the book's own vocabulary: _ule -> r:107", '#auto'),  # [r]ule
    366: ('ca', 'high', 'by hand: which minde men must much more [ca]rie towards their wiues', '#editor'),  # [ca]rie
    367: ('ga', 'high', 'by hand: It was for our saluation that Christ [ga]ue himselfe', '#editor'),  # [ga]ue
    368: ('th', 'high', "the book's own vocabulary: _eir -> th:4253", '#auto'),  # [th]eir
    369: ('m', 'medium', "the book's own vocabulary: _easure -> m:48, l:3", '#auto'),  # [m]easure
    370: ('af', 'high', "the book's own vocabulary: _fections -> af:19", '#auto'),  # [af]fections
    371: ('be', 'high', 'by hand: if any extraordinary charge must [be] laid out', '#editor'),  # [be]
    372: ('wi', 'high', 'by hand: little loue [wi]ll then appeare', '#editor'),  # [wi]ll
    373: ('an', 'medium', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232", '#auto'),  # [an]d
    374: ('g', 'high', 'by hand: As [g]old and other like mettals are tryed by the fire', '#editor'),  # [g]ld
    375: ('affl', 'high', 'by hand: so loue by [affl]ictions and crosses', '#editor'),  # [affl]ictions
    376: ('t', 'high', 'by hand: now [t]ender-hearted, then againe hard-hearted', '#editor'),  # [t]ender
    377: ('l', 'high', 'by hand: now smiling, then [l]owring', '#editor'),  # [l]owring
    378: ('y', 'high', "the book's own vocabulary: _oung -> y:77", '#auto'),  # [y]oung
    379: ('t', 'medium', "the book's own vocabulary: _hose -> t:393, w:60, c:2", '#auto'),  # [t]hose
    380: ('a', 'high', 'by hand: proue in their loue as cold [a]s ice', '#editor'),  # [a]s
    381: ('t', 'high', "the book's own vocabulary: _heir -> t:4253", '#auto'),  # [t]heir
    382: ('u', 'high', "the book's own vocabulary: ne_er -> u:146", '#auto'),  # ne[u]er
    383: ('w', 'high', 'by hand: [w]e haue on the one side a good direction', '#editor'),  # [w]e
    384: ('lo', 'high', 'by hand: a good direction to teach vs how to [lo]ue our wiues', '#editor'),  # [lo]ue
    385: ('o', 'high', "the book's own vocabulary: _ther -> o:860", '#auto'),  # [o]ther
    386: ('far', 'high', 'by hand: it sheweth vs how [far]re short we come', '#editor'),  # [far]re
    387: ('m', 'medium', "the book's own vocabulary: _ay -> m:1244, w:165, s:141, d:90", '#auto'),  # [m]ay
    388: ('w', 'high', 'by hand: a Subiection [w]hereunto by nature we are all loath to yeeld', '#editor'),  # [w]hereunto
    389: ('th', 'medium', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944", '#auto'),  # [th]e
    390: ('m', 'high', 'by hand: and [m]uch more easie it is to performe the part of a wife', '#editor'),  # [m]uch
    391: ('ter', 'high', "the book's own vocabulary: pat_ne -> ter:89 (auto(3 letters))", '#auto'),  # pat[ter]ne
    392: ('wiu', 'high', 'by hand: So ought men to loue their [wiu]es as their owne bodies', '#editor'),  # [wiu]es
    393: ('n', 'high', 'by hand: see they neither faune o[n] them, nor flatter them', '#editor'),  # o[n]
    394: ('t', 'high', 'by hand: as great as possibly i[t] can be', '#editor'),  # i[t]
    395: ('s', 'medium', "the book's own vocabulary: _oone -> s:51, m:4, b:1, n:1", '#auto'),  # [s]oone
    396: ('f', 'medium', "the book's own vocabulary: _or -> f:2960, n:228, c:196, h:2", '#auto'),  # [f]or
    397: ('h', 'high', "the book's own vocabulary: _eart -> h:198", '#auto'),  # [h]eart
    398: ('re', 'high', "the book's own vocabulary: _adinesse -> re:19", '#auto'),  # [re]adinesse
    399: ('b', 'medium', "the book's own vocabulary: _ooz -> b:2", '#auto'),  # [b]ooz
    400: ('h', 'medium', "the book's own vocabulary: be_oofull -> h:1", '#auto'),  # be[h]oofull
    401: ('in', 'high', 'by hand: as the history [in] many particulars sheweth', '#editor'),  # [in]
    402: ('a', 'high', "the book's own vocabulary: _miable -> a:12", '#auto'),  # [a]miable
    403: ('v', 'high', "the book's own vocabulary: _ices -> v:53", '#auto'),  # [v]ices
    404: ('ou', 'high', 'by hand: with goodnes he [ou]ght to ouercome euill', '#editor'),  # [ou]ught
    405: ('t', 'medium', "the book's own vocabulary: _hat -> t:4575, w:636", '#auto'),  # [t]hat
    406: ('lo', 'high', 'by hand: for [lo]ue hopeth all things (1 Cor. 13. 7)', '#editor'),  # [lo]ue
    407: ('sa', 'high', 'by hand: as he may iustly [sa]y', '#editor'),  # [sa]y
    408: ('c', 'high', "the book's own vocabulary: _hurch -> c:500", '#auto'),  # [c]hurch
    409: ('af', 'high', "the book's own vocabulary: _ford -> af:35 (auto(2 letters))", '#auto'),  # [af]ford
    410: ('ali', 'high', "the book's own vocabulary: _enate -> ali:6 (auto(3 letters))", '#auto'),  # [ali]enate
    412: ('', 'high', 'by hand: more abomi[]nable -- the bullet is a blot, not a letter', '#editor'),  # abomi[]nable
    413: ('o', 'medium', "the book's own vocabulary: _r -> o:1440, f:1, t:1", '#auto'),  # [o]r
    414: ('s', 'high', "the book's own vocabulary: sub_tance -> s:35", '#auto'),  # sub[s]tance
    415: ('s', 'medium', "the book's own vocabulary: _eeme -> s:54, d:1", '#auto'),  # [s]eeme
    416: ('re', 'high', "the book's own vocabulary: pa_nts -> re:1302", '#auto'),  # pa[re]nts
    417: ('cia', 'high', "the book's own vocabulary: espe_lly -> cia:147", '#auto'),  # espe[cia]lly
    418: ('d', 'medium', "the book's own vocabulary: an_ -> d:8820, y:710, s:4, a:2", '#auto'),  # an[d]
    419: ('i', 'medium', "the book's own vocabulary: _n -> i:5378, a:1059, o:506, v:1", '#auto'),  # [i]n
    420: ('o', 'medium', "the book's own vocabulary: _r -> o:1440, f:1, t:1", '#auto'),  # [o]r
    421: ('i', 'high', "the book's own vocabulary: _mpious -> i:12", '#auto'),  # [i]mpious
    422: ('s', 'high', "the book's own vocabulary: compri_ed -> s:36", '#auto'),  # compri[s]ed
    423: ('b', 'medium', "the book's own vocabulary: _y -> b:1790, m:123", '#auto'),  # [b]y
    424: ('th', 'medium', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944", '#auto'),  # [th]e
    425: ('to', 'high', 'by hand: children haue euer vsed [to] giue those titles', '#editor'),  # [to]
    426: ('b', 'medium', "the book's own vocabulary: _athsheba -> b:4", '#auto'),  # [b]athsheba
    429: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    430: ('n', 'medium', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3", '#auto'),  # [n]ot
    431: ('re', 'high', "the book's own vocabulary: pa_nts -> re:1302", '#auto'),  # pa[re]nts
    432: ('o', 'high', "the book's own vocabulary: _bserue -> o:67", '#auto'),  # [o]bserue
    433: ('m', 'medium', "the book's own vocabulary: _ore -> m:914, s:10, f:4", '#auto'),  # [m]ore
    434: ('se', 'medium', "the book's own vocabulary: v_ -> se:260, ow:25, iz:12, ir:12", '#auto'),  # v[se]
    435: ('r', 'high', "the book's own vocabulary: pa_able -> r:10", '#auto'),  # pa[r]able
    436: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    437: ('t', 'high', 'by hand: much offended and grieued [t]hereat', '#editor'),  # [t]hereat
    438: ('v', 'high', "the book's own vocabulary: _ery -> v:274", '#auto'),  # [v]ery
    439: ('b', 'high', "the book's own vocabulary: _efore -> b:494", '#auto'),  # [b]efore
    440: ('be', 'high', 'by hand: must [be] so framed both for matter and manner', '#editor'),  # [be]
    441: ('oc', 'high', "the book's own vocabulary: _casion -> oc:123", '#auto'),  # [oc]casion
    442: ('th', 'medium', "the book's own vocabulary: _em -> th:1875, qu:6, id:3, rh:2", '#auto'),  # [th]em
    443: ('pa', 'high', "the book's own vocabulary: _rents -> pa:1302", '#auto'),  # [pa]rents
    444: ('du', 'medium', "the book's own vocabulary: _ty -> du:169, ci:2", '#auto'),  # [du]ty
    446: ('ll', 'high', 'by hand: they doe not so generally disa[ll]ow this dutie', '#editor'),  # disa[ll]ow
    450: ('', 'high', 'by hand: as some will haue it -- the bullet is a blot', '#editor'),  # []it
    451: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    452: ('s', 'high', "the book's own vocabulary: _onnes -> s:47", '#auto'),  # [s]onnes
    453: ('c', 'high', "the book's own vocabulary: _ommended -> c:59", '#auto'),  # [c]ommended
    454: ('b', 'high', 'by hand: It is collected [b]oth by ancient and later Diuines', '#editor'),  # [b]oth
    455: ('in', 'high', 'by hand: our Lord Iesus Christ [in] his younger yeeres', '#editor'),  # [in]
    456: ('th', 'medium', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944", '#auto'),  # [th]e
    457: ('ie', 'high', "the book's own vocabulary: sub_ction -> ie:297", '#auto'),  # sub[ie]ction
    458: ('le', 'medium', "the book's own vocabulary: cal_d -> le:93, ce:1", '#auto'),  # cal[le]d
    459: ('bo', 'high', 'by hand: an hand in placing [bo]th their children', '#editor'),  # [bo]th
    460: ('w', 'high', "the book's own vocabulary: _orld -> w:137", '#auto'),  # [w]orld
    461: ('w', 'high', "the book's own vocabulary: _hile -> w:105", '#auto'),  # [w]hile
    462: ('sh', 'high', 'by hand: that they [sh]ould see their children well trained vp', '#editor'),  # [sh]ould
    463: ('ent', 'high', 'by hand: children may [ent]er into religious orders', '#editor'),  # [ent]er
    464: ('gai', 'high', "the book's own vocabulary: a_nst -> gai:408", '#auto'),  # a[gai]nst
    465: ('doe', 'high', 'by hand: Whereby they [doe] not only patronize apparent disobedience', '#editor'),  # [doe]
    466: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    468: ('f', 'medium', "the book's own vocabulary: _or -> f:2960, n:228, c:196, h:2", '#auto'),  # [f]or
    469: ('d', 'high', "the book's own vocabulary: _uty -> d:169", '#auto'),  # [d]uty
    471: ('s', 'medium', "the book's own vocabulary: alij_ -> s:2", '#auto'),  # alij[s]
    472: ('d', 'high', 'by hand: while the [d]ate of their couenant lasteth', '#editor'),  # [d]ate
    473: ('t', 'high', 'by hand: greater [t]hen of a childe', '#editor'),  # [t]hen
    474: ('p', 'medium', "the book's own vocabulary: _ower -> p:260, l:3, t:1", '#auto'),  # [p]ower
    475: ('p', 'medium', "the book's own vocabulary: _ower -> p:260, l:3, t:1", '#auto'),  # [p]ower
    476: ('u', 'high', "the book's own vocabulary: ser_ant -> u:247", '#auto'),  # ser[u]ant
    477: ('s', 'high', "the book's own vocabulary: Be_ides -> s:52", '#auto'),  # Be[s]ides
    478: ('a', 'medium', "the book's own vocabulary: _way -> a:186, s:4", '#auto'),  # [a]way
    479: ('t', 'medium', "the book's own vocabulary: _aken -> t:190, s:2", '#auto'),  # [t]aken
    480: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    481: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    482: ('', 'high', 'by hand: My sonne, saith he -- the bullet is a blot', '#editor'),  # []he
    483: (' ', 'medium', 'a broken word space: the letters on both sides spell two words', '#auto'),  # a[ ]glad
    486: ('c', 'medium', "the book's own vocabulary: _ocker -> c:3 (auto(1 letters))", '#auto'),  # [c]ocker
    487: ('b', 'high', "the book's own vocabulary: for_eare -> b:46", '#auto'),  # for[b]eare
    488: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    490: ('n', 'high', "the book's own vocabulary: Io_athan -> n:10 (auto(1 letters))", '#auto'),  # Io[n]athan
    493: ('b', 'high', 'by hand: [b]ut it hardly ascendeth from children to parents', '#editor'),  # [b]ut
    496: ('o', 'medium', "the book's own vocabulary: su_rum -> o:1", '#auto'),  # su[o]rum
    497: ('p', 'high', 'by hand: More tulere [p]atrum (Virgil, Aen. 11. 185-6)', '#editor'),  # [p]a
    498: ('t', 'high', 'by hand: More tulere pa[t]rum', '#editor'),  # pa[t]rum
    499: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    500: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    501: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    502: ('f', 'medium', "the book's own vocabulary: _arre -> f:140, w:12, b:2, i:1", '#auto'),  # [f]arre
    503: ('S', 'high', 'by hand: [S]ome by the needlesse solemnitie of their parents funerall', '#editor'),  # [S]ome
    504: ('so', 'high', 'by hand: are [so] farre cast into debt', '#editor'),  # [so]
    505: ('t', 'medium', "the book's own vocabulary: _he -> t:12236, s:713", '#auto'),  # [t]he
    506: ('le', 'high', "the book's own vocabulary: so_mnitie -> le:8", '#auto'),  # so[le]mnitie
    507: ('g', 'high', "the book's own vocabulary: char_es -> g:10", '#auto'),  # char[g]es
    508: ('b', 'medium', "the book's own vocabulary: _urying -> b:3", '#auto'),  # [b]urying
    509: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    510: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    511: ('k', 'high', "the book's own vocabulary: ma_eth -> k:178", '#auto'),  # ma[k]eth
    512: ('v', 'high', "the book's own vocabulary: _engeance -> v:30", '#auto'),  # [v]engeance
    513: ('a', 'high', 'by hand: such measure to be meated out to them, [a]s they mete', '#editor'),  # [a]s
    514: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    515: ('t', 'high', "the book's own vocabulary: ingra_itude -> t:9", '#auto'),  # ingra[t]itude
    516: ('o', 'high', 'by hand: apud Di[o]g. Laert. l. 1.', '#editor'),  # Di[o]g
    517: ('u', 'high', "the book's own vocabulary: Da_ids -> u:18", '#auto'),  # Da[u]ids
    518: ('m', 'medium', "the book's own vocabulary: She_ei -> m:1 (auto(1 letters))", '#auto'),  # She[m]ei
    519: ('i', 'high', "the book's own vocabulary: _ustice -> i:35", '#auto'),  # [i]ustice
    520: ('a', 'high', "the book's own vocabulary: allow_nce -> a:27", '#auto'),  # allow[a]nce
    521: ('h', 'high', "the book's own vocabulary: _eart -> h:198", '#auto'),  # [h]eart
    522: ('p', 'medium', "the book's own vocabulary: _ower -> p:260, l:3, t:1", '#auto'),  # [p]ower
    523: ('n', 'medium', "the book's own vocabulary: shi_ing -> n:1", '#auto'),  # shi[n]ing
    524: ('th', 'medium', "the book's own vocabulary: _ey -> th:2982, ob:109, pr:5, wh:1", '#auto'),  # [th]ey
    525: ('th', 'medium', "the book's own vocabulary: _ey -> th:2982, ob:109, pr:5, wh:1", '#auto'),  # [th]ey
    526: ('w', 'high', "the book's own vocabulary: _eary -> w:12", '#auto'),  # [w]eary
    527: ('th', 'medium', "the book's own vocabulary: _em -> th:1875, qu:6, id:3, rh:2", '#auto'),  # [th]em
    528: ('er', 'high', "the book's own vocabulary: young_ -> er:27", '#auto'),  # young[er]
    529: ('w', 'high', "the book's own vocabulary: _eary -> w:12", '#auto'),  # [w]eary
    530: ('th', 'high', "the book's own vocabulary: _eir -> th:4253", '#auto'),  # [th]eir
    531: ('ce', 'high', 'by hand: the law of God maketh it plaine in[ce]st', '#editor'),  # in[ce]st
    532: ('s', 'medium', "the book's own vocabulary: parent_ -> s:1302, i:1", '#auto'),  # parent[s]
    533: ('', 'high', 'by hand: a lost book number in a marginal cross-reference', '#editor'),  # []
    534: ('i', 'high', 'by hand: that dutie [i]s due to them', '#editor'),  # [i]s
    535: ('s', 'high', "the book's own vocabulary: de_ert -> s:5", '#auto'),  # de[s]ert
    536: ('f', 'high', "the book's own vocabulary: _rom -> f:963", '#auto'),  # [f]rom
    537: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    538: ('t', 'medium', "the book's own vocabulary: _hey -> t:2982, w:1", '#auto'),  # [t]hey
    541: ('ni', 'medium', "the book's own vocabulary: Hoph_ -> ni:2", '#auto'),  # Hoph[ni]
    542: ('a', 'medium', "the book's own vocabulary: _re -> a:2300, e:2", '#auto'),  # [a]re
    543: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    544: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    545: ('in', 'high', 'by hand: though he truly [in]tend what he promiseth', '#editor'),  # [in]tend
    546: ('e', 'medium', "the book's own vocabulary: _ither -> e:109, w:1, h:1", '#auto'),  # [e]ither
    547: ('h', 'high', 'by hand: but thought when [h]e made the promise', '#editor'),  # [h]e
    548: ('u', 'medium', "the book's own vocabulary: e_ent -> u:3", '#auto'),  # e[u]ent
    549: ('str', 'high', 'by hand: Gods power cannot be so [str]aitned', '#editor'),  # [str]aitned
    550: ('th', 'high', 'by hand: men may be taken away before [th]e time', '#editor'),  # [th]etime
    551: ('li', 'high', 'by hand: but God euer [li]ueth, and changeth not', '#editor'),  # [li]eth
    552: ('sa', 'high', 'by hand: Gods, who euer remaineth the [sa]me', '#editor'),  # [sa]me
    553: ('pa', 'high', "the book's own vocabulary: com_rison -> pa:24 (auto(2 letters))", '#auto'),  # com[pa]rison
    554: ('b', 'high', 'by hand: no dutie so holy and necessarie, [b]ut may be peruerted', '#editor'),  # [b]ut
    555: ('si', 'high', 'by hand: the catalogue of notorious [si]nnes', '#editor'),  # [si]nnes
    556: ('lu', 'high', 'by hand: through couetousnesse, [lu]st, vaine-glory', '#editor'),  # [lu]st
    557: ('sh', 'high', 'by hand: in stead of the good which they [sh]ould doe', '#editor'),  # [sh]ould
    558: ('t', 'medium', "the book's own vocabulary: _hem -> t:1875, r:2, s:1", '#auto'),  # [t]hem
    559: ('re', 'medium', 'by hand: Is not this mee[re] apish kindnesse?', '#editor'),  # mee[re]
    561: ('c', 'high', 'by hand: Basil. loc. [c]it.', '#editor'),  # [c]it
    562: ('y', 'high', "the book's own vocabulary: _oung -> y:77", '#auto'),  # [y]oung
    563: ('d', 'high', "the book's own vocabulary: _oubt -> d:27", '#auto'),  # [d]oubt
    564: ('tr', 'high', "the book's own vocabulary: coun_ies -> tr:5 (auto(2 letters))", '#auto'),  # coun[tr]ies
    565: ('w', 'high', 'by hand: the sincere milke of the [w]ord (1 Pet. 2. 2)', '#editor'),  # [w]ord
    566: ('i', 'high', "the book's own vocabulary: _nfants -> i:7", '#auto'),  # [i]nfants
    567: ('pr', 'high', 'by hand: the abilitie, and [pr]omptnesse which is in them to sucke', '#editor'),  # [pr]omptnesse
    568: ('ca', 'high', 'by hand: Gods prouidence in [ca]using a womans breasts to yeeld milke', '#editor'),  # [ca]using
    569: ('t', 'medium', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10", '#auto'),  # [t]o
    570: ('i', 'high', "the book's own vocabulary: _mplie -> i:5", '#auto'),  # [i]mplie
    571: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    573: ('n', 'high', "the book's own vocabulary: _ourished -> n:11", '#auto'),  # [n]ourished
    574: ('y', 'high', "the book's own vocabulary: _oung -> y:77", '#auto'),  # [y]oung
    575: ('lo', 'high', 'by hand: mothers [lo]ue those children best', '#editor'),  # [lo]ue
    576: ('sh', 'high', 'by hand: and we [sh]all finde the dutie in question', '#editor'),  # [sh]all
    577: ('p', 'high', 'by hand: that the [p]aps of that woman gaue him sucke', '#editor'),  # [p]aps
    578: ('s', 'medium', "the book's own vocabulary: _ucke -> s:50, b:2, d:1", '#auto'),  # [s]ucke
    579: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    580: ('fo', 'medium', 'by hand: to lay them [fo]rth for ostentation?', '#editor'),  # [fo]rth
    581: ('w', 'high', 'by hand: no warrant for that in all Gods [w]ord', '#editor'),  # [w]ord
    582: ('n', 'high', 'by hand: there is [n]o milke in the breasts', '#editor'),  # [n]o
    583: ('ly', 'high', "the book's own vocabulary: ordinari_ -> ly:22", '#auto'),  # ordinari[ly]
    584: ('th', 'medium', "the book's own vocabulary: _ey -> th:2982, ob:109, pr:5, wh:1", '#auto'),  # [th]ey
    585: ('o', 'medium', "the book's own vocabulary: _f -> o:10396, i:1181", '#auto'),  # [o]f
    586: ('an', 'medium', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232", '#auto'),  # [an]d
    587: ('th', 'high', "the book's own vocabulary: mo_ers -> th:104", '#auto'),  # mo[th]ers
    588: ('c', 'high', "the book's own vocabulary: _hilde -> c:356", '#auto'),  # [c]hilde
    589: ('c', 'high', "the book's own vocabulary: _hild -> c:29", '#auto'),  # [c]hild
    590: ('d', 'high', 'by hand: She was therefore a [d]rie nurse', '#editor'),  # [d]rie
    591: ('h', 'medium', "the book's own vocabulary: _aue -> h:1133, g:102, s:13, r:1", '#auto'),  # [h]aue
    592: ('d', 'high', 'by hand: those nurses might be [d]ead', '#editor'),  # [d]ead
    593: ('n', 'high', 'by hand: for want of milke, [n]ipple, or some other like defect', '#editor'),  # [n]ipple
    594: ('to', 'high', 'by hand: the childe which she [to]oke for her owne to nurse', '#editor'),  # [to]oke
    595: ('f', 'medium', "the book's own vocabulary: o_ -> f:10396, r:1440, n:506, b:8", '#auto'),  # o[f]
    596: ('f', 'medium', "the book's own vocabulary: o_ -> f:10396, r:1440, n:506, b:8", '#auto'),  # o[f]
    597: ('n', 'high', "the book's own vocabulary: _icenesse -> n:5 (auto(1 letters))", '#auto'),  # [n]icenesse
    598: ('n', 'high', "the book's own vocabulary: Elka_ah -> n:13", '#auto'),  # Elka[n]ah
    599: ('c', 'high', "the book's own vocabulary: _hildren -> c:1420", '#auto'),  # [c]hildren
    600: ('v', 'medium', "the book's own vocabulary: _nder -> v:344, u:1", '#auto'),  # [v]nder
    601: ('t', 'high', "the book's own vocabulary: _his -> t:2062", '#auto'),  # [t]his
    602: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    603: ('i', 'medium', "the book's own vocabulary: _n -> i:5378, a:1059, o:506, v:1", '#auto'),  # [i]n
    604: ('se', 'high', 'by hand: a faithfull and constant ob[se]ruance of this ordinance', '#editor'),  # ob[se]ruance
    605: ('e', 'high', "the book's own vocabulary: _lizabeth -> e:7", '#auto'),  # [e]lizabeth
    606: ('t', 'medium', "the book's own vocabulary: Deu_ -> t:59, m:6, s:2, l:1", '#auto'),  # Deu[t]
    607: ('c', 'high', "the book's own vocabulary: _hildren -> c:1420", '#auto'),  # [c]hildren
    608: ('r', 'high', 'by hand: heathenish, idolatrous, [r]idiculous names', '#editor'),  # [r]idiculous
    609: ('d', 'medium', "the book's own vocabulary: _oe -> d:944, g:174, w:12, r:6", '#auto'),  # [d]oe
    610: ('b', 'high', "the book's own vocabulary: _aptised -> b:18", '#auto'),  # [b]aptised
    611: ('t', 'medium', "the book's own vocabulary: congrega_ion -> t:2", '#auto'),  # congrega[t]ion
    612: ('it', 'high', 'by hand: or to the childe [it] selfe', '#editor'),  # [it]
    613: ('r', 'high', "the book's own vocabulary: _eckoned -> r:21", '#auto'),  # [r]eckoned
    614: ('b', 'high', "the book's own vocabulary: _eginneth -> b:9", '#auto'),  # [b]eginneth
    615: ('f', 'high', 'by hand: till it be [f]it to be placed forth', '#editor'),  # [f]t
    617: ('r', 'high', "the book's own vocabulary: appa_ell -> r:62", '#auto'),  # appa[r]ell
    618: ('b', 'high', 'by hand: tagged and ragged like beggars [b]rats', '#editor'),  # [b]rats
    619: ('o', 'high', 'by hand: but [o]uer-strictly hold them in', '#editor'),  # [o]uer
    620: ('b', 'high', 'by hand: [b]ut plaine vnnaturalnesse in such parents', '#editor'),  # [b]ut
    621: ('th', 'medium', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944", '#auto'),  # [th]e
    622: ('d', 'high', "the book's own vocabulary: ten_ernesse -> d:7", '#auto'),  # ten[d]ernesse
    623: ('da', 'medium', "the book's own vocabulary: _intily -> da:2", '#auto'),  # [da]intily
    626: ('', 'high', 'by hand: (in the way that he should go) -- the bullet is a blot', '#editor'),  # go[]
    627: ('', 'medium', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words', '#auto'),  # []grieuous
    628: ('', 'medium', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words', '#auto'),  # []bane
    629: ('', 'high', 'by hand: Parents are bour[]d -- see TEXT_FIXES: printed "bound"', '#editor'),  # bour[]d
    631: ('z', 'high', "the book's own vocabulary: solemni_ing -> z:5", '#auto'),  # solemni[z]ing
    632: ('o', 'high', 'by hand: workes of mercy [o]r of iudgement', '#editor'),  # [o]r
    633: ('t', 'medium', "the book's own vocabulary: _he -> t:12236, s:713", '#auto'),  # [t]he
    634: ('e', 'medium', "the book's own vocabulary: _ach -> e:86, z:2", '#auto'),  # [e]ach
    635: ('lik', 'high', 'by hand: so [lik]ewise other masters (see TEXT_FIXES for the space)', '#editor'),  # so[lik]ewise
    636: ('h', 'medium', "the book's own vocabulary: _er -> h:1661, i:23, p:10, v:6", '#auto'),  # [h]er
    637: ('If', 'high', 'by hand: [If] masters themselues be religious', '#editor'),  # [If]
    638: ('', 'high', 'by hand: (same lacuna, second of three adjacent gaps)', '#editor'),  # If[]
    639: ('', 'high', 'by hand: (same lacuna, third of three adjacent gaps)', '#editor'),  # If[]
    640: ('d', 'medium', "the book's own vocabulary: _oe -> d:944, g:174, w:12, r:6", '#auto'),  # [d]oe
    641: ('th', 'high', 'by hand: very profitable to [th]e children', '#editor'),  # [th]e
    642: ('g', 'medium', "the book's own vocabulary: _ood -> g:1027, f:55, w:6, h:5", '#auto'),  # [g]ood
    646: ('e', 'high', 'by hand: Quo sem[e]l est imbuta (Horace, Ep. 1. 2. 69)', '#editor'),  # sem[e]lest
    647: ('o', 'high', 'by hand: seruabit od[o]rem testa diu', '#editor'),  # od[o]rem
    648: ('t', 'high', 'by hand: [t]hen be suffered to runne on in euill', '#editor'),  # [t]hen
    649: ('t', 'high', 'by hand: till they get an habit [t]herein', '#editor'),  # [t]herein
    650: ('c', 'high', "the book's own vocabulary: _hildren -> c:1420", '#auto'),  # [c]hildren
    651: ('m', 'high', "the book's own vocabulary: _ens -> m:24", '#auto'),  # [m]ens
    652: ('co', 'high', "the book's own vocabulary: _nceiue -> co:18", '#auto'),  # [co]nceiue
    653: ('m', 'high', 'by hand: they learne them [m]eerely by rote', '#editor'),  # [m]eerely
    654: ('bu', 'high', 'by hand: [bu]t afterwards come to make very good vse of them', '#editor'),  # [bu]t
    655: ('fore', 'high', 'by hand: Where[fore] children are to be instructed betimes', '#editor'),  # Where[fore]
    656: ('cr', 'high', 'by hand: as corne is sowne in winter to receiue [cr]op', '#editor'),  # [cr]op
    657: ('the', 'high', 'by hand: against [the]ir minde', '#editor'),  # [the]ir
    658: ('n', 'high', 'by hand: his father taught him eue[n] while he was tender', '#editor'),  # eue[n]
    659: ('s', 'high', 'by hand: the smart of neglecting hi[s] other children', '#editor'),  # hi[s]
    664: ('n', 'high', 'by hand: more peruersenesse and vntowardnesse i[n] such parents', '#editor'),  # i[n]
    665: ('u', 'high', 'by hand: illos & seipsum [u]na perdidit (Chrys. in 1 Tim. hom. 9)', '#editor'),  # [u]na
    666: ('', 'high', 'by hand: therein, he brought destruction -- the bullet is a blot', '#editor'),  # []he
    667: ('l', 'high', 'by hand: who are [l]oth to giue them a foule word', '#editor'),  # [l]oth
    668: ('e', 'medium', "the book's own vocabulary: _very -> e:3", '#auto'),  # [e]very
    669: ('n', 'medium', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3", '#auto'),  # [n]ot
    670: ('a', 'medium', "the book's own vocabulary: Ch_sten -> a:1", '#auto'),  # Ch[a]sten
    671: ('e', 'high', 'by hand: semetipsos in furorem iudicij dem[e]rgunt (Orig. in Iob)', '#editor'),  # dem[e]rgunt
    672: ('e', 'medium', "the book's own vocabulary: d_inceps -> e:1", '#auto'),  # d[e]inceps
    673: ('a', 'medium', "the book's own vocabulary: _nd -> a:8820, e:132", '#auto'),  # [a]nd
    674: ('v', 'high', 'by hand: to be of little [v]se', '#editor'),  # [v]se
    675: ('fit', 'high', 'by hand: though children be neuer so [fit] for these callings', '#editor'),  # [fit]
    676: ('n', 'high', 'by hand: God hath placed such a[n] one in his place', '#editor'),  # a[n]
    677: ('ir', 'medium', "the book's own vocabulary: the_ -> ir:4253, re:557, se:525, ss:6", '#auto'),  # the[ir]
    678: ('t', 'high', 'by hand: Ma[t]. 6. 19. expounded', '#editor'),  # Ma[t]
    688: ('et', 'high', "the book's own vocabulary: comp_ent -> et:6 (auto(2 letters))", '#auto'),  # comp[et]ent
    689: ('in', 'high', 'by hand: [in] case God take them away', '#editor'),  # [in]n
    690: ('u', 'medium', "the book's own vocabulary: pro_ided -> u:36, v:1", '#auto'),  # pro[u]ided
    691: ('ll', 'high', 'by hand: as a[ll] their care is to aduance their eldest sonne', '#editor'),  # a[ll]
    692: ('n', 'high', 'by hand: and i[n] the meane while neglect their younger children', '#editor'),  # i[n]
    695: ('n', 'medium', "the book's own vocabulary: _iggardly -> n:2", '#auto'),  # [n]iggardly
    696: ('x', 'high', 'by hand: ...phrontisteria... constru[x]it (Niceph. eccl. hist.)', '#editor'),  # constru[x]
    697: ('h', 'high', "the book's own vocabulary: _eauen -> h:117", '#auto'),  # [h]eauen
    701: ('l', 'high', 'by hand: the seruants of Lidia, and of the Iay[l]er', '#editor'),  # Iay[l]er
    714: ('d', 'medium', "the book's own vocabulary: _ominus -> d:4", '#auto'),  # [d]ominus
    715: ('t', 'high', 'by hand: vt fra[t]rem propter fidei societatem (Constit. Apost.)', '#editor'),  # fra[t]rem
    716: ('n', 'medium', "the book's own vocabulary: Se_ec -> n:3", '#auto'),  # Se[n]ec
    717: ('tuum', 'high', 'by hand: istum quem seruum [tuum] vocas (Seneca, Ep. 47)', '#editor'),  # [tuum]
    718: ('r', 'high', 'by hand: the errata list: "ibid. in ma[r]g. l. 8." (in the margin)', '#editor'),  # ma[r]g
}
