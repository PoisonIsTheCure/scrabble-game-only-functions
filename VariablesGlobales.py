def init_registre():
    global registre
    registre = {}

cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]
#A RENDRE LA FONCTION INIT_BONUS GLOBAL
def init_bonus():
    """
    Fonction qui creer une liste bonus telque:
    list[0] = MT/list[1] = MD/list[2] = LT/list[3] = LD
    """
    global lbonus
    lbonus = [cases_MT,cases_MD,cases_LT,cases_LD] # initiation d'une liste contenant les listes des jitions des bonus
    return lbonus

PosPremierJocker = []
PosDeuxiemeJocker = []

def init_dico():
    global dico
    dico={"A":{"occ":9,"val":1},
          "B": {"occ": 2, "val": 3},
          "C": {"occ": 2, "val": 3},
          "D": {"occ": 3, "val": 2},
          "E": {"occ": 15, "val": 1},
          "F": {"occ": 2, "val": 4},
          "G": {"occ": 2, "val": 2},
          "H": {"occ": 2, "val": 4},
          "I": {"occ": 8, "val": 1},
          "J": {"occ": 1, "val": 8},
          "K": {"occ": 1, "val": 10},
          "L": {"occ": 5, "val": 1},
          "M": {"occ": 3, "val": 2},
          "N": {"occ": 6, "val": 1},
          "O": {"occ": 6, "val": 1},
          "P": {"occ": 2, "val": 3},
          "Q": {"occ": 1, "val": 8},
          "R": {"occ": 6, "val": 1},
          "S": {"occ": 6, "val": 1},
          "T": {"occ": 6, "val": 1},
          "U": {"occ": 6, "val": 1},
          "V": {"occ": 2, "val": 4},
          "W": {"occ": 1, "val": 10},
          "X": {"occ": 1, "val": 10},
          "Y": {"occ": 1, "val": 10},
          "Z": {"occ": 1, "val": 10},
          "?": {"occ": 2, "val": 0},
    }
    return dico

PremierTour = True