from Joueur import Joueur

class Annonce:
    couleurChoisi = ""
    valeur = [80,90,100,110,120,130,140,150,160,500] #if capo non annoncer, pensser a donnée 250
    valeurChoisi = 0
    contrer = False
    partance = 0
    dernierParler = ""
    nombreDePasse = 0
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
        valeur = 0
        couleur = ""
        contrer = False
        passe = False


        # clic sur le btn passe => passe = true


        # clic sur le btn contre => contre = true
        

        # si valeur et couleur select et clic btn valider
            #recuperer valeur, couleur choisi sur interface



        # teste 
        print("a vous de parler")
        print("annonce possible :")
        print(self.valeur)

        if self.valeurChoisi != 0:
            print("valeur de la derniere annonce faite")
            print(self.valeurChoisi)
            valeur = int(input("si passe 1 | si contre 2 sinon valeur de lannonce"))
        else:
            valeur = int(input("si passe 1 | sinon valeur de lannonce"))


        if valeur == 1:
            passe = True
        elif valeur == 2:
            contrer = True
        else:
            couleur = input("couleur de lannonce")
        # fin teste


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
            
    

    def start(self):
        i=self.partance

        #lannonce sarrete si : capo annonce, contrer, 4 passe au debut, annonce et 3 passe
        while self.valeurChoisi != 500 and self.contrer != True and (self.nombreDePasse == 4 and self.valeurChoisi == 0) and (self.nombreDePasse == 3 and self.valeurChoisi != 0):
            # penser a remettre passe a 0 si annonce
            self.parle(self.listJoueurs[i])

            if i < 3:
                i += 1
            else:
                i = 0
        

        if self.valeurChoisi == 0: # personne a parler on recomence une annonce
            return True
        else:   
            return False