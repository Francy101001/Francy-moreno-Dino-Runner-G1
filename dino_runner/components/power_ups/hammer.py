import pygame
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager


class Hammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        self.is_active = False
        self.power_up = PowerUp(HAMMER, HAMMER_TYPE)
        self.hammer_image = HAMMER
        self.hammer_rect = self.hammer_image.get_rect()
        


    def throw_hammer(self, player):
        if self.power_up.duration:
            self.hammer_rect.x = player.rect.x + player.rect.width
            self.hammer_rect.y = player.rect.y + player.rect.height/2 - self.hammer_rect.height/2
            self.is_active = True
            for obstacle in player.obstacle_manager.obstacles:
                if self.hammer_rect.colliderect(obstacle.rect):
                    player.obstacle_manager.remove_obstacle(obstacle)
            if self.hammer_rect.x > SCREEN_WIDTH:
                self.hammer_rect.x = player.rect.x + player.rect.width
                self.is_active = False


    def draw(self, screen):
        super().draw(screen)
        if self.is_active:
            screen.blit(self.hammer_image, self.hammer_rect)