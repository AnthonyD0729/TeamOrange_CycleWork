#imports needed**********************************************************
import pygame,sys
from button import Button
from pygame.locals import *

from util import load_save, reset_keys
from controls import Controls_Handler
from tank import Tank
import random
import backnforth, sduck

#allows us to use pygame features
pygame.init()

#Game variables *****************************************************************
SCREEN_WIDTH = 1280
SCREEN_HEIGHT =720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Menu")
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS=60

home_page = True

pregamescreen = False
running = True

actions = {"Left": False, "Right": False, "Up": False, "Down": False, "Start": False, "Action1": False}

save = load_save()
control_handler = Controls_Handler(save)

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

vec = pygame.math.Vector2

# Fonts and Music ***************************************************************************

#definition for the font
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/RetroFont.ttf", size)

font = pygame.font.Font('images/font.ttf',70)
background_music = pygame.mixer.music.load("images/music4.wav")

# Images **********************************************************************
background = pygame.image.load("images/Background.png")

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
confer = pygame.image.load("images/confer.png")

#Buttons ***********************************************************************
GAME_BUTTON = Button(play_rect, pos=(640, 250),
                        text_input="GAME", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
OPTIONS_BUTTON = Button(option_rect, pos=(640, 400),
                        text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
QUIT_BUTTON = Button(quit_rect, pos=(400, 400),
                        text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

PLAY_BUTTON = Button(play_rect, pos=(640, 250),
                        text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

BACK_BUTTON = Button(None, pos=(1100, 660), text_input="BACK", font=get_font(50), base_color="white", hovering_color="Green")

SOUND_BUTTON = Button(None, pos=(200,400), text_input="SOUND", font=get_font(50), base_color= "white", hovering_color="Green")

CONTROLS_BUTTON = Button(None, pos=(1100,180), text_input=("CONTROLS"),font= get_font(50), base_color="white", hovering_color="Green")

RESUME_BUTTON = Button(None, pos= (1100,400), text_input = ("RESUME"), font=get_font(50), base_color="White", hovering_color="Green")

FUN_BUTTON = Button(None, pos=(1100, 400),
                        text_input="FUN", font=get_font(50), base_color="white", hovering_color="Green")

PAUSE_BUTTON = Button(None, pos=(1100,0), text_input=None, font=get_font(75), base_color="Black",hovering_color="Green")

FULLSCREEN_BUTTON = Button(None, pos=(200,180), text_input="Fullscreen", font=get_font(50), base_color="white", hovering_color="Green")

INFO_BUTTON = Button(None, pos=(200,660), text_input="INFO", font=get_font(50), base_color="white", hovering_color="Green")

EASY_BUTTON = Button(None, pos=(175,340), text_input="EASY", font=get_font(50), base_color="white", hovering_color="Green")

MEDIUM_BUTTON = Button(None, pos=(175,340), text_input="MEDIUM", font=get_font(50), base_color="white", hovering_color="Green")

HARD_BUTTON = Button(None, pos=(175,340), text_input="HARD", font=get_font(50), base_color="white", hovering_color="Green")

SITTING_DUCK_BUTTON = Button(None, pos=(450,200), text_input="SDUCK", font=get_font(50), base_color="White", hovering_color="Green")

BACKNFORTH_BUTTON = Button(None, pos=(450,400), text_input="BACKNFORTH", font=get_font(50), base_color="White", hovering_color="Green")

PEASHOOT_BUTTON = Button(None, pos=(450,600), text_input="PEASHOOT", font=get_font(50), base_color="White", hovering_color="Green")

ZITGUN_BUTTON = Button(None, pos=(900,200), text_input="ZITGUN", font=get_font(50), base_color="White", hovering_color="Green")

TRACKER_BUTTON = Button(None, pos=(900,400), text_input="TRACKER", font=get_font(50), base_color="White", hovering_color="Green")

WALLBOMB_BUTTON = Button(None, pos=(900,600), text_input="WALLBOMB", font=get_font(50), base_color="White", hovering_color="Green")

CIRCLES_BUTTON = Button(None, pos=(450,200), text_input="CIRCLES", font=get_font(50), base_color="White", hovering_color="Green")

GLADYS_BUTTON = Button(None, pos=(450,400), text_input="GLADYS", font=get_font(50), base_color="White", hovering_color="Green")

INDIRECT_BUTTON = Button(None, pos=(450,600), text_input="INDIRECT", font=get_font(50), base_color="White", hovering_color="Green")

MOSQUITO_BUTTON = Button(None, pos=(900,200), text_input="MOSQUITO", font=get_font(50), base_color="White", hovering_color="Green")

OVERHEAT_BUTTON = Button(None, pos=(900,400), text_input="OVERHEAT", font=get_font(50), base_color="White", hovering_color="Green")

RAMMER_BUTTON = Button(None, pos=(900,600), text_input="RAMMER", font=get_font(50), base_color="White", hovering_color="Green")

SCOOTER_BUTTON = Button(None, pos=(450,200), text_input="SCOOTER", font=get_font(50), base_color="white", hovering_color="Green")

SUICIDE_BUTTON = Button(None, pos=(450,400), text_input="SUICIDE", font=get_font(50), base_color="white", hovering_color="Green")

TRAPPER_BUTTON = Button(None, pos=(450,600), text_input="TRAPPER", font=get_font(50), base_color="white", hovering_color="Green")

TOBI_8_BUTTON = Button(None, pos=(900,200), text_input="TOBI-8", font=get_font(50), base_color="white", hovering_color="Green")

SWEEPER_BUTTON = Button(None, pos=(900,400), text_input="SWEEPER", font=get_font(50), base_color="white", hovering_color="Green")

SHANNON_BUTTON = Button(None, pos=(900,600), text_input="SHANNON", font=get_font(50), base_color="White", hovering_color="Green")

# Defintions ***************************************************************************************************************************************

def options():
    sound_on = True
    running = True
    while running:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("orange")

        OPTIONS_TEXT = get_font(75).render("OPTIONS SCREEN", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 60))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        screen.blit(confer, (500,300))

        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SOUND_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        CONTROLS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        FULLSCREEN_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        INFO_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        CONTROLS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        for button in [SOUND_BUTTON, FUN_BUTTON, CONTROLS_BUTTON, FULLSCREEN_BUTTON, INFO_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)
        BACK_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
                if FUN_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    funscreen()
                if CONTROLS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    controlspage()
                if FULLSCREEN_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    fullscreen_option()
                if INFO_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    infopage()
        pygame.display.update()

def pausescreen():
    sound_on =True
    run = True
    while run:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill('orange')

        OPTIONS_TEXT = get_font(80).render("GAME PAUSED", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 30))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

    
        RESUME_BUTTON.changeColor(PAUSE_MOUSE_POS)
        SOUND_BUTTON.changeColor(PAUSE_MOUSE_POS)
        CONTROLS_BUTTON.changeColor(PAUSE_MOUSE_POS)
        FULLSCREEN_BUTTON.changeColor(PAUSE_MOUSE_POS)
        INFO_BUTTON.changeColor(PAUSE_MOUSE_POS)
        for button in [SOUND_BUTTON, RESUME_BUTTON, CONTROLS_BUTTON, FULLSCREEN_BUTTON]:
            button.changeColor(PAUSE_MOUSE_POS)
            button.update(screen)
        RESUME_BUTTON.update(screen)

        #check if game is paused
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    return
                if SOUND_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    sound_on = not sound_on
                    if sound_on:
                        pygame.mixer.music.play(loops=-1)
                    else:
                            pygame.mixer.music.stop()
                if FUN_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    funscreen()
                if CONTROLS_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    controlspage()
                if FULLSCREEN_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    fullscreen_option()
                if INFO_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    infopage()

        pygame.display.update()

def controlspage():
    running = True
    while running:
        screen.fill('orange')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_b:
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
                    actions['Action 1'] = True

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
                    actions['Action 1'] = False

        control_handler.update(actions)
        canvas.fill(('orange'))
        control_handler.render(canvas)
        screen.blit(pygame.transform.scale(canvas, (SCREEN_WIDTH*2.7, SCREEN_HEIGHT*2.7)), (0,0))
        pygame.display.update()
        reset_keys(actions)


def infopage():
    run = True
    while run:

        screen.fill('Orange')

        INFO_TEXT = get_font(80).render("GAME CREATED BY", True, "White")
        INFO_RECT = INFO_TEXT.get_rect(center=(640, 30))
        screen.blit(INFO_TEXT, INFO_RECT)

        INFO_TEXT = get_font(30).render("Anthony Deyoe, Kevin Malone, Sal Mecca, Isaac Otto", True, "White")
        INFO_RECT = INFO_TEXT.get_rect(center=(640, 360))
        screen.blit(INFO_TEXT, INFO_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return

        pygame.display.update()

def fullscreen_option():
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    fullscreen = False
    run = True
    while run:
        screen.fill("orange")
        FULL_TEXT = get_font(30).render("PRESS F FOR FULLSCREEN", True, "White")
        FULL_RECT = FULL_TEXT.get_rect(center=(640, 360))
        screen.blit(FULL_TEXT, FULL_RECT)

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

def easyscreen():
    running = True
    while running:
        screen.fill('orange')
        EASYSCREEN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN_TEXT = get_font(75).render("CHOOSE YOUR OPPONENT:", True, "White")
        SCREEN_RECT = SCREEN_TEXT.get_rect(center=(640, 30))
        screen.blit(SCREEN_TEXT, SCREEN_RECT)
        
        SITTING_DUCK_BUTTON.changeColor(EASYSCREEN_MOUSE_POS)
        BACKNFORTH_BUTTON.changeColor(EASYSCREEN_MOUSE_POS)
        PEASHOOT_BUTTON.changeColor(EASYSCREEN_MOUSE_POS)
        ZITGUN_BUTTON.changeColor(EASYSCREEN_MOUSE_POS)
        TRACKER_BUTTON.changeColor(EASYSCREEN_MOUSE_POS)
        WALLBOMB_BUTTON.changeColor(EASYSCREEN_MOUSE_POS)
        for button in [SITTING_DUCK_BUTTON, BACKNFORTH_BUTTON, PEASHOOT_BUTTON, ZITGUN_BUTTON, TRACKER_BUTTON, WALLBOMB_BUTTON]:
            button.changeColor(EASYSCREEN_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_b:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SITTING_DUCK_BUTTON.checkForInput(EASYSCREEN_MOUSE_POS):
                    sduckBot()
                if BACKNFORTH_BUTTON.checkForInput(EASYSCREEN_MOUSE_POS):
                    backnforthBot() # Added 'Bot' to the end because of conflicting names
                if PEASHOOT_BUTTON.checkForInput(EASYSCREEN_MOUSE_POS):
                    peashoot()
                if ZITGUN_BUTTON.checkForInput(EASYSCREEN_MOUSE_POS):
                    zitgun()
                if TRACKER_BUTTON.checkForInput(EASYSCREEN_MOUSE_POS):
                    tracker()
                if WALLBOMB_BUTTON.checkForInput(EASYSCREEN_MOUSE_POS):
                    wallbomb()
        pygame.display.update()

def mediumscreen():
    running = True
    while running:
        screen.fill('orange')
        MEDIUMSCREEN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN_TEXT = get_font(75).render("CHOOSE YOUR OPPONENT:", True, "White")
        SCREEN_RECT = SCREEN_TEXT.get_rect(center=(640, 30))
        screen.blit(SCREEN_TEXT, SCREEN_RECT)
        
        CIRCLES_BUTTON.changeColor(MEDIUMSCREEN_MOUSE_POS)
        GLADYS_BUTTON.changeColor(MEDIUMSCREEN_MOUSE_POS)
        INDIRECT_BUTTON.changeColor(MEDIUMSCREEN_MOUSE_POS)
        MOSQUITO_BUTTON.changeColor(MEDIUMSCREEN_MOUSE_POS)
        OVERHEAT_BUTTON.changeColor(MEDIUMSCREEN_MOUSE_POS)
        RAMMER_BUTTON.changeColor(MEDIUMSCREEN_MOUSE_POS)
        for button in [CIRCLES_BUTTON,GLADYS_BUTTON,INDIRECT_BUTTON,MOSQUITO_BUTTON,OVERHEAT_BUTTON,RAMMER_BUTTON]:
            button.changeColor(MEDIUMSCREEN_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_b:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CIRCLES_BUTTON.checkForInput(MEDIUMSCREEN_MOUSE_POS):
                    circles()
                if GLADYS_BUTTON.checkForInput(MEDIUMSCREEN_MOUSE_POS):
                    gladys()
                if INDIRECT_BUTTON.checkForInput(MEDIUMSCREEN_MOUSE_POS):
                    indirect()
                if MOSQUITO_BUTTON.checkForInput(MEDIUMSCREEN_MOUSE_POS):
                    mosquito()
                if OVERHEAT_BUTTON.checkForInput(MEDIUMSCREEN_MOUSE_POS):
                    overheat()
                if RAMMER_BUTTON.checkForInput(MEDIUMSCREEN_MOUSE_POS):
                    rammer()
        pygame.display.update()



def hardscreen():
    running = True
    while running:
        screen.fill('orange')
        HARDSCREEN_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN_TEXT = get_font(75).render("CHOOSE YOUR OPPONENT:", True, "White")
        SCREEN_RECT = SCREEN_TEXT.get_rect(center=(640, 30))
        screen.blit(SCREEN_TEXT, SCREEN_RECT)
        
        SCOOTER_BUTTON.changeColor(HARDSCREEN_MOUSE_POS)
        SUICIDE_BUTTON.changeColor(HARDSCREEN_MOUSE_POS)
        TRAPPER_BUTTON.changeColor(HARDSCREEN_MOUSE_POS)
        TOBI_8_BUTTON.changeColor(HARDSCREEN_MOUSE_POS)
        SWEEPER_BUTTON.changeColor(HARDSCREEN_MOUSE_POS)
        SHANNON_BUTTON.changeColor(HARDSCREEN_MOUSE_POS)
        for button in [SCOOTER_BUTTON,SUICIDE_BUTTON,TRAPPER_BUTTON,TOBI_8_BUTTON,SWEEPER_BUTTON,SHANNON_BUTTON]:
            button.changeColor(HARDSCREEN_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_b:
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SCOOTER_BUTTON.checkForInput(HARDSCREEN_MOUSE_POS):
                    scooter()
                if SUICIDE_BUTTON.checkForInput(HARDSCREEN_MOUSE_POS):
                    suicide()
                if TRAPPER_BUTTON.checkForInput(HARDSCREEN_MOUSE_POS):
                    trapper()
                if TOBI_8_BUTTON.checkForInput(HARDSCREEN_MOUSE_POS):
                    tobi8()
                if SWEEPER_BUTTON.checkForInput(HARDSCREEN_MOUSE_POS):
                    sweeper()
                if SHANNON_BUTTON.checkForInput(HARDSCREEN_MOUSE_POS):
                    shannon()
        pygame.display.update()


def sduckBot():

    tank = sduck.Tank(random.randint(60,SCREEN_WIDTH-60),random.randint(60,SCREEN_HEIGHT-60))
    tank_group = pygame.sprite.Group()
    tank_group.add(tank)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        tank.run()
        screen.fill('black')
        tank_group.draw(screen)

        pygame.display.update()

        clock.tick(FPS)
       
def backnforthBot():

    tank = backnforth.Tank(random.randint(60,SCREEN_WIDTH-60),random.randint(60,SCREEN_HEIGHT-60))
    tank_group = pygame.sprite.Group()
    tank_group.add(tank)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        tank.run()
        screen.fill('black')
        tank_group.draw(screen)

        pygame.display.update()

        clock.tick(FPS)

def peashoot():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def zitgun():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def tracker():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def wallbomb():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def circles():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def gladys():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def indirect():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def mosquito():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def overheat():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def rammer():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def scooter():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def suicide():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def trapper():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def tobi8():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def sweeper():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()

def shannon():
    run = True
    while run:

        screen.fill('black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    return
                if event.key == pygame.K_p:
                    pausescreen()

        pygame.display.update()


def funscreen():
    pygame.quit()
    
# MAIN ****************************************************************************************
while running:
    if home_page:
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TEAM ORANGE", True, "white")
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
        
        PREGAME_MOUSE_POS = pygame.mouse.get_pos()

        PREGAME_TEXT = get_font(75).render("CHOOSE YOUR DIFFICULTY:", True, "WHITE")
        PREGAME_RECT = PREGAME_TEXT.get_rect(center=(640, 100))

        EASY_BUTTON = Button(None, pos=(640,250), text_input="EASY", font=get_font(50), base_color="White", hovering_color="Green")

        MEDIUM_BUTTON = Button(None, pos=(640,450), text_input="MEDIUM", font=get_font(50), base_color="White", hovering_color="Green")

        HARD_BUTTON = Button(None, pos=(640,650), text_input="HARD", font=get_font(50), base_color="White", hovering_color="Green")


        screen.blit(PREGAME_TEXT, PREGAME_RECT)
        for button in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button.changeColor(PREGAME_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    pregamescreen = False
                    home_page = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(PREGAME_MOUSE_POS):
                    easyscreen()
                if MEDIUM_BUTTON.checkForInput(PREGAME_MOUSE_POS):
                    mediumscreen()
                if HARD_BUTTON.checkForInput(PREGAME_MOUSE_POS):
                    hardscreen()


        pygame.display.update()
    
    pygame.display.update()