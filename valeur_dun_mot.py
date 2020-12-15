import ConstructionDesMots as cdm
import plateau as plt
import PlacementDeMot as pdm
import VariablesGlobales as vg
import Boucle_De_Jeu as bdj


def LettreDoubleOuTriple(ligne,colonne,valeur):
    """
    verifie si un lettre est sur une position LT ou LD
    puis renvoi la valeur multiplier, sinon renvoi même valeur
    """
    pos = [ligne,colonne]
    if pos in vg.lbonus[2]: #verifie si lettre est double
        if vg.PosPremierJocker == pos : return 0
        if vg.PosDeuxiemeJocker == pos : return 0
        vg.lbonus[2].remove(pos)
        return 3*valeur
    elif pos in vg.lbonus[3]: #verifie lettre triple
        if vg.PosPremierJocker == pos : return 0
        if vg.PosDeuxiemeJocker == pos : return 0
        vg.lbonus[3].remove(pos)
        return 2*valeur
    else:
        if vg.PosPremierJocker == pos : return 0
        if vg.PosDeuxiemeJocker == pos : return 0
        return valeur

def MotDoubleOuTriple(ligne,colonne):
    """
    verifie si le mot est sur une position MT ou MD
    puis renvoi la valeur de multiplication, sinon renvoi 1
    """
    pos = [ligne,colonne]
    if pos in vg.lbonus[0]: #verifie si mot est double
        vg.lbonus[0].remove(pos)
        return 3
    elif pos in vg.lbonus[1]: #verifie mot triple
        vg.lbonus[1].remove(pos)
        return 2
    else:
        return 1

def valeur_mot(mot,dico,ligne=101,colonne=101,dir='h'):
    """
    Cette fonction calcule la valeur du mot seule,
    si elle reçoit des cooredonnées , elles le calcules avec bonus et cases spécialles
    """
    mot=mot.upper()
    mot=list(mot)
    somme=0
    if ligne==colonne==101:
        if len(mot)==7:
            somme=50
        for i in range(len(mot)):
            if mot[i] in dico.keys(): 
                valeur=dico[mot[i]]["val"]
                somme += valeur
        return somme
    else:
        MultiplierMot = 1
        if len(mot)==7:
            somme=50
        for i in range(len(mot)):
            if mot[i] in dico.keys(): 
                valeur=dico[mot[i]]["val"]
                somme += LettreDoubleOuTriple(ligne,colonne,valeur)
                MultiplierMot *= MotDoubleOuTriple(ligne,colonne)
            if bdj.dir == 'h': colonne += 1 # On Change ligne ou colonne pour pouvoir verifier la position et donner le bonus convenable
            if bdj.dir == 'v': ligne += 1
        ResultatFinal = somme*MultiplierMot
        return ResultatFinal


def meilleur_mot(motsfr,ll,dico):
    """Fonction qui calcule et renvoie le meilleur mot (de plus haute valeur
telle que calculée avec valeur mot), parmi les mots autorisés de la liste motsfr

    Args:
        motsfr (liste): la liste des mots autorisés
        ll (liste): liste des lettres

    Returns:
        string : retourne le meilleur mot
    """    
    haut_valeur=0
    meilleur=[]
    ljouable = cdm.mots_jouables(motsfr,ll)

    for i in range (len(ljouable)):
        valeur=valeur_mot(ljouable[i],dico)
        if valeur>haut_valeur:
            haut_valeur=valeur

    for i in range (len(ljouable)):
        valeur2=valeur_mot(ljouable[i],dico)
        if valeur2==haut_valeur:
            meilleur.append(ljouable[i])

    return meilleur