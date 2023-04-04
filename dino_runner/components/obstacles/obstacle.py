from pygame.sprite import Sprite
from pygame import Surface
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image: Surface, pos_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = pos_y

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()



    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
