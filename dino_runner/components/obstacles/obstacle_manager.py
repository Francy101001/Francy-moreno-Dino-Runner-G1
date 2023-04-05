
import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus_small import SmallCactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.rat import Rat



class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            obstacle_type = random.choice(["cactus", "bird", "small_cactus", "rat"])
            if obstacle_type == "cactus":
                self.obstacles.append(Cactus())
            elif obstacle_type == "small_cactus":
                self.obstacles.append(SmallCactus())
            elif obstacle_type == "rat":
                self.obstacles.append(Rat())
            else:
                self.obstacles.append(Bird())
            
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.colliderect(player.rect):
                on_death()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def reset(self):
        self.obstacles = []
