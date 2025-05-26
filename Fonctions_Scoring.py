from Fonctions_Generation import *
from random import *
from time import *



#Fonction mettant à jour le dictionnaire
def Scoring(Dic,Value):
    Dic[str(Value)] +=3
    return Dic


#Pistaller auto pi exe

#Fonction Donnant un descente pour L'axe X
def DescenteX(Grille,row,column,Départ,Fin,a,b):
    
    while row != Départ:
        
        Grille[row][column] = Grille[row-1][column]
        row -= 1
        

       
    Grille[Départ][column] = Générationcontrolée()

    return Grille
#Fonction Vérifiant si Coup possible sur L'axe Y
def véricationX(Grille,X,Y,Dic,Départ,Fin,a,b):

    NombreDeCasesValide = 1
    
    TempoXPlus = X+1
    TempoXMoins = X-1

    Porte1 = True
    Porte2 = True

    
    
    while Porte1 == True:
        if Grille[Y][X] == Grille[Y][TempoXPlus] and Grille[Y][TempoXPlus]!=0:
            NombreDeCasesValide += 1
            TempoXPlus += 1
            
            
        else:
            Porte1 = False

    
    
    while Porte2 == True:
        if Grille[Y][X] == Grille[Y][TempoXMoins] and Grille[Y][TempoXMoins]!=0:
            NombreDeCasesValide += 1
            TempoXMoins -= 1
            
            
        else:
            Porte2 = False
    
    
    if NombreDeCasesValide >= 3:
        Scoring(Dic,Grille[Y][X])
        print(NombreDeCasesValide)
        for i in range (TempoXMoins+1,TempoXPlus):
            Grille = DescenteX(Grille,Y,i,Départ,Fin,a,b)
            sleep(0.05)

        
        return Grille
         
    else:
        return Grille

#Fonction Donnant un descente pour L'axe Y
def DescenteY(Grille,row,column,Ecart,Départ,Fin,a,b):

    #print("L'écart est de :",Ecart)
    
    while row >= Départ+Ecart-1:
        Grille[row][column] = Grille[row-Ecart][column]
        
        row -= 1
        #print("La case (",row,",",column,")","Vient d'être traitée")            
    for Y in range(Départ,Départ+Ecart):
        sleep(0.05)
        Grille[Y][column] = Générationcontrolée()


    return Grille

#Fonction Vérifiant si Coup possible sur L'axe X
def véricationY(Grille,X,Y,Dic,Départ,Fin,a,b):

    NombreDeCasesValide = 1
    
    TempoYPlus = Y
    TempoYMoins = Y

    Porte1 = True
    Porte2 = True
    
    while Porte1 == True:
        if Grille[Y][X] == Grille[TempoYPlus+1][X] and Grille[TempoYPlus+1][X] !=0:

            TempoYPlus += 1
            NombreDeCasesValide += 1

        else:
            Porte1 = False
    

    while Porte2 == True:
        if Grille[Y][X] == Grille[TempoYMoins-1][X] and Grille[TempoYMoins-1][X]:

            TempoYMoins -= 1
            NombreDeCasesValide += 1

        else:
            Porte2 = False

    #print("Cases valide Y pour les coordonnées (",X,",",Y,")",NombreDeCasesValide)
    

    Ecart = TempoYPlus - TempoYMoins+1
    
    if NombreDeCasesValide >= 3:
        Scoring(Dic,Grille[Y][X])
        #print("Passe a la descente")
        
        Grille = DescenteY(Grille,TempoYPlus,X,Ecart,Départ,Fin,a,b)

        return Grille
            
    else:
        #print("return normal")
        return Grille





def CheckForBonus(Grille,X,Y):

    if Grille[Y][X] == 8:
        for i in range(5,15):
            DescenteX(Grille,Y,i)

    if Grille[Y][X] == 9:
        for i in range(5,15):
            Grille[i][X] = Générationcontrolée()

    if Grille[Y][X] == 10:
        for i in range(5,15):
            DescenteX(Grille,Y,i)
            Grille[i][X] = Générationcontrolée()

    if Grille[Y][X] == 11:
        ValeurRandom = Générationcontrolée() 
        for i in range(5,15):
            for j in range(5,15):
                if Grille[i][j] == ValeurRandom:
                    DescenteX(Grille,i,j)  
        Grille[Y][X] = ValeurRandom

    if Grille[Y][X] == 12:
        for i in range(Y-1,Y+2):
            for j in range(X-1,X+2):
                if Grille[i][j] == 0:
                    pass
                else:
                    Grille = DescenteX(Grille,i,j)
   
    return Grille
#Vérifie que tout les coups possible de la grille sont joués
def balayage(Grille,X,Y,Dic,Départ,Fin,a,b):
    Grille = véricationX(Grille,X,Y,Dic,Départ,Fin,a,b)
    Grille = véricationY(Grille,X,Y,Dic,Départ,Fin,a,b)
    return Grille


#Vérification en Boucle pour n'en louper aucun 
def verifbalayage(Grille,Dico,Départ,Fin,a,b):
    porte = 0

    DicTempo1 = Dico 
    DicTempo2 = Dico 


    while porte != 1:

        
        for Y in range(Départ,Fin):
            for X in range(a,b):
                #print("Vérification de :",Y,X)
                Grille = balayage(Grille,X,Y,DicTempo2,Départ,Fin,a,b)
        if DicTempo1 != DicTempo2:
            DicTempo1 = DicTempo2
            continue               
        elif DicTempo1 == DicTempo2:
            porte = 1         



    Dico = DicTempo1 
    return Grille
