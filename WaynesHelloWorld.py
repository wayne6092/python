import pygame, sys
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (53, 198, 188)
PURPLE = (230, 0, 255)
YELLOW = (255, 247, 0)

# Set up fonts.
basicFont = pygame.font.SysFont(None, 48)


# Set up the text.
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw the white background onto the surface.
windowSurface.fill(WHITE)

pygame.draw.line(windowSurface, GREEN, [570, 50], [50,50], 10)
pygame.draw.line(windowSurface, RED, [570, 60], [50,60], 10)
pygame.draw.line(windowSurface, BLUE, [570, 70], [50,70], 10)
pygame.draw.line(windowSurface, CYAN, [570, 80], [50,80], 10)
pygame.draw.line(windowSurface, BLACK, [570, 90], [50,90], 10)
pygame.draw.line(windowSurface, PURPLE, [570, 100], [50,100], 10)
pygame.draw.line(windowSurface, YELLOW, [570, 110], [50,110], 10)
pygame.draw.line(windowSurface, GREEN, [570, 120], [50,120], 10)
pygame.draw.line(windowSurface, RED, [570, 130], [50,130], 10)
pygame.draw.line(windowSurface, BLUE, [570, 140], [50,140], 10)
pygame.draw.line(windowSurface, CYAN, [570, 150], [50,150], 10)
pygame.draw.line(windowSurface, BLACK, [570, 160], [50,160], 10)
pygame.draw.line(windowSurface, PURPLE, [570, 170], [50,170], 10)
pygame.draw.line(windowSurface, YELLOW, [570, 180], [50,180], 10)

pygame.draw.line(windowSurface, GREEN, [570, 190], [50,190], 10)
pygame.draw.line(windowSurface, RED, [570, 200], [50,200], 10)
pygame.draw.line(windowSurface, BLUE, [570, 210], [50,210], 10)
pygame.draw.line(windowSurface, CYAN, [570, 220], [50,220], 10)
pygame.draw.line(windowSurface, BLACK, [570, 230], [50,230], 10)
pygame.draw.line(windowSurface, PURPLE, [570, 240], [50,240], 10)
pygame.draw.line(windowSurface, YELLOW, [570, 250], [50,250], 10)
pygame.draw.line(windowSurface, GREEN, [570, 260], [50,260], 10)
pygame.draw.line(windowSurface, RED, [570, 270], [50,270], 10)
pygame.draw.line(windowSurface, BLUE, [570, 280], [50,280], 10)
pygame.draw.line(windowSurface, CYAN, [570, 290], [50,290], 10)
pygame.draw.line(windowSurface, BLACK, [570, 300], [50,300], 10)
pygame.draw.line(windowSurface, PURPLE, [570, 310], [50,310], 10)
pygame.draw.line(windowSurface, YELLOW, [570, 320], [50,320], 10)


# Draw a green polygon onto the surface.
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw some blue lines onto the surface.
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue circle onto the surface.
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Draw a red ellipse onto the surface.
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw the text's background rectangle onto the surface.
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Draw a new shape, arc lines, triangles, and aalines.
pygame.draw.arc(windowSurface, CYAN, (10, 225, 275, 200), 3.14159/2, 10, 11)
pygame.draw.arc(windowSurface, CYAN, (50, 255, 50, 255), 3.14159/2, 20.3, 17)

pygame.draw.aaline(windowSurface, CYAN, [0, 25],[22, 56], True)
pygame.draw.lines(windowSurface, BLACK, False, [[0, 44], [40, 60], [150, 70], [120, 60]], 9)
pygame.draw.lines(windowSurface, BLACK, False, [[0, 80], [20, 40], [220, 50], [220, 30]], 5)


##pygame.draw.line(windowSurface, GREEN, [570, 50], [50,50], 10)
##pygame.draw.line(windowSurface, RED, [570, 60], [50,60], 10)
##pygame.draw.line(windowSurface, BLUE, [570, 70], [50,70], 10)
##pygame.draw.line(windowSurface, CYAN, [570, 80], [50,80], 10)
##pygame.draw.line(windowSurface, BLACK, [570, 90], [50,90], 10)
##pygame.draw.line(windowSurface, PURPLE, [570, 100], [50,100], 10)
##pygame.draw.line(windowSurface, YELLOW, [570, 110], [50,110], 10)
##pygame.draw.line(windowSurface, GREEN, [570, 120], [50,120], 10)
##pygame.draw.line(windowSurface, RED, [570, 130], [50,130], 10)
##pygame.draw.line(windowSurface, BLUE, [570, 140], [50,140], 10)
##pygame.draw.line(windowSurface, CYAN, [570, 150], [50,150], 10)
##pygame.draw.line(windowSurface, BLACK, [570, 160], [50,160], 10)
##pygame.draw.line(windowSurface, PURPLE, [570, 170], [50,170], 10)
##pygame.draw.line(windowSurface, YELLOW, [570, 180], [50,180], 10)
##
##pygame.draw.line(windowSurface, GREEN, [570, 190], [50,190], 10)
##pygame.draw.line(windowSurface, RED, [570, 200], [50,200], 10)
##pygame.draw.line(windowSurface, BLUE, [570, 210], [50,210], 10)
##pygame.draw.line(windowSurface, CYAN, [570, 220], [50,220], 10)
##pygame.draw.line(windowSurface, BLACK, [570, 230], [50,230], 10)
##pygame.draw.line(windowSurface, PURPLE, [570, 240], [50,240], 10)
##pygame.draw.line(windowSurface, YELLOW, [570, 250], [50,250], 10)
##pygame.draw.line(windowSurface, GREEN, [570, 260], [50,260], 10)
##pygame.draw.line(windowSurface, RED, [570, 270], [50,270], 10)
##pygame.draw.line(windowSurface, BLUE, [570, 280], [50,280], 10)
##pygame.draw.line(windowSurface, CYAN, [570, 290], [50,290], 10)
##pygame.draw.line(windowSurface, BLACK, [570, 300], [50,300], 10)
##pygame.draw.line(windowSurface, PURPLE, [570, 310], [50,310], 10)
##pygame.draw.line(windowSurface, YELLOW, [570, 320], [50,320], 10)




#This is triangle
pygame.draw.polygon(windowSurface, BLACK, [[190, 80], [4, 100], [100, 200]], 15)


# Get a pixel array of the surface.
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# Draw the text onto the surface.
windowSurface.blit(text, textRect)

# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
