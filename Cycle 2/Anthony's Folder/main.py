__all__ = ['main']

import pygame, sys
import pygame_menu
from pygame_menu.examples import create_example_window
from util import load_save, reset_keys
from controls import Controls_Handler
from random import randrange
from typing import Tuple, Any, Optional, List
from sound import Sound
# Constants and global variables
ABOUT = [f'pygame-menu {pygame_menu.__version__}',
         f'Authors: Anthony Deyoe, Kevin Malone, Sal Mecca, and Isaac Otto',
         f'Email: teamorange_isnumber_1@aol.com']
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
DIFFICULTY = ['EASY']
BOT = ['BOT1']
FPS = 60
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background_music = pygame.mixer.music.load("images/music4.wav")
clock: Optional['pygame.time.Clock'] = None
main_menu: Optional['pygame_menu.Menu'] = None
surface: Optional['pygame.Surface'] = None
actions = {"Left": False, "Right": False, "Up": False, "Down": False, "Start": False, "Action1": False}
save = load_save()
control_handler = Controls_Handler(save)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
# DEFINTIONS ******************************************************

def drawbots():
    pass
def fullscreen_option():
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    fullscreen = False
    run = True

    while run:
        screen.fill("orange")
        f= pygame.font.Font('images/font.ttf', 70)
        FULL_TEXT =f.render('DO YOU WANT FULLSCREEN? PRESS F', True ,(255,255,255))
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

def change_difficulty(value: Tuple[Any, int], difficulty: str) -> None:
    """
    Change difficulty of the game.
    :param value: Tuple containing the data of the selected object
    :param difficulty: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
    DIFFICULTY[0] = difficulty

def change_bot(value: Tuple[Any, int], bot: str) -> None:
    """
    Change bot of the game.
    :param value: Tuple containing the data of the selected object
    :param bot: Optional parameter passed as argument to add_selector
    """
    selected, index = value
    print(f'Selected bot: "{selected}" ({bot}) at index {index}')
    BOT[0] = bot

def random_color() -> Tuple[int, int, int]:
    """
    Return a random color.
    :return: Color tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def play_function(difficulty: List, bot: List, font: 'pygame.font.Font', test: bool = False) -> None:
    """
    Main game function.
    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :param test: Test method, if ``True`` only one loop is allowed
    """
    assert isinstance(difficulty, list)
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    assert isinstance(bot, list)
    bot = bot[0]
    assert isinstance(bot, str)


    # Define globals
    global main_menu
    global clock

    if difficulty == 'EASY':
        f = font.render('Playing as a baby (easy)', True, (255, 255, 255))
    elif difficulty == 'MEDIUM':
        f = font.render('Playing as a kid (medium)', True, (255, 255, 255))
    elif difficulty == 'HARD':
        f = font.render('Playing as a champion (hard)', True, (255, 255, 255))
    else:
        raise ValueError(f'unknown difficulty {difficulty}')
    f_esc = font.render('Press ESC to open the menu', True, (255, 255, 255))


    if bot == 'BOT1':
        f = font.render('Sitting Duck (easy)', True, (255, 255, 255))
    elif bot == 'BOT2':
        f = font.render('Sniper (medium)', True, (255, 255, 255))
    elif bot == 'BOT3':
        f = font.render('Ultimate Weapon (hard)', True, (255, 255, 255))
    else:
        raise ValueError(f'unknown bot {bot}')
    f_esc = font.render('Press ESC to open the menu', True, (255, 255, 255))

    # Draw random color and text
    bg_color = 'orange'

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.full_reset()

    frame = 0

    while True:

        # noinspection PyUnresolvedReferences
        clock.tick(60)
        frame += 1

        # Application events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    main_menu.enable()

                    # Quit this function, then skip to loop of main-menu on line 223
                    return

        # Pass events to main_menu
        if main_menu.is_enabled():
            main_menu.update(events)

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, (int((WINDOW_SIZE[0] - f.get_width()) / 2),
                         int(WINDOW_SIZE[1] / 2 - f.get_height())))
        surface.blit(f_esc, (int((WINDOW_SIZE[0] - f_esc.get_width()) / 2),
                             int(WINDOW_SIZE[1] / 2 + f_esc.get_height())))
        pygame.display.flip()

        # If test returns
        if test and frame == 2:
            break


def main_background() -> None:
    """
    Function used by menus, draw on background while menu is active.
    """
    global surface
    surface.fill('orange')

def controlspage():
    running = True
    while running:
        surface.fill('orange')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
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
        canvas.fill('orange')
        control_handler.render(canvas)
        surface.blit(pygame.transform.scale(canvas, (SCREEN_WIDTH*2.7, SCREEN_HEIGHT*2.7)), (0,0))
        pygame.display.update()
        reset_keys(actions)

def main(test: bool = False) -> None:
    """
    Main program.
    :param test: Indicate function is being tested
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global clock
    global main_menu
    global surface

    # -------------------------------------------------------------------------
    # Create window
    # -------------------------------------------------------------------------
    surface = create_example_window('Team Orange Game', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Create menus: Play Menu
    # -------------------------------------------------------------------------
    play_menu = pygame_menu.Menu(
        theme= pygame_menu.themes.THEME_ORANGE.copy(),
        height=WINDOW_SIZE[1],
        title='Game Menu',
        width=WINDOW_SIZE[0]
    )

    submenu_theme = pygame_menu.themes.THEME_ORANGE.copy()
    submenu_theme.widget_font_size = 30
    play_options = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=submenu_theme,
        title='Options',
        width=WINDOW_SIZE[0]
    )
    play_options.add.button('Video', pygame_menu.events.BACK)
    play_options.add.button('Controls', controlspage)
    play_options.add.button('Sound', pygame.mixer.music.play(loops = -1))
    play_options.add.button('Fullscreen', fullscreen_option)
    play_options.add.button('Return to main menu', pygame_menu.events.RESET)

    play_menu.add.button('Start',  # When pressing return -> play(DIFFICULTY[0], font)
                         play_function,
                         DIFFICULTY,
                         BOT,
                         pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))

    play_menu.add.selector('Select difficulty ',
                           [('1 - Easy', 'EASY'),
                            ('2 - Medium', 'MEDIUM'),
                            ('3 - Hard', 'HARD')],
                           onchange=change_difficulty,
                           selector_id='select_difficulty')

    play_menu.add.selector('Select your Opponent: ',
                           [('1 - BOT1', 'BOT1'),
                            ('2 - BOT2', 'BOT2'),
                            ('3 - BOT3', 'BOT3')],
                           onchange=change_bot,
                           selector_id='select_bots')

    play_menu.add.button('Options', play_options)
    play_menu.add.button('Return to main menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus:About
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_ORANGE.copy()
    about_theme.widget_margin = (0, 0)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=about_theme,
        title='About',
        width=WINDOW_SIZE[0]
    )

    for m in ABOUT:
        about_menu.add.label(m, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)
    about_menu.add.vertical_margin(30)
    about_menu.add.button('Return to menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus: Main
    # -------------------------------------------------------------------------
    main_theme = pygame_menu.themes.THEME_ORANGE.copy()

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1],
        theme=main_theme,
        title='Main Menu',
        width=WINDOW_SIZE[0]
    )

    main_menu.add.button('Play', play_menu)
    main_menu.add.button('About', about_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Application events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        # Main menu
        if main_menu.is_enabled():
            main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()