import sys
import pygame
def check_keydown_events(event, ship):
    """Check keydown events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keyup_events(event, ship):
    """Check keydown events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_events(ship):
    """Check keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship):
    """Update image on screen and draw new screen"""
    # add screen backround
    screen.fill(game_settings.bg_color)
    # add ship to screen
    ship.blitme()
    # display the last screen
    pygame.display.flip()