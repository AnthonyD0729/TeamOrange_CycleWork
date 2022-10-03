import pygame

class Player():
    def player():
        blue = pygame.image.load("BlueSprite.png")
        cyan = pygame.image.load("CyanSprite.png")
        green = pygame.image.load("GreenSprite.png")
        orange = pygame.image.load("OrangeSprite.png")
        pink = pygame.image.load("PinkSprite.png")
        red = pygame.image.load("RedSprite.png")
        yellow = pygame.image.load("YellowSprite.png")
        player_rect_blue = blue.get_rect(midbottom = (80,100))
        player_rect_cyan = cyan.get_rect(midbottom = (80,200))
        player_rect_green = green.get_rect(midbottom = (80,300))
        player_rect_orange = orange.get_rect(midbottom = (80,400))
        player_rect_pink = pink.get_rect(midbottom = (80,500))
        player_rect_red = red.get_rect(midbottom = (80,600))
        player_rect_yellow = yellow.get_rect(midbottom = (80,700))
