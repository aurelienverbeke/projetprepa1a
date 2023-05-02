import numpy.polynomial.polynomial as poly
from utils_polynome import *
from tests import longueur_banque, utiliser_banque



n = longueur_banque("binaire")
print(n)



testsOk = 0

for i in range(n-1):
    P = utiliser_banque(i, "binaire")
    Q = utiliser_banque(i+1, "binaire")
    
    if poly.Polynomial(poly.polymul(P, Q)) == poly.Polynomial(produit(P, Q)):
        testsOk += 1

print(testsOk)



testsOk = 0

for i in range(n-1):
    P = utiliser_banque(i, "binaire")
    Q = utiliser_banque(i+1, "binaire")
    
    if poly.Polynomial(poly.polyadd(P, Q)) == poly.Polynomial(somme(P, Q)):
        testsOk += 1

print(testsOk)



testsOk = 0

for i in range(n-1):
    P = utiliser_banque(i, "binaire")
    Q = utiliser_banque(i+1, "binaire")
    
    if poly.Polynomial(poly.polysub(P, Q)) == poly.Polynomial(diff(P, Q)):
        testsOk += 1

print(testsOk)
