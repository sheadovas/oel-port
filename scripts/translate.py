import goslate

raw = [
" gehoert ihnen nicht!",
" geht nicht!",
" gelungen ",
" gesamt = ",
" gesellschaft oelfeld preis $",
"gesellschaft preis besitzer ",
" gesellschaft preis besitzer",
" gesellschaft pumpenpreis in $",
" g = tankwagen",
"happybohr ",
" hey, hier ist agent diabolo huggi baer",
" hier das gesamtergebnis:",
" hier faellt die entscheidung !",
" h = naechster spieler",
" ich hoffe sie hatten viel freude und",
"ihren bohrgestaengepreis fuer 500 m fest",
" ihr kapital betraegt jetzt",
" ihr kapital $",
" ihr oelfeldlagerverwalter teilt ihnen",
" ihr or aben ist gelungen!",
" ihr tankwagenpreis",
"immerdruck ",
" i = sabotage betreiben",
"jahr:",
" jetzt zahlbar : 5 0 0 0.-- $",
" j = preisfestlegung",
"j neuer lkw-preis",
" kapital $",
"kauf bei welcher firma ",
"kauf von wieviel lkw ",
"kauf von wieviel pumpen",
" kein angebot",
"kein angebot",
"kein angebot da",
" keine festlegung",
"keine mehr da",
" kein kauf = 'x'",
"knaltex gmbh ",
" k = weitermachen",
" lassen. = f1",
" lassen. = f5",
" legen sie den pumpenpreis fest",
"legen sie den pumpenpreis fest",
"leider muessen wir ihnen mitteilen, dass",
" lieber doch nichts machen. = 'x'",
" liegt noch kein angebot vor",
"liquides kapital:$",
" lkwkapazitaet:",
"lkwkauf bei welcher firma",
" lkwzahl :",
"lucky hole ",
" mehr or anden. wir brauchen nachschub!",
" misslungen",
" mit dem meisten kapital am ende",
"n",
" neuer preis",
"never & again ",
"never come back",
" noch zahlbar $",
" nr",
" nr firma anzahl preis",
"nr firma gestaengepreis",
" nr f i r m a lkw preis ",
"nr firma pumpenpreis",
"nr firma tankwagenpreis",
" o e l f e l d a n g e b o t e ",
" oelfeldnummer",
"oil on the road",
" or en, sprengs to ff etc = ",
" or ueber",
"overbubble ",
"pech gehabt",
" preis neu festlegen?",
" preis :$",
" pumpe ",
" pumpenanzahl :",
" pumpenfirma durch sabotage ausser",
" & pumpenvereinigungsgesellschaft",
" ** pumpenverkaeuferangebote ** ",
" quelle erschoepft!",
" raffke und sohn bankkreditabteilung ",
" Raffke und Sohn einen Bankkredit von",
"raff und gier ",
"ra$ raffinerieabnahmepreis = $",
" o e l f e l d ",
" sabotageergebnis durch tastendruck",
" sabotiert und uebernommen werden?",
"sala to il inc ",
" schade - das wir nicht ins geschaeft kommen",
"sell & hopp ",
"sie besitzen ein or aufsrecht auf die",
" sieger ist logischer weise der",
" sie haben die ",
" sie nicht wollen druecken sie 'x'",
" sie sind nun besitzer der firma:",
" sie sind nun besitzer der firma:",
"sie sind nun inhaber der gesellschaft legen sie nun",
" zu lang",
" so. fuer die sabotage des oelfeldes",
" soll ich zur tat schreiten?",
" soll sabotiert werden?",
"spc(t)sabotageaktion",
" spesen, schmiergelder etc = ",
" spiel",
" spieler bankkredit kapital",
" stehen zur verfuegung:",
"swimminoil inc",
" tankwagen :",
" tankwagenfirma durch bestechhung",
" t a n k w a g e n f i r m e n ",
" ** tankwagenverkaufsangebote ** ",
" teilt mit:",
"turbo & drill gmbh ",
" unrealistisch!",
" unterbreiten.",
" verbleibe als ihr oely.",
" v e r k a u f ",
"verkauft",
" versandmenge :",
"von ihnen sabotierte tankwagenfirma:",
" welche der folgenden bohrgesellschaft-",
" welche der folgenden pumpenfirmen soll",
" welche der folgenden tankwagenfirmen",
" welche firma",
" welche firma (nr)",
" welche gesellschaft wollen sie kaufen?",
"welches feld soll gekauft werden? @}",
" welches oelfeld soll ich sabotieren?",
" wenn sie eine fabrik kaufen wollen;",
"wieviel 500m einheiten wollen sie",
" wieviel liter sollen weg",
" wir koennen ihnen folgende angebote",
" wir sind fuendig.",
" wollen sie kaufen (j/n)?",
"zu hoch!",
"zum verkauf ansteht.",
" zur zeit keine pumpenherstellungsfirma",
" zuviel"
]


gs = goslate.Goslate()
for s in raw:
    t =  gs.translate(s, 'en', 'de')
    print "%s -> %s" % (s, t)
