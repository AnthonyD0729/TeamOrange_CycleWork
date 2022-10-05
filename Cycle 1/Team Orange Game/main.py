import random
import pygame

from objects import Ball, Line, Circle, Square, get_circle_position, \
					Particle, ScoreCard, Button, Message, rotate_image, \
					BlinkingText

pygame.init()
SCREEN = WIDTH, HEIGHT = 1280, 720
CENTER = WIDTH //2, HEIGHT // 2

info = pygame.display.Info()
width = info.current_w
height = info.current_h

if width >= height:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
else:
	win = pygame.display.set_mode(SCREEN, pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN)

clock = pygame.time.Clock()
FPS = 60

# COLORS *********************************************************************

RED = (255,0,0)
GREEN = (0,177,64)
BLUE = (30, 144,255)
ORANGE = (252,76,2)
YELLOW = (254,221,0)
PURPLE = (155,38,182)
AQUA = (0,103,127)
WHITE = (255,255,255)
BLACK = (30,30,30)
GRAY = (128,128,128)

score_bg = 128

color_list = [BLUE, GREEN, RED, ORANGE, YELLOW, PURPLE]
color_index = 0
color = color_list[color_index]

# FONT ************************************************************************

font = "font.ttf"

f = pygame.font.Font(font, 45)

play = BlinkingText(WIDTH//2, HEIGHT-60, 20, "WANT TO PLAY? TAP AWAY", None, WHITE, win)

# Sounds ********************************************************************
click = pygame.mixer.Sound("click.wav")
click.set_volume(0.2)
background_music = pygame.mixer.music.load("music2.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.7)


# Images **********************************************************************
blue = pygame.image.load("BlueSprite.png")
cyan = pygame.image.load("CyanSprite.png")
green = pygame.image.load("GreenSprite.png")
orange = pygame.image.load("OrangeSprite.png")
pink = pygame.image.load("PinkSprite.png")
red = pygame.image.load("RedSprite.png")
yellow = pygame.image.load("YellowSprite.png")
option_rect = pygame.image.load("Options Rect.png")
sound_off_img = pygame.image.load("soundOffBtn.png")
sound_on_img = pygame.image.load("soundOnBtn.png")
#Buttons ***********************************************************************
options_btn = Button(cyan, (100,100), WIDTH// 4 - 18, HEIGHT//2 + 120, hovering_color = 'Green')
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 + 120, hovering_color= "Green")
play_btn = Button(pink, (100,100), WIDTH //4 -20, HEIGHT//4 +100, hovering_color="Green")
# Groups *********************************************************************************

RADIUS = 70
ball = Ball((CENTER[0], CENTER[1]+RADIUS), RADIUS, 90, win)
# Variables **************************************************************************
home_page = True
game_page = False
options_page = False
running = True
while running:

    win.fill("ORANGE")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or \
			    event.key == pygame.K_q:
                running = False

        #if event.type == pygame.MOUSEBUTTONDOWN:

        if home_page:
            play.update()
            #win.blit()
            PLAY_BUTTON = Button(pink, (100,100), x = 640, y=250, 
                            hovering_color="Black")
            OPTIONS_BUTTON = Button(option_rect,(100,100), x=640, y=400, 
                            hovering_color="Black")

            if play_btn.draw(win):
                home_page = False
                game_page = True
            if options_btn.draw(win):
                home_page= False
                options_page = True

        if sound_btn.draw(win):
            sound_on = not sound_on
            if sound_on:
                sound_btn.update_image(sound_on_img)
                pygame.mixer.music.play(loops=-1)
            else:
                sound_btn.update_image(sound_off_img)
                pygame.mixer.music.stop()
    clock.tick(FPS)
    pygame.display.update()
running = False