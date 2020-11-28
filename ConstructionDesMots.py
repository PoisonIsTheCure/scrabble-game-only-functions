#1
def generer_dico(nf):
    """
    fonction reçois le nom de ficher et
    rnvoie un liste de son contenu
    """
    fichier = open(nf,"r")
    dictionnaire = []
    for ligne in fichier:
        mot = ligne[:-1]
        dictionnaire.append(mot)
    return dictionnaire

'''
#2 --> Script pour tester
f = 'littre.txt'
dictio = generer_dico(f)
for elt in dictio :
    if elt[0:3:].lower() == 'ali':
        print(elt)
'''

#3
def mot_jouable(mot, ll):
    liste = list(ll)
    existe = True
    for lettre in mot:
        if lettre.upper() in liste : # remarque : les lettres dans la liste doivent etre upper
            liste.remove(lettre.upper())
        elif '?' in liste:
            liste.remove('?')
        else:
            existe = False

    return existe

'''
#TEST DE L'EXERCICE 3
ll = ['A',"H","F","M","L","I"]
mot = 'ali'
print(mot_jouable(mot,ll))
'''

#4
def mots_jouables(motsfr, ll):
    ljouable = []
    for mot in motsfr:
        if mot_jouable(mot,ll):
            ljouable.append(mot)
    return ljouable

'''
#SCRIPT TEST POUR PARTIE 4
ll = ['A',"A","A","P","P","?","?","M","M","E","E","N","R"]
f = 'littre.txt'
dictio = generer_dico(f)
#print(dictio[0:30])
print(mots_jouables(dictio, ll))
'''

# TOUT LES FONCTIONS AU DESSUS ON ETAIENT TESTÉE
