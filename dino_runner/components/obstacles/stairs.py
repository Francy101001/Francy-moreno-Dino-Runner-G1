
from pygame import Surface
import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import STAIRS

class Stairs(Sprite):
    def __init__(self):
        super().__init__()
        self.image = STAIRS
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(STAIRS, (211, 241))
        self.rect.x = 80
        self.rect.y = 50
        
        
    def draw(self, screen: Surface ):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    