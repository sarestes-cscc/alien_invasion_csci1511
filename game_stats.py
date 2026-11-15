"""
    GraveYard Shift
    Sarah Estes
    Controls for stats: max score and hi-score
    11/15/2026 
"""


# from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from graveyard_shift import GraveYardShift

class GameStats:
    """Track statistics for Graveyard Shift"""
    def __init__(self, game: 'GraveYardShift'):
        """Initializing the stats"""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()


    def init_saved_scores(self):
        """Checks for hi-score"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # save the file 


    def save_scores(self):
        """Saves hi-score in json file"""
        scores = {
            "hi_score": self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')


    def reset_stats(self):
        """Resets stats when game ends"""
        self.cats_left = self.settings.starting_cat_count
        self.score = 0
        self.level = 1


    def update(self, collisions):
        """Update scores"""
        self._update_score(collisions)
        # update max score
        self._update_max_score()
        # calculate high score
        self._update_hi_score()


    def _update_score(self, collisions):
        """Updates current score"""
        for bat in collisions.values():
            self.score += self.settings.bat_points
        # print(f"Basic: {self.score}")


    def _update_max_score(self):
        """Updates Max score"""
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f"Max score: {self.max_score}")


    def _update_hi_score(self):
        """Updates hi-score"""
        if self.score > self.hi_score:
            self.hi_score = self.score
        # print(f"Max score: {self.hi_score}")


    def update_level(self):
        """Update level when fleet is destroyed"""
        self.level += 1
        # print(self.level)