import pygame
pygame.init()

#create game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT =720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#color
TEXT_COL = (255,255,255)

#draws text on the screen
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    SCREEN.blit(img,(x,y))

#font
font = pygame.font.SysFont('RetroFont.ttf',40)

#game loop
run = True
game_pause = False
while run:
    SCREEN.fill((52,78,91))
    draw_text("Press Space to pause", font, TEXT_COL, 160,250)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE:
                game_pause = True
            if event.type == pygame.QUIT:
                run = False
pygame.display.update()