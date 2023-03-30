from classes.InterfaceIHM import InterfaceIHM
from classes.Plit import Plit
from classes.Joueur import Joueur

class Manche:
    atout = ""
    valeur = 0
    plt = Plit
    point_E1_E2 = [int]*2
    joueurPartie = [Joueur]*4
    IHM = InterfaceIHM

    def __init__(self, jrs, IHM) -> None:
        self.joueurPartie = jrs
        self.IHM = IHM
    
    def getPoint_E1_E2(self):
        return self.point_E1_E2

    def start(self, atout, valeur, contrer, partance):
        self.atout = atout
        self.valeur = valeur
        self.plt = Plit(partance, self.joueurPartie)

        for i in range(8):
            self.plt.start()
        
        self.point_E1_E2 = self.plt.getPoint_E1_E2()