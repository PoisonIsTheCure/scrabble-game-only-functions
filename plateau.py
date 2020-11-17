#Première partie du programme

class Plateau(object):
    """docstring for Plateau."""

    def __init__(self):
        super(Plateau, self).__init__()
        self.plateau = [["   " for i in range(15)] for j in range(15)] #Création du plateau avec des espaces


    def init_bonus(self):
        lbonus = ['MT','MD','LT','LD','']
        return lbonus

    def init_jetons(self):
        print("Hello World!")

    def affiche_jetons(self,j):
        pass
