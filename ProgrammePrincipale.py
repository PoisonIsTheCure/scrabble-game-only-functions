#!/usr/bin/env python3
import plateau as plt
import pioche as pio
import ConstructionDesMots as cdm
import valeur_dun_mot as vdm
import PlacementDeMot as plm
import Boucle_De_Jeu as bdj
import VariablesGlobales as vg
import json

def principal():
    """Cette fonction est la fonction principale , dès qu'elle est appeler elle commence
    a appliquer les instructions
    """    
    vg.init_registre()
    vg.init_bonus()
    lplateau = plt.init_jetons()
    dico = vg.init_dico()
    sac = pio.init_pioche(dico)
    #sac = ['A', 'A', '?', '?', '?', 'E', 'F', 'I', 'I', 'N', 'P', 'S', 'T', 'T', 'U', 'U', 'W', 'Z']
    #sac = ['A', 'A', '?', '?', '?', 'E', 'F', 'I', 'I', 'N', 'P', 'S', 'T', 'T']
    #lplateau
    while True:
        nb_joueur = input("Si une Partie Sauvegarder existe,\nRecharger la en ecrivant 'recharge'\nQuelle est le nombre des joueurs (2-4): ")
        if nb_joueur.isdigit():
            nb_joueur = int(nb_joueur)
            if 2<=nb_joueur<=4 : break
        elif nb_joueur.lower() == 'recharge':
            ChargementPartiePrecedente()
    for i in range(nb_joueur):
        vg.registre[i] = pio.cree_joueurs(i,sac)
    while True:
        joueur = bdj.detect_tour(vg.registre)
        nom = vg.registre[joueur]["nom"]
        main = vg.registre[joueur]["main"]
        fini = bdj.fin_partie(sac,main)
        if fini : break
        pio.completer_main(main,sac)
        bdj.tour_joueur(lplateau , sac ,joueur,dico)
    print("###---FIN DE LA PARTIE!!!---###")
    bdj.FonctionDeFin(sac,lplateau)

def PrincipalSauvegarde():
    """Cette fonction est la fonction principale , dès qu'elle est appeler elle commence
    a appliquer les instructions
    """    
    lplateau = LePlateau
    dico = vg.init_dico()
    sac = LeSac
    while True:
        joueur = bdj.detect_tour(vg.registre)
        nom = vg.registre[joueur]["nom"]
        main = vg.registre[joueur]["main"]
        fini = bdj.fin_partie(sac,main)
        if fini : break
        pio.completer_main(main,sac)
        bdj.tour_joueur(lplateau , sac ,joueur,dico)
    print("###---FIN DE LA PARTIE!!!---###")
    bdj.FonctionDeFin(sac,lplateau)

def ChargementPartiePrecedente():
    vg.init_registre()
    vg.init_bonus()
    try:
        DicoSauvegarde = json.load(open("partie-scrabble.json"))
    except FileNotFoundError:
        print("^^^Pas de Partie Sauvegarder^^^")
        principal()
    vg.registre = DicoSauvegarde['registre']
    print(vg.registre)
    listes_cles = list(vg.registre.keys())
    for key in listes_cles:
        vg.registre[int(key)] = vg.registre.pop(key)
    vg.PosPremierJocker = DicoSauvegarde['PosPremierJocker']
    vg.PosDeuxiemeJocker = DicoSauvegarde['PosDeuxiemeJocker']
    vg.lbonus = DicoSauvegarde['lbonus']
    vg.PremierTour = DicoSauvegarde['PremierTour']
    global LeSac
    LeSac = DicoSauvegarde['sac']
    global LePlateau
    LePlateau = DicoSauvegarde['plateau']
    print("~~~~~~Partie Recharger~~~~~~")
    PrincipalSauvegarde()

while True:
    principal()
    while True:
        reponse = input("Vouler vous rejouer?? (oui/non)")
        if reponse.isalpha() and reponse.lower() in ('oui','non') :
            reponse = reponse.lower()
            break
    if reponse == 'oui':
        principal()
    else:
        quit()