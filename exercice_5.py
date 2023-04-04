# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERBEKE Aurelien
    - VERGNOU Brice
"""
from utils_polynome import *
import matplotlib.pyplot as plt
from math import atan

def integrale_polynome(a,b,P):
    """
    Renvoie l'intégrale de P de a à b
    Args :
        - a (float) : la borne inférieure
        - b (float) : la borne supérieure
        - P (list) : le polynôme à intégrer
    Returns :
        float : le résultat de l'intégrale
    >>> P = [8,12,13,7,15]
    >>> integrale_polynome(1,12,P)
    791208.9166666666
    """
    primitive = primitive_polyn(P)
    # différence des primitives évaluées en b et a
    return evalue(primitive,b) - evalue(primitive,a) 

def lagrange(f,L):
    """
    Retourne un polynome de Lagrange qui approxime la fonction f aux points de L
    Pour tout x dans L, le polynome P généré donnera P(x) = f(x)
    Args:
        - f (function) : la fonction a approximer
        - L (list) : liste des points que doit couper le polynôme
    Returns :
        list : le polynôme de Lagrange associé
    >>> f = lambda x : 1/(1+25*x**2)
    >>> L = [0,1]
    >>> lagrange(f,L)
    [1.0, -0.9615384615384616]
    """
    n = len(L)
    P = [0]
    for i in range(n):
        x_k = L[:i] + L[i+1:] # liste des points sans x_i
        # le numérateur est un polynome de newton avec les points de x_k
        numerateur = poly_newton(x_k) 
        denominateur = 1
        # le dénominateur est le produit des x_i - x_k
        for x in x_k:
            denominateur *= (L[i]-x)
        Li = produit(numerateur,[1/denominateur]) # multiplication par un scalaire
        nouveau_terme = produit(Li, [f(L[i])])
        P = somme(P,nouveau_terme)
    return P

def integrale_fonction(a,b,f,n):
    h = (b-a)/n
    L = [a + i*h for i in range(n+1)]
    polynome_lagrange = lagrange(f,L)
    if n == 50:
        print(polyn_to_str(polynome_lagrange))
    return integrale_polynome(a,b,polynome_lagrange)

def rectm(a,b,f,n):
    h = (b-a)/n
    s = 0
    for i in range(1,n+1):
        s += f(a+i*h+h/2)
    return h*s

if __name__=="__main__":
    f = lambda x : 1/(1+25*x**2)
    a = -1
    b = 1
    result = (atan(5) - atan(-5)) / 5
    x = list(range(1,51))
    y_rect = []
    y_poly = []
    for n in x:
        y_rect.append(abs(
                rectm(a,b,f,n)-result
                ))
        y_poly.append(abs(
                integrale_fonction(a,b,f,n) - result
                ))
    plt.plot(x,y_poly,label="lagrange")
    plt.plot(x,y_rect,label="rectangles milieux")
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()