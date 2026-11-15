"""
    GraveYard Shift
    Sarah Estes
    Main controls for the bullet actions
    11/15/2026 
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from graveyard_shift import GraveYardShift


class Arsenal:
    """Controls for player's arsenal and bullet affects"""
    def __init__(self, game: 'GraveYardShift'):
        """Initializing arsenal settings"""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Updates arsenal as bullets move off screen"""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Removes bullet from game once it moves off screen"""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draws a bullet from Bullet"""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Creates new bullet ad adds to bullets group"""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    
