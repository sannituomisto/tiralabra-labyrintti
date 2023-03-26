from labyrintin_generointi import generoidaan_labyrintti
import ui

def main():
    while True:
        """Aloitus"""
        ui.aloitus()
        """Labyrintin mittojen syöttö"""
        korkeus_ja_leveys = ui.labyrintin_mitat()
        """Labyrintin teko"""
        labyrintti=generoidaan_labyrintti(korkeus_ja_leveys, korkeus_ja_leveys)
        ui.labyrintti(labyrintti, korkeus_ja_leveys)

if __name__ == '__main__':
    main()