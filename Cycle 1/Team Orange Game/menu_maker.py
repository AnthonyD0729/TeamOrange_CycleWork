import pygame
import pygame_menu

def menu_maker():
    def set_difficulty(value, difficulty):
        pass
    def start_the_game():
        pass
    menu = pygame_menu.Menu("Welcome", 1280,720, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.selector('Difficulty: (1=Easy, 2=Medium, 3=Hard', [('Hard',1), ('Easy',1), ('Medium', 2)], onchange=set_difficulty)

