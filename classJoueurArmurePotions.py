from random import*

class Equipement:
    def __init__(self, slot = "Armure", name = "Des Cieux",HP = 10, PROT = 10,STAM =  10, MANA = 10, INTEL = 10, ATK = 10):
        self.type = slot
        self.name = name
        self.stat= {"HP": HP,
                    "PROT":PROT,
                    "MANA": MANA,
                    "INTEL": INTEL,
                    "STAM": STAM,
                    "ATK":ATK}

    def equipe(self,dicoJ):
        dicoJ["HP"] += self.stat["HP"]
        dicoJ["PROT"]+=self.stat["PROT"]
        dicoJ["MANA"]+=self.stat["MANA"]
        dicoJ["STAM"]+=self.stat["STAM"]
        dicoJ["INTEL"]+=self.stat["INTEL"]
        dicoJ["ATKmax"] +=self.stat["ATK"]
        dicoJ["HPmax"] += self.stat["HP"]
        dicoJ["PROTmax"]+=self.stat["PROT"]
        dicoJ["MANAmax"]+=self.stat["MANA"]
        dicoJ["INTELmax"]+=self.stat["INTEL"]
        dicoJ["ATKmax"] +=self.stat["ATK"]

    def desequipe(self, dicoJ):

        if dicoJ["HP"] - self.stat["HP"] <= 0:
            dicoJ["HP"] = 1
        if dicoJ["HP"] -self.stat["HP"] > 0:
            dicoJ["HP"] -= self.stat["HP"]

        dicoJ["STAM"]+=self.stat["STAM"]
        dicoJ["PROT"]-=self.stat["PROT"]
        dicoJ["MANA"]-=self.stat["MANA"]
        dicoJ["INTEL"]-=self.stat["INTEL"]
        dicoJ["ATKmax"] -=self.stat["ATK"]
        dicoJ["HPmax"] -= self.stat["HP"]
        dicoJ["PROTmax"]-=self.stat["PROT"]
        dicoJ["MANAmax"]-=self.stat["MANA"]
        dicoJ["INTELmax"]-=self.stat["INTEL"]
        dicoJ["ATKmax"] -=self.stat["ATK"]


class Potions():
    def __init__(self, typePotion = None, ty = " De Santé ", regen = 5):
        self.type = "Potion"
        self.name = ty
        self.typePotion = typePotion
        self.regen = regen

    def utiliser(self, dicJoueur):
        # Stats limitées
        # HP
        if self.typePotion == "HP" :
            if dicJoueur["HP"] + self.regen > dicJoueur["HPmax"]:
                dicJoueur["HP"] += dicJoueur["HPmax"] - dicJoueur["HP"]
            if dicJoueur["HP"] +  self.regen <=  dicJoueur["HPmax"]:
                dicJoueur["HP"] += self.regen
    
        #MANA   
        if self.typePotion == "MANA" :
            if dicJoueur["MANA"] + self.regen > dicJoueur["MANAmax"]:
                dicJoueur["MANA"] += dicJoueur["MANAmax"] - dicJoueur["MANA"]
            if dicJoueur["MANA"] +  self.regen <=  dicJoueur["MANAmax"]:
                dicJoueur["MANA"] += self.regen
       
        #STAMINA
        if self.typePotion == "STAM" :
            if dicJoueur["STAM"] + self.regen > dicJoueur["STAMmax"]:
                dicJoueur["STAM"] += dicJoueur["STAMmax"] - dicJoueur["STAM"]
            if dicJoueur["STAM"] +  self.regen <=  dicJoueur["STAMmax"]:
                dicJoueur["STAM"] += self.regen
        #PROT
        if self.typePotion == "PROT" :
            dicJoueur["PROT"] += self.regen
        #ATK
        if self.typePotion == "ATK" :
            dicJoueur["ATK"] += self.regen
        
