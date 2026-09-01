# Analiza nogometnih tekem (Premier League, La Liga, Bundesliga)

Projektna naloga pri predmetu Uvod v programiranje. Program zajame podatke o
več kot 10.000 nogometnih tekmah (Premier League 2010/11-2020/21, La Liga
2012/13-2020/21, Bundesliga 2010/11-2020/21), jih ustrezno predela, shrani in
analizira (povprečno število golov po ligi, domača prednost, trend skozi
sezone, derbiji).
Moj vir podatkov: footballcsv - javno dostopni
(public domain, CC0) rezultati tekem v CSV obliki.


## Struktura projekta

`zajem.py` - Prenaša surove CSV datoteke z GitHuba (footballcsv) za izbrane lige/sezone in jih shranjuje v `podatki/csv/`.
`izluscenje.py` - Prebere lokalne CSV datoteke, izlušči rezultat iz stolpca "FT" (npr. "2-1"), preskoči preložene/manjkajoče tekme.
`naredi_csv.py` - Zapisuje očiščene podatke v `podatki/tekme.csv`.
`main.py` - Glavna skripta, ki poveže celoten cevovod (zajem -> izluščenje -> shranjevanje).
`analiza_funkcije.py` - Pomožne funkcije za analizo (določitev zmagovalca, veliko golov, prepoznavanje derbijev), ločene od notebooka zaradi berljivosti.
`analiza.ipynb` - Jupyter zvezek z dejansko analizo in grafi na pravih podatkih.
`tekme.csv` - Končni, že pripravljen nabor podatkov (10.426 vrstic), če ne želiš znova poganjati zajema.
`uporaba-ui.md` - Dokumentacija uporabe orodij umetne inteligence pri nastajanju projekta.

## Kaj vsebuje analiza (analiza.ipynb)

Notebook je že izveden (vsebuje prave grafe in izpise, ni ga treba poganjati,
da vidiš rezultate), z naslednjimi razdelki:
1. Osnovni pregled podatkov (število tekem/sezon po ligi)
2. Čiščenje podatkov - poenotenje različnih zapisov imen ekip
3. Povprečno število golov na tekmo po ligi
4.  Trend golov skozi sezone - primerjava vseh treh lig na enem grafu
5. Porazdelitev števila golov na tekmo (histogrami)
6. Domača prednost po ligi (zmage domačih/gostov/neodločeno)
7. Domača prednost skozi čas (vključno z opazko o sezonah brez gledalcev, COVID-19)
8. Najboljše napadalne ekipe po ligi (povprečje golov/tekmo)
9. Tekme z veliko goli in prepoznani derbiji
10. Ekstremi - tekme z največ goli
11. Strnjene zaključne ugotovitve


## Ugotovitve (na dejanskih podatkih)
  V narejeni analizi sem prišel do raznih ugotovitev.
-Bundesliga ima v povprečju največ golov na tekmo (~2,96), sledita Premier League (~2,74) in La Liga (~2,71).
-Domača prednost je v vseh treh ligah podobna: ~45 % zmag domačih, ~24-25 % neodločenih, ~29-31 % zmag gostov - a v sezonah brez gledalcev (2019/20-2020/21, COVID-19) opazno pade, kar podpira hipotezo o vplivu navijačev na rezultat.
- Več kot 4 gole je padlo na 1.573 od 10.426 tekem (~15%).
- Imena ekip niso vedno zapisana konsistentno skozi sezone (npr. "Everton" vs "Everton FC") - to je bilo treba popraviti (glej `normaliziraj_ime_ekipe` v `analiza_funkcije.py`), preden je analiza po ekipah sploh smiselna.
- Vodilne ekipe (Bayern München, Real Madrid, Barcelona, Manchester City) dosegajo bistveno več golov od povprečja lige.
