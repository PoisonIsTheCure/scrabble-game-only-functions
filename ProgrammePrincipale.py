import plateau as plt
import pioche as pio
import ConstructionDesMots as cdm
import valeur_dun_mot as vdm
import PlacementDeMot as plm
import Boucle_De_Jeu as bdj


def principal():
    registre = {}
    lplateau = plt.init_jetons()
    dico = pio.init_dico()
    #sac = pio.init_pioche(dico)
    sac = ['A', 'A', '?', '?', '?', 'E', 'F', 'I', 'I', 'N', 'P', 'S', 'T', 'T', 'U', 'U', 'W', 'Z']
    #lplateau
    print(sac)
    while True:
        nb_joueur = int(input("Quelle est le nombre des joueurs (2-4): "))
        if 2<=nb_joueur<=4 : break
    for i in range(nb_joueur):
        registre[i] = pio.cree_joueurs(i,sac)
    print(registre)
    print(sac)
    while True:
        joueur = bdj.detect_tour(registre)
        nom = registre[joueur]["nom"]
        main = registre[joueur]["main"]
        fini = bdj.fin_partie(sac,main)
        print(sac)
        if fini : break
        pio.completer_main(main,sac)
        bdj.tour_joueur(lplateau , sac , main, nom,dico)
        print(registre[joueur])
    print("FIN DE LA PARTIE!!!")


principal()
