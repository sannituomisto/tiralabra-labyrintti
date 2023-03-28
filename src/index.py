from labyrintin_hakeminen import labyrintin_haku
import ui

def main():
    while True:
        """Aloitus"""
        ui.aloitus()
        """Labyrintin mittojen syöttö"""
        labyrintin_nro = ui.labyrintin_nro()
        if labyrintin_nro == False:
            continue
        """Labyrintin teko"""
        labyrintti=labyrintin_haku(labyrintin_nro)
        ui.labyrintti(labyrintti)

if __name__ == '__main__':
    main()