"""Dead end filling-algoritmin toiminnasta vastaava moduuli."""
from collections import deque
import time


class DeadEndFilling:
    """Luokka, joka vastaa dead end filling- algoritmista.
    """

    def __init__(self, labyrintti, koko, ruudun_koko, laby_nro, pygame_ikkuna):
        self.labyrintti = labyrintti
        self.koko = koko
        self.ruudun_koko = ruudun_koko
        self.labyrintin_numero = laby_nro
        self.pygame_ikkuna = pygame_ikkuna

    def aloita_dead_end_filling(self):
        """Aloittaa visualisoinnin pygamesta vastaavan moduulin avulla, jonka jälkeen kokoaa algoritmin vaiheet yhteen
        ja lopuksi mahdollistaa visualisoinnin lopettamisen pygamesta vastaavan moduulin avulla.
        """
        self.pygame_ikkuna.ikkunan_alustus(
            'DEAD END FILLING ALGORITMI LABYRINTISSA '+str(self.labyrintin_numero))
        self.labyrintin_teko()
        umpikujat = self.etsi_umpikujat()
        self.taytetaan_umpikujat(umpikujat)
        self.pygame_ikkuna.ydin_funktio()

    def labyrintin_teko(self):
        """Piirtää labyrintin pygame ikkunaan pygamesta vastaavan moduulin avulla.
        """
        x = 0
        y = 0
        for i in range(0, self.koko):
            for j in range(0, self.koko):
                if self.labyrintti[i][j] == '.':
                    self.pygame_ikkuna.piirto(
                        (255, 205, 178), (x, y, self.ruudun_koko, self.ruudun_koko))
                else:
                    self.pygame_ikkuna.piirto(
                        (120, 150, 100), (x, y, self.ruudun_koko, self.ruudun_koko))
                x = x+self.ruudun_koko
            y = y+self.ruudun_koko
            x = 0
        self.pygame_ikkuna.ikkunan_paivitys()

    def etsi_umpikujat(self):
        """Etsii lapyrintin umpikujat ja piirtää ne labyrinttiin pygamesta vastaavan moduulin avulla.

        Returns:
            Labyrintin umpikujien koordinaatit listassa.
        """
        umpikujat = []
        for i in range(1, self.koko-1):
            for j in range(1, self.koko-1):
                viereiset_ruudut = self.ymparoivat_ruudut(i, j)
                if self.labyrintti[i][j] != "@" and viereiset_ruudut.count("@") >= 3:
                    umpikujat.append((i, j))
                    self.pygame_ikkuna.piirto(
                        (229, 152, 155), (j*self.ruudun_koko, i*self.ruudun_koko, self.ruudun_koko, self.ruudun_koko))
                    self.pygame_ikkuna.ikkunan_paivitys()
                    time.sleep(0.2)
        return umpikujat

    def ymparoivat_ruudut(self, korkeus, leveys):
        """Etsii ruudun ympäröivät ruudut (pohjoinen, itä, etelä ja länsi)

        Args:
            korkeus (int): labyrintin ruudun korkeus koordinaatti
            leveys (int): labyrintin ruudun leveys koordinaatti

        Returns:
            Ruudun ympäröivät ruudut.
        """
        viereiset_ruudut = []
        viereiset_ruudut.append(self.labyrintti[korkeus-1][leveys])
        viereiset_ruudut.append(self.labyrintti[korkeus+1][leveys])
        viereiset_ruudut.append(self.labyrintti[korkeus][leveys-1])
        viereiset_ruudut.append(self.labyrintti[korkeus][leveys+1])
        return viereiset_ruudut

    def taytetaan_umpikujat(self, umpikujat):
        """Täyttää labyrintin polkuja umpikujista lähtien kunnes vain ratkaisu on jäljellä. Piirtää pygamesta vastaavan
        moduulin avulla täytettävät polut.

        Args:
            umpikujat (lista): labyrintin umpikujat

        Returns:
            Labyrintin umpikujien kujien koordinaatit listassa. Palautusarvo on testejä varten
        """
        jono = deque()
        umpikujien_kujat = []
        for umpikuja in umpikujat:
            jono.append(umpikuja)
            while len(jono) > 0:
                ruutu = jono.popleft()
                self.labyrintti[ruutu[0]][ruutu[1]] = '#'
                umpikujien_kujat.append(ruutu)
                self.pygame_ikkuna.piirto((255, 183, 0), (
                    ruutu[1]*self.ruudun_koko, ruutu[0]*self.ruudun_koko, self.ruudun_koko, self.ruudun_koko))
                self.pygame_ikkuna.ikkunan_paivitys()
                time.sleep(0.1)
                for siirto in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    uusi_ruutu = (ruutu[0]+siirto[0], ruutu[1]+siirto[1])
                    if uusi_ruutu[0] == self.koko-1 or uusi_ruutu[1] == self.koko-1:
                        continue
                    viereiset_ruudut = self.ymparoivat_ruudut(
                        uusi_ruutu[0], uusi_ruutu[1])
                    if viereiset_ruudut.count(".") > 1:
                        continue
                    if self.labyrintti[uusi_ruutu[0]][uusi_ruutu[1]] == "@":
                        continue
                    if self.labyrintti[uusi_ruutu[0]][uusi_ruutu[1]] == ".":
                        jono.append(uusi_ruutu)
        return umpikujien_kujat
