import os
import csv
import re

MAPA_PODATKI = "podatki"
MAPA_CSV = os.path.join(MAPA_PODATKI, "csv")


PRIKAZNA_IMENA_LIG = {
    "eng.1": "Premier League",
    "es.1": "La Liga",
    "de.1": "Bundesliga",
}


VZOREC_REZULTATA = re.compile(r"^\s*(\d+)\s*[-–]\s*(\d+)\s*$")


def razcleni_rezultat(besedilo):
    """Iz niza kot '2-1' vrne (2, 1); ob manjkajočem/neveljavnem rezultatu (None, None)."""
    if not besedilo:
        return None, None
    ujemanje = VZOREC_REZULTATA.match(besedilo)
    if not ujemanje:
        return None, None
    return int(ujemanje.group(1)), int(ujemanje.group(2))


def izlusci_eno_datoteko(pot_datoteke, ime_lige, sezona):
    """Prebere eno surovo CSV datoteko in vrne seznam očiščenih vrstic (slovarjev)."""
    očiščeni_seznam = []

    with open(pot_datoteke, "r", encoding="utf-8", errors="ignore") as f:
        bralec = csv.DictReader(f)

        for vrstica in bralec:
            domaca_ekipa = vrstica.get("Team 1")
            gostujoca_ekipa = vrstica.get("Team 2")
            rezultat_besedilo = vrstica.get("FT")

            if not domaca_ekipa or not gostujoca_ekipa:
                continue

            goli_domaci, goli_gosti = razcleni_rezultat(rezultat_besedilo)
            if goli_domaci is None:
                continue

            ocisceni_zapis = {
                "datum": vrstica.get("Date"),
                "domaca_ekipa": domaca_ekipa,
                "gostujoca_ekipa": gostujoca_ekipa,
                "goli_domaci": goli_domaci,
                "goli_gosti": goli_gosti,
                "liga": ime_lige,
                "sezona": sezona,
            }
            očiščeni_seznam.append(ocisceni_zapis)

    return očiščeni_seznam


def izlusci_podatke():
    """Prebere vse surove CSV datoteke v podatki/csv/ in vrne skupen seznam vrstic."""
    vse_tekme = []

    if not os.path.isdir(MAPA_CSV):
        print(f"Mapa {MAPA_CSV} ne obstaja. Najprej poženi zajem.py.")
        return vse_tekme

    datoteke = [f for f in os.listdir(MAPA_CSV) if f.endswith(".csv")]
    datoteke.sort()

    print(f"Začenjam obdelavo {len(datoteke)} CSV datotek...")

    for ime_datoteke in datoteke:
        
        deli = ime_datoteke.replace(".csv", "").split("_")
        koda_lige = deli[1]
        sezona = deli[2]
        ime_lige = PRIKAZNA_IMENA_LIG.get(koda_lige, koda_lige)

        pot_datoteke = os.path.join(MAPA_CSV, ime_datoteke)
        tekme_iz_datoteke = izlusci_eno_datoteko(pot_datoteke, ime_lige, sezona)
        for tekma in tekme_iz_datoteke:
            vse_tekme.append(tekma)

    print(f"Izluščenje uspešno zaključeno! Skupaj tekem: {len(vse_tekme)}")
    return vse_tekme


if __name__ == "__main__":
    izlusci_podatke()
