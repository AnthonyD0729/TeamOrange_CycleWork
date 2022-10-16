#imports needed**********************************************************
from operator import truediv
import pygame,sys
from button import Button
import pygame_menu
from util import load_save, reset_keys
from controls import Controls_Handler

#allows us to use pygame features
pygame.init()

#Game variables *****************************************************************
SCREEN_WIDTH = 1280
SCREEN_HEIGHT =720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu")
canvas = pygame.Surface((480,270))
game_paused =False
clock = pygame.time.Clock()
FPS=60
play_page = False
home_page = True
game_page = False
options_page = False
running = True
# Colors **********************************************************************************
RED = (255,0,0)
GREEN = (0,0,255)
BLUE = (0, 0,255)
ORANGE = (252,76,2)
YELLOW = (254,221,0)
PURPLE = (155,38,182)
AQUA = (0,103,127)
BLACK = (30,30,30)
GRAY = (128,128,128)
TEXT_COL = (255,255,255)

# Fonts and Music ***************************************************************************
#definition for the font
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/RetroFont.ttf", size)

font = pygame.font.Font('images/font.ttf',40)
background_music = pygame.mixer.music.load("images/music2.mp3")

# Images **********************************************************************
BG = pygame.image.load("images/Background.png")
blue = pygame.image.load("images/BlueSprite.png")
cyan = pygame.image.load("images/CyanSprite.png")
green = pygame.image.load("images/GreenSprite.png")
orange = pygame.image.load("images/OrangeSprite.png")
pink = pygame.image.load("images/PinkSprite.png")
red = pygame.image.load("images/RedSprite.png")
yellow = pygame.image.load("images/YellowSprite.png")
play_rect = pygame.image.load("images/Play Rect.png")
option_rect = pygame.image.load("images/Options Rect.png")
quit_rect = pygame.image.load("images/Quit Rect.png")
back_rect = pygame.image.load("images/Back Rect.png")
sound_off_img = pygame.image.load("images/soundOffBtn.png")
sound_on_img = pygame.image.load("images/soundOnBtn.png")
return_img = pygame.image.load("images/button_resume.png")
#Buttons ***********************************************************************
GAME_BUTTON = Button(play_rect, pos=(640, 250),
                        text_input="GAME", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
OPTIONS_BUTTON = Button(option_rect, pos=(640, 400),
                        text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
QUIT_BUTTON = Button(quit_rect, pos=(400, 400),
                        text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
SOUND_BUTTON = Button(sound_on_img, pos=(100,100), text_input="Sound?", font=get_font(75), base_color= "#d7fcd4", hovering_color="Green")

PLAY_BUTTON = Button(play_rect, pos=(640, 250),
                        text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

RESUME_BUTTON = Button
# Defintions ***************************************************************************************************************************************
def draw_text(text,font, text_col,x,y):
    img = font.render(text,True, text_col)
    SCREEN.blit(img,(x,y))

def options():
    sound_on = True
    running = True
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(back_rect, pos=(1100, 660), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        SOUND_BUTTON = Button(sound_on_img, pos=(1100,500), text_input="Sound?", font=get_font(75), base_color= "Black", hovering_color="Green")
        CONTROLS_BUTTON = Button(blue, pos=(640,360), text_input=("CONTROLS"),font= get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        SOUND_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        CONTROLS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        for button in [SOUND_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)        
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return
                if SOUND_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    sound_on = not sound_on
                    if sound_on:
                        pygame.mixer.music.play(loops=-1)
                    else:
                        pygame .mixer.music.stop()
        pygame.display.update()

def pausescreen():
    running = True
    game_play = False
    while running:
        SCREEN.fill((52,78,91))
        #check if game is paused
        if game_play == True:
            play()
            #display menu
        else:
            draw_text("Press Space to play", font, TEXT_COL, 160,250)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    game_play = True
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

def play():
    running = True
    while running:
        SCREEN.fill('WHITE')
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    pausescreen()
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
# MAIN ****************************************************************************************
while running:
    if home_page:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TEAM ORANGE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        GAME_BUTTON = Button(play_rect, pos=(640, 250),
                                text_input="GAME", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        OPTIONS_BUTTON = Button(option_rect, pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(quit_rect, pos=(640, 550),
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [GAME_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    home_page = False
                    pausescreen()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False

    pygame.display.update()
