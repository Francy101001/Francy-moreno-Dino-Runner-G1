
import os
import pygame
from pygame.sprite import Sprite
from dino_runner.components.text_class import Text

class Score(Sprite):
    def __init__(self):
        self.score = 0
        self.high_score = self.load_high_score()
        
    
    def load_high_score(self):
        if not os.path.exists("high_score.txt"):
            return 0
        with open("high_score.txt", "r") as f:
            return int(f.read().strip())

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))
    
    def update_score(self, score):
        self.score = score
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
    
    def reset_score(self):
        self.score = 0
        
        
    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2
        self.update_score(self.score)

    def draw(self, screen):
        text, text_rect = Text.create_text(f"Score: {self.score}", 22, (0, 0, 0), 1000, 50)
        screen.blit(text, text_rect)
    