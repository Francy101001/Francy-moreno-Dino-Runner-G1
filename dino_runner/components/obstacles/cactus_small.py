import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS


class SmallCactus(Obstacle):
    def __init__(self):
        random_img = random.randint(0, 2)
        super().__init__(SMALL_CACTUS[random_img], pos_y=325)
