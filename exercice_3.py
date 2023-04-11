# -*- coding: utf-8 -*-

""""
Authors:
    - BOURGOUIN Raphael
"""

from fractions import Fraction as F
from utils_polynome import derive_polyn, pgcd, division, evalue, produit, puissance, polyn_to_str
from math import sqrt

R = [F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)]

# On calcule Q = R/(R^R')
R_prime = derive_polyn(R)
denominateur = pgcd(R, R_prime)
Q = division(R, denominateur)[0]
print(f"Question 1: R/(R^R') = {polyn_to_str(Q)}\n")

# -1 est bien une racine de Q
print(f"Question 2: Q(-1) = {evalue(Q, -1)}\n")

# On calcule les racines restantes de Q
T = division(Q, [1, 1])[0] # C'est un polynome de second degré
delta = T[1]**2-4*T[0]*T[2]
racine1 = F(-1)

# On utilise la formule
racine2 = F(int(-T[1] + sqrt(delta)), 2*T[2])
racine3 = F(int(-T[1] - sqrt(delta)), 2*T[2])
print(f"            Les racines de Q sont {racine1}, {racine2} et {racine3}\n")

multiplicite_racine1 = 1
multiplicite_racine2 = 1
multiplicite_racine3 = 1

derive_R = derive_polyn(R)
r1 = evalue(derive_R, racine1)
r2 = evalue(derive_R, racine2)
r3 = evalue(derive_R, racine3)

# Si r est une racine est d'ordre k, alors r est racine de la dérivee k-1 ieme mais pas de la dérivee k-ieme
while r1 == 0 or r2 == 0 or r3 == 0:
    derive_R = derive_polyn(derive_R)
    if r1 == 0:
        multiplicite_racine1 += 1
        r1 = evalue(derive_R, racine1)

    if r2 == 0:
        multiplicite_racine2 += 1
        r2 = evalue(derive_R, racine2)

    if r3 == 0:
        multiplicite_racine3 += 1
        r3 = evalue(derive_R, racine3)

print(f"Question 3: Les racines de R sont les mêmes que celles de Q, donc les racines de R sont {racine1}, {racine2} et {racine3}\n"
      f"            De plus:\n"
      f"            - La racine {racine1} est de multiplicité {multiplicite_racine1}\n"
      f"            - La racine {racine2} est de multiplicité {multiplicite_racine2}\n"
      f"            - La racine {racine3} est de multiplicité {multiplicite_racine3}\n")

pol_r1 = puissance([-racine1, F(1)], multiplicite_racine1)
pol_r2 = puissance([-racine2, F(1)], multiplicite_racine2)
pol_r3 = puissance([-racine3, F(1)], multiplicite_racine3)

# On trouve le polynome unitaire associé aux racines
R_uni = produit(produit(pol_r1, pol_r2), pol_r3)
R_exp = produit(R_uni, [24]) # On multiplie R_exp par le coefficient dominant de R
print(f"Question 4: On trouve en multipliant les racines le polynome {polyn_to_str(R_uni)}\n"
      f"            Donc en multipliant par dom(R), on retrouve bien R ({polyn_to_str(R_exp)})\n")