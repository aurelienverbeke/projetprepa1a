# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERBEKE Aurelien
    - VERGNOU Brice
"""

from utils_polynome import puissance

def binom(n):
    """
    Renvoie une liste des coefficients binomiaux k parmi n avec 0 <= k <= n
    Args :
        n (int >= 0) : la ligne du triangle de Pascal
    Returns :
        list : les coef binomiaux de k parmis n
    >>> binom(15)
    [1, 15, 105, 455, 1365, 3003, 5005, 6435,
    6435, 5005, 3003, 1365, 455, 105, 15, 1]
    """
    return puissance([1,1],n) # on utilise le principe du binome de newton

if __name__=="__main__":
    print(binom(15))