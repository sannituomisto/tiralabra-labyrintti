from colorama import init
from colorama import Fore, Style

def aloitus():
    # Sovelluksen aloitusnäkymä
    print("Labyrinttisovellus")

def labyrintin_mitat():
    print("Valitse labyrintin mitat. Korkeus ja leveys ovat samat.")
    korkeus_ja_leveys = int(input("Labyrintin korkeus x leveys: "))
    if korkeus_ja_leveys < 10:
        print("min 10x10")
        print('\n')
        return False
    if korkeus_ja_leveys > 60:
        print("max 60x60")
        print('\n')
        return False
    print('\n')
    return korkeus_ja_leveys

def labyrintti(labyrintti, korkeus_ja_leveys):
    # Alustetaan colorama
    init()

    for i in range(0, korkeus_ja_leveys):
        for j in range(0, korkeus_ja_leveys):
            if (labyrintti[i][j] == 'u'):
                    print(Fore.WHITE + str(labyrintti[i][j]), end=" ")
            elif (labyrintti[i][j] == '*'):
                    print(Fore.GREEN + Style.BRIGHT + str(labyrintti[i][j]), end=" ")
            else:
                print(Fore.CYAN+ Style.BRIGHT + str(labyrintti[i][j]), end=" ")
        
        print('\n')
    print(Style.RESET_ALL)