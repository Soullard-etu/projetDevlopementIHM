class Cartes:
    atout = False
    name = 0
    valeur = 0
    couleur = ""

    def __init__(self, name, valeur, couleur):
        self.name = name
        self.valeur = valeur
        self.couleur = couleur

    def setAtout(self):
        if self.atout == False:
            self.atout = True

            if self.name == 9:
                self.valeur = 14

            elif self.name == 11:
                self.valeur = 20

    def removeAtout(self):
        if self.atout == True:
            self.atout = False

            if self.name == 9:
                self.valeur = 0
                
            elif self.name == 11:
                self.valeur = 2