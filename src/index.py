from labyrintin_luonti import labyrintin_luonti
import ui

def main():
    while True:
        """Aloitus"""
        ui.aloitus()
        """Labyrintin mittojen syöttö"""
        korkeus_ja_leveys = ui.labyrintin_mitat()
        if korkeus_ja_leveys == False:
            continue
        """Labyrintin teko"""
        labyrintti=labyrintin_luonti(korkeus_ja_leveys, korkeus_ja_leveys)
        ui.labyrintti(labyrintti, korkeus_ja_leveys)

if __name__ == '__main__':
    main()