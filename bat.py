"""
    GraveYard Shift
    Sarah Estes
    Drawing bats to the screen and movement
    11/15/2026 
"""


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bat_fleet import BatFleet


class Bat(Sprite):
    """Represents a single bat in the fleet"""
    def __init__(self, fleet: 'BatFleet', x: float, y: float):
        """Initialize the bat and set its starting position"""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.bat_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bat_w, self.settings.bat_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


    def update(self):
        """Set the speed and move the alien left or right"""
        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y


    def check_edges(self):
        """Return True if alien is at edge of screen"""
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)
    

    def draw_bat(self):
        """Draws a bat to the screen"""
        self.screen.blit(self.image, self.rect)

        
