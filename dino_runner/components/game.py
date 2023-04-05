import pygame
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, START, DEAD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.text_class import Text

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score= Score()
        self.death_count = 0
        self.text = Text()
        
    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def play(self):
        self.playing = True
        self.obstacle_manager.reset()
        self.score.reset_score()
        while self.playing:
            self.events()
            self.update()
            self.draw()
       

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def on_death(self):
        pygame.time.delay(500)
        self.playing = False
        self.death_count += 1
        print("I´m dead")
        print(self.death_count)
    
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.fill((255,255,255))
        if self.death_count:
            game_over_text, game_over_rect = self.text.create_text("GAME OVER", 30, (0,0,0), half_screen_width, half_screen_height - 80)
            self.screen.blit(game_over_text, game_over_rect)

            score_text, score_rect = self.text.create_text(f"Score: {self.score.score}", 22, (0,0,0), half_screen_width, half_screen_height - 20)
            self.screen.blit(score_text, score_rect)

            death_count_text, death_count_rect = self.text.create_text(f"Deaths: {self.death_count}", 22, (0,0,0), half_screen_width, half_screen_height + 10)
            self.screen.blit(death_count_text, death_count_rect)

            high_score_text, high_score_rect = self.text.create_text(f"High score: {self.score.high_score}", 22, (0,0,0), half_screen_width, half_screen_height + 40)
            self.screen.blit(high_score_text, high_score_rect)

            self.screen.blit(DEAD, (half_screen_width - 40, half_screen_height - 190))
        else:
            start_text, start_rect = self.text.create_text("Press any key to start", 30, (0,0,0), half_screen_width, half_screen_height)
            self.screen.blit(start_text, start_rect)
            self.screen.blit(START, (half_screen_width - 45, half_screen_height - 140))
        
        pygame.display.update()
        self.menu_event()
    
    def menu_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()




