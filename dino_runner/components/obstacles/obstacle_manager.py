
import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus_small import SmallCactus
from dino_runner.components.obstacles.obstacle import Obstacle



class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        if not self.obstacles:
            obstacle_type = random.choice(["cactus", "bird", "small_cactus"])
            if obstacle_type == "cactus":
                self.obstacles.append(Cactus())
            elif obstacle_type == "small_cactus":
                self.obstacles.append(SmallCactus())
            else:
                self.obstacles.append(Bird())
            
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                #game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
