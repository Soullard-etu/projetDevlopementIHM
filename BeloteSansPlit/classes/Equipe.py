from classes.Joueur import Joueur


class Equipe:
    joueurEquipe = [Joueur]*2
    pointEquipe = 0

    def __init__(self, j1, j2) -> None:
        self.joueurEquipe[0] = j1
        self.joueurEquipe[1] = j2
    
    def setPoint(self, var):
        self.pointEquipe = var

    def getPoint(self):
        return self.pointEquipe