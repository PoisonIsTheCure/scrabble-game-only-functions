import VariablesGlobales as vg
#Première partie du programme

#plateau = [["   " for i in range(15)] for j in range(15)] #Création du plateau avec des espaces



def CreationDuPlateauVide():
    return [["   " for i in range(15)] for j in range(15)]

def AjoutDesSignesCasesBonus(ListeBonus, lplateau , Signe):
    for i in range(len(ListeBonus)):
        lplateau[ListeBonus[i][0]][ListeBonus[i][1]]= Signe

def init_jetons():
    lplateau = CreationDuPlateauVide()
    AjoutDesSignesCasesBonus(vg.cases_MT, lplateau , "***")
    AjoutDesSignesCasesBonus(vg.cases_MD, lplateau , "** ")
    AjoutDesSignesCasesBonus(vg.cases_LT, lplateau , "---")
    AjoutDesSignesCasesBonus(vg.cases_LD, lplateau , "-- ")
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
    if j in vg.cases_MT :
        lplateau[j[0]][j[1]]= VerifierLongueur(f"*{lettre}*")
    elif j in vg.cases_MD :
        lplateau[j[0]][j[1]]= VerifierLongueur(f" {lettre}*")
    elif j in vg.cases_LT :
        lplateau[j[0]][j[1]]= VerifierLongueur(f"-{lettre}-")
    elif j in vg.cases_LD :
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
