import pygame
from settings import *
from os import path


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
BROWN = (128,0,0)
TURQUOISE = (0,206,209)
MAGENTA = (255,0,255)
ROSE =(249,66,158)
GREY = (211,211,211) 
SHY_BLUE = (51,102,255)
VIOLET = (153,0,204)

WINDOW_SIZE = [WIDTH, HEIGHT]
display_width,display_height = WINDOW_SIZE
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Projet SAAK")

gameDisplay = pygame.display.set_mode((WINDOW_SIZE[0],WINDOW_SIZE[1]))


def text_objects(text, font):
    ##Fonction qui s'occupe de mettre du texte
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    ##Fonction pour afficher le texte dans une fenetre déjà existante
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()

def button(msg,x,y,w,h,ic,ac,sort,DicEnnemi):
    ## msg -> message
    ## x, y -> position dans la fenetre
    ## w, h -> longueur et largeur
    ##ic, ac -> couleur lors du non survol de la souris puis du surval de la souris
    ##action -> cheat code pour associer une fonction avec le bouton
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    ic = pg.transform.scale(ic,(w,h))
    ac = pg.transform.scale(ac,(w,h))
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        gameDisplay.blit(ac,(x,y))

        if click[0] == 1:
            sort(DicEnnemi)
    else:
        gameDisplay.blit(ic,(x,y))

    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def buttonok(msg,x,y,w,h,ic,ac):
    ## msg -> message
    ## x, y -> position dans la fenetre
    ## w, h -> longueur et largeur
    ##ic, ac -> couleur lors du non survol de la souris puis du surval de la souris
    ##action -> cheat code pour associer une fonction avec le bouton
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    ic = pg.transform.scale(ic,(w,h))
    ac = pg.transform.scale(ac,(w,h))
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        gameDisplay.blit(ac,(x,y))

        if click[0] == 1:
            return True
    else:
        gameDisplay.blit(ic,(x,y))

    smallText = pygame.font.Font("freesansbold.ttf",15)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)




