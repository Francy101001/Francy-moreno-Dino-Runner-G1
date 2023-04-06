import pygame
from pygame import Surface
from pygame.sprite import Sprite
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING, JUMPING, DUCKING, HAT, RUNNING_SHIELD, SCREEN_WIDTH, SHIELD_TYPE
from dino_runner.components.text_class import Text



DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"
IMG_RUNNING = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
IMG_JUMPING = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
IMG_DUCKING = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}

class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = IMG_RUNNING[self.type][0]
        self.set_position()
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.hat = HAT[0]
        self.hat_image = pygame.transform.scale(HAT[0], (80, 80))
        self.hat_rect = self.hat_image.get_rect(center=(0, 0))
        self.hat_rotation = 0
        self.power_up_time_up = 0
        
        


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
        self.update_image(IMG_RUNNING[self.type][self.step // 5])
        self.set_position()
        self.step += 1
    
    def jump(self):
        pos_y = self.rect.y - self.jump_velocity * 4
        self.update_image(IMG_JUMPING[self.type], pos_y=pos_y)
        self.jump_velocity -= 0.8
        self.hat_rotation = 360
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.action = DINO_RUNNING
            self.set_position()
            self.jump_velocity = self.JUMP_VELOCITY
    
    def duck(self):
        self.image = IMG_DUCKING[self.type][self.step // 5]
        self.rect = self.image.get_rect()
        self.set_position()
        self.rect.y = self.POS_Y + 40
        self.step += 1
    
    def set_position(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
    
    def update_image(self, image:pygame.Surface, pos_x = None, pos_y=None, on_death= False):
        self.image = image
        if not on_death:
            self.rect = image.get_rect()
            self.rect.x = pos_x or self.POS_X
            self.rect.y = pos_y or self.POS_Y
        


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
        
    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        self.power_up_time_up = power_up.start_time + power_up.duration * 1000

    def draw_power_up(self, screen):
        if self.type != DEFAULT_TYPE:
            time_to_show = round(
                (self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                text, text_rect = Text.create_text(f"{self.type.capitalize()} enabled for {time_to_show} seconds", 18, (0,0,0), SCREEN_WIDTH // 2, 40)
                screen.blit(text, text_rect)

            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0
