class Cartes:
    atout = False
    nom = 0
    valeur = 0
    couleur = ""

    def __init__(self, nom, valeur, couleur):
        self.nom = nom
        self.valeur = valeur
        self.couleur = couleur

    def setAtout(self):
        if self.atout == False:
            self.atout = True

            if self.nom == 9:
                self.valeur = 14

            elif self.nom == 11:
                self.valeur = 20

    def removeAtout(self):
        if self.atout == True:
            self.atout = False

            if self.nom == 9:
                self.valeur = 0
                
            elif self.nom == 11:
                self.valeur = 2
    
    def copy(self, crt):
        self.atout = crt.atout
        self.couleur = crt.couleur
        self.nom = crt.nom
        self.valeur = crt.valeur
    
    def __str__(self):
        return str(self.atout) + "," + self.couleur + "," + str(self.nom) + "," + str(self.valeur)
