import pygame, sys
from button import Button
import random 
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#variables
BG = pygame.image.load("Background.png")
blue = pygame.image.load("BlueSprite.png")
cyan = pygame.image.load("CyanSprite.png")
green = pygame.image.load("GreenSprite.png")
orange = pygame.image.load("OrangeSprite.png")
pink = pygame.image.load("PinkSprite.png")
red = pygame.image.load("RedSprite.png")
yellow = pygame.image.load("YellowSprite.png")
direction = 1
clock = pygame.time.Clock()
player_rect_blue = blue.get_rect(midbottom = (80,100))
player_rect_cyan = cyan.get_rect(midbottom = (80,200))
player_rect_green = green.get_rect(midbottom = (80,300))
player_rect_orange = orange.get_rect(midbottom = (80,400))
player_rect_pink = pink.get_rect(midbottom = (80,500))
player_rect_red = red.get_rect(midbottom = (80,600))
player_rect_yellow = yellow.get_rect(midbottom = (80,700))

#definition for the font
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

#play screen
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(blue, player_rect_blue)
        SCREEN.blit(cyan, player_rect_cyan)
        SCREEN.blit(green, player_rect_green)
        SCREEN.blit(orange, player_rect_orange)
        SCREEN.blit(pink, player_rect_pink)
        SCREEN.blit(red, player_rect_red)
        SCREEN.blit(yellow, player_rect_yellow)

        speed_x = 2
        speed_y = 1
        direction = 1
        #implementing random movement
        if player_rect_blue.right <=80 or player_rect_blue.right >= 1260:
            direction *= -1
            speed_x = random.randint(0,2) * direction
            speed_y = random.randint(0,2) * direction

            if speed_x==0 and speed_y ==0:
                speed_x = random.randint(2, 4) * direction
                speed_y = random.randint(2, 4) * direction
        if player_rect_blue.top <= 100 or player_rect_blue.bottom >= 700:
            direction *= -1
            speed_x = random.randint(0, 4) * direction
            speed_y = random.randint(0, 4) * direction
 
        # Changing the value if speed_x
        # and speed_y both are zero
            if speed_x == 0 and speed_y == 0:
                speed_x = random.randint(2, 8) * direction
                speed_y = random.randint(2, 8) * direction
        player_rect_blue.left += speed_x
        player_rect_blue.top += speed_y

        player_rect_cyan.x +=1
        if player_rect_cyan.right == 1000:
            player_rect_cyan.x -=2
        player_rect_green.x +=1
        player_rect_orange.x +=1
        player_rect_pink.x +=1
        player_rect_red.x +=1
        player_rect_yellow.x +=1


        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)

        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#option screen    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        music_paused = False
        SCREEN.fill("white")

        OPTIONS_SOUND = Button(image = None, pos=(1000,60),
                            text_input="SOUND?", font= get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK = Button(image=None, pos=(55, 690), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_SOUND.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_SOUND.update(SCREEN)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_SOUND.checkForInput(OPTIONS_MOUSE_POS):
                    music_paused = not music_paused
                    if music_paused:
                        pygame.mixer.music.pause()
                        main_menu()
                    else:
                        pygame.mixer.music.unpause()
                        main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#main menu screen
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("TEAM ORANGE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Black")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

