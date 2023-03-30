from classes.Cartes import Cartes

class Joueur:
    nom = ""
    main = [Cartes]*8
    compteurCarte = 0

    def __init__(self, nom) -> None:
        self.nom = nom
    
    def setCartes(self, carte):
        self.main[self.compteurCarte].copy(self.main[self.compteurCarte],carte)
        
        if self.compteurCarte<7:
            self.compteurCarte += 1
        else:
            self.compteurCarte = 0
    
