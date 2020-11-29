import plateau as plt
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

def lire_mot(plateau,i,mot,dirbool):
    lenmot = len(mot)
    y = i[0]
    x = i[1]
    motpl = []
    if dirbool: #cas horizental
        return 0 if (len(lplateau[y]) - x) < lenmot
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            x+=1
    elif not(dirbool): #cas vertical
        return 0 if (len(lplateau) - y) < lenmot
        for index in range(lenmot):
            motpl.append(lire_lettre(y,x,plateau))
            y+=1
    return motpl

def tester_placement(plateau,i,j,dir,mot):
