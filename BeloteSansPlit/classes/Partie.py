import random
from classes.InterfaceIHM import InterfaceIHM
from classes.Equipe import Equipe
from classes.paquetCartes import paquet
from classes.Joueur import Joueur
from classes.Manche import Manche
from classes.Annonce import Annonce

class Partie:
    POINTMAX = 2000
    equipe1 = Equipe
    equipe2 = Equipe
    joueursPartie = [Joueur]*4
    paquetCarte = paquet
    annonce = Annonce
    manche = Manche
    joueurPartance = -1
    IHM = InterfaceIHM


    def __init__(self, jrs) -> None:
        for i in range(4):
            self.joueursPartie[i] = jrs[i]
        
        self.equipe1 = Equipe(jrs[0], jrs[2])
        self.equipe2 = Equipe(jrs[1], jrs[3])
        
        self.annonce = Annonce(jrs, self.IHM)
        self.manche = Manche(jrs, self.IHM)

        self.equipe1.pointEquipe = 0
        self.equipe2.pointEquipe = 0

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
        k = 0   # retenu pour parcourir le paquet
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
        while(self.equipe1.pointEquipe<self.POINTMAX and self.equipe2.pointEquipe<self.POINTMAX):
            # annonce
            condition = True
            while condition == True:
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
                if self.joueursPartie[i].nom == joueurRemportantLannonce:
                    if i == 0 or i == 2:
                        equipeDeLannonce = 0    #equipe 1
                        equipeSansLannonce = 1
                    else:
                        equipeDeLannonce = 1    #equipe 2
                        equipeSansLannonce = 0
            
            # modification des atout
            self.setAtout(couleurAtout)
            
            # plits
            self.manche.start(couleurAtout, valeur, contrer, partance)

            # comptage point
            pointDeLaManche = self.manche.getPoint_E1_E2()
            print("les point de la manche : ", pointDeLaManche)
            
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
            if equipeDeLannonce == 0:
                self.equipe1.pointEquipe += pointDeLaManche[equipeDeLannonce]
                self.equipe2.pointEquipe += pointDeLaManche[equipeSansLannonce]

            else:
                self.equipe1.pointEquipe += pointDeLaManche[equipeSansLannonce]
                self.equipe2.pointEquipe += pointDeLaManche[equipeDeLannonce]