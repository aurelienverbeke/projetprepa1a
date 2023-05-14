# -*- coding: utf-8 -*-



import matplotlib.pyplot as plt



### EXERCICE 6.1
def nbCar(nom):
    contenu = ""
    with open(nom, "r") as f:
        contenu = f.read()
    return len(contenu)

# on compte les retour chariot
def nbLignes(nom):
    contenu = ""
    with open(nom, "r") as f:
        contenu = f.read()
    return contenu.count("\n") + 1

def nbOccurrences(nom, c):
    contenu = ""
    with open(nom, "r") as f:
        contenu = f.read()
    return contenu.count(c)

def MAJ(nom):
    contenu = ""
    with open(nom, "r") as f:
        contenu = f.read()
    with open("maj" + nom, "w") as f:
        f.write(contenu.upper())

with open("bandeorga.txt", "w") as f:
    f.write("Oui, ma gâtée, RS4 gris nardo, bien sûr qu'ils m'ont raté (gros, bien sûr)\nSoleil dans la bulle, sur le Prado, Shifter pro' (Shifter pro')\nContre-sens (ah), ma chérie, tu es à contre-sens\nPuta, où tu étais quand j'mettais des sept euros d'essence (hein)")

print(f"Caracteres de bandeorga : {nbCar('bandeorga.txt')}")
print(f"Lignes de bandeorga : {nbLignes('bandeorga.txt')}")
print(f"Occurrences de e de bandeorga : {nbOccurrences('bandeorga.txt', 'e')}\n")
MAJ('bandeorga.txt')






## EXERCICE 6.2
with open("courbe.txt", "r") as f:
    contenu = f.read()
    contenu = contenu.replace("\n", " : ")
    coordonnees = contenu.split(" : ")
    coordonnees.pop() # on enleve la dernier coordonnee vide

    print("Nombre de coordonnees = " + str(len(coordonnees)))

    m0 = 0
    x = list()
    y = list()
    for i in coordonnees: # pour chaque couple x, y
        index = i.find(",") # on cherche l'indice de la virgule
        m0 += float(i[index+1:]) # on recupere l'abscisse
        x.append(float(i[:index])) # de meme
        y.append(float(i[index+1:])) # on recupere l'ordonnee
    m0 /= len(coordonnees) # on calcule la moyenne

    print("Moyenne des ordonnees = " + str(m0))
    
    plt.plot(x, y)
    plt.plot([x[0], x[-1]], [m0, m0])
    plt.show()







### EXERCICE 6.3
def tab_mult(a,b):
  for i in range(a,b+1):
    with open(f"table_de_{i}.txt","w") as f:
      for k in range(1,101):
        f.write(f"{k} x {i} = {k*i}\n")
