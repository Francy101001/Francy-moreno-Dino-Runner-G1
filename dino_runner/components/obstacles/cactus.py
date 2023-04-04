
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        random_img = random.randint(0,2) 
        super().__init__(LARGE_CACTUS[random_img], pos_y = 300)