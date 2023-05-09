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
        self.is_test = is_test

    def dead_end_filling(self):
        """Kokoaa algoritmin vaiheet yhteen, jotta algoritmi toimii hyvin muun sovelluksen kanssa.

        Returns:
            Boolean, list: Palauttaa True, jos algoritmia ei keskeytetty ja lopullisen labyrintin listassa,
            johon on merkitty umpikujat. Tätä lopullista labyrinttiä listamuodossa ei tarvita muualla kuin
            testeissä, sillä algoritmit visualisoidaan pygamella.
        """
        dead_ends = self.find_dead_ends()
        if dead_ends:
            self.fill_dead_ends(dead_ends)
            return True, self.labyrinth
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

    def fill_dead_ends(self, dead_ends):
        """Täyttää labyrintin polkuja umpikujista risteykseen asti kunnes vain ratkaisu on jäljellä
        ja kutsuu Labyrinth luokan fuktiota, joka päivittää algotimin vaiheet eli nyt umpikujista lähtevät polut labyrinttiin.
        Funktiossa on myös pygame ikkunan tapahtumien käsittelyyn tarvittavaa koodia, joka ei liity algoritmin toimintaan.

        Args:
            dead_ends (lista): labyrintin umpikujat

        Returns:
            Labyrintin umpikujista risteykseen asti lähtevien polkujen koordinaatit listassa. Palautusarvo on testejä varten.
        """
        start_block = self.start_and_end_block()[0]
        end_block = self.start_and_end_block()[1]
        stack = []
        dead_end_paths = []
        for dead_end in dead_ends:
            stack.append(dead_end)
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
                                return False
                block = stack.pop()
                self.labyrinth[block[0]][block[1]] = '#'
                dead_end_paths.append(block)
                self.labyrinth_class.update_labyrinth(
                    "deadend_path", block[1], block[0])
                time.sleep(0.1)
                if block == end_block:
                    break
                if block == start_block:
                    self.labyrinth_class.update_labyrinth(
                    "no_solution_def")
                for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_block = (block[0]+move[0], block[1]+move[1])
                    neighbour_blocks = self.surrounding_blocks(
                        new_block[0], new_block[1])
                    if neighbour_blocks.count(".") > 1:
                        continue
                    if self.labyrinth[new_block[0]][new_block[1]] == ".":
                        stack.append(new_block)
        return dead_end_paths
