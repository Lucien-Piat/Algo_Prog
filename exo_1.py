"""
Lucien PIAT M1 Bioinfo 15/05/2024

Exercice 1 - Des arbres, des billes et des collisions
"""

def inserer_ab(A, pere, fils, etiquette=None, type_fils=None):
    if fils is None:
        return
    if not pere is None:
        A[type_fils][pere] = fils
        A['pere'][fils] = pere
        A['fils_gauche'][fils] = None
        A['fils_droit'][fils] = None
        A['etiquettes'][fils] = etiquette


def creer_arbre_vide():
    return {
    'racine' : None,
    'etiquettes' : {},
    'fils_droit' : {},
    'fils_gauche' : {},
    'pere' : {}
    }

def creer_arbre(racine=None, etiquette=None):
    res = creer_arbre_vide()
    inserer_racine(res, racine, etiquette)
    return res

def inserer_racine(A, racine, etiquette=None):
    A['racine'] = racine
    inserer_ab(A, None, racine, etiquette, type_fils=None)


def inserer_fils_gauche(A, pere, fils, etiquette=None):
    inserer_ab(A, pere, fils, etiquette=etiquette, type_fils='fils_gauche')

def inserer_fils_droit(A, pere, fils, etiquette=None):
    inserer_ab(A, pere, fils, etiquette=etiquette, type_fils='fils_droit')


def nouvelle_etiquette(longueur, hauteur, orientation, SO, NE, billes=[]): 
    return {
        "longueur":longueur, 
        "hauteur":hauteur, 
        "orientation":orientation, 
        "billes" : billes, 
        "SO" : SO, 
        "NE" : NE
        }

def construire_arbre_collision(H,L,nb_etape):
    etiquette_racine = nouvelle_etiquette(L, H, "verticale", (0,0), (L,H))
    A = creer_arbre(etiquette = etiquette_racine)

construire_arbre_collision(6,6,1)