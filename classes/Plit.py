from classes.Joueur import Joueur

class Plit:
    pointE1 = 0
    pointE2 = 0
    partance = 0
    joueurPartie = [Joueur]*4
    joueurPrenantDernierPlit = Joueur

    def __init__(self, partance, joueurPartie) -> None:
        self.partance = partance
        self.joueurPartie = joueurPartie

    def getPoint_E1_E2(self):
        return [self.pointE1, self.pointE2]

    def start(self):
        1