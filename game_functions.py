import sys
import pygame
def check_events(ship):
    """Check keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False



def update_screen(game_settings, screen, ship):
    """Update image on screen and draw new screen"""
    # add screen backround
    screen.fill(game_settings.bg_color)
    # add ship to screen
    ship.blitme()
    # display the last screen
    pygame.display.flip()