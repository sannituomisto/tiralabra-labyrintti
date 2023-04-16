"""Pygame ikkunasta vastaava moduuli.
    """
import pygame


class PygameIkkuna():
    """Luokka, jonka avulla visualisoidaan algoritmien toiminta labyrintissa pygamella.
    """

    def __init__(self):
        self.kello = pygame.time.Clock()

    def ikkunan_alustus(self, otsikko):
        """Alustaa pygame ikkunan.

        Args:
            otsikko (str): Pygame ikkunan otsikko.
        """
        pygame.init()
        self.peli_ikkuna = pygame.display.set_mode((600, 600))
        pygame.display.set_caption(otsikko)

    def piirto(self, vari, sijainti):
        """Piirtää suorakulmiot pygame ikkunaan. 

        Suorakulmioista muodostuu labyrintti ja algoritmien toiminnan kuvaaminen.

        Args:
            vari (tuple): Pygame värikoodi
            sijainti (tuple): Suorakulmion sijainti ja mitat.
        """
        pygame.draw.rect(self.peli_ikkuna, vari, sijainti)

    def ikkunan_paivitys(self):
        """Päivittää pygame ikkunan.
        """
        pygame.display.flip()

    def ydin_funktio(self):
        """Mahdollistaa pygame-ikkunan sulkemisen. Ikkunaa ei voida sulkea ennen kuin algoritmi on päässyt loppuun.
        """
        running = True
        while running:
            self.kello.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


pygame_ikkuna = PygameIkkuna()
