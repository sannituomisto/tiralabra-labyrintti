from colorama import init
from colorama import Fore, Style

def aloitus():
    """Sovelluksen aloitusnäkymä"""
    print('\n')
    print("Labyrinttisovellus")

def labyrintin_nro():
    """Käyttäjä syöttää halutun labyrintin numeron"""
    labyrintin_nro = int(input("Näytä labyrintti (1-5): "))
    if labyrintin_nro not in [1,2,3,4,5]:
        print("Anna labyrintin numero 1-5")
        return False
    print('\n')
    return labyrintin_nro

def labyrintti(labyrintti):
    """Labyrintin visualisointi"""
    init()
    for i in range(0, 20):
            for j in range(0, 20):
                if (labyrintti[i][j] == '.'):
                        print(Fore.GREEN + Style.BRIGHT + str(labyrintti[i][j]), end=" ")
                else:
                    print(Fore.CYAN+ Style.BRIGHT + str(labyrintti[i][j]), end=" ")
            
            print(Style.RESET_ALL)