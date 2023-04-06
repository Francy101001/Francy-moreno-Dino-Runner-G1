
import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.rat import Rat




class ObstacleManager:
    OBTSACLES = [Cactus, Bird, Rat]


    def __init__(self):
        self.obstacles: list[Obstacle] = []
        

    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            obstacle = random.choice(self.OBTSACLES)
            self.obstacles.append(obstacle())
    
            
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if isinstance(obstacle, Rat) and obstacle.rect.colliderect(player.rect):
                # Comprobar si el jugador está por debajo o encima de la escalera
                player_top = player.rect.top
                stairs_bottom = obstacle.stairs.rect.bottom
                stairs_top = obstacle.stairs.rect.top
                stairs_height = obstacle.stairs.rect.height
                if player_top >= stairs_bottom:
                    # El jugador está por encima de la escalera-> ignorar la colisión
                    continue
                elif player_top + player.rect.height < stairs_top + stairs_height:
                    # El jugador está por debajo de la escalera-> morir
                    continue
                    #on_death()
            elif obstacle.rect.colliderect(player.rect):
                #on_death()
                continue
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    
    def reset(self):
        self.obstacles = []
    
    
