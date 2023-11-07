import random
import pygame

class Player:
    def __init__(self):
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        
    # Game related functions
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)