# -*- coding: utf-8 -*-

"""
Authors:
    - VERGNOU Brice
"""

from utils_polynome import *

def tchebychev(n):
    """
    Retourne le polynôme de Tchebychev T_n définit tel que :
        T0 = 1
        T1 = X
        T_(n+2) = 2XT_(n+1) - T_n
    Args :
        - n (int >= 0) : le rang du polynôme désiré
    Returns :
        - list : le polnyome T_n
    >>> tchebychev(5)
    16 X**5 - 20 X**3 + 5 X
    >>> tchebychev(10)
    512 X**10 - 1280 X**8 + 1120 X**6 - 400 X**4 + 50 X**2 - 1
    """
    # cas de base qui n'est pas respecté par le while qui suit
    if n == 0:
        return monome(0) 
    # initialisation des termes
    T_0 = monome(0)
    T_1 = monome(1)
    i = 1
    # on itère jusqu'à i = n
    while i < n:
        x2 = [0,2]
        T_2 = produit(x2,T_1) # 2XT_(n+1)
        T_2 = diff(T_2, T_0) # 2XT_(n+1) - T_n
        T_0,T_1 = T_1, T_2
        i += 1
    return T_1

if __name__ == "__main__":
    print("On a:")
    print(f"T5 = {polyn_to_str(tchebychev(5))}")
    print(f"T10 = {polyn_to_str(tchebychev(10))}")