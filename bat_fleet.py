"""
    GraveYard Shift
    Sarah Estes
    Logic for bat fleet - drawing to screen and actions
    11/15/2026 
"""


import pygame
from typing import TYPE_CHECKING
from bat import Bat

if TYPE_CHECKING:
    from graveyard_shift import GraveYardShift
    

class BatFleet:
    """Controls the bat fleet placement, movement, collisions"""
    def __init__(self, game: 'GraveYardShift'):
        """Initializing bat fleet settings"""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()


    def create_fleet(self):
        """Create the fleet of bats"""
        bat_w = self.settings.bat_w
        bat_h = self.settings.bat_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(bat_w, screen_w, bat_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(bat_w, bat_h, screen_w, fleet_w, fleet_h)

        self._create_rectangle_fleet(bat_w, bat_h, fleet_w, fleet_h, x_offset, y_offset)


    def _create_rectangle_fleet(self, bat_w, bat_h, fleet_w, fleet_h, x_offset, y_offset):
        """Create shape the fleet takes"""
        center_col = fleet_w // 2
        center_row = fleet_h // 2

        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = bat_w * col + x_offset
                current_y = bat_h * row + y_offset
                
                if row == center_row or col == center_col:
                    self._create_bat(current_x, current_y)


    def calculate_offsets(self, bat_w, bat_h, screen_w, fleet_w, fleet_h):
        """Calculates offset based on screensize"""
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * bat_w
        fleet_vertical_space = fleet_h * bat_h

        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)
        return x_offset,y_offset


    def calculate_fleet_size(self, bat_w, screen_w, bat_h, screen_h):
        """Calculates size of fleet so they fill screen"""
        fleet_w = (screen_w//bat_w)
        fleet_h = ((screen_h / 2)//bat_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)


    def _create_bat(self, current_x: int, current_y: int):
        """Creates a new bat and place in fleet"""
        new_bat = Bat(self, current_x, current_y)

        self.fleet.add(new_bat)


    def _check_fleet_edges(self):
        """Bats respond to edges and stay on screen"""
        bat: Bat
        for bat in self.fleet:
            if bat.check_edges():
                self._drop_bat_fleet()
                self.fleet_direction *= -1
                break


    def _drop_bat_fleet(self):
        """Drop fleet"""
        for bat in self.fleet:
            bat.y += self.fleet_drop_speed


    def update_fleet(self):
        """Updates fleet"""
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        """Draws bat from Bat class"""
        bat: 'Bat'
        for bat in self.fleet:
            bat.draw_bat()


    def check_collisions(self, other_group):
        """Fleet collision check"""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)


    def check_fleet_bottom(self):
        """Checks for bottom of screen collision"""
        bat: Bat
        for bat in self.fleet:
            if bat.rect.bottom >= self.settings.screen_h:
                return True
        return False


    def check_destroyed_status(self):
        """Check if fleet is destroyed"""
        return not self.fleet
    