# -*- coding: utf-8 -*-

"""
Authors:
    VERGNOU Brice
"""
import matplotlib.pyplot as plt

##### Q1 ######

def NbCar(fichier):
  with open(fichier,"r") as f:
    return len(f.read())

def NbLigne(fichier):
  with open(fichier,"r") as f:
    return len(f.readlines())

def NbOccurences(fichier,char):
  with open(fichier,'r') as f:
    s = 0
    texte = f.read()
    for lettre in texte:
      if lettre == char:
        s+=1
    return s

def MAJ(fichier):
  with open(fichier,'r') as f:
    texte = f.read()
  texte = texte.upper()
  with open("maj"+fichier,"w") as f:
    f.write(texte)
    
print("------ Q1 --------")
fichier = "prepainp.txt"
print(f"Dans {fichier}, il y a {NbCar(fichier)} caractères")
print(NbLigne(fichier), "lignes")
print(NbOccurences(fichier,"e"),"fois la lettre e")
MAJ(fichier)

##### Q2 ######


with open("courbe.txt","r") as f:
  points = [L.strip() for L in f.readlines()]

points = [L.split(" : ") for L in points]
coordonnes = []

for L in points:
  coordonnes += L

print(f"On a {len(coordonnes)} points codés")

x= []
y = []
for elements in coordonnes:
  point = elements.split(",")
  x.append(float(point[0]))
  y.append(float(point[1]))

mo = sum(y)/len(y)
plt.plot(x,y,"r")
plt.plot([x[0],x[-1]],[mo,mo],"--b",label="moyenne")
plt.legend()
plt.axhline(color="k")
plt.axvline(color="k")
plt.show()

###### Q3 #####
def tab_mult(a,b):
  for i in range(a,b+1):
    with open(f"tables/table_de_{i:06d}.txt","w") as f:
      print(f"{i:06d}")
      for k in range(1,101):
        f.write(f"{k} x {i} = {k*i}\n")

tab_mult(2,5)