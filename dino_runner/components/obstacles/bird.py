import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD[0], pos_y=random.choice([280, 220, 170]))
        self.index = 0

        
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
     
        screen.blit(BIRD[self.index // 5], self.rect)
        self.index += 1