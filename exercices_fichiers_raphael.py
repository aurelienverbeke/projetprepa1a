# -*- coding: utf-8 -*-

"""
Authors:
    BOURGOUIN Raphael
"""

import matplotlib.pyplot as plt


# Exercice 6.1

# 3
def NbCar(file):
    with open(f"{file}", "r") as f:
        nb = len(f.read().strip())

    return nb


# 4
def NbLigne(file):
    with open(f"{file}", "r") as f:
        nb = len(f.readlines())

    return nb


# 5
def NbOccurences(file, c):
    with open(f"{file}", "r") as f:
        occurences = 0
        for car in "".join(f.readlines()):
            if car == c:
                occurences += 1

    return occurences


# 6
def MAJ(file):
    with open(f"{file}", "r") as f:
        lignes = f.read()

    lignes = lignes.upper()

    with open(f"MAJ_{file}", "w") as f:
        f.write(lignes)


with open("coucou", "w") as f:
    f.write("wow un fichier texte avec du texte dedans\nIncroyable non?")

print(f"Le fichier coucou possède {NbCar('coucou')} caractères")
print(f'Il possède {NbLigne("coucou")} lignes')
print(f'Et il y a {NbOccurences("coucou", "e")} e dans le fichier coucou')
MAJ("coucou")

# Exercice 6.2

with open(f"courbe.txt", "r") as f:
    liste_points_bruts = f.read().replace("\n", " : ").split(" : ")  # Récupère le texte et le sépare avec " : "
    liste_points_bruts = [x.split(",") for x in
                          liste_points_bruts]  # Convertis la liste de caractère en liste de couples de la forme ("x", "y")
    points = [(float(x[0]), float(x[1])) for x in liste_points_bruts[:-1]]  # Convertis les coordonnées de str à float

x = [i[0] for i in points]
y = [i[1] for i in points]
mO = sum(y) / len(points)

plt.figure("test")
plt.plot(x, y)
plt.plot([0, 11], [mO, mO])
plt.show()


# Exercice 6.3

def tab_mult(a, b):
    for i in range(a, b + 1):
        with open(f"fichiers/table_de_{i}.txt", "w") as f:
            for j in range(1, 101):
                f.write(f"{j} x {i} = {i * j}\n")


tab_mult(2, 5)
