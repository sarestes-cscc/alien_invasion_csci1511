"""
    GraveYard Shift
    Sarah Estes
    Draws and updates bullet
    11/15/2026 
"""


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graveyard_shift import GraveYardShift


class Bullet(Sprite):
    """Manages bullets fired from the cat"""
    def __init__(self, game: 'GraveYardShift'):
        """Create a bullet object at the cat's current position"""
        super().__init__()
        
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.cat.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)

        
