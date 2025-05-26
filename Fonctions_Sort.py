from time import *

class druide:
    def sortVert(DicScore,DicEnnemi):
        sleep(0.1)
        if DicScore["3"] >= 2 and DicScore["7"] >= 1:

            DicScore["1"] -= 2
            DicScore["7"] -= 1
            DicEnnemi["2"] -= 3
            DicScore["2"] += 3

        else:
            pass
        return None

    def sortMorronUltime(DicScore,DicEnnemi):
        sleep(0.1)
        if DicScore["5"] >= 5 and DicScore["7"] >= 1:

            DicScore["5"] -= 5
            DicScore["7"] -= 1
            DicEnnemi["2"] -= 7

        else:
            pass
        return None 

    def sortBlanc(DicScore,DicEnnemi):
        sleep(0.1)
        if DicScore["7"] >= 4:

            DicScore["7"] -= 4
            DicEnnemi["2"] -= 15

        else:
            pass
        return None 
