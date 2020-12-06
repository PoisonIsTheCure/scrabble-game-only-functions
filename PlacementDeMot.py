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

def lire_mot(plateau,x,y,mot,dirbool): #i c'
    lenmot = len(mot)
    motpl = []
    if dirbool: #cas horizental
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
    print(plateau)
    print(motexistant)
    if acceptee:
        return lmot
    else:
        return []

lplateau[7][7] = " A*"
lplateau[8][7] = "*M*"
lplateau[11][7] = "-E-"
print(tester_placement(lplateau,7,7,'v','AMINE'))

#3
def placer_mot(plateau,lm,mot,i,j,dir):
