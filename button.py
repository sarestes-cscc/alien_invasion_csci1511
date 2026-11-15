"""
    GraveYard Shift
    Sarah Estes
    Draws and controls for start button
    11/15/2026 
"""


import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graveyard_shift import GraveYardShift

class Button:
    """Builds the Start button"""
    def __init__(self, game: "GraveYardShift", msg):
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
            self.settings.button_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draw blank button and then draw message"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        """Check if button is clicked"""
        return self.rect.collidepoint(mouse_pos)