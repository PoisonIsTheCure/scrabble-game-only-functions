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
    for i in range(len(cases_MT)):
        a=cases_MT[i]
        lplateau[a[0]][a[1]]="***"
    for i in range(len(cases_MD)):
        a=cases_MD[i]
        lplateau[a[0]][a[1]]="** "
    for i in range(len(cases_LT)):
        a=cases_LT[i]
        lplateau[a[0]][a[1]]="---"
    for i in range(len(cases_LD)):
        a=cases_LD[i]
        lplateau[a[0]][a[1]]="-- "
    return lplateau

def veril(i): #verifie que la longueur du chaine du caractère est coherant , à utiliser our chaque string
    if len(i) != 3 :
        if i == 1:
            i = ' '+str(i.upper)+' '
        elif i == 2:
            i = str(i.upper())+' '
    else:
        i = i.upper()
    return i

def affiche_jetons(j):
    lettre = "j"
    #j'ai changer la place de bonus (deplacer vers init_jetons()) affichee car elle n'étaient pad demandés dans la consigne
    #on considera même d'enlever les mot MT , MD , LT , LD pour diminuer le confusion
    #il n'est pas bien déterminer le but de cette fonction
    pos = [j[0],j[1]]
    if pos in cases_MT :
        lplateau[j[0]][j[1]]= veril(f"*{lettre}*")
    elif pos in cases_MD :
        lplateau[j[0]][j[1]]= veril(f" {lettre}*")
    elif pos in cases_LT :
        lplateau[j[0]][j[1]]= veril(f"-{lettre}-")
    elif pos in cases_LD :
        lplateau[j[0]][j[1]]= veril(f" {lettre}-")
    else:
        lplateau[j[0]][j[1]]= veril(lettre)
    #J'ai changer la methode d'affichage des bonus pour qu'ils soient mieux lisibles
    return lplateau


def cree_plateau(lplateau):
    for l in range(len(lplateau)):
        unligne = ''
        for i in lplateau[l]:
            unligne += i
        print(unligne)






lplateau = init_jetons()
affiche_jetons([0,0])
affiche_jetons([7,7])
cree_plateau(lplateau)
