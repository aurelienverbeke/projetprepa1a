from utils_polynome import polyn_to_str
from random import randint, uniform
import struct



def generer_banque(n, deg, maxCoeff, types, mode):
    """
        Cree une banque de test avec des polynomes

        En tête du fichier cree, s'il est binaire:
        - 1 octet pour savoir le type de donnees stockees (0 = int, 1 = float)
        - 8 octets d'entier non signe (long long) pour savoir le nombre de polynomes stockes
        - 8 octets d'entier non signe (long long) pour savoir la longueur d'un polynome (son degre + 1)

        Args:
            - n (int): nombre de polynomes a generer
            - deg (int) : degre des polynomes a generer
            - maxCoeff (int) : coefficient maximal pour chaque monome, en valeur absolue
            - types (str): int, float
            - mode (str): liste, binaire
    """
    
    fichier = "banque_" + mode + ".txt"

    # on choisit la bonne fonction aleatoire a utiliser, en fonction de la demande
    # cree par la meme occasion le format a utiliser lors de l'ecriture dans le fichier
    # (on ecrira avec les bits de poids fort a gauche)
    fonctionRandom = randint
    formatPack = f">{deg+1}q"
    
    if types == "float":
        fonctionRandom = uniform
        formatPack = f">{deg+1}d"
    

    # on ecrit en mode liste
    if mode == "liste":
        with open(fichier, "w") as f:
            for i in range(n):
                polynome = [fonctionRandom(-maxCoeff, maxCoeff) for _ in range(deg + 1)]
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
            
            # longueur des polynomes stockes (degre + 1)
            bufferLongueur = struct.pack(">Q", deg+1)
            f.write(bufferLongueur)
           

            # --- DONNEES ---
            for i in range(n):
                polynome = [fonctionRandom(-maxCoeff, maxCoeff) for _ in range(deg + 1)]
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
