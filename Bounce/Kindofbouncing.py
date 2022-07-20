import pygame, sys, time
from pygame.locals import *



class Ball():
        def __init__(self):
                self.x, self.y = WINDOWWIDTH/2, WINDOWHEIGHT/2
                self.speed_x = 3
                self.speed_y = 3
                self.size = 8
       
        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
##                if self.y <= 0:
##                        self.speed_y += 1

                        
                if self.y >= WINDOWHEIGHT:
                        self.speed_y *= -1
                        ###############
                        
##                if self.y >= 0:
##                        self.speed_y += 1
                        
##                if self.y <= WINDOWHEIGHT:
##                        self.speed_y -= 1

 
                if self.x <= 0:
                        self.speed_x *= -1#
                        self.speed_y += 1
                     
                if self.x >= WINDOWWIDTH:
                        self.speed_x *= -1
                        self.speed_y *= -1
##                if self.x <= WINDOWWIDTH:
##                        self.speed_x *= +1

##                if self.x <= WINDOWHEIGHT:
##                        self.speed_x -= 1
                        
                if self.x <= WINDOWHEIGHT:
                        self.speed_x += 1
                        self.speed_y -= 1
                        
        def drawBall(self):
                pygame.draw.ellipse(windowSurface, (CYAN), (self.x, self.y, 8, 8))


# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

# Set up direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CYAN = (53, 198, 188)
PURPLE = (230, 0, 255)
YELLOW = (255, 247, 0)
X = 40
Y = 40
# Set up the box data structure.
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}

boxes = [b1, b2, b3]
ball = Ball()





def main():
    # Run the game loop.
    while True:
        # Check for the QUIT event.
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Draw the white background onto the surface.
        windowSurface.fill(WHITE)
        pygame.draw.ellipse(windowSurface, YELLOW, (Y, 100, X, 100), 1)
        for b in boxes:
            # Move the box data structure.
            if b['dir'] == DOWNLEFT:
                b['rect'].left -= MOVESPEED
                b['rect'].top += MOVESPEED
            if b['dir'] == DOWNRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top += MOVESPEED
            if b['dir'] == UPLEFT:
                b['rect'].left -= MOVESPEED
                b['rect'].top -= MOVESPEED
            if b['dir'] == UPRIGHT:
                b['rect'].left += MOVESPEED
                b['rect'].top -= MOVESPEED

            # Check whether the box has moved out of the window.
            if b['rect'].top < 0:
                # The box has moved past the top.
                if b['dir'] == UPLEFT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = DOWNRIGHT
            if b['rect'].bottom > WINDOWHEIGHT:
                # The box has moved past the bottom.
                if b['dir'] == DOWNLEFT:
                    b['dir'] = UPLEFT
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = UPRIGHT
            if b['rect'].left < 0:
                # The box has moved past the left side.
                if b['dir'] == DOWNLEFT:
                    b['dir'] = DOWNRIGHT
                if b['dir'] == UPLEFT:
                    b['dir'] = UPRIGHT
            if b['rect'].right > WINDOWWIDTH:
                # The box has moved past the right side.
                if b['dir'] == DOWNRIGHT:
                    b['dir'] = DOWNLEFT
                if b['dir'] == UPRIGHT:
                    b['dir'] = UPLEFT






    ##############################
            # Draw the box onto the surface.
            pygame.draw.rect(windowSurface, b['color'], b['rect'])
            ball.movement()
            ball.drawBall()
        # Draw the window onto the screen.
        pygame.display.update()
        time.sleep(0.02)
main()
