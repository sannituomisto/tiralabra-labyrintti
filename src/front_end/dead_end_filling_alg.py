"""Dead end filling- algoritmin toiminnasta vastaava moduuli käyttöliittymän puolella.
"""

from front_end.nayta_labyrintti import labyrintin_nro
from front_end.nayta_labyrintti import labyrintin_koko
from front_end.nayta_labyrintti import labyrintin_haku
from dead_end_filling import DeadEndFilling
from ikkuna import pygame_ikkuna


def nayta_dead_end_filling():
    """Hakee käyttämän syöttämän labyrintin numeron ja sitä vastaavan labyrintin ja kutsuu dead end filling- algoritmin
    toiminnasta vastaavaa moduulia.
    """
    laby_nro = labyrintin_nro()
    laby_koko, ruudun_koko = labyrintin_koko(laby_nro)
    labyrintti = labyrintin_haku(laby_nro)
    DeF_labyrintti = DeadEndFilling(
        labyrintti, laby_koko, ruudun_koko, laby_nro, pygame_ikkuna)
    DeF_labyrintti.aloita_dead_end_filling()
