
import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.rat import Rat



class ObstacleManager:
    OBTSACLES = [Cactus, Bird]


    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            obstacle = random.choice(self.OBTSACLES)
            self.obstacles.append(obstacle())
            
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect):
                on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        self.obstacles = []
