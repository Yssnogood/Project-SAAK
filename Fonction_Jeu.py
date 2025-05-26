import threading
from Fonctions_Generation import *
from Fonctions_Scoring import *
from Fonctions_Pygame import *
from Fonctions_Sort import *
from Fonctions_IA import *
import pygame
from os import path
from random import *
from time import *
from multiprocessing import*

#Fonction créant une boucle infinie permettant de stoper le jeu ;
#ce dernier reprenant quand la boucle avec un autre clic de l'utilisateur
def Stop(DicScore):
    sleep(0.2)
    lock = threading.Lock()
    print("stop")
    with lock:
        if DicScore["15"] == 1:
            DicScore["15"] = 0
            print("unpaused")
        elif DicScore["15"] == 0:
            DicScore["15"] = 1
            print("paused")

#Fonction Principale de la phase de combat
def jeu(player):
    lock = threading.Lock()

    game_folder = path.dirname(__file__)
    back_folder = path.join(game_folder,'img/background/')
    back_img =  pg.transform.scale(pg.image.load(path.join(back_folder, TITLESCREEN)),(1260,720))
    button_folder = path.join(game_folder,'img/ui/')
    button_img = [pg.image.load(path.join(button_folder, BUTTONREC0)),pg.image.load(path.join(button_folder, BUTTONREC1))]
    fond_button = [pg.image.load(path.join(button_folder, 'buttonLong_grey.PNG')),pg.image.load(path.join(button_folder, 'buttonLong_grey_pressed.PNG'))]
    fond_jeu = pg.image.load(path.join(button_folder, 'panelInset_blue.PNG'))

    DicScoreSave = {"0":0,"1":0,"2":20,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
    player.stats["14"] = 0
    DicScore2 = {"0":0,"1":0,"2":10,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}

    n = 50
    WIDTH = 30
    HEIGHT = 30
    MARGIN = 5
    Grille = GenGrille(n)

    pygame.init()

    font = pygame.font.SysFont("comicsansms", 20)
    font_info = pygame.font.SysFont("comicsansms", 13)

    Grille = Randomisation(Grille,5,15,5,15)
    Grille = Randomisation(Grille,5,15,20,30)
    #Grille = Randomisation(Grille,5,15,35,45)

    clock = pygame.time.Clock()
    clock.tick(120)

    Grille = verifbalayage(Grille,player.stats,5,15,5,5)   
    #G1= threading.Thread(target=Play,args=(Grille,player.stats,5,15,5,15,DicScore2))
    G2= threading.Thread(target=Play,args=(Grille,DicScore2,5,15,20,30,player.stats))
    
    G2.daemon = True

    
    G2.start()
    #G1.start()

    PosTempo = []
    PosTempoValue = 0
    cpt = 0 
    fin = False
    switch = None

    screen.blit(back_img,(0,0))
    screen.blit(pg.transform.scale(fond_jeu,(385,385)),(160,160))
    screen.blit(pg.transform.scale(fond_jeu,(385,385)),(680,160))

    while fin is not True:
        Grille = verifbalayage(Grille,player.stats,5,15,5,15)
        pos = pygame.mouse.get_pos()
            #print("dans la boucle")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    print ("Space bar pressed down.")
            elif event.type == pygame.QUIT:
                    
                    pygame.display.quit()
                    #pygame.quit()
                    DicScore2['14']=1
                    fin = True
                    return None
                    
            elif event.type == pygame.MOUSEBUTTONDOWN and 177<pos[0]<526 and 180<pos[1]<525 and DicScore2["15"] != 1:
                #les chiffres sont la position dela grille du joueur dans la fenetre
                with lock:
                    print(pos)
                    
                        
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    print(column,row)

                    if cpt == 0:
                        PosTempo.append(row)
                        PosTempo.append(column)
                        PosTempoValue = Grille[row][column]
                        cpt += 1

                    elif cpt == 1:
                        
                        if Grille[row][column] == 0 or Grille[PosTempo[0]][PosTempo[1]] == 0:
                               
                            cpt = 0
                            PosTempo = []
                            PosTempoValue = 0

                            Grille = verifbalayage(Grille,player.stats,5,15,5,15)                        
        
                        elif  Grille[row][column] != 0 and Grille[PosTempo[0]][PosTempo[1]] != 0:

                            Grille[PosTempo[0]][PosTempo[1]] = Grille[row][column]
                            Grille[row][column] = PosTempoValue

                            Grille = véricationY(Grille,PosTempo[1],PosTempo[0],player.stats,5,15,5,5)
                            Grille = véricationX(Grille,column,row,player.stats,5,15,5,5)

                            Grille = véricationX(Grille,PosTempo[1],PosTempo[0],player.stats,5,15,5,5)
                            Grille = véricationY(Grille,column,row,player.stats,5,15,5,5)
                            
                                #Grille = CheckForBonus(Grille,row,column)
                                #Grille = CheckForBonus(Grille,PosTempo[1],PosTempo[0])

                            Grille = verifbalayage(Grille,player.stats,5,15,5,15)
                            
                            cpt = 0
                            PosTempo = []
                            PosTempoValue = 0
        
        screen.blit(pg.transform.scale(button_img[0],(1260,130)),(0,590))
        screen.blit(pg.transform.scale(button_img[0],(1260,130)),(0,0))
        for row in range(n):
            for column in range(n):
                color = None
                if Grille[row][column] == 2:
                    color = RED
                if Grille[row][column] == 3:
                    color = YELLOW
                if Grille[row][column] == 4:
                    color = ORANGE
                if Grille[row][column] == 5:
                    color = TURQUOISE
                if Grille[row][column] == 6:
                    color = BROWN
                if Grille[row][column] == 7:
                    color = WHITE
                    
                if color != None:
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
            
        textBlanc = font.render("Points d'action: "+str(player.stats["7"]), True, (0, 0, 0))
        screen.blit(textBlanc,(50 , 10))
           
        textRouge = font.render("Points de vie: "+str(player.stats["2"]), True, (0, 0, 0))
        screen.blit(textRouge,(50, 40))

        textJaune = font.render("Energie: "+str(player.stats["3"]), True, (0, 0, 0))
        screen.blit(textJaune,(50, 70))

        textOrange = font.render("Attaque bonus : "+str(player.stats["4"]), True, (0, 0, 0))
        screen.blit(textOrange,(270, 10))

        textMarron = font.render("Mana: "+str(player.stats["5"]), True, (0, 0, 0))
        screen.blit(textMarron,(270, 70))

        textBleu = font.render("Intelligence bonus:"+str(player.stats["6"]), True, (0, 0, 0))
        screen.blit(textBleu,(270, 40))


        textBlanc = font.render("Points d'action ennemi: "+str(DicScore2["7"]), True, (0, 0, 0))
        screen.blit(textBlanc,(700 , 10))

        textRouge = font.render("Points de vie ennemi: "+str(DicScore2["2"]), True, (0, 0, 0))
        screen.blit(textRouge,(700 , 40))

        textJaune = font.render("Energie ennemi: "+str(DicScore2["3"]), True, (0, 0, 0))
        screen.blit(textJaune,(700 , 75))

        textOrange = font.render("Attaque bonus ennemi: "+str(DicScore2["4"]), True, (0, 0, 0))
        screen.blit(textOrange,(970 , 10))

        textMarron = font.render("Mana ennemi: "+str(DicScore2["5"]), True, (0, 0, 0))
        screen.blit(textMarron,(970 , 40))

        textBleu = font.render("Intelligence bonus ennemi:"+str(DicScore2["6"]), True, (0, 0, 0))
        screen.blit(textBleu,(970 , 75))

        #textVert = font.render("Vert: "+str(DicScore2["1"]), True, (0, 0, 0))
        #screen.blit(textVert,(1340 - textVert.get_width() // 2, 140 - textVert.get_height() // 2))

        #textLevel = font.render("Niveau Actuel: "+str(DicScore2["13"]), True, (0, 0, 0))
        #screen.blit(textLevel,(1540 - textLevel.get_width() // 2, 140 - textLevel.get_height() // 2))

        if player.name == "Soxi":
            phrase = font.render(player.sort_name[0]+" coûte 1 d'Energie", 1,(0,0,0))
            screen.blit(phrase,(935,595))
            phrase = font.render(player.sort_name[1]+" coûte 5 d'Energie ", 1,(0,0,0))
            screen.blit(phrase,(935,620))
            phrase = font.render("et 1 Point d'Action", 1,(0,0,0))
            screen.blit(phrase,(935,640))
            phrase = font.render(player.sort_name[2]+" coûte 4 Point", 1,(0,0,0))
            screen.blit(phrase,(935,662))
            phrase = font.render(" d'Action", 1,(0,0,0))
            screen.blit(phrase,(935,680))

        if player.name == "Edalf":
            phrase = font.render(player.sort_name[0]+" coûte 1 de Mana", 1,(0,0,0))
            screen.blit(phrase,(935,595))
            phrase = font.render(player.sort_name[1]+" coûte 5 de Mana ", 1,(0,0,0))
            screen.blit(phrase,(935,620))
            phrase = font.render("et 1 Point d'Action", 1,(0,0,0))
            screen.blit(phrase,(935,640))
            phrase = font.render(player.sort_name[2]+" coûte 4 ", 1,(0,0,0))
            screen.blit(phrase,(935,662))
            phrase = font.render("Point d'Action", 1,(0,0,0))
            screen.blit(phrase,(935,680))

        if DicScore2["15"] != 1:

            button("Pause",740,620,180,60,fond_button[0],fond_button[1],Stop,DicScore2) 
            button(player.sort_name[0],50,620,180,60,fond_button[0],fond_button[1],player.sortUn,DicScore2)
            button(player.sort_name[1],285,620,180,60,fond_button[0],fond_button[1],player.sortDeux,DicScore2)
            button(player.sort_name[2],510,620,185,60,fond_button[0],fond_button[1],player.sortTrois,DicScore2)

        else:
            print("En pause")
            button("En Pause",750,620,180,60,fond_button[0],fond_button[1],Stop,DicScore2) 


        # Limit to 60 frames per second
        if switch == None:
            a = CheckForWin(Grille,DicScore2,player,DicScoreSave)
            
        if a == 1 or switch == "v":
            print("opt F1")
            switch = "v"
            if player.name == "Soxi":
                player.stats = {"0":0,"1":50,"2":50,"3":25,"4":20,"5":10,"6":10,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                #player.stats["13"] = memoireexp + int(DicScore2["13"])
            if player.name =="Edalf":
                player.stats = {"0":0,"1":0,"2":50,"3":10,"4":10,"5":30,"6":20,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                #player.stats["13"] = memoireexp + int(DicScore2["13"])
            for i in DicScore2.keys():
                DicScore2[i]= 0            

            DicScoreSave["13"] = 0
            DicScore2["2"] = 20

            screen.blit(pg.transform.scale(button_img[0],(500,200)),(375,250))
            question = font.render("Vous avez remporté le combat", 1,(0,0,0))
            gameDisplay.blit(question,(480,290))

            ok = buttonok("Ok",580,330,80,60,button_img[0],button_img[1])
            if ok:
                return 1
            
            player.stats['14']=1
            DicScore2['14']=1
            
            
        elif a == 2 or switch =="d" :
            switch = "d"
            print("opt F2")

            if player.name == "Soxi":
                player.stats = {"0":0,"1":50,"2":50,"3":25,"4":20,"5":10,"6":10,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                #player.stats["13"] = memoireexp + int(DicScore2["13"])
            if player.name =="Edalf":
                player.stats = {"0":0,"1":0,"2":50,"3":10,"4":10,"5":30,"6":20,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                #player.stats["13"] = memoireexp + int(DicScore2["13"])
            for i in DicScore2.keys():
                DicScore2[i]= 0    

            screen.blit(pg.transform.scale(button_img[0],(500,200)),(375,250))
            question = font.render("Vous avez perdu le combat", 1,(0,0,0))
            gameDisplay.blit(question,(495,290))

            ok = buttonok("Ok",580,330,80,60,button_img[0],button_img[1])
            if ok:
                return 2
            
            player.stats['14']=1
            DicScore2['14']=1
            
        if a == 0:
            pass

        pygame.display.flip()

    pygame.quit()

    return None







    
