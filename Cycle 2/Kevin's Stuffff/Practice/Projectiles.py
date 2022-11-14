#FUNCTION: This program makes an AT Robot launch projectiles.
# with smooth movement.
#ADAPTED BY: Kevin Malone
#SOURCE(S): Sir Isaac Otto
#           Pygame get mouse position code example. pygame get mouse position Code Example. (n.d.). 
#               Retrieved October 5, 2022, from https://www.codegrepper.com/code-examples/python/pygame+get+mouse+position
#           YouTube. (2020, May 22). Python / pygame tutorial: Creating a basic bullet shooting mechanic. YouTube. 
#               Retrieved October 24, 2022, from https://www.youtube.com/watch?v=JmpA7TU_0Ms&amp;t=666s 

import pygame, math
from pygame.locals import *
from random import randint
vec = pygame.math.Vector2

pygame.init()   #Start a pygame.

# Setup the CLOCK---------------------------------------------------------------------- # 
clock = pygame.time.Clock()

# Setup the DISPLAY SCREEN ------------------------------------------------------------ #
xUnits = 1280   #X dimension of the screen.
yUnits = 720    #Y dimension of the screen.
screen = pygame.display.set_mode([xUnits, yUnits], 0, 32)  #Assign the dimension of screen.

# Setup the SPRITE SETTINGS ----------------------------------------------------------- # 
speed1 = 0      #Set character sprite speed to 0.
speed2 = 0      #Set projectile sprite speed to 0.
angle = 0       #Set sprite angle to 0.
x1 = randint(0, xUnits) #Initially set the player in a random x-coordinate.
y1 = randint(0, yUnits) #Initially set the player in a random y-coordinate.
endPos = x1, y1         #Set the random coordinates to endPos.
currLoc1 = endPos        #Set endPos to currLoc.
currLoc2 = endPos

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
        global speed1       #Import variable speed.
        global currLoc1     #Import variable currLoc.
        self.dir = angle    #Set the angle of the vector to self.dir.
        self.vel = vec( math.cos(math.radians(self.dir))*speed1, #Calculate the vectors to.
                        math.sin(math.radians(self.dir))*speed1) #move at a constant speed.
        self.image = pygame.transform.rotate(self.ogim, -angle-90)  #Rotate the sprite to the direction of the mouse click location.
        self.rect = self.image.get_rect(center=self.rect.center)    #Rotate the sprite about its center.
        self.position += self.vel           #Set the velocity added to the position of the Sprite to self.position.
        self.rect.center = self.position    #Center the sprite at its current location.    
        currLoc1 = self.position             #Set self.position to currLoc.
        tempX1, tempY1 = currLoc1           #Set the coordinates of currLoc to tempX1 and tempY1.
        tempX2, tempY2 = endPos             #Set the coordinates ofendPos to tempX2 and tempY2.
        if (round(tempX1) == tempX2) and (round(tempY1) == tempY2): #If the sprite is at the end of the vector...
            speed1 = 0   #STOP THE SPRITE!!!

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bulletScale.png")       #Load the bullet image.
        self.ogim = self.image                                  #Load the sprite image into self.ogim.
        self.position = vec(x1, y1)                             #Place the sprite at x1, y1.
        self.rect = self.image.get_rect(center=self.position)   #Center the sprite at x1, y1.

    def update(self):
        global speed2       #Import variable speed.
        global currLoc2     #Import variable currLoc.
        self.dir = angle    #Set the angle of the vector to self.dir.
        self.vel = vec( math.cos(math.radians(self.dir))*speed2,    #Calculate the vectors to.
                        math.sin(math.radians(self.dir))*speed2)    #move at a constant speed.
        self.image = pygame.transform.rotate(self.ogim, -angle-90)  #Rotate the sprite to the direction of the mouse click location.
        self.rect = self.image.get_rect(center=self.rect.center)    #Rotate the sprite about its center.
        self.position += self.vel           #Set the velocity added to the position of the Sprite to self.position.
        self.rect.center = self.position    #Center the sprite at its current location.    
        currLoc2 = self.position            #Set self.position to currLoc.
        tempX1, tempY1 = currLoc2           #Set the coordinates of currLoc to tempX1 and tempY1.
        tempX2, tempY2 = endPos             #Set the coordinates ofendPos to tempX2 and tempY2.
        if (round(tempX1) == tempX2) and (round(tempY1) == tempY2): #If the sprite is at the end of the vector...
            speed2 = 0   #STOP THE SPRITE!!!

all_sprites = pygame.sprite.Group()
all_sprites.add(Tank())
all_bullets = pygame.sprite.Group()
all_bullets.add(Tank())
# Setup the GAME ---------------------------------------------------------------------- # 
loopCon = True              #Loop condition variable
while loopCon:              #Run the game until...
    # EVENT IN GAME ------------------------------------------------------------------- #
    for event in pygame.event.get():        #there is an event in the game...
        if event.type == pygame.QUIT:           #where the event is the exit button being pressed...
           loopCon = False                          #terminate the game.
        if pygame.mouse.get_pressed()[0]:       #Where there is an event where the mouse gets pressed...
            x1, y1 = currLoc1                       #set the sprite's current location to x1 and y1...
            x2, y2 = pygame.mouse.get_pos()         #assign the x and y coordinates of the mouse click position to x2 and y2...
            endPos = x2, y2                         #set x2 and y2 to endPos...
            y21 = y2 - y1                           #set the difference of y2 and y1 to y21...
            x21 = x2 - x1                           #set the difference of x2 and x1 to x21...
            if (x21 > 0) and (y21 == 0):            #if x21 is positive and y21 is equal to 0...
                angle = 0                               #set angle to 0.
            if (x21 < 0) and (y21 == 0):            #if x21 is negative and y21 is equal to 0...
                angle = 180                             #set angle to 180.
            if (x21 == 0) and (y21 > 0):            #if x21 is equal to 0 and y21 is positive...
                angle = 90                              #set angle to 90.
            if (x21 == 0) and (y21 < 0):            #if x21 is equal to 0 and y21 is negative...
                angle = -90                             #set angle to -90.
            if (x21 != 0):                          #if x21 does not equal 0...
                angle = math.degrees(math.atan(y21/x21))    #set angle to the inverse tangent of y21 divided by x21...
                if (x21 < 0) and (y21 >= 0):                #if x21 is negative and y21 is greater than or equal to 0...
                    angle = 180 + angle                         #set angle added to 180 to angle.
                if (x21 < 0) and (y21 < 0):                 #if x21 is negative and y21 is less than 0...
                    angle = angle - 180                     #set angle subtracted by 180 to angle.
            #speed1 = 1                               #MOVE THE SPRITE!!!
            speed2 = 2
    # DISPLAY TO SCREEN --------------------------------------------------------------- #       
    all_sprites.update()        #Update the sprite's movement.
    all_bullets.update()
    screen.fill((74, 65, 42))   #Refill the screen with the background after the sprite has moved.
    all_bullets.draw(screen)
    all_sprites.draw(screen)    #Display to the screen.
    pygame.draw.line(screen, [255, 0, 0], currLoc1, endPos, 1)   #Draw the vector.
    pygame.display.update()     #Update the display.
    clock.tick(60)              #Set the frame rate to 60 FPS.
    