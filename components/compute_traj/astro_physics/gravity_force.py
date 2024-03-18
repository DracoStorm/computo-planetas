import numpy as np


def calculate(X: [float], m1: int, m2: int):
    """
        Cálcula la atracción  gravitaticional de dos cuerpos utilizando ecuaciones diferenciales ordinarias (ODEs).

        Parameters
        ----------
        X:float[]
            Arreglo con las pocisiones y velocidades de los astros.
        m1:int
            Masa del primer astro.
        m2:int
            Masa del segundo astro.

        Returns
        -------
        XP:float[]
            Arreglo con las posiciones y velocidades de los astros después de ser derivados.
    """
    # Constante Gravitacional
    G = 6.672e-11

    # XP significa 'X Prime' una notación común para el estado derivado del vector 'X'
    XP = np.zeros(8)

    # Inicializa los valores de las velocidades derivadas
    XP[0:4] = X[4:8]

    # Calcula la distancia entre los dos astros
    # La suma del último término es un valor de estabilización numérica
    # Previene la división de valores extremadamente pequeños y cero
    L = np.sqrt((X[2] - X[0])**2 + (X[3] - X[1])**2) + 1e-9

    # Calcula la aceleración de los astros en x,y con las formulas derivadas de la segunda ley de Newton
    XP[4] = (G * m2 * (X[2] - X[0])) / (L**3)
    XP[5] = (G * m2 * (X[3] - X[1])) / (L**3)
    XP[6] = (G * m1 * (X[0] - X[2])) / (L**3)
    XP[7] = (G * m1 * (X[1] - X[3])) / (L**3)

    return XP
