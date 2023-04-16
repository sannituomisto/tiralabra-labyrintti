"""Labyrinttien hausta vastaava moduuli.
"""


def labyrintin_haku(labyrintin_nro):
    """Hakee labyrintit tiedostoista.

    Args:
        labyrintin_nro (int): haettavan labyrintin numero

    Returns:
        Tiedostosta luetun labyrintin listassa.
    """
    labyrintti = []
    if labyrintin_nro <= 5:
        with open("20x20labyrintit/labyrintti"+str(labyrintin_nro)+".txt", encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.replace("\n", "")
                labyrintti.append(list(rivi))
    # Tähän tulee mahdollisesti vielä isompien labyrinttien hakeminen.
    return labyrintti
