#from livewires import games, color
import pygame
from pygame.locals import *
import math, random, time, sys

pygame.init()

screen = pygame.display.set_mode((640,480))

font = pygame.font.SysFont("arial",16)

clock = pygame.time.Clock()


end_game = False

ammo = 20
score = 0
#print(dir(pygame))
#print(dir(pygame.sprite.Sprite))
#print(dir(pygame.sprite.Group))

ammoDisplay = font.render(str(ammo),1,(0,0,0))
scoreDisplay = font.render(str(score),1,(0,0,0))

screen.blit(scoreDisplay,(10,10))
screen.blit(ammoDisplay, (10,20))

playField = pygame.sprite.Group(())
player = pygame.sprite.Group(())
gun = pygame.sprite.Group(())
enemy = pygame.sprite.Group(())
missile = pygame.sprite.Group(())
explosion = pygame.sprite.Group(())

#We need a HERO

class Tank(pygame.sprite.Sprite):
    image = pygame.image.load("tank.bmp")
    GunX = 0
    GunY = 0
    GunAngle = 0#angle of the gun
    MISSILE_DELAY = 30

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
       
        self.image = Tank.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))#What does this do?
        self.rect.x = x
        self.rect.y = y

        Tank.GunX =  self.rect.x + self.rect.width/2 - 12
        Tank.GunY = self.rect.top + 6
        
        the_gun = Gun(Tank.GunX  , Tank.GunY)#instantiates gun
        gun.add(the_gun)
    
        self.missile_wait = 0
   # new code #     
    def stop_message(self):
            
            stop_message = font.render("Not allowed past this point, Please reverse direction",1,(255,0,0))
            screen.blit(stop_message,(screen.get_width()/2,screen.get_height()/2))
            
    def update(self):
        global ammo
        global end_game
        key = pygame.key.get_pressed()
        
        if self.missile_wait > 0:
            self.missile_wait -= 1       
        if key[K_LEFT] and  self.rect.x > 20:
            self.rect.left -= 1
            Tank.GunX -= 1
        if key[K_RIGHT] and self.rect.x <= 346:
            self.rect.left += 1
            Tank.GunX += 1
        if self.rect.x >= 346:
            self.stop_message()
        
        if key[K_SPACE] and self.missile_wait == 0 and self.rect.x <= 346:
            new_missile = Missile(self.rect.x, self.rect.y, Tank.GunAngle )#Tank angle is 0, instantiate missile
            missile.add(new_missile)
            self.missile_wait = Tank.MISSILE_DELAY

            ammo -= 1
            #ammo.left = 10
            #new
            if ammo <= 0:
                end_game = True
                
    # def end_game(self):
        
        # end_message = font.render("Game Over",1,(255,0,0))
        # screen.blit(end_message,(screen.get_width()/2,screen.get_height()/2))
        # # end_message = games.Message(value = "Game Over",
                                    # # size = 90,
                                    # # color = color.red,
                                    # # x = games.screen.width/2,
                                    # # y = games.screen.height/2,
                                    # # lifetime =  games.screen.fps,
                                    # # after_death = games.screen.quit)
        # #games.screen.add(end_message)
        
class Missile(pygame.sprite.Sprite):

    image = pygame.image.load("missile.bmp")

    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 25#25 times through the loop
    TT = 0
    SX = 0
    SY = 0

    def __init__(self, tank_x, tank_y, tank_angle):
        """ Initialize missile sprite. """
        super().__init__()
        #pygame.sprite.Sprite.__init__(self)
        self.image = Missile.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        
        # convert to radians
        self.angle = (tank_angle + 90) * math.pi / 180  
        self.tank_x = tank_x
        self.tank_y = tank_y
        
        # calculate missile's starting position 
        self.buffer_x = Missile.BUFFER * math.sin(self.angle)
        self.buffer_y = Missile.BUFFER * -math.cos(self.angle)
        self.rect.x = tank_x + self.buffer_x
        self.rect.y = tank_y + self.buffer_y

        # calculate missile's velocity components
        self.dx = Missile.VELOCITY_FACTOR * math.sin(self.angle)
        self.dy = Missile.VELOCITY_FACTOR * -math.cos(self.angle)


         # calculate missile's velocity components
        self.vx = self.dx
        self.vy = self.dy
        #explosion.draw(screen)

        # create the missile
        # super(Missile, self).__init__(image = Missile.image,
                                      # x = x, y = y,
                                      # dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME
      
##    def collide(self):
##        while self.is_collideable == False:
##            print ("collide")
##            self.kill()


    def die(self):
        """ Destroy self and leave explosion behind. """

        new_explosion = Explosion(x = self.rect.x, y = self.rect.y)
        explosion.add(new_explosion)
        self.image.set_colorkey(self.image.get_at((0,0)))

        self.kill()


     
    def update(self):
        global GRAVITY
        """ Move the missile. """
        super(Missile, self).update() 
   
        time.sleep(.01)            
        
        # if lifetime is up, start the decent   
        self.lifetime -= 1
      
        if self.lifetime <= 0:

            self.SX = self.rect.x
            self.SY = self.rect.y

            self.rect.x = int(self.dx * self.TT + self.rect.x)
            self.rect.y = int ((.5 * GRAVITY * self.TT * self.TT) - (self.dy * self.TT) + self.rect.y)

            self.TT += .25
       

        else:
            #quick (and sub-optimal) replacement for the missing livewires update method
            #no smooth trajectories today...
            self.rect.x += self.dx
            self.rect.y += self.dy#velocity


        self.check_collide()

        self.check_kill_enemy()
        
    def check_collide(self):
        if self.rect.y > 344:
            self.die()

    def check_kill_enemy(self):
        global score
        
        for e in pygame.sprite.groupcollide(missile,enemy,0,1):
  
            self.die()
            #new"Update SCORE"
            score += 10
            #score.right = screen.width - 10
            
            the_enemy = Enemy()
            enemy.add(the_enemy)

class Gun(pygame.sprite.Sprite):
    image = pygame.image.load("gun.bmp")
 
    
    def __init__(self,  tank_x, tank_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Gun.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect.x = tank_x
        self.rect.y = tank_y
        self.angle = 90
        #super(Gun, self).__init__(image = Gun.image,
                                      #x = x, y = y)
    def update(self):
        super().__init__()
        key = pygame.key.get_pressed()

        if key[K_UP]:
            self.angle -= 1
            Tank.GunAngle -= 1
                
        if key[K_DOWN]:
 
            self.angle += 1
            Tank.GunAngle += 1

        if Tank.GunAngle < -90:
                self.angle += 1
                Tank.GunAngle += 1
             
        if Tank.GunAngle > 0:
            self.angle -= 1
            Tank.GunAngle -= 1
            
            
        self.rect.left = Tank.GunX
        self.rect.bottom = Tank.GunY

class Explosion(pygame.sprite.Sprite):
    """ Explosion animation. """
    #sound = games.load_sound("explosion.wav")
    pygame.mixer.music.load('pickup.wav')
    expSound = pygame.mixer.Sound('pickup.wav')

    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super().__init__()
        self.is_collideable = True
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load("explosion2.bmp")
        self.images = []
        self.images.append(pygame.image.load('explosion1.bmp'))
        self.images.append(pygame.image.load('explosion2.bmp'))
        self.images.append(pygame.image.load('explosion3.bmp'))
        self.images.append(pygame.image.load('explosion4.bmp'))
        self.images.append(pygame.image.load('explosion5.bmp'))
        self.images.append(pygame.image.load('explosion6.bmp'))
        self.images.append(pygame.image.load('explosion7.bmp'))
        self.images.append(pygame.image.load('explosion8.bmp'))
        self.images.append(pygame.image.load('explosion9.bmp'))
        self.images.append(pygame.image.load('exp1.bmp'))
        self.current_image = 0

        self.image = self.images[self.current_image]
  
        self.rect = self.image.get_rect()

        self.rect.width = 1
        self.rect.x = x
        self.rect.y = y
        self.rect.center = (x,y)

##        super(Explosion, self).__init__(images = Explosion.images,
##                                        x = x, y = y,
##                                        repeat_interval = 4, repeat_interval = 4,
##                                        is_collideable = False)

    def update(self,speed):
        super().__init__()
        self.image.set_colorkey(self.image.get_at((0,0)))
        if self.is_collideable == True:
            explosion.draw(screen)
            self.current_image += 0.25
            if int(self.current_image) >= len(self.images):
                self.current_image = 0

        
    
            elif int(self.current_image) >= 9:
                    self.kill()
                    self.image.set_colorkey(self.image.get_at((0,0)))
                    self.is_collideable = False
        self.image = self.images[int(self.current_image)]

    def kill (self):

        pygame.display.flip()
        

    

class Enemy(pygame.sprite.Sprite):
    
    image = pygame.image.load("enemy.bmp")

   
    def __init__(self, speed = 1, odds_change = 200):
        pygame.sprite.Sprite.__init__(self)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect.x = 600
        self.rect.y = 344
        self.dx = speed
        
        # super(Enemy, self).__init__(image = Enemy.image,
                                   # x = 600,
                                   # y = 344,
                                   # dx = speed)
        
        self.odds_change = odds_change


    def update(self):
        """ Determine if direction needs to be reversed. """
        if self.rect.left < 400 or self.rect.right > screen.get_width():
           self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
        
        self.rect.x += self.dx


class Church(pygame.sprite.Sprite):
    image = pygame.image.load("church.bmp")
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Church.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False
    
                                 
def main():
    
    
    global GRAVITY
    GRAVITY = 1
    
    # establish background
    background_image = pygame.image.load("background.jpg")
    #game.screen.background = background_image
    
    
    
##    #load tank
    the_tank = Tank( x = 100, y = 344)
    player.add(the_tank)
## 
    the_enemy = Enemy()
    enemy.add(the_enemy)
##   Church( x = 380, y = 333)
    
    the_church = Church( x = 380, y = 333)
    playField.add(the_church)

    #game.screen.mainloop()
    loop = True
    while loop:
        clock.tick(30)
        if ammo <= 0:
            end_game()
            loop = False

        screen.fill((0,0,0))
        screen.blit(background_image,(0,0))
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
 
                loop = False
                
        ammoDisplay = font.render("Ammo: " + str(ammo),1,(0,0,0))
        scoreDisplay = font.render("Score" + str(score),1,(0,0,0))

        screen.blit(scoreDisplay,(10,10))
        screen.blit(ammoDisplay, (10,25))
        
        if end_game:
            end_message = font.render("Game Over",1,(255,0,0))
            screen.blit(end_message,(screen.get_width()/2,screen.get_height()/2))
            loop = False

        player.update()
        gun.update()
        enemy.update()

        missile.update()
        explosion.update(0.87)
        playField.update()


        player.draw(screen)
        gun.draw(screen)
        enemy.draw(screen)
        missile.draw(screen)
        playField.draw(screen)

        pygame.display.flip()

 
    if end_game:
        pygame.time.wait(2000)
# kick it off!
main()


