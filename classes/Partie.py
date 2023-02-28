import random
from classes.Joueurs import Joueurs
from classes.paquetCartes import paquetCartes
from classes.Manche import Manche

class Partie:
    pointMax = 2000
    joueursPartie = [Joueurs]*4
    paquetCarte = paquetCartes
    joueurPartance = 0

    def __init__(self, jrs) -> None:
        for i in range(4):
            self.joueursPartie[i] = jrs[i]

        self.paquetCarte = paquetCartes()
        
        pass

    def partance(self):
        if self.joueurPartance < 3:
            self.joueurPartance += 1
        else:
            self.joueurPartance = 0
        
        return self.joueurPartance
    
    def distribuCartes(self):
        # on melange le paquet
        random.shuffle(self.paquetCarte.paquet)

        #on distribue
        i = 0
        j = 0
        k = 0
        for i in range(4):
            for j in range(8):
                self.joueursPartie[i].carte[j] = self.paquetCarte.paquet[j+k]
            k += 8
        
    def startJeu(self):

        return

    