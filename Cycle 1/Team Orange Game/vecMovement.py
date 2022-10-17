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
#    print("Recall my words when the End begins.")

import pygame
import math
import random
import sys
from pygame.locals import *

vec = pygame.math.Vector2


pygame.init()

# Set the game's tick speed
FPS = 60
tickrate = pygame.time.Clock()

# Sets screen size
screenWidth = 800
screenHeight = 600

# Displays the window
screen = pygame.display.set_mode((screenWidth,screenHeight), 0, 32)
#pygame.display.set_icon(pygame.image.load("OrangeIcon.png"))
pygame.display.set_caption("vector")
BLACK = (0,0,0)
RED = (255,0,0)

# Tank class
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("OrangeSprite.png")
        self.position = vec(screenWidth/2, screenHeight/2)
        self.rect = self.image.get_rect(center=self.position)
        self.vel = vec(1,1)
        self.angle = 0

    #maybe a get_vec function that creates a vector based on angle+speed

    # Moves the tank using vector
    def update(self):
        self.position += self.vel
        self.rect.center = self.position


all_sprites = pygame.sprite.Group()
tank = Tank()
all_sprites.add(tank)

running = True
while running:

    # Quit parameters
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.update()

    tickrate.tick(FPS)