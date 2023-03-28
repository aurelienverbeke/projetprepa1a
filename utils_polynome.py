# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERBEKE Aurelien
    - VERGNOU Brice
"""





# Aurelien

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
    longueurMax = max([len(P1), len(P2)])
    
    # on cree le nouveau polynome qui contiendra la somme des deux
    pSomme = [0] * longueurMax
    
    # on ajoute les coefficients de chaque monome au nouveau polynome, s'ils existent
    for i in range(longueurMax):
        if i < len(P1):
            pSomme[i] += P1[i]
        if i < len(P2):
            pSomme[i] += P2[i]
    
    # on supprime les coefficients nuls
    while pSomme[-1] == 0:
        pSomme.pop()
    
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
    longueurMax = max([len(P1), len(P2)])
    
    # on cree le nouveau polynome qui contiendra la difference des deux
    pDiff = [0] * longueurMax
    
    for i in range(longueurMax):
        # on ajoute les coefficients de chaque monome du premier polynome au nouveau polynome, s'ils existent
        if i < len(P1):
            pDiff[i] += P1[i]
        # on soustrait les coefficients de chaque monome du deuxieme polynome au nouveau polynome, s'ils existent
        if i < len(P2):
            pDiff[i] -= P2[i]
    
    # on supprime les coefficients nuls
    while pDiff[-1] == 0:
        pDiff.pop()
    
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

# Raphael

