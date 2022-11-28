#expiration = False
#iAmGoingToLoseIt = True

#if iAmGoingToLoseIt:
#    expiration = True
#    print("I have perished due to 'rect' being the single worst piece of garbage ever conceived.")
#    print("How could something so absolutely vile exist without an endlessly malevolent creator?")
#    print("The implications of such a being spell doom for the human race,")
#    print("for they seek only to cause suffering as far as their arms can reach.")
#    print("The only remedy for my fellow man is to accept imminent demise...")
#    print("...or to end it all before the suffering begins.")

from turtle import update
import pygame
import math
import random
from pygame.locals import *

vec = pygame.math.Vector2


pygame.init()

# Set the game's tick speed
FPS = 30
tickrate = pygame.time.Clock()

# Sets screen size
screenWidth = 600
screenHeight = 600

# Displays the window
screen = pygame.display.set_mode((screenWidth,screenHeight), 0, 32)
pygame.display.set_icon(pygame.image.load("images/OrangeIcon.png"))
pygame.display.set_caption("who made this lol")
GREY = (76,81,83)

MAXSPEED = 4
newspeed = 0
speed = 0
oldangle = 0
angle = 0
currLoc = 0
currThrot = 0
throt = 0
turn = 0

# Tank class
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/OrangeTank.png")
        self.ogim = self.image
        self.position = vec(screenWidth/2, screenHeight/2)
        self.rect = self.image.get_rect(center=self.position)
        

    # Moves the tank using vector
    def update(self):
        global currLoc
        global angle
        global speed
        global throt
        self.dir = angle
        self.vel = vec( math.cos(math.radians(self.dir))*speed,
                        math.sin(math.radians(self.dir))*speed)
        self.position += self.vel
        currLoc = self.position
        self.rect.center = self.position
        #why does the rotation only work here??
        self.image = pygame.transform.rotate(self.ogim, -angle-90)
        self.rect = self.image.get_rect(center=self.rect.center)      

        if speed < MAXSPEED * throt/100:
            speed += MAXSPEED/60
        if speed > MAXSPEED:
            speed = MAXSPEED

        if angle > turn:
            angle -= 2
            #print(angle)
        if angle < turn:
            angle += 2
            #print("poop")
        # keep angle within 0-360
        if angle > 360:
            angle -= 360
        if angle < 0:
            angle += 360
        
    

    def boundarycheck(self):
        global currLoc
        global angle
        x, y = currLoc
        if (x>screenWidth or x<0) or (y>screenHeight or y<0):
            pygame.time.wait(200)
            angle += 180

    def turn(self, turn_input):
        global turn
        turn = turn_input

    def throttle(self, throt_input):
        global throt
        throt = throt_input


    def wait(self, time):
        print('mama')


all_sprites = pygame.sprite.Group()
all_sprites.add(Tank())
 
running = True
while running:

    # Quit parameters
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


    all_sprites.update()
    Tank().boundarycheck()
    Tank().throttle(100)
    Tank().turn(200)

    screen.fill(GREY)
    all_sprites.draw(screen)
    pygame.display.update()

    # ATROBOT tank "program"



    tickrate.tick(FPS)