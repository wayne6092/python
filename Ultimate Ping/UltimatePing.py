import pygame, time

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


BACKGROUNDCOLOR = (255, 255, 255)        
TEXTCOLOR = (0, 0, 0)

SCR_WID, SCR_HEI = 640, 480
class Player():
        def __init__(self, name):
                self.name = name
                if self.name == "hero":
                        self.x, self.y = 16, SCR_HEI/2
                        self.padWid, self.padHei = 8, 64
                        
                elif self.name == "enemy":
                        self.padWid, self.padHei = 8, 64
                        self.x, self.y = SCR_WID-16, SCR_HEI/2

                   
       
                else:
                        self.y, self.x = SCR_WID-400, SCR_HEI-30
                        self.padWid, self.padHei = 64, 8
                        
                self.speed = 3
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
        def scoring(self):

                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))

                if player2.score >= 10 or player.score >= 10 or enemy.score >= 10:
                            screen.blit(gameOver2Stretched, (0,0))
                            if self.score == 11:
                                    exit()

                if self.name == "hero":
                        screen.blit(scoreBlit, (32, 16))

                        
                elif self.name == "enemy":
                        screen.blit(scoreBlit, (SCR_HEI+92, 16))



                else:
                        screen.blit(scoreBlit, (SCR_HEI/2, SCR_WID/2))
##                        if self.score >= 10:
##                                print ("player 3 wins!")
##                                exit()
           
       
        def movement(self):
                keys = pygame.key.get_pressed()
                if self.name == "hero":
                    if keys[pygame.K_w]:
                            self.y -= self.speed
                    elif keys[pygame.K_s]:
                            self.y += self.speed
           
                    if self.y <= 0:
                            self.y = 0
                    elif self.y >= SCR_HEI-64:
                            self.y = SCR_HEI-64

                elif self.name == "enemy":
                    if keys[pygame.K_UP]:
                            self.y -= self.speed
                    elif keys[pygame.K_DOWN]:
                            self.y += self.speed
           
                    if self.y <= 0:
                            self.y = 0
                    elif self.y >= SCR_HEI-64:
                            self.y = SCR_HEI-64
                            
                else:
                    if keys[pygame.K_f]:
                        self.y -= self.speed#left
                    elif keys[pygame.K_g]:
                        self.y += self.speed

                    if self.y <= 0:
                        self.y = 0
                    elif self.y > SCR_WID-64:
                        self.y = SCR_WID-64
        def draw(self):
                pygame.draw.rect(screen, (255, 0, 200), (self.x, self.y, self.padWid, self.padHei))

        def draw2(self):
                pygame.draw.rect(screen, (0, 255, 0), ( self.y, self.x, self.padWid, self.padHei))
                
        def draw3(self):
                pygame.draw.rect(screen, (0, 0, 255), ( self.x, self.y, self.padWid, self.padHei))

class Ball():
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
                self.size = 12


        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
                
                #wall collide bottom top

                if self.y <= 0:
                        self.speed_y *= -1
                  
                elif self.y >= SCR_HEI-self.size:
                        self.__init__()
                        player2.score -= 1
                        
                if self.x <= 0:
                        self.__init__()
                        enemy.score += 1
                        #ballOut.play()
                        
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed_x = 3
                        player.score += 1
                        
                ##wall col
                #paddle col
                #player
                #                  y is width                 x is height
                                                
                for n in range(-self.size, player2.padWid):
                        if self.y == player2.x + n:
                                if self.x >= player2.padHei:
                                        if self.x >= player2.y - player2.padWid:
                                                if self.x <= player2.y + player2.padWid:
                                                        self.speed_y *= -1
                                                        ballOut.play()#Added sound to ball hit
                                                        
                                                        player2.score += 1
       
                                                        break
                                                        #self.speed_y *= -1
                                        

                        n += 1
                        
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        ballOut.play()#Added sound to ball hit
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x - enemy.padWid:
                                        self.speed_x *= -1
                                        ballOut.play()#Added sound to ball hit
                                        break
                        n += 1



                ##paddle col
 
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))

                



pygame.init()
SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60
pygame.mixer.music.load('pickup.wav')
ballOut = pygame.mixer.Sound('pickup.wav')

musicPlaying = True

backGround = pygame.image.load('pingpongtable.png')
backGroundStretched = pygame.transform.scale(backGround, (640, 480))

backGround2 = pygame.image.load('pingpongtable3.png')
backGround2Stretched = pygame.transform.scale(backGround2, (640, 480))

backGround3 = pygame.image.load('pingpongtable4.png')
backGround3Stretched = pygame.transform.scale(backGround3, (640, 480))

gameOver = pygame.image.load('gameover.png')
gameOverStretched = pygame.transform.scale(gameOver, (640, 480))

gameOver2 = pygame.image.load('gameover.png')
gameOver2Stretched = pygame.transform.scale(gameOver2, (640, 480))

player = Player("hero")
player2 = Player("Jim")
enemy = Player("enemy")
ball = Ball()

def main():
        while True:
            #process
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            print ("Game exited by user")
                            exit()


                            
            ##process
            #logic
            ball.movement()
            player.movement()
            enemy.movement()
            player2.movement()
            ##logic
            #draw
            screen.fill((0, 0, 0))
            screen.blit(backGroundStretched, (0, 0))
            if player2.score >= 3 or player.score >= 3 or enemy.score >= 3:
                    screen.blit(backGround2Stretched, (0,0))

            if player2.score >= 7 or player.score >= 7 or enemy.score >= 7:
                    screen.blit(backGround3Stretched, (0,0))
                    
                    if player2.score == 10:
                            print("Player3 wins!")
                            break
                    if player.score == 10:
                            print ("player 1 wins!")
                            break
                    if enemy.score == 10:
                            print("Player2 wins!")
                            break

            ball.draw()
            player.draw()
            player2.draw2()
            player2.scoring()
            player.scoring()
            enemy.draw3()
            enemy.scoring()
            drawText("hi", "Arial", (window), 100, 100, (0,0,0))
            ##draw
            #_______
            pygame.display.flip()
            clock.tick(FPS)

main()


#all the variables of Rect
##x, y, top, left, bottom, right, topleft,
##bottomleft, topright, bottomright, midtop,
##midleft, midbottom, midright, center, centerx,
##centery, size, width, height, w, h

