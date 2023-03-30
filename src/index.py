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
        if labyrintin_nro <= 5:
            koko=20
        else:
            koko=100
        # 150x150 kokoiset labyrintit, jos tulevat sovellukseen
        # else:
        #     koko=150
        ui.labyrintti(labyrintti,koko)

if __name__ == '__main__':
    main()