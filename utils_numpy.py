import numpy.polynomial.polynomial as poly
from utils_polynome import produit
from tests import longueur_banque, utiliser_banque

n = longueur_banque("binaire")
for i in range(n-1):
    P = utiliser_banque(i, "binaire")
    Q = utiliser_banque(i+1, "binaire")
    try:
        assert poly.Polynomial(poly.polymul(P, Q)) == poly.Polynomial(produit(P, Q)), (P, Q, poly.polymul(P, Q), poly.Polynomial(produit(P, Q)))
    except Exception as e:
        print(e, P, Q)