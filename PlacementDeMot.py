import plateau as plt
from plateau import affiche_jetons , affiche_plateau
import ConstructionDesMots as cdm
import VariablesGlobales as vg
#1
def lire_coords():
    """Fonction qui lit les coordonnées sur le plateau

    Returns:
        int: [renvoie une liste des coordonnées y : ligne et x: colonne]
    """
    while True:
        y = input("A Quelle ligne voulez vous commencer : ")
        x = input("A Quelle colonne : ")
        if (x+y).isdigit() :
            x = int(x)
            y = int(y)
            if 0<=x<=14 and 0<=y<=14: break
    return y,x
#2
def lire_lettre(y,x,plateau):
    """Cette fonction reçoit les cooredonnées et lit la lettre sur le plateau

    Args:
        y (int): ligne
        x (int): colonne
        plateau (liste): plateau initiale

    Returns:
        string: renvoi la lettre lut sans les * et - et les ecpaces
    """    
    ligne = y
    colonne = x
    lettre = plateau[ligne][colonne]
    newstr = lettre.replace(' ','')
    thenewstr = newstr.replace('*','')
    recentstr = thenewstr.replace('-','')
    return recentstr

def lire_mot(plateau,x,y,mot,dir): #i c'
    lenmot = len(mot)
    motpl = []
    if dir == 'h': #cas horizental
        if (len(plateau[y]) - x) < lenmot :
            return 0
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            x+=1
    elif dir == 'v': #cas vertical
        if (len(plateau) - y) < lenmot :
            return 0
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            y+=1
    if not(vg.PremierTour):
        ToutElementsVides = True
        for elt in motpl:
            if len(elt) != 0 : ToutElementsVides = False
        if ToutElementsVides :
            print("Votre mot doit au moins passée par un lettre déjà existant !")
            return 0
    return motpl

def verifie_mot(mot,lmotexistant):
    mot.upper()
    lmot = list(mot)
    lmot.extend(lmotexistant)
    dict_fr = cdm.generer_dico()
    mots_possibles = cdm.mots_jouables(dict_fr, lmot)
    return True if mot in mots_possibles else False
    

def tester_placement(plateau,i,j,dir,mot):
    mot.upper()
    lmot = []
    acceptee = True
    motexistant = lire_mot(plateau,i,j,mot,dir)
    VerifieSiLePremierMotPassParLeCentre(mot,dir,j,i)
    if motexistant != 0 :
        for index in range(len(motexistant)) :
            if motexistant[index] == "" :
                lmot.append(mot[index])
            elif motexistant[index] == mot[index]:
                continue
            else:
                acceptee = False
                print("le mot est incompatible avec les lettres qui existe!!")
    if acceptee and motexistant!=0 and not(vg.PremierTour):
        return lmot
    else:
        return []

#3
def verifie_main(main,liste_lettres):
    lmain = list(main)
    for elt in liste_lettres:
        if elt in lmain:
            lmain.remove(elt)
        elif "?" in lmain:
            lmain.remove("?")
        else:
            print("La main est insuffisante!!!")
            return False
    return True

def EnleverLesJetonsDeLaMain(jeton, lm,ligne,colonne):
    if not(jeton in lm):
        if '?' in lm:
            lm.remove("?")
            if len(vg.PosPremierJocker) == 0:
                vg.PosPremierJocker.extend([ligne,colonne])
            else:
                vg.PosDeuxiemeJocker.extend([ligne, colonne])
    else:
        lm.remove(jeton)

def VerifierSiPositionAuCentre(ligne,colonne):
    pos = [ligne,colonne]
    if vg.PremierTour and pos == [7,7]:
        vg.PremierTour = False

def VerifieSiLePremierMotPassParLeCentre(mot,dir,ligne,colonne):
    if dir == 'h':
        for i in range(len(mot)):
            VerifierSiPositionAuCentre(ligne,colonne)
            colonne += 1
    else:
        for i in range(len(mot)):
            VerifierSiPositionAuCentre(ligne,colonne)
            ligne += 1
    if vg.PremierTour:
        print("Le mot doit passer par le point centrale du tableau (7,7) !")

def placer_mot(plateau,lm,mot,i,j,dir):
    x = i
    y = j
    liste_lettres = tester_placement(plateau,x,y,dir,mot) # liste_lettres contient les lettres dont on est besoin
    mot_valide = verifie_mot(mot,liste_lettres)
    verifier_main = verifie_main(lm,liste_lettres) 
    let_util = 0
    while mot_valide:
        if len(liste_lettres) != 0 and verifier_main:
            if dir == 'h': #cas horizental
                for index in range(len(mot)):
                    lettre = lire_lettre(y,x,plateau)
                    if len(lettre) == 0 :
                        jeton = liste_lettres[let_util]
                        EnleverLesJetonsDeLaMain(jeton, lm,y,x)
                        j = [y,x]
                        affiche_jetons(j,jeton,plateau)
                        let_util += 1
                    x+=1
            elif dir == 'v': #cas vertical
                for index in range(len(mot)):
                    lettre = lire_lettre(y,x,plateau)
                    if len(lettre) == 0 :
                        jeton = liste_lettres[let_util]
                        EnleverLesJetonsDeLaMain(jeton, lm,y,x)
                        j = [y,x]
                        affiche_jetons(j,jeton,plateau)
                        let_util += 1
                    y+=1
            return True
        return False
    print("Mot Non Valide, Veiller réessayer ...")
    return False