#la pioche
#1
from random import randint
def init_dico():
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
#2
def init_pioche(dico):
    l = []
    dk=list(dico.keys())
    dv=list(dico.values())
    for i in range (27):
        for j in range(dv[i]['occ']):
            l.append(dk[i])
    return l
#print(init_pioche(init_dico()))




#3
def piocher(x,sac):
    main=[]
    for i in range (x):
        a=randint(0,len(sac)-1)
        main.append(sac.pop(a))
    print(sac)
    return main
#4
def completer_main(main,sac):
    if len(main)<7 :
        x = 7-len(main)
        liste = piocher(x,sac)
        main.extend(liste)
    return main

#5
def echanger(jetons ,main, sac):
    existe = True
    sacsuff = True
    for elt in jetons:
        existe = (elt in main) and existe
        sacsuff = (len(sac)>= len(jetons)) and sacsuff
    if sacsuff and existe :
        nouveau = piocher(len(jetons), sac)
        sac.extend(jetons)
        main.extend(nouveau)
        for elt in jetons:
            main.remove(elt)
        return True
    else:
        if not(existe) and not(sacsuff):
            print("Jetons non disponibles dans la main et sac insuffisant!")
        elif not(existe):
            print("Jetons non disponibles dans la main!")
        elif not(sacsuff):
            print("Sac insuffisant!")
        return False
#6
def cree_joueurs(i,sac):
    """
    creation du es joueurs avec un paramètre (nombre des joueurs),
    demande le nom des joueurs,
    renvoie un dictionnaire contenant les noms des joueurs comme cles
    chaque cle contient les lettre du pioche du joueurs
    """
    joueur = {}
    nb_joueur = i+1
    name = input(f"Quelle est le nom de joueur numéro ({nb_joueur}) : ")
    main = piocher(7,sac)
    score = 0
    joueur["nom"]= name
    joueur["score"]= score
    joueur["main"]= main
    joueur["tour"] = False
    return joueur

'''
#sac=init_pioche(init_dico())
sac = init_pioche(init_dico())
print(len(sac))
print(sac)
#main = piocher(7,sac)
#main=['A','C']
#jetons = ['A','D']
#echanger(jetons,main,sac)
joueurs = cree_joueurs(2,sac)
print(joueurs)
print(sac)
print(len(sac))
'''

#Tous les fonction on étaient testés et tout va bien

"""
def echanger(jetons,main,sac):

    if jetons[0] in main:
        main.remove(jetons[0])
        a=random.randint(0,len(sac)-1)
        main.append(sac[a])

        sac.append(jetons[0])
    else:
        print("111")
sac=init_pioche(init_dico())
print(echanger(["A"],["X","E","A"],sac))
"""
