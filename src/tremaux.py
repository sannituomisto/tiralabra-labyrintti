import sys
import time
from random import randint
import pygame


class Tremaux:
    """Luokka, joka vastaa Tremauxin algoritmista.
    """

    def __init__(self, labyrinth, labyrinth_class, size, is_test=False):
        self.labyrinth = labyrinth
        self.labyrinth_class = labyrinth_class
        self.size = size
        self.is_test = is_test

    def tremaux(self):
        """Tremauxin algoritmista vastaava funktio. Pidetään muistissa vierailtuja ruutuja ja muodostuvaa ratkaisupolkua.
        Edetään polkuja pitkin kunnes tullaan risteykseen, jossa ei olla vierailtu, jolloin arvotaan uusi suunta. Jos törmätään
        umpikujaan tai risteykseen, jossa on jo vierailtu, lähdetään peruutamaan samaa polkua pitkin takaisin. Jos saavutaan
        risteykseen, jossa ollaan jo vierailtu mutta polku, jota pitkin saavuttiin risteykseen on jo merkitty kahdesti, täytyy
        valita risteyksestä uusi reitti, jossa on vierailtu maximissaan kerran mutta valitaan vierailematon polku, jos
        mahdollista. Funktiossa on myös pygame ikkunan tapahtumien käsittelyyn tarvittavaa koodia, joka ei liity algoritmin
        toimintaan.

        Returns:
            Ratkaisupolun kooridaatit listassa. Palautusarvo on testejä varten.
        """
        visited_blocks = set()
        solved_path = []
        stack = []
        start, end = self.start_and_end_block()
        stack.append(start)

        while stack:
            # Seuraavat 11 riviä ovat pygame ikkunan tapahtumien käsittelyyn tarvittavaa koodia, joka ei liity algoritmiin.
            if not self.is_test:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_m:
                            return False, None
            block = stack[-1]
            self.labyrinth_class.update_labyrinth(
                "visited_once", block[1], block[0])
            time.sleep(0.1)
            unvisited_blocks = []
            if block == end:
                return True, solved_path

            if block not in visited_blocks:
                visited_blocks.add(block)

            neighbour_blocks = self.surrounding_blocks(block[0], block[1])
            for neighbour_block in neighbour_blocks:
                if neighbour_block not in visited_blocks:
                    unvisited_blocks.append(neighbour_block)

            if unvisited_blocks:
                index = randint(0, len(unvisited_blocks)-1)
                next_block = unvisited_blocks[index]
                solved_path.append(block)
                stack.append(next_block)
            else:
                self.labyrinth_class.update_labyrinth(
                    "visited_twice", block[1], block[0])
                time.sleep(0.1)
                stack.pop()
                if solved_path:
                    solved_path.pop()
        self.labyrinth_class.update_labyrinth(
                    "no_solution_tre")
        return True, solved_path

    def start_and_end_block(self):
        """Etsii aloitus- ja lopetusruudun.

        Returns:
            tuple: aloitus- ja lopetusruudun koordinaatit.
        """
        start = None
        end = None
        for i in range(0, self.size):
            if self.labyrinth[0][i] == ".":
                start = (0, i)
        for j in range(0, self.size):
            if self.labyrinth[self.size-1][j] == ".":
                end = (self.size-1, j)
        return start, end

    def surrounding_blocks(self, height, width):
        """Etsii ruudun ympäröivät ruudut, jotka eivät ole seiniä (pohjoinen, itä, etelä ja länsi).

        Args:
            height (int): labyrintin ruudun height koordinaatti
            width (int): labyrintin ruudun width koordinaatti

        Returns:
            lista: Ruudun ympäröivät ruudut, jotka eivät ole seiniä.
        """
        neighbour_blocks = []
        if height > 0 and self.labyrinth[height-1][width] == ".":
            neighbour_blocks.append((height - 1, width))
        if height < self.size - 1 and self.labyrinth[height+1][width] == ".":
            neighbour_blocks.append((height + 1, width))
        if width > 0 and self.labyrinth[height][width-1] == ".":
            neighbour_blocks.append((height, width - 1))
        if width < self.size - 1 and self.labyrinth[height][width+1] == ".":
            neighbour_blocks.append((height, width + 1))
        return neighbour_blocks
