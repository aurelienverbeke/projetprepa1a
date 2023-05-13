# -*- coding: utf-8 -*-

""""
Authors:
    - BOURGOUIN Raphael
"""

from utils_polynome import derive_polyn, division, pgcd, deg, unitaire, evalue, polyn_to_str
from fractions import Fraction as F
import numpy as np

def Newton(f, a, b, k):
    """
    Trouve le zéro de f présent entre a et b avec une précision de epsilon
    Args:
         - f (lambda) : la fonction pour laquelle on cherches le zéro
         - a (float) : le minimum de l'intervalle de recherche
         - b (float) : le maximum de l'intervalle de recherche
         - k (int) : le nombre de décimales de précision
    Returns:
        float : le zéro de f
    """
    epsilon = 10**-k

    # On réduit l'intervalle afin de faire converger la suite plus rapidement
    while abs(a - b) > 1:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m

    # Sachant que souvent a et b seront des zéros d'une des dérivées
    # On préfèrera prendre x et y au milieu de l'intervalle afin de s'en éloigner
    x = (a+b)/2
    y = x + epsilon*10

    # On utilise le principe de la méthode de Newton
    while abs(y - x) > epsilon:
        # Si y sort de l'intervalle, on applique une dichotomie et on recommence
        if y < a or y > b:
            m = (a+b)/2
            if f(a)*f(m) <= 0:
                b = m
            else:
                a = m
            x = (a+b)/2
            y = x + epsilon*10
        tmp = y
        y = y - f(y)*(y-x)/(f(y)-f(x))
        x = tmp
    return y

def racines_polyn_faible_degree(Q):
    """
    Renvoie les racines d'un polynome de degré au plus 2
    Args:
        - P (list) : Le polynome pour lequel on veut les racines
    Return:
        list: La liste des racines de P
    """

    if deg(Q) <= 0:
        return []
    if deg(Q) == 1:
        return [-Q[0]/Q[1]]
    if deg(Q) == 2:
        delta = Q[1] ** 2 - 4 * Q[2] * Q[0]
        if delta > 0:
            x1 = (-Q[1] + np.sqrt(delta)) / (2 * Q[2])
            x2 = (-Q[1] - np.sqrt(delta)) / (2 * Q[2])
            # Il faut ordoner les racines
            if x1 > x2:
                return [x2, x1]
            else:
                return [x1, x2]
        if delta == 0:
            return [-Q[1] / (2 * Q[2])]
        else:
            return []

    raise ValueError(f"Le polynome doit etre de degree inferieur ou egal a 2, or ici Q={Q}")

def racines_polyn(P, nombre_decimales=8):
    """
    Renvoie la liste des racines d'un polynome
    Args:
        - P (list) : le polynome pour lequel on veut les racines
        - nombre_decimales (int) : Le nombre de chiffre après la virgule de précision
    Returns:
        list: La liste des racines de P
    """

    # Si le polynome est constant, on considère qu'il n'a pas de racines
    if deg(P) <= 0:
        return []

    # On réduit le polynome en un polynomes Q ayant les memes racines que P mais uniquement en racines simples
    P = [F(x) for x in P]
    Q = division(P, pgcd(P, derive_polyn(P)))[0]
    Q = unitaire([float(x) for x in Q])

    # Si le degré est de 1 ou 2, on utilise directement les formules que l'on connait
    if deg(P) <= 2:
        return racines_polyn_faible_degree(Q)

    # On calcule un encadrement de toutes les racines
    mu = max(1, sum([abs(Q[x]) for x in range(len(Q)-1)]))

    # On calcule les dérivées successives de Q jusqu'à tomber sur un polynome de degré 2
    derivees = [Q]
    while deg(derivees[-1]) > 2:
        derivees.append(unitaire(derive_polyn(derivees[-1])))
        # On rend tous les polynomes unitaires afin d'éviter les erreurs qui peuvent survenir
        # avec des flotants trop grands lorsqu'on évalue

    intervalles = [-mu, mu]
    # On remonte la liste des dérivée
    # En utilisant le fait entre 2 racines successives de la dérivée il existe au plus une racine
    for idx in range(len(derivees)-1, -1, -1):
        f = lambda x: evalue(derivees[idx], x)

        if deg(derivees[idx]) <= 2:
            racines = racines_polyn_faible_degree(derivees[idx])
        else:
            racines = []
            for i in range(len(intervalles)-1):
                # On vérifie la présence d'un racine avec un TVI
                if f(intervalles[i])*f(intervalles[i+1]) <= 0:
                    # On applique Newton
                    racines.append(Newton(f, intervalles[i], intervalles[i+1], nombre_decimales))

        intervalles = [-mu] + racines + [mu]

    return intervalles[1:-1]

def racines_polyn_fich(ftxt):
    """
    Crée un fichier racines_{ftxt} dans lequel avec le format [polynome]::[racines] pour chaque racine présente dans {ftxt}
    Affiche chaque polynome suivi de ses racines
    Args:
        - ftxt (str): le nom du fichier contenant les polynomes
    """
    # On récupère les polynomes en les séparant
    with open(ftxt, "r") as f:
        polynomes = f.read().split("\n")

    with open(f"racines_{ftxt}", "w") as f:
        for p in polynomes:
            P = p[1:-1].split(", ") # On sépare chaque élément de la liste en enlevant les crochets
            P = [float(x) for x in P] # On convertit tous les éléments en flotants
            print(f"{polyn_to_str(P)}. Racines : {racines_polyn(P)}") # On affiche les racines
            f.write(f"{P}::{racines_polyn(P)}\n") # On écrit dans les polynomes et leurs racines dans le fichier


if __name__ == "__main__":
    P = [F(2), F(-7), F(-6), F(34), F(10), F(-63), F(-22), F(44), F(24)]
    racines = racines_polyn(P)
    print(f"Les racines de {polyn_to_str(P)} sont : {racines[0]}, {racines[1]} et {racines[2]}\n")
    print(f"Les racines de polynomes de polyn.txt sont:")
    racines_polyn_fich("polyn.txt")