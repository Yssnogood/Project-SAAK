import pygame as pg
import sys
from os import path

from random import *
from settings import *
from sprites import *
from tilemap import*

import threading
from Fonctions_Generation import *
from Fonctions_Scoring import *
from Fonctions_Pygame import *
from Fonctions_Sort import *
from Fonctions_IA import *
from Fonction_Jeu import *
import pygame
from random import *
from time import *

joueurname = "Edalf"
pg.init()


gameDisplay =pg.display.set_mode((WIDTH,HEIGHT))
pygame.mixer.music.set_volume(0.5)
pg.mixer.music.load("intro.wav")
pg.mixer.music.play(-1)

def text_objects(text, font):
    #sert juste à placer un message dans une suface
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    #sert juste à afficher un message
    largeText = pg.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pg.display.update()
    time.sleep(2)

    game_loop()
    
    
def button(msg,x,y,w,h,ic,ac,action=None):
    # on récupére la position de la souris
    #et on regarde si les boutons sont pressés
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    #adaptation des dimensions des images
    ic = pg.transform.scale(ic,(w,h))
    ac = pg.transform.scale(ac,(w,h))

    #si la souris rentre dans les coordonées du bouton
    #on affiche une image si elle n'y est pas c'est une autre image
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        gameDisplay.blit(ac,(x,y))

        if click[0] == 1 and action != None:
            action()
    else:
        gameDisplay.blit(ic,(x,y))

    smallText = pg.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect) 


def buttonChar(msg,x,y,w,h,ic,ac,CHARCHOOSE=0):
    global CHARIMG, SWITCH, PLAYER_NAME

    # SWITCH ne sert qu'à afficher en continue une image
    # on récupére la position de la souris et on regarde si les boutons sont pressés
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    #adaptation des dimensions des images
    ic = pg.transform.scale(ic,(w,h))
    ac = pg.transform.scale(ac,(w,h))

    #chargement des ressources
    font = pg.font.Font("freesansbold.ttf",20)
    question = font.render("Voulez-vous jouer en tant que "+PLAYER_NAME+" ?", 1,(0,0,0))

    game_folder = path.dirname(__file__)
    button_folder = path.join(game_folder,'img/ui/')

    #chargement des variables qui vont être utilisées en fonction du bouton posé
    #bouton CHARCHOOSE ==0 correspond à Edalf CHARCHOOSE == 1 à Soxi
    if CHARCHOOSE == 0:
        char_folder = path.join(game_folder,'img/char/char00')
        stats = {"0":0,"1":0,"2":50,"3":10,"4":10,"5":30,"6":20,"7":10}
    if CHARCHOOSE == 1:
        char_folder = path.join(game_folder,'img/char/char01')
        stats = {"0":0,"1":50,"2":50,"3":25,"4":20,"5":10,"6":10,"7":10}


    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        gameDisplay.blit(ac,(x,y))
        
        gameDisplay.blit(pg.transform.scale(pg.image.load(
            path.join(button_folder, BUTTONREC0)),(500,200)),(100,500))
        
        gameDisplay.blit(pg.transform.scale(pg.image.load(
            path.join(button_folder, PANEL)),(100,100)),(110,400))
        
        gameDisplay.blit(pg.transform.scale(pg.image.load(
            path.join(char_folder, PLAYER_IMG)),(90,90)),(115,405))

        textRouge = font.render("Vie: "+str(stats["2"]), True, (0,0,0))
        screen.blit(textRouge,(120,540))

        textJaune = font.render("Energie: "+str(stats["3"]), True, (0,0,0))
        screen.blit(textJaune,(220,540))

        textOrange = font.render("Attaque bonus: "+str(stats["4"]), True, (0,0,0))
        screen.blit(textOrange,(350,540))

        textMarron = font.render("Mana: "+str(stats["5"]), True, (0,0,0))
        screen.blit(textMarron,(120,590))

        textBleu = font.render("Intelligence: "+str(stats["6"]), True, (0,0,0))
        screen.blit(textBleu,(220,590))

        #Si l'on clique sur le bouton cela va charger les informations dans des variables globals qui vont être utilisées dans
        #la class Player pour gèrer les stats et l'affichage du personnage
        if click[0] == 1:
            SWITCH = True
            if CHARCHOOSE==0:
                CHARIMG = 'img/char/char00'
                PLAYER_NAME = "Edalf"
            if CHARCHOOSE==1:
                CHARIMG = 'img/char/char01'
                PLAYER_NAME = "Soxi"
            

    else:
        # si rien ne se passe, on montre juste l'image du bouton au repos
        gameDisplay.blit(ic,(x,y))
    # si switch devient vrai ( de base il est faux ) alors on affiche une pop-up sur l'écran de l'écran
    
    if SWITCH:
        gameDisplay.blit(pg.transform.scale(pg.image.load(
            path.join(button_folder, BUTTONREC0)),(500,200)),(375,250))
        gameDisplay.blit(question,(450,290))
        
        button("Oui",480,350,80,60,pg.image.load(
            path.join(button_folder, BUTTONREC0)),pg.image.load(
            path.join(button_folder, BUTTONREC1)),jouer)
        
        button("Non",680,350,80,60,pg.image.load(
            path.join(button_folder, BUTTONREC0)),pg.image.load(
            path.join(button_folder, BUTTONREC1)),choixPerso)
    

    smallText = pg.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect) 

  
def jouer():
    g = Game()
    pygame.mixer.music.stop()
    pg.mixer.music.load("wander.wav")
    pg.mixer.music.play(-1)
    while True:
        g.new()
        g.run()



def menu():

    pg.display.set_caption('Projet SAAK ')
    clock = pg.time.Clock()
    

    # chargement des ressources

    game_folder = path.dirname(__file__)

    back_folder = path.join(game_folder,'img/background/')
    back_img =  pg.transform.scale(pg.image.load(path.join(back_folder, TITLESCREEN)),(WIDTH,HEIGHT))

    button_folder = path.join(game_folder,'img/ui/')
    button_img = [pg.image.load(path.join(button_folder, BUTTONREC0)),pg.image.load(path.join(button_folder, BUTTONREC1))]
    fond_button = [pg.image.load(path.join(button_folder, BUTTONREC0)),pg.image.load(path.join(button_folder, 'buttonLong_grey.PNG'))]
    
    font = pg.font.SysFont("comicsansms", 20)

    loop = True

    # boucle pour afficher l'écran de menu
    gameDisplay.blit(back_img,(0,0))
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = True
        

        button("Projet SAAK",960,60,250,80,button_img[0],button_img[0])
        
        button("Jouer",980,200,200,60,button_img[0],button_img[1],choixPerso)
        button("Comment jouer",980,300,200,60,button_img[0],button_img[1])
        button("Quitter",980,400,200,60,button_img[0],button_img[1],quit)

        pg.display.update()
        clock.tick(60)
    

def choixPerso():
    global SWITCH
    SWITCH = False

    #creation de la fenetre
    pg.display.set_caption('Projet SAAK ')
    clock = pg.time.Clock()

    #chargement des ressources
    game_folder = path.dirname(__file__)
    
    back_folder = path.join(game_folder,'img/background/')
    back_img =  pg.transform.scale(pg.image.load(path.join(back_folder, TITLESCREEN)),(WIDTH,HEIGHT))

    button_folder = path.join(game_folder,'img/ui/')
    button_img = [pg.image.load(path.join(button_folder, BUTTONREC0)),pg.image.load(path.join(button_folder, BUTTONREC1))]
    
    font = pg.font.SysFont("comicsansms", 20)

    loop = True

    
    gameDisplay.blit(back_img,(0,0))
    # boucle pour afficher l'écran de choix de perso
    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                loop = True
        

        button("Projet SAAK",960,60,250,80,button_img[0],button_img[0])
        
        buttonChar("Edalf",980,200,200,60,button_img[0],button_img[1],0)
        buttonChar("Soxi",980,300,200,60,button_img[0],button_img[1],1)
        
        button("Retour",980,500,200,60,button_img[0],button_img[1],menu)

        pg.display.update()
        clock.tick(60)






class Game:
    def __init__(self):
        # init de pygame + mise en place des dimensions de la fenetre de jeu
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):

        # chargement des ressources
        
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,CHARIMG)
        img_folder_pnj = path.join(game_folder,'img/pnj')
        img_folder_mob = path.join(game_folder,'img/mobs')
        map_folder = path.join(game_folder,'maps')
        self.map = [Map(path.join(map_folder,'mapA1.txt')),Map(path.join(map_folder,'mapA2.txt')),Map(path.join(map_folder,'mapA3.txt'))]
        self.map_sel = 0
        self.map_sel_old = 0
        
        self.pnj_img = pg.transform.scale(pg.image.load(path.join(img_folder_pnj, PNJ_IMG)),(40,50))

        self.mob_img = pg.transform.scale(pg.image.load(path.join(img_folder_mob,MOB_IMG)),(40,50))

        self.player_img = pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG)),(40,50))
        self.player_img_down = [pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_DOWN0)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_DOWN1)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_DOWN2)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_DOWN3)),(40,50))]
        self.player_img_up = [pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_UP0)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_UP1)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_UP2)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_UP3)),(40,50))]
        self.player_img_left = [pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_LEFT0)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_LEFT1)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_LEFT2)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_LEFT3)),(40,50))]
        self.player_img_right = [pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_RIGHT0)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_RIGHT1)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_RIGHT2)),(40,50)),pg.transform.scale(pg.image.load(path.join(img_folder, PLAYER_IMG_RIGHT3)),(40,50))]

    def new(self):
        #initialisation des variables pour pouvoir les afficher plus tard
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.pnjs = pg.sprite.Group()
        self.changement = pg.sprite.Group()

        # chargement des ressources

        game_folder = path.dirname(__file__)
        
        img_folder_background = path.join(game_folder,'img/background')

        img_wall = pg.image.load(path.join(img_folder_background,"Bricks.jpg"))
        img_porte_bas = pg.image.load(path.join(img_folder_background,"esca_down.jpg"))
        img_porte_haut = pg.image.load(path.join(img_folder_background,"esca_up.png"))
        img_sol = pg.image.load(path.join(img_folder_background,"Cavern_wall.jpg"))

        # on créer les classes des sprites et images
        
        for row, tiles in enumerate(self.map[self.map_sel].data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row,img_wall)
                if tile == 'C':
                    Pnj(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == '4':
                    Wall(self,col,row,img_porte_bas)
                if tile == '2':
                    Changement_zone(self, col, row, img_porte_bas)
                if tile == '3':
                    Changement_zone(self, col, row,img_porte_haut)
                if tile== '0':
                    Wall(self,col,row,img_sol)
                if tile == 'P':
                    self.player = Player(self, col, row, PLAYER_NAME)

        self.camera= Camera(self.map[self.map_sel].width, self.map[self.map_sel].height)
        self.encounters = self.player.walkCount

    def loadMap(self, switch):
        #initialisation des variables pour pouvoir les afficher plus tard
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.pnjs = pg.sprite.Group()
        self.changement = pg.sprite.Group()

        # variables servant à mémoriser l'emplacement des escaliers dans la grille
        # sert pour le placement du joueur lors des changements de carte
        
        self.cgt_entree_gauche = [0, 0]
        self.cgt_entree_droit = [0, 0]

        # chargement des ressources
        
        game_folder = path.dirname(__file__)
        
        img_folder_background = path.join(game_folder,'img/background')

        img_wall = pg.image.load(path.join(img_folder_background,"Bricks.jpg"))
        img_porte_bas = pg.image.load(path.join(img_folder_background,"esca_down.jpg"))
        img_porte_haut = pg.image.load(path.join(img_folder_background,"esca_up.png"))
        img_sol = pg.image.load(path.join(img_folder_background,"Cavern_wall.jpg"))

        # on créer les classes des sprites et images
        
        for row, tiles in enumerate(self.map[self.map_sel].data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row,img_wall)
                if tile == 'C':
                    Pnj(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == '4':
                    Wall(self,col,row,img_porte_bas)
                if tile == '2':
                    self.cgt_entree_gauche[0] = col
                    self.cgt_entree_gauche[1] = row
                    Changement_zone(self, col, row, img_porte_bas)
                if tile == '3':
                    self.cgt_entree_droit[0] = col
                    self.cgt_entree_droit[1] = row
                    Changement_zone(self, col, row,img_porte_haut)
                if tile== '0':
                    Wall(self,col,row,img_sol)

        # on regarde l'argument donnée à la methode si c'est droit, 
        # ça veut dire que le jouer 'monte d'un étage' en prenant les escaliers montant
        # on le fait donc réaparaitre au prochain tableau à côté d'escaliers descendant
        # inversement pour la descende
                    
        if switch == 'droit' and self.cgt_entree_droit[1] != 0 :
            self.player = Player(self, self.cgt_entree_droit[0]-1, self.cgt_entree_droit[1], PLAYER_NAME)
            switch = 20
        if switch == 'gauche' and self.cgt_entree_gauche[1] != 0:
            self.player = Player(self, self.cgt_entree_gauche[0]+1,self.cgt_entree_gauche[1], PLAYER_NAME)
            switch = 20

        self.camera= Camera(self.map[self.map_sel].width, self.map[self.map_sel].height)
        
    def run(self):
        #boucle faisant tourner le jeu en mode exploration
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # partie où l'on met à jour les images / evenements
        self.all_sprites.update()
        self.camera.update(self.player)

        hits = pg.sprite.spritecollide(self.player, self.mobs, False)
        for hit in hits:
            hits = pg.sprite.spritecollide(self.player, self.mobs, True)
            pg.mixer.music.load("Fight.mp3")
            pg.mixer.music.play(-1)
            jeu(self.player)
            pg.mixer.music.load("wander.wav")
            pg.mixer.music.play(-1)

        #rencontre aléatoire, elle se met à jour aux nouveaux cycles d'animations
        # self.encounters permet d'éviter de se faire attraper dès le début
        if self.player.walkCount == 1 and self.encounters != self.player.walkCount :
            # on prend un nombre aleatoire entre 0 et 100 si le nombre est
            #inférieur ou égale à 8, on lance le combat
            if randint(0,100) <= 8:
                self.encounters = self.player.walkCount
                pg.mixer.music.load("Fight.mp3")
                pg.mixer.music.play(-1)
                jeu(self.player)
                pg.mixer.music.load("wander.wav")
                pg.mixer.music.play(-1)

        
        # ici, on regarde si la carte en cours d'affichage à changer
        #si elle a changé, on change d'affichage de carte et on passe à une nouvelle
        if self.map_sel != self.map_sel_old:
            if self.map_sel < self.map_sel_old:
                self.map_sel_old = self.map_sel
                #pour éviter d'avoir deux joueurs
                self.player.kill()
                self.loadMap('droit')
            if self.map_sel > self.map_sel_old:
                self.map_sel_old = self.map_sel
                self.player.kill()
                self.loadMap('gauche')
                
        

    def draw_grid(self):
        #permet juste d'afficher des carreaux sur l'écran et les fps
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image,
                             self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


menu()

