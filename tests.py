from utils_polynome import polyn_to_str
from random import randint, uniform
import struct



def generer_banque(n, deg, maxCoeff, types, mode):
    """
        Cree une banque de test avec des polynomes

        En tête du fichier cree, s'il est binaire:
        - 1 bit pour savoir le type de donnees stockees (0 = int, 1 = float)
        - 8 bits d'entier non signe (long long) pour savoir le nombre de polynomes stockes
        - 8 bits d'entier non signe (long long) pour savoir la longueur d'un polynome (son degre + 1)

        Args:
            - n (int): nombre de polynomes a generer
            - deg (int) : degre des polynomes a generer
            - maxCoeff (int) : coefficient maximal pour chaque monome, en valeur absolue
            - types (str): int, float
            - mode (str): lisible, liste, binaire
    """
    
    fichier = "banque_" + mode + ".txt"

    # on choisit la bonne fonction aleatoire a utiliser, en fonction de la demande
    # cree par la meme occasion le format a utiliser lors de l'ecriture dans le fichier
    fonctionRandom = randint
    formatPack = f"{deg+1}q"
    
    if types == "float":
        fonctionRandom = uniform
        formatPack = f"{deg+1}d"
    

    # on ecrit en mode textuel
    if mode != "binaire":
        with open(fichier, "w") as f:
            
            # on ecrit sous forme de liste python
            if mode == "liste":
                for i in range(n):
                    polynome = [fonctionRandom(-maxCoeff, maxCoeff) for _ in range(deg + 1)]
                    f.write("[" + ", ".join([str(nb) for nb in polynome]) + "]\n")
            
            # on ecrit sous forme plus lisible
            if mode == "lisible":
                for i in range(n):
                    polynome = [fonctionRandom(-maxCoeff, maxCoeff) for _ in range(deg + 1)]
                    f.write(polyn_to_str(polynome) + "\n")
    

    # on ecrit en mode binaire
    else:
        with open(fichier, "wb") as f:
            # --- EN TETE ---
            # type des coefficients stockes (int ou float)
            bufferType = struct.pack("?", types=="float")
            f.write(bufferType)

            # nombre de polynomes stockes
            bufferNb = struct.pack("Q", n)
            f.write(bufferNb)
            
            # longueur des polynomes stockes (degre + 1)
            bufferLongueur = struct.pack("Q", deg+1)
            f.write(bufferLongueur)
           

            # --- DONNEES ---
            for i in range(n):
                polynome = [fonctionRandom(-maxCoeff, maxCoeff) for _ in range(deg + 1)]
                buffer = struct.pack(formatPack, *polynome)
                f.write(buffer)
