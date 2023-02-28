from classes.Cartes import Cartes

class paquetCartes:
    paquet = [Cartes]*32

    def __init__(self):
        self.paquet[0] = Cartes(1, 11, "coeur")
        self.paquet[1] = Cartes(7, 0, "coeur")
        self.paquet[2] = Cartes(8, 0, "coeur")
        self.paquet[3] = Cartes(9, 0, "coeur")
        self.paquet[4] = Cartes(10, 10, "coeur")
        self.paquet[5] = Cartes(11, 2, "coeur")
        self.paquet[6] = Cartes(12, 3, "coeur")
        self.paquet[7] = Cartes(13, 4, "coeur")
        self.paquet[8] = Cartes(1, 11, "trefle")
        self.paquet[9] = Cartes(7, 0, "trefle")
        self.paquet[10] = Cartes(8, 0, "trefle")
        self.paquet[11] = Cartes(9, 0, "trefle")
        self.paquet[12] = Cartes(10, 10, "trefle")
        self.paquet[13] = Cartes(11, 2, "trefle")
        self.paquet[14] = Cartes(12, 3, "trefle")
        self.paquet[15] = Cartes(13, 4, "trefle")
        self.paquet[16] = Cartes(1, 11, "carreau")
        self.paquet[17] = Cartes(7, 0, "carreau")
        self.paquet[18] = Cartes(8, 0, "carreau")
        self.paquet[19] = Cartes(9, 0, "carreau")
        self.paquet[20] = Cartes(10, 10, "carreau")
        self.paquet[21] = Cartes(11, 2, "carreau")
        self.paquet[22] = Cartes(12, 3, "carreau")
        self.paquet[23] = Cartes(13, 4, "carreau")
        self.paquet[24] = Cartes(1, 11, "pique")
        self.paquet[25] = Cartes(7, 0, "pique")
        self.paquet[26] = Cartes(8, 0, "pique")
        self.paquet[27] = Cartes(9, 0, "pique")
        self.paquet[28] = Cartes(10, 10, "pique")
        self.paquet[29] = Cartes(11, 2, "pique")
        self.paquet[30] = Cartes(12, 3, "pique")
        self.paquet[31] = Cartes(13, 4, "pique")


    def setAtout(self, couleur):
        for i in range(32):
            if self.paquet[i].couleur == couleur:
                self.paquet[i].setAtout()
            else :
                self.paquet[i].removeAtout()