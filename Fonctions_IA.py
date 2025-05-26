from Fonctions_Generation import *
from Fonctions_Scoring import *
from Fonctions_Sort import *
from random import *
from time import *
import pygame 
import threading


lock = threading.Lock()
#Fonction Vériiant si l'utilisateur gagne/perd/Continue
def CheckForWin(Grille,DicScore2,player,DicScoreSave):

    memoireexp = player.stats["13"]

    if DicScore2["2"]<=0:
        print("joueur gagne")
        with lock:

            Grille = Randomisation(Grille,5,15,5,15)
            Grille = Randomisation(Grille,5,15,20,30)

            return 1
        
        
    elif player.stats["2"]<=0:
        print("joueur perd")
        with lock:

            if player.name == "Soxi":
                player.stats = {"0":0,"1":50,"2":50,"3":25,"4":20,"5":10,"6":10,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                player.stats["13"] = memoireexp
            if player.name =="Edalf":
                player.stats = {"0":0,"1":0,"2":50,"3":10,"4":10,"5":30,"6":20,"7":10,"8":0,"9":0,"10":0,"11":0,'12':0,'13':0,'14':0,'15':0}
                player.stats["13"] = memoireexp
            
            DicScoreSave["13"]+=1
            for i in DicScore2.keys():
                DicScore2[i]= 0            

            DicScore2["2"] = 20

        
            Grille = Randomisation(Grille,5,15,5,15)
            Grille = Randomisation(Grille,5,15,20,30)

            return 2
            
    else:
        return 0


#Fonction du bot analysant les coups possibles sur l'axe X
def AnalyseX(Grille,Départ,Fin,a,b):
    ListePièce =[]
    ListeCoup = []
    for Y in range(Départ+2,Fin-2):
        for X in range(a+2,b-2):

            NombreDeCasesValide = 1

            TempoXPlus = X+1
            TempoXMoins = X-1

            Porte1 = True
            Porte2 = True

            
            while Porte2 == True:

                if Grille[Y][X] == Grille[Y][TempoXMoins] and Grille[Y][TempoXMoins] != 0:
                    ListePièce.append([Y,TempoXMoins])
                    TempoXMoins -= 1
                    NombreDeCasesValide += 1
                    
                else:
                    Porte2 = False

            
            ListePièce.append([Y,X])

            while Porte1 == True:

                if Grille[Y][X] == Grille[Y][TempoXPlus] and Grille[Y][TempoXPlus] != 0:
                    ListePièce.append([Y,TempoXPlus])
                    TempoXPlus += 1
                    NombreDeCasesValide += 1

                else:
                    Porte1 = False

            
            if NombreDeCasesValide >= 2:
                
                #print ("X ;coup possible de:",NombreDeCasesValide,"Avec Les pièces suivantes",ListePièce )
                ListeCoup.append(ListePièce)
                ListePièce=[]
            else:
                ListePièce=[]

    return ListeCoup

#Fonction du bot analysant les coups possibles sur l'axe Y
def AnalyseY(Grille,Départ,Fin,a,b):
    ListePièce =[]
    ListeCoup =[]
    for Y in range(Départ+2,Fin-2):
        for X in range(a+2,b-2):

            NombreDeCasesValide = 1

            TempoYPlus = Y+1
            TempoYMoins = Y-1

            Porte1 = True
            Porte2 = True

            
            while Porte2 == True:

                if Grille[Y][X] == Grille[TempoYMoins][X] and Grille[TempoYMoins][X]!=0:
                    ListePièce.append([TempoYMoins,X])
                    TempoYMoins -= 1
                    NombreDeCasesValide += 1
                    
                else:
                    Porte2 = False

            
            ListePièce.append([Y,X])

            while Porte1 == True:

                if Grille[Y][X] == Grille[TempoYPlus][X] and Grille[TempoYPlus][X] !=0:
                    ListePièce.append([TempoYPlus,X])
                    TempoYPlus += 1
                    NombreDeCasesValide += 1

                else:
                    Porte1 = False

            
            if NombreDeCasesValide >= 2:
                
                #print ("X ;coup possible de:",NombreDeCasesValide,"Avec Les pièces suivantes",ListePièce )
                ListeCoup.append(ListePièce)
                ListePièce=[]
            else:
                ListePièce=[]

    return ListeCoup
#Try De list de list
def SortListOfList(Liste):

    Liste.sort()
    Cache = None

    for el in Liste:
        if el != Cache:
            Cache = el
        if el == Cache:
            Liste.remove(el)
    Liste.sort()
#Fonction Sélectionnant le meilleur coup pour un axe
def FindBestCoup(Liste):
    MaxLenght = 0
    ListeCoupMaxLenght = []

    for el in Liste:

        if len(el) > MaxLenght:
            ListeCoupMaxLenght= []
            ListeCoupMaxLenght.append(el)
            MaxLenght = len(el)

        if len(el) == MaxLenght:
            
            ListeCoupMaxLenght.append(el)
            
        else:
            pass

    ListeCoupMaxLenght[0].sort()

    return ListeCoupMaxLenght
#Fonction retournant le coup final qui sera joué
def FindCoupFinal(Liste1,Liste2,Départ,Fin,a,b):
    ListeFinal = []

    for el in Liste1:
        ListeFinal.append(el)
    for el in Liste2:
        ListeFinal.append(el)
    if ListeFinal == []:
        NbRandom1 = randint(Départ+2,Fin-2)
        NbRandom2 = randint(a+2,b-2)

        return[[NbRandom1,NbRandom2],[NbRandom1,NbRandom2+1]]

    NbRandom = randint(0,len(ListeFinal)-1)
    ListeFinal = ListeFinal[NbRandom]
    


    return list(ListeFinal)
#Fonction Cherchant une valeur en fonction du coup final 
def SearchForValue(Grille,Liste,Départ,Fin,a,b):

    ListeValueSwapable = []
    Liste.sort()
    for Y in range(Départ+2,Fin-2):
        for X in range(a+2,b-2):
            if Grille[Y][X] == Grille[Liste[1][0]][Liste[1][1]]:
                ListeValueSwapable.append([Y,X])

    try:
        for el in Liste:
            for sel in el:
                for ssel in sel:
                    ListeValueSwapable.remove(ssel)
    except:
        pass

    if ListeValueSwapable == []:
        ListeValueSwapable.append([randint(Départ+2,Fin-2),randint(a+2,b-2)])
    return ListeValueSwapable

#Fonction swappant les valeures aux bons endroits pour effectuer le coup
def SwapValues(Grille,CoupFinal,Liste):

    
    
    NbRandom = randint(0,len(Liste)-1)
    NbChoisi = Liste[NbRandom]


    CoupFinalMin = CoupFinal[0]
    CoupFinalMax = CoupFinal[-1]
   

    while 0!=1:

        print(CoupFinal ,Grille[CoupFinalMin[0]][CoupFinalMin[1]],Grille[CoupFinalMax[0]][CoupFinalMax[1]])
        if CoupFinal[0][0] == CoupFinal[1][0] and CoupFinal[0][0]!=0 and CoupFinal[1][0]!=0:
            print("X")
        
            if Grille[CoupFinalMin[0]][CoupFinalMin[1]-1] != 0 and Grille[CoupFinalMin[0]][CoupFinalMin[1]]!= 0:
                print("Option 1")
                Grille[NbChoisi[0]][NbChoisi[1]]   ,Grille[CoupFinalMin[0]][CoupFinalMin[1]-1] = Grille[CoupFinalMin[0]][CoupFinalMin[1]-1]   ,   Grille[NbChoisi[0]][NbChoisi[1]]
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMin[0],CoupFinalMin[1]-1],"=",Grille[CoupFinalMin[0]][CoupFinalMin[1]-1])
                
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMin[0],CoupFinalMin[1]-1],"=",Grille[CoupFinalMin[0]][CoupFinalMin[1]-1])

                return (Grille,NbChoisi,CoupFinalMin)

            elif Grille[CoupFinalMax[0]][CoupFinalMax[0]+1]!= 0 and Grille[CoupFinalMax[0]][CoupFinalMax[0]]!= 0:
                print("Option 2")      
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMax[0],CoupFinalMax[1]+1],"=",Grille[CoupFinalMax[0]][CoupFinalMax[1]+1])
                Grille[NbChoisi[0]][NbChoisi[1]],Grille[CoupFinalMax[0]][CoupFinalMax[1]+1] = Grille[CoupFinalMax[0]][CoupFinalMax[1]+1],Grille[NbChoisi[0]][NbChoisi[1]]
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMax[0],CoupFinalMax[1]+1],"=",Grille[CoupFinalMax[0]][CoupFinalMax[1]+1])

                return (Grille,NbChoisi,CoupFinalMax)
            else:
                return (Grille,NbChoisi,CoupFinalMax) 
            

               

                   
        elif CoupFinal[0][1] == CoupFinal[1][1] and CoupFinal[0][1]!=0 and CoupFinal[1][1]!=0:
            print("Y")

            if Grille[CoupFinalMin[0]-1][CoupFinalMin[0]] != 0 and Grille[CoupFinalMin[0]][CoupFinalMin[0]]!=0:
                print("Option 1")             
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMin[0]-1,CoupFinalMin[1]],"=",Grille[CoupFinalMin[0]-1][CoupFinalMin[1]])
                Grille[NbChoisi[0]][NbChoisi[1]],Grille[CoupFinalMin[0]-1][CoupFinalMin[1]] = Grille[CoupFinalMin[0]-1][CoupFinalMin[1]],Grille[NbChoisi[0]][NbChoisi[1]]
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMin[0]-1,CoupFinalMin[1]],"=",Grille[CoupFinalMin[0]-1][CoupFinalMin[1]])

                
                return (Grille,NbChoisi,CoupFinalMin)
            elif Grille[CoupFinalMax[0]+1][CoupFinalMax[0]] != 0 and Grille[CoupFinalMax[0]][CoupFinalMax[0]]!=0:
                print("Option 2")          
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMax[0]+1,CoupFinalMax[1]],"=",Grille[CoupFinalMax[0]+1][CoupFinalMax[1]])
                Grille[NbChoisi[0]][NbChoisi[1]],Grille[CoupFinalMax[0]+1][CoupFinalMax[1]] = Grille[CoupFinalMax[0]+1][CoupFinalMax[1]],Grille[NbChoisi[0]][NbChoisi[1]]
                #print(NbChoisi,"=",Grille[NbChoisi[0]][NbChoisi[1]],"et",[CoupFinalMax[0]+1,CoupFinalMax[1]],"=",Grille[CoupFinalMax[0]+1][CoupFinalMax[1]])

                return (Grille,NbChoisi,CoupFinalMax)
            
                #print("Vraiment ? ")
            else:
                return (Grille,NbChoisi,CoupFinalMax)
            



#Fonction créant un coup similaire à celui d'un utilisateur
def Action(Grille,DicScore,Départ,Fin,a,b):                             
    with lock:
        Grille = verifbalayage(Grille,DicScore,Départ,Fin,a,b)
    #AfficheGrille(Grille)   
    ListeCoupX=AnalyseX(Grille,Départ,Fin,a,b)
    ListeCoupY=AnalyseY(Grille,Départ,Fin,a,b)


    #print("La liste des coups Possible X;")
    SortListOfList(ListeCoupX)
    #AfficheGrille(ListeCoupX)

    #print("La liste des coups Possible Y;")
    SortListOfList(ListeCoupY)
    #AfficheGrille(ListeCoupY)

    CoupFinal = FindCoupFinal(ListeCoupY,ListeCoupX,Départ,Fin,a,b)
    #print("#")
    #print("Etant le coup final",CoupFinal)
    
    ListeValuePossible = SearchForValue(Grille,CoupFinal,Départ,Fin,a,b)
    #print(ListeValuePossible,"Liste des valeures possibles")
    with lock:
        Grille,NbChoisi,CoupFinalMin = SwapValues(Grille,CoupFinal,ListeValuePossible)
    with lock:
        Grille = verifbalayage(Grille,DicScore,Départ,Fin,a,b)
    #sleep(0.3)
    return None

def CheckSpell(DicSelf,DicFoe):
    with lock:
        druide.sortVert(DicSelf,DicFoe)
    with lock:
        druide.sortMorronUltime(DicSelf,DicFoe)
    with lock:
        druide.sortBlanc(DicSelf,DicFoe)
    
def AttackEnnemi(DicSelf,DicFoe):
    CheckSpell(DicSelf,DicFoe)
    

#Fonction lancant l'ia sur une grille, effectuant des actions en boucle
def Play(Grille,DicScore,Départ,Fin,a,b,DicEnnemi):
    while 1!=0:
        while DicScore["15"] == 1:
            print('currently paused' )
        Action(Grille,DicScore,Départ,Fin,a,b)
        AttackEnnemi(DicScore,DicEnnemi)
        sleep(1)
        #sleep(0.1)
        if  DicScore['14']==1:
            return None
    

