# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERBEKE Aurelien
    - VERGNOU Brice
"""
from math import inf









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
    while pCopie[-1] == 0 and len(pCopie) > 1:
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

    # on recupere le degre maximal des deux polynomes
    degre = max([deg(P1), deg(P2)])

    # on cree le nouveau polynome qui contiendra la somme des deux
    pSomme = [0] * (degre + 1)

    # on ajoute les coefficients de chaque monome au nouveau polynome, s'ils existent
    for i in range(degre+1):
        if i < len(P1):
            pSomme[i] += P1[i]
        if i < len(P2):
            pSomme[i] += P2[i]

    # on supprime les coefficients nuls
    pSomme = reduire_coeff(pSomme)

    return pSomme





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

    # on recupere le degre maximal des deux polynomes
    longueurMax = max([deg(P1), deg(P2)])

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
    pDiff = reduire_coeff(pDiff)

    return pDiff










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


if __name__ == "__main__":
    with open("polyn.txt", "r") as f:
        for p in f.readlines():
            p = list(map(int, eval(p)))
            print(polyn_to_str(p))
    print(polyn_to_str([0, -2, -1, 0, 0, 3]))
