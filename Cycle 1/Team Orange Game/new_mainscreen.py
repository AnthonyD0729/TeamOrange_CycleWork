import pygame,sys
from button import Button
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")


clock = pygame.time.Clock()
FPS=60

# Colors
RED = (255,0,0)
GREEN = (0,177,64)
BLUE = (30, 144,255)
ORANGE = (252,76,2)
YELLOW = (254,221,0)
PURPLE = (155,38,182)
AQUA = (0,103,127)
WHITE = (200,200,200)
BLACK = (30,30,30)
GRAY = (128,128,128)

score_bg = 128

color_list = [BLUE, GREEN, RED, ORANGE, YELLOW, PURPLE]
color_index = 0
color = color_list[color_index]

# Fonts
#definition for the font
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

background_music = pygame.mixer.music.load("music2.mp3")
# Images **********************************************************************
BG = pygame.image.load("Background.png")
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
PLAY_BUTTON = Button(play_rect, pos=(640, 250), scale=(200,100),
                        text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
OPTIONS_BUTTON = Button(option_rect, pos=(640, 400), scale=(200,100),
                        text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
QUIT_BUTTON = Button(quit_rect, pos=(400, 400), scale=(200,100),
                        text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
SOUND_BUTTON = Button(sound_on_img, pos=(100,100), scale=(200,100), text_input="Sound?", font=get_font(75), base_color= "#d7fcd4", hovering_color="Green")

# Defintions

def options():
    sound_on = True
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(img=back_rect, pos=(640, 460), scale=(200,100), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        SOUND_BUTTON = Button(img=sound_on_img, pos=(100,100), scale=(200,100), text_input="Sound?", font=get_font(75), base_color= "Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        SOUND_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        for button in [SOUND_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)        
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    return
                if SOUND_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    sound_on = not sound_on
                    if sound_on:
                        SOUND_BUTTON.update_image(sound_on_img)
                        pygame.mixer.music.play(loops=-1)
                    else:
                        SOUND_BUTTON.update_image(sound_off_img)
                        pygame.mixer.music.stop()

        pygame.display.update()
#*************************************************************

home_page = True
game_page = False
options_page = False
running = True

#main menu screen
while True:
    SCREEN.blit(BG, (0, 0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    MENU_TEXT = get_font(100).render("TEAM ORANGE", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    PLAY_BUTTON = Button(play_rect, pos=(640, 250), scale=(200,100), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
    OPTIONS_BUTTON = Button(option_rect, pos=(640, 400), scale=(200,100), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
    QUIT_BUTTON = Button(quit_rect, pos=(640, 550), scale=(200,100),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")

    SCREEN.blit(MENU_TEXT, MENU_RECT)

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                
            if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                options()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()

    pygame.display.update()
