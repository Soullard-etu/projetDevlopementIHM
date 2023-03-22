class Carte:
       
    COULEURS = ["Coeur", "Carreau", "Trèfle", "Pique"]

    # Remplacez 'Points' par 'POINTS' et 'Points_Atout' par 'POINTS_ATOUT'
    POINTS = {
        "7": 0,
        "8": 0,
        "9": 0,
        "Valet": 2,
        "Dame": 3,
        "Roi": 4,
        "10": 10,
        "As": 11,
    }

    POINTS_ATOUT = {
        "7": 0,
        "8": 0,
        "9": 14,
        "Valet": 20,
        "Dame": 3,
        "Roi": 4,
        "10": 10,
        "As": 11,
    }
    
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur
    
    def points(self, atout):
        if self.couleur == atout:
            return self.POINTS_ATOUT[self.valeur]
        else:
            return self.POINTS[self.valeur]


    #Redefinission des méthodes basiques pour faciliter la manipulation des cartes
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Carte):
            return self.couleur == other.couleur and self.valeur == other.valeur
