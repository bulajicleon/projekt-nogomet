# Analiza nogometnih tekem (Premier League, La Liga, Bundesliga)

Projektna naloga pri predmetu Uvod v programiranje. Program zajame podatke o
10.426 nogometnih tekmah (Premier League 2010/11-2020/21, La Liga 2012/13-2020/21,
Bundesliga 2010/11-2020/21), jih ustrezno predela, shrani in analizira
(povprecno stevilo golov po ligi, domaca prednost, trend skozi sezone, derbiji).

Vir podatkov: [footballcsv](https://github.com/footballcsv) - javno dostopni
(public domain, CC0) rezultati tekem v CSV obliki.

## Struktura projekta

- `zajem.py` - Prenaša surove CSV datoteke z GitHuba (footballcsv) za izbrane lige/sezone in jih shranjuje v `podatki/csv/`.
- `izluscenje.py` - Prebere lokalne CSV datoteke, izlusci rezultat iz stolpca "FT" (npr. "2-1"), preskoci preložene/manjkajoce tekme.
- `naredi_csv.py` - Zapisuje ociscene podatke v `podatki/tekme.csv`.
- `main.py` - Glavna skripta, ki poveze celoten cevovod (zajem -> izluscenje -> shranjevanje).
- `analiza_funkcije.py` - Pomozne funkcije za analizo (dolocitev zmagovalca, veliko golov, prepoznavanje derbijev), locene od notebooka zaradi berljivosti.
- `analiza.ipynb` - Jupyter zvezek z dejansko analizo in grafi na pravih podatkih.
- `tekme.csv` - Koncni, ze pripravljen nabor podatkov (10.426 vrstic), ce ne zelis znova poganjati zajema.
- `uporaba-ui.md` - Dokumentacija uporabe orodij umetne inteligence pri nastajanju projekta.

## Namestitev

```
python -m venv venv
.\venv\Scripts\Activate.ps1      # na macOS/Linux: source venv/bin/activate
pip install requests pandas matplotlib jupyter
```

## Zagon

```
python main.py
```

To znova prenese vse CSV-je z GitHuba in obnovi `podatki/tekme.csv`. Ce zelis
samo ponovno sestaviti CSV iz ze prenesenih surovih datotek (brez ponovnega
prenosa), poženi:

```
python main.py --skip-download
```

Ce ti ni treba nič spreminjati, je `tekme.csv` že priložen in ga lahko takoj
odpreš v `analiza.ipynb`.

## Kaj vsebuje analiza (analiza.ipynb)

Notebook je ze izveden (vsebuje prave grafe in izpise, ni ga treba poganjati,
da vidis rezultate), z naslednjimi razdelki:

1. Osnovni pregled podatkov (stevilo tekem/sezon po ligi)
2. Ciscenje podatkov - poenotenje razlicnih zapisov imen ekip
3. Povprecno stevilo golov na tekmo po ligi
4. Trend golov skozi sezone - primerjava vseh treh lig na enem grafu
5. Porazdelitev stevila golov na tekmo (histogrami)
6. Domaca prednost po ligi (H/D/A)
7. Domaca prednost skozi cas (vkljucno z opazbo o sezonah brez gledalcev, COVID-19)
8. Najboljse napadalne ekipe po ligi (povprecje golov/tekmo)
9. Tekme z veliko goli in prepoznani derbiji
10. Ekstremi - tekme z najvec goli
11. Strnjene zakljucne ugotovitve

## Ugotovitve (na dejanskih podatkih)

- Bundesliga ima v povprecju najvec golov na tekmo (~2,96), sledita Premier League (~2,74) in La Liga (~2,71).
- Domaca prednost je v vseh treh ligah podobna: ~45% zmag domacih, ~24-25% neodlocenih, ~29-31% zmag gostov - a v sezonah brez gledalcev (2019/20-2020/21, COVID-19) opazno pade, kar podpira hipotezo o vplivu navijacev.
- Vec kot 4 gole je padlo na 1.573 od 10.426 tekem (~15%).
- Imena ekip niso vedno zapisana konsistentno skozi sezone (npr. "Everton" vs "Everton FC") - to je bilo treba popraviti (glej `normaliziraj_ime_ekipe` v `analiza_funkcije.py`), preden je analiza po ekipah sploh smiselna.
- Vodilne ekipe (Bayern München, Real Madrid, Barcelona, Manchester City) dosegajo bistveno vec golov od povprecja lige.
