import pygame, sys
pygame.init()
class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('images/attack_1.png'))
		self.sprites.append(pygame.image.load('images/attack_2.png'))
		self.sprites.append(pygame.image.load('images/attack_3.png'))
		self.sprites.append(pygame.image.load('images/attack_4.png'))
		self.sprites.append(pygame.image.load('images/attack_5.png'))
		self.sprites.append(pygame.image.load('images/attack_6.png'))
		self.sprites.append(pygame.image.load('images/attack_7.png'))
		self.sprites.append(pygame.image.load('images/attack_8.png'))
		self.sprites.append(pygame.image.load('images/attack_9.png'))
		self.sprites.append(pygame.image.load('images/attack_10.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0
				self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]