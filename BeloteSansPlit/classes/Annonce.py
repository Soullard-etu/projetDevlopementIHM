from classes.InterfaceIHM import InterfaceIHM
from classes.Joueur import Joueur

class Annonce:
    couleurChoisi = ""
    valeur = [80,90,100,110,120,130,140,150,160,500] #if capo non annoncer, pensser a donnée 250
    valeurChoisi = 0
    contrer = False
    partance = 0
    dernierParler = ""
    nombreDePasse = 0
    listJoueurs = [Joueur]*4
    IHM = InterfaceIHM

    def __init__(self, jrs, IHM) -> None:
        self.listJoueurs = jrs
        self.IHM = IHM

    def getCouleur(self):
        return self.couleurChoisi

    def getValeur(self):
        return self.valeurChoisi

    def getContrer(self):
        return self.contrer
    
    def getDernierParler(self):
        return self.dernierParler
    
    def parle(self, j):
        valeur = 0
        couleur = ""
        contrer = False
        passe = False

        res = self.IHM.annonce(self, self.valeur, self.valeurChoisi, j, self.couleurChoisi)

        passe = res[0]
        contrer = res[1]
        valeur = res[2]
        couleur = res[3]

        if passe:
            self.nombreDePasse += 1

        elif contrer:
            self.contrer = True
        
        else:
            #set valchoisi, couleur
            self.valeurChoisi = valeur
            self.couleurChoisi = couleur
            self.dernierParler = j.nom
            self.nombreDePasse = 0

        return passe
        

    def start(self):
        i=self.partance

        #lannonce sarrete si : capo annonce, contrer, 4 passe au debut, annonce et 3 passe
        while self.valeurChoisi != 500 and self.contrer != True and not (self.nombreDePasse == 4 and self.valeurChoisi == 0) and not (self.nombreDePasse == 3 and self.valeurChoisi != 0):
            # penser a remettre passe a 0 si annonce
            res = self.parle(self.listJoueurs[i])

            if res == False:
                self.nombreDePasse = 0

            if i < 3:
                i += 1
            else:
                i = 0

        self.nombreDePasse = 0

        if self.valeurChoisi == 0: # personne a parler on recomence une annonce
            return True
        else:   
            return False
        

