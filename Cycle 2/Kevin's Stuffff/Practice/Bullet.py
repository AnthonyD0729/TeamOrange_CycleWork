#FUNCTION: This program displays the bullet.
#ADAPTED BY: Kevin Malone

import pygame
class bullet(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("bulletScale.png")
        self.rect = self.image.get_rect()
        self.speed = 6
