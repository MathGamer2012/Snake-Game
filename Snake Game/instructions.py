import pygame
from config import Config
from game import Game

class instruct:

    def __init__(self):
        self.myText = ""
        self.myText2 = ""
        self.myText3 = ""
        self.myText4 = ""
        self.myText5 = ""
        self.myText6 = ""
        self.myText7 = ""
        self.myText8 = "" 
        self.font = pygame.font.Font('./text.ttf', 20)
        self.font2 = pygame.font.Font('./text.ttf', 30)
        self.bg = pygame.image.load("snake_background.jpg")
        self.color = Config['colors']['black']
        self.color2 = Config['colors']['apple-red']
        self.color3 = Config['colors']['green']
        self.effect = pygame.mixer.Sound("click.mp3")



    def loop(self, screen):
        quitVar = True

        while quitVar == True:
            screen.blit(self.bg, (0,0))

            game = pygame.draw.rect(screen, self.color3, (470, 530, 250, 50))

            text9 = self.font.render('Return to Menu ->', True, self.color)
            textRect9 = text9.get_rect(center = (590, 550))
            screen.blit(text9, textRect9)
            
            self.text = self.font.render(self.myText, True, self.color)
            textRect = self.text.get_rect(center = (600, 150))
            screen.blit(self.text, textRect)

            self.text2 = self.font2.render(self.myText2, True, self.color2)
            textRect2 = self.text2.get_rect(center = (600, 50))
            screen.blit(self.text2, textRect2)

            self.text3 = self.font.render(self.myText3, True, self.color)
            textRect3 = self.text3.get_rect(center = (600, 200))
            screen.blit(self.text3, textRect3)

            self.text4 = self.font.render(self.myText4, True, self.color)
            textRect4 = self.text4.get_rect(center = (600, 250))
            screen.blit(self.text4, textRect4)

            self.text5 = self.font.render(self.myText5, True, self.color)
            textRect5 = self.text5.get_rect(center = (600, 300))
            screen.blit(self.text5, textRect5)

            self.text6 = self.font.render(self.myText6, True, self.color)
            textRect6 = self.text6.get_rect(center = (600, 350))
            screen.blit(self.text6, textRect6)

            self.text7 = self.font.render(self.myText7, True, self.color)
            textRect7 = self.text7.get_rect(center = (600, 400))
            screen.blit(self.text7, textRect7)

            self.text8 = self.font.render(self.myText8, True, self.color)
            textRect8 = self.text8.get_rect(center = (600, 450))
            screen.blit(self.text8, textRect8)


            self.myText2 = "Instructions:"
            self.myText = "- To move the snake press the up, down, left, right or a, w, s, d keys"
            self.myText3 = "- Navigate the snake towards the apple"
            self.myText4 = "- The harder the skill level the more points you get per apple"
            self.myText5 = "- Each time the snake consumes an apple it grows bigger"
            self.myText6 = "- Make sure to not crash the head of the snake to the body, or else your snake will die!"
            self.myText7 = "- Make sure to not crash the border, or else your snake will die!"
            self.myText8 = "- Try staying alive for long and eating lots of apples to get a strong score, and make it on the leaderboards!"

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()

                    if game.collidepoint(position):
                        self.effect.play()
                        exec(open("main.py").read())



                if event.type == pygame.QUIT:
                    quitVar = False

            pygame.display.update()
            
    pygame.quit() 


