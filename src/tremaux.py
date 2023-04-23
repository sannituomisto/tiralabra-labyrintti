"""Tremauxin algoritmista vastaava moduuli.

    """
import sys
import time
from collections import deque
from random import randint
import pygame


class Tremaux:
    """Luokka, joka vastaa Tremauxin algoritmista.
    """

    def __init__(self, labyrinth, labyrinth_class, size, is_test=False):
        self.labyrinth = labyrinth
        self.labyrinth_class = labyrinth_class
        self.size = size
        self.finished = False
        self.is_test = is_test

    def start_tremaux(self):
        """Aloittaa visualisoinnin pygamesta vastaavan moduulin avulla, jonka jälkeen kokoaa algoritmin vaiheet yhteen
        ja lopuksi mahdollistaa visualisoinnin lopettamisen pygamesta vastaavan moduulin avulla.
        """
        self.tremaux()
        return self.finished

    def tremaux(self):
        """Tremauxin algoritmista vastaava funktio. Pidetään muistissa vierailtuja blockja ja muodostuvaa ratkaisupolkua.
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
        visited_blocks = set()
        solved_path = []
        stack = deque()
        start, end = self.start_and_end_block()
        stack.append(start)

        while stack:
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
                            return False
            block = stack[-1]
            self.labyrinth_class.update_labyrinth(
                "visited_once", block[1], block[0])
            time.sleep(0.1)
            unvisited_blocks = []
            if block == end:
                self.finished = True
                return solved_path

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
                solved_path.pop()
        return None

    def start_and_end_block(self):
        """Etsii start- ja endruudun.

        Returns:
            tuple: start- ja endruudun koordinaatit.
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

    def handle_event(self, event):
        """Käsittelee algoritminäkymän tapahtumat, kun tremauxin algoritmi on päässyt loppuun.
        Args:
            event (pygame event): Pygame tapahtuma
        """
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_m:
                return True
        return None
