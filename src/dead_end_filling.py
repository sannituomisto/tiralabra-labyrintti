"""Dead end filling-algoritmin toiminnasta vastaava moduuli."""
from collections import deque
import sys
import time
import pygame


class DeadEndFilling:
    """Luokka, joka vastaa dead end filling- algoritmista.
    """

    def __init__(self, labyrinth, labyrinth_class, size, is_test=False):
        self.labyrinth = labyrinth
        self.labyrinth_class = labyrinth_class
        self.size = size
        self.finished = False
        self.is_test = is_test

    def start_dead_end_filling(self):
        """Kokoaa algoritmin vaiheet yhteen.

        Returns:
            Boolean, list: Palauttaa True, jos algoritmia ei keskeytetty ja lopullisen labyrintin listassa,
            johon on merkitty umpikujat. Tätä lopullista labyrinttiä listamuodossa ei tarvita muualla kuin
            testeissä, sillä algoritmit visualisoidaan pygamella.
        """
        dead_ends = self.find_dead_ends()
        if dead_ends:
            self.fill_dead_ends(dead_ends)
            return self.finished, self.labyrinth
        return None, self.labyrinth

    def find_dead_ends(self):
        """Etsii lapyrintin umpikujat ja kutsuu Labyrinth luokan fuktiota, joka päivittää algotimin vaiheet
        eli nyt umpikujat labyrinttiin. Funktiossa on myös pygame ikkunan tapahtumien käsittelyyn tarvittavaa
        koodia, joka ei liity algoritmin toimintaan.

        Returns:
            Labyrintin umpikujien koordinaatit listassa.
        """
        dead_ends = []
        for i in range(1, self.size-1):
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
            for j in range(1, self.size-1):
                neighbour_blocks = self.surrounding_blocks(i, j)
                if self.labyrinth[i][j] != "@" and neighbour_blocks.count("@") >= 3:
                    dead_ends.append((i, j))
                    self.labyrinth_class.update_labyrinth("deadend", j, i,)
                    time.sleep(0.2)
        return dead_ends

    def surrounding_blocks(self, height, width):
        """Etsii ruudun ympäröivät ruudut (pohjoinen, itä, etelä ja länsi)

        Args:
            height (int): labyrintin ruudun korkeus koordinaatti
            width (int): labyrintin ruudun leveys koordinaatti

        Returns:
            Ruudun ympäröivät ruudut.
        """
        neighbour_blocks = []
        if height > 0:
            neighbour_blocks.append(self.labyrinth[height-1][width])
        if height < self.size - 1:
            neighbour_blocks.append(self.labyrinth[height+1][width])
        if width > 0:
            neighbour_blocks.append(self.labyrinth[height][width-1])
        if width < self.size - 1:
            neighbour_blocks.append(self.labyrinth[height][width+1])
        return neighbour_blocks

    def find_end_block(self):
        """Etsii lopetus ruudun.

        Returns:
            tuple: lopetusruudun koordinaatit.
        """
        end = None
        for j in range(0, self.size):
            if self.labyrinth[self.size-1][j] == ".":
                end = (self.size-1, j)
        return end

    def fill_dead_ends(self, dead_ends):
        """Täyttää labyrintin polkuja umpikujista risteykseen asti kunnes vain ratkaisu on jäljellä
        ja kutsuu Labyrinth luokan fuktiota, joka päivittää algotimin vaiheet eli nyt umpikujista lähtevät polut labyrinttiin.
        Funktiossa on myös pygame ikkunan tapahtumien käsittelyyn tarvittavaa koodia, joka ei liity algoritmin toimintaan.

        Args:
            dead_ends (lista): labyrintin umpikujat

        Returns:
            Labyrintin umpikujista risteykseen asti lähtevien polkujen koordinaatit listassa. Palautusarvo on testejä varten.
        """
        end_block = self.find_end_block()
        queue = deque()
        dead_end_paths = []
        for dead_end in dead_ends:
            queue.append(dead_end)
            while len(queue) > 0:
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
                block = queue.popleft()
                self.labyrinth[block[0]][block[1]] = '#'
                dead_end_paths.append(block)
                self.labyrinth_class.update_labyrinth(
                    "deadend_path", block[1], block[0])
                time.sleep(0.1)
                if block == end_block:
                    break
                for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_block = (block[0]+move[0], block[1]+move[1])
                    neighbour_blocks = self.surrounding_blocks(
                        new_block[0], new_block[1])
                    if neighbour_blocks.count(".") > 1:
                        continue
                    if self.labyrinth[new_block[0]][new_block[1]] == ".":
                        queue.append(new_block)
        self.finished = True
        return dead_end_paths
