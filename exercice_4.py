# -*- coding: utf-8 -*-

""""
Authors:
    - BOURGOUIN Raphael
"""

from utils_polynome import derive_polyn, division, pgcd, deg, unitaire, evalue
from fractions import Fraction as F
import numpy as np
from math import inf
from time import time
from exercice_1 import tchebychev

def Newton(f, a, b, epsilon):
    """
    Trouve le zéro de f présent entre a et b avec une précision de epsilon
    Args:
         - f (lambda) : la fonction pour laquelle on cherches le zéro
         - a (float) : le minimum de l'intervalle de recherche
         - b (float) : le maximum de l'intervalle de recherche
         - epsilon (float) : la précision
    Returns:
        float : le zéro de f
    """
    # Sachant que souvent a et b seront des zéros d'une des dérivées
    # On préfèrera prendre x et y au milieu de l'intervalle afin de s'en éloigner
    x = (a+b)/2
    y = x + 1e-3

    # On utilise le principe de la méthode de Newton
    while abs(y - x) > epsilon:
        tmp = y
        y = y - f(y)*(y-x)/(f(y)-f(x))
        x = tmp
    return y

def racines_polyn(P, precision=1e-8, reduire=False, renvoyer_intervalles=False):
    """
    Revoie la liste des racines d'un polynome
    Args:
        - P (list) : le polynome pour lequel on veut les racines
        - precision : la precision des racines
        - reduire : True si l'on veut reduire le polynome avec Q = P/pgcd(P, P_prime), le laisser à false rend très souvent
        la fonction plus rapide
        - renvoyer_intervalles : Doit être laissé à False
    """

    # Si le polynome est constant, on considère qu'il n'a pas de racines
    if deg(P) == - inf:
        return []
    if deg(P) == 0:
        return []

    if reduire:
        # On réduit le polynôme pour avoir un polynôme plus petit mais avec les même racines
        P = [F(x) for x in P]
        P_prime = derive_polyn(P)
        Q = division(P, pgcd(P, P_prime))[0]

        Q = unitaire([float(x) for x in Q])
    else:
        Q = unitaire(P)

# ------------------CAS DE BASE-------------------
    # Si le polynôme est de degré 1 ou 2 on utilise les formules que l'on connait pour revoyer les racines
    if deg(Q) == 1:
        return [-Q[0]/Q[1]]
    if deg(Q) == 2:
        delta = Q[1]**2-4*Q[2]*Q[0]
        if delta > 0:
            x1 = (-Q[1]+np.sqrt(delta))/(2*Q[2])
            x2 = (-Q[1]-np.sqrt(delta))/(2*Q[2])
            # Il faut ordoner les racines
            if x1 > x2:
                return [x2, x1]
            else:
                return [x1, x2]
        if delta == 0:
            return [-Q[1]/(2*Q[2])]
        else:
            return []

# ------------------RECURSIVITE-------------------
    # On récupère les racines de toutes les dérivées du polynôme

    # Même si les dérivées premières et secondes sont suffisantes pour garantir la convergence, si l'on ne considère que
    # les racines de la dérivée première et seconde, il arrive que la suite de Newton sorte de l'intervalle
    # la même chose arrive si l'on considère aussi les racines de la dérivée troisième
    racines_derivees = racines_polyn(derive_polyn(Q), reduire=False, renvoyer_intervalles=True)

    # On calcule l'intervalle dans lequel les racines sont situées
    mu = max(1, sum([abs(x) for x in Q[:-1]]))

    # On obtient un subdivision de l'intervalle [-mu, mu] pour lequel il y a au maximum une racine dans chaque intervalle
    # de cette subdivision
    intervalles = [-mu-1e-3] + racines_derivees + [mu+1e-3]

    racines = []
    f = lambda x: evalue(Q, x)
    for i in range(len(intervalles)-1):
        a = intervalles[i]
        b = intervalles[i+1]

        # On ajoute si nécéssaire les racines des dérivées
        if renvoyer_intervalles and i > 0:
            racines.append(a)

        # On applique un TVI afin de vérifier l'existence d'un racine dans l'intervalle
        if f(a)*f(b) <= 0:
            # On calcule la racine grâce à la méthode de Newton
            racines.append(Newton(f, a, b, precision))

    return racines
