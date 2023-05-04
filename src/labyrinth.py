"""Algoritmien visualisointinäkymästä vastaava moduuli.
    """
import pygame

WHITE = (255, 255, 255)
ROSEBROWN = (238, 180, 180)
GREEN = (84, 139, 84)
SALMON = (250, 128, 114)
RED = (139, 0, 0)


class Labyrinth:
    """Labyrintin hakemisesta, piirtämisestä ja päivittämisestä vastaava luokka.
    """

    def __init__(self, screen):
        """
        Args:
            screen (pygame display): Pygameikkuna
        """
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.screen_def = self.screen.subsurface(
            (0, 100, self.screen_width//2, self.screen_height-100))
        self.screen_tre = self.screen.subsurface(
            (self.screen_width//2, 100, self.screen_width//2, self.screen_height-100))
        self.ins_font = pygame.font.SysFont('Verdana', 18)
        self.head_font = pygame.font.SysFont('Verdana', 30)
        self.block_size = 20
        self.labyrinth=None
        self.labyrinth_size = 20

    def get_labyrinth(self, labyrinth_number):
        """Hakee labyrintin tiedostosta."""
        labyrinth = []
        if labyrinth_number <= 5:
            with open("20x20labyrinths/labyrinth"+str(labyrinth_number)+".txt", encoding="utf-8") as file:
                for row in file:
                    row = row.replace("\n", "")
                    labyrinth.append(list(row))
        self.labyrinth = labyrinth
        return labyrinth

    def draw_labyrinth(self):
        """Alustaa näytön, jossa algoritmit visualisoidaan. Funktio tekee otsikot ja piirtää
        labyrintit.
        """
        self.screen.fill(WHITE)
        header = self.head_font.render("Dead-end filling", True, SALMON)
        header2 = self.head_font.render("Trémaux", True, SALMON)
        instructions = self.ins_font.render(
            "Palaa valikkoon painamalla m-näppäintä.", True, GREEN)
        header_rect = header.get_rect(topleft=(90, 50))
        header2_rect = header2.get_rect(topleft=(530, 50))
        instructions_rect = instructions.get_rect(topleft=(5, 10))
        self.screen.blit(header, header_rect)
        self.screen.blit(header2, header2_rect)
        self.screen.blit(instructions, instructions_rect)
        x = 0
        y = 0
        for i in range(0, self.labyrinth_size):
            for j in range(0, self.labyrinth_size):
                if self.labyrinth[i][j] == '.':
                    pygame.draw.rect(self.screen_tre, ROSEBROWN,
                                     (x, y, self.block_size, self.block_size))
                    pygame.draw.rect(self.screen_def, ROSEBROWN,
                                     (x, y, self.block_size, self.block_size))
                else:
                    pygame.draw.rect(self.screen_tre, GREEN,
                                     (x, y, self.block_size, self.block_size))
                    pygame.draw.rect(self.screen_def, GREEN,
                                     (x, y, self.block_size, self.block_size))
                x = x+self.block_size
            y = y+self.block_size
            x = 0
        pygame.display.flip()

    def update_labyrinth(self, update_type, x, y):
        """Päivittää labyrintteja algoritmien edetessä askel askeleelta.

        Args:
            update_type (str): Algoritmin vaihe, joka halutaan päivittää labyrinttiin.
            x (int): Ruudun, joka halutaan päivittää, leveyskordinaatti.
            y (int: Ruudun, joka halutaan päivittää, korkeuskordinaatti.
        """
        if update_type == "deadend":
            pygame.draw.rect(self.screen_def, SALMON, (
                x*self.block_size, y*self.block_size, self.block_size, self.block_size))
        if update_type == "deadend_path":
            pygame.draw.rect(self.screen_def, RED, (
                x*self.block_size, y*self.block_size, self.block_size, self.block_size))
        if update_type == "visited_once":
            pygame.draw.rect(self.screen_tre, SALMON, (
                x*self.block_size, y*self.block_size, self.block_size, self.block_size))
        if update_type == "visited_twice":
            pygame.draw.rect(self.screen_tre, RED, (
                x*self.block_size, y*self.block_size, self.block_size, self.block_size))
        pygame.display.flip()
