import pygame
import testank
import tankclass



pygame.init()

# Set the game's tick speed
FPS = 60
tickrate = pygame.time.Clock()

# Sets screen size
screenWidth = 600
screenHeight = 600

# Displays the window
screen = pygame.display.set_mode((screenWidth,screenHeight), 0, 32)
pygame.display.set_icon(pygame.image.load("images/OrangeIcon.png"))
pygame.display.set_caption("oh brother")
GREY = (76,81,83)


tank = tankclass.Tank(100, 100)
allsprites = pygame.sprite.Group
allsprites.add(testank())

running = True
while running:

    # Quit parameters
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


    screen.fill(GREY)
    allsprites.draw(screen)
    pygame.display.update()

    # ATROBOT tank "program"



    tickrate.tick(FPS)