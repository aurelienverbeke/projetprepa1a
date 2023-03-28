import numpy as np

def polynome_interpolation_lagrange(x,y):
    """
    Renvoie un polynôme P d'interpolation de lagrange
    passant par tout les P(x_i) = y_i 
    Args:
        x (list): les x_i
        y (list): les y_i
        
        len(x) == len(y)
    """
    n = len(x)
    X = np.poly1d([1, 0])
    P = 0
    for i in range(n):
        Li = 1
        for j in range(n):
            if i == j:
                Li *= 1
            else :
                Li *= (X-x[j])/(x[i]-x[j])
        P += Li*y[i]
    return P
