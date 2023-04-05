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
        self.hat_image = pygame.transform.scale(HAT[0], (80, 80))
        self.hat_rect = self.hat_image.get_rect(center=(0, 0))
        self.hat_rotation = 0
        
        


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
        
        if self.hat_rotation > 0:
            self.hat_rotation -= 10
        elif self.hat_rotation < 0:
            self.hat_rotation += 10
        
    
    def run(self):
        self.image = RUNNING[self.step // 5]
        self.set_position()
        self.step += 1
    
    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        self.hat_rotation = 360
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

        if self.action == DINO_RUNNING or self.action == DINO_JUMPING:
            hat_x, hat_y = self.rect.x + 45, self.rect.y - 5
        elif self.action == DINO_DUCKING:
            hat_x, hat_y = self.rect.x + 80, self.rect.y - 10
        else:
            hat_x, hat_y = -100, -100

        self.hat_rect.center = (hat_x, hat_y)
        rotated_hat = pygame.transform.rotate(self.hat_image, self.hat_rotation)
        screen.blit(rotated_hat, self.hat_rect)# Dibuja la imagen redimensionada
        
    


