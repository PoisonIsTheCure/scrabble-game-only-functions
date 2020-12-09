#fonction qui détecte la fin de la partie
def fin_partie(sac,lm):
    '''
    Fonction renvoie True tant que le sac est suffisant
    est False le sac est insuffisant
    '''
    if len(lm) == 7 :
        return True
    else:
        besoin = 7 - len(lm)
        if besoin > len(sac):
            return False
        else:
            return True