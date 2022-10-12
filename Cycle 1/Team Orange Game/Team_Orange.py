import random
import pygame

from objects import Ball, Line, Circle, Square, get_circle_position, \
					Particle, ScoreCard, Button, Message, rotate_image, \
					BlinkingText

pygame.init()
info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w, info.current_h
CENTER = WIDTH //2, HEIGHT // 2

screen= pygame.Surface((800,600))

win = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()
FPS = 20

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

#play = BlinkingText(WIDTH//2, HEIGHT-60, 20, "WANT TO PLAY? TAP AWAY", None, WHITE, win)
title_msg = f.render('TEAM ORANGE', 'True', WHITE)
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
play_rect = pygame.image.load("Play Rect.png")
option_rect = pygame.image.load("Options Rect.png")
quit_rect = pygame.image.load("Quit Rect.png")
back_rect = pygame.image.load("Back Rect.png")
sound_off_img = pygame.image.load("soundOffBtn.png")
sound_on_img = pygame.image.load("soundOnBtn.png")

#Buttons ***********************************************************************
options_btn = Button(option_rect, (200,100), WIDTH//2 -90 , HEIGHT//2 -25 , hovering_color = 'Green')
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT//2 + 120, hovering_color= "Green")
play_btn = Button(play_rect, (200,100), WIDTH //2 -90, HEIGHT//2 -200, hovering_color="Green")
back_btn = Button(back_rect, (100,100), WIDTH//4 -18, HEIGHT// 2 -180, hovering_color = "Green")
quit_btn = Button(quit_rect, (200,100), WIDTH//2 -90, HEIGHT// 2 +150, hovering_color = "Green")
full_screen_btn = Button(quit_rect, (200,100), WIDTH//2 -90, HEIGHT// 2 -150, hovering_color = "Green")




# Groups *********************************************************************************

RADIUS = 70
#ball = Ball((CENTER[0], CENTER[1]+RADIUS), RADIUS, 90, win)
# Variables **************************************************************************
home_page = True
game_page = False
options_page = False
sound_on = True
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
            #play.update()
            #win.blit()
            win.blit(title_msg, (575, HEIGHT//2 - 300))
            if play_btn.draw(win):
                home_page = False
                game_page = True
            if options_btn.draw(win):
                home_page= False
                options_page = True
            if quit_btn.draw(win):
                running = False
        if options_page:
            if back_btn.draw(win):
                home_page = True
                options_page = False
            if sound_btn.draw(win):
                sound_on = not sound_on
                if sound_on:
                    sound_btn.update_image(sound_on_img)
                    pygame.mixer.music.play(loops=-1)
                else:
                    sound_btn.update_image(sound_off_img)
                    pygame.mixer.music.stop()
        if game_page:
            if back_btn.draw(win):
                home_page = True
                game_page = False            
    clock.tick(FPS)
    pygame.display.update()
running = False