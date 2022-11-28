import pygame
import math
import random
from pygame.locals import *
vec = pygame.math.Vector2


class Tank(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/OrangeSprite.png")
        self.ogimg = self.image
        self.position = vec(xpos, ypos)
        self.rect = self.image.get_rect(center=self.position)
