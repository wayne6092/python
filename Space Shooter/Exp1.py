import os, sys, pygame, random, time
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stonks")
#icon = pygame.image.load("money")
#icon = pygame.display.set_icon(icon)
#screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

music = pygame.mixer.music.load ("data/music/blassic.ogg") #lost.ogg
pygame.mixer.music.play(-1)

#Load Images
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
#   try:
    image = pygame.image.load(fullname)
##    except pygame.error(
##        print 'Cannot load image:', fullname
##        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()



#Load Sounds
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
##    try:
    sound = pygame.mixer.Sound(fullname)
##    except pygame.error, message:
##        print 'Cannot load sound:', fullname
##        raise SystemExit, message
    return sound


class Arena(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("menu/background.png", -1)
        self.dy = 5
        self.reset()
        
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1200:
            self.reset() 
    
    def reset(self):
        self.rect.top = -600


############################################################################
def game():#Menu
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))
    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True
    counter = 0
  
    #Main Loop
    while keepGoing:
       clock.tick(30)
       #input
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
################################################################################
#Class Module
class StockMenu:

#Define the initalize self options
    def __init__(self, *options):

        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [0, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

#Draw the menu
    def draw(self, surface):
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x, self.y + i*self.font.get_height()))
            i+=1

#Menu Input            
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

#Position Menu
    def set_pos(self, x, y):
        self.x = x
        self.y = y

#Font Style        
    def set_font(self, font):
        self.font = font

#Highlight Color        
    def set_highlight_color(self, color):
        self.hcolor = color

#Font Color        
    def set_normal_color(self, color):
        self.color = color

#Font position        
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)
        
        

def missionMenu():
    
    #Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))
    

    #Title for Option Menu
    menuTitle = StockMenu(
        ["Trade Stocks!"])

    #Option Menu Text
    instructions = StockMenu(
        [""], 
        ["Solve a riddle or two!"],
        [""],
        ["This game is mouse control only."],
        [""],
        ["Navigate the menu with the arrow keys obviously"],
        [""],
        ["Anyways, trading in the stock market isn't easy, it takes guts."],
        [""],
        ["It takes determination, willpower, and most importantly a good attitude."],
        [""],
        ["Have fun, try to get the highest price that you can!"],
        [""],
        [""],
        ["                   PRESS ESC TO RETURN                    "])

    #Title 
    menuTitle.center_at(150, 150)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))
        

    #Title Center
    instructions.center_at(440, 350)

    #Menu Font
    instructions.set_font(pygame.font.Font("data/fonts/arial.ttf", 22))

    #Highlight Color
    instructions.set_normal_color((0, 255, 0))


    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
           #Draw
           screen.blit(background, (0,0))    
           arena.update()
           arena.draw(screen)
           menuTitle.draw(screen)
           instructions.draw(screen)
           pygame.display.flip()




def aboutMenu():
 
    #Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))
    
    #About Menu Text
    #Title for Option Menu
    menuTitle = StockMenu(
        ["About menu!"])

    info = StockMenu(
        [""], 
        ["World of Stocks Beta"],
        [""],
        ["Devloped by the programmer."],
        [""],
        ["Student from Mr. Schleiss' class ITCS 1950"],
        [""],
        [""],
        ["      PRESS ESC TO RETURN            "])
        #Citation: I used some classes from SpaceShooter, a classic game among the best
        #I believe my teacher allowed me permission to use this code for my assignments.

    #About Title Font color, alignment, and font type
    menuTitle.center_at(150, 150)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 48))
    menuTitle.set_highlight_color((0, 255, 0))

    #About Menu Text Alignment
    info.center_at(400, 310)

    #About Menu Font
    info.set_font(pygame.font.Font("data/fonts/arial.ttf", 28))

    #About Menu Font Color
    info.set_normal_color((0, 255, 0))


    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
           #Draw
           screen.blit(background, (0,0))    
           arena.update()
           arena.draw(screen)
           menuTitle.draw(screen)
           info.draw(screen)
           pygame.display.flip()

#Functions

def option1():
    game()
def option2():
    missionMenu()
def option3():
    aboutMenu()   
def option4():
    pygame.quit()
    sys.exit()
    
        

#Main
def main():

    
    #Arena
    arena = Arena()
    arena = pygame.sprite.RenderPlain((arena))

   
    #Defines menu, option functions, and option display. For example,
    #Changing "Start" to "Begin" will display Begin, instead of start. 
    menuTitle = StockMenu(
        ["World of Stocks"])
        
    menu = StockMenu(
        ["Start", option1],
        ["My Game", option2],
        ["About", option3],
        ["Quit", option4])
        
        

    #Title
    menuTitle.center_at(200, 200)
    menuTitle.set_font(pygame.font.Font("data/fonts/arial.ttf", 48))
    menuTitle.set_highlight_color((155, 177, 185))
    
    #Menu settings
    menu.center_at(200, 320)
    menu.set_font(pygame.font.Font("data/fonts/arial.ttf", 32))
    menu.set_highlight_color((100, 255, 200))
    menu.set_normal_color((200, 200, 0))
    
    clock = pygame.time.Clock()
    keepGoing = True


    while 1:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Update Menu
        menu.update(events)

        #Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return

        #Draw
        screen.blit(background, (0,0))
        arena.update()
        arena.draw(screen)
        menu.draw(screen)
        menuTitle.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
   main()

