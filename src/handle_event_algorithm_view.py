import sys
import pygame


def handle_event(event):
    """Käsittelee algoritminäkymän tapahtumat, jos tremauxin algoritmi annetaan suorittaa loppuun asti.
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
