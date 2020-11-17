#Première partie du programme

plateau = [["   " for i in range(15)] for j in range(15)] #Création du plateau avec des espaces

cases_MT = [[0,0],[0,7],[0,14],[7,0],[7,14],[14,0],[14,7],[14,14]]
cases_MD = [[1,1],[1,13],[2,2],[2,12],[3,3],[3,11],[4,4],[4,10],[7,7],[10,4],[10,10],[11,3],[11,11],[12,2],[12,12],[13,1],[13,13]]
cases_LT = [[1,5],[1,9],[5,1],[5,5],[5,9],[5,13],[9,1],[9,5],[9,9],[9,13],[13,5],[13,9]]
cases_LD = [[0,3],[0,11],[2,6],[2,8],[3,0],[3,7],[3,14],[6,2],[6,6],[6,8],[6,12],[7,3],[7,11],[8,2],[8,6],[8,8],[8,12],[11,0],[11,7],[11,14],[12,6],[12,8],[14,3],[14,11]]

def init_bonus():
    lbonus = [cases_MT,cases_MD,cases_LT,cases_LD] # initiation d'une liste contenant les listes des positions des bonus
    return lbonus

def init_jetons():
    lplateau = []
    for i in range(15):
        ligne = []
        for j in range(15):
            ligne.append("   ")
        lplateau.append(ligne)
    return lplateau

def init_jetons():
    lplateau = []
    for i in range(15):
        ligne = []
        for j in range(15):
            ligne.append("   ")
        lplateau.append(ligne)
    return lplateau

def affiche_jetons(j):
    lplateau[j[0]][j[1]]="j"
    for i in range(len(cases_MT)):
        a=cases_MT[i]
        lplateau[a[0]][a[1]]="MT"
    for i in range(len(cases_LD)):
        a=cases_LD[i]
        lplateau[a[0]][a[1]]="LD"
    for i in range(len(cases_LT)):
        a=cases_LT[i]
        lplateau[a[0]][a[1]]="LT"
    for i in range(len(cases_MD)):
        a=cases_MD[i]
        lplateau[a[0]][a[1]]="MD"

    return lplateau

def cree_plateau(lplateau):
    for l in range(len(lplateau)):
        unligne = ''
        for i in lplateau[l]:
            unligne += " | "+" | ".join(i)
        print(unligne)


lplateau= init_jetons()
affiche_jetons([0,5])
cree_plateau(lplateau)

"""
for i in range(15):
    for j in range(15):
        print(lplateau[i][j],end=" ")
    print()
"""
"""""
def init_jetons():
    lplateau = []
    for i in range(15):
        ligne = []
        for j in range(15):
            ligne.append("A")
        lplateau.append(ligne)
    return lplateau

def affiche_jetons(j):
    lplateau[j[0]][j[1]]="j"
    for i in range(len(cases_MT)):
        a=cases_MT[i]
        lplateau[a[0]][a[1]]="MT"
    for i in range(len(cases_LD)):
        a=cases_LD[i]
        lplateau[a[0]][a[1]]="LD"
    for i in range(len(cases_LT)):
        a=cases_LT[i]
        lplateau[a[0]][a[1]]="LT"
    for i in range(len(cases_MD)):
        a=cases_MD[i]
        lplateau[a[0]][a[1]]="MD"

    return lplateau


lplateau= init_jetons()
print(affiche_jetons([0,5]))

def affiche_jetons(j,i):
    lplateau[i[0]][i[1]] = j
    return lplateau

def affiche_bonus(lbonus):
    for i in range(len(lbonus[0])):
        print("f")
        pos = [0,i]
        lplateau = affiche_jetons("MT",pos)
    for i in range(len(lbonus[1])):
        print(i)
        pos = [1,i]
        lplateau = affiche_jetons("MD",pos)
    for i in range(len(lbonus[2])):
        print(i)
        pos = [2,i]
        lplateau = affiche_jetons("LT",pos)
    for i in range(len(lbonus[3])):
        pos = [3,i]
        lplateau = affiche_jetons("LD",pos)
    return lplateau
"""""
