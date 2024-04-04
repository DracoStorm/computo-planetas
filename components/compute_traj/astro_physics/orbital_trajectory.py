from astro_physics import gravity_force
import numpy as np


def calculate(X: np.ndarray[float], m1: int, m2: int, h: float):
    """
        Cácula la trayectoria de la órbita utilizando el método de 4to orden de Runge-Kutta para reolver ODEs.

        Parameters
        ----------
        X:[float]
            Arreglo con las posiciones y velocidades de los astros.
        m1:int
            Masa del primer astro.
        m2:int
            Masa del segundo astro.
        h:float
            Intervalo entre lapsos de tiempo.
        N:float
            Iteraciones que definen el tiempo total de la simulación.

        Returns
        -------
        t:[float]
            Puntos de tiempo de la simulación.
        astro1_p:[float]
            Posición x,y del astro 1.
        astro2_p:[float]
            Posición x,y del astro 2.
    """

    # Resuelve las ODEs utilizando las aproximaciones del método de 4to orden de Runge-Kutta
    K1 = gravity_force.calculate(X, m1, m2)
    K2 = gravity_force.calculate(X + 0.5 * h * K1, m1, m2)
    K3 = gravity_force.calculate(X + 0.5 * h * K2, m1, m2)
    K4 = gravity_force.calculate(X + 1.0 * h * K3, m1, m2)

    # Formula de actualización
    X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)

    return X
