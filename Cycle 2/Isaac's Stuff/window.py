import pygame
import backnforth, sduck



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
pygame.display.set_caption("me when your mom")
GREY = (76,81,83)


tank1 = backnforth.Tank(200,200)
tank2 = sduck.Tank(400,400)

tank_group = pygame.sprite.Group()
tank_group.add(tank1,tank2)

running = True
while running:

    # Quit parameters
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False


    tank1.run()
    tank2.run()
    screen.fill(GREY)
    tank_group.draw(screen)
    pygame.display.update()
 

    tickrate.tick(FPS)