#la pioche
#1
from random import randint

#2
def init_pioche(dico):
    l = []
    dk=list(dico.keys())
    dv=list(dico.values())
    for i in range (27):
        for j in range(dv[i]['occ']):
            l.append(dk[i])
    return l
#print(init_pioche(init_dico()))




#3
def piocher(x,sac):
    main=[]
    for i in range (x):
        a=randint(0,len(sac)-1)
        main.append(sac.pop(a))
    return main
#4
def completer_main(main,sac):
    if len(main)<7 :
        x = 7-len(main)
        liste = piocher(x,sac)
        main.extend(liste)
    return main

#5
def echanger(jetons ,main, sac):
    existe = True
    sacsuff = True
    for elt in jetons:
        existe = (elt in main) and existe
        sacsuff = (len(sac)>= len(jetons)) and sacsuff
    if sacsuff and existe :
        nouveau = piocher(len(jetons), sac)
        sac.extend(jetons)
        main.extend(nouveau)
        for elt in jetons:
            main.remove(elt)
        return True
    else:
        if not(existe) and not(sacsuff):
            print("Jetons non disponibles dans la main et sac insuffisant!")
        elif not(existe):
            print("Jetons non disponibles dans la main!")
        elif not(sacsuff):
            print("Sac insuffisant!")
        return False
#6
def cree_joueurs(i,sac):
    """
    creation du es joueurs avec un paramètre (nombre des joueurs),
    demande le nom des joueurs,
    renvoie un dictionnaire contenant les noms des joueurs comme cles
    chaque cle contient les lettre du pioche du joueurs
    """
    joueur = {}
    nb_joueur = i+1
    while True:
        name = input(f"Quelle est le nom de joueur numéro ({nb_joueur}) : ")
        if name.isalnum() : break
    main = piocher(7,sac)
    score = 0
    joueur["nom"]= name
    joueur["score"]= score
    joueur["main"]= main
    joueur["tour"] = False
    return joueur

#Tous les fonction on étaient testés et tout va bien
