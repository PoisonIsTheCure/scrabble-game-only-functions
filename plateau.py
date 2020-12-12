#Première partie du programme

#plateau = [["   " for i in range(15)] for j in range(15)] #Création du plateau avec des espaces

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
    lbonus = [cases_MT,cases_MD,cases_LT,cases_LD] # initiation d'une liste contenant les listes des jitions des bonus
    return lbonus

def CreationDuPlateauVide():
    return [["   " for i in range(15)] for j in range(15)]

def AjoutDesSignesCasesBonus(ListeBonus, lplateau , Signe):
    for i in range(len(ListeBonus)):
        lplateau[ListeBonus[i][0]][ListeBonus[i][1]]= Signe

def init_jetons():
    lplateau = CreationDuPlateauVide()
    AjoutDesSignesCasesBonus(cases_MT, lplateau , "***")
    AjoutDesSignesCasesBonus(cases_MD, lplateau , "** ")
    AjoutDesSignesCasesBonus(cases_LT, lplateau , "---")
    AjoutDesSignesCasesBonus(cases_LD, lplateau , "-- ")
    return lplateau

def VerifierLongueur(i): #verifie que la longueur du chaine du caractère est coherant , à utiliser our chaque string
    if len(str(i)) != 3 :
        if len(str(i)) == 1:
            i = ' '+str(i).upper()+' '
        elif len(str(i)) == 2:
            i = str(i).upper()+' '
    else:
        i = str(i).upper()
    return i

def affiche_jetons(j,jeton,lplateau):
    lettre = jeton
    #j'ai changer la place de bonus (deplacer vers init_jetons()) affichee car elle n'étaient pad demandés dans la consigne
    #on considera même d'enlever les mot MT , MD , LT , LD pour diminuer le confusion
    #il n'est pas bien déterminer le but de cette fonction
    if j in cases_MT :
        lplateau[j[0]][j[1]]= VerifierLongueur(f"*{lettre}*")
    elif j in cases_MD :
        lplateau[j[0]][j[1]]= VerifierLongueur(f" {lettre}*")
    elif j in cases_LT :
        lplateau[j[0]][j[1]]= VerifierLongueur(f"-{lettre}-")
    elif j in cases_LD :
        lplateau[j[0]][j[1]]= VerifierLongueur(f" {lettre}-")
    else:
        lplateau[j[0]][j[1]]= VerifierLongueur(lettre)
    #J'ai changer la methode d'affichage des bonus pour qu'ils soient mieux lisibles
    return lplateau


def affiche_plateau(lplateau):
    largeur = len(lplateau[0])*len(lplateau[0][0]) + len(lplateau[0])+ 5
    column_liste = [VerifierLongueur(i) for i in range(len(lplateau[0]))]
    separe = "".join(["~" for i in range(largeur)])
    haut = "   §"+ "|".join(column_liste) + "§"
    print(haut)
    print(separe)
    for l in range(len(lplateau)):
        if l == 0:
            unligne = "|".join(lplateau[l])
            print(f" {l} §{unligne}§    Légende:")
        elif l == 1:
            unligne = "|".join(lplateau[l])
            print(f""" {l} §{unligne}§    Case des mots triples : "***" , lettre en case d'un mot triple : "*A*" """)
        elif l == 2:
            unligne = "|".join(lplateau[l])
            print(f""" {l} §{unligne}§    Case des mots doubles : "** " , lettre en case d'un mot double : "A* " """)
        elif l == 3:
            unligne = "|".join(lplateau[l])
            print(f""" {l} §{unligne}§    Case des lettres triples : "---" , lettre en case d'une lettre triple : "-A-" """)
        elif l == 4:
            unligne = "|".join(lplateau[l])
            print(f""" {l} §{unligne}§    Case des lettres doubles : "-- " , lettre en case d'une lettre double : "A- " """)
        elif l < 10:
            unligne = "|".join(lplateau[l])
            print(f" {l} §{unligne}§")
        else:
            unligne = "|".join(lplateau[l])
            print(f"{l} §{unligne}§")
