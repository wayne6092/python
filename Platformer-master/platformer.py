import pygame
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
aqua =( 0, 255, 255)
navy_blue= ( 0, 0, 128)
yellow =(255, 255, 0)
lightblue=(157,255,255)
dw=1024
dh=640
tilesize=128
platformimg=[pygame.image.load('platform'+str(i)+'.png') for i in range(1,10)]
lenemyimg=[pygame.image.load('L'+str(i)+'E.png') for i in range(1,12)]
renemyimg=[pygame.image.load('R'+str(i)+'E.png') for i in range(1,12)]
rightwalkimg=[pygame.image.load('R'+str(i)+'.png') for i in range(1,10)]
leftwalkimg=[pygame.image.load('L'+str(i)+'.png') for i in range(1,10)]
waterimg=[pygame.image.load('w'+str(i)+'.png') for i in range(1,18)]
laserimg=pygame.image.load('laser.png')
enemylaserimg=pygame.image.load('elaser.png')
screen=pygame.display.set_mode([dw,dh])
pygame.display.set_caption("Platformer template")
clock=pygame.time.Clock()
class Map:
   def __init__(self,filename):
      self.data=[]
      with open(filename,'r+') as f:
         for line in f:
            self.data.append(line.strip())
      self.tilewidth=len(self.data[0])
      self.tileheight=len(self.data)
      self.width=self.tilewidth*tilesize
      self.height=self.tileheight*tilesize
class Camera:
   def __init__(self,width,height):
      self.camera=pygame.Rect(0,0,width,height)
      self.width=width
      self.height=height
   def apply(self,entity):
      return entity.rect.move(self.camera.topleft)
   def update(self,target):
      x=-target.rect.x+int(dw/2)
      x=min(0,x)
      x=max(-(self.width-dw),x)
      self.camera=pygame.Rect(x,0,self.width,self.height)
class Player(pygame.sprite.Sprite):
   def __init__(self,x,y,game):
      super().__init__()
      self.game=game
      self.image=rightwalkimg[0]
      self.rect=self.image.get_rect()
      self.rect.x=x*tilesize
      self.rect.y=y*tilesize
      self.x=x
      self.y=y
      self.leftbullet=0
      self.rightbullet=1
      self.vx=0
      self.vy=0
      self.lc=0
      self.rc=0
      self.jc=0
      self.bc=0
      self.health=100
      self.lastshoot=pygame.time.get_ticks()
   def gravity(self):
      if self.vy==0:
         self.vy=5
      else:
         self.vy+=0.35
   def shoot(self):
      if self.rightbullet:
         self.bullet=Bullet(self,self.rect.right,self.rect.top+30,10)
         self.game.bullets.add(self.bullet)
         self.game.all_sprites.add(self.bullet)
      if self.leftbullet:
         self.image=leftwalkimg[0]
         self.bullet=Bullet(self,self.rect.left,self.rect.top+30,-10)
         self.game.bullets.add(self.bullet)
         self.game.all_sprites.add(self.bullet)
   def jump(self):
      self.rect.y+=2
      hits=pygame.sprite.spritecollide(self,self.game.platforms,False)
      self.rect.y-=2
      if len(hits) or self.rect.bottom>=dh:
         self.vy=-10
   def update(self):
      self.gravity()
      now=pygame.time.get_ticks()
      self.vx=0      
      keys=pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
         self.vx=-5
         self.leftbullet=1
         self.rightbullet=0
         if self.lc+1<27:
            self.image=leftwalkimg[self.lc//3]
            self.lc+=1
         else:
            self.lc=0
      elif keys[pygame.K_RIGHT]:
         self.vx=5
         self.leftbullet=0
         self.rightbullet=1
         if self.rc+1<27:
            self.image=rightwalkimg[self.rc//3]
            self.rc+=1
         else:
            self.rc=0
      else:
         if self.rightbullet:
            self.image=rightwalkimg[0]
         if self.leftbullet:
            self.image=leftwalkimg[0]
      if keys[pygame.K_UP]:
         self.jump()
      if keys[pygame.K_SPACE]:       
         if now-self.lastshoot>500:
            self.lastshoot=now
            self.shoot()
      self.rect.x+=self.vx
      hits1=pygame.sprite.spritecollide(self,self.game.platforms,False)
      for hit in hits1:
         if self.vx>0:
            self.rect.right=hit.rect.left
         elif self.vx<0:
            self.rect.left=hit.rect.right
         self.vx=0
      self.rect.y+=self.vy
      hits2=pygame.sprite.spritecollide(self,self.game.platforms,False)
      for hit in hits2:
         if self.vy>0:
            self.rect.bottom=hit.rect.top
         elif self.vy<0:
            self.rect.top=hit.rect.bottom
         self.vy=0
      if self.rect.bottom>=dh:
          self.rect.bottom=dh
      if self.rect.left<=0:
          self.rect.left=0
      if self.rect.top<=0:
          self.rect.top=0
      if self.rect.right>=self.game.map.width:
         self.rect.right=self.game.map.width
class EBullet(pygame.sprite.Sprite):
   def __init__(self,enemy,x,y,vx):
      super().__init__()
      self.enemy=enemy
      self.image=enemylaserimg
      self.image=pygame.transform.rotate(self.image,90)
      self.rect=self.image.get_rect()
      self.rect.x=x
      self.rect.y=y
      self.vx=vx
      self.last=pygame.time.get_ticks()
   def update(self):
      now=pygame.time.get_ticks()
      if now-self.last>300:
         self.last=now
         self.kill()
      self.rect.x+=self.vx
      hits=pygame.sprite.spritecollide(self,self.enemy.game.platforms,0)
      if  hits:
         self.kill()
class Bullet(pygame.sprite.Sprite):
   def __init__(self,player,x,y,vx):
      super().__init__()
      self.player=player
      self.image=laserimg
      self.image=pygame.transform.rotate(self.image,90)
      self.rect=self.image.get_rect()
      self.rect.x=x
      self.rect.y=y
      self.vx=vx
      self.last=pygame.time.get_ticks()
   def update(self):
      now=pygame.time.get_ticks()
      self.rect.x+=self.vx
      hits=pygame.sprite.spritecollide(self,self.player.game.platforms,0)
      if now-self.last>300 or hits:
         self.kill()
class Platform(pygame.sprite.Sprite):
   def __init__(self,x,y,i):
      super().__init__()
      self.image=platformimg[i]
      self.rect=self.image.get_rect()
      self.rect.x=x*tilesize
      self.rect.y=y*tilesize
class MovingPlatform(pygame.sprite.Sprite):
   def __init__(self,x,y):
      super().__init__()
      self.image=platformimg[8]
      self.rect=self.image.get_rect()
      self.rect.x=x*tilesize
      self.rect.y=y*tilesize
      self.temp=x*tilesize
      self.leftlimit=(x-1)*tilesize
      self.rightlimit=(x+1)*tilesize
      self.vx=2
   def update(self):
      if self.rect.x==self.leftlimit:
         self.vx=2
      elif self.rect.x==self.rightlimit:
         self.vx*=-1
      self.rect.x+=self.vx

class Water(pygame.sprite.Sprite):
   def __init__(self,x,y):
      super().__init__()
      self.image=waterimg[0]
      self.rect=self.image.get_rect()
      self.rect.x=x*tilesize
      self.rect.y=y*tilesize
      self.wc=0
   def update(self):
      if self.wc+1<34:
         self.image=waterimg[self.wc//2]
         self.wc+=1
      else:
         self.wc=0
class Enemy(pygame.sprite.Sprite):
   def __init__(self,x,y,game):
      super().__init__()
      self.game=game
      self.image=renemyimg[0].copy()
      self.rect=self.image.get_rect()
      self.rect.x=x*tilesize
      self.rect.y=y*tilesize
      self.lc=0
      self.rc=0
      self.leftlimit=(x-1)*tilesize
      self.rightlimit=(x+1)*tilesize
      self.vx=2
      self.vy=0
      self.health=60
      self.last=pygame.time.get_ticks()
   def shoot(self):
      now=pygame.time.get_ticks()
      if now-self.last>1000:
         self.last=now
         if self.vx>0:
            self.image=renemyimg[0].copy()
            self.ebullet=EBullet(self,self.rect.right,self.rect.top+30,10)
            self.game.ebullets.add(self.ebullet)
            self.game.all_sprites.add(self.ebullet)
         if self.vx<0:
            self.image=lenemyimg[0].copy()
            self.ebullet=EBullet(self,self.rect.left,self.rect.top+30,-10)
            self.game.ebullets.add(self.ebullet)
            self.game.all_sprites.add(self.ebullet)
         
   def gravity(self):
      if self.vy==0:
         self.vy=5
      else:
         self.vy+=0.35
   def draw_health(self):
      if self.health>40:
         col=green
      elif self.health>20:
         col=yellow
      else:
         col=red
      if self.health<60:
         pygame.draw.rect(self.image,col,(0,0,self.health,7))
      if self.health>0 and self.health<60:
         pygame.draw.rect(self.image,white,(0,0,60,7),3)
   def update(self):
      self.gravity()
      self.rect.x+=self.vx
      if int(self.rect.x)==int(self.rightlimit):
         self.vx*=-1         
      if int(self.rect.x)==int(self.leftlimit):
         self.vx=2
      if self.vx<0:
         if self.lc+1<30:
            self.image=lenemyimg[self.lc//3].copy()
            self.lc+=1
         else:
            self.lc=0
      if self.vx>0:
         if self.rc+1<30:
            self.image=renemyimg[self.rc//3].copy()
            self.rc+=1
         else:
            self.rc=0
      self.rect.y+=self.vy
      hits2=pygame.sprite.spritecollide(self,self.game.platforms,False)
      for hit in hits2:
         if self.vy>0:
            self.rect.bottom=hit.rect.top+6
         elif self.vy<0:
            self.rect.top=hit.rect.bottom
         self.vy=0
      self.shoot()
      if self.health<=0:
         self.kill()
         self.health=60
class Game:
   def __init__(self):
      self.health=100
   def drawgrid(self):
      for i in range(0,dw,tilesize):
         pygame.draw.line(screen,white,(i,0),(i,dh))
      for j in range(0,dh,tilesize):
         pygame.draw.line(screen,white,(0,j),(dw,j))
   def new(self):
      self.map=Map('map2.txt')
      self.player=Player(2,4,self)
      self.all_sprites=pygame.sprite.Group()
      self.all_sprites.add(self.player)
      self.platforms=pygame.sprite.Group()
      self.enemies=pygame.sprite.Group()
      self.bullets=pygame.sprite.Group()
      self.ebullets=pygame.sprite.Group()
      self.waters=pygame.sprite.Group()
      for row,tiles in enumerate(self.map.data):
         for col,tile in enumerate(tiles):
            if tile=='e':
               self.enemy=Enemy(col,row,self)
               self.enemies.add(self.enemy)
               self.all_sprites.add(self.enemy)
            if tile=='1':
               self.platform=Platform(col,row,0)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='2':
               self.platform=Platform(col,row,1)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='3':
               self.platform=Platform(col,row,2)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='4':
               self.platform=Platform(col,row,3)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='5':
               self.platform=Platform(col,row,4)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='6':
               self.platform=Platform(col,row,5)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='7':
               self.platform=Platform(col,row,6)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='8':
               self.platform=Platform(col,row,7)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='9':
               self.platform=Platform(col,row,8)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='m':
               self.platform=MovingPlatform(col,row)
               self.platforms.add(self.platform)
               self.all_sprites.add(self.platform)
            if tile=='w':
               self.water=Water(col,row)#If there is a w then we add water to the group, instantiate camera, puts water in col + row
               self.waters.add(self.water)
               self.all_sprites.add(self.water)
      self.camera=Camera(self.map.width,self.map.height)
   def message(self,text,x,y,size,color):
       self.font=pygame.font.SysFont('arial',size,1)
       self.msg=self.font.render(text,1,color)
       self.msgrect=self.msg.get_rect()
       self.msgrect.x=x
       self.msgrect.y=y
       screen.blit(self.msg,(self.msgrect.x,self.msgrect.y))
   def events(self):
      for event in pygame.event.get():
         if event.type==pygame.QUIT:
            pygame.quit()
            quit()
   def update(self):
      self.all_sprites.update()
      self.camera.update(self.player)
      hits1 = pygame.sprite.spritecollide(self.player,self.ebullets,1)
      if hits1:
         self.health-=10
      if self.health<=0:
         self.player.kill()
      hits2 = pygame.sprite.groupcollide(self.enemies,self.bullets,False,True)
      for hit in hits2:
         hit.health-=10
   def playerhealthbar(self):
      if self.health>60:
         col=green
      elif self.health>30:
         col=yellow
      else:
         col=red
      if self.health>0:
         self.message('Player HP',20,5,20,red)
         pygame.draw.rect(screen,col,(20,30,self.health,30))
         pygame.draw.rect(screen,white,(20,30,100,30),3)      
   def draw(self):
      screen.fill(lightblue)
      for sprite in self.all_sprites:
         if isinstance(sprite,Enemy):
            sprite.draw_health()
         screen.blit(sprite.image,self.camera.apply(sprite))      
      self.playerhealthbar()
   def run(self):
      while 1:
         clock.tick(60)
         self.events()#CHECK EVENT QUEUE
         self.update()#CHECK FOR UPDATE
         self.draw()
         pygame.display.flip()
g=Game()
while g.run:
   g.new()
   g.run()
