import sys
import pygame

def run_game():
    # init game and create display object
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Example Game")
    # backround color
    bg_color = (238,238,228)

    while True:
        # control keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # add screen backround
        screen.fill(bg_color)
        # display the last screen
        pygame.display.flip()
# test game
run_game()