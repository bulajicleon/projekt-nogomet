import os
import time
import requests


MAPA_PODATKI = "podatki"
MAPA_CSV = os.path.join(MAPA_PODATKI, "csv")


OSNOVNI_URL = "https://raw.githubusercontent.com/footballcsv"


LIGE = [
    ("england", "eng.1", "Premier League",
     ["2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16",
      "2016-17", "2017-18", "2018-19", "2019-20", "2020-21"]),
    ("espana", "es.1", "La Liga",
     ["2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18",
      "2018-19", "2019-20", "2020-21"]),
    ("deutschland", "de.1", "Bundesliga",
     ["2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16",
      "2016-17", "2017-18", "2018-19", "2019-20", "2020-21"]),
]


def desetletje_mape(sezona):
    """Iz '2013-14' vrne '2010s', kot uporablja footballcsv v strukturi map."""
    zacetno_leto = int(sezona[:4])
    desetletje = (zacetno_leto // 10) * 10
    return f"{desetletje}s"


def prenesi_csv(repozitorij, koda_lige, sezona):
    """Prenese en CSV (ena liga, ena sezona) in ga shrani lokalno."""
    os.makedirs(MAPA_CSV, exist_ok=True)

    ime_datoteke = f"{repozitorij}_{koda_lige}_{sezona}.csv"
    pot_datoteke = os.path.join(MAPA_CSV, ime_datoteke)

    if os.path.exists(pot_datoteke):
        print(f"{repozitorij} {koda_lige} {sezona} je že prenesena, preskakujem.")
        return

    mapa = desetletje_mape(sezona)
    url = f"{OSNOVNI_URL}/{repozitorij}/master/{mapa}/{sezona}/{koda_lige}.csv"
    print(f"Prenašam: {url}")

    odziv = requests.get(url)
    if odziv.status_code == 200:
        with open(pot_datoteke, "w", encoding="utf-8") as f:
            f.write(odziv.text)
    else:
        print(f"Napaka pri {repozitorij} {koda_lige} {sezona}: status {odziv.status_code}")

    time.sleep(0.3)


def prenesi_vse():
    """Prenese CSV datoteke za vse lige in sezone, definirane v LIGE."""
    for repozitorij, koda_lige, _prikazno_ime, sezone in LIGE:
        for sezona in sezone:
            prenesi_csv(repozitorij, koda_lige, sezona)
    print("Prenos končan.")


if __name__ == "__main__":
    prenesi_vse()
