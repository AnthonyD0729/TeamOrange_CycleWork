import pygame
import math
SCREEN_WIDTH = 1280
SCREEN_HEIGHT =720  
vec = pygame.math.Vector2
speed =1
angle = 45
currLoc = 0

class Tank(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/OrangeSprite.png")
        self.ogim = self.image
        self.position = vec(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.rect = self.image.get_rect(center=self.position)
        

    # Moves the tank using vector
    def update(self):
        global currLoc
        self.dir = angle
        self.vel = vec( math.cos(math.radians(self.dir))*speed,
                        math.sin(math.radians(self.dir))*speed)
        self.position += self.vel
        currLoc = self.position
        self.rect.center = self.position
        #why does the rotation only work here??
        self.image = pygame.transform.rotate(self.ogim, -angle-90)
        self.rect = self.image.get_rect(center=self.rect.center)        


    def boundarycheck(self):
        global currLoc
        global angle
        x, y = currLoc
        if (x>SCREEN_WIDTH or x<0) or (y>SCREEN_WIDTH or y<0):
            pygame.time.wait(200)
            angle += 180
