from Plit import Plit
from Joueur import Joueur

class Manche:
    atout = ""
    valeur = 0
    plt = Plit
    point_E1_E2 = [int]*2
    joueurPartie = [Joueur]*4

    def __init__(self, atout, valeur, partance, joueurPartie):
        self.atout = atout
        self.valeur = valeur
        self.joueurPartie = joueurPartie
        self.plt = Plit(partance, joueurPartie)
    
    def getPoint_E1_E2(self):
        return self.point_E1_E2

    def start(self):
        for i in range(8):
            self.plt.start()
        
        self.point_E1_E2 = self.plt.getPoint_E1_E2()