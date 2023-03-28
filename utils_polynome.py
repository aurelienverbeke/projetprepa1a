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

# Brice


# Raphael

