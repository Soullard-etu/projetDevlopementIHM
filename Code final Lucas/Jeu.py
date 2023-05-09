from Joueur import Joueur
from Carte import Carte
from InterfaceTexte import InterfaceUtilisateur
import random

class Jeu:
    #Initialisation des 'règles'
    COULEURS = ["Coeur", "Carreau", "Trèfle", "Pique"]
    VALEURS = ["7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
    ATOUTS = COULEURS
    joueurs = []
    premiere_carte = None
    
    equipe1 = []
    equipe2 = []
    score = {1: 0, 2: 0}
    
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
            test = 8
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
        partance = self.joueurs[0].id
             
        for joueur in self.joueurs:
                 
            #On demande a l'utilisateur de jouer une carte
            carte_jouee = joueur.jouer_carte(self.premiere_carte, self.atout, self.cartes_jouees)
                 
            #On ajoute la carte jouée a notre tableau de cartes jouées
            self.cartes_jouees.append(carte_jouee)
                 
            #On affiche la carte jouée ainsi que les cartes présentes sur le tapis
            InterfaceUtilisateur.afficherCarteJouee(joueur.id, carte_jouee, self.cartes_jouees)
                 
            if not self.premiere_carte:
                #On initilise la premiere carte a la carte jouée
                self.premiere_carte = carte_jouee
    
        carte_gagnante = self.gagnant_pli()
        InterfaceUtilisateur.afficherCarteGagnante(carte_gagnante)
        
        self.compter_points(self.equipe_gagnant(partance, carte_gagnante))
        InterfaceUtilisateur.afficherCarteGagnante(carte_gagnante)
        self.cartes_jouees = []
         
    def setupEquipes(self):
        self.equipe1.append(1)
        self.equipe2.append(2)
        self.equipe1.append(3)
        self.equipe2.append(4)
        
        
    
    def compter_points(self,equipe):
        for carte in self.cartes_jouees:
            self.score[equipe] += carte.points(self.atout)
    
        print(f"Points de l'équipe 1 : {self.score[1]}")
        print(f"Points de l'équipe 2 : {self.score[2]}")
        
        if len(self.joueurs[0].main) == 0:
            if self.score[1] > self.score[2]:
                print("L'équipe 1 remporte la partie !")
            elif self.score[2] > self.score[1]:
                print("L'équipe 2 remporte la partie !")
            else:
                print("Egalité !")

    def equipe_gagnant(self,partance,carte_gagnante):
        #Voir si le gagnant est dans l'équipe de la partance ou non
        if(self.cartes_jouees[0]==carte_gagnante)or(self.cartes_jouees[2]==carte_gagnante):
            #on verifie dans quelle équipe est la partance
            if(partance == 1 or partance == 3):
                
                return 1
            else:
                return 2
        else:
            
            if(partance == 1 or partance == 3):
                
                return 2
            else:
                return 1
            
        
         
    def jouer(self):
        self.distribuer_cartes()
        
        InterfaceUtilisateur.afficherMainJoueurs(self.joueurs)
        InterfaceUtilisateur.afficherAtouts(self.atout)
        
        while len(self.joueurs[0].main) > 0:
            self.jouer_tour()