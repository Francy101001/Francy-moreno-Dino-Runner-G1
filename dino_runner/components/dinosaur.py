import pygame
from pygame import Surface
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, HAT

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.set_position()
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.hat = HAT[0]


    def update(self, user_input):
        if self.action ==DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
           self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else: 
                self.action = DINO_RUNNING
        
        if self.step >= 10:
            self.step = 0
    
    def run(self):
        self.image = RUNNING[self.step // 5]
        self.set_position()
        self.step += 1
    
    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.action = DINO_RUNNING
            self.set_position()
            self.jump_velocity = self.JUMP_VELOCITY
    
    def duck(self):
        self.image = DUCKING[self.step // 5]
        self.rect = self.image.get_rect()
        self.set_position()
        self.rect.y = self.POS_Y + 40
        self.step += 1
    
    def set_position(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        


    def draw(self, screen: Surface ):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        hat_image = HAT[0]
        hat_width, hat_height = hat_image.get_size()
        new_width = int(hat_width / 4)  # Redimensiona la imagen a un cuarto del ancho original
        new_height = int(hat_height / 4)  # Redimensiona la imagen a un cuarto de la altura original
        hat_image = pygame.transform.scale(hat_image, (new_width, new_height))  # Redimensiona la imagen
        
        hat_rect = hat_image.get_rect()
        hat_rect.x = self.rect.x + 15
        if self.action == DINO_RUNNING or self.action == DINO_JUMPING:
            hat_rect.y = self.rect.y - 30
        elif self.action == DINO_DUCKING:
            hat_rect.x = self.rect.x + 40
            hat_rect.y = self.rect.y - 30
        screen.blit(hat_image, hat_rect)  # Dibuja la imagen redimensionada
        
    


