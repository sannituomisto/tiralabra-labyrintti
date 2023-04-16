"""Labyrinttien visualisoinnista vastaava moduuli.
"""
from labyrintin_hakeminen import labyrintin_haku
from ikkuna import pygame_ikkuna


def labyrintin_teko():
    """Kokoaa yhteen käyttäjän valitseman labyrintin visualisoinnin.
    """
    laby_nro = labyrintin_nro()
    labyrintti = labyrintin_haku(laby_nro)
    koko, ruudun_koko = labyrintin_koko(laby_nro)
    labyrintin_visualisointi(labyrintti, koko, ruudun_koko, laby_nro)
    pygame_ikkuna.ydin_funktio()
    return True


def labyrintin_nro():
    """Käyttäjä syöttää haluamansa labyrintin numeron."""
    labyrintin_numero = int(input("Syötä labyrintin numero (1-5): "))
    return labyrintin_numero


def labyrintin_koko(lab_nro):
    """Tarkastaa labyrintin koon.

    Args:
        lab_nro (int): käyttäjän valitseman labyrintin numero

    Returns:
        Käyttäjän valitseman labyrintin korkeuden ja leveyden.
    """
    if lab_nro <= 5:
        koko = 20
        ruudun_koko = 30
    # Tähän tulee mahdollisesti vielä isompien labyrinttien koot.
    return koko, ruudun_koko


def labyrintin_visualisointi(labyrintti, koko, ruudun_koko, laby_nro):
    """Labyrintin visualisointi"""
    pygame_ikkuna.ikkunan_alustus('LABYRINTTI '+str(laby_nro))
    x = 0
    y = 0
    for i in range(0, koko):
        for j in range(0, koko):
            if labyrintti[i][j] == '.':
                pygame_ikkuna.piirto(
                    (255, 205, 178), (x, y, ruudun_koko, ruudun_koko))
            else:
                pygame_ikkuna.piirto(
                    (120, 150, 100), (x, y, ruudun_koko, ruudun_koko))
            x = x+ruudun_koko
        y = y+ruudun_koko
        x = 0
    pygame_ikkuna.ikkunan_paivitys()
