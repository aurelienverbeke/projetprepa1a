# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERBEKE Aurelien
    - VERGNOU Brice
"""


# Aurelien


# Brice


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
