import sys
import pygame

WHITE = (255, 255, 255)
ROSEBROWN = (238, 180, 180)
GREEN = (84, 139, 84)
SALMON = (250, 128, 114)
RED = (139, 0, 0)


class Menu:
    """Valikkonäkymästä ja sen toiminnallisuudesta vastaava luokka.
    """

    def __init__(self, screen):
        """
        Args:
            screen (pygame display): Pygameikkuna näyttö
        """
        self.screen = screen
        self.laby_font = pygame.font.SysFont('Verdana', 30)
        self.ins_font = pygame.font.SysFont('Verdana', 18)
        self.head_font = pygame.font.SysFont('Verdana', 30)
        self.labyrinths = ["Labyrintti 1", "Labyrintti 2",
                           "Labyrintti 3", "Labyrintti 4", "Labyrintti 5", "Labyrintti 6"]
        self.selected_labyrinth = 0

    def draw(self):
        """Piirtää valikkonäkymän elementit.
        """
        self.screen.fill(WHITE)
        header = self.head_font.render(
            "Dead-end filling ja Trémauxin algoritmit labyrintissa", True, SALMON)
        instructions = self.ins_font.render(
            "Selaa labyrintteja nuolinäppäimillä ja valitse labyrintti painamalla enter.", True, GREEN)
        header_rect = header.get_rect(
            center=(self.screen.get_width() // 2, 50))
        instructions_rect = instructions.get_rect(center=(self.screen.get_width() // 2, 95))
        self.screen.blit(header, header_rect)
        self.screen.blit(instructions, instructions_rect)
        for i in range(len(self.labyrinths)):
            text = self.laby_font.render(self.labyrinths[i], True, GREEN)
            text_rect = text.get_rect(topleft=(10, 140 + i * 50))
            self.screen.blit(text, text_rect)
            if i == self.selected_labyrinth:
                pygame.draw.rect(self.screen, ROSEBROWN, text_rect, 3)

    def handle_event(self, event):
        """Käsittelee valikkonäkymän pygame tapahtumat.

        Args:
            event (pygame event): Pygameikkunan tapahtuma

        Returns:
            int: Käyttäjän valitseman labyrintin numero.
        """
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP:
                self.selected_labyrinth = (
                    self.selected_labyrinth - 1) % len(self.labyrinths)
            elif event.key == pygame.K_DOWN:
                self.selected_labyrinth = (
                    self.selected_labyrinth + 1) % len(self.labyrinths)
            elif event.key == pygame.K_RETURN:
                return self.selected_labyrinth
