from Joueur import Joueur

class Annonce:
    couleurChoisi = ""
    valeur = [80,90,100,110,120,130,140,150,160,500] #if capo non annoncer, pensser a donnée 250
    valeurChoisi = 0
    contrer = False
    partance = 0
    dernierParler = ""
    listJoueurs = [Joueur]*4

    def __init__(self, partance, jrs) -> None:
        self.partance = partance
        self.listJoueurs = jrs

    def getCouleur(self):
        return self.couleur

    def getValeur(self):
        return self.valeurChoisi

    def getContrer(self):
        return self.contrer
    
    def getDernierParler(self):
        return self.dernierParler
    
    def parle(self, j):
        valeur = self.valeurChoisi
        couleur = ""
        contrer = False
        passe = False


        # clic sur le btn passe => passe = true


        #recuperer valeur, couleur choisi sur interface


        # ou si contrer



        if passe == False:
            #set valchoisi, couleur
            self.valeurChoisi = valeur
            self.couleurChoisi = couleur

        elif contrer:
            self.contrer = True

        return valeur
    
    def start(self):
        i=self.partance
        nombreDePasse=0
        valeur = 0


        #lannonce sarrete si : capo annonce, contrer, 4 passe au debut, annonce et 3 passe
        while valeur != 500 and self.contrer != True and (nombreDePasse == 4 and valeur == 0) and (nombreDePasse == 3 and valeur != 0):
            # penser a remettre passe a 0 si annonce
            
            valeur = self.parle(self.listJoueurs[i])
            
            self.dernierParler = self.listJoueurs[i].nom


            if i < 3:
                i += 1
            else:
                i = 0
        

        if valeur == 0: # personne a parler on recomence une annonce
            return True
        else:   
            return False