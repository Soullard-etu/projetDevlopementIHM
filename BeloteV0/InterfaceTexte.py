from Carte import Carte

BLUE = '\033[34m'
GREEN = '\033[32m'
RESET = '\033[0m'
PURPLE = '\033[35m'


class InterfaceUtilisateur:
    
    # Couleurs de texte ANSI
    
    @staticmethod
    def choix_carte_utilisateur(joueur, premiere_carte):
        cartes_valides = joueur.cartes_valides(premiere_carte)
        
       


        print(f"{BLUE}Main du joueur {joueur.id} : {joueur.main}{RESET}")

        print(f"{GREEN}Cartes valides : {cartes_valides}{RESET}")
        # Initialise avec une carte fictive
        carte_choisie = Carte("Fictive", "Fictive")
        while carte_choisie not in cartes_valides:
            carte_str = input(
                f"Joueur {joueur.id}, choisissez une carte à jouer (ex: 'Roi de Coeur'): ").strip()
            if carte_str =='stop':
                quit()
            try:
                valeur, couleur = carte_str.split(" de ")
                carte_choisie = Carte(couleur, valeur)
                if carte_choisie not in cartes_valides:
                    print(
                        "Vous ne pouvez pas jouer cette carte. Veuillez choisir une carte valide.")
            except ValueError:
                print(
                    "Format de carte invalide. Veuillez entrer la carte au format 'valeur de couleur' (ex: 'Roi de Coeur')")
        return carte_choisie

    @staticmethod
    def afficherMainJoueurs(joueurs):
        for joueur in joueurs:
            print(f"Main du joueur {joueur.id} : {joueur.main}")
        
    @staticmethod
    def afficherAtouts(atout):
        print(f"Atout : {atout}")
    
    @staticmethod
    def afficherCarteJouee(joueur,carte,cartes):
        print(f"Joueur {joueur} a joué : {carte}")
        print(f"{PURPLE}Cartes sur le tapis :", cartes,f"{RESET}")
    
    @staticmethod    
    def afficherCarteGagnante(carte):
        print(f"Le pli est remporté par la carte : {carte}")
