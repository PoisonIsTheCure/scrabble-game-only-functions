#import pioche
#from pioche import *
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
def get_valeur(lettre,dico):
    key = lettre.upper()
    if key in dico.keys():
        valeur = dico[key]["val"]
    return valeur
print(get_valeur('a',dico))


'''
les variables global:
==>lplateau pour definir lr plateau dont on travail
==>dico pour definir la liste des dictionnaires
==> dirbool = True si horizental, et dirbool = False if vertical
'''

"""
je vais crée un dictionnaire registre ou il y a tout les nom et les valeur des joueur
exemple : registre = {'ali':{'main':['A','C','D','H','I','K','L'] , 'score': 50}}
"""

"""
Légende:
Case des mots triples : "***" , lettre en case d'un mot triple : "*A*"
Case des mots doubles : " **" , lettre en case d'un mot double : " A*"
Case des lettres triples : "---" , lettre en case d'une lettre triple : "-A-"
Case des lettres doubles : " --" , lettre en case d'une lettre double : " A-"
"""

'''
def affiche_jetons(j):
    ligne = j[0]
    colonne = j[1]
    lettre = lplateau[ligne][colonne]
    newstr = lettre.replace(' ','')
    thenewstr = newstr.replace('*','')
    recentstr = thenewstr.replace('-','')
    return recentstr
'''

'''
def cree_plateau(lplateau):
    largeur = len(lplateau[0])*len(lplateau[0][0]) + len(lplateau[0])+ 5
    column_liste = [veril(i) for i in range(len(lplateau[0]))]
    separe = "".join(["~" for i in range(largeur)])
    haut = "   §"+ "|".join(column_liste) + "§"
    print(haut)
    print(separe)
    for l in range(len(lplateau)):
        if l < 10:
            unligne = "|".join(lplateau[l])
            print(f" {l} §{unligne}§")
        elif l >= 10 :
            unligne = "|".join(lplateau[l])
            print(f"{l} §{unligne}§")
'''
