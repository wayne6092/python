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

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Set up the player and food data structure.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player1 = pygame.Rect(300, 100, 50, 50)
player2 = pygame.Rect(100, 300, 50, 50)
players = [player1, player2]
foods = []
#creates a list of 20 green squares
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 5


# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #if event.type == KEYDOWN:






            
            # Change the keyboard variables. Keys to move the box object.
##            if event.key == K_LEFT or event.key == K_a:
##                moveRight = False
##                moveLeft = True
##            if event.key == K_RIGHT or event.key == K_d:
##                moveLeft = False
##                moveRight = True
##            if event.key == K_UP or event.key == K_w:
##                moveDown = False
##                moveUp = True
##            if event.key == K_DOWN or event.key == K_s:
##                moveUp = False
##                moveDown = True

        for player in players:
            if event.type == KEYDOWN:
                if player1:
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
                  
                    if moveDown and player1.bottom < WINDOWHEIGHT:
                        player1.top += MOVESPEED
                    if moveUp and player1.top > 0:
                        player1.top -= MOVESPEED
                    if moveLeft and player1.left > 0:
                        player1.left -= MOVESPEED
                    if moveRight and player1.right < WINDOWWIDTH:
                        player1.right += MOVESPEED
                        
                    if moveDown and player1.bottom < WINDOWHEIGHT:
                        player1.top += MOVESPEED
                    if moveUp and player1.top > 0:
                        player1.top -= MOVESPEED
                    if moveLeft and player1.left > 0:
                        player1.left -= MOVESPEED
                    if moveRight and player1.right < WINDOWWIDTH:
                        player1.right += MOVESPEED
                    if event.type == KEYUP:#lifting finger off key
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                            
                            if event.key == K_LEFT:
                                moveLeft = False
                            if event.key == K_RIGHT:
                                moveRight = False
                            if event.key == K_UP:
                                moveUp = False
                            if event.key == K_DOWN:
                                moveDown = False


                    
                if player2:
                    if event.key == K_a:
                        moveRight = False
                        moveLeft = True
                    if event.key == K_d:
                        moveLeft = False
                        moveRight = True
                    if event.key == K_w:
                        moveDown = False
                        moveUp = True
                    if event.key == K_s:
                        moveUp = False
                        moveDown = True
            
                    if moveDown and player2.bottom < WINDOWHEIGHT:
                        player2.top += MOVESPEED
                    if moveUp and player2.top > 0:
                        player2.top -= MOVESPEED
                    if moveLeft and player2.left > 0:
                        player2.left -= MOVESPEED
                    if moveRight and player2.right < WINDOWWIDTH:
                        player2.right += MOVESPEED

#check event key up or down
        for player2 in players:
            if event.type == KEYUP:#lifting finger off key
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    if player2:
                        if event.key == K_a:
                            moveLeft = False
                        if event.key == K_d:
                            moveRight = False
                        if event.key == K_w:
                            moveUp = False
                        if event.key == K_s:
                            moveDown = False
                        if event.key == K_x:
                            self.top = random.randint(0, WINDOWHEIGHT - self.height)
                            self.left = random.randint(0, WINDOWWIDTH - self.width)
                    
                        if moveDown and player2.bottom < WINDOWHEIGHT:
                            player2.top -= MOVESPEED
                        if moveUp and player2.top > 0:
                            player2.top += MOVESPEED
                        if moveLeft and player2.left > 0:
                            player2.left += MOVESPEED
                        if moveRight and player2.right < WINDOWWIDTH:
                            player2.right -= MOVESPEED

                        if event.key == K_a:
                            moveRight = False
                            moveLeft = True
                        if event.key == K_d:
                            moveLeft = False
                            moveRight = True
                        if event.key == K_w:
                            moveDown = False
                            moveUp = True
                        if event.key == K_s:
                            moveUp = False
                            moveDown = True
                
                        if moveDown and player2.bottom < WINDOWHEIGHT:
                            player2.top += MOVESPEED
                        if moveUp and player2.top > 0:
                            player2.top -= MOVESPEED
                        if moveLeft and player2.left > 0:
                            player2.left -= MOVESPEED
                        if moveRight and player2.right < WINDOWWIDTH:
                            player2.right += MOVESPEED

            
##            if event.key == K_ESCAPE:
##                pygame.quit()
##                sys.exit()
##            if event.key == K_LEFT or event.key == K_a:
##                moveLeft = False
##            if event.key == K_RIGHT or event.key == K_d:
##                moveRight = False
##            if event.key == K_UP or event.key == K_w:
##                moveUp = False
##            if event.key == K_DOWN or event.key == K_s:
##                moveDown = False
##            if event.key == K_x:
##                player.top = random.randint(0, WINDOWHEIGHT - player.height)
##                player.left = random.randint(0, WINDOWWIDTH - player.width)
##                player2.top = random.randint(0, WINDOWHEIGHT - player.height)
##                player2.left = random.randint(0, WINDOWWIDTH - player.width)
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player.

    for player1 in players:

        if player1:
            if moveDown and player1.bottom < WINDOWHEIGHT:
                player1.top += MOVESPEED
            if moveUp and player1.top > 0:
                player1.top -= MOVESPEED
            if moveLeft and player1.left > 0:
                player1.left -= MOVESPEED
            if moveRight and player1.right < WINDOWWIDTH:
                player1.right += MOVESPEED
            if event.type == KEYUP:#lifting finger off key
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    if player1:
                        if event.key == K_LEFT:
                            moveLeft = False
                        if event.key == K_RIGHT:
                            moveRight = False
                        if event.key == K_UP:
                            moveUp = False
                        if event.key == K_DOWN:
                            moveDown = False
        if player2:    
            if moveDown and player2.bottom < WINDOWHEIGHT:
                player2.top -= MOVESPEED
            if moveUp and player2.top > 0:
                player2.top += MOVESPEED
            if moveLeft and player2.left > 0:
                player2.left += MOVESPEED
            if moveRight and player2.right < WINDOWWIDTH:
                player2.right -= MOVESPEED
    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, BLACK, player1)
    pygame.draw.rect(windowSurface, BLACK, player2)
    # Check if the player has intersected with any food squares.
    for player in players:
        for food in foods[:]:
            if player1.colliderect(food):
                foods.remove(food)
            if player2.colliderect(food):
                foods.remove(food)
    # Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(10 )
