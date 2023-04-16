"""Tremauxin algoritmista vastaava moduuli.

    """
from collections import deque
from random import randint
import time


class Tremaux:
    """Luokka, joka vastaa Tremauxin algoritmista.
    """

    def __init__(self, labyrintti, koko, ruudun_koko, laby_nro, pygame_ikkuna):
        self.labyrintti = labyrintti
        self.koko = koko
        self.ruudun_koko = ruudun_koko
        self.labyrintin_numero = laby_nro
        self.pygame_ikkuna = pygame_ikkuna

    def aloita_tremaux(self):
        """Aloittaa visualisoinnin pygamesta vastaavan moduulin avulla, jonka jälkeen kokoaa algoritmin vaiheet yhteen
        ja lopuksi mahdollistaa visualisoinnin lopettamisen pygamesta vastaavan moduulin avulla.
        """
        self.pygame_ikkuna.ikkunan_alustus(
            'TREMAUXIN ALGORITMI LABYRINTISSA '+str(self.labyrintin_numero))
        self.labyrintin_teko()
        self.tremaux()
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

    def tremaux(self):
        """Tremauxin algoritmista vastaava funktio. Pidetään muistissa vierailtuja ruutuja ja muodostuvaa ratkaisupolkua.
        Edetään polkuja pitkin kunnes tullaan risteykseen, jossa ei olla vierailtu, jolloin arvotaan uusi suunta. Merkitään 
        (eli piirretään) pygamesta vastaavan moduulin avulla ruudut, jossa ollaan vierailtu kerran yhdellä värillä samalla,
        kun edetään labyrintissa. Jos törmätään umpikujaan tai risteykseen, jossa on jo vierailtu, lähdetään peruutamaan
        samaa polkua pitkin takaisin ja merkitään (eli piirretään) nämä kahdesti vieraillut ruudut peruutettaessa uudella värillä
        pygamesta vastaavan moduulin avulla. Jos saavutaan risteykseen, jossa ollaan jo vierailtu mutta polku, jota pitkin
        saavuttiin risteykseen on jo merkitty kahdesti, täytyy valita risteyksestä uusi reitti, jossa on vierailtu maximissaan
        kerran mutta valitaan vierailematon polku, jos mahdollista.   

        Returns:
            Ratkaisupolun kooridaatit listassa. Palautusarvo on testejä varten.
        """
        vieraillut_ruudut = set()
        ratkaistu_polku = []
        pino = deque()
        aloitus, lopetus = self.aloitus_ja_lopetus_ruutu()
        pino.append(aloitus)

        while pino:
            ruutu = pino[-1]
            self.pygame_ikkuna.piirto((229, 152, 155), (
                ruutu[1]*self.ruudun_koko, ruutu[0]*self.ruudun_koko, self.ruudun_koko, self.ruudun_koko))
            self.pygame_ikkuna.ikkunan_paivitys()
            time.sleep(0.1)
            vierailemattomat_ruudut = []
            if ruutu == lopetus:
                return ratkaistu_polku

            if ruutu not in vieraillut_ruudut:
                vieraillut_ruudut.add(ruutu)

            viereiset_ruudut = self.ymparoivat_ruudut(ruutu[0], ruutu[1])
            for naapuri_ruutu in viereiset_ruudut:
                if naapuri_ruutu not in vieraillut_ruudut:
                    vierailemattomat_ruudut.append(naapuri_ruutu)

            if vierailemattomat_ruudut:
                indeksi = randint(0, len(vierailemattomat_ruudut)-1)
                seuraava_ruutu = vierailemattomat_ruudut[indeksi]
                ratkaistu_polku.append(ruutu)
                pino.append(seuraava_ruutu)
            else:
                self.pygame_ikkuna.piirto((255, 183, 0), (
                    ruutu[1]*self.ruudun_koko, ruutu[0]*self.ruudun_koko, self.ruudun_koko, self.ruudun_koko))
                self.pygame_ikkuna.ikkunan_paivitys()
                time.sleep(0.1)
                pino.pop()
                ratkaistu_polku.pop()
        return None

    def aloitus_ja_lopetus_ruutu(self):
        """Etsii aloitus- ja lopetusruudun.

        Returns:
            tuple: Aloitus- ja lopetusruudun koordinaatit.
        """
        aloitus = None
        lopetus = None
        for i in range(0, self.koko):
            if self.labyrintti[0][i] == ".":
                aloitus = (0, i)
        for j in range(0, self.koko):
            if self.labyrintti[self.koko-1][j] == ".":
                lopetus = (self.koko-1, j)
        return aloitus, lopetus

    def ymparoivat_ruudut(self, korkeus, leveys):
        """Etsii ruudun ympäröivät ruudut, jotka eivät ole seiniä (pohjoinen, itä, etelä ja länsi).

        Args:
            korkeus (int): labyrintin ruudun korkeus koordinaatti
            leveys (int): labyrintin ruudun leveys koordinaatti

        Returns:
            lista: Ruudun ympäröivät ruudut, jotka eivät ole seiniä.
        """
        viereiset_ruudut = []
        if korkeus > 0 and self.labyrintti[korkeus-1][leveys] == ".":
            viereiset_ruudut.append((korkeus - 1, leveys))
        if korkeus < self.koko - 1 and self.labyrintti[korkeus+1][leveys] == ".":
            viereiset_ruudut.append((korkeus + 1, leveys))
        if leveys > 0 and self.labyrintti[korkeus][leveys-1] == ".":
            viereiset_ruudut.append((korkeus, leveys - 1))
        if leveys < self.koko - 1 and self.labyrintti[korkeus][leveys+1] == ".":
            viereiset_ruudut.append((korkeus, leveys + 1))
        return viereiset_ruudut
