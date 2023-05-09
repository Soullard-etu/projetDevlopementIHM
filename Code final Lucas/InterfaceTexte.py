from Carte import Carte

BLUE = '\033[34m'
GREEN = '\033[32m'
RESET = '\033[0m'
PURPLE = '\033[35m'
class InterfaceUtilisateur:
    # Couleurs de texte ANSI
    

    @classmethod
    def choix_carte_utilisateur(cls, joueur, premiere_carte, atout, cartes_jouees):
        cartes_valides = joueur.cartes_valides(premiere_carte, atout, cartes_jouees)
        print(f"{BLUE}Main du joueur {joueur.id} : {joueur.main}{RESET}")
        print(f"{GREEN}Cartes valides : {cartes_valides}{RESET}")

        carte_choisie = None
        while carte_choisie not in cartes_valides:
            carte_str = input(f"Joueur {joueur.id}, choisissez une carte à jouer (ex: 'Roi de Coeur'): ").strip()
            if carte_str == 'stop':
                quit()
            try:
                valeur, couleur = carte_str.split(" de ")
                carte_choisie = Carte(couleur, valeur)
                if carte_choisie not in cartes_valides:
                    print("Vous ne pouvez pas jouer cette carte. Veuillez choisir une carte valide.")
            except ValueError:
                print("Format de carte invalide. Veuillez entrer la carte au format 'valeur de couleur' (ex: 'Roi de Coeur')")

        return carte_choisie
    @staticmethod
    def afficherMainJoueurs(joueurs):
        for joueur in joueurs:
            print(f"Main du joueur {joueur.id} : {joueur.main}")
        
    @staticmethod
    def afficherAtouts(atout):
        print(f"Atout : {atout}")
    
    def afficherCarteJouee(joueur_id, carte, cartes_jouees):
        print(f"Joueur {joueur_id} a joué : {carte}")
        print(f"{PURPLE}Cartes sur le tapis :", cartes_jouees,f"{RESET}")
    
    @staticmethod    
    def afficherCarteGagnante(carte):
        print(f"Le pli est remporté par la carte : {carte}")