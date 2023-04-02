from colorama import init
from colorama import Fore, Style
from labyrintin_hakeminen import labyrintin_haku
import os

def labyrintin_teko():
    laby_nro=labyrintin_nro()
    labyrintti=labyrintin_haku(laby_nro)
    koko=labyrintin_koko(laby_nro)
    labyrintin_visualisointi(labyrintti, koko)
    

def labyrintin_nro():
    """Käyttäjä syöttää halutun labyrintin numeron"""
    print('Labyrintit 1-5 ovat 20x20 ja 6-10 ovat 100x100')
    labyrintin_numero = int(input("Syötä labyrintin numero (1-10): "))
    return labyrintin_numero

def labyrintin_koko(lab_nro):
    if lab_nro <= 5:
        koko=20
    else:
        koko=100
    return koko

def labyrintin_visualisointi(labyrintti, koko):
    """Labyrintin visualisointi"""
    print('\r')
    init()
    for i in range(0, koko):
        for j in range(0, koko):
            if (labyrintti[i][j] == '.'):
                print(Fore.GREEN + Style.BRIGHT + str(labyrintti[i][j]), end=" ")
            elif (labyrintti[i][j] == 'u'):
                print(Fore.RED + Style.BRIGHT + '.', end=" ")
            elif (labyrintti[i][j] == '#'):
                print(Fore.RED + Style.BRIGHT + '@', end=" ")
            else:
                print(Fore.CYAN+ Style.BRIGHT + str(labyrintti[i][j]), end=" ")
            
        print(Style.RESET_ALL)