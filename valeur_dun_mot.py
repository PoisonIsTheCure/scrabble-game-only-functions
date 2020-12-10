def valeur_mot(mot,dico):
    mot=mot.upper()
    mot=list(mot)
    somme=0
    if len(mot)==7:
        somme=50
    for i in range(len(mot)):
       if mot[i] in dico.keys(): # !!! on a un sac pour quoi on cherche dans dico keys!!
            valeur=dico[mot[i]]["val"]
            somme +=valeur
    return somme

#dico=init_dico()
#print(valeur_mot("amine",dico))

def meilleur_mot(motsfr,ll,dico):
    haut_valeur=0
    meilleur=[]
    ljouable=mots_jouables(motsfr,ll)

    for i in range (len(ljouable)):
        valeur=valeur_mot(ljouable[i],dico)
        if valeur>haut_valeur:
            haut_valeur=valeur

    for i in range (len(ljouable)):
        valeur2=valeur_mot(ljouable[i],dico)
        if valeur2==haut_valeur:
            meilleur.append(ljouable[i])

    return meilleur
#dico=init_dico()
#print(meilleur_mot(["courir","pied","depit","tapir","marcher"],["P","I","D","E","T","A","R"],dico))
