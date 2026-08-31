import pandas as pd


def doloci_zmagovalca(vrstica):
    """Vrne 'Domacini', 'Gostje' ali 'Neodloceno' glede na goli_domaci/goli_gosti."""
    if pd.isna(vrstica["goli_domaci"]) or pd.isna(vrstica["goli_gosti"]):
        return "Ni podatkov"
    elif vrstica["goli_domaci"] > vrstica["goli_gosti"]:
        return "Domacini"
    elif vrstica["goli_domaci"] < vrstica["goli_gosti"]:
        return "Gostje"
    else:
        return "Neodloceno"


def je_veliko_golov(vrstica, prag=4):
    """Vrne True, ce je bilo na tekmi vec golov kot prag (privzeto 4)."""
    if pd.isna(vrstica["goli_domaci"]) or pd.isna(vrstica["goli_gosti"]):
        return False
    return (vrstica["goli_domaci"] + vrstica["goli_gosti"]) > prag


# Imena ekip se skozi sezone rahlo razlikujejo (npr. "Everton" vs "Everton FC",
# "Manchester Utd" vs "Manchester United FC"), zato pri prepoznavanju derbijev
# preverjamo, ali kljucna beseda nastopa v imenu ekipe, namesto tocnega ujemanja.
ZNANI_DERBIJI = [
    ({"Manchester United", "Manchester Utd"}, {"Manchester City"}),
    ({"Liverpool"}, {"Everton"}),
    ({"Real Madrid"}, {"FC Barcelona", "Barcelona"}),
]


def _vsebuje_katero(ime_ekipe, mnozica_kljucnih_besed):
    for kljucna_beseda in mnozica_kljucnih_besed:
        if kljucna_beseda in ime_ekipe:
            return True
    return False


def je_derbi(vrstica):
    """Vrne True, ce gre tekma med dvema ekipama iz istega znanega derbija."""
    domaca = vrstica["domaca_ekipa"]
    gostujoca = vrstica["gostujoca_ekipa"]

    for ekipe_a, ekipe_b in ZNANI_DERBIJI:
        domaca_v_a = _vsebuje_katero(domaca, ekipe_a)
        gostujoca_v_b = _vsebuje_katero(gostujoca, ekipe_b)
        domaca_v_b = _vsebuje_katero(domaca, ekipe_b)
        gostujoca_v_a = _vsebuje_katero(gostujoca, ekipe_a)
        if (domaca_v_a and gostujoca_v_b) or (domaca_v_b and gostujoca_v_a):
            return True
    return False


# Posebni primeri, kjer se ime ekipe skozi sezone razlikuje bolj kot le
# s priponko (npr. okrajšava namesto polnega imena).
ALIASI_EKIP = {
    "Manchester Utd": "Manchester United",
    "Newcastle Utd": "Newcastle United",
    "Sheffield Utd": "Sheffield United",
    "West Brom": "West Bromwich Albion",
    "Wolves": "Wolverhampton Wanderers",
    "Tottenham": "Tottenham Hotspur",
    "West Ham": "West Ham United",
}

PRIPONKE_ZA_ODSTRANITI = (" FC", " AFC", " CF")


def normaliziraj_ime_ekipe(ime):
    """
    Poenoti razlicne zapise istega imena ekipe (npr. 'Everton FC' -> 'Everton',
    'Manchester Utd' -> 'Manchester United'), da lahko ekipe pravilno grupiramo
    skozi vec sezon.
    """
    ime = ime.strip()
    for priponka in PRIPONKE_ZA_ODSTRANITI:
        if ime.endswith(priponka):
            ime = ime[: -len(priponka)]
            break
    return ALIASI_EKIP.get(ime, ime)
