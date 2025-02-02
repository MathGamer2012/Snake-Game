import pygame
from config import Config
import random

class Apple:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = ""
        self.colour = Config['colors']['apple-red']
        self.width = Config['apple']['width']
        self.height = Config['apple']['height']
        self.randomize()

    def createApple(self, screen):
        self.rect = pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

    def randomize(self):
        self.x = random.randint(50, 1150)
        self.y = random.randint(50, 550)

   

