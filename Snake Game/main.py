import pygame
from game import Game
from config import Config
from instructions import instruct

pygame.init()

pygame.display.set_caption("Snake Game") 

screen = pygame.display.set_mode((1200,650))

bg = pygame.image.load("snake_background.jpg")

image = pygame.image.load("snake.png")
image_x = 600
image_y = 180 

font = pygame.font.Font('./text.ttf', 20)

color = Config['colors']['green']
color2 = Config['colors']['black']
color3 = Config['colors']['apple-red'] 


screen.blit(bg, (0,0))

start = pygame.draw.rect(screen, color, (470, 350, 250, 50))
instructions = pygame.draw.rect(screen, color, (470, 430, 250, 50))
easy = pygame.draw.rect(screen, color, (360, 520, 150, 50))
medium = pygame.draw.rect(screen, color, (520, 520, 150, 50))
hard = pygame.draw.rect(screen, color, (680, 520, 150, 50))


text = font.render('Play', True, color2)
textRect = text.get_rect(center = (590, 370))
screen.blit(text, textRect)

text2 = font.render('Instructions', True, color2)
textRect2 = text2.get_rect(center = (590, 450))
screen.blit(text2, textRect2)

text3 = font.render('Easy', True, color2)
textRect3 = text3.get_rect(center = (430, 540))
screen.blit(text3, textRect3)

text4 = font.render('Medium', True, color2)
textRect4 = text4.get_rect(center = (590, 540))
screen.blit(text4, textRect4)

text5 = font.render('Hard', True, color2)
textRect5 = text5.get_rect(center = (750, 540))
screen.blit(text5, textRect5)

rect = image.get_rect()
rect.center = (image_x, image_y) 
screen.blit(image, rect)
Start = Game()

effect = pygame.mixer.Sound("bgtrack.mp3")
effect2 = pygame.mixer.Sound("click.mp3")

select = ""

effect.play()

    
quitVar = True

while quitVar == True:

    for event in pygame.event.get():

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            if start.collidepoint(position):
                effect.stop()
                effect2.play()
                Start.loop(screen)


            if instructions.collidepoint(position):
                effect.stop()
                effect2.play()
                Start2 = instruct()
                Start2.loop(screen)
                
            if select == "easy":
                break 

            if select == "medium":
                break

            if select == "hard":
                break


            if easy.collidepoint(position):
                Start.diff(0, 0, 0)
                pygame.draw.rect(screen, color3, (360, 520, 150, 50))
                text3 = font.render('Easy', True, color2)
                textRect3 = text3.get_rect(center = (430, 540))
                screen.blit(text3, textRect3)
                select = "easy"
                effect2.play()

               
                
            if medium.collidepoint(position):
                Start.diff(3, -3, 1)
                pygame.draw.rect(screen, color3, (520, 520, 150, 50))
                text4 = font.render('Medium', True, color2)
                textRect4 = text4.get_rect(center = (590, 540))
                screen.blit(text4, textRect4)
                select = "medium"
                effect2.play()


            if hard.collidepoint(position):
                Start.diff(5, -5, 3)
                pygame.draw.rect(screen, color3, (680, 520, 150, 50))
                text5 = font.render('Hard', True, color2)
                textRect5 = text5.get_rect(center = (750, 540))
                screen.blit(text5, textRect5)
                select = "hard"
                effect2.play()

                
                            
    pygame.display.update()

pygame.quit()





