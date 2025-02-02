import pygame
from config import Config
from snake import Snake
from apple import Apple


class Game:
    def __init__(self):  
        self.snake = Snake()
        self.apple = Apple()
        self.score = 0
        self.score2 = 1 
        self.FPS = 90
        self.fpsClock = pygame.time.Clock()
        self.font = pygame.font.Font('./text.ttf', 20)
        self.font2 = pygame.font.Font('./text.ttf', 40)
        self.myText = ""
        self.myText2 = ""
        self.color = Config['colors']['black']
        self.color2 = Config['colors']['apple-red']
        self.file = "highscore.txt"
        self.speed1 = 5
        self.speed2 = -5
        self.effect = pygame.mixer.Sound("sound.mp3")
        self.effect2 = pygame.mixer.Sound("gg.mp3")
        self.effect3 = pygame.mixer.Sound("eat.wav")

    def diff(self, value, value2, score):
        self.speed1 += value
        self.speed2 += value2
        self.score2 += score
        
    def loop(self, screen):

        self.effect.play()

        quitVar = True

        while quitVar == True:
            background = pygame.image.load("snake_background.jpg")
            screen.blit(background, (0,0))
            bumper = Config['game']['bumper_size']
            border_color = Config['colors']['green']
            border1 = pygame.draw.rect(screen, border_color, (0, 0, 20, 650))
            border2 = pygame.draw.rect(screen, border_color, (1180, 0, 20, 650))
            border3 = pygame.draw.rect(screen, border_color, (0, 630, 1200, 20))
            border4 = pygame.draw.rect(screen, border_color, (0, 0, 1200, 20))
            self.myText = "Score:" + str(self.score)
            self.text = self.font.render(self.myText, True, self.color)
            self.textRect = self.text.get_rect(center = (600, 600))
            screen.blit(self.text, self.textRect)
            self.myText2 = "Game Over" 
            self.text2 = self.font2.render(self.myText2, True, self.color2)
            self.textRect2 = self.text2.get_rect(center = (600, 300))

            if self.snake.show == True: 
                self.snake.createSnake(screen) 
                self.apple.createApple(screen)

            else:
                screen.blit(self.text2, self.textRect2)
                self.effect.stop()
                self.effect2.play()
                
               
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    quitVar = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.speed_y = self.speed2
                        self.snake.speed_x = 0

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.speed_y = self.speed1
                        self.snake.speed_x = 0
                        
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.speed_x = self.speed2
                        self.snake.speed_y = 0 

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.speed_x = self.speed1
                        self.snake.speed_y = 0
                        

            if self.snake.rect.colliderect(self.apple.rect):
                self.apple.randomize()
                self.score += self.score2
                self.effect3.play()
                self.snake.eat()

            self.snake.move()
                               
                
            if self.snake.rect.colliderect(border1):
                self.snake.show = False 
                
                
            if self.snake.rect.colliderect(border2):
                self.snake.show = False
                
                

            if self.snake.rect.colliderect(border3):
                self.snake.show = False
                

            if self.snake.rect.colliderect(border4):
                self.snake.show = False
                 
            
            pygame.display.update()
            self.fpsClock.tick(self.FPS)

        pygame.quit()


