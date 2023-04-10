# -*- coding: utf-8 -*-

""""
Authors:
    - BOURGOUIN Raphael
"""

from utils_polynome import derive_polyn, division, pgcd, deg, unitaire, evalue
from fractions import Fraction as F
import numpy as np
from math import inf

def Newton(f, a, b, epsilon):
    x = (a+b)/2
    y = x + 1e-3
    while abs(y - x) > epsilon:
        tmp = y
        y = y - f(y)*(y-x)/(f(y)-f(x))
        x = tmp
    return y

def racines_polyn(P, precision=1e-8, reduire=True, renvoyer_intervalles=False):

    if deg(P) == - inf:
        return []
    if deg(P) == 0:
        return []

    if reduire:
        P = [F(x) for x in P]
        P_prime = derive_polyn(P)
        Q = division(P, pgcd(P, P_prime))[0]

        Q = unitaire([float(x) for x in Q])
    else:
        Q = unitaire(P)

    if deg(Q) == 1:
        return [-Q[0]/Q[1]]
    if deg(Q) == 2:
        delta = Q[1]**2-4*Q[2]*Q[0]
        if delta > 0:
            x1 = (-Q[1]+np.sqrt(delta))/(2*Q[2])
            x2 = (-Q[1]-np.sqrt(delta))/(2*Q[2])
            if x1 > x2:
                return [x2, x1]
            else:
                return [x1, x2]
        if delta == 0:
            return [-Q[1]/(2*Q[2])]
        else:
            return []

    intervalles_derivee = racines_polyn(derive_polyn(Q), reduire=False, renvoyer_intervalles=True)
    mu = max(1, sum([abs(x) for x in Q[:-1]]))
    intervalles = [-mu-1e-3] + intervalles_derivee + [mu+1e-3]

    racines = []
    f = lambda x: evalue(Q, x)
    for i in range(len(intervalles)-1):
        if f(intervalles[i])*f(intervalles[i+1]) <= 0:
            racines.append(Newton(f, intervalles[i], intervalles[i+1], precision))

    if not renvoyer_intervalles:
        return racines

    nouveaux_intervalles = []
    i = 0
    j = 0
    while i < len(racines) and j < len(intervalles_derivee):
        if racines[i] < intervalles_derivee[j]:
            nouveaux_intervalles.append(racines[i])
            i += 1
        else:
            nouveaux_intervalles.append(intervalles_derivee[j])
            j += 1
    nouveaux_intervalles += racines[i:] + intervalles_derivee[j:]

    return nouveaux_intervalles
