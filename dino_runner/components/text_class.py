import pygame

class Text:
    @staticmethod
    def create_text(message, size, color, x, y):
        font = pygame.font.Font("freesansbold.ttf", size)
        text = font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        return text, text_rect