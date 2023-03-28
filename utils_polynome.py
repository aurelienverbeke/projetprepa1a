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

    longueurMax = max([len(P1), len(P2)])
    somme = [0] * longueurMax
    
    for i in range(longueurMax):
        if i < len(P1):
            somme[i] += P1[i]
        if i < len(P2):
            somme[i] += P2[i]
    
    while somme[-1] == 0:
        somme.pop()
    
    return somme





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

    longueurMax = max([len(P1), len(P2)])
    diff = [0] * longueurMax
    
    for i in range(longueurMax):
        if i < len(P1):
            diff[i] += P1[i]
        if i < len(P2):
            diff[i] -= P2[i]
    
    while diff[-1] == 0:
        diff.pop()
    
    return diff










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

