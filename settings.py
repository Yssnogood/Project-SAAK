import pygame as pg

#paramètres allant êre utilisés dans le fonctionnement du jeu à divers endroits et temps

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1260   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 720  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Projet SAAK "
TITLESCREEN = "background_title_screen.PNG"

BUTTONREC0 = 'buttonLong_beige.PNG'
BUTTONREC1 = 'buttonLong_beige_pressed.PNG'
PANEL = 'panel_beige.PNG'

BGCOLOR = LIGHTGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


#mob img

MOB_IMG = 'b0.PNG'
MOB_SPEED = 200
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)


#pnj settings

PNJ_IMG = 'b0.png'

# player settings


CHARCHOOSE = 0
CHARIMG = 'img/char/char00'

PLAYER_NAME = "Edalf"

PLAYER_SPEED = 300
PLAYER_IMG = 'b0.PNG'

PLAYER_IMG_DOWN0 = 'b0.PNG'
PLAYER_IMG_DOWN1 = 'b1.PNG'
PLAYER_IMG_DOWN2 = 'b0.PNG'
PLAYER_IMG_DOWN3 = 'b2.PNG'

PLAYER_IMG_LEFT0 = 'g0.PNG'
PLAYER_IMG_LEFT1 = 'g1.PNG'
PLAYER_IMG_LEFT2 = 'g0.PNG'
PLAYER_IMG_LEFT3 = 'g2.PNG'

PLAYER_IMG_RIGHT0 = 'd0.PNG'
PLAYER_IMG_RIGHT1 = 'd1.PNG'
PLAYER_IMG_RIGHT2 = 'd0.PNG'
PLAYER_IMG_RIGHT3 = 'd2.PNG'

PLAYER_IMG_UP0 = 'h0.PNG'
PLAYER_IMG_UP1 = 'h1.PNG'
PLAYER_IMG_UP2 = 'h0.PNG'
PLAYER_IMG_UP3 = 'h2.PNG'
