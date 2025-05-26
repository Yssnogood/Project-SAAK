import pygame as pg
from settings import *
from time import *
vec = pg.math.Vector2



def collide_with_walls(sprite,group,dir):

        # cette fonction sert à vérifié les collisions entre deux sprites
        # si un sprite rentre en collision dans un autre, sa vitesse devient égale à 0
        # ça l'empêche de bouger et donc de traverser l'autre image
        
        if dir =='x':
            hits = pg.sprite.spritecollide(sprite,group,False)
            if hits:
                if sprite.vel.x > 0 :
                    sprite.pos.x = hits[0].rect.left - sprite.rect.width
                if sprite.vel.x < 0:
                    sprite.pos.x = hits[0].rect.right
                sprite.vel.x = 0
                sprite.rect.x = sprite.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(sprite,group,False)
            if hits:
                if sprite.vel.y > 0 :
                    sprite.pos.y = hits[0].rect.top - sprite.rect.height
                if sprite.vel.y < 0:
                    sprite.pos.y = hits[0].rect.bottom
                sprite.vel.y = 0
                sprite.rect.y = sprite.pos.y





class Player(pg.sprite.Sprite):
        #on récupere le jeu pour l'afficher sur un écran, des coordonnées pour l'afficher à un endroit
        #et le nom du joueur sélectionné à l'écran de choix des perso
    def __init__(self, game, x, y, name = PLAYER_NAME):
        #initialisation des variables
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        #on charge les images pour le joueur qui vont servir pour l'animation
        self.image = game.player_img
        self.imageOld = self.image
        
        self.imageDown = game.player_img_down
        self.imageUp = game.player_img_up
        self.imageLeft = game.player_img_left
        self.imageRight = game.player_img_right

        #on créer un rectangle qui va correspondre à la corpulence du joueur 
        self.rect = self.image.get_rect()
        self.vel = vec(0,0)
        self.pos = vec(x,y)*TILESIZE
        
        self.walkCount = 0


        # variables pour gérer l'équipement du joueur, pas utilisées dans cette version du jeu
        self.gear = ["*","*"]
        self.inventory=[]

        #on charge le nom, les noms des sorts du personnage et ses statistiques ici
        self.name = name
        if self.name == "Edalf":
                
                # 0-> noir sert à remplir la fenetre, 1->potion, 2-> hp, 3-> energie, 4 -> points d'attaque en plus, 5-> mana, 6-> intel(sort plus puissant)
                # 7-> pts d'actions permettent, 8 à 12 compris bonus, 13 à 15 compris variables utilitaires dans la grille
                self.stats = {"0":0,"1":0,"2":50,"3":10,"4":10,"5":30,"6":20,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                self.sort_name =["Flammèche","Boule de feu","Explosion pyrotechnique"]
                
        if self.name ==  "Soxi" :
                
                self.stats = {"0":0,"1":50,"2":50,"3":25,"4":20,"5":10,"6":10,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                self.sort_name =["Frappe","Frappe ciblée","Frappe héroïque"]

    def sortUn(self,DicEnnemi):
        #Premiers sort
        #les sorts utilisent des ressources pour faire des dégats
        sleep(0.3)
        if self.name=="Soxi":
            if self.stats["3"] > 0:
                self.stats["3"] -=1
                DicEnnemi["2"] -= self.stats["4"]
        else:
            if self.stats["5"] > 0:
                self.stats["5"] -=1
                DicEnnemi["2"] -= self.stats["6"]
        
            
    def sortDeux(self,DicEnnemi):
        sleep(0.3)
        if self.name == "Soxi":    
            if self.stats["3"] >= 5 and self.stats["7"] >= 1:
                self.stats["3"] -= 5
                self.stats["7"] -= 1
                DicEnnemi["2"] -= 7
        else:
            if self.stats["5"] >= 5 and self.stats["7"] >= 1:
                self.stats["5"] -= 5
                self.stats["7"] -= 1
                DicEnnemi["2"] -= 7

    def sortTrois(self,DicEnnemi):
        sleep(0.3)
        if self.name == "Soxi":
            if self.stats["7"] >= 4:
                self.stats["7"] -= 4
                DicEnnemi["2"] -= 15
        else:
            if self.stats["7"] >= 4:
                self.stats["7"] -= 4
                DicEnnemi["2"] -= 15
            


        
        
    def seeInventory(self):
        #methode pour voir l'inventaire du personnage
        #n'est pas mise dans le jeu 
        seeInventory = []
        for i in range(0,len(self.inventory)):
            seeInventory.append(self.inventory[i].type + " " + self.inventory[i].name)
        print(seeInventory)

    def seeGear(self):
        #methode pour voir l'équipement mis du personnage
        #n'est pas mise dans le jeu 
        seeGear = []
        if self.gear[0] =="*" and self.gear[1] == "*":
            print(self.gear)
            
        if self.gear[0] == "*" and self.gear[1] != "*":
            print(self.gear[0], self.gear[1].type,"",self.gear[1].name)
            
        if self.gear[1] == "*" and self.gear[0] != "*":
            print(self.gear[0].type,"",self.gear[0].name,self.gear[1])
            
        if self.gear[0]!="*" and self.gear[1] !="*":
            for i in range(0,len(self.gear)):
                seeGear.append(self.gear[i].type + " " + self.gear[i].name)               
            print(seeGear)
                

    def unuseGear(self, slot):
        #methode pour déséquiper un équipement du personnage
        if slot <= len(self.gear) and slot >=0:
            self.inventory.append(self.gear[slot])
            self.gear[slot] = "*"
        
    
    def useInventory(self, numObjetL):
        #permets d'utiliser un objet de l'inventaire
        if numObjetL <= len(self.inventory) and numObjetL >= 0:
            if self.inventory[numObjetL].type == "potion":
                self.inventory[numObjetL].utiliser(self.joueur)
                del self.inventory[numObjetL]
                return 0
                
            if self.inventory[numObjetL].type == "Armure" and self.gear[0] != "*":  
                self.inventory.append(self.gear[0])
                self.gear[0].desequipe(self.joueur)
                self.gear[0] = self.inventory[numObjetL]
                self.inventory[numObjetL].equipe(self.joueur)
                del self.inventory[numObjetL]
                return 0
                    
            if self.inventory[numObjetL].type == "Arme" and self.gear[1] != "*":
                seself.inventory.append(self.gear[1])
                self.gear[1].desequipe(self.joueur)
                self.gear[1] = self.inventory[numObjetL]
                self.inventory[numObjetL].equipe(self.joueur)
                del self.inventory[numObjetL]
                return 0
                    
            if self.inventory[numObjetL].type == "Armure" and self.gear[0] == "*":
                self.gear[0] = self.inventory[numObjetL]
                self.inventory[numObjetL].equipe(self.joueur)
                del self.inventory[numObjetL]
                return 0
                    
            if self.inventory[numObjetL].type == "Arme" and self.gear[1] == "*":
                self.gear[1] = self.inventory[numObjetL]
                self.inventory[numObjetL].equipe(self.joueur)
                del self.inventory[numObjetL]
                return 0
        else:
            print("Il n'y a pas d'item à cet emplacement")
            return 0
        



    def changement_zone(self):
        #methode utilisélors de la collision entre le joueur et le sprite du changement de zone
        #si le joueur va vers la droite cela veut dire que le joueur avance, on charge donc la prochaine zone
        # si le joueur va vers la gauche, il recule, on charge la précédente
        if self.vel.x > 0 :
            hits = pg.sprite.spritecollide(self,self.game.changement,False)
            if hits :
                self.game.map_sel += 1 
        if self.vel.x < 0 :
            hits = pg.sprite.spritecollide(self,self.game.changement,False)
            if hits :
                self.game.map_sel -= 1 
 
    def get_keys(self):
        # on utilise le vecteur de velocite, vitesse
        # en fonction de la touche appuyée, le vecteur va changer, il sera plus tard ajouter à la position du joueur
        self.vel = vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_q]:
            
            self.vel.x = -PLAYER_SPEED

            #self.walkCount ne sert qu'à parcourir une liste de quatre image
            #le compteur ne doit pas dépasser 60 car il dépassera la liste d'image, voir plus bas pourquoi
            if self.walkCount +1 > 60 :
                self.walkCount = 0

            #on affiche ici l'image qui va être affiché à l'écran en tant que joueur
            #l'application tourne à 60 image par seconde, cad qu'elle fait 60 boucles en une seconde
            #pour avoir une animation fluide avec quatre image, l'animation doit se faire en quatre secondes  
            #pour afficher la bonne image on a alors juste à afficher l'occurence de l'image dans la liste en fonction du compteur divisé par 15
            #( par 15 car on a 4 images et le jeu est à 60 fps, 60 / 4 = 15, ça montre combien de boucles du jeu le joueur doit conserver son image )
            self.image = self.imageLeft[self.walkCount//15]
            self.walkCount += 1
                
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
            if self.walkCount +1 > 60 :
                self.walkCount = 0
            self.image = self.imageRight[self.walkCount//15]
            self.walkCount += 1
            
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            if self.walkCount + 1 > 60:
                self.walkCount = 0
            self.image = self.imageDown[self.walkCount//15]
            self.walkCount += 1
            
        elif keys[pg.K_UP] or keys[pg.K_z]:
            self.vel.y = -PLAYER_SPEED
            
            if self.walkCount +1 > 60 :
                self.walkCount = 0
            self.image = self.imageUp[self.walkCount//15]
            self.walkCount += 1
            
        else:
            self.image = self.imageOld
            
        
        

    def update(self):
        # methode appellée dans la class game pour mettre à jour toutes les methodes de la class player
        self.get_keys()
        self.pos += self.vel * self.game.dt
        self.rect.x = self.pos.x
        collide_with_walls(self,self.game.walls,'x')
        self.rect.y = self.pos.y
        collide_with_walls(self, self.game.walls,'y')
        self.changement_zone()




class Pnj(pg.sprite.Sprite):
        #pas utilisée dans cette version du jeu
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.pnjs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.pnj_img
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILESIZE
        self.rect.center = self.pos


class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.rot = 0

    def update(self):
        #ici on a un code pour permettre au monstre d'aller jusqu'au joueur
        #retirer car hitbox du monstre + déplacement du monstre pas cool
        pass
        #self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        #self.rect = self.image.get_rect()
        #self.rect.center = self.pos
        #self.acc = vec(MOB_SPEED, 0).rotate(-self.rot)
        #self.acc += self.vel * -1
        #self.vel += self.acc * self.game.dt
        #self.pos += self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2
        #self.hit_rect.centerx = self.pos.x
        #collide_with_walls(self, self.game.walls, 'x')
        #self.hit_rect.centery = self.pos.y
        #collide_with_walls(self, self.game.walls, 'y')
        #self.rect.center = self.hit_rect.center
        
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y,img):
        #class des murs, ne sert qu'à afficher une image de mur à un emplacement précis
        #les collisions sont gérer avec la fonction collide_with_walls
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #TILESIZE -> correspond aux dimensions de la grille ici 64
        self.image = pg.transform.scale(img,(TILESIZE, TILESIZE))
        #self.image.fill(self.image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        
class Changement_zone(pg.sprite.Sprite):
    def __init__(self, game, x, y ,img):
        #même chose que pour le mur
        #collision gérer en dehors de la class
        self.groups = game.all_sprites, game.changement
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = pg.transform.scale(img,(TILESIZE, TILESIZE))
        
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
                


