import plateau as plt
from plateau import affiche_jetons , affiche_plateau
import ConstructionDesMots as cdm
#1
def lire_coords():
    y = int(input("A Quelle ligne voulez vous commencer : "))
    x = int(input("A Quelle colonne : "))
    '''
    while lplateau[y][x] != '   ':
        y = int(input("A Quelle ligne voulez vous commencer : "))
        x = int(input("A Quelle colonne : "))
    '''
    return y,x
#2
def lire_lettre(y,x,plateau):
    ligne = y
    colonne = x
    print("ligne en fonction lire_lettre = ",ligne)
    print("colonne en fonction lire_lettre = ",colonne)
    lettre = plateau[ligne][colonne]
    print("la lettre lit par fonction lire_lettre avant enlever les choses = ",lettre)
    newstr = lettre.replace(' ','')
    thenewstr = newstr.replace('*','')
    recentstr = thenewstr.replace('-','')
    print("la lettre lit par fonction lire_lettre = ",recentstr)
    return recentstr

def lire_mot(plateau,x,y,mot,dirbool): #i c'
    lenmot = len(mot)
    motpl = []
    if dirbool: #cas horizental
        print(len(plateau[y]) - x)
        print(lenmot)
        if (len(plateau[y]) - x) < lenmot :
            return 0
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            x+=1
    elif not(dirbool): #cas vertical
        if (len(plateau) - y) < lenmot :
            return 0
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            y+=1
        print(f"liste donnée par lire_mot : {motpl}")
    return motpl

#ajouté par moi
def verifie_mot(mot,lmotexistant):
    mot.upper()
    lmot = list(mot)
    lmot.extend(lmotexistant)
    dict_fr = cdm.generer_dico()
    mots_possibles = cdm.mots_jouables(dict_fr, lmot)
    return True if mot in mots_possibles else False
    #a utiliser dans le fonction placer mot
    

def tester_placement(plateau,i,j,dir,mot):
    mot.upper()
    lmot = []
    acceptee = True
    if dir == 'h':
        dirbool = True
    if dir == 'v':
        dirbool = False
    motexistant = lire_mot(plateau,i,j,mot,dirbool)
    print("valeur retourner par lire_mot en tester_placement: ",motexistant)
    if motexistant != 0 :
        for index in range(len(motexistant)) :
            if motexistant[index] == "" :
                lmot.append(mot[index])
            elif motexistant[index] == mot[index]:
                continue
            else:
                acceptee = False
    if acceptee and motexistant!=0:
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
            return False
    return True

def placer_mot(plateau,lm,mot,i,j,dir):
    x = i
    y = j
    liste_lettres = tester_placement(plateau,x,y,dir,mot)
    print("valeur retourner par liste lettres en placer_mot: ",liste_lettres)
    mot_valide = verifie_mot(mot,liste_lettres)
    verifier_main = verifie_main(lm,liste_lettres) 
    print("valeur retourner par verifier main en placer_mot: ",verifier_main)
    let_util = 0
    while mot_valide:
        if len(liste_lettres) != 0 and verifier_main:
            if dir == 'h': #cas horizental
                for index in range(len(mot)):
                    lettre = lire_lettre(y,x,plateau)
                    if len(lettre) == 0 :
                        jeton = liste_lettres[let_util]
                        lm.remove(jeton)
                        j = [y,x]
                        affiche_jetons(j,jeton,plateau)
                        let_util += 1
                    x+=1
            elif dir == 'v': #cas vertical
                for index in range(len(mot)):
                    lettre = lire_lettre(y,x,plateau)
                    if len(lettre) == 0 :
                        jeton = liste_lettres[let_util]
                        lm.remove(jeton)
                        j = [y,x]
                        affiche_jetons(j,jeton,plateau)
                        let_util += 1
                    y+=1
            return True
        return False
    print("Mot Non Valide, Veiller réessayer ...")
    return False