"""Pygame ikkunan mainloop, joka hallinnoi koko ohjelman toimintaa ja näkymien vaihtamista.
    """
import sys
import pygame
from menu import Menu
from labyrinth import Labyrinth
from dead_end_filling import DeadEndFilling
from tremaux import Tremaux
import handle_event_algorithm_view

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

menu = Menu(screen)

labyrinth = Labyrinth(screen)

state = "MENU"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if state == "MENU":
                selected_labyrinth_number = menu.handle_event(event)
                if selected_labyrinth_number is not None:
                    selected_labyrinth1 = labyrinth.get_labyrinth(
                        selected_labyrinth_number)
                    selected_labyrinth2 = labyrinth.get_labyrinth(
                        selected_labyrinth_number)
                    labyrinth.draw_labyrinth()
                    dead_end_filling_alg = DeadEndFilling(
                        selected_labyrinth1, labyrinth, 20)
                    tremaux_alg = Tremaux(selected_labyrinth2, labyrinth, 20)
                    state = "LABYRINTH"
            elif state == "WAIT":
                back_to_menu = handle_event_algorithm_view.handle_event(event)
                if back_to_menu:
                    state = "MENU"

    if state == "LABYRINTH":
        dead_end_filling_state = dead_end_filling_alg.start_dead_end_filling()[
            0]
        if not dead_end_filling_state:
            state = "MENU"
            continue
        tremaux_state = tremaux_alg.start_tremaux()
        if not tremaux_state:
            state = "MENU"
            continue
        state = "WAIT"

    if state == "MENU":
        menu.draw()

    pygame.display.update()
