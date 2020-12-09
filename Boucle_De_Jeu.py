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