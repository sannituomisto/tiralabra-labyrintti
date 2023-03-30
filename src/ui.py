from colorama import init
from colorama import Fore, Style

def aloitus():
    """Sovelluksen aloitusnäkymä"""
    print('\n')
    print("Labyrinttisovellus")

def labyrintin_nro():
    """Käyttäjä syöttää halutun labyrintin numeron"""
    print('Labyrintit 1-5 ovat 20x20 ja 6-10 ovat 100x100')
    try:
        labyrintin_nro = int(input("Näytä labyrintti (1-10): "))
        if labyrintin_nro < 1 or labyrintin_nro > 10:
            print("Anna labyrintin numero 1-10")
            return False
    except:
        print("Syötä numero")
        return False
    
    print('\n')
    return labyrintin_nro

def labyrintti(labyrintti, koko):
    """Labyrintin visualisointi"""
    init()
    for i in range(0, koko):
        for j in range(0, koko):
            if (labyrintti[i][j] == '.'):
                print(Fore.GREEN + Style.BRIGHT + str(labyrintti[i][j]), end=" ")
            else:
                print(Fore.CYAN+ Style.BRIGHT + str(labyrintti[i][j]), end=" ")
            
        print(Style.RESET_ALL)