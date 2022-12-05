import pygame
pygame.init()

xUnits = 600
yUnits = 600
screen = pygame.display.set_mode([xUnits, yUnits], 0, 32)  #Assign the dimension of screen
clock = pygame.time.Clock()
clock.tick(60)              #Cap the frames per second [fps] to 60 fps

loopCon = True
while loopCon:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           loopCon = False

    screen.fill((74, 65, 42))   #Refill the screen with the background after the square has moved
    pygame.draw.line(screen, [255, 0, 0], [0, 0], [xUnits/2, yUnits/2], 1)
    pygame.display.flip()       #Update the entire display surface to the computer screen

