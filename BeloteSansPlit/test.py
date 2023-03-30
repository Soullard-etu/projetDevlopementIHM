from classes.Partie import Partie
from classes.Joueur import Joueur


j1 = Joueur("lucas")
j2 = Joueur("Ange")
j3 = Joueur("Axel")
j4 = Joueur("PA")

lJoueur = [j1, j2, j3, j4]

p = Partie(lJoueur)

p.startJeu()

