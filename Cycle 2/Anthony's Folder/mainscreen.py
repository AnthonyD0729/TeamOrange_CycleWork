#imports needed**********************************************************
import pygame,sys
from button import Button
#import pygame_menu
from util import load_save, reset_keys
from controls import Controls_Handler

#allows us to use pygame features
pygame.init()

#Game variables *****************************************************************
#SCREEN_WIDTH = 1280
#SCREEN_HEIGHT =720
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Menu")
canvas = pygame.Surface((480,270))
clock = pygame.time.Clock()
FPS=60
play_page1 = False
play_page2 = False
play_page3 = False
home_page = True
game_page = False
options_page = False
pregamescreen = False
running = True
save = load_save()
control_handler = Controls_Handler(save)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

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

font = pygame.font.Font('images/font.ttf',70)
background_music = pygame.mixer.music.load("images/music4.wav")

# Images **********************************************************************
BG = pygame.image.load("images/Background.png")
BG2 = pygame.image.load("images/Background2.png")
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
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/Options Rect.png").convert_alpha()
quit_img = pygame.image.load("images/Quit Rect.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/Back Rect.png').convert_alpha()
pause_img = pygame.image.load('images/pause.png').convert_alpha()
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

BACK_BUTTON = Button(None, pos=(1100, 660), text_input="BACK", font=get_font(50), base_color="Black", hovering_color="Green")

SOUND_BUTTON = Button(sound_on_img, pos=(1100,500), text_input="SOUND", font=get_font(50), base_color= "Black", hovering_color="Green")

CONTROLS_BUTTON = Button(None, pos=(1100,180), text_input=("CONTROLS"),font= get_font(50), base_color="Black", hovering_color="Green")

RESUME_BUTTON = Button(None, pos= (1100,660), text_input = ("RESUME"), font=get_font(75), base_color="Black", hovering_color="Green")

VIDEO_BUTTON = Button(None, pos=(1100, 340),
                        text_input="VIDEO", font=get_font(50), base_color="Black", hovering_color="Black")

PAUSE_BUTTON = Button(back_rect, pos=(1100,0), text_input=None, font=get_font(75), base_color="Black",hovering_color="Green")

FULLSCREEN_BUTTON = Button(None, pos=(175,180), text_input="Fullscreen", font=get_font(50), base_color="Black", hovering_color="Green")

INFO_BUTTON = Button(None, pos=(175,340), text_input="INFO", font=get_font(50), base_color="Black", hovering_color="Green")
# Defintions ***************************************************************************************************************************************

def draw_text(text,font, text_col,x,y):
    img = font.render(text,True, text_col)
    screen.blit(img,(x,y))

def options():
    sound_on = True
    running = True
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SOUND_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        CONTROLS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        for button in [SOUND_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)
        BACK_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    return
                if SOUND_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    sound_on = not sound_on
                    if sound_on:
                        pygame.mixer.music.play(loops=-1)
                    else:
                        pygame .mixer.music.stop()
        pygame.display.update()

def pausescreen():
    sound_on =True
    run = True
    while run:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill('white')

        OPTIONS_TEXT = get_font(80).render("GAME PAUSED", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        RESUME_BUTTON.changeColor(PAUSE_MOUSE_POS)
        SOUND_BUTTON.changeColor(PAUSE_MOUSE_POS)
        CONTROLS_BUTTON.changeColor(PAUSE_MOUSE_POS)
        FULLSCREEN_BUTTON.changeColor(PAUSE_MOUSE_POS)
        INFO_BUTTON.changeColor(PAUSE_MOUSE_POS)
        for button in [SOUND_BUTTON, RESUME_BUTTON, VIDEO_BUTTON, CONTROLS_BUTTON, FULLSCREEN_BUTTON, INFO_BUTTON]:
            button.changeColor(PAUSE_MOUSE_POS)
            button.update(screen)
        RESUME_BUTTON.update(screen)

        #check if game is paused
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    return
                if SOUND_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    sound_on = not sound_on
                    if sound_on:
                        pygame.mixer.music.play(loops=-1)
                    else:
                            pygame.mixer.music.stop()
                if VIDEO_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    print("Video Settings")
                if CONTROLS_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    controlspage()
                if FULLSCREEN_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    fullscreen_option()
                if INFO_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    infopage()

        pygame.display.update()

def controlspage():
    save = load_save()
    control_handler = Controls_Handler(save)
    actions = {"Left": False, "Right": False, "Up": False, "Down": False, "Start": False, "Action1": False}
    running = True
    while running:
    ################################# CHECK PLAYER INPUT #################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = True
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = True
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = True
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = True
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = True
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = True

            if event.type == pygame.KEYUP:
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = False
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = False
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = False
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = False
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = False
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = False

        ################################# UPDATE THE GAME #################################
        control_handler.update(actions)
        ################################# RENDER WINDOW AND DISPLAY #################################
        canvas.fill(("white"))
        control_handler.render(canvas)
        screen.blit(pygame.transform.scale(canvas, (1280,720) ), (0,0))
        pygame.display.update()
        reset_keys(actions)

def infopage():
    run = True
    while run:

        screen.fill('Orange')

        INFO_TEXT = get_font(80).render("GAME CREATED BY", True, "Black")
        INFO_RECT = INFO_TEXT.get_rect(center=(640, 30))
        screen.blit(INFO_TEXT, INFO_RECT)

        INFO_TEXT = get_font(30).render("Anthony Deyoe, Kevin Malone, Sal Mecca, Isaac Otto", True, "Black")
        INFO_RECT = INFO_TEXT.get_rect(center=(640, 360))
        screen.blit(INFO_TEXT, INFO_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()

def fullscreen_option():
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    fullscreen = False
    run = True
    while run:
        screen.fill("white")
        FULL_TEXT = get_font(30).render("PRESS F FOR FULLSCREEN", True, "Black")
        FULL_RECT = FULL_TEXT.get_rect(center=(640, 360))
        screen.blit(FULL_TEXT, FULL_RECT)

        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(screen.get_width() - 5 - (screen.get_width() / 5), 50, screen.get_width() / 5, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                if event.key == pygame.K_b:
                    return
    
        pygame.display.update()
        clock.tick(60)
# MAIN ****************************************************************************************
while running:
    if home_page:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TEAM ORANGE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        GAME_BUTTON = Button(play_rect, pos=(640, 250),
                                text_input="GAME", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        OPTIONS_BUTTON = Button(option_rect, pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(quit_rect, pos=(640, 550),
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [GAME_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    home_page = False
                    pregamescreen = True
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    running = False
    
    if pregamescreen:
        screen.fill("ORANGE")

        PREGAME_TEXT = get_font(80).render("CHOOSE YOUR DIFFICULT:", True, "WHITE")
        PREGAME_RECT = PREGAME_TEXT.get_rect(center=(640, 100))

        PREGAME1_TEXT = get_font(80).render("1 = EASY", True, "WHITE")
        PREGAME1_RECT = PREGAME1_TEXT.get_rect(center=(640, 250))

        PREGAME2_TEXT = get_font(80).render("2 = MEDIUM", True, "WHITE")
        PREGAME2_RECT = PREGAME2_TEXT.get_rect(center=(640, 400))

        PREGAME3_TEXT = get_font(80).render("3 = HARD", True, "WHITE")
        PREGAME3_RECT = PREGAME3_TEXT.get_rect(center=(640, 550))

        screen.blit(PREGAME_TEXT, PREGAME_RECT)
        screen.blit(PREGAME1_TEXT, PREGAME1_RECT)
        screen.blit(PREGAME2_TEXT, PREGAME2_RECT)
        screen.blit(PREGAME3_TEXT, PREGAME3_RECT)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pregamescreen = False
                    play_page1 = True
                if event.key == pygame.K_2:
                    pregamescreen = False
                    play_page2 = True
                if event.key == pygame.K_3:
                    pregamescreen = False
                    play_page3 = True
                if event.key == pygame.K_ESCAPE:
                    quit()

        pygame.display.update()


    
    if play_page1:
        screen.blit(BG2, (0,0))
        
        PLAY1_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TEAM ORANGE 1", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 105))

        screen.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausescreen()
        
    if play_page2:
        screen.blit(BG2, (0,0))
        
        PLAY2_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TEAM ORANGE 2", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 105))

        screen.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausescreen()

    if play_page3:
        screen.blit(BG2, (0,0))
        
        PLAY3_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TEAM ORANGE 3", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 105))

        screen.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausescreen()

    pygame.display.update()
