from Joueur import Joueur
from Carte import Carte
from InterfaceTexte import InterfaceUtilisateur
import random

class Jeu:
    #Initialisation des 'règles'
    COULEURS = ["Coeur", "Carreau", "Trèfle", "Pique"]
    VALEURS = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    ATOUTS = COULEURS
    VALEURS = ["7", "8", "9", "Valet", "Dame", "Roi", "10", "As"]
    joueurs = []
    nbCartesParJOueurs = 2
    premiere_carte = None
    def __init__(self):
        self.joueurs = [Joueur(i) for i in range(1, 5)]
        self.cartes_jouees = []
        self.atout = random.choice(self.ATOUTS)

    def distribuer_cartes(self):
        #On crée le deck et on le mélange
        deck = [Carte(couleur, valeur) for couleur in self.COULEURS for valeur in self.VALEURS]
        random.shuffle(deck)
        #On distribue les cartes
        for i, joueur in enumerate(self.joueurs):
            #On choisit le nombre de cartes (test) peut varier pour faire des tests
            test = 2
            joueur.recevoir_cartes(deck[i*test:(i+1)*test])

    def gagnant_pli(self):
        #On prend la première carte et de la on les compares tous grace a leur points
        #si il y a un ou plusieurs atout, on ne compare qu'euxs
        cartes_atout = [carte for carte in self.cartes_jouees if carte.couleur == self.atout]
        if len(cartes_atout)==1:
            return cartes_atout[0]
        
        
        #Si pas d'atout, on ne compare que les cartes de couleur maitre
        elif len(cartes_atout)==0:
            cartes_maitre = [carte for carte in self.cartes_jouees if carte.couleur == self.premiere_carte.couleur]
            carte_gagnante = cartes_maitre[0]
            if len(cartes_maitre)>1:
                for carte in cartes_maitre[1:]:
                    if carte.points(self.atout) > carte_gagnante.points(self.atout):
                        carte_gagnante = carte
            return carte_gagnante
        
        
        
        
        else:
            carte_gagnante = self.cartes_jouees[0]
            for carte in self.cartes_jouees[1:]:
                if carte.points(self.atout) > carte_gagnante.points(self.atout):
                    carte_gagnante = carte
            return carte_gagnante
            
        
        

    def jouer_tour(self):
         self.premiere_carte = None
         for joueur in self.joueurs:
             
             #On demande a l'utilisateur de jouer une carte
             carte_jouee = joueur.jouer_carte(InterfaceUtilisateur.choix_carte_utilisateur(joueur, self.premiere_carte))
             #On ajoute la carte jouée a notre tableau de cartes jouées
             self.cartes_jouees.append(carte_jouee)
             
             #On affiche la carte jouée ainsi que les cartes présentes sur le tapis
             InterfaceUtilisateur.afficherCarteJouee(joueur.id, carte_jouee, self.cartes_jouees)
             
             if not self.premiere_carte:
                 #On initilise la premiere carte a la carte jouée
                 self.premiere_carte = carte_jouee

         carte_gagnante = self.gagnant_pli()
         
         InterfaceUtilisateur.afficherCarteGagnante(carte_gagnante)
         
         
    def jouer(self):
        self.distribuer_cartes()
        
        InterfaceUtilisateur.afficherMainJoueurs(self.joueurs)
        InterfaceUtilisateur.afficherAtouts(self.atout)
        
        self.jouer_tour()
