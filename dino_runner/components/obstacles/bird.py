import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self):
        pos_y = random.randint(200,320)
        super().__init__(BIRD[0], pos_y)
        self.step = 0
    
    def update(self, game_speed, obstacles):
        self.image = BIRD[self.step // 10]
        super().update(game_speed + 3, obstacles)
        self.step += 1
        if self.step >= 20:
            self.step = 0

    