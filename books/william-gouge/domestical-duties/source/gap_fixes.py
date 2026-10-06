"""Illegible gaps filled for this edition, keyed by the TEI pipeline's gap
index (build_tei.py --list). Carried over from the earlier Gouge converter
(sources/gap_resolver.py): "#editor" entries were read by hand from context
or from the work cited; "#auto" ones were matched against the book's own
vocabulary (its most frequent word of that shape). An empty fill means there
was no missing letter: a blot or a broken space."""

GAP_FIXES = {
    0: ('πρότερον καὶ ἀναγκαιότερον οἰκία πόλεως', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n3): Ep. Ded. margin by 'Church and Commonwealth'; Arist. EN 8.12 (1162a18); καὶ printed as ϗ compendium", '#editor'),  # πρότερον καὶ ἀναγκαιότερον οἰκία πόλεως
    1: ('Μακρολόγος ἔστιν ὁ περὶ ὀλίγων πολλὰ λέγων. Πολυλόγος ὁ περὶ πολλῶν πολλά', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n4): Ep. Ded. top margin before 'Ammon.'; accent on first περὶ ambiguous (acute/grave)", '#editor'),  # Μακρολόγος ἔστιν ὁ περὶ ὀλίγων πολλὰ λέγων. Πολυλόγος ὁ περὶ πολλῶν πολλά
    2: ('παρ’ ἄλληλα τὰ ἐναντία μάλιστα φαίνεται', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n4): margin by 'contraries laid together'; Arist. Rhet. 3.2; παρ ligature then ἄλληλα (could be read as one word παράλληλα); φαίνεται with ται ligature", '#editor'),  # παρ’ ἄλληλα τὰ ἐναντία μάλιστα φαίνεται
    3: ('μισογύνης', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n6): margin '* μισογύνης. Athen.' keyed to 'an hater of women'", '#editor'),  # μισογύνης
    4: ('e', 'high', "the book's own vocabulary: f_are -> e:298", '#auto'),  # f[e]are
    5: ('t', 'high', "the book's own vocabulary: s_ealing -> t:4; confirmed on the 1622 page image (n19)", '#auto'),  # s[t]ealing
    6: ('ὑποτασσόμενοι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n25): p.2 margin 'ὑποτασσόμενοι, submitting.' Eph 5:21", '#editor'),  # ὑποτασσόμενοι
    7: ('ὑποτάσσεσθε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n25): p.2 margin 'ὑποτάσσεσθε, submit.' Eph 5:22", '#editor'),  # ὑποτάσσεσθε
    8: ('ἀλλήλοις', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n27): p.4 margin below '2. Doct.'", '#editor'),  # ἀλλήλοις
    9: ('διάκονος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n28): p.5 margin above 'Rom.13.4.'", '#editor'),  # διάκονος
    10: ('οὐθὲν μάτην ἡ φύσις ποιεῖ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n40): p.17 margin before 'Arist. Polit. lib.1'; ου ligature, μάτην with ην ligature", '#editor'),  # οὐθὲν μάτην ἡ φύσις ποιεῖ
    11: ('ὑποτάσσεσθε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n51): p.26 margin note p, keyed to 'THe p word'", '#editor'),  # ὑποτάσσεσθε
    12: ('ἰδίοις', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n52): p.27 margin '* ἰδίοις.' keyed to '( * owne )'", '#editor'),  # ἰδίοις
    13: ('τὸν ἴδιον ἄνδρα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n52): p.27 margin after '1 Cor.7.2.', before 'See §.82,83.'", '#editor'),  # τὸν ἴδιον ἄνδρα
    14: ('οἱ ἄνδρες. αἱ γυναῖκες', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n53): p.28 margin '* οἱ ἄνδρες. αἱ γυναῖκες.' keyed to 'men*' and women (one note, both words)", '#editor'),  # οἱ ἄνδρες. αἱ γυναῖκες
    15: ('ὡς', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n55): p.30 margin '* ὡς.' keyed to '( * euen as )'", '#editor'),  # ὡς
    16: ('ὥσπερ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n56): p.31 margin note ſ keyed to Manner ( ſ as )', '#editor'),  # ὥσπερ
    17: ('ἐν παντί', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n56): p.31 margin '* ἐν παντί.' keyed to '( * in euery thing )'", '#editor'),  # ἐν παντί
    18: ('καὶ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n59): p.34 margin above '1. Obser.', ϗ compendium with grave, by 'The copulatiue particle (AND)'", '#editor'),  # καὶ
    19: ('σωτὴρ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n60): p.35 margin '* σωτὴρ.' before 'Sotera inscriptum...'", '#editor'),  # σωτὴρ
    20: ('σώζειν εἰς τὸ παντελὲς δύναται', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n60): p.35 margin after '* Heb.7.25.'; printed σώζειν (no iota subscript), δύναται with ται ligature", '#editor'),  # σώζειν εἰς τὸ παντελὲς δύναται
    21: ('αὐτὸς', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n61): p.36 margin '* αὐτὸς.' keyed to '( * HEE)'", '#editor'),  # αὐτὸς
    22: ('ἐκκλησία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n63): p.38 margin before 'Ecclesia ex vocatione...'", '#editor'),  # ἐκκλησία
    23: ('ἑαυτῶν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n69): p.44 margin '* ἑαυτῶν.' keyed to 'their * owne Wiues' (Eph 5:28)", '#editor'),  # ἑαυτῶν
    24: ('ἰδίοις', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n69): p.44 margin '“ ἰδίοις.' keyed to 'their “ owne Husbands'", '#editor'),  # ἰδίοις
    25: ('ἑαυτοῦ. ἴδιον', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n69): p.44 margin '* ἑαυτοῦ. ἴδιον. See §.82.' keyed to 'Where * these two words' (1 Cor 7:2); one note, both words", '#editor'),  # ἑαυτοῦ. ἴδιον
    26: ('καθὼς', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n69): p.44 margin '* καθὼς.' keyed to '( * Euen as )'", '#editor'),  # καθὼς
    27: ('παρέδωκεν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n72): p.47 margin '* παρέδωκεν.' keyed to 'The * Greeke word' (Eph 5:25)", '#editor'),  # παρέδωκεν
    28: ('ἀρχηγὸς τῆς ζωῆς', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n73): p.48 margin after 'k Acts 3.15.'", '#editor'),  # ἀρχηγὸς τῆς ζωῆς
    29: ('ἀσυγχύτως. ἀτρέπτως. ἀδιαιρέτως. ἀχωρίστως', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n74): p.49 margin '*' note before 'Symbol. Calced.', four adverbs one per line, matching 'without confusion, alteration, distraction, separation'; stop after the first may be ';'", '#editor'),  # ἀσυγχύτως. ἀτρέπτως. ἀδιαιρέτως. ἀχωρίστως
    30: ('διὸ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n76): p.51 margin under 'Phil.2.9.' (WHEREFORE)", '#editor'),  # διὸ
    31: ('καθαρίσας', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n77): p.52 margin '* καθαρίσας. See §.39.' keyed to '* hauing cleansed it'", '#editor'),  # καθαρίσας
    32: ('ἵνα ἁγιάσῃ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n79): p.54 margin '* ἵνα ἁγιάσῃ.' keyed to '* THAT'; breathing on α smudged (rough per Eph 5:26), iota subscript printed", '#editor'),  # ἵνα ἁγιάσῃ
    33: ('καθαρίσας', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n83): p.58 margin '* καθαρίσας.' keyed to '* hauing cleansed it'", '#editor'),  # καθαρίσας
    34: ('e', 'high', 'by hand: O wretched m[e]n that we are', '#editor'),  # m[e]n
    35: ('i', 'high', "the book's own vocabulary: d_ebus -> i:1; confirmed on the 1622 page image (n89)", '#auto'),  # d[i]ebus
    36: ('h', 'high', "read from the 1622 page image (n89), replacing the guess 'it': Image shows 'Paſc!a': the surviving stroke is the ascender of an italic h, and the 'a' after it is the end of the same word: 'Paſcha' (praeterquam in Pascha & Pentecoste). Not 'Paſcit a'; the TCP's space before 'a' is the broken h, so the word is Paſcha (no space).", '#editor'),  # Pasc[it]
    37: ('n', 'high', 'by hand: L.L. Pipi[n]i (the Frankish Leges Pipini), Carol. M.', '#editor'),  # Pipi[n]
    38: ('t', 'high', 'by hand: Qui diem obij[t] antequam baptisaretur', '#editor'),  # obij[t]
    39: ('h', 'medium', "read from the 1622 page image (n89), replacing the guess '': Note e reads 'Ex opere operato, R[h]em. loc. citat.': an ascender (h) shows before an ink blot, then 'em.'. The TCP's 'B' looks like the italic R of 'Rhem.' in note d just above ('d Rhem. annot. on Ioh.3.5.'), which is what 'loc. citat.' points back to. So the word is 'Rhem.' (the Rhemists), not Bellarmine: fill 'h' and read the first letter as R.", '#editor'),  # B[]
    40: ('παραστήσῃ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n95): p.70 margin at foot by 'solemnizing'; Eph 5:27; opening παρ ligature faintly inked, rest clear (iota subscript printed)", '#editor'),  # παραστήσῃ
    41: ('ἔνδοξον', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n97): p.72 margin under 'Doctr.' by 'glorious'", '#editor'),  # ἔνδοξον
    42: ('ἄρρητα ῥήματα ἃ οὐκ ἐξὸν ἀνθρώπῳ λαλῆσαι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n98): p.73 margin after 'p 2 Cor.12.4.'; printed ἄῤῥητα (old ρρ breathings normalized), οὐκ as ου ligature", '#editor'),  # ἄρρητα ῥήματα ἃ οὐκ ἐξὸν ἀνθρώπῳ λαλῆσαι
    43: ('καθ’ ὑπερβολὴν εἰς ὑπερβολὴν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n98): p.73 margin '*' after 'q 2 Cor.4.17.', keyed to '* a farre more exceeding'", '#editor'),  # καθ’ ὑπερβολὴν εἰς ὑπερβολὴν
    44: ('ὡς περικαθάρματα τοῦ κόσμου, πάντων περίψημα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n98): p.73 margin after 's 1 Cor.4.13.'", '#editor'),  # ὡς περικαθάρματα τοῦ κόσμου, πάντων περίψημα
    45: ('ψίλος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n98): p.73 margin '* ψίλος.' keyed to '*spot'; first letter clearly printed ψ: a printer's misprint for σπίλος (Eph 5:27), transcribed as printed", '#editor'),  # ψίλος
    46: ('ῥύτις', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n98): p.73 margin '* ῥύτις.' keyed to '( * wrinkle )'; accent printed on υ (critical text ῥυτίς)", '#editor'),  # ῥύτις
    47: ('ἤ τι τῶν τοιούτων', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n98): p.73 margin by 'or any such thing'; Eph 5:27", '#editor'),  # ἤ τι τῶν τοιούτων
    48: ('ἀλλά', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n99): p.74 margin '* ἀλλά.' keyed to adversative particle (BVT)", '#editor'),  # ἀλλά
    49: ('ἄμωμος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n99): p.74 margin '* ἄμωμος.' keyed to '* without blemish'", '#editor'),  # ἄμωμος
    50: ('ἐκτρέφει', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n103): p.78 margin, first of two words after Aug. note, by 'To nourish' (Eph 5:29); printed with τρ ligature", '#editor'),  # ἐκτρέφει
    51: ('θάλπει', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n103): p.78 margin, second word before 'Proprie dicitur de galina...', by 'To cherish'", '#editor'),  # θάλπει
    52: ('e', 'high', "the book's own vocabulary: Summ_ -> e:15, o:1, a:1; confirmed on the 1622 page image (n104)", '#auto'),  # Summ[e]
    53: ('', 'high', 'by hand: a lost section number in a marginal cross-reference', '#editor'),  # []
    54: ('ἄστοργοι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n105): p.80 margin '* ἄστοργοι.' keyed to '* without naturall affection', then Rom.1.30", '#editor'),  # ἄστοργοι
    55: ('φιλόστοργοι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n105): p.80 margin '* φιλόστοργοι' after 'b Rom. 12.10', keyed to 'as * we are'; no stop visible", '#editor'),  # φιλόστοργοι
    56: ('u', 'high', 'by hand: nam a[u]arus (Aug. de doctr. Chr. 1. 25)', '#editor'),  # a[u]arus
    57: ('φιλαυτία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n108): p.83 margin '* φιλαυτία.' keyed to '* Selfe-loue'", '#editor'),  # φιλαυτία
    58: ('ἐσμὲν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n118): p.93 margin before 'Paul ranketh himselfe...', by 'We are ]'", '#editor'),  # ἐσμὲν
    59: ('τοῦ σώματος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n119): p.94 margin note e, keyed to '( e OF his body )'", '#editor'),  # τοῦ σώματος
    60: ('ἐκ τῆς σαρκὸς. ἐκ τῶν ὀστέων', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n119): p.94 margin note f (two lines), keyed to 'OF f his flesh; and OF his bones'; τῆς/τῶν printed as τ with abbreviation mark", '#editor'),  # ἐκ τῆς σαρκὸς. ἐκ τῶν ὀστέων
    61: ('ἐξ οὗ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n119): p.94 margin under 'i Eph.4.16.' (From whom)", '#editor'),  # ἐξ οὗ
    62: ('ἐκ σπέρματος Δαβὶδ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n120): p.95 margin after 'f 2 Tim.2.8.'; print slightly smudged but clear", '#editor'),  # ἐκ σπέρματος Δαβὶδ
    63: ('ἐξ ὧν ὁ Χριστὸς τὸ κατὰ σάρκα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n120): p.95 margin after 'g Rom.9.5.'; κατὰ printed as compendium", '#editor'),  # ἐξ ὧν ὁ Χριστὸς τὸ κατὰ σάρκα
    64: ('e', 'high', "the book's own vocabulary: ar_ -> e:2300, t:12, s:1; confirmed on the 1622 page image (n122)", '#auto'),  # ar[e]
    65: ('εἴ τις ἐν Χριστῷ, καινὴ κτίσις', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n130): p.105 margin after '2 Cor.5.17.' (two lines); εἴ τις set close, almost as one word", '#editor'),  # εἴ τις ἐν Χριστῷ, καινὴ κτίσις
    66: ('αὐτοῦ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n131): p.106 margin by 'This relatiue particle (HIS) twice repeated'; breathing printed over α", '#editor'),  # αὐτοῦ
    67: ('ἄνωθεν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n132): p.107 margin '* ἄνωθεν. Ioh.3.3.' keyed to '* from aboue'", '#editor'),  # ἄνωθεν
    68: ('ἐκ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n133): p.108 margin by 'The preposition (OF) twice set downe'", '#editor'),  # ἐκ
    69: ('ἐξ οὗ πᾶν τὸ σῶμα ἐπιχορηγούμενον αὔξει τὴν αὔξησιν τοῦ Θεοῦ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n133): p.108 margin after 'a Col.2.19.', six lines; Gouge's abridgement of Col 2:19, as printed", '#editor'),  # ἐξ οὗ πᾶν τὸ σῶμα ἐπιχορηγούμενον αὔξει τὴν αὔξησιν τοῦ Θεοῦ
    70: ('ἀντὶ τούτου', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n135): p.110 margin by '(for this cause)'; Eph 5:31", '#editor'),  # ἀντὶ τούτου
    71: ('προσκολληθήσεται. κόλλα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n137): p.112 top margin 'προσκολληθήσεται. κόλλα. Glue.' (Glue already in TCP); προσ in ligature", '#editor'),  # προσκολληθήσεται. κόλλα
    72: ('ἔσονται οἱ δύο εἰς σάρκα μίαν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n137): margin by 'they two shall be one flesh', p.112; Gen 2:24/Eph 5:31", '#editor'),  # ἔσονται οἱ δύο εἰς σάρκα μίαν
    73: ('οἱ δύο', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n137): margin by 'this particle THEY (they two)', p.112", '#editor'),  # οἱ δύο
    74: ('a', 'high', 'by hand: itaque duceb[a]tur in domum sponsi (Erasmus, Adagia)', '#editor'),  # duceb[a]tur
    75: ('c', 'high', 'by hand: nes[c]iret redeundi viam ad aedes parentum', '#editor'),  # nes[c]iret
    76: ('εἰς σάρκα μίαν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n141): margin note * keyed to 'come * into one flesh', foot of p.116", '#editor'),  # εἰς σάρκα μίαν
    77: ('πλὴν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n153): margin by 'Neverthelesse', p.128; ην ligature with grave; Eph 5:33", '#editor'),  # πλὴν
    78: ('ὑμεῖς οἱ καθ’ ἕνα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n154): margin by 'Every one of you in particular', p.129; Eph 5:33", '#editor'),  # ὑμεῖς οἱ καθ’ ἕνα
    79: ('τὰ τέκνα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n157): margin by 'The first word (children)', p.132", '#editor'),  # τὰ τέκνα
    80: ('οἱ γόνεις', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n157): margin by 'word (parents)', p.132; acute printed over the omicron and no visible circumflex on the ει ligature (standard οἱ γονεῖς)", '#editor'),  # οἱ γόνεις
    81: ('τὰ τέκνα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n158): margin under '* Treat. 5. §. 56, 57, &c.', by 'children ... neuter gender', p.133", '#editor'),  # τὰ τέκνα
    82: ('τοῖς γονεῦσι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n158): margin by 'He expresseth parents in the plurall', p.133; ευ ligature, its accent not clearly visible", '#editor'),  # τοῖς γονεῦσι
    83: ('ὑμῶν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n158): margin by 'relatiue particle your', p.133; ων ligature", '#editor'),  # ὑμῶν
    84: ('ὑπακούετε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n158): margin by 'The word (Obey)', p.133; Eph 6:1", '#editor'),  # ὑπακούετε
    85: ('ἀκούειν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n158): margin '* ἀκούειν' keyed to 'the * verbe', p.133; ου ligature", '#editor'),  # ἀκούειν
    86: ('ὑπὸ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n158): margin '* ὑπὸ' keyed to 'the * preposition', p.133; ὑπ ligature, grave", '#editor'),  # ὑπὸ
    87: ('ἐν Κυρίῳ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n159): margin by 'The clause added (in the Lord)', p.134; iota subscript printed; Eph 6:1", '#editor'),  # ἐν Κυρίῳ
    88: ('τοῦτο γάρ ἐστι δίκαιον', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n159): margin by '(for this is right)', p.134; ου and εστι ligatures; Eph 6:1", '#editor'),  # τοῦτο γάρ ἐστι δίκαιον
    89: ('ἐντολὴ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n161): margin by 'The * word here vsed', p.136", '#editor'),  # ἐντολὴ
    90: ('ἵνα εὖ σοι γένηται', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n165): margin by 'that it may be well with thee', p.140; γένηται set with ligatures; Eph 6:3", '#editor'),  # ἵνα εὖ σοι γένηται
    91: ('θεοστυγεῖς', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n166): margin '* θεοστυγεῖς' keyed to 'such as are * haters of God', p.141; στ ligature; Rom 1:30", '#editor'),  # θεοστυγεῖς
    92: ('φιλόθεοι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n166): margin '* φιλόθεοι' keyed to 'such as are * loued of him', p.141", '#editor'),  # φιλόθεοι
    93: ('יארכון', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n171): Hebrew, unpointed, margin by 'they shall prolong thy daies', p.146; Exod 20:12 יַאֲרִכוּן; the 4th letter is squarish (could pass for ב) and the 5th wider than a usual vav, read as כ and ו from the verse", '#editor'),  # יארכון
    94: ('צבח', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n176): Hebrew, unpointed, margin by 'him that hath his time appointed for warfare', p.151; clearly printed צבח (last letter ח, legs joined at top), for צבא of Job 7:1 — likely a misprint; use צבא if correcting", '#editor'),  # צבח
    95: ('πατέρες', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n179): margin by 'the word (Fathers)', p.154; accent on ε a blot, acute assumed", '#editor'),  # πατέρες
    96: ('παροργίζετε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n180): margin by 'the exposition of one Greeke word', p.155; Eph 6:4", '#editor'),  # παροργίζετε
    97: ('ἀλλὰ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n181): margin by 'the Apostle addeth a BVT', p.156", '#editor'),  # ἀλλὰ
    98: ('s', 'high', 'by hand: such mischiefes a[s] children may fall into', '#editor'),  # a[s]
    99: ('ἐκτρέφετε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n181): margin at foot of p.156, by 'The word translated (bring vp)'; Eph 6:4", '#editor'),  # ἐκτρέφετε
    100: ('ἐκτρέφει', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n182): margin top of p.157 above 'Enutrite, Beza'; Eph 5:29 (word 'there translated nourisheth')", '#editor'),  # ἐκτρέφει
    101: ('ἐκτρέφετε αὐτὰ ἐν παιδείᾳ. ἐκτρέφετε καὶ παιδεύετε αὐτὰ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n182): margin under '4. Obseru. Parents to prouide all needfull things for children.', p.157; two Greek lines in one run (καὶ printed as ϗ ligature, last αὐτὰ with grave as printed)", '#editor'),  # ἐκτρέφετε αὐτὰ ἐν παιδείᾳ. ἐκτρέφετε καὶ παιδεύετε αὐτὰ
    102: ('παιδεία. εἰ παιδείαν ὑπομένετε. πρὸς παιδείαν τὴν ἐν δικαιοσύνῃ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n182): margin under '5. Obseru.', p.157; Heb 12:7 and 2 Tim 3:16 as cited in the text; one Greek run", '#editor'),  # παιδεία. εἰ παιδείαν ὑπομένετε. πρὸς παιδείαν τὴν ἐν δικαιοσύνῃ
    103: ('παιδεία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n182): margin under '6. Obseru.', p.157 (the note's first Greek line; the next, '* παιδεύειν', is gap 104)", '#editor'),  # παιδεία
    104: ('παιδεύειν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n182): margin '* παιδεύειν, Instituere vt puerili aetati conuenit', keyed to 'according to the * Greeke notation', p.157", '#editor'),  # παιδεύειν
    105: ('νουθεσία. νουθετεῖν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n183): margin p.158 by 'This word (admonition) according to the * notation': two lines 'νουθεσία.' and '* νουθετεῖν, menti indere.'; the TCP made the * the note's n, so it is left out here", '#editor'),  # νουθεσία. νουθετεῖν
    106: ('μετὰ μίαν καὶ δευτέραν νουθεσίαν', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n183): margin note a, p.158; Tit 3:10; μετὰ printed as contraction (μ with τ and grave above), καὶ as ϗ', '#editor'),  # μετὰ μίαν καὶ δευτέραν νουθεσίαν
    107: ('νουθετεῖν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n183): margin under '7. Obseru.', p.158", '#editor'),  # νουθετεῖν
    108: ('שנן', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n183): Hebrew, unpointed, margin note d 'Doctus inter Hebr. vocem שנן continuò loqui exponit', p.158; root of Deut 6:7 וְשִׁנַּנְתָּם", '#editor'),  # שנן
    109: ('Κυρίου', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n184): margin by 'The last word (of the Lord)', p.159; ου ligature", '#editor'),  # Κυρίου
    110: ('οἱ δοῦλοι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n185): margin by 'This title (Seruants)', p.160; Eph 6:5", '#editor'),  # οἱ δοῦλοι
    111: ('ap', 'high', 'by hand: Vide [ap]ud Viu[es]. ibid.', '#editor'),  # [ap]ud
    112: ('τοῖς κυρίοις', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n185): margin 'τοῖς κυρίοις. What masters are meant', p.160; Eph 6:5", '#editor'),  # τοῖς κυρίοις
    113: ('ὑπακούετε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n186): margin by 'Vnder this word (obey)', p.161", '#editor'),  # ὑπακούετε
    114: ('κατὰ σάρκα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n186): margin under '6. Obseru.' by 'This clause (according to the flesh)', p.161; κατὰ printed as contraction κ with τ and grave", '#editor'),  # κατὰ σάρκα
    115: ('μετὰ φόβου, καὶ τρόμου', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n187): margin 'Seruants feare of their masters.' then the Greek, p.162; μετὰ contracted, καὶ as ϗ; Eph 6:5", '#editor'),  # μετὰ φόβου, καὶ τρόμου
    116: ('φόβος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n188): margin '* φόβος. Vers. 33.' keyed to '* Feare', p.163", '#editor'),  # φόβος
    117: ('τρόμος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n188): margin '* τρόμος' keyed to '* Trembling', p.163", '#editor'),  # τρόμος
    118: ('ἐν ἁπλότητι τῆς καρδίας ὑμῶν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n188): margin by 'in singlenesse of heart', p.163; Eph 6:5; breathing on ἁπλότητι not clearly visible", '#editor'),  # ἐν ἁπλότητι τῆς καρδίας ὑμῶν
    119: ('ὡς τῷ Χριστῷ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n189): margin under '1 Sam. 16. 7.' by 'clause, as vnto Christ', p.164; Eph 6:5", '#editor'),  # ὡς τῷ Χριστῷ
    120: ('ὀφθαλμοδουλεία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n189): margin under '11. Obser.' at foot of p.164 (ὀφθαλμοδου-|λεία), by 'is termed eie-seruice'", '#editor'),  # ὀφθαλμοδουλεία
    121: ('ἀνθρωπάρεσκοι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n190): margin 'Men pleasers.' then the Greek, p.165; Eph 6:6", '#editor'),  # ἀνθρωπάρεσκοι
    122: ('εὐαρέστους εἶναι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n191): margin '* εὐαρέστους εἶ(ναι)' keyed to 'to * please well', p.166; Tit 2:9; ναι printed as an abbreviation sign after εἶ", '#editor'),  # εὐαρέστους εἶναι
    123: ('δοῦλοι τοῦ Χριστοῦ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n191): margin 'δοῦλοι τοῦ Χριστοῦ. Who are seruants of Christ.', p.166; Eph 6:6", '#editor'),  # δοῦλοι τοῦ Χριστοῦ
    124: ('μετ’ εὐνοίας', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n193): margin by 'as the notation of the Greeke word sheweth', p.168; Eph 6:7", '#editor'),  # μετ’ εὐνοίας
    125: ('δουλεύοντες', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n193): margin by 'namely this (doing seruice)', p.168; Eph 6:7", '#editor'),  # δουλεύοντες
    126: ('ὑπακούετε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n193): margin note a, keyed to '(a obey)', p.168", '#editor'),  # ὑπακούετε
    127: ('δουλεύοντες', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n193): margin note b, keyed to '(b doing seruice)', p.168", '#editor'),  # δουλεύοντες
    128: ('δοῦλος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n193): margin note c, keyed to 'title of a c seruant', p.168; ος ligature, accent on ου not visible", '#editor'),  # δοῦλος
    129: ('ὡς τῷ κυρίῳ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n193): margin by 'The clause annexed (as to the Lord)', p.168; Eph 6:7", '#editor'),  # ὡς τῷ κυρίῳ
    130: ('εἰδότες', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n195): margin under '20. Obser.' by '(Knowing)', p.170; Eph 6:8", '#editor'),  # εἰδότες
    131: ('τοῦτο κομιεῖται', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n195): margin by '(the same shall he receiue)', p.170; -ται printed as abbreviation; Eph 6:8", '#editor'),  # τοῦτο κομιεῖται
    132: ('τοῦτο καὶ θερίσει', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n195): margin note o, under 'Gal. 6. 7.', p.170 (τοῦτο καὶ θε-|ρίσει; καὶ as ϗ); the 'o' is the TCP note's n", '#editor'),  # τοῦτο καὶ θερίσει
    133: ('παρὰ τοῦ Κυρίου', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n196): margin top of p.171 (Κυ-|ρίου) by 'Of the Lord: for it is the Lord that'; παρὰ set as the old πα-ρ ligature with grave; Eph 6:8", '#editor'),  # παρὰ τοῦ Κυρίου
    134: ('τὰ αὐτὰ ποιεῖτε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n197): margin under '* §. 124.' by 'doe the same things', p.172 (ποι-|εῖτε); Eph 6:9", '#editor'),  # τὰ αὐτὰ ποιεῖτε
    135: ('ἀνιέντες τὴν ἀπειλὴν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n199): margin top of p.174 by '(forbearing threatning)'; Eph 6:9; accent on ἀνιέντες sits between ι and ε, final grave on ἀπειλὴν as printed", '#editor'),  # ἀνιέντες τὴν ἀπειλὴν
    136: ('εἰδότες', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n200): p.175 margin beside 'knowing' (Eph 6:9 εἰδότες); breathing faint", '#editor'),  # εἰδότες
    137: ('καὶ ὑμῶν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n200): p.175 margin by 'your also'; καὶ as the ϗ ligature", '#editor'),  # καὶ ὑμῶν
    138: ('καὶ ὑμῶν, καὶ αὐτῶν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n200): p.175 margin, two lines, by 'both your and their master' (Eph 6:9 variant); καὶ as ϗ ligature", '#editor'),  # καὶ ὑμῶν, καὶ αὐτῶν
    139: ('κατ᾽ ἐξοχήν', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n201): p.176 margin note *; ἐξοχὴν/ήν accent on the ην ligature not distinguishable, standard acute given', '#editor'),  # κατ᾽ ἐξοχήν
    140: ('פנים', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n202): p.177 margin, unpointed Hebrew, followed by note letter 'a'", '#editor'),  # פנים
    141: ('πρόσωπον', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n202): p.177 margin note * under פנים', '#editor'),  # πρόσωπον
    142: ('ἐν πᾶσι', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n208): p.183 margin above Heb.13.4 (ἐν πᾶσι, printed without final ν)', '#editor'),  # ἐν πᾶσι
    143: ('C', 'medium', "read from the 1622 page image (n209), replacing the guess 'c': Faint first letter is cap-height (as tall as the l), the same shape as the C of 'Conuerſ.' above: 'ad Cler.' (De conversione ad Clericos). Letter c is right; the 1622 has it as a capital.", '#editor'),  # [c]ler
    144: ('c', 'high', "the book's own vocabulary: _itat -> c:12", '#auto'),  # [c]itat
    145: ('ta', 'high', 'by hand: secundas nuptias [ta]nquam supra damnare', '#editor'),  # [ta]nquam
    146: ('ſt', 'high', "read from the 1622 page image (n212), replacing the guess 's': Image shows ſ plus a short t stroke before 'upra': 'tanquam ſtupra damnare' (Tertullian condemned second marriages as fornications). 'supra' makes no sense here.", '#editor'),  # [s]upra
    147: ('ἧλιξ ἥλικα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n213): p.188 margin above 'Arist. Eth. l.8. c.12.' (proverb ἧλιξ ἥλικα [τέρπει]); accents read with the standard form, marks small", '#editor'),  # ἧλιξ ἥλικα
    148: ('e', 'high', "the book's own vocabulary: estat_ -> e:175", '#auto'),  # estat[e]
    149: ('i', 'high', "the book's own vocabulary: _nsult -> i:8", '#auto'),  # [i]nsult
    150: ('', 'high', 'pages 191-196, missing from the filmed copy: supplied from another 1622 copy (A68107.supplied.xml, revisionDesc #supplied-pages)', '#editor'),  # 6 pages missing
    151: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n226)", '#auto'),  # [a]nd
    152: ('S', 'high', 'by hand: [S]uch as the virgin Mary will be a good example', '#editor'),  # [S]uch
    153: ('so', 'high', "the book's own vocabulary: _brietie -> so:4 (auto(2 letters)); confirmed on the 1622 page image (n226)", '#auto'),  # [so]brietie
    154: ('g', 'high', "the book's own vocabulary: _ood -> g:1027, f:55, w:6, h:5; confirmed on the 1622 page image (n226)", '#auto'),  # [g]ood
    155: ('an', 'high', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232; confirmed on the 1622 page image (n226)", '#auto'),  # [an]d
    156: ('i', 'high', 'by hand: the precedency [i]s giuen to the younger', '#editor'),  # [i]s
    157: ('r', 'high', 'by hand: excellently deciphe[r]ed in Solomons Song', '#editor'),  # deciphe[r]ed
    158: ('διὰ τὴν ἐνεστῶσαν ἀνάγκην', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n230): p.211 margin note a under 1 Cor.7.26', '#editor'),  # διὰ τὴν ἐνεστῶσαν ἀνάγκην
    159: ('τὴν λύσιν ἐκεῖνος ποιεῖ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n234): p.215 margin above 'Phot. in 1 Cor.7.'", '#editor'),  # τὴν λύσιν ἐκεῖνος ποιεῖ
    160: ('ὄντως χήρα', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n235): p.216 margin note * above 1 Tim.5.5', '#editor'),  # ὄντως χήρα
    161: ('σχολάζητε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n236): p.217 margin note * (1 Cor 7:5), before 'Non dixit simpliciter'", '#editor'),  # σχολάζητε
    162: ('e', 'high', "the book's own vocabulary: H_b -> e:62, a:2; confirmed on the 1622 page image (n236)", '#auto'),  # H[e]b
    163: ('ἑαυτου. ἴδιον', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n236): p.217 margin after '1 Cor.7.2.': two words on two lines, ἑαυτοῦ printed without circumflex (TCP has the final '.' after the gap)", '#editor'),  # ἑαυτου. ἴδιον
    164: ('εὔνοια', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n241): p.222 margin note * (1 Cor 7:3); breathing+accent printed over ε, normalized to εὔνοια', '#editor'),  # εὔνοια
    165: ('ὀφειλομένη', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n241): p.222 margin note *, printed nominative ὀφειλομένη (text: ὀφειλομένην)', '#editor'),  # ὀφειλομένη
    166: ('e', 'high', "the book's own vocabulary: Io_l -> e:2; confirmed on the 1622 page image (n242)", '#auto'),  # Io[e]l
    167: ('b', 'high', 'by hand: the bridegroome and [b]ride goe out of their chamber', '#editor'),  # [b]ride
    168: ('b', 'high', 'by hand: in the time of a Fast it must [b]e forborne', '#editor'),  # [b]e
    169: ('m', 'high', "the book's own vocabulary: _eanes -> m:331", '#auto'),  # [m]eanes
    170: ('I', 'high', 'by hand: [I] will haue mercy, and not sacrifice (Hos. 6. 6)', '#editor'),  # [I]
    171: ('luſt', 'high', "read from the 1622 page image (n242), replacing the guess 'sacrifice': Line start lies in the gutter shadow, but 'ſt ?' is clearly printed, with the stub of a u stem before it: 'ſhall not mans or womans luſt? for ſo I may well terme this vnſeaſonable deſire'. Not 'sacrifice' (the TCP gap covers the whole word; the 'lu' is in the shadow).", '#editor'),  # [sacrifice]
    172: ('or', 'high', 'by hand: continue so long sicke, [or] otherwise weake', '#editor'),  # [or]
    173: ('o', 'high', "the book's own vocabulary: _wne -> o:496", '#auto'),  # [o]wne
    174: ('assu', 'high', "the book's own vocabulary: _redly -> assu:23 (auto(4 letters))", '#auto'),  # [assu]redly
    175: ('fro', 'high', 'by hand: what can be expected [fro]m such polluted copulation', '#editor'),  # [fro]m
    176: ('φιλάνδρους εἶναι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n244): p.225 margin above 'Tit.2.4.'", '#editor'),  # φιλάνδρους εἶναι
    177: ('μεριμνᾶν, quasi μερίζειν τὸν νοῦν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n248): p.229 margin under 1 Cor.7.33,34; the TCP note is a single gap, so the Latin 'quasi' is inside it; τὸν printed as abbreviated τ̀", '#editor'),  # μεριμνᾶν, quasi μερίζειν τὸν νοῦν
    178: ('יבן', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n249): p.230 margin above 'Vide Musc. in Gen.2.22.'; unpointed Hebrew (וַיִּבֶן 'he built', Gen 2:22)", '#editor'),  # יבן
    179: ('συνοικοῦντες. συνοικῶν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n249): p.230 margin note *: line '*συνοικοῦντες.' (1 Pet 3:7) then 'συνοικῶν coniux.'; the TCP note (n='*') has one gap before 'coniux', covering both words", '#editor'),  # συνοικοῦντες. συνοικῶν
    180: ('σύνοικος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n249): p.230 margin, 'σύνοικος uxor.'", '#editor'),  # σύνοικος
    181: ('a', 'high', "the book's own vocabulary: _re -> a:2300, e:2; confirmed on the 1622 page image (n252)", '#auto'),  # [a]re
    182: ('c', 'high', "the book's own vocabulary: Soli_iting -> c:1; confirmed on the 1622 page image (n252)", '#auto'),  # Soli[c]iting
    183: ('i', 'high', "read from the 1622 page image (n252), replacing the guess 'm': Line start at the gutter reads 'iuſt cauſe of diuorce', with the dotted i visible: 'it giueth iuſt cauſe of diuorce'. Not 'muſt'.", '#editor'),  # [m]ust
    184: ('u', 'high', "the book's own vocabulary: di_orce -> u:10", '#auto'),  # di[u]orce
    185: ('p', 'high', "the book's own vocabulary: com_laine -> p:15", '#auto'),  # com[p]laine
    186: ('t', 'high', "the book's own vocabulary: _he -> t:12236, s:713; confirmed on the 1622 page image (n252)", '#auto'),  # [t]he
    187: ('n', 'high', "the book's own vocabulary: ma_age -> n:8", '#auto'),  # ma[n]age
    188: ('ke', 'high', "the book's own vocabulary: pluc_d -> ke:1 (auto(2 letters)); confirmed on the 1622 page image (n252)", '#auto'),  # pluc[ke]d
    189: ('be', 'high', 'by hand: may sundry other wayes [be] applied', '#editor'),  # [be]
    190: ('b', 'high', 'by hand: by way of comparison to [b]e taken', '#editor'),  # [b]e
    191: ('m', 'high', "the book's own vocabulary: _any -> m:635", '#auto'),  # [m]any
    192: ('πάντοτε', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n254): p.235 margin note a above Luke 18.1', '#editor'),  # πάντοτε
    193: ('ἀδιαλείπτως', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n254): p.235 margin note b above 1 Thess.5.17', '#editor'),  # ἀδιαλείπτως
    194: ('e', 'high', "the book's own vocabulary: _ither -> e:109, w:1, h:1; confirmed on the 1622 page image (n254)", '#auto'),  # [e]ither
    195: ('', 'high', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words; confirmed on the 1622 page image (n256)', '#auto'),  # []rotten
    196: ('l', 'high', 'by hand: to carry away the goods and [l]ands', '#editor'),  # [l]ands
    197: ('συγκληρονόμοι χάριτος ζωῆς', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n258): p.239 margin under 1 Pet.3.7; accent on ζωῆς small, looks acute over ω, standard circumflex given', '#editor'),  # συγκληρονόμοι χάριτος ζωῆς
    198: ('', 'high', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words; confirmed on the 1622 page image (n258)', '#auto'),  # []edifie
    199: ('ἵνα κερδηθήσονται', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n258): p.239 margin under 1 Pet.3.1', '#editor'),  # ἵνα κερδηθήσονται
    200: ('b', 'high', 'by hand: two that were in one [b]ed together', '#editor'),  # [b]ed
    201: ('o', 'high', "the book's own vocabulary: _ne -> o:990", '#auto'),  # [o]ne
    202: ('c', 'high', "the book's own vocabulary: _ouple -> c:14", '#auto'),  # [c]ouple
    203: ('ἀνθρωπάρεσκοι', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n263): p.244 margin under Eph.6.6', '#editor'),  # ἀνθρωπάρεσκοι
    204: ('h', 'high', 'by hand: when [h]e obserued her to be with childe', '#editor'),  # [h]e
    205: ('f', 'high', "the book's own vocabulary: _or -> f:2960, n:228, c:196, h:2; confirmed on the 1622 page image (n266)", '#auto'),  # [f]or
    206: ('παραδειγματίσαι αὐτὴν', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n266): p.247 margin note b (Matt 1:19), printed in this order, αὐτὴν with grave', '#editor'),  # παραδειγματίσαι αὐτὴν
    207: ('s', 'high', 'by hand: The [s]ame respect moued Bathsheba', '#editor'),  # [s]ame
    208: ('t', 'high', "read from the 1622 page image (n266), replacing the guess 'w': Gutter: first letter lost in the shadow; the print reads '?ell him that ſhe was with childe'. The sense, 'moued Bethſheba to ſend ſecretly to Dauid, and tell him' (2 Sam. 11.5), needs 'tell', not 'well'.", '#editor'),  # [w]ell
    209: ('ou', 'high', 'by hand: man and wife ought (the transcription reads "aght")', '#editor'),  # [ou]aght
    210: ('gr', 'high', 'by hand: and that on good [gr]ounds', '#editor'),  # [gr]ounds
    211: ('c', 'high', 'by hand: better then pre[c]ious ointment (Eccl. 7. 1)', '#editor'),  # pre[c]ious
    212: ('ab', 'high', "read from the 1622 page image (n266), replacing the guess 'l': Italic 'boue great riches' is clearly printed, with the edge of an a in the gutter: 'to be choſen aboue great riches' (Prov. 22.1). The TCP gap stands before 'oue', but the b survives in print, so the word is 'aboue', not 'loue'.", '#editor'),  # [l]oue
    213: ('t', 'high', "the book's own vocabulary: pra_e -> t:3; confirmed on the 1622 page image (n270)", '#auto'),  # pra[t]e
    214: ('r', 'high', "the book's own vocabulary: tho_owly -> r:4; confirmed on the 1622 page image (n272)", '#auto'),  # tho[r]owly
    215: ('ſ', 'high', "read from the 1622 page image (n272), replacing the guess 't': Gutter: first letter lost; 'he alſo is bound hereunto'. The subject is the wife ('whether ſhe be bound to take any care about the goods... proofe enough to ſhew that euen ſhe alſo is bound'), so the word is 'ſhe', not 'the'.", '#editor'),  # [t]he
    216: ('t', 'high', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10; confirmed on the 1622 page image (n272)", '#auto'),  # [t]o
    217: ('s', 'high', "the book's own vocabulary: mea_ure -> s:48", '#auto'),  # mea[s]ure
    218: ('d', 'high', "the book's own vocabulary: _icing -> d:2; confirmed on the 1622 page image (n274)", '#auto'),  # [d]icing
    219: ('o', 'high', 'by hand: Ios. 4. 15', '#editor'),  # J[o]s
    220: ('. 2', 'high', "read from the 1622 page image (n277), replacing the guess '': Margin note e reads 'Joſ. 24.15.': after the ſ there is a faint stop, then the top hook of a 2 just before '4.15'. So the gap holds a stop and the digit 2 (not 'no letter lost'), and the reference is Josh. 24.15 ('I and mine house will serve the Lord', fitting 'of Ioſuah' ruling his house), not Josh. 4.15.", '#editor'),  # Jos[]
    221: ('d', 'high', 'by hand: haue no helpe from you, [d]o not in those things', '#editor'),  # [d]o
    222: ('ὑποτάσσεσθε', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n286): p.267 margin note a (Eph 5:22), bottom of page', '#editor'),  # ὑποτάσσεσθε
    223: ('ἰδίοις', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n286): p.267 margin note b', '#editor'),  # ἰδίοις
    224: ('ἐν παντὶ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n287): p.268 margin note e 'ἐν παντὶ, In euerie thing'", '#editor'),  # ἐν παντὶ
    225: ('t', 'high', 'by hand: iustum est vt eum gubernatorem assuma[t] (Ambr. Hexaem.)', '#editor'),  # assuma[t]
    226: ('Κύριος', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n289): p.270 margin note c; smudged final letters, read Κύριος (1 Pet 3:6 κύριον αὐτὸν καλοῦσα)', '#editor'),  # Κύριος
    227: ('בעל', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n289): p.270 margin note d, unpointed Hebrew ba'al (Est 1:17 בַּעְלֵיהֶן)", '#editor'),  # בעל
    228: ('אלוף', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n289): p.270 margin note e, unpointed Hebrew (Prov 2:17 אַלּוּף)', '#editor'),  # אלוף
    229: ('κεφαλὴ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n289): p.270 margin note f, grave accent as printed', '#editor'),  # κεφαλὴ
    230: ('εἰκὼν καὶ δόξα Θεοῦ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n289): p.270 margin note g (1 Cor 11:7); καὶ printed as ϗ ligature; Θεοῦ circumflex blurred', '#editor'),  # εἰκὼν καὶ δόξα Θεοῦ
    231: ('συγκληρονόμοι', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n290): p.271 margin note e under '1 Pet.3.7.', hyphenated συγκληρονό-μοι", '#editor'),  # συγκληρονόμοι
    232: ('ἴδιοι', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n291): p.272 margin note b 'ἴδιοι. Eph.5.22,24.'; print clearly ends -οι (no ς), so not ἰδίοις as in the text of Eph 5:22", '#editor'),  # ἴδιοι
    233: ('i', 'high', "the book's own vocabulary: _mage -> i:58", '#auto'),  # [i]mage
    234: ('n', 'high', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3; confirmed on the 1622 page image (n292)", '#auto'),  # [n]ot
    235: ('v', 'high', "the book's own vocabulary: _assals -> v:2; confirmed on the 1622 page image (n292)", '#auto'),  # [v]assals
    236: ('a', 'high', "the book's own vocabulary: _rrogancy -> a:3; confirmed on the 1622 page image (n292)", '#auto'),  # [a]rrogancy
    237: ('m', 'high', "the book's own vocabulary: _ore -> m:914, s:10, f:4; confirmed on the 1622 page image (n292)", '#auto'),  # [m]ore
    238: ('m', 'high', "the book's own vocabulary: _ary -> m:38, c:1; confirmed on the 1622 page image (n292)", '#auto'),  # [m]ary
    239: ('φοβῆται', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n293): p.274 margin note b under Eph.5.33; circumflex over η blurred', '#editor'),  # φοβῆται
    240: ('ἐν φόβῳ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n293): p.274 margin note c under 1 Pet.3.2', '#editor'),  # ἐν φόβῳ
    241: ('i', 'high', 'by hand: so is [i]t a cause of many other vices', '#editor'),  # [i]t
    242: ('ἀναστροφὴν ἁγνὴν ἐν φόβῳ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n296): p.277 margin note c under 1 Pet.3.1 (word order as printed; ην ligature with grave); breathing on ἁγνὴν read as rough per the word', '#editor'),  # ἀναστροφὴν ἁγνὴν ἐν φόβῳ
    243: ('ἡσυχία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n301): p.282 margin note a '1 Tim.2.12. ἡσυχία.'; the print keys one note 'a' to both 'silence' and 'quietnesse', the TCP gives it twice (gaps 243 and 244)", '#editor'),  # ἡσυχία
    244: ('ἡσυχία', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n301): p.282, same note a as gap 243 (TCP duplicates the note)', '#editor'),  # ἡσυχία
    245: ('e', 'high', 'by hand: contracted thus, Iack[e], Tom, Will, Hall', '#editor'),  # Iack[e]
    246: ('ὑπήκουσε', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n305): p.286 margin note c under 1 Pet.3.6; ου as ȣ ligature', '#editor'),  # ὑπήκουσε
    247: ('f', 'high', 'by hand: to a very naturall, or a [f]renzy man', '#editor'),  # [f]renzy
    248: ('v', 'high', 'by hand: some rent, annuity, fees, [v]ailes, or the like', '#editor'),  # [v]ailes
    249: ('Παράφερνα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n310): p.291 margin (the TCP's [309,310] pair: p.291 is scan 310, the right page)", '#editor'),  # Παράφερνα
    250: ('τὰ ἐξώπροικα', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n310): p.291 margin 'dicuntur τὰ ἐξώπροικα'; an ink blot covers the π, read from the known legal term ἐξώπροικα (= paraphernalia)", '#editor'),  # τὰ ἐξώπροικα
    251: ('h', 'high', "the book's own vocabulary: _ard -> h:26, w:1, b:1; confirmed on the 1622 page image (n310)", '#auto'),  # [h]ard
    252: ('sh', 'high', 'by hand: to dispose as [sh]e please', '#editor'),  # [sh]e
    253: ('g', 'high', 'by hand: to order his [g]ift as he please', '#editor'),  # [g]ift
    254: ('fe', 'high', 'by hand: She is herein but as a [fe]offee in trust', '#editor'),  # [fe]offee
    255: ('st', 'high', 'by hand: other he reserueth for a [st]ocke', '#editor'),  # [st]ocke
    256: ('n', 'high', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3; confirmed on the 1622 page image (n310)", '#auto'),  # [n]ot
    257: ('b', 'high', "the book's own vocabulary: _ound -> b:105, f:19, s:18, w:8; confirmed on the 1622 page image (n310)", '#auto'),  # [b]ound
    258: ('οἰκοδεσποτεῖν', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n311): p.292 margin under 1 Tim.5.14', '#editor'),  # οἰκοδεσποτεῖν
    259: ('g', 'high', "the book's own vocabulary: Gre_ -> g:21, w:1; confirmed on the 1622 page image (n312)", '#auto'),  # Gre[g]
    260: ('', 'medium', 'by hand: a lost folio number in "Coke Rep. 4. 3 [?] 3."; the 1622 page image (n315) does not settle it: Margin note h: \'Coke Rep. 4.\' then \'3 ε ;. Deu. 12.\' The gap glyph is a broken figure shaped like ε, which could be the left half of an 8, giving \'38\'. The next mark could be a damaged 3 or b. The print is too damaged to read with confidence. Ognel\'s Case is usually cited as 4 Co. Rep. 48b; that would need the first figure to be a 4, and it looks like an old-style 3. Leave the gap marked as lost, or check another copy.', '#editor'),  # []
    261: ('a', 'high', 'by hand: Non excus[a]bit bona intentio vxoris (Greg. Sayr.)', '#editor'),  # excus[a]bit
    262: ('τὰ ἐνόντα', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n324): p.305 margin note d under Luke 11.41', '#editor'),  # τὰ ἐνόντα
    263: ('o', 'high', "the book's own vocabulary: _r -> o:1440, f:1, t:1; confirmed on the 1622 page image (n324)", '#auto'),  # [o]r
    264: ('t', 'high', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10; confirmed on the 1622 page image (n324)", '#auto'),  # [t]o
    265: ('ἐκ τῆς τοῦ οὐρίου', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n326): p.307 margin under Matth.1.6; name printed lowercase οὐρίου, ου as ȣ ligatures', '#editor'),  # ἐκ τῆς τοῦ οὐρίου
    266: ('ὁ τελώνης', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n326): p.307 margin under Matth.10.3', '#editor'),  # ὁ τελώνης
    267: ('n', 'high', "read from the 1622 page image (n331), replacing the guess 'd': Margin: 'ſi?e viri licentia', with the broken strokes of an n between i and e: 'ſine viri licentia ſaltem praeſumpta' (without the husband's leave, presumed at least). 'ſide' makes no sense.", '#editor'),  # si[d]e
    268: ('tt', 'high', "read from the 1622 page image (n331), replacing the guess 's': 'com-|mi??it': two t stems (crossbars faint) stand between 'mi' and 'it', and the TCP marks the gap as 2 letters: 'verè furtum committit'. Not 'commisit'.", '#editor'),  # commi[s]it
    269: ('שמואל', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n333): p.314 margin note *, unpointed Hebrew 'Samuel' (the name given to the child)", '#editor'),  # שמואל
    270: ('s', 'high', 'by hand: componitur ex diuersis vocibu[s]', '#editor'),  # vocibu[s]
    271: ('שאלתי אתו מאל', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n333): p.314 margin, two lines unpointed: שאלתי / אתו מאל (cf. 1 Sam 1:20 מֵיְהוָה שְׁאִלְתִּיו)', '#editor'),  # שאלתי אתו מאל
    272: ('', 'high', "read from the 1622 page image (n334), replacing the guess 's': The line begins flush 'ought to haue the force', level with 'This' below, so no letter is lost: 'the very knowledge... of her husbands minde and will, ought to haue the force of a ſtraight commandement'. The fill 's' (sought) is wrong.", '#editor'),  # [s]ought
    273: ('t', 'high', "the book's own vocabulary: Es_h -> t:7", '#auto'),  # Es[t]h
    274: ('hi', 'high', 'by hand: Hebraei docent Vast[hi]am natam fuisse (Feuardent)', '#editor'),  # Vast[hi]am
    275: ('d', 'high', "the book's own vocabulary: kindle_ -> d:1; confirmed on the 1622 page image (n339)", '#auto'),  # kindle[d]
    276: ('χάρις', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n340): p.321 margin (1 Pet 2:19)', '#editor'),  # χάρις
    277: ('χάρις παρὰ Θεῷ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n340): p.321 margin (1 Pet 2:20); παρὰ as a ligature, partly blotted', '#editor'),  # χάρις παρὰ Θεῷ
    278: ('t', 'high', 'by hand: about the mee[t]nesse of it', '#editor'),  # mee[t]nesse
    279: ('c', 'high', 'by hand: quid censeas di[c]as, minime prohibeo (Greg. Naz.)', '#editor'),  # di[c]
    280: ('o', 'high', 'by hand: minime prohibe[o]: sed viri tui sententiam...', '#editor'),  # prohibe[o]
    281: ('g', 'high', "the book's own vocabulary: Gre_ -> g:21, w:1; confirmed on the 1622 page image (n357)", '#auto'),  # Gre[g]
    282: ('i', 'high', "read from the 1622 page image (n366), replacing the guess 'o': Gutter: the first letter is lost before 'f ſhe ſhall reiect this good helpe'. The sentence ('She being... more vnable to helpe her ſelfe, if ſhe ſhall reiect this good helpe... is ſhe not moſt iniurious') needs 'if', not 'of'.", '#editor'),  # [o]f
    283: ('s', 'high', "the book's own vocabulary: de_pise -> s:27", '#auto'),  # de[s]pise
    284: ('o', 'high', "the book's own vocabulary: _f -> o:10396, i:1181; confirmed on the 1622 page image (n366)", '#auto'),  # [o]f
    285: ('c', 'high', "the book's own vocabulary: _heerefull -> c:14", '#auto'),  # [c]heerefull
    286: ('b', 'high', 'by hand: no greater ingratitude can [b]e shewed', '#editor'),  # [b]e
    287: ('g', 'high', "the book's own vocabulary: in_ratitude -> g:9", '#auto'),  # in[g]ratitude
    288: ('t', 'high', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10; confirmed on the 1622 page image (n366)", '#auto'),  # [t]o
    289: ('n', 'high', 'by hand: to carry away the [n]ame of gratefulnesse', '#editor'),  # [n]ame
    290: ('o', 'high', "the book's own vocabulary: _f -> o:10396, i:1181; confirmed on the 1622 page image (n366)", '#auto'),  # [o]f
    291: ('p', 'high', "the book's own vocabulary: _reuailes -> p:1; confirmed on the 1622 page image (n366)", '#auto'),  # [p]reuailes
    292: ('f', 'high', "the book's own vocabulary: _orce -> f:42", '#auto'),  # [f]orce
    293: ('b', 'high', 'by hand: not the example of one only, [b]ut of many', '#editor'),  # [b]ut
    294: ('s', 'high', "the book's own vocabulary: _aints -> s:137", '#auto'),  # [s]aints
    295: ('al', 'high', "the book's own vocabulary: _l -> al:1504, il:62, co:31, ga:28; confirmed on the 1622 page image (n366)", '#auto'),  # [al]l
    296: ('κατὰ γνῶσιν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n372): p.353 margin under 1 Pet.3.7; κατὰ as the κ+τ' abbreviation", '#editor'),  # κατὰ γνῶσιν
    297: ('s', 'high', "read from the 1622 page image (n373), replacing the guess 'e': Margin note on p.354 (scan 373, not 374): 'regere fœ-|minas.' The last letter before the stop is a blotted round s, not e. Augustine has 'ad viros pertinet virtute vincere, exemplo regere feminas' (accusative). Word: fœminas.", '#editor'),  # foemina[e]
    298: ('כנגדו', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n376): p.357 margin under Gen.2.18, unpointed (Gen 2:18 כְּנֶגְדּוֹ)', '#editor'),  # כנגדו
    299: ('ἑαυτόν', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n376): p.357 margin under Eph.5.28; accent stroke near-vertical, acute or grave', '#editor'),  # ἑαυτόν
    300: ('συγκληρονόμοι Χριστοῦ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n376): p.357 margin under Rom.8.17; γκ printed as ligature, Χριστοῦ abbreviated with ȣ', '#editor'),  # συγκληρονόμοι Χριστοῦ
    301: ('Θεοῦ συνεργοί', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n376): p.357 margin under 1 Cor.3.9; final accent unclear (acute/grave)', '#editor'),  # Θεοῦ συνεργοί
    302: ('t', 'high', 'by hand: gubernatorem [t]e Deus voluit esse sexus inferioris', '#editor'),  # [t]e
    303: ('מחמד עיניך', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n379): p.360 margin note a under Ezec.24.16, unpointed, two lines; final ד of מחמד has a long stem (looks like ך) but the word is מַחְמַד', '#editor'),  # מחמד עיניך
    304: ('אילת אהבים יעלת חן', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n380): p.361 margin, three lines of unpointed Hebrew (Prov 5:19) above 'Col.1.13.'", '#editor'),  # אילת אהבים יעלת חן
    305: ('υἱὸς τῆς ἀγάπης αὐτοῦ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n380): p.361 margin under Col.1.13; αὐτοῦ with ȣ ligature', '#editor'),  # υἱὸς τῆς ἀγάπης αὐτοῦ
    306: ('תשׁגה', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n380): margin by 'erre thou in her loue' (Prov 5:19 tishgeh); unpointed except a shin dot over ש", '#editor'),  # תשׁגה
    307: ('οἰκοδεσποτεῖν', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n386): note d, 1 Tim 5:14 οἰκοδεσποτεῖν', '#editor'),  # οἰκοδεσποτεῖν
    308: ('n', 'high', 'by hand: namely, to be a[n] helpe', '#editor'),  # a[n]
    309: ('q', 'high', "the book's own vocabulary: re_uireth -> q:101", '#auto'),  # re[q]uireth
    310: ('d', 'high', 'by hand: commend and reward what she hath well [d]one', '#editor'),  # [d]one
    311: ('t', 'high', "the book's own vocabulary: _hat -> t:4575, w:636; confirmed on the 1622 page image (n388)", '#auto'),  # [t]hat
    312: ('fr', 'high', 'by hand: Giue her of the [fr]uit of her hands (Prov. 31. 31)', '#editor'),  # [fr]uit
    313: ('h', 'high', "the book's own vocabulary: _er -> h:1661, i:23, p:10, v:6; confirmed on the 1622 page image (n388)", '#auto'),  # [h]er
    314: ('If', 'high', 'by hand: [If] there be no delight in ones person', '#editor'),  # [If]
    315: ('τοὺς ἀντιδιατιθεμένους', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n391): 2 Tim 2:25; printed τοὺς ἀντιδια-|τιθεμένους across two lines, ους ligatures', '#editor'),  # τοὺς ἀντιδιατιθεμένους
    316: ('a', 'high', "the book's own vocabulary: _dde -> a:42", '#auto'),  # [a]dde
    317: ('s', 'high', "the book's own vocabulary: _mall -> s:34", '#auto'),  # [s]mall
    318: ('i', 'high', "read from the 1622 page image (n402), replacing the guess 'o': p.383 is scan 402. Gutter: the first letter is lost before 'f before them ſhe ſhould be rebuked'. The sense ('which otherwiſe they would quickly take, if before them ſhe ſhould be rebuked') needs 'if', not 'of'. The line above starts 'of deſpiſing' with the o half visible; here only the f shows.", '#editor'),  # [o]f
    319: ('t', 'high', "the book's own vocabulary: _hat -> t:4575, w:636; confirmed on the 1622 page image (n402)", '#auto'),  # [t]hat
    320: ('c', 'high', 'by hand: as of a discontented [c]reditor ouer a desperate debtor', '#editor'),  # [c]reditor
    321: ('ſu', 'high', "read from the 1622 page image (n406), replacing the guess 'o': Gutter: the end of a u stroke is visible before 'biect that hath diſpleaſed him'. Like the lines around it ('[p]riſoners', '[c]reditor'), the line has lost its first letters: '4. A fierce fiery countenance, as of an angry King ouer a ſubiect that hath diſpleaſed him'. The word is 'ſubiect' (subject), not 'obiect'.", '#editor'),  # [o]biect
    322: ('e', 'high', 'by hand: n[e]que quicquam tale exprobrauit (Chrysostom)', '#editor'),  # n[e]
    323: ('', 'high', 'by hand: C[or]nelius -- the transcription reads "C•raelius"; Acts 10. 2, 30 in the margin identifies him', '#editor'),  # C[]raelius
    324: ('l', 'high', 'by hand: the lawes vnder which they [l]iue', '#editor'),  # [l]iue
    325: ('f', 'high', 'by hand: vse all the [f]raudulent meanes they can', '#editor'),  # [f]raudulent
    326: ('n', 'high', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3; confirmed on the 1622 page image (n426)", '#auto'),  # [n]ot
    327: ('b', 'high', "the book's own vocabulary: dou_le -> b:32", '#auto'),  # dou[b]le
    328: ('k', 'high', "the book's own vocabulary: vn_indnesse -> k:9", '#auto'),  # vn[k]indnesse
    329: ('t', 'high', "the book's own vocabulary: _hinking -> t:20", '#auto'),  # [t]hinking
    330: ('w', 'high', "the book's own vocabulary: _iues -> w:1085, l:13, g:4, v:1; confirmed on the 1622 page image (n426)", '#auto'),  # [w]iues
    331: ('l', 'high', "the book's own vocabulary: _esse -> l:66, n:1, m:1, b:1; confirmed on the 1622 page image (n430)", '#auto'),  # [l]esse
    332: ('d', 'high', 'by hand: affected with a wrong [d]one to the bodie', '#editor'),  # [d]one
    333: ('i', 'high', "the book's own vocabulary: _n -> i:5378, a:1059, o:506, v:1; confirmed on the 1622 page image (n430)", '#auto'),  # [i]n
    334: ('s', 'high', "the book's own vocabulary: _trangers -> s:27", '#auto'),  # [s]trangers
    335: ('h', 'high', 'by hand: for [h]e hath more power ouer them in his house', '#editor'),  # [h]e
    336: ('o', 'high', "the book's own vocabulary: _r -> o:1440, f:1, t:1; confirmed on the 1622 page image (n430)", '#auto'),  # [o]r
    337: ('u', 'high', "the book's own vocabulary: ser_ants -> u:1096", '#auto'),  # ser[u]ants
    338: ('an', 'high', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232; confirmed on the 1622 page image (n430)", '#auto'),  # [an]d
    339: ('n', 'high', "the book's own vocabulary: _eeds -> n:48, d:9, s:1, w:1; confirmed on the 1622 page image (n430)", '#auto'),  # [n]eeds
    340: ('אלוֹף', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n432): Prov 2:17 'guide' (MT אַלּוּף); printed unpointed but with a dot over the ו (holem), so given as printed", '#editor'),  # אלוֹף
    341: ('p', 'high', 'by hand: the most [p]eeuish, and peruerse wiues', '#editor'),  # [p]eeuish
    342: ('i', 'high', 'by hand: they are very deuils [i]ncarnate', '#editor'),  # [i]ncarnate
    343: ('sh', 'high', 'by hand: in their place [sh]ew themselues so vnlike to Christ', '#editor'),  # [sh]ew
    344: ('l', 'high', "the book's own vocabulary: _oue -> l:633, m:78, i:2, d:1; confirmed on the 1622 page image (n434)", '#auto'),  # [l]oue
    345: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n434)", '#auto'),  # [a]nd
    346: ('s', 'high', 'by hand: they may haue [s]ome bait to allure their affections', '#editor'),  # [s]ome
    347: ('o', 'high', "the book's own vocabulary: _r -> o:1440, f:1, t:1; confirmed on the 1622 page image (n434)", '#auto'),  # [o]r
    348: ('p', 'high', "the book's own vocabulary: _ortion -> p:48", '#auto'),  # [p]ortion
    349: ('e', 'high', "the book's own vocabulary: _xpect -> e:16", '#auto'),  # [e]xpect
    350: ('lo', 'high', 'by hand: This cannot be a true sound [lo]ue', '#editor'),  # [lo]ue
    351: ('in', 'high', "the book's own vocabulary: _heritance -> in:48", '#auto'),  # [in]heritance
    352: ('lo', 'high', 'by hand: an holy, pure, chaste, [lo]ue', '#editor'),  # [lo]ue
    353: ('ef', 'high', 'by hand: as is euident by the [ef]fect thereof', '#editor'),  # [ef]fect
    354: ('to', 'high', 'by hand: I am euen ashamed [to] mention', '#editor'),  # [to]
    355: ('at', 'high', 'by hand: let such know, th[at] they shall be accounted', '#editor'),  # th[at]
    356: ('te', 'high', "the book's own vocabulary: adul_rers -> te:3 (auto(2 letters)); confirmed on the 1622 page image (n435)", '#auto'),  # adul[te]rers
    357: ('l', 'high', "the book's own vocabulary: _eaue -> l:80", '#auto'),  # [l]eaue
    358: ('m', 'high', "the book's own vocabulary: _ust -> m:767, i:131, l:13, d:4; confirmed on the 1622 page image (n436)", '#auto'),  # [m]ust
    359: ('p', 'high', 'by hand: a pit of needlesse [p]erill', '#editor'),  # [p]erill
    360: ('st', 'high', 'by hand: to bring vs to this [st]raite of parting with our life', '#editor'),  # [st]raite
    361: ('a', 'high', "read from the 1622 page image (n436), replacing the guess 't': p.417 gutter: the start of the line is lost in the gutter shadow (1-2 letters, as 'th' of 'their' on the line above); 'when the good we / [a]ime at in the behalfe of our wiues'; 'ime at' visible. 'time at' makes no sense; the sense is 'aim at' (1622 'aime'); one letter lost, as '[m]ust', '[p]erill' nearby", '#editor'),  # [t]ime
    362: ('e', 'high', 'by hand: cannot any other way be [e]ffected', '#editor'),  # [e]ffected
    363: ('to', 'high', 'by hand: no other way [to] redeeme the Church', '#editor'),  # [to]
    364: ('g', 'high', "the book's own vocabulary: _reater -> g:116", '#auto'),  # [g]reater
    365: ('r', 'high', "the book's own vocabulary: _ule -> r:107", '#auto'),  # [r]ule
    366: ('ca', 'high', 'by hand: which minde men must much more [ca]rie towards their wiues', '#editor'),  # [ca]rie
    367: ('ga', 'high', 'by hand: It was for our saluation that Christ [ga]ue himselfe', '#editor'),  # [ga]ue
    368: ('th', 'high', "the book's own vocabulary: _eir -> th:4253", '#auto'),  # [th]eir
    369: ('pl', 'medium', "read from the 1622 page image (n436), replacing the guess 'm': p.417 gutter: the start of the line is lost in the gutter shadow (1-2 letters, as 'th' of 'their' on the line above); 'their profit, their / [pl]eaſure, their promotion'; 'eaſure' visible, letters before it gone. The gap is as wide as the 'th' lost from 'their' on the line above, so it fits 'pl' as well as 'm'; 'pleasure' is the sense (profit, pleasure, promotion), 'measure' is not", '#editor'),  # [m]easure
    370: ('af', 'high', "the book's own vocabulary: _fections -> af:19", '#auto'),  # [af]fections
    371: ('be', 'high', 'by hand: if any extraordinary charge must [be] laid out', '#editor'),  # [be]
    372: ('wi', 'high', 'by hand: little loue [wi]ll then appeare', '#editor'),  # [wi]ll
    373: ('an', 'high', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232; confirmed on the 1622 page image (n436)", '#auto'),  # [an]d
    374: ('g', 'high', 'by hand: As [g]old and other like mettals are tryed by the fire', '#editor'),  # [g]ld
    375: ('affl', 'high', 'by hand: so loue by [affl]ictions and crosses', '#editor'),  # [affl]ictions
    376: ('t', 'high', 'by hand: now [t]ender-hearted, then againe hard-hearted', '#editor'),  # [t]ender
    377: ('l', 'high', 'by hand: now smiling, then [l]owring', '#editor'),  # [l]owring
    378: ('y', 'high', "the book's own vocabulary: _oung -> y:77", '#auto'),  # [y]oung
    379: ('t', 'high', "the book's own vocabulary: _hose -> t:393, w:60, c:2; confirmed on the 1622 page image (n438)", '#auto'),  # [t]hose
    380: ('a', 'high', 'by hand: proue in their loue as cold [a]s ice', '#editor'),  # [a]s
    381: ('t', 'high', "the book's own vocabulary: _heir -> t:4253", '#auto'),  # [t]heir
    382: ('u', 'high', "the book's own vocabulary: ne_er -> u:146", '#auto'),  # ne[u]er
    383: ('w', 'high', 'by hand: [w]e haue on the one side a good direction', '#editor'),  # [w]e
    384: ('lo', 'high', 'by hand: a good direction to teach vs how to [lo]ue our wiues', '#editor'),  # [lo]ue
    385: ('o', 'high', "the book's own vocabulary: _ther -> o:860", '#auto'),  # [o]ther
    386: ('far', 'high', 'by hand: it sheweth vs how [far]re short we come', '#editor'),  # [far]re
    387: ('m', 'high', "the book's own vocabulary: _ay -> m:1244, w:165, s:141, d:90; confirmed on the 1622 page image (n438)", '#auto'),  # [m]ay
    388: ('w', 'high', 'by hand: a Subiection [w]hereunto by nature we are all loath to yeeld', '#editor'),  # [w]hereunto
    389: ('th', 'high', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944; confirmed on the 1622 page image (n438)", '#auto'),  # [th]e
    390: ('m', 'high', 'by hand: and [m]uch more easie it is to performe the part of a wife', '#editor'),  # [m]uch
    391: ('ter', 'high', "the book's own vocabulary: pat_ne -> ter:89 (auto(3 letters))", '#auto'),  # pat[ter]ne
    392: ('wiu', 'high', 'by hand: So ought men to loue their [wiu]es as their owne bodies', '#editor'),  # [wiu]es
    393: ('n', 'high', 'by hand: see they neither faune o[n] them, nor flatter them', '#editor'),  # o[n]
    394: ('t', 'high', 'by hand: as great as possibly i[t] can be', '#editor'),  # i[t]
    395: ('n', 'high', "read from the 1622 page image (n440), replacing the guess 's': p.421 gutter: the start of the line is lost in the gutter shadow; 'when the Sunne ſhineth forth at / [n]oone day.' 'oone day' visible, a trace of the lost letter; the sense is 'noon day' (cf. Prov 4:18 / Ps 37:6), 'soone day' is nonsense", '#editor'),  # [s]oone
    396: ('f', 'high', "the book's own vocabulary: _or -> f:2960, n:228, c:196, h:2; confirmed on the 1622 page image (n440)", '#auto'),  # [f]or
    397: ('h', 'high', "the book's own vocabulary: _eart -> h:198", '#auto'),  # [h]eart
    398: ('re', 'high', "the book's own vocabulary: _adinesse -> re:19", '#auto'),  # [re]adinesse
    399: ('B', 'high', "read from the 1622 page image (n440), replacing the guess 'b': p.421 gutter: the start of the line is lost in the gutter shadow; italic '[B]ooz ſaith to Ruth'; 'ooz' visible. Same letter, but a capital: the name, printed 'Booz' four lines below ('the ſaid Booz to Ruth')", '#editor'),  # [b]ooz
    400: ('h', 'high', "the book's own vocabulary: be_oofull -> h:1; confirmed on the 1622 page image (n440)", '#auto'),  # be[h]oofull
    401: ('in', 'high', 'by hand: as the history [in] many particulars sheweth', '#editor'),  # [in]
    402: ('a', 'high', "the book's own vocabulary: _miable -> a:12", '#auto'),  # [a]miable
    403: ('v', 'high', "the book's own vocabulary: _ices -> v:53", '#auto'),  # [v]ices
    404: ('ou', 'high', 'by hand: with goodnes he [ou]ght to ouercome euill', '#editor'),  # [ou]ught
    405: ('t', 'high', "the book's own vocabulary: _hat -> t:4575, w:636; confirmed on the 1622 page image (n444)", '#auto'),  # [t]hat
    406: ('lo', 'high', 'by hand: for [lo]ue hopeth all things (1 Cor. 13. 7)', '#editor'),  # [lo]ue
    407: ('sa', 'high', 'by hand: as he may iustly [sa]y', '#editor'),  # [sa]y
    408: ('c', 'high', "the book's own vocabulary: _hurch -> c:500", '#auto'),  # [c]hurch
    409: ('af', 'high', "the book's own vocabulary: _ford -> af:35 (auto(2 letters))", '#auto'),  # [af]ford
    410: ('ali', 'high', "the book's own vocabulary: _enate -> ali:6 (auto(3 letters))", '#auto'),  # [ali]enate
    411: ('ἀστοργία', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n449): margin above Rom 1:30, 2 Tim 3:3 (ἄστοργος); στ ligature', '#editor'),  # ἀστοργία
    412: ('', 'high', 'by hand: more abomi[]nable -- the bullet is a blot, not a letter', '#editor'),  # abomi[]nable
    413: ('o', 'high', "the book's own vocabulary: _r -> o:1440, f:1, t:1; confirmed on the 1622 page image (n450)", '#auto'),  # [o]r
    414: ('s', 'high', "the book's own vocabulary: sub_tance -> s:35", '#auto'),  # sub[s]tance
    415: ('s', 'high', "the book's own vocabulary: _eeme -> s:54, d:1; confirmed on the 1622 page image (n450)", '#auto'),  # [s]eeme
    416: ('re', 'high', "the book's own vocabulary: pa_nts -> re:1302", '#auto'),  # pa[re]nts
    417: ('cia', 'high', "the book's own vocabulary: espe_lly -> cia:147", '#auto'),  # espe[cia]lly
    418: ('d', 'high', "the book's own vocabulary: an_ -> d:8820, y:710, s:4, a:2; confirmed on the 1622 page image (n451)", '#auto'),  # an[d]
    419: ('i', 'high', "the book's own vocabulary: _n -> i:5378, a:1059, o:506, v:1; confirmed on the 1622 page image (n452)", '#auto'),  # [i]n
    420: ('o', 'high', "the book's own vocabulary: _r -> o:1440, f:1, t:1; confirmed on the 1622 page image (n452)", '#auto'),  # [o]r
    421: ('i', 'high', "the book's own vocabulary: _mpious -> i:12", '#auto'),  # [i]mpious
    422: ('s', 'high', "the book's own vocabulary: compri_ed -> s:36", '#auto'),  # compri[s]ed
    423: ('b', 'high', "the book's own vocabulary: _y -> b:1790, m:123; confirmed on the 1622 page image (n452)", '#auto'),  # [b]y
    424: ('th', 'high', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944; confirmed on the 1622 page image (n452)", '#auto'),  # [th]e
    425: ('to', 'high', 'by hand: children haue euer vsed [to] giue those titles', '#editor'),  # [to]
    426: ('B', 'high', "read from the 1622 page image (n452), replacing the guess 'b': Gutter: italic '..athsheba' visible; the name is set with a capital in italic (Salomon to Bathsheba), so the lost letter is 'B', not 'b' (case only).", '#editor'),  # [b]athsheba
    427: ('κύριε', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n452): after Matt 21:30 (ἐγώ, κύριε); ρ worn', '#editor'),  # κύριε
    428: ('אדני', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n452): after Gen 31:35 (אֲדֹנִי, 'Lord'); unpointed, ד and נ worn but certain from the verse", '#editor'),  # אדני
    429: ('o', 'high', "the book's own vocabulary: _f -> o:10396, i:1181; confirmed on the 1622 page image (n452)", '#auto'),  # [o]f
    430: ('n', 'high', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3; confirmed on the 1622 page image (n452)", '#auto'),  # [n]ot
    431: ('re', 'high', "the book's own vocabulary: pa_nts -> re:1302", '#auto'),  # pa[re]nts
    432: ('o', 'high', "the book's own vocabulary: _bserue -> o:67", '#auto'),  # [o]bserue
    433: ('m', 'high', "the book's own vocabulary: _ore -> m:914, s:10, f:4; confirmed on the 1622 page image (n452)", '#auto'),  # [m]ore
    434: ('rge', 'high', "read from the 1622 page image (n453), replacing the guess 'se': Line-final at the outer edge: 'vrg' clearly printed, the last letter lost off the edge, catchword 'matters'. The word is 'vrge' (must needs urge matters to the very uttermost), not 'vse'.", '#editor'),  # v[se]
    435: ('r', 'high', "the book's own vocabulary: pa_able -> r:10", '#auto'),  # pa[r]able
    436: ('n', 'high', "read from the 1622 page image (n454), replacing the guess 't': Gutter: 'o answer at all' visible; the sense (pout, lour, swell, and give no answer at all to their parents; margin 'Stomachfull silence') requires 'no', not 'to'.", '#editor'),  # [t]o
    437: ('t', 'high', 'by hand: much offended and grieued [t]hereat', '#editor'),  # [t]hereat
    438: ('v', 'high', "the book's own vocabulary: _ery -> v:274", '#auto'),  # [v]ery
    439: ('b', 'high', "the book's own vocabulary: _efore -> b:494", '#auto'),  # [b]efore
    440: ('be', 'high', 'by hand: must [be] so framed both for matter and manner', '#editor'),  # [be]
    441: ('oc', 'high', "the book's own vocabulary: _casion -> oc:123", '#auto'),  # [oc]casion
    442: ('th', 'high', "the book's own vocabulary: _em -> th:1875, qu:6, id:3, rh:2; confirmed on the 1622 page image (n454)", '#auto'),  # [th]em
    443: ('pa', 'high', "the book's own vocabulary: _rents -> pa:1302", '#auto'),  # [pa]rents
    444: ('du', 'high', "the book's own vocabulary: _ty -> du:169, ci:2; confirmed on the 1622 page image (n454)", '#auto'),  # [du]ty
    445: ('למען יארכון ימיך', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n457): Exod 20:12 'that thy days may be prolonged'; three lines, unpointed (a stray dot in ימיך)", '#editor'),  # למען יארכון ימיך
    446: ('ll', 'high', 'by hand: they doe not so generally disa[ll]ow this dutie', '#editor'),  # disa[ll]ow
    447: ('τέκνα ἀνυπότακτα', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n460): note g, Tit 1:6 τέκνα ... ἀνυπότακτα', '#editor'),  # τέκνα ἀνυπότακτα
    448: ('בני־בליעל', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n460): note h, Deut 13:13 'sons of Belial', printed with a hyphen (maqaf). NB the note goes on 'ex בלי non & יעל profuit': the TCP has 'ex non & profuit' with the Hebrew בלי (after ex) and יעל (after &) silently dropped, no gap marked", '#editor'),  # בני־בליעל
    449: ('בלי עול', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n460): note h ends 'quasi בלי עול' (without yoke)", '#editor'),  # בלי עול
    450: ('', 'high', 'by hand: as some will haue it -- the bullet is a blot', '#editor'),  # []it
    451: ('s', 'high', "read from the 1622 page image (n462), replacing the guess 't': Gutter: '..o carefull to send prouision' with the edge of the 'o'. Sense needs 'Ishai was so carefull' (printed with long s, ſo), not 'to'.", '#editor'),  # [t]o
    452: ('s', 'high', "the book's own vocabulary: _onnes -> s:47", '#auto'),  # [s]onnes
    453: ('c', 'high', "the book's own vocabulary: _ommended -> c:59", '#auto'),  # [c]ommended
    454: ('b', 'high', 'by hand: It is collected [b]oth by ancient and later Diuines', '#editor'),  # [b]oth
    455: ('in', 'high', 'by hand: our Lord Iesus Christ [in] his younger yeeres', '#editor'),  # [in]
    456: ('th', 'high', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944; confirmed on the 1622 page image (n462)", '#auto'),  # [th]e
    457: ('ie', 'high', "the book's own vocabulary: sub_ction -> ie:297", '#auto'),  # sub[ie]ction
    458: ('le', 'high', "the book's own vocabulary: cal_d -> le:93, ce:1; confirmed on the 1622 page image (n462)", '#auto'),  # cal[le]d
    459: ('bo', 'high', 'by hand: an hand in placing [bo]th their children', '#editor'),  # [bo]th
    460: ('w', 'high', "the book's own vocabulary: _orld -> w:137", '#auto'),  # [w]orld
    461: ('w', 'high', "the book's own vocabulary: _hile -> w:105", '#auto'),  # [w]hile
    462: ('sh', 'high', 'by hand: that they [sh]ould see their children well trained vp', '#editor'),  # [sh]ould
    463: ('ent', 'high', 'by hand: children may [ent]er into religious orders', '#editor'),  # [ent]er
    464: ('gai', 'high', "the book's own vocabulary: a_nst -> gai:408", '#auto'),  # a[gai]nst
    465: ('doe', 'high', 'by hand: Whereby they [doe] not only patronize apparent disobedience', '#editor'),  # [doe]
    466: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n464)", '#auto'),  # [a]nd
    467: ('1', 'high', 'read from another 1622 copy (archive.org bim_early-english-books-1475-1640_of-domesticall-duties_gouge-william_1622, n780): "1. It doth not necessarily imply"; the filmed copy is cut at the gutter here (n464), as the 1634 edition confirms', '#editor'),  # [1.]
    468: ('f', 'high', "the book's own vocabulary: _or -> f:2960, n:228, c:196, h:2; confirmed on the 1622 page image (n464)", '#auto'),  # [f]or
    469: ('d', 'high', "the book's own vocabulary: _uty -> d:169", '#auto'),  # [d]uty
    470: ('Νυμφευμάτων μὲν τῶν ἐμῶν πατὴρ ἐμοῦ μέριμναν ἕξει, κοὐκ ἐμὸν τάδε κρίνειν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n467): Euripides, Andromache 987-8 (Gouge's text: ἐμοῦ for ἐμὸς, τάδε κρίνειν for κρίνειν τάδε); μὲν and τῶν printed as contractions, κοὐκ printed κ'οὐκ with ȣ ligature", '#editor'),  # Νυμφευμάτων μὲν τῶν ἐμῶν πατὴρ ἐμοῦ μέριμναν ἕξει, κοὐκ ἐμὸν τάδε κρίνειν
    471: ('que', 'medium', "read from the 1622 page image (n467), replacing the guess 's': End of the long note f in the bottom margin: 'Perkins in Oecon.c.6.alijq' -- the lost letter is a 'q' with the -que abbreviation mark (aliisque, as the book abbreviates 'quoq;' on the same page), not 's'. Small blurred type, but the q's descender and mark are visible.", '#editor'),  # alij[s]
    472: ('d', 'high', 'by hand: while the [d]ate of their couenant lasteth', '#editor'),  # [d]ate
    473: ('t', 'high', 'by hand: greater [t]hen of a childe', '#editor'),  # [t]hen
    474: ('p', 'high', "the book's own vocabulary: _ower -> p:260, l:3, t:1; confirmed on the 1622 page image (n470)", '#auto'),  # [p]ower
    475: ('p', 'high', "the book's own vocabulary: _ower -> p:260, l:3, t:1; confirmed on the 1622 page image (n470)", '#auto'),  # [p]ower
    476: ('u', 'high', "the book's own vocabulary: ser_ant -> u:247", '#auto'),  # ser[u]ant
    477: ('s', 'high', "the book's own vocabulary: Be_ides -> s:52", '#auto'),  # Be[s]ides
    478: ('a', 'high', "the book's own vocabulary: _way -> a:186, s:4; confirmed on the 1622 page image (n472)", '#auto'),  # [a]way
    479: ('t', 'high', "the book's own vocabulary: _aken -> t:190, s:2; confirmed on the 1622 page image (n472)", '#auto'),  # [t]aken
    480: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n472)", '#auto'),  # [a]nd
    481: ('t', 'high', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10; confirmed on the 1622 page image (n478)", '#auto'),  # [t]o
    482: ('', 'high', 'by hand: My sonne, saith he -- the bullet is a blot', '#editor'),  # []he
    483: (' ', 'high', 'a broken word space: the letters on both sides spell two words; confirmed on the 1622 page image (n479)', '#auto'),  # a[ ]glad
    484: ('κατὰ πάντα', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n483): note a, Col 3:20 κατὰ πάντα; κατὰ printed as the κ-τ contraction', '#editor'),  # κατὰ πάντα
    485: ('ἐν κυρίῳ', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n483): note b, Eph 6:1 ἐν κυρίῳ', '#editor'),  # ἐν κυρίῳ
    486: ('m', 'high', "read from the 1622 page image (n484), replacing the guess 'c': Gutter: the last minims of an 'm' show before 'ocker to his father'. The word is 'mocker' (Gen 27:12, Geneva 'I shall seeme to him as a mocker'), not 'cocker'.", '#editor'),  # [c]ocker
    487: ('b', 'high', "the book's own vocabulary: for_eare -> b:46", '#auto'),  # for[b]eare
    488: ('o', 'high', "the book's own vocabulary: _f -> o:10396, i:1181; confirmed on the 1622 page image (n484)", '#auto'),  # [o]f
    489: ('τῆς σαρκὸς', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n486): Heb 12:9 τῆς σαρκὸς; τῆς as a contraction', '#editor'),  # τῆς σαρκὸς
    490: ('n', 'high', "the book's own vocabulary: Io_athan -> n:10 (auto(1 letters))", '#auto'),  # Io[n]athan
    491: ('οὐθὲν ποιήσας ἄξιον τῶν ὑπηργμένων δέδρακεν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n488): Aristotle EN 8.14 (1163b), Gouge's order, without γὰρ; ου ligature, τῶν contracted", '#editor'),  # οὐθὲν ποιήσας ἄξιον τῶν ὑπηργμένων δέδρακεν
    492: ('ἀμοιβὰς ἀποδιδόναι', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n488): 1 Tim 5:4 ἀμοιβὰς ἀποδιδόναι', '#editor'),  # ἀμοιβὰς ἀποδιδόναι
    493: ('b', 'high', 'by hand: [b]ut it hardly ascendeth from children to parents', '#editor'),  # [b]ut
    494: ('ἀμοιβὰς ἀποδιδόναι', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n492): note h, 1 Tim 5:4, same words as gap 492', '#editor'),  # ἀμοιβὰς ἀποδιδόναι
    495: ('πελαργός. ἀντιπελαργεῖν.', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n493): note * on 'Greeke name of a Storke': two lines, πελαργός. / ἀντιπελαργεῖν.; TCP joined the next margin note ('Sin of Pharisies...') straight after the gap, so the closing stop is kept", '#editor'),  # πελαργός. ἀντιπελαργεῖν.
    496: ('o', 'high', "the book's own vocabulary: su_rum -> o:1; confirmed on the 1622 page image (n494)", '#auto'),  # su[o]rum
    497: ('p', 'high', 'by hand: More tulere [p]atrum (Virgil, Aen. 11. 185-6)', '#editor'),  # [p]a
    498: ('t', 'high', 'by hand: More tulere pa[t]rum', '#editor'),  # pa[t]rum
    499: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n496)", '#auto'),  # [a]nd
    500: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n496)", '#auto'),  # [a]nd
    501: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n496)", '#auto'),  # [a]nd
    502: ('f', 'high', "the book's own vocabulary: _arre -> f:140, w:12, b:2, i:1; confirmed on the 1622 page image (n496)", '#auto'),  # [f]arre
    503: ('S', 'high', 'by hand: [S]ome by the needlesse solemnitie of their parents funerall', '#editor'),  # [S]ome
    504: ('so', 'high', 'by hand: are [so] farre cast into debt', '#editor'),  # [so]
    505: ('t', 'high', "the book's own vocabulary: _he -> t:12236, s:713; confirmed on the 1622 page image (n496)", '#auto'),  # [t]he
    506: ('le', 'high', "the book's own vocabulary: so_mnitie -> le:8", '#auto'),  # so[le]mnitie
    507: ('g', 'high', "the book's own vocabulary: char_es -> g:10", '#auto'),  # char[g]es
    508: ('b', 'high', "the book's own vocabulary: _urying -> b:3; confirmed on the 1622 page image (n496)", '#auto'),  # [b]urying
    509: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n496)", '#auto'),  # [a]nd
    510: ('o', 'high', "the book's own vocabulary: _f -> o:10396, i:1181; confirmed on the 1622 page image (n496)", '#auto'),  # [o]f
    511: ('k', 'high', "the book's own vocabulary: ma_eth -> k:178", '#auto'),  # ma[k]eth
    512: ('v', 'high', "the book's own vocabulary: _engeance -> v:30", '#auto'),  # [v]engeance
    513: ('a', 'high', 'by hand: such measure to be meated out to them, [a]s they mete', '#editor'),  # [a]s
    514: ('t', 'high', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10; confirmed on the 1622 page image (n498)", '#auto'),  # [t]o
    515: ('t', 'high', "the book's own vocabulary: ingra_itude -> t:9", '#auto'),  # ingra[t]itude
    516: ('o', 'high', 'by hand: apud Di[o]g. Laert. l. 1.', '#editor'),  # Di[o]g
    517: ('u', 'high', "the book's own vocabulary: Da_ids -> u:18", '#auto'),  # Da[u]ids
    518: ('m', 'high', "the book's own vocabulary: She_ei -> m:1 (auto(1 letters)); confirmed on the 1622 page image (n500)", '#auto'),  # She[m]ei
    519: ('i', 'high', "the book's own vocabulary: _ustice -> i:35", '#auto'),  # [i]ustice
    520: ('a', 'high', "the book's own vocabulary: allow_nce -> a:27", '#auto'),  # allow[a]nce
    521: ('h', 'high', "the book's own vocabulary: _eart -> h:198", '#auto'),  # [h]eart
    522: ('p', 'high', "the book's own vocabulary: _ower -> p:260, l:3, t:1; confirmed on the 1622 page image (n502)", '#auto'),  # [p]ower
    523: ('n', 'high', "the book's own vocabulary: shi_ing -> n:1; confirmed on the 1622 page image (n502)", '#auto'),  # shi[n]ing
    524: ('th', 'high', "the book's own vocabulary: _ey -> th:2982, ob:109, pr:5, wh:1; confirmed on the 1622 page image (n502)", '#auto'),  # [th]ey
    525: ('th', 'high', "the book's own vocabulary: _ey -> th:2982, ob:109, pr:5, wh:1; confirmed on the 1622 page image (n502)", '#auto'),  # [th]ey
    526: ('w', 'high', "the book's own vocabulary: _eary -> w:12", '#auto'),  # [w]eary
    527: ('th', 'high', "the book's own vocabulary: _em -> th:1875, qu:6, id:3, rh:2; confirmed on the 1622 page image (n502)", '#auto'),  # [th]em
    528: ('er', 'high', "the book's own vocabulary: young_ -> er:27", '#auto'),  # young[er]
    529: ('w', 'high', "the book's own vocabulary: _eary -> w:12", '#auto'),  # [w]eary
    530: ('th', 'high', "the book's own vocabulary: _eir -> th:4253", '#auto'),  # [th]eir
    531: ('ce', 'high', 'by hand: the law of God maketh it plaine in[ce]st', '#editor'),  # in[ce]st
    532: ('s', 'high', "the book's own vocabulary: parent_ -> s:1302, i:1; confirmed on the 1622 page image (n507)", '#auto'),  # parent[s]
    533: ('', 'high', 'by hand: a lost book number in a marginal cross-reference', '#editor'),  # []
    534: ('i', 'high', 'by hand: that dutie [i]s due to them', '#editor'),  # [i]s
    535: ('s', 'high', "the book's own vocabulary: de_ert -> s:5", '#auto'),  # de[s]ert
    536: ('f', 'high', "the book's own vocabulary: _rom -> f:963", '#auto'),  # [f]rom
    537: ('o', 'high', "the book's own vocabulary: _f -> o:10396, i:1181; confirmed on the 1622 page image (n510)", '#auto'),  # [o]f
    538: ('t', 'high', "the book's own vocabulary: _hey -> t:2982, w:1; confirmed on the 1622 page image (n510)", '#auto'),  # [t]hey
    539: ('καλὸν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n511): note b on 'Good or honest', 1 Tim 5:4 καλὸν", '#editor'),  # καλὸν
    540: ('δίκαιον', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n511): note c on 'right'", '#editor'),  # δίκαιον
    541: ('ni', 'high', "the book's own vocabulary: Hoph_ -> ni:2; confirmed on the 1622 page image (n513)", '#auto'),  # Hoph[ni]
    542: ('a', 'high', "the book's own vocabulary: _re -> a:2300, e:2; confirmed on the 1622 page image (n514)", '#auto'),  # [a]re
    543: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n514)", '#auto'),  # [a]nd
    544: ('t', 'high', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10; confirmed on the 1622 page image (n514)", '#auto'),  # [t]o
    545: ('in', 'high', 'by hand: though he truly [in]tend what he promiseth', '#editor'),  # [in]tend
    546: ('e', 'high', "the book's own vocabulary: _ither -> e:109, w:1, h:1; confirmed on the 1622 page image (n514)", '#auto'),  # [e]ither
    547: ('h', 'high', 'by hand: but thought when [h]e made the promise', '#editor'),  # [h]e
    548: ('u', 'high', "the book's own vocabulary: e_ent -> u:3; confirmed on the 1622 page image (n514)", '#auto'),  # e[u]ent
    549: ('str', 'high', 'by hand: Gods power cannot be so [str]aitned', '#editor'),  # [str]aitned
    550: ('th', 'high', 'by hand: men may be taken away before [th]e time', '#editor'),  # [th]etime
    551: ('li', 'high', 'by hand: but God euer [li]ueth, and changeth not', '#editor'),  # [li]eth
    552: ('sa', 'high', 'by hand: Gods, who euer remaineth the [sa]me', '#editor'),  # [sa]me
    553: ('pa', 'high', "the book's own vocabulary: com_rison -> pa:24 (auto(2 letters))", '#auto'),  # com[pa]rison
    554: ('b', 'high', 'by hand: no dutie so holy and necessarie, [b]ut may be peruerted', '#editor'),  # [b]ut
    555: ('si', 'high', 'by hand: the catalogue of notorious [si]nnes', '#editor'),  # [si]nnes
    556: ('lu', 'high', 'by hand: through couetousnesse, [lu]st, vaine-glory', '#editor'),  # [lu]st
    557: ('sh', 'high', 'by hand: in stead of the good which they [sh]ould doe', '#editor'),  # [sh]ould
    558: ('t', 'high', "the book's own vocabulary: _hem -> t:1875, r:2, s:1; confirmed on the 1622 page image (n518)", '#auto'),  # [t]hem
    559: ('re', 'high', 'by hand: Is not this mee[re] apish kindnesse?; confirmed on the 1622 page image (n519)', '#editor'),  # mee[re]
    560: ('ἀδιαλείπτως', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n520): 1 Thess 5:17 ἀδιαλείπτως', '#editor'),  # ἀδιαλείπτως
    561: ('c', 'high', 'by hand: Basil. loc. [c]it.', '#editor'),  # [c]it
    562: ('y', 'high', "the book's own vocabulary: _oung -> y:77", '#auto'),  # [y]oung
    563: ('d', 'high', "the book's own vocabulary: _oubt -> d:27", '#auto'),  # [d]oubt
    564: ('tr', 'high', "the book's own vocabulary: coun_ies -> tr:5 (auto(2 letters))", '#auto'),  # coun[tr]ies
    565: ('w', 'high', 'by hand: the sincere milke of the [w]ord (1 Pet. 2. 2)', '#editor'),  # [w]ord
    566: ('i', 'high', "the book's own vocabulary: _nfants -> i:7", '#auto'),  # [i]nfants
    567: ('pr', 'high', 'by hand: the abilitie, and [pr]omptnesse which is in them to sucke', '#editor'),  # [pr]omptnesse
    568: ('ca', 'high', 'by hand: Gods prouidence in [ca]using a womans breasts to yeeld milke', '#editor'),  # [ca]using
    569: ('t', 'high', "the book's own vocabulary: _o -> t:10165, s:1630, n:828, d:10; confirmed on the 1622 page image (n528)", '#auto'),  # [t]o
    570: ('i', 'high', "the book's own vocabulary: _mplie -> i:5", '#auto'),  # [i]mplie
    571: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n528)", '#auto'),  # [a]nd
    572: ('εἰ ἐτεκνοτρόφησεν', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n528): 1 Tim 5:10 εἰ ἐτεκνοτρόφησεν, split ἐτεκνοτρό-|φησεν', '#editor'),  # εἰ ἐτεκνοτρόφησεν
    573: ('n', 'high', "the book's own vocabulary: _ourished -> n:11", '#auto'),  # [n]ourished
    574: ('y', 'high', "the book's own vocabulary: _oung -> y:77", '#auto'),  # [y]oung
    575: ('lo', 'high', 'by hand: mothers [lo]ue those children best', '#editor'),  # [lo]ue
    576: ('sh', 'high', 'by hand: and we [sh]all finde the dutie in question', '#editor'),  # [sh]all
    577: ('p', 'high', 'by hand: that the [p]aps of that woman gaue him sucke', '#editor'),  # [p]aps
    578: ('s', 'high', "the book's own vocabulary: _ucke -> s:50, b:2, d:1; confirmed on the 1622 page image (n530)", '#auto'),  # [s]ucke
    579: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n530)", '#auto'),  # [a]nd
    580: ('fo', 'high', 'by hand: to lay them [fo]rth for ostentation?; confirmed on the 1622 page image (n530)', '#editor'),  # [fo]rth
    581: ('w', 'high', 'by hand: no warrant for that in all Gods [w]ord', '#editor'),  # [w]ord
    582: ('n', 'high', 'by hand: there is [n]o milke in the breasts', '#editor'),  # [n]o
    583: ('ly', 'high', "the book's own vocabulary: ordinari_ -> ly:22", '#auto'),  # ordinari[ly]
    584: ('th', 'high', "the book's own vocabulary: _ey -> th:2982, ob:109, pr:5, wh:1; confirmed on the 1622 page image (n530)", '#auto'),  # [th]ey
    585: ('o', 'high', "the book's own vocabulary: _f -> o:10396, i:1181; confirmed on the 1622 page image (n530)", '#auto'),  # [o]f
    586: ('an', 'high', "the book's own vocabulary: _d -> an:8820, go:1102, ha:353, di:232; confirmed on the 1622 page image (n530)", '#auto'),  # [an]d
    587: ('th', 'high', "the book's own vocabulary: mo_ers -> th:104", '#auto'),  # mo[th]ers
    588: ('c', 'high', "the book's own vocabulary: _hilde -> c:356", '#auto'),  # [c]hilde
    589: ('c', 'high', "the book's own vocabulary: _hild -> c:29", '#auto'),  # [c]hild
    590: ('d', 'high', 'by hand: She was therefore a [d]rie nurse', '#editor'),  # [d]rie
    591: ('h', 'high', "the book's own vocabulary: _aue -> h:1133, g:102, s:13, r:1; confirmed on the 1622 page image (n532)", '#auto'),  # [h]aue
    592: ('d', 'high', 'by hand: those nurses might be [d]ead', '#editor'),  # [d]ead
    593: ('n', 'high', 'by hand: for want of milke, [n]ipple, or some other like defect', '#editor'),  # [n]ipple
    594: ('to', 'high', 'by hand: the childe which she [to]oke for her owne to nurse', '#editor'),  # [to]oke
    595: ('f', 'high', "the book's own vocabulary: o_ -> f:10396, r:1440, n:506, b:8; confirmed on the 1622 page image (n533)", '#auto'),  # o[f]
    596: ('f', 'high', "the book's own vocabulary: o_ -> f:10396, r:1440, n:506, b:8; confirmed on the 1622 page image (n533)", '#auto'),  # o[f]
    597: ('n', 'high', "the book's own vocabulary: _icenesse -> n:5 (auto(1 letters))", '#auto'),  # [n]icenesse
    598: ('n', 'high', "the book's own vocabulary: Elka_ah -> n:13", '#auto'),  # Elka[n]ah
    599: ('c', 'high', "the book's own vocabulary: _hildren -> c:1420", '#auto'),  # [c]hildren
    600: ('v', 'high', "the book's own vocabulary: _nder -> v:344, u:1; confirmed on the 1622 page image (n538)", '#auto'),  # [v]nder
    601: ('t', 'high', "the book's own vocabulary: _his -> t:2062", '#auto'),  # [t]his
    602: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n538)", '#auto'),  # [a]nd
    603: ('i', 'high', "the book's own vocabulary: _n -> i:5378, a:1059, o:506, v:1; confirmed on the 1622 page image (n538)", '#auto'),  # [i]n
    604: ('se', 'high', 'by hand: a faithfull and constant ob[se]ruance of this ordinance', '#editor'),  # ob[se]ruance
    605: ('e', 'high', "the book's own vocabulary: _lizabeth -> e:7", '#auto'),  # [e]lizabeth
    606: ('s', 'high', "read from the 1622 page image (n540), replacing the guess 't': Margin note: 'quod intelligitur Deus. Hier. in Eph.4.' -- the italic 's' is blotted but its shape and the full stop after it are visible; 'Deus' (God, one name of Father, Son and Spirit), not 'Deut'.", '#editor'),  # Deu[t]
    607: ('c', 'high', "the book's own vocabulary: _hildren -> c:1420", '#auto'),  # [c]hildren
    608: ('r', 'high', 'by hand: heathenish, idolatrous, [r]idiculous names', '#editor'),  # [r]idiculous
    609: ('d', 'high', "the book's own vocabulary: _oe -> d:944, g:174, w:12, r:6; confirmed on the 1622 page image (n544)", '#auto'),  # [d]oe
    610: ('b', 'high', "the book's own vocabulary: _aptised -> b:18", '#auto'),  # [b]aptised
    611: ('t', 'high', "the book's own vocabulary: congrega_ion -> t:2; confirmed on the 1622 page image (n544)", '#auto'),  # congrega[t]ion
    612: ('it', 'high', 'by hand: or to the childe [it] selfe', '#editor'),  # [it]
    613: ('r', 'high', "the book's own vocabulary: _eckoned -> r:21", '#auto'),  # [r]eckoned
    614: ('b', 'high', "the book's own vocabulary: _eginneth -> b:9", '#auto'),  # [b]eginneth
    615: ('f', 'high', 'by hand: till it be [f]it to be placed forth', '#editor'),  # [f]t
    616: ('ἐκτρέφετε αὐτὰ ἐν παιδεία', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n545): Eph 6:4; printed παι-|δεία with no iota subscript visible', '#editor'),  # ἐκτρέφετε αὐτὰ ἐν παιδεία
    617: ('r', 'high', "the book's own vocabulary: appa_ell -> r:62", '#auto'),  # appa[r]ell
    618: ('b', 'high', 'by hand: tagged and ragged like beggars [b]rats', '#editor'),  # [b]rats
    619: ('o', 'high', 'by hand: but [o]uer-strictly hold them in', '#editor'),  # [o]uer
    620: ('b', 'high', 'by hand: [b]ut plaine vnnaturalnesse in such parents', '#editor'),  # [b]ut
    621: ('th', 'high', "the book's own vocabulary: _e -> th:12236, ar:2300, on:990, do:944; confirmed on the 1622 page image (n546)", '#auto'),  # [th]e
    622: ('d', 'high', "the book's own vocabulary: ten_ernesse -> d:7", '#auto'),  # ten[d]ernesse
    623: ('da', 'high', "the book's own vocabulary: _intily -> da:2; confirmed on the 1622 page image (n546)", '#auto'),  # [da]intily
    624: ('παιδεία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n549): note * on 'The word nurture'", '#editor'),  # παιδεία
    625: ('εὐσχημόνως', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n549): note * on 'walke decently', Rom 13:13 εὐσχημόνως; σχ ligature", '#editor'),  # εὐσχημόνως
    626: ('', 'high', 'by hand: (in the way that he should go) -- the bullet is a blot', '#editor'),  # go[]
    627: ('', 'high', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words; confirmed on the 1622 page image (n552)', '#auto'),  # []grieuous
    628: ('', 'high', 'no letter lost: a blot or broken space, the letters on both sides already spell whole words; confirmed on the 1622 page image (n552)', '#auto'),  # []bane
    629: ('', 'high', 'by hand: Parents are bour[]d -- see TEXT_FIXES: printed "bound"', '#editor'),  # bour[]d
    630: ('ὑγιαίνοντοι λόγοι', 'medium', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n558): 2 Tim 1:13 (ὑγιαινόντων λόγων); the print clearly ends -ντοι (misprint for ὑγιαίνοντες?), transcribed as printed', '#editor'),  # ὑγιαίνοντοι λόγοι
    631: ('z', 'high', "the book's own vocabulary: solemni_ing -> z:5", '#auto'),  # solemni[z]ing
    632: ('o', 'high', 'by hand: workes of mercy [o]r of iudgement', '#editor'),  # [o]r
    633: ('t', 'high', "the book's own vocabulary: _he -> t:12236, s:713; confirmed on the 1622 page image (n560)", '#auto'),  # [t]he
    634: ('te', 'high', "read from the 1622 page image (n560), replacing the guess 'e': Gutter: the right edge of an 'e' then 'ach children from whence these come'. The word is 'teach' (parallel to 'instruct children in the causes thereof' just before), not 'each'; the lost span is 'te' (TCP has the gap before 'ach').", '#editor'),  # [e]ach
    635: ('lik', 'high', 'by hand: so [lik]ewise other masters (see TEXT_FIXES for the space)', '#editor'),  # so[lik]ewise
    636: ('h', 'high', "the book's own vocabulary: _er -> h:1661, i:23, p:10, v:6; confirmed on the 1622 page image (n560)", '#auto'),  # [h]er
    637: ('If', 'high', 'by hand: [If] masters themselues be religious', '#editor'),  # [If]
    638: ('', 'high', 'by hand: (same lacuna, second of three adjacent gaps)', '#editor'),  # If[]
    639: ('', 'high', 'by hand: (same lacuna, third of three adjacent gaps)', '#editor'),  # If[]
    640: ('d', 'high', "the book's own vocabulary: _oe -> d:944, g:174, w:12, r:6; confirmed on the 1622 page image (n560)", '#auto'),  # [d]oe
    641: ('th', 'high', 'by hand: very profitable to [th]e children', '#editor'),  # [th]e
    642: ('g', 'high', "the book's own vocabulary: _ood -> g:1027, f:55, w:6, h:5; confirmed on the 1622 page image (n560)", '#auto'),  # [g]ood
    643: ('שחרו מוּסר שחר', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n563): note c, Prov 13:24 שחרו מוסר, then שחר 'mane'; three lines; a dot (shuruk) by the ו of מוסר, otherwise unpointed", '#editor'),  # שחרו מוּסר שחר
    644: ('שחר', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n563): 'inde in Piel שחר mane facere'", '#editor'),  # שחר
    645: ('ἀπὸ βρέφους· Βρέφος τὸ ἄρτι γεγονὸς παιδίον', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n563): note d, 2 Tim 3:15 ἀπὸ βρέφους; then the gloss 'Βρέφος τὸ ἄρτι γεγονὸς παιδίον' (Puer recens natus); ους and ος ligatures", '#editor'),  # ἀπὸ βρέφους· Βρέφος τὸ ἄρτι γεγονὸς παιδίον
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
    660: ('τὰ τέκνα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n566): margin by 'word which in Scripture and other writers' (Children)", '#editor'),  # τὰ τέκνα
    661: ('νουθεσία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n568): first margin entry, 'See Treat. 1. §. 120' (admonition)", '#editor'),  # νουθεσία
    662: ('παιδεία', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n568): second entry, 'See Treat. 1. §. 119' (nurture)", '#editor'),  # παιδεία
    663: ('שנן', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n568): note g, Deut 6:7 (root of ושננתם) 'Acuit. in Piel acuit valde'; unpointed", '#editor'),  # שנן
    664: ('n', 'high', 'by hand: more peruersenesse and vntowardnesse i[n] such parents', '#editor'),  # i[n]
    665: ('u', 'high', 'by hand: illos & seipsum [u]na perdidit (Chrys. in 1 Tim. hom. 9)', '#editor'),  # [u]na
    666: ('', 'high', 'by hand: therein, he brought destruction -- the bullet is a blot', '#editor'),  # []he
    667: ('l', 'high', 'by hand: who are [l]oth to giue them a foule word', '#editor'),  # [l]oth
    668: ('', 'high', "read from the 1622 page image (n570), replacing the guess 'e': Gutter: the line begins with the clipped 'v' of 'very wise man)'; the TCP already has 'very' after its gap, so nothing is lost. Read 'a very wise man', not 'a every wise man' (fill should be empty).", '#editor'),  # [e]very
    669: ('n', 'high', "the book's own vocabulary: _ot -> n:2211, h:7, g:6, w:3; confirmed on the 1622 page image (n570)", '#auto'),  # [n]ot
    670: ('a', 'high', "the book's own vocabulary: Ch_sten -> a:1; confirmed on the 1622 page image (n571)", '#auto'),  # Ch[a]sten
    671: ('e', 'high', 'by hand: semetipsos in furorem iudicij dem[e]rgunt (Orig. in Iob)', '#editor'),  # dem[e]rgunt
    672: ('e', 'high', "the book's own vocabulary: d_inceps -> e:1; confirmed on the 1622 page image (n580)", '#auto'),  # d[e]inceps
    673: ('a', 'high', "the book's own vocabulary: _nd -> a:8820, e:132; confirmed on the 1622 page image (n580)", '#auto'),  # [a]nd
    674: ('v', 'high', 'by hand: to be of little [v]se', '#editor'),  # [v]se
    675: ('fit', 'high', 'by hand: though children be neuer so [fit] for these callings', '#editor'),  # [fit]
    676: ('n', 'high', 'by hand: God hath placed such a[n] one in his place', '#editor'),  # a[n]
    677: ('', 'medium', "read from the 1622 page image (n581), replacing the guess 'ir': Gutter side of p.562: the line ends 'relinquish the' with the 'e' half under the fold, then 'place.' on the next line. Nearby lines lose only their last letter at the fold ('fait[h]', 'knowin[g]'), and the 'e' is in that last-letter spot, so the justified line seems to end at 'the': read 'relinquish the place', no letters lost. TCP marked 2 illegible letters and 'their place' is also Gouge's phrase elsewhere, so only medium.", '#editor'),  # the[ir]
    678: ('t', 'high', 'by hand: Ma[t]. 6. 19. expounded', '#editor'),  # Ma[t]
    679: ('θησαυρίζειν ἀπὸ τοῦ τιθέναι εἰς αὔριον', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n585): note * on 'treasuring vp' (Matt 6:19), etymology 'from laying up for tomorrow'; lines 2-3 clear (ρ of αὔριον worn); end of first word is a ligature read as -ειν, could be another ending of θησαυρίζ-", '#editor'),  # θησαυρίζειν ἀπὸ τοῦ τιθέναι εἰς αὔριον
    680: ('τὰ τέκνα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): margin by 'this word ( Children )'", '#editor'),  # τὰ τέκνα
    681: ('τέκνα ἀγαπητά', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): Eph 5:1 τέκνα ἀγαπητά (printed τέκνα' ἀγα-|πητά with a stray grave-like mark after τέκνα)", '#editor'),  # τέκνα ἀγαπητά
    682: ('בנך את־יחידך τὸν υἱόν σου τὸν ἀγαπητὸν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): Gen 22:2 Hebrew (line order: את־ ... -בנך then יחידך, read as בנך את־יחידך; a hireq under ח) followed by LXX τὸν υἱόν σου τὸν ἀγαπητὸν (final accent printed grave), all before 'Hesychius'", '#editor'),  # בנך את־יחידך τὸν υἱόν σου τὸν ἀγαπητὸν
    683: ('ἀγαπητὸν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): 'Hesychius ἀγαπητὸν exponit'", '#editor'),  # ἀγαπητὸν
    684: ('μονογενῆ', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): 'exponit μονογενῆ' (γε ligature, circumflex over η)", '#editor'),  # μονογενῆ
    685: ('ἀγαπητὸν υἱὸν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): 'Plutarchus dicit ἀγαπητὸν υἱὸν vocari'", '#editor'),  # ἀγαπητὸν υἱὸν
    686: ('μοῦνον', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): 'vocari μοῦνον' (ου ligature with circumflex)", '#editor'),  # μοῦνον
    687: ('ἀγαπητὸν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n594): 'Arist. Rhet. 1. vocat vnicum oculum ἀγαπητόν', printed ἀγα-|πητὸν with grave", '#editor'),  # ἀγαπητὸν
    688: ('et', 'high', "the book's own vocabulary: comp_ent -> et:6 (auto(2 letters))", '#auto'),  # comp[et]ent
    689: ('in', 'high', 'by hand: [in] case God take them away', '#editor'),  # [in]n
    690: ('u', 'high', "the book's own vocabulary: pro_ided -> u:36, v:1; confirmed on the 1622 page image (n596)", '#auto'),  # pro[u]ided
    691: ('ll', 'high', 'by hand: as a[ll] their care is to aduance their eldest sonne', '#editor'),  # a[ll]
    692: ('n', 'high', 'by hand: and i[n] the meane while neglect their younger children', '#editor'),  # i[n]
    693: ('τέκνα ἀγαπητά', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n600): note o, Eph 5:1', '#editor'),  # τέκνα ἀγαπητά
    694: ('τοὺς ἰδίους', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n603): note * on 'a mans OVVNE', 1 Tim 5:8 τῶν ἰδίων... printed τοὺς ἰδίους", '#editor'),  # τοὺς ἰδίους
    695: ('n', 'high', "the book's own vocabulary: _iggardly -> n:2; confirmed on the 1622 page image (n604)", '#auto'),  # [n]iggardly
    696: ('x', 'high', 'by hand: ...phrontisteria... constru[x]it (Niceph. eccl. hist.)', '#editor'),  # constru[x]
    697: ('h', 'high', "the book's own vocabulary: _eauen -> h:117", '#auto'),  # [h]eauen
    698: ('אדון', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n614): note * on 'Lord', Gen 24:9; unpointed", '#editor'),  # אדון
    699: ('Κύριος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n614): 'Κύριος. Eph. 6. 5.'", '#editor'),  # Κύριος
    700: ('ὑπακούετε', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n615): note d on 'Greeke word ... Obey', Eph 6:5 ὑπακούετε; ου ligature", '#editor'),  # ὑπακούετε
    701: ('l', 'high', 'by hand: the seruants of Lidia, and of the Iay[l]er', '#editor'),  # Iay[l]er
    702: ('μὴ ἀντιλέγοντας', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n632): note b, Tit 2:9, printed μὴ ἀντιλέ-|γοντας', '#editor'),  # μὴ ἀντιλέγοντας
    703: ('τὴν παρακαταθήκην φύλαξον', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n642): note b, 1 Tim 6:20; τὴν and παρα printed as ligatures (smudged), rest clear', '#editor'),  # τὴν παρακαταθήκην φύλαξον
    704: ('μὴ νοσφιζομένους', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n644): note b, Tit 2:10, printed νοσφιζο-|μένους, ου ligature', '#editor'),  # μὴ νοσφιζομένους
    705: ('ἐνοσφίσατο', 'high', 'read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n644): note c, Acts 5:2; -σατο as ligature', '#editor'),  # ἐνοσφίσατο
    706: ('Κύριος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n660): p.641 margin beside 'The word which the Apostle vseth in Greeke'; capital K, -ος ligature", '#editor'),  # Κύριος
    707: ('εἷς κύριος', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n660): p.641 note c under '1 Cor. 8.6.'; -ος ligature; breathing/accent on εἷς small but matches 1 Cor 8:6", '#editor'),  # εἷς κύριος
    708: ('τοῦ ἰδίου οἴκου προϊστάμενον εὖ', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n669): p.650 note a under '1 Tim. 3.4.', four lines; ου and προ ligatures clear; last line a single εὖ ligature with breathing and circumflex (Gouge's 'well'; the NT has καλῶς), read as εὖ but the ligature is cramped", '#editor'),  # τοῦ ἰδίου οἴκου προϊστάμενον εὖ
    709: ('οἰκοδεσποτεῖν', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n669): p.650 note b under '1 Tim. 5.14.'; 1 Tim 5:14; σπ ligature smudged but word certain", '#editor'),  # οἰκοδεσποτεῖν
    710: ('אף ab אנף', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n677): p.658 margin note keyed '*' beside 'In Hebrew the same word signifieth a face, and wrath'. Letters certain, unpointed: אנף and אף with Latin 'ab' between (the TCP has no 'ab', so the gap covers the whole note). Visually the line runs '* אנף ab אף' left to right; given here in sense order 'af from anaf' (noun from the root). If kept in visual order: 'אנף ab אף'.", '#editor'),  # אף ab אנף
    711: ('τὸ δίκαιον καὶ τὴν ἰσότητα', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n684): p.665 note * under 'Coloss. 4.1.'; ϗ compendium expanded to καὶ, τ with superscript ην expanded to τὴν; matches Col 4:1", '#editor'),  # τὸ δίκαιον καὶ τὴν ἰσότητα
    712: ('σιτομέτριον', 'medium', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n688): p.669 note * under 'Luk. 12. 42.' (Luke 12:42, 'portion'). σι, το ligature, μέ clear; the -τρι- is blurred and could be read -τει- (misprint or ligature); given as the NT word", '#editor'),  # σιτομέτριον
    713: ('שנים', 'high', "read from the 1622 page image (archive.org bim_early-english-books-1475-1640_of-domesticall-duties-ei_gouge-william_1622, n689): p.670 note * under 'Pro. 31.21.'; unpointed, wide final mem; Prov 31:21 'scarlet'/'double', as the text explains", '#editor'),  # שנים
    714: ('D', 'medium', "read from the 1622 page image (n710), replacing the guess 'd': Margin note (p.691 is index 710): first letter broken, only faint specks before 'ominus fidelem habens seruum'. The note opens a Latin sentence (Const. Apost.), and the same note has 'Dominum patrem' capitalized, so the letter was a capital 'D'; case only.", '#editor'),  # [d]ominus
    715: ('t', 'high', 'by hand: vt fra[t]rem propter fidei societatem (Constit. Apost.)', '#editor'),  # fra[t]rem
    716: ('n', 'high', "the book's own vocabulary: Se_ec -> n:3; confirmed on the 1622 page image (n710)", '#auto'),  # Se[n]ec
    717: ('tuum', 'high', 'by hand: istum quem seruum [tuum] vocas (Seneca, Ep. 47)', '#editor'),  # [tuum]
    718: ('r', 'high', 'by hand: the errata list: "ibid. in ma[r]g. l. 8." (in the margin)', '#editor'),  # ma[r]g
}
