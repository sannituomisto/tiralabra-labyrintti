"""Labyrinttien visualisoinnista vastaava moduuli.
"""
from colorama import init
from colorama import Fore, Style
from labyrintin_hakeminen import labyrintin_haku


def labyrintin_teko():
    """Kokoaa yhteen käyttäjän valitseman labyrintin visualisoinnin.
    """
    laby_nro = labyrintin_nro()
    labyrintti = labyrintin_haku(laby_nro)
    koko = labyrintin_koko(laby_nro)
    labyrintin_visualisointi(labyrintti, koko)


def labyrintin_nro():
    """Käyttäjä syöttää haluamansa labyrintin numeron."""
    print('Labyrintit 1-5 ovat 20x20 ja 6-10 ovat 100x100')
    labyrintin_numero = int(input("Syötä labyrintin numero (1-10): "))
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
    else:
        koko = 100
    return koko


def labyrintin_visualisointi(labyrintti, koko):
    """Tulostaa labyrintin.

    Args:
        labyrintti (lista): labyrintti
        koko (int): labyrintin koko
    """
    print('\r')
    init()
    for i in range(0, koko):
        for j in range(0, koko):
            if labyrintti[i][j] == '.':
                print(Fore.GREEN + Style.BRIGHT +
                      str(labyrintti[i][j]), end=" ")
            elif labyrintti[i][j] == 'u':
                print(Fore.RED + Style.BRIGHT + '.', end=" ")
            elif labyrintti[i][j] == '#':
                print(Fore.RED + Style.BRIGHT + '@', end=" ")
            else:
                print(Fore.CYAN + Style.BRIGHT +
                      str(labyrintti[i][j]), end=" ")

        print(Style.RESET_ALL)
