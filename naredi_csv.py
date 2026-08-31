import os
import pandas as pd
from izluscenje import izlusci_podatke

MAPA_PODATKI = "podatki"
POT_CSV = os.path.join(MAPA_PODATKI, "tekme.csv")


def shrani_v_csv(podatki):
    if podatki is None or len(podatki) == 0:
        print("Opozorilo: Podatki so prazni!")
        return

    os.makedirs(MAPA_PODATKI, exist_ok=True)

    df = pd.DataFrame(podatki)
    df.to_csv(POT_CSV, index=False, encoding="utf-8-sig")

    print(f"Podatki so bili uspešno shranjeni v '{POT_CSV}'.")
    print(f"Skupaj zapisanih vrstic: {len(df)}")


if __name__ == "__main__":
    tekme = izlusci_podatke()
    shrani_v_csv(tekme)
