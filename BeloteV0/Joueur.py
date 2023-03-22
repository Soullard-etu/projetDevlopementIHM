class Joueur:
    def __init__(self, id):
        self.id = id
        self.main = []
    
    def cartes_valides(self, premiere_carte):
       if not premiere_carte:
           return self.main
       
        #Possibilités de cartes a jouer a completer pour le moment
        #*uniquement les cartes de meme couleur
        #|||||||||||||||||||||||||||||||||||||||||||||||||||||
        
       cartes_meme_couleur = [carte for carte in self.main if carte.couleur == premiere_carte.couleur]
       return cartes_meme_couleur if cartes_meme_couleur else self.main

    def recevoir_cartes(self, cartes):
        self.main.extend(cartes)

    def jouer_carte(self, carte):
        if carte in self.main:
            self.main.remove(carte)
            return carte
        else:
            raise ValueError(f"Le joueur {self.id} n'a pas cette carte en main : {carte}")
