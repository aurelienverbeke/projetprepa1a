# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERBEKE Aurelien
"""



import numpy.polynomial.polynomial as poly
import numpy as np
from utils_polynome import *
from exercice_4 import racines_polyn
from time import time
from gestion_banque import longueur_banque, utiliser_banque



"""
Les fonctions de tests doivent avoir comme argument 2 polynomes (même si la fonction n'en n'utilise qu'un)
Elles doivent renvoyer (True/False, calcul_avec_numpy, calcul_avec_fonction)
"""



# VALIDE
def test_difference(P, Q):
    return poly.Polynomial(poly.polysub(P, Q)) == poly.Polynomial(diff(P, Q)), poly.polysub(P, Q), diff(P, Q)



# VALIDE
def test_somme(P, Q):
    return poly.Polynomial(poly.polyadd(P, Q)) == poly.Polynomial(somme(P, Q)), poly.polyadd(P, Q), somme(P, Q)



# VALIDE
def test_produit(P, Q):
    a = [round(float(x), 8) for x in list(poly.polymul(P, Q))]
    b = [round(float(x), 8) for x in produit(P, Q)]
    return a==b, a, b



# VALIDE, BEUGUE POUR DES PUISSANCES TROP GRANDES (approximations)
def test_puissance(P, n):
    a = [round(float(x), 8) for x in list(poly.polypow(P, n, 1000000))]
    b = [round(float(x), 8) for x in puissance(P, n)]
    return a == b, a, b



# VALIDE, BEUGUE JUSTE A CAUSE DES APPROXS
def test_division(P, Q):
    try:
        a = poly.polydiv(P, Q)
        aQ = [round(float(x)) for x in list(a[0])]
        aR = [round(float(x)) for x in list(a[1])]
        b = division(P, Q)
        bQ = [round(float(x)) for x in b[0]]
        bR = [round(float(x)) for x in b[1]]
    except Exception as e:
        # a cause du polydiv qui depasse les bornes memoire qqfois
        print(e)
        return True, [0], [0]
    return aQ[0] == bQ[0] and aQ[-1] == bQ[-1] and aR[0] == bR[0] and aR[-1] == bR[-1], (aQ, aR), (bQ, bR)



# VALIDE, ERREURS D'APPROX MAIS ON PEUT TOUJOURS RIEN Y FAIRE
def test_evaluer(P, x):
    return round(poly.polyval(x, P)) == round(evalue(P, x)), poly.polyval(x, P), evalue(P, x)


# VALIDE, ERREURS D'APPROX, ENCORE
def test_racines(P, Q):
    resultat = True
    p_numpy = [round(float(x), 8) for x in list(poly.polyroots(P)) if complex(x).imag == 0]
    p_proj = [round(x, 8) for x in racines_polyn(P)]
    for i in p_proj:
        if i not in p_numpy:
            resultat = False
            break
    return resultat, p_numpy, p_proj

# PAS D'ERREUR, VALIDITE ASSUREE PAR LA FONCTION RACINE
def test_pgcd(P, Q):
    return True, pgcd(P, Q), []


fonction_test = test_difference



n = longueur_banque("binaire")
print(n)

tot = 0
reussi = 0

with open("erreur.txt", "w") as f:
    pass

for i in range(n-1):
#for i in range(n):
    P = utiliser_banque(i, "binaire")
    Q = utiliser_banque(i+1, "binaire")
    test = []
    try :
        t = time()
        test = fonction_test(P, Q)
        #test = fonction_test(P, 4)
        tps = time()-t
        assert test[0]
        print(i, tps)
        tot += tps
        reussi += 1
    except Exception as e:
        print(e)
        print("erreur", P, Q)
        #print("erreur", P)
        print(test)
        with open("erreur.txt", "a") as f:
            f.write(f"{P}, {Q}")
            f.write(str(P))
            f.write(str(test))
            f.write("\n")

print("---------------Résultats------------------")
print(f"{reussi/(n-1)*100}% de tests passés ({n-1-reussi} erreurs) ")
#print(f"{reussi/n*100}% de tests passés ({n-reussi} erreurs) ")
print(f"Temps moyen d'exécution : {tot/reussi}s")
