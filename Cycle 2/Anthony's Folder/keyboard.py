import pygame
from pygame.locals import *

# Dictionary containing the names associated with the key constants defined
# by SDL.

inverse_keys = \
    {
        KMOD_ALT: "Alt",
        KMOD_CAPS: "Caps",
        KMOD_CTRL: "Ctrl",
        KMOD_LALT: "Left Alt",
        KMOD_LCTRL: "Left Ctrl",
        KMOD_LMETA: "Left Meta",
        KMOD_LSHIFT: "Left Shift",
        KMOD_META: "Meta",
        KMOD_MODE: "Mode",
        KMOD_NONE: "None",
        KMOD_NUM: "Num Lock",
        KMOD_RALT: "Right Alt",
        KMOD_RCTRL: "Right Ctrl",
        KMOD_RMETA: "Right Meta",
        KMOD_RSHIFT: "Right Shift",
        KMOD_SHIFT: "Shift",
        K_0: "0",
        K_1: "1",
        K_2: "2",
        K_3: "3",
        K_4: "4",
        K_5: "5",
        K_6: "6",
        K_7: "7",
        K_8: "8",
        K_9: "9",
        K_AMPERSAND: "&",
        K_ASTERISK: "*",
        K_AT: "@",
        K_BACKQUOTE: "`",
        K_BACKSLASH: "\\",
        K_BACKSPACE: "Backspace",
        K_BREAK: "Break",
        K_CAPSLOCK: "Caps Lock",
        K_CARET: "Caret",
        K_CLEAR: "Clear",
        K_COLON: ":",
        K_COMMA: ",",
        K_DELETE: "Delete",
        K_DOLLAR: "$",
        K_DOWN: "Down",
        K_END: "End",
        K_EQUALS: "=",
        K_ESCAPE: "Escape",
        K_EURO: "Euro",
        K_EXCLAIM: "!",
        K_F1: "F1",
        K_F10: "F10",
        K_F11: "F11",
        K_F12: "F12",
        K_F13: "F13",
        K_F14: "F14",
        K_F15: "F15",
        K_F2: "F2",
        K_F3: "F3",
        K_F4: "F4",
        K_F5: "F5",
        K_F6: "F6",
        K_F7: "F7",
        K_F8: "F8",
        K_F9: "F9",
        #K_FIRST: "First",
        K_GREATER: ">",
        K_HASH: "#",
        K_HELP: "Help",
        K_HOME: "Home",
        K_INSERT: "Insert",
        K_KP0: "Keypad 0",
        K_KP1: "Keypad 1",
        K_KP2: "Keypad 2",
        K_KP3: "Keypad 3",
        K_KP4: "Keypad 4",
        K_KP5: "Keypad 5",
        K_KP6: "Keypad 6",
        K_KP7: "Keypad 7",
        K_KP8: "Keypad 8",
        K_KP9: "Keypad 9",
        K_KP_DIVIDE: "Keypad /",
        K_KP_ENTER: "Keypad Enter",
        K_KP_EQUALS: "Keypad =",
        K_KP_MINUS: "Keypad -",
        K_KP_MULTIPLY: "Keypad *",
        K_KP_PERIOD: "Keypad .",
        K_KP_PLUS: "Keypad +",
        K_LALT: "Left Alt",
        #K_LAST: "Last",
        K_LCTRL: "Left Ctrl",
        K_LEFT: "Left",
        K_LEFTBRACKET: "(",
        K_LEFTPAREN: "(",
        K_LESS: "<",
        K_LMETA: "Left Meta",
        K_LSHIFT: "Left Shift",
        K_LSUPER: "Left Super",
        K_MENU: "Menu",
        K_MINUS: "-",
        K_MODE: "Mode",
        K_NUMLOCK: "Num Lock",
        K_PAGEDOWN: "Page Down",
        K_PAGEUP: "Page Up",
        K_PAUSE: "Pause",
        K_PERIOD: ".",
        K_PLUS: "+",
        K_POWER: "^",
        K_PRINT: "Print",
        K_QUESTION: "?",
        K_QUOTE: "'",
        K_QUOTEDBL: '"',
        K_RALT: "Right Alt",
        K_RCTRL: "Right Ctrl",
        K_RETURN: "Return",
        K_RIGHT: "Right",
        K_RIGHTBRACKET: ")",
        K_RIGHTPAREN: ")",
        K_RMETA: "Right Meta",
        K_RSHIFT: "Right Shift",
        K_RSUPER: "Right Super",
        K_SCROLLOCK: "Scroll Lock",
        K_SEMICOLON: ";",
        K_SLASH: "/",
        K_SPACE: "Space",
        K_SYSREQ: "Sys Req",
        K_TAB: "Tab",
        K_UNDERSCORE: "_",
        K_UNKNOWN: "Unknown",
        K_UP: "Up",
        K_a: "a",
        K_b: "b",
        K_c: "c",
        K_d: "d",
        K_e: "e",
        K_f: "f",
        K_g: "g",
        K_h: "h",
        K_i: "i",
        K_j: "j",
        K_k: "k",
        K_l: "l",
        K_m: "m",
        K_n: "n",
        K_o: "o",
        K_p: "p",
        K_q: "q",
        K_r: "r",
        K_s: "s",
        K_t: "t",
        K_u: "u",
        K_v: "v",
        K_w: "w",
        K_x: "x",
        K_y: "y",
        K_z: "z"
    }
