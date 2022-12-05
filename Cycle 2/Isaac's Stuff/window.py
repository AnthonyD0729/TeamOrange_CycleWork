import pygame
import testank
import tankclass



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
pygame.display.set_caption("oh brother")
GREY = (76,81,83)



all_sprites = pygame.sprite.Group()
all_sprites.add(tankclass.Tank(50,50))

running = True
while running:

    # Quit parameters
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


    screen.fill(GREY)
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    # pooper
    # holy canoli


    tickrate.tick(FPS)