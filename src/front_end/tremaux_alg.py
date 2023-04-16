"""Tremauxin algoritmin toiminnasta vastaava moduuli käyttöliittymän puolella. Moduuli siis täysin keskeneräinen.
"""
from front_end.nayta_labyrintti import labyrintin_nro
from front_end.nayta_labyrintti import labyrintin_koko
from front_end.nayta_labyrintti import labyrintin_haku
from tremaux import Tremaux
from ikkuna import pygame_ikkuna


def nayta_tremaux():
    """Hakee käyttämän syöttämän labyrintin numeron ja sitä vastaavan labyrintin ja kutsuu Tremauxin algoritmin toiminnasta
    vastaavaa moduulia.
    """
    laby_nro = labyrintin_nro()
    laby_koko, ruudun_koko = labyrintin_koko(laby_nro)
    labyrintti = labyrintin_haku(laby_nro)
    Tremaux_labyrintti = Tremaux(
        labyrintti, laby_koko, ruudun_koko, laby_nro, pygame_ikkuna)
    Tremaux_labyrintti.aloita_tremaux()
