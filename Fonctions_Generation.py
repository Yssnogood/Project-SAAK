from random import *
#Créer La Grille de jeu 
def GenGrille(n):
    Grille= []
    
    for X in range(0,n):
        GrilleTempo = []
        for Y in range(0,n):
            GrilleTempo.append(0)
        Grille.append(GrilleTempo)

    return Grille

#Affichage Console 
def AfficheGrille(Grille):
    for el in Grille:
        print(el,end="\n")

#Affichage Console des coups possibles
def AfficheCoup(Liste):
    for el in Liste:
        for sel in el:
            print(sel,end="\n")
#Affichage Console du score
def AfficheScore(Dic):
    for Cle,Valeur in Dic.items():
        print("Score de ",Cle,"est de ",Valeur,end="\n")
#Ccréation de valeures random dans l'espace défini
def Randomisation(Grille,Départ,Fin,a,b):
    NewGrille = []
    for i in range(Départ,Fin):
        for j in range(a,b):
            Grille[i][j] = Générationcontrolée()
    return Grille


#Ancienne fonction d'échange de values
def Swap(Grille,X1,X2,Y1,Y2):

    Tempo = Grille[Y2][X2]
    Grille[Y2][X2] = Grille[Y1][X1]
    Grille[Y1][X1] = Tempo

    return Grille
#Permet de gérer les valeures arrivant dans la grille par probabilités
def Générationcontrolée():
        NbRandom = randint(1,100)

        if NbRandom <= 20:
                return 2
        if NbRandom <= 45 and NbRandom >20:
                return 3
        if NbRandom <= 60 and NbRandom >45:
                return 4
        if NbRandom <= 75 and NbRandom >60:
                return 5
        if NbRandom <= 85 and NbRandom >75:
                return 6
        if NbRandom <= 100 and NbRandom >85:
                return 7
        
