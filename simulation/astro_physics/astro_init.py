import numpy as np


def init():
    """
        Crea las condiciones iniciales para la simulación de los astros.

        Returns
        -------
            X: float[]
                Arreglo de los valores de las posiciones y velocidades del par de astros.

            astro1_m: int
                Masa del astro 1.

            astro2_m:int
                Masa del astro 2.

    """

    # Posciciones en m
    astro1_x, astro1_y = 0.3817, 0.1538
    astro2_x, astro2_y = 0.14466, 0.12304

    # Velocidad en sus componentes m/s
    astro1_vx, astro1_vy = 5e-06, -5e-06
    astro2_vx, astro2_vy = -5e-06, 5e-06

    # Masas en kg
    astro1_m = 5
    astro2_m = 5

    # Arreglo que contiene los datos de las pocisiones y velocidades
    # El sentido es la búsqueda de cálculos de alto rendimiento
    X = np.array([astro1_x, astro1_y, astro2_x, astro2_y,
                 astro1_vx, astro1_vy, astro2_vx, astro2_vy])

    return X, astro1_m, astro2_m
