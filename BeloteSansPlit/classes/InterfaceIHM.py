class InterfaceIHM:


    def annonce(self, listVal, dernierAnnonce, jr, dernierCouleur):
        passe = False
        contrer = False
        couleur = ""
        valeur = 0
        valeurChoisi = 0

        print("")
        print("a vous de parler", jr.nom)
        print("annonce possible :")
        print(listVal)

        if dernierAnnonce != 0:
            print("valeur de la derniere annonce faite")
            print(dernierAnnonce, " : ", dernierCouleur)
            valeur = int(input("si passe 1 | si contre 2 sinon valeur de lannonce: "))

        else:
            valeur = int(input("si passe 1 | sinon valeur de lannonce: "))

        if valeur == 1:
            passe = True
        elif valeur == 2:
            contrer = True
        else:
            valeurChoisi = valeur
            couleur = input("couleur de lannonce: ")
        

        return [passe, contrer, valeurChoisi, couleur]