import pygame, sys, random
from pygame.locals import *

# Set up pygame.

pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')
pygame.mouse.set_visible(False)
# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the player and food data structure.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()

player2Image = pygame.image.load('player.png')
player2Rect = player2Image.get_rect()
# Set up movement variables.


MOVESPEED = 6
##def waitForPlayerToPressKey():
##    while True:
##        for event in pygame.event.get():
##            if event.type == QUIT:
##                terminate()
##            if event.type == KEYDOWN:
##                if event.key == K_ESCAPE: # Pressing ESC quits.
##                    terminate()
##                return
##waitForPlayerToPressKey()            
##def playerHasHitBaddie(playerRect, food):
##    for food in foods:
##        if playerRect.colliderect(food['rect']):
##            return True
##    return False





foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
#creates a list of 20 green squares

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_UP:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or K_a:
                moveLeft = False
            if event.key == K_RIGHT or K_d:
                moveRight = False
            if event.key == K_UP or K_w:
                moveUp = False
            if event.key == K_DOWN or K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
                
##        if event.type == KEYUP:
##            if event.key == K_w:
##                player2Rect.y = MOVESPEED
##            if event.key == K_s:
##                player2Rect.y *= MOVESPEED
##            if event.key == K_d:
##                player2Rect.x *= MOVESPEED
##            if event.key == K_a:
##                player2Rect.x *= MOVESPEED

        if event.type == KEYDOWN:
            if event.key == K_w:
                player2Rect.y = True
            if event.key == K_s:
                player2Rect.y = True
            if event.key == K_d:
                player2Rect.x = True
            if event.key == K_a:
                player2Rect.x = True
        if event.type == MOUSEMOTION:
            # If the mouse moves, move the player where to the cursor.
            playerRect.centerx = event.pos[0]
            playerRect.centery = event.pos[1]
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)
    
##    
##    if player2Rect.y < WINDOWHEIGHT:
##        player2Rect.y += MOVESPEED
##    if player2Rect.y > 0:
##        player2Rect.y -= MOVESPEED
##    if player2Rect.x > 0:
##        player2Rect.x -= MOVESPEED
##    if player2Rect.x < WINDOWWIDTH:
##        player2Rect.x += MOVESPEED

        
    # Move the player.
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, BLACK, player)
    windowSurface.blit(playerImage, playerRect)
    windowSurface.blit(player2Image, player2Rect)
    # Check if the player has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
        elif playerRect.colliderect(food):
            foods.remove(food)
        elif player2Rect.colliderect(food):
            foods.remove(food)
            
    # Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40 )
