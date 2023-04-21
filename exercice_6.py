# -*- coding: utf-8 -*-

"""
Authors:
    - BOURGOUIN Raphael
    - VERGNOU Brice
"""

from utils_polynome import *
import matplotlib.pyplot as plt
from math import cos,pi
from exercice_5 import *
from exercice_4 import *
from exercice_1 import tchebychev

def deplacement_racines(a,b,L):
    f = lambda x : (b-a)/2*x + (b+a)/2
    return [f(e) for e in L]

def visualisation(f,a,b,n):
    # Création du polynome de lagrange avec pas régulier
    h = (b-a)/n
    L = [a+i*h for i in range(n+1)]
    polynome_pas_regulier = lagrange(f,L)
    # Fonction associée + évaluation
    fonction_pas_regulier = lambda x : evalue(polynome_pas_regulier,x)
    N = n * 100
    e = (b-a)/N
    x = [a+i*e for i in range(N+1)]
    y_pas_regulier = list(map(fonction_pas_regulier,x))
    # affichage des points d'intersection
    for i in range(len(L)):
        plt.plot([L[i]],[fonction_pas_regulier(L[i])],"or")
    # Création du polynome avec points de Tchebychev
    # poly_tchebychev = tchebychev(n)
    # L = racines_polyn(poly_tchebychev)
    L = [cos((2*k+1)/(2*n)*pi) for k in range(n)] # racines exactes des polynomes de tchebychev
    L = deplacement_racines(a,b,L)
    polynome_pas_tcheby = lagrange(f,L)
    # fonction associée + évaluation
    fonction_pas_tcheby = lambda x : evalue(polynome_pas_tcheby,x)
    y_pas_tcheby = list(map(fonction_pas_tcheby,x))
    # affichage des points d'intersection
    for i in range(len(L)):
        plt.plot([L[i]],[fonction_pas_tcheby(L[i])],"ok")
    # évaluation de la fonction "normale"
    y_fonction = list(map(f,x))
    # Visualisation
    plt.plot(x,y_fonction,label="Fonction")
    plt.plot(x,y_pas_regulier,label="Lagrange avec pas régulier",color="r")
    plt.plot(x,y_pas_tcheby,label="Lagrange avec points de Tchebychev",color='k')
    plt.legend()
    plt.axis([x[0] ,x[-1] , min(y_fonction) - 1 , max(y_fonction) + 1])
    plt.show()

if __name__=="__main__":
    f = lambda x : 3**(-x**2)
    a = -5
    b = 5
    n = 30
    visualisation(f,a,b,n)
    visualisation(int,a,b,n) # marche moins bien avec des fonctions discountinues
    
"""
De base, la fonction a du mal a être approximée aux extrémités.
Utiliser les racines du polynomes de tchebychev revient a projeter les points d'un cercle sur l'axe des abscisses et utiliser les points projetés.
Or, il y a plus de points projettés sur les côtés qu'au milieu à cause de la forme du cercle
Donc on compense les erreurs d'approximations ( une explication plus rigoureuse explicant pourquoi les points de tchebychev 
sont meilleurs est fournie avec le reste du projet grâce à un exercice guidé de M. Montaut)
"""