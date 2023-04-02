"""Dead end filling- algoritmin toiminnasta vastaava moduuli käyttöliittymän puolella.
"""

from front_end.nayta_labyrintti import labyrintin_nro
from front_end.nayta_labyrintti import labyrintin_koko
from front_end.nayta_labyrintti import labyrintin_haku
from front_end.nayta_labyrintti import labyrintin_visualisointi
from dead_end_filling import dead_end_filling


def nayta_dead_end_filling():
    """Hakee ja vie kaksi eri labyrinttia tulostettavaksi. Toinen on labyrintti, jossa
    on merkitty umpikujat ja toinen on labyrintti, jossa on umpikujat täytetty ja vain ratkaistu polku
    näkyvillä. 
    """
    laby_nro = labyrintin_nro()
    laby_koko = labyrintin_koko(laby_nro)
    labyrintti = labyrintin_haku(laby_nro)
    labyrintti2 = labyrintin_haku(laby_nro)
    ratkaistu_labyrintti, umpikujat = dead_end_filling(labyrintti, laby_koko)
    labyrintti_umpikujilla = umpikujat_labyrinttiin(labyrintti2, umpikujat)
    print('\r')
    print('Labyrintin umpikujat:')
    labyrintin_visualisointi(labyrintti_umpikujilla, laby_koko)
    print('\r')
    print('Ratkaisu:')
    labyrintin_visualisointi(ratkaistu_labyrintti, laby_koko)


def umpikujat_labyrinttiin(labyrintti2, umpikujat):
    """Merkitsee umpikujat labyrinttiin.

    Args:
        labyrintti2 (lista): labyrintti, johon umpikujat merkitään
        umpikujat (lista): labyrintin umpikujien koordinaatit

    Returns:
        Labyrintin, johon on merkitty umpikujien koordinaatit.
    """
    for umpikuja in umpikujat:
        labyrintti2[umpikuja[0]][umpikuja[1]] = 'u'
    return labyrintti2
