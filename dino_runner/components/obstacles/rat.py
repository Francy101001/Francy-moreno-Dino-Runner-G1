import random

import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import RAT


class Rat(Obstacle):
    def __init__(self):
        super().__init__(RAT[0], pos_y=190)
        self.index = 0


        
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
     
        self.index += 1
        
        screen.blit(RAT[self.index // 5], self.rect)