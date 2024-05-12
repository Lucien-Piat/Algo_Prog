"""
Lucien PIAT M1 Bioinfo 15/05/2024

Exercice 1 - Des arbres, des billes et des collisions
"""

def creer_boite(longueur, hauteur, orientation, billes, SO, NE): 
    return {
        "longueur":longueur, 
        "hauteur":hauteur, 
        "orientation":orientation, 
        "billes" : billes, 
        "SO" : SO, 
        "NE" : NE
        }

longueur = 3
hauteur = 3
orientation = "verticale"
billes = []
SO = (1,0)
NE = (2,3)




print(creer_boite(longueur, hauteur, orientation, billes, SO, NE))