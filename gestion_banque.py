# -*- coding: utf-8 -*-

"""
Authors:
    - VERBEKE Aurelien
"""


from utils_polynome import polyn_to_str, monome
from random import randint, uniform
import struct



def generer_banque(n, degMax, maxCoeff, types, mode):
    """
        Cree une banque de test avec des polynomes

        En tête du fichier cree, s'il est binaire:
        - 1 octet pour savoir le type de donnees stockees (0 = int, 1 = float)
        - 8 octets d'entier non signe (long long) pour savoir le nombre de polynomes stockes
        - 8 octets d'entier non signe (long long) pour savoir la longueur d'un polynome (son degre + 1)

        Args:
            - n (int): nombre de polynomes a generer
            - degMax (int) : degre maximal des polynomes a generer
            - maxCoeff (int) : coefficient maximal pour chaque monome, en valeur absolue
            - types (str): int, float
            - mode (str): liste, binaire
    """
    
    # on doit pouvoir au moins ranger le polynome nul,
    # le polynome avec tous ses coefficients a 1,
    # et tous les monomes de degre allant de 0 au degre max
    if n < degMax + 3:
        print("Le nombre de polynomes demande n'est pas assez grand")
        return

    fichier = "banque_" + mode + ".txt"

    # on choisit la bonne fonction aleatoire a utiliser, en fonction de la demande
    # on cree par la meme occasion le format a utiliser lors de l'ecriture dans le fichier
    # (on ecrira avec les bits de poids fort a gauche)
    fonctionRandom = randint
    formatPack = f">{degMax+1}q"
    
    if types == "float":
        fonctionRandom = uniform
        formatPack = f">{degMax+1}d"
    

    polyn_de_test = [
        [0]*(degMax + 1),
        [1]*(degMax + 1)
    ]

    polyn_de_test += [monome(i) + [0]*(degMax - i) for i in range(degMax + 1)]


    # on ecrit en mode liste
    if mode == "liste":
        with open(fichier, "w") as f:
            for P in polyn_de_test:
                f.write("[" + ", ".join([str(nb) for nb in P]) + "]\n")

            for i in range(n-len(polyn_de_test)):
                deg = randint(0, degMax) # degre du polynome ecrit
                # on rajoute des 0 pour qu'ils fassent tous la meme taille
                polynome = [fonctionRandom(-maxCoeff, maxCoeff) for _ in range(deg + 1)] + [0]*(degMax - deg)
                f.write("[" + ", ".join([str(nb) for nb in polynome]) + "]\n")
            

    # on ecrit en mode binaire avec les bits de poids fort a gauche
    else:
        with open(fichier, "wb") as f:
            # --- EN TETE ---
            # type des coefficients stockes (int ou float)
            bufferType = struct.pack(">b", int(types=="float"))
            f.write(bufferType)

            # nombre de polynomes stockes
            bufferNb = struct.pack(">Q", n)
            f.write(bufferNb)
            
            # longueur des polynomes stockes (degre max + 1)
            bufferLongueur = struct.pack(">Q", degMax+1)
            f.write(bufferLongueur)
           

            # --- DONNEES ---
            for P in polyn_de_test:
                buffer = struct.pack(formatPack, *P)
                f.write(buffer)

            for i in range(n-len(polyn_de_test)):
                deg = randint(0, degMax) # degre du polynome ecrit
                # on rajoute des 0 pour qu'ils fassent tous la meme taille
                polynome = [fonctionRandom(-maxCoeff, maxCoeff) for _ in range(deg + 1)] + [0]*(degMax - deg)
                buffer = struct.pack(formatPack, *polynome)
                f.write(buffer)





def longueur_banque(mode):
    """
        Cherche le nombre de polynomes contenu dans un fichier
        Args:
            - mode (str): liste, binaire
        Returns:
            int: nombre de polynomes
    """

    # nom du fichier correspondant au mode d'ecriture
    fichier = "banque_" + mode + ".txt"
    
    # on initialise le nombre de polynomes a -12, s'il y a un probleme on le verra
    longueur = -12

    # on cherche dans un fichier ecrit en mode liste
    if mode != "binaire":
        with open(fichier, "r") as f:
            contenu = f.read()
            # il y a un polynome par ligne, on compte les retours a la ligne
            longueur = contenu.count("\n")

    # on cherche dans un fichier ecrit en mode binaire
    else:
        with open(fichier, "rb") as f:
            # voir description en-tete generer_banque
            
            # on se place dans l'en-tete entre le type de donnees et le nombre de polynomes
            f.seek(1)
            # on lit les 8 octets suivants (nombre de polynomes)
            buffer = f.read(8)
            # on reconvertit les octets en valeurs lisibles
            contenu = struct.unpack(">Q", buffer)
            # on extrait le nombre de polynomes
            longueur = contenu[0]
    
    return longueur






def longueur_polynome_banque_binaire():
    """
        Retourne la longueur (degre + 1) des polynomes dans une banque de test binaire
        Returns:
            int: longeur du polynome
    """

    # on initialise la longueur des polynomes a -12, s'il y a un probleme on le verra
    longueur = -12

    with open("banque_binaire.txt", "rb") as f:
        # voir description en-tete generer_banque
        
        # on se place dans l'en-tete entre le type de donnees et le nombre de polynomes
        f.seek(9)
        # on lit les 8 octets suivants (nombre de polynomes)
        buffer = f.read(8)
        # on reconvertit les octets en valeurs lisibles
        contenu = struct.unpack(">Q", buffer)
        # on extrait le nombre de polynomes
        longueur = contenu[0]
    
    return longueur






def type_coefficients_banque_binaire():
    """
        Retourne le type des coefficients des polynomes dans une banque de test binaire
        Returns:
            str: type des coefficients
    """

    # on initialise...
    _type = ""
    # on initialise a -12, s'il y a un probleme on le verra
    contenu = -12

    with open("banque_binaire.txt", "rb") as f:
        # voir description en-tete generer_banque
        
        # on lit les 8 octets suivants (nombre de polynomes)
        buffer = f.read(1)
        # on reconvertit les octets en valeurs lisibles
        contenu = struct.unpack(">b", buffer)[0]

    if contenu == 0:
        return "int"
    else:
        return "float"






def utiliser_banque(indice, mode):
    """
        Va chercher un polynome dans une banque de tests
        Args:
            - indice (int): numero du polynome a aller chercher (commence a 0)
            - mode (str): liste, binaire
        Returns:
            list: le polynome demande
    """

    # nom du fichier correspondant au mode d'ecriture
    fichier = "banque_" + mode + ".txt"

    # on initialise le polynome
    polynome = list()

    # on cherche dans un fichier ecrit en mode liste
    if mode != "binaire":
        with open(fichier, "r") as f:
            ligne = f.readline()
            for _ in range(indice):
                ligne = f.readline()
        polynome = eval(ligne)

    # on cherche dans un fichier ecrit en mode binaire
    else:
        with open(fichier, "rb") as f:
            # voir description en-tete generer_banque

            # on commence par trouver la longueur du polynome (degre + 1)
            longueur_polynome = longueur_polynome_banque_binaire()
            
            # on cree le format a utiliser lors de l'ecriture dans le fichier
            formatUnpack = ""
            if type_coefficients_banque_binaire() == "int":
                formatUnpack = f">{longueur_polynome}q"
            else:
                formatUnpack = f">{longueur_polynome}d"


            # on se place la ou il faut
            # 17 octets d'en-tete + un certain nombre d'octets pour chaque polynome
            f.seek(17 + longueur_polynome * indice * struct.calcsize("q"))
            # on lit les octets suivants (tous les coefficients du polynome)
            buffer = f.read(longueur_polynome * struct.calcsize("q"))
            # on reconvertit les octets en valeurs lisibles
            contenu = struct.unpack(formatUnpack, buffer)
            # on extrait le nombre de polynomes
            polynome = list(contenu)

    return polynome
