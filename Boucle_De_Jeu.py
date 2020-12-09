import plateau as plt
import pioche as pio
import PlacementDeMot as placement
def tour_joueur():
    list_plateau=plt.init_jetons()
    lplateau=plt.cree_plateau(list_plateau)
    sac=pio.init_pioche(pio.init_dico())
    main=pio.piocher(7,sac)
    print(main)
    Q1=input("passer,echange,placer ? ")
    if Q1=="echange":
        jetons_list=[]
        nb_jeton=int(input("combien des jetons vous voulez echange"))
        for i in range(nb_jeton):
            jetons=input("choisir un jeton")
            jetons_list.append(jetons)
        echange=pio.echanger(jetons_list,main,sac)
        print(main)
    elif Q1=="placer":
        mot=input("entrez un mot : ")
        ligne=int(input("ligne de depart ? "))
        colone=int(input("colone de depart ? "))
        dir=input("v ou h ? ")
        placer=placement.placer_mot(lplateau,main,mot,ligne,colone,dir)
        print(placer)
    elif Q1=="passer":
        pass
#print(tour_joueur())


#fonction qui détecte la fin de la partie
def fin_partie(sac,lm):
    if len(lm) == 7 :
        return True
    else:
        besoin = 7 - len(lm)
        if besoin > len(sac):
            return False
        else:
            return True
