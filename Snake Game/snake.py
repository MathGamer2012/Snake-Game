import pygame
import random 
from config import Config

class Snake:
    def __init__(self):
        self.x = 600
        self.y = 300
        self.body = []
        self.rect = "" 
        self.colour = Config['colors']['green']
        self.width = Config['snake']['width']
        self.height = Config['snake']['height']
        self.size = 0
        self.speed_x = Config['snake']['speed']
        self.speed_y = Config['snake']['speed']
        self.show = True 

    def eat(self):
        self.size += 1
        
    def createSnake(self, screen):
        self.rect = pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        for i in range(self.size):
            hi = pygame.draw.rect(screen, self.colour, (self.body[i][0], self.body[i][1], self.width, self.height))
            for i in range(len(self.body)):
                if (self.body[i] == [self.x, self.y]):
                    self.show = False 
                    
    def move(self):

        self.body.append([self.x,self.y])
       
        self.x += self.speed_x
        self.y += self.speed_y
        

        if len(self.body) > self.size:
            self.body.pop(0)





