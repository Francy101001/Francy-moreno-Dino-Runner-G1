
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    CACTUS_TYPE = [
        (LARGE_CACTUS, 300),
        (SMALL_CACTUS, 325)
    ]

    def __init__(self):
        image, pos_y = random.choice(self.CACTUS_TYPE)
        random_img = random.randint(0,2) 
        super().__init__(image[random_img], pos_y)