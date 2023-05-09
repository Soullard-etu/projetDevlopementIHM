from InterfaceTexte import InterfaceUtilisateur
class Joueur:
    def __init__(self, id):
        self.id = id
        self.main = []
        self.atout = None

    def recevoir_cartes(self, cartes):
        self.main = cartes

    def jouer_carte(self, premiere_carte, atout, cartes_jouees):
        
        
        carte = InterfaceUtilisateur.choix_carte_utilisateur(self, premiere_carte, atout, cartes_jouees)
        self.main.remove(carte)
        carte.joueur = self  # Ajout de cette ligne pour définir l'attribut joueur de la carte jouée
        return carte

    def cartes_valides(self, premiere_carte, atout, cartes_jouees):
        
        if premiere_carte is None:
            return self.main
        else:
            couleur_demandee = premiere_carte.couleur
            cartes_couleur_demandee = [carte for carte in self.main if carte.couleur == couleur_demandee]
            if cartes_couleur_demandee:
                return cartes_couleur_demandee
            
            
            elif any(carte.couleur == atout for carte in self.main):
                #CAS 3e JOUEUR DE JOUER
                if(len(cartes_jouees)==2):
                    #SI LE DEUXIEME JOUEUR A COUPER
                    if(cartes_jouees[1].couleur== atout):
                        
                        return[carte for carte in self.main if (carte.couleur == atout and carte.points(atout)>cartes_jouees[1].points)]
                    elif(cartes_jouees[0].couleur == cartes_jouees[1].couleur and cartes_jouees[0].points > cartes_jouees[1].points):
                        return[carte for carte in self.main if (carte.couleur == atout)]
                    else:
                        return self.main
                            
                elif(len(cartes_jouees)==3):    
                    #si ton partenaire a déja coupé et pas le 3e joueur tu peux jouer ta main
                    if(cartes_jouees[1].couleur==atout and cartes_jouees[2].couleur!=atout):
                        
                        return self.main
                    #Dans le cas ou ton partenaire s'est fait coupé
                    elif(cartes_jouees[1].couleur!=atout and cartes_jouees[2].couleur==atout):
                        #Si il peut surcouper
                        if(len([carte for carte in self.main if (carte.couleur == atout and carte.points(atout)>cartes_jouees[2].points)])>0):
                            return [carte for carte in self.main if (carte.couleur == atout and carte.points(atout)>cartes_jouees[2].points)]
                        #sinon il peut tt jouer
                        else:
                            return self.main
                    #si ton partenaire a couper mais que le 3e joueur a jouer un atout aussi    
                    elif(cartes_jouees[1].couleur==atout and cartes_jouees[2].couleur==atout):
                        #si ton partenaire est maitre tu joues tout
                        if(cartes_jouees[1].points(atout)>cartes_jouees[2].points(atout)):
                            
                            return self.main
                        else:
                            #Si il peut surcouper
                            if(len([carte for carte in self.main if (carte.couleur == atout and carte.points(atout)>cartes_jouees[2].points)])>0):
                                return [carte for carte in self.main if (carte.couleur == atout and carte.points(atout)>cartes_jouees[2].points)]
                            #Sinon il peut tt jouer
                            else:
                                return self.main
                else:  
                    return [carte for carte in self.main if carte.couleur == atout]
            else:
                return self.main

    def doisCouper(atouts):
        return 