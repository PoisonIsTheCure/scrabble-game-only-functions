import plateau as plt
from plateau import affiche_jetons , affiche_plateau
lplateau = plt.init_jetons()
#1
def lire_coords():
    y = int(input("A Quelle ligne voulez vous commencer : "))
    x = int(input("A Quelle colonne : "))
    while lplateau[y][x] != '   ':
        y = int(input("A Quelle ligne voulez vous commencer : "))
        x = int(input("A Quelle colonne : "))
    return y,x
#2
def lire_lettre(y,x,plateau):
    ligne = y
    colonne = x
    lettre = lplateau[ligne][colonne]
    newstr = lettre.replace(' ','')
    thenewstr = newstr.replace('*','')
    recentstr = thenewstr.replace('-','')
    return recentstr

def lire_mot(plateau,x,y,mot,dirbool): #i c'
    lenmot = len(mot)
    motpl = []
    if dirbool: #cas horizental
        print(len(lplateau[y]) - x)
        print(lenmot)
        if (len(lplateau[y]) - x) < lenmot :
            return 0
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            x+=1
    elif not(dirbool): #cas vertical
        if (len(lplateau) - y) < lenmot :
            return 0
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            y+=1
    return motpl

def tester_placement(plateau,i,j,dir,mot):
    mot.upper()
    lmot = []
    acceptee = True
    if dir == 'h':
        dirbool = True
    if dir == 'v':
        dirbool = False
    motexistant = lire_mot(plateau,i,j,mot,dirbool)
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
def placer_mot(plateau,lm,mot,i,j,dir):
    x = i
    y = j
    liste_lettres = tester_placement(plateau,x,y,dir,mot)
    verifier_main =  all(item in lm for item in liste_lettres)
    let_util = 0
    if len(liste_lettres) != 0 and verifier_main:
        if dir == 'h': #cas horizental
            for index in range(len(mot)):
                lettre = lire_lettre(y,x,plateau)
                if len(lettre) == 0 :
                    jeton = liste_lettres[let_util]
                    j = [y,x]
                    affiche_jetons(j,jeton,plateau)
                    let_util += 1
                x+=1
        elif dir == 'v': #cas vertical
            for index in range(len(mot)):
                lettre = lire_lettre(y,x,plateau)
                if len(lettre) == 0 :
                    jeton = liste_lettres[let_util]
                    j = [y,x]
                    affiche_jetons(j,jeton,plateau)
                    let_util += 1
                y+=1
        return True
    return False
lm= ['I','N','A','M','E','K']
lplateau[7][7] = " A*"
lplateau[8][7] = "*M*"
lplateau[11][7] = "-E-"
#print(tester_placement(lplateau,7,7,'v','AMINE'))
print(placer_mot(lplateau,lm,'AMINE',7,11,'h'))
affiche_plateau(lplateau)
print(lm)