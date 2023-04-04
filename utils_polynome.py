# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERBEKE Aurelien
    - VERGNOU Brice
"""
from math import inf
from time import time
from random import randint
import fractions as F









# Aurelien

def reduire_coeff(P):
    """
        Retire les coefficients nuls en fin de polynome
        Args:
            P (list): le polynome a reduire
        Returns:
            list: le polynome reduit
        Exemple:
            >>> reduire_coeff([1, 4, 3, 0, 0])
            [1, 4, 3]
    """

    # on copie le polynome pour ne pas travailler sur le polynome en entree
    # la copie de cette maniere est possible, la liste etant a une dimension
    pCopie = list(P)

    # on supprime les coefficients nuls
    while len(pCopie) > 1 and pCopie[-1] == 0:
        pCopie.pop()

    return pCopie





def somme(P1, P2):
    """
        Renvoie la somme de deux polynomes
        Args:
            - P1, P2 (list): deux polynomes a additionner
        Returns:
            list: somme des deux polynomes
        Exemple:
            >>> somme([4, 3, -2], [3, 6, 2])
            [7, 9]
    """
    
    # si un des polynomes est nul, on renvoie l'autre
    if deg(P1) == -inf:
        return P2
    if deg(P2) == -inf:
        return P1

    # on recupere le degre maximal des deux polynomes
    degre = max(deg(P1), deg(P2))

    # on cree le nouveau polynome qui contiendra la somme des deux
    pSomme = [0] * (degre + 1)

    # on ajoute les coefficients de chaque monome au nouveau polynome, s'ils existent
    for i in range(degre+1):
        if i < len(P1):
            pSomme[i] += P1[i]
        if i < len(P2):
            pSomme[i] += P2[i]

    # on supprime les coefficients nuls
    return reduire_coeff(pSomme)





def diff(P1, P2):
    """
        Renvoie la difference de deux polynomes (premier moins deuxieme)
        Args:
            - P1, P2 (list): deux polynomes a soustraire
        Returns:
            list: difference des deux polynomes
        Exemple:
            >>> diff([4, 3, -2], [3, 6, 2])
            [1, -3, -4]
    """
    
    # si un des polynomes est nul, on renvoie l'autre
    if deg(P1) == -inf:
        return P2
    if deg(P2) == -inf:
        return P1

    # on recupere le degre maximal des deux polynomes
    degre = max(deg(P1), deg(P2))

    # on cree le nouveau polynome qui contiendra la difference des deux
    pDiff = [0] * (degre + 1)

    for i in range(degre + 1):
        # on ajoute les coefficients de chaque monome du premier polynome au nouveau polynome, s'ils existent
        if i < len(P1):
            pDiff[i] += P1[i]
        # on soustrait les coefficients de chaque monome du deuxieme polynome au nouveau polynome, s'ils existent
        if i < len(P2):
            pDiff[i] -= P2[i]

    # on supprime les coefficients nuls
    return reduire_coeff(pDiff)





def produit(P1, P2):
    """
        Renvoie le produit de deux polynomes
        Args:
            - P1, P2 (list): deux polynomes a multiplier
        Returns:
            list: produit de deux polynomes
        Exemple:
            >>> produit([0, 0, 4, 3], [1, 2])
            [0, 0, 4, 11, 6]
    """

    if deg(P1) == - inf or deg(P2) == - inf:
        return [0]

    # on cree le nouveau polynome
    pProd = [0]*(deg(P1)+deg(P2)+1)

    P1 = reduire_coeff(P1)
    P2 = reduire_coeff(P2)

    for puissance1, valeur1 in enumerate(P1):
        for puissance2, valeur2 in enumerate(P2):
            # on calcule le produit de deux coefficients et on l'ajoute dans la bonne case correspondant a la bonne puissance de X
            pProd[puissance1 + puissance2] += valeur1*valeur2

    # on en profite pour enlever les coefficients inutiles
    return pProd





def evalue(P, x):
    """
        Evalue un polynome en nombre grace a l'algorithme d'Horner
        Args:
            - P list: le polynome a evaluer
            - x float: la valeur en laquelle evaluer le polynome
        Returns:
            float: la valeur du polynome en x donne
        Exemple:
            >>> evalue([1, 2, 3], 4)
            57.0
    """

    P = reduire_coeff(P)

    if deg(P) == -inf:
        return 0.0

    n = deg(P)

    valeur = P[n]
    for i in range(n-1,-1,-1):
        valeur = valeur*x + P[i]

    return float(valeur)





def poly_newton(L):
    """
        Retourne le polynome de newton associe a une liste de coefficients
        Args:
            L list: coefficients
        Returns:
            list: le polynome de newton correspondant aux coefficients fournis
        Exemple:
        >>> poly_newton([1, 2, 3])
        [-6, 11, -6, 1]
    """

    P = [-L[0], 1]

    for i in range(1, len(L)):
        P = produit(P, [-L[i], 1])

    return P





def division(P1, P2):
    """
        Effectue la division euclidienne du polynome 1 par le polynome 2
        Args:
            - P1, P2 (list): les polynomes a diviser
        Returns:
            tuple: quotient et reste de la division euclidienne
    """
    P1 = reduire_coeff(P1)
    P2 = reduire_coeff(P2)
    quotient = [0]
    
    while(deg(P1) >= deg(P2)):
        monomeMultiplicatif = monome(deg(P1) - deg(P2))
        coeffMultiplicatif = P1[-1] / P2[-1]
        aSoustraire = produit(produit(monomeMultiplicatif, P2), [coeffMultiplicatif])
        quotient = somme(quotient, produit(monomeMultiplicatif, [coeffMultiplicatif]))
        P1 = diff(P1, produit(produit(monomeMultiplicatif, P2), [coeffMultiplicatif]))

    return (quotient, P1)





def est_divisible(P1, P2):
    """
        Dit si le polynome 1 est divisible par le polynome 2
        S'il l'est, le reste de la division euclidienne sera donc de 0
        Args:
            - P1, P2 (list) : les polynomes pour lesquels ont doit determiner la divisibilite
        Returns:
            bool: True si P1 est divisible par P2, False sinon
    """
    return division(P1, P2)[1] == [0]










# Brice

def monome(n):
  """
    Renvoie une liste de coefficients par ordre de puissances croissantes
    correspondant au monome X^n
    Args:
        - n (int >=0 ): degré du monome
    Returns :
        list : liste de coefficients du monômes
    Exemple :
      >>> monome(4)
      [0, 0, 0, 0, 1]
    """
  return [0]*(n) + [1]

def deg(P):
  """
    Renvoie le degré du polynôme passé en entrée  
    Args:
        - P (list): le polynôme
    Returns :   
        int or float : le degré du polynôme
    Exemple :
      >>> deg([0])
      -inf
      >>> deg([5,6,3,0])
      2
  """
  P = reduire_coeff(P)
  degre = len(P) - 1
  if degre == 0 and P[0] == 0:
    return - inf
  else:
    return degre







# Raphael

def polyn_to_str(P):
    """
    Renvoie la chaine de caractères représentant le polynôme P, sous la forme "a X**n + b X**(n-1) + ... "
    Args:
        - P (list): le polynome à représenter
    Returns:
        str: Chaine de caractères représentant le polynômes
    Exemple:
        >>> polyn_to_str([1, -2, -1, 0, 1, 3])
        "3 X**5 + X**4 - X**2 - 2 X + 1"
    """
    chaine = ""
    for i in range(len(P) - 1, -1, -1):
        if P[i] != 0:

            # On détermine le signe du coefficient
            if P[i] / abs(P[i]) > 0:
                signe = "+"
            else:
                signe = "-"

            # On construit le coefficient, si sa valeur absolue est égale à 1, on affiche uniquement le signe
            if abs(P[i]) == 1 and i != 0:
                coef = f"{signe} "
            else:
                coef = f"{signe} {abs(P[i])} "

            # On construit le monome X**i, en ne gardant que X si son degré et de 1 et rien si son degré est de 0
            if i == 1:
                monome = "X "
            elif i == 0:
                monome = " "
            else:
                monome = f"X**{i} "
            chaine += coef + monome
    return chaine.strip("+ ")


def unitaire(P):
    """
    Revoie le polynome unitaire correspondant a P
    Args:
         - P (list): Le polynome que l'on veut transformer en polynome unitaire
    Returns:
        list: Le polynome unitaire correspondant à P
    Exemple:
        >>> unitaire([2, -7, -6, 34, 10, -63, -22, 44, 24])
        [0.08333333333333333, -0.2916666666666667, -0.25, 1.4166666666666667, 0.4166666666666667, -2.625, -0.9166666666666666, 1.8333333333333333, 1.0]
    """
    if P == [0]:
        return [0]
    elif P[-1] == 1:
        return reduire_coeff(P)

    p_unitaire = reduire_coeff(P)
    coef_dominant = p_unitaire[-1]
    p_unitaire = [x/coef_dominant for x in p_unitaire]
    return p_unitaire

"""
def produit(P, Q):
    if len(P) == 1:
        return [P[0]*x for x in Q]
    if len(Q) == 1:
        return [Q[0]*x for x in P]
    if P == [0] or Q == [0]:
        return [0]

    degreeP = deg(P)
    degreeQ = deg(Q)
    n = max(degreeP, degreeQ) + 1
    if n % 2 == 1 : n += 1

    n //= 2

    P1 = P[:max(n, degreeP)]
    Q1 = Q[:max(n, degreeQ)]
    P2 = P[max(n, degreeP):]
    Q2 = Q[max(n, degreeQ):]

    if not P2: P2 = [0]
    if not Q2: Q2 = [0]

    E1 = produit(P1, Q1)
    E2 = produit(P2, Q2)
    E3 = produit(somme(P1, P2), somme(Q1, Q2))

    print(P1, Q1, P2, Q2, n)
    print(E1, E2, E3, n)

    P_inter = [0]*n + diff(diff(E3, E1), E2)
    P_extr = [0]*(2*n) + E2

    print(somme(somme(E1, P_inter), P_extr), P, Q)

    return somme(somme(E1, P_inter), P_extr)
"""
def puissance_opti(P, n, stockage={}):
    P = list(P)
    if n == 0:
        return [1]
    if n == 1:
        return P
    if n % 2 == 0:
        T = stockage.get(n//2, None)
        if T is None:
          T = puissance_opti(P, n//2, stockage=stockage)
          stockage[n//2] = T
        return produit(T, T)
    else:
        T = stockage.get((n-1)//2, None)
        if T is None:
          T = puissance_opti(P, (n-1)//2, stockage=stockage)
          stockage[(n-1)//2] = T
        return produit(produit(T, T), P)


def puissance(P, n):
    """
    Renvoie le polynôme P^n
    Args:
         - P (list): Le polynôme à mettre à la puissance
         - n (int): La puissance
    Returns:
        - list: Le polynome P^n
    Exemple:
        >>> puissance([1, 1], 2)
        [1, 2, 1]
    """
    if n == 0:
        return monome(0)

    P = list(P)
    T = list(P)
    for i in range(n-1):
        P = produit(P, T)
    return P


def derive_polyn(P):
    """
    Dérive le polynome
    Args:
        - P (list): Le polynome à dériver
    Returns:
        list: Le polynome dérivé
    Exemple:
        >>> derive_polyn([1, 1])
        [1]
    """
    derive_P = []
    for i, x in enumerate(P[1:]):
        derive_P.append((i+1)*x)
    return derive_P


def primitive_polyn(P):
    """
    Renvoie le polynome primitif de coefficient constant nul
    Args:
        - P (list): Le polynome à primitiver
    Returns:
        list: Le polynome primitif
    Exemple:
        >>> primitive_polyn([1, 1])
        [0, 1, .5]
    """
    primitive_P = [0]
    for i, x in enumerate(P):
        primitive_P.append(x/(i+1))
    return primitive_P


if __name__ == "__main__":
    P = [randint(0, 100) for x in range(100)]
    n = 50
    t = time()
    puissance(P, n)
    print(time() - t)
    t = time()
    puissance_opti(P, n)
    print(time() - t)
