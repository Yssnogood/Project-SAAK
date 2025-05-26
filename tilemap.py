import pygame as pg
from os import path
from settings import *

class Map:
    def __init__(self, filename):
        #class permettant de lire un fichier .txt et de le convertir en liste
        self.data = []

        with open(filename, 'rt') as f:
            for line in f:
                #la boucle parcourt le fichier
                #puis on ajoute les caractères dans une liste
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE



class Camera:
    def __init__(self, width, height):
        #on crée un rectangle qui va suivre les déplacements d'une entité
        self.camera = pg.Rect(0,0, width,height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = - target.rect.y + int(HEIGHT /2)

        #limit scrol
        x = min(0 , x) #gauche
        y = min(0, y) # haut
        x = max(-(self.width - WIDTH),x)
        y = max(-(self.height - HEIGHT),y)
        self.camera = pg.Rect(x,y, self.width, self.height)
