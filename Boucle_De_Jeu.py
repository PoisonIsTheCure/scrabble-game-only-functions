import plateau as plt
import pioche as pio
import PlacementDeMot as pdm
import valeur_dun_mot as vdm
import VariablesGlobales as vg

def DemanderDirection():
    while True:
        global dir
        dir = input("direction vertical (v) ou horizontal (h) ? : ")
        if dir == 'vertical' : dir = 'v'
        if dir == 'horizontal': dir = 'h'
        if dir in ('v','h') : break
    return dir

def EchangerLesJetons(main, sac):
    jetons_list=[]
    jetons = input("Ecrivez les jetons que vous souhaitez les echanger\nseparez les par des virgules : ")
    jetons = jetons.upper()
    jetonsf = jetons.replace(' ','')
    jetons_list = jetonsf.split(",")
    return pio.echanger(jetons_list,main,sac)

def PlacementMotEtCalculScore(lplateau , main,joueur,dico):
    coords = pdm.lire_coords()
    ligne = coords[0]
    colonne = coords[1]
    while True:
        mot = input("Quelle mot voulez vous placer : ")
        if mot.isalpha() : break
    mot = mot.upper()
    dir = DemanderDirection()
    PlacementReussit = pdm.placer_mot(lplateau,main,mot,colonne,ligne,dir)
    if PlacementReussit:
        global tempscore
        vg.registre[joueur]["score"] += vdm.valeur_mot(mot,dico,ligne,colonne,dir)
    return PlacementReussit

def tour_joueur(lplateau , sac , joueur,dico):
    nom = vg.registre[joueur]["nom"]
    main = vg.registre[joueur]["main"]
    plt.affiche_plateau(lplateau)
    print(f"C'est le tour de {nom} :")
    print(f"Votre Score est de {vg.registre[joueur]['score']} points.")
    print("Les lettres dans votre main sont : ",main)
    while True:
        ReponsesPossibles = ("echanger" , "e","placer" , "p","passer" , "s","sauvegarde","sortir")
        while True:
            Q1=input("Tapez 'sortir' pour sortir du Jeu\npasser (s), echanger (e), placer (p) ou 'sauvegarde' pour sauvegarder ? : ")
            Q1 = Q1.lower()
            if Q1.isalpha() and Q1 in ReponsesPossibles : break    
        if Q1 in ("echanger" , "e"):
            while True:
                echange = EchangerLesJetons(main, sac)
                if echange : break
            if echange : break
        elif Q1 in ("placer" , "p"):
            placer = PlacementMotEtCalculScore(lplateau,main,joueur,dico)
            if placer : break
        elif Q1 in ("passer" , "s"):
            break
        elif Q1 == "sauvegarde":
            vg.SauvegardeDeLaPartie(lplateau,sac)
        else:
            print("######   AU REVOIR   ######")
            quit()

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
    for key in registre.keys():
        statut = registre[key]["tour"]
        if statut == False:
            pass
        elif statut == True:
            div = len(registre.keys())-1 #return len of registre -1
            registre[key]["tour"] = False
            nouv = 0 if key == div else int(key)+1
            registre[nouv]["tour"] = True
            return key
    if tous_false:
        registre[1]["tour"] = True
        return 0

def ChercheLaValeurDuLettre(lettre):
    return vg.dico[lettre]["val"]

def SommeDesValeurDansLaMain(joueur):
    if len(vg.registre[joueur]['main']) == 0 : return 0
    valeur = 0
    for lettre in vg.registre[joueur]['main'] :
        valeur += ChercheLaValeurDuLettre(lettre)
    return valeur

def SoustractionDesScores():
    """
    Fonction qui calcule les valeurs finales des joueurs, en prenon compte des lettres dans leur main
    """
    ListeDesValeurs = []
    for joueur in range(len(vg.registre)):
        ListeDesValeurs.append(SommeDesValeurDansLaMain(joueur))
    for index in range(len(ListeDesValeurs)):
        if ListeDesValeurs[index] == 0:
            ValeurAjouté = 0
            for Valeur in ListeDesValeurs:
                if Valeur == 0:
                    ValeurAjouté += Valeur
            vg.registre[index]['score'] += ValeurAjouté
        else:
            vg.registre[index]['score'] -= ListeDesValeurs[index]

def FonctionDeFin(sac,plateau):
    plt.affiche_plateau(plateau)
    print(f"Les Lettres restant dans le sac sont : {sac}")
    SoustractionDesScores()
    ScoreJoueurs = []
    for joueur in vg.registre.keys():
        ScoreJoueurs.append(vg.registre[int(joueur)]['score'])
    Gangant = max(ScoreJoueurs)
    for joueur in range(len(vg.registre)):
        nom = vg.registre[joueur]["nom"]
        main = vg.registre[joueur]["main"]
        score = vg.registre[joueur]["score"]
        print(f"Les lettres restants dans la main de {nom} : {main}")
        print(f"Le score de {nom} est : {score}")
        if score == Gangant:
            print(f"~~~~~~{nom} A GAGNE LA PARTIE!!!~~~~~~")
        print("--------------------------------------------------")