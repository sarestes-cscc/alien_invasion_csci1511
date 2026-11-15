import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graveyard_shift import GraveYardShift
    from arsenal import Arsenal


class Cat:

    def __init__(self, game: 'GraveYardShift', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.cat_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.cat_w, self.settings.cat_h)
            )
        
        self.rect = self.image.get_rect()
        self._center_cat()

        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_cat(self):
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)


    def update(self):
        self._update_cat_movement()
        self.arsenal.update_arsenal()


    def _update_cat_movement(self):
        # updating the position of the cat
        temp_speed = self.settings.cat_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x


    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)


    def fire(self):
        return self.arsenal.fire_bullet()


    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_cat()
            return True
        return False
