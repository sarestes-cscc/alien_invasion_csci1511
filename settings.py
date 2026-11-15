from pathlib import Path

class Settings:

    def __init__(self):
        self.name: str = "Graveyard Shift"
        self.screen_w = 1300
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "graveyard.png" 
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / "Assets" / "file" / "scores.json"

        self.cat_file = Path.cwd() / "Assets" / "Images" / "cat.png"
        self.cat_w = 70
        self.cat_h = 90

        self.bullet_file = Path.cwd() / "Assets" / "Images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "pew.mp3"
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "pop.mp3"
        

        self.bat_file = Path.cwd() / 'Assets' / 'images' / 'bat.png'
        self.bat_w = 40
        self.bat_h = 30
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 0, 0)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'


    def initialize_dynamic_settings(self):
        self.cat_speed = 5
        self.starting_cat_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 30
        self.bat_points = 50


    def increase_difficulty(self):
        self.cat_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
