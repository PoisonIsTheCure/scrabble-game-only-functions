import plateau as plt
import pioche as pio
import ConstructionDesMots as cdm
import valeur_dun_mot as vdm
import PlacementDeMot as plm
import Boucle_De_Jeu as bdj


def principal():
    registre = {}
    dico = pio.init_dico()
    sac = pio.init_pioche(dico)
    print(sac)
    while True:
        nb_joueur = int(input("Quelle est le nombre des joueurs (2-4): "))
        if 2<=nb_joueur<=4 : break
    for i in range(nb_joueur):
        registre[i] = pio.cree_joueurs(i,sac)
    print(registre)
    print(sac)

principal()
