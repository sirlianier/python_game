import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for alien description"""
    def __init__(self, game_settings, screen):
        """Create alen object and define its start position"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        # Load alien image and set rect atribute
        self.image = pygame.image.load("images/alien.bmp")
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # set alien position
        self.x = float(self.rect.x)
    def blitme(self):
        """Draw alien at this position"""
        self.screen.blit(self.image, self.rect)