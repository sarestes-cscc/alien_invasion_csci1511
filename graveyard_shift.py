"""
    GraveYard Shift
    Sarah Estes
    Main game file and logic
    11/15/2026 
"""


import sys
import pygame
from settings import Settings
from game_stats import GameStats
from cat import Cat
from arsenal import Arsenal
# from bat import Bat
from bat_fleet import BatFleet
from time import sleep
from button import Button
from hud import HUD

class GraveYardShift:
    """Main logic for GraveYard Shift"""
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.5)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)


        self.cat = Cat(self, Arsenal(self))
        self.bat_fleet = BatFleet(self)
        self.bat_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False


    def run_game(self):
        """Start the main loop for the game"""
        while self.running:
            self._check_events()
            if self.game_active:
                self.cat.update()
                self.bat_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)


    def _check_collisions(self):
        """Checks cat, bat, and laser collisions"""
        if self.cat.check_collisions(self.bat_fleet.fleet):
            self._check_game_status()
            # subtract one life if possible

        # check collisions for bats and bottom of screen
        if self.bat_fleet.check_fleet_bottom():
            self._check_game_status()
       
        # check collisions of projectiles and bats
        collisions = self.bat_fleet.check_collisions(self.cat.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.bat_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # udpate game stats level
            self.game_stats.update_level()
            # update HUD view
            self.HUD.update_level()


    def _check_game_status(self):
        """Checks status and ends game if no lives left"""
        if self.game_stats.cats_left > 0:
            self.game_stats.cats_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False


    def _reset_level(self):
        """Resets level once all lives are lost"""
        self.cat.arsenal.arsenal.empty()
        self.bat_fleet.fleet.empty()
        self.bat_fleet.create_fleet()


    def restart_game(self):
        """Restart game once all lives are lost"""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.cat._center_cat()
        self.game_active = True
        pygame.mouse.set_visible(False)


    def _update_screen(self):
        """Updates screen and draws assets and HUD"""
        self.screen.blit(self.bg, (0,0))
        self.cat.draw()
        self.bat_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()


    def _check_events(self):
        """Check player events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()


    def _check_button_clicked(self):
        """Check is start button is clicked"""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()


    def _check_keyup_events(self, event):
        """Prevents cat from moving if not clicking l/r arrows"""
        if event.key == pygame.K_RIGHT:
            self.cat.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.cat.moving_left = False


    def _check_keydown_events(self, event):
        """Makes cat move if clicking l/r arrows"""
        if event.key == pygame.K_RIGHT:
            self.cat.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.cat.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.cat.fire():
                self.laser_sound.play()
                # self.laser_sound.fadeout(250)

        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()   

if __name__ == '__main__':
    """Game instance"""
    ai = GraveYardShift()
    ai.run_game()
