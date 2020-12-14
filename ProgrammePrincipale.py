#!/usr/bin/env python3
import plateau as plt
import pioche as pio
import ConstructionDesMots as cdm
import valeur_dun_mot as vdm
import PlacementDeMot as plm
import Boucle_De_Jeu as bdj
import VariablesGlobales as vg


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
        nb_joueur = input("Quelle est le nombre des joueurs (2-4): ")
        if nb_joueur.isdigit():
            nb_joueur = int(nb_joueur)
            if 2<=nb_joueur<=4 : break
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

#help(pio)
principal()