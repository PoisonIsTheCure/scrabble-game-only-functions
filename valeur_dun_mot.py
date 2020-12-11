import ConstructionDesMots as cdm
import plateau as plt

def LettreDoubleOuTriple(ligne,colonne,valeur):
    list_bonus = plt.init_bonus()
    pos = [ligne,colonne]
    if pos in list_bonus[2]: #verifie si lettre est double
        return 2*valeur
    elif pos in list_bonus[3]: #verifie lettre triple
        return 3*valeur
    else:
        return valeur

def MotDoubleOuTriple(ligne,colonne,valeurmot):
    list_bonus = plt.init_bonus()
    pos = [ligne,colonne]
    if pos in list_bonus[0]: #verifie si mot est double
        return 2*valeurmot
    elif pos in list_bonus[1]: #verifie mot triple
        return 3*valeurmot
    else:
        return valeurmot

def valeur_mot(mot,dico):
    mot=mot.upper()
    mot=list(mot)
    somme=0
    if len(mot)==7:
        somme=50
    for i in range(len(mot)):
       if mot[i] in dico.keys(): 
            valeur=dico[mot[i]]["val"]
            somme += valeur
    return somme

#dico=init_dico()
#print(valeur_mot("amine",dico))

def meilleur_mot(motsfr,ll,dico):
    haut_valeur=0
    meilleur=[]
    ljouable = cdm.mots_jouables(motsfr,ll)

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
