import argparse
from zajem import prenesi_vse
from izluscenje import izlusci_podatke
from naredi_csv import shrani_v_csv


def glavna_funkcija():
    parser = argparse.ArgumentParser(
        description="Celoten cevovod za zajem, obdelavo in shranjevanje podatkov o nogometnih tekmah."
    )
    parser.add_argument(
        "-s", "--skip-download",
        action="store_true",
        help="Preskoči prenos CSV datotek s spleta (uporabi že shranjene datoteke)."
    )
    argumenti = parser.parse_args()

    if not argumenti.skip_download:
        prenesi_vse()
    else:
        print("Preskakujem prenos, uporabljam že shranjene CSV datoteke.")

    tekme = izlusci_podatke()
    shrani_v_csv(tekme)


if __name__ == "__main__":
    glavna_funkcija()
