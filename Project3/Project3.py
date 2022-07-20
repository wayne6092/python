import pygame, random #I imported random module

pygame.init()
# Setting up the window 
screenWidth = 700
screenHeight = 498
screen = pygame.display.set_mode((screenWidth, screenHeight))
monster_group = pygame.sprite.Group()
character_group = pygame.sprite.Group()

class PlayerImage(pygame.sprite.Sprite):
    health = 100
    def __init__(self, xCenter, yCenter):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png")
        self.health = 100
        self.healthFont = pygame.font.Font("font/arial.ttf", 24)
        self.rect = self.image.get_rect()
        self.rect.center = [xCenter, yCenter]
        
    def health(self):
        self.health = 100
        print("Hello")

    def update(self):#Added update methods to player and enemy classes
        x = random.randint(1, 5)
        healthBlit = self.healthFont.render("Player HP: " + str(self.health), 1, (0, 200, 0))
        screen.blit(healthBlit, (440, 340))
        key = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.health -= 10

class EnemyImage(pygame.sprite.Sprite):
    
    def __init__(self, xCenter, yCenter):
        pygame.sprite.Sprite.__init__(self)
        self.healthFont = pygame.font.Font("font/arial.ttf", 24)
        self.image = pygame.image.load("images/enemy.png")
        self.health = 100
        self.rect = self.image.get_rect()
        self.rect.center = [xCenter, yCenter]
            
    def health(self):
        self.health = 100
        print("Hello")
        
    def update(self):
        y = random.randint(5, 35)
        healthBlit = self.healthFont.render("Enemy HP: " + str(self.health), 1, (0, 200, 0))
        screen.blit(healthBlit, (210, 350))
        key = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.health -= 15
##class PlayerHealth(pygame.sprite.Sprite):
##    def __init__(self, xCenter, yCenter):
##        pygame.sprite.Sprite.__init__(self)
##        #font = pygame.font.Fon

def main():
    # creates an instance of pygame
    pygame.init()
    # Setting up the window 
    screenWidth = 700
    screenHeight = 498
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    # Caption
    pygame.display.set_caption("Project 3")
    # Main Background 
    initialBackground = pygame.image.load("images/DBackground.jfif")
    # Setting up the music
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/theme.mp3")
    pygame.mixer.music.play(-1, 0.0)

    # creating a local instance of the class Player Image
    character = PlayerImage(450,300)
    # PlayerImage Sprite Group
    #character_group = pygame.sprite.Group()
    character_group.add(character)

    # creating a local instance of the class Enemy Image
    monster = EnemyImage(250,320)
    # monster sprite group
    #monster_group = pygame.sprite.Group()
    monster_group.add(monster)
    
    # Run the game loop
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return main()
            # Doing some testing with key presses
##            if event.type == pygame.KEYDOWN:
##                if event.key == pygame.K_a:
                    #print("Hello")
##                elif event.key == pygame.K_d:
##                    print("Goodbye")
                
        # Draw the window onto the screen
        screen.blit(initialBackground,(0,0))
 
        character_group.draw(screen)
        character_group.update()
        monster_group.draw(screen)
        monster_group.update()
        pygame.display.flip()
main()
