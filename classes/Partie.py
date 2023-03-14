import random
from classes.paquetCartes import paquet
from classes.Joueur import Joueur
from classes.Manche import Manche
from classes.Annonce import Annonce

class Partie:
    pointMax = 2000
    point_E1_E2 = [int]*2
    joueursPartie = [Joueur]*4
    paquetCarte = paquet
    annonce = Annonce
    manche = Manche
    joueurPartance = 0


    def __init__(self, jrs) -> None:
        for i in range(4):
            self.joueursPartie[i] = jrs[i]
        
        self.annonce = Annonce(self.joueurPartance, jrs)
        self.manche = Manche()

        self.point_E1_E2[0] = 0
        self.point_E1_E2[1] = 0
        
        pass

    def prin(self):
        return self.paquetCarte

    def majPartance(self):
        if self.joueurPartance < 3:
            self.joueurPartance += 1
        else:
            self.joueurPartance = 0
        
        return self.joueurPartance
    
    def distribuCartes(self):
        # on melange le paquet
        random.shuffle(self.paquetCarte)

        #on distribue
        i = 0   # parcourir les joueurs
        j = 0   # parcourir le paquet
        k = 0   # parcourir le paquet
        for i in range(4):
            for j in range(8):
                self.joueursPartie[i].setCartes(self.paquetCarte[j+k])
            k += 8
        
    def setAtout(self, couleur):
        for i in range(32):
            if self.paquetCarte[i].couleur == couleur:
                self.paquetCarte[i].setAtout()
            else :
                self.paquetCarte[i].removeAtout()
        
    def startJeu(self):
        # debut de la manche 
        while(self.point_E1_E2[0]<self.pointMax and self.point_E1_E2[1]<self.pointMax):
            # annonce
            condition = True
            while condition:
                 # modification partance
                partance = self.majPartance()

                # distribution carte 
                self.distribuCartes()

                condition = self.annonce.start()   
                
            
            joueurRemportantLannonce = self.annonce.getDernierParler()
            couleurAtout = self.annonce.getCouleur()
            valeur = self.annonce.getValeur()
            contrer = self.annonce.getContrer()

            for i in range(4):
                if self.joueursPartie[i].nom == joueurRemportantLannonce.nom:
                    if i == 0 or i == 2:
                        equipeDeLannonce = 0    #equipe 1
                        equipeSansLannonce = 1
                    else:
                        equipeDeLannonce = 1    #equipe 2
                        equipeSansLannonce = 0
            
            # modification des atout
            self.setAtout(couleurAtout)

            # plits
            self.manche.start(couleurAtout, valeur, contrer, partance, self.joueursPartie)

            # comptage point
            pointDeLaManche = self.manche.getPoint_E1_E2()
            
            if valeur > pointDeLaManche[equipeDeLannonce]:
                pointDeLaManche[equipeDeLannonce] = 0
                pointDeLaManche[equipeSansLannonce] = 160
                if contrer:
                    pointDeLaManche[equipeSansLannonce] *= 2

            elif pointDeLaManche[equipeSansLannonce] == 0:
                if valeur == 500:
                    pointDeLaManche[equipeDeLannonce] = 500
                else:
                    pointDeLaManche[equipeDeLannonce] = 250
                    if contrer:
                        pointDeLaManche[equipeDeLannonce] *= 2

            else:
                if contrer:
                    pointDeLaManche[equipeDeLannonce] = 320
                    pointDeLaManche[equipeSansLannonce] = 0
            

            # set point 
            self.point_E1_E2 += pointDeLaManche

