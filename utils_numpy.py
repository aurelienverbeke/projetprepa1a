import numpy.polynomial.polynomial as poly
from utils_polynome import *
from exercice_4 import racines_polyn
from time import time
from tests import longueur_banque, utiliser_banque

"""
Les fonctions de tests doivent avoir comme argument 2 polynomes (même si la fonction n'en n'utilise qu'un)
Elles doivent renvoyer (True/False, calcul_avec_numpy, calcul_avec_fonction)
"""

def test_difference(P, Q):
    return poly.Polynomial(poly.polysub(P, Q)) == poly.Polynomial(diff(P, Q)), poly.polysub(P, Q), diff(P, Q)

def test_racines(P, Q):
    resultat = True
    p_numpy = [round(float(x), 8) for x in list(poly.polyroots(P)) if complex(x).imag == 0]
    p_proj = [round(x, 8) for x in racines_polyn(P)]
    for i in p_proj:
        if i not in p_numpy:
            resultat = False
            break
    return resultat, p_numpy, p_proj

fonction_test = test_racines

n = longueur_banque("binaire")
print(n)
tot = 0
reussi = 0
with open("erreur.txt", "w") as f:
    pass

for i in range(n-1):
    P = utiliser_banque(i, "binaire")
    Q = utiliser_banque(i+1, "binaire")
    test = []
    try :
        t = time()
        test = fonction_test(P, Q)
        tps = time()-t
        assert test[0]
        print(i, tps)
        tot += tps
        reussi += 1
    except Exception as e:
        print(e)
        print("erreur", P, Q)
        print(test)
        with open("erreur.txt", "a") as f:
            f.write(f"{P}, {Q}")
            f.write(test)
            f.write("\n")

print("---------------Résultats------------------")
print(f"{reussi/(n-1)*100}% de tests passés ({n-1-reussi} erreurs) ")
print(f"Temps moyen d'exécution : {tot/reussi}s")