#FUNCTION: This program makes an AT Robot go to the cursor click location
# with smooth movement.
#ADAPTED BY: Kevin Malone
#SOURCE(S): Sir Isaac Otto
#           Pygame get mouse position code example. pygame get mouse position Code Example. (n.d.). 
#               Retrieved October 5, 2022, from https://www.codegrepper.com/code-examples/python/pygame+get+mouse+position

import pygame, math
from pygame.locals import *
vec = pygame.math.Vector2

pygame.init()   #Start a pygame.

# Setup the CLOCK---------------------------------------------------------------------- # 
clock = pygame.time.Clock()

# Setup the DISPLAY SCREEN ------------------------------------------------------------ #
xUnits = 1280   #X dimension of the screen.
yUnits = 720    #Y dimension of the screen.
screen = pygame.display.set_mode([xUnits, yUnits], 0, 32)  #Assign the dimension of screen.

# Setup the SPRITE SETTINGS ----------------------------------------------------------- # 
speedTank = 0       #Set sprite speed to 0.
angleTank = 0       #Set sprite angle to 0.
speedBull = 0       #Set sprite speed to 0.
angleBull = 0       #Set sprite angle to 0.
x21 = 0
y21 = 0
x1, y1 = xUnits/2, yUnits/2
endPos = x1, y1         #Set the random coordinates to endPos.
currLoc = endPos        #Set endPos to currLoc.
startPos = endPos       #Set endPos to currLoc.

# Load in the SPRITE ------------------------------------------------------------------ # 
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("OrangeSprite.png")      #Load the sprite image.
        self.ogim = self.image                                  #Load the sprite image into self.ogim.
        self.position = vec(x1, y1)                             #Place the sprite at x1, y1.
        self.rect = self.image.get_rect(center=self.position)   #Center the sprite at x1, y1.

    # Move the SPRITE------------------------------------------------------------------ # 
    def update(self):
        global speedTank, currLoc, startPos
        self.dir = angleTank    #Set the angle of the vector to self.dir.
        self.vel = vec( math.cos(math.radians(self.dir))*speedTank, #Calculate the vectors to.
                        math.sin(math.radians(self.dir))*speedTank) #move at a constant speed.
        self.image = pygame.transform.rotate(self.ogim, -angleTank-90)  #Rotate the sprite to the direction of the mouse click location.
        self.rect = self.image.get_rect(center=self.rect.center)    #Rotate the sprite about its center. 
        self.position += self.vel           #Set the velocity added to the position of the Sprite to self.position.
        self.rect.center = self.position    #Center the sprite at its current location.
        currLoc = self.position             #Set self.position to currLoc.
        tempX1, tempY1 = currLoc            #Set the coordinates of currLoc to tempX1 and tempY1.
        tempX2, tempY2 = xUnits, yUnits
        if (tempX2 - 3 < tempX1 < tempX2 + 3) or (tempY2 - 3 < tempY1 < tempY2 + 3) or (tempX1 < 0) or (tempY1 < 0): #If the sprite is at the end of the vector...
            speedTank = 0   #STOP THE SPRITE!!!

# Load in the SPRITE ------------------------------------------------------------------ # 
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bulletScale.png")       #Load the sprite image.
        self.ogim = self.image                                  #Load the sprite image into self.ogim.
        self.position = vec(x1, y1)                             #Place the sprite at x1, y1.
        self.rect = self.image.get_rect(center=self.position)   #Center the sprite at x1, y1.

    # Move the SPRITE------------------------------------------------------------------ # 
    def update(self):
        global speedBull, currLoc, startPos
        self.dir = angleBull    #Set the angle of the vector to self.dir.
        self.vel = vec( math.cos(math.radians(self.dir))*speedBull, #Calculate the vectors to.
                        math.sin(math.radians(self.dir))*speedBull) #move at a constant speed.
        self.image = pygame.transform.rotate(self.ogim, 180-angleBull)  #Rotate the sprite to the direction of the mouse click location.
        self.rect = self.image.get_rect(center=self.rect.center)    #Rotate the sprite about its center.
        self.position += self.vel           #Set the velocity added to the position of the Sprite to self.position.
        self.rect.center = self.position    #Center the sprite at its current location.
        currLoc = self.position             #Set self.position to currLoc.
        tempX1, tempY1 = currLoc            #Set the coordinates of currLoc to tempX1 and tempY1.
        tempX2, tempY2 = xUnits, yUnits
        if (tempX2 - 3 < tempX1 < tempX2 + 3) or (tempY2 - 3 < tempY1 < tempY2 + 3) or (tempX1 < 0) or (tempY1 < 0): #If the sprite is at the end of the vector...
            speedBull = 0   #STOP THE SPRITE!!!
            self.position = startPos

all_sprites = pygame.sprite.Group()
all_sprites.add(Tank())
all_bullets = pygame.sprite.Group()
all_bullets.add(Bullet())

# Setup the GAME ---------------------------------------------------------------------- # 
loopCon = True              #Loop condition variable
while loopCon:              #Run the game until...
    # EVENT IN GAME ------------------------------------------------------------------- #
    for event in pygame.event.get():        #there is an event in the game...
        if event.type == pygame.QUIT:           #where the event is the exit button being pressed...
           loopCon = False                          #terminate the game.
        if pygame.mouse.get_pressed()[0]:       #Where there is an event where the mouse gets pressed...
            x1, y1 = currLoc                        #set the sprite's current location to x1 and y1...
            x2, y2 = pygame.mouse.get_pos()         #assign the x and y coordinates of the mouse click position to x2 and y2...
            endPos = x2, y2                         #set x2 and y2 to endPos...
            y21 = y2 - y1                           #set the difference of y2 and y1 to y21...
            x21 = x2 - x1                           #set the difference of x2 and x1 to x21...
            if (x21 > 0) and (y21 == 0):            #if x21 is positive and y21 is equal to 0...
                angleTank = 0                               #set angle to 0.
            if (x21 < 0) and (y21 == 0):            #if x21 is negative and y21 is equal to 0...
                angleTank = 180                             #set angle to 180.
            if (x21 == 0) and (y21 > 0):            #if x21 is equal to 0 and y21 is positive...
                angleTank = 90                              #set angle to 90.
            if (x21 == 0) and (y21 < 0):            #if x21 is equal to 0 and y21 is negative...
                angleTank = -90                             #set angle to -90.
            if (x21 != 0):                          #if x21 does not equal 0...
                angleTank = math.degrees(math.atan(y21/x21))    #set angle to the inverse tangent of y21 divided by x21...
                if (x21 < 0) and (y21 >= 0):                #if x21 is negative and y21 is greater than or equal to 0...
                    angleTank = 180 + angleTank                 #set angle added to 180 to angle.
                if (x21 < 0) and (y21 < 0):                 #if x21 is negative and y21 is less than 0...
                    angleTank = angleTank - 180                 #set angle subtracted by 180 to angle.
            #speedTank = 2                           #MOVE THE SPRITE!!!
        if event.type == KEYDOWN:       #If a key is pressed...
            if (event.key == K_k):              #if the key is k...
                if (x21 > 0) and (y21 == 0):        #if x21 is positive and y21 is equal to 0...
                    angleBull = 0                       #set angle to 0.
                if (x21 < 0) and (y21 == 0):        #if x21 is negative and y21 is equal to 0...
                    angleBull = 180                     #set angle to 180.
                if (x21 == 0) and (y21 > 0):        #if x21 is equal to 0 and y21 is positive...
                    angleBull = 90                      #set angle to 90.
                if (x21 == 0) and (y21 < 0):        #if x21 is equal to 0 and y21 is negative...
                    angleBull = -90                     #set angle to -90.
                if (x21 != 0):                      #if x21 does not equal 0...
                    angleBull = math.degrees(math.atan(y21/x21))    #set angle to the inverse tangent of y21 divided by x21...
                    if (x21 < 0) and (y21 >= 0):                #if x21 is negative and y21 is greater than or equal to 0...
                        angleBull = 180 + angleBull                         #set angle added to 180 to angle.
                    if (x21 < 0) and (y21 < 0):                 #if x21 is negative and y21 is less than 0...
                        angleBull = angleBull - 180                     #set angle subtracted by 180 to angle.
                speedBull = 6                       #MOVE THE SPRITE!!!
    # DISPLAY TO SCREEN -------------------------------------------------------------- #       
    all_bullets.update()        #Update the sprite's movement.
    all_sprites.update()        #Update the sprite's movement.
    screen.fill((74, 65, 42))   #Refill the screen with the background after the sprite has moved.
    all_bullets.draw(screen)    #Display to the screen.
    all_sprites.draw(screen)    #Display to the screen.
    pygame.display.update()     #Update the display.
    clock.tick(60)              #Set the frame rate to 60 FPS.