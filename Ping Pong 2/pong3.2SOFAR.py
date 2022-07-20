import pygame


SCR_WID, SCR_HEI = 640, 480
class Player():
        def __init__(self, name):
                self.name = name
                if self.name == "hero":
                        self.x, self.y = 16, SCR_HEI/2
                        self.padWid, self.padHei = 8, 64
                        
                elif self.name == "player":
                        self.padWid, self.padHei = 8, 64
                        self.y, self.x = SCR_WID-400, SCR_HEI-30
                   
       
                else:
                        self.x, self.y = SCR_WID-16, SCR_HEI/2
                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
        def scoring(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                if self.name == "hero":
                    screen.blit(scoreBlit, (32, 16))
                    if self.score == 10:
                        print ("player 1 wins!")
                        exit()
                else:
                    screen.blit(scoreBlit, (SCR_HEI+92, 16))
                    if self.score == 10:
                        print ("player 2 wins!")
                        exit()
       
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

                elif self.name == "player":
                    if keys[pygame.K_f]:
                        self.y -= self.speed#left
                    elif keys[pygame.K_g]:
                        self.y += self.speed

                    if self.y <= 0:
                        self.y = 0
                    elif self.y > SCR_WID-64:
                        self.y = SCR_WID-64
                else:
                   
                    if keys[pygame.K_UP]:
                            self.y -= self.speed
                    elif keys[pygame.K_DOWN]:
                            self.y += self.speed
           
                    if self.y <= 0:
                            self.y = 0
                    elif self.y >= SCR_HEI-64:
                            self.y = SCR_HEI-64
       
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))

        def draw2(self):
                pygame.draw.rect(screen, (255, 255, 255), ( self.y, self.x, self.padWid, self.padHei))
##class Enemy():
##        def __init__(self):
##                self.x, self.y = SCR_WID-16, SCR_HEI/2
##                self.speed = 3
##                self.padWid, self.padHei = 8, 64
##                self.score = 0
##                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
##       
##        def scoring(self):
##                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
##                screen.blit(scoreBlit, (SCR_HEI+92, 16))
##                if self.score == 10:
##                        print ("Player 2 wins!")
##                        exit()
##       
##        def movement(self):

##       
##        def draw(self):
##                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
## 
class Ball():
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
                self.size = 10

        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
                
                #wall collide bottom top

                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
                        
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
                                                
                for n in range(-self.size, player2.padHei):
                        if self.y == 470:
                                if self.y == player.padWid : #+ player2.midtop:
                                        self.speed_x *= -1
                                        #self.speed_y *= -1
                                        ballOut.play()#Added sound to ball hit
                                        break
                      
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

##        def ballHitsPad(self):
##                for ball in balls:
##                        if player2.colliderect(ball['rect']):
##                            return True
##                return False

pygame.init()
SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60
pygame.mixer.music.load('pickup.wav')
ballOut = pygame.mixer.Sound('pickup.wav')
#pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
backGround = pygame.image.load('pingpongtable.png')
backGroundStretched = pygame.transform.scale(backGround, (640, 480))



player = Player("hero")
player2 = Player("player")

ball = Ball()
#player = Player()
enemy = Player("enemy")
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
            ball.draw()
            player.draw()
            player2.draw2()
            player.scoring()
            enemy.draw()
            enemy.scoring()

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

