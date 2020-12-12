import plateau as plt
import pioche as pio
import PlacementDeMot as pdm
import valeur_dun_mot as vdm
"""
def tour_joueur(lplateau , sac , main):
    #list_plateau=plt.init_jetons()
    #lplateau=plt.affiche_plateau(list_plateau)
    #sac=pio.init_pioche(pio.init_dico())
    main=pio.piocher(7,sac)
    print(main)
    Q1.lower()=input("passer,echange,placer ? ")
    if Q1.lower()=="echange":
        jetons_list=[]
        nb_jeton=int(input("combien des jetons vous voulez echange"))
        for i in range(nb_jeton):
            jetons=input("choisir un jeton")
            jetons_list.append(jetons)
        echange=pio.echanger(jetons_list,main,sac)
        print(main)
    elif Q1.lower()=="placer":
        mot=input("entrez un mot : ")
        ligne=int(input("ligne de depart ? "))
        colone=int(input("colone de depart ? "))
        dir=input("v ou h ? ")
        placer=pdm.placer_mot(lplateau,main,mot,ligne,colone,dir)
        print(placer)
    elif Q1.lower()=="passer":
        pass
#print(tour_joueur())
"""
def DemanderDirection():
    while True:
        dir = input("direction vertical (v) ou horizontal (h) ? : ")
        if dir == 'vertical' : dir = 'v'
        if dir == 'horizontal': dir = 'h'
        if dir in ('j','h') : break
    return dir

def EchangerLesJetons(main, sac):
    jetons_list=[]
    jetons = input("Ecrivez les jetons que vous souhaitez les echanger\nseparez les par des virgules : ")
    jetons = jetons.upper()
    jetonsf = jetons.replace(' ','')
    jetons_list = jetonsf.split(",")
    return pio.echanger(jetons_list,main,sac)

def PlacementMotEtCalculScore(lplateau , main,dico):
    coords = pdm.lire_coords()
    ligne = coords[0]
    colonne = coords[1]
    mot = input("Quelle mot voulez vous placer : ")
    mot = mot.upper()
    dir = DemanderDirection()
    PlacementReussit = pdm.placer_mot(lplateau,main,mot,colonne,ligne,dir)
    if PlacementReussit:
        global tempscore
        tempscore = vdm.valeur_mot(mot,dico,ligne,colonne)
    return PlacementReussit

def tour_joueur(lplateau , sac , main, nom,dico):
    plt.affiche_plateau(lplateau)
    print(f"C'est le tour de {nom} :")
    print("Les lettres dans votre main sont : ",main)
    Q1=input("passer (s), echanger (e), placer (p) ? : ")
    Q1 = Q1.lower()
    if Q1 in ("echanger" , "e"):
        while True:
            echange = EchangerLesJetons(main, sac)
            if echange : break
        print(main)
    elif Q1 in ("placer" , "p"):
        while True:
            placer = PlacementMotEtCalculScore(lplateau,main,dico)
            if placer : break
            print("valeur retourner par placer en tour_joueur: ",placer)
    elif Q1 in ("passer" , "s"):
        pass

#fonction qui détecte la fin de la partie
def fin_partie(sac,lm):
    '''
    Fonction renvoie False tant que le sac est suffisant
    est True le sac est insuffisant
    '''
    if len(lm) == 7 :
        return False
    else:
        besoin = 7 - len(lm)
        return besoin > len(sac)

def detect_tour(registre):
    tous_false = True
    for i in range(len(registre.keys())):
        statut = registre[i]["tour"]
        if statut == False:
            pass
        elif statut == True:
            div = len(registre.keys())-1 #return len of registre -1
            registre[i]["tour"] = False
            nouv = 0 if i == div else i+1
            registre[nouv]["tour"] = True
            return i
    if tous_false:
        registre[1]["tour"] = True
        return 0
