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







## EXERCICE 6.2
with open("courbe.txt", "r") as f:
    contenu = f.read()
    contenu = contenu.replace("\n", " : ")
    coordonnees = contenu.split(" : ")
    coordonnees.pop() # on enleve la dernier coordonnee vide

    print("Nombre = " + str(len(coordonnees)))

    m0 = 0
    x = list()
    y = list()
    for i in coordonnees: # pour chaque couple x, y
        index = i.find(",") # on cherche l'indice de la virgule
        m0 += float(i[:index]) # on recupere l'abscisse
        x.append(float(i[:index])) # de meme
        y.append(float(i[index+1:])) # on recupere l'ordonnee
    m0 /= len(coordonnees) # on calcule la moyenne

    print("Moyenne = " + str(m0))
    
    plt.plot(x, y)
    plt.show()







### EXERCICE 6.3
def tab_mult(a,b):
  for i in range(a,b+1):
    with open(f"table_de_{i}.txt","w") as f:
      for k in range(1,101):
        f.write(f"{k} x {i} = {k*i}\n")
