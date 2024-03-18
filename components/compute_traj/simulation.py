import numpy
import plot_animation as pl
from astro_physics import orbital_trajectory
from astro_physics import astro_init


def main():
    # Obtiene las condiciones iniciales
    X, m1, m2 = astro_init.init()
    # Calcula la trayectoria con las condiciones iniciales
    # h es el valor del intervalo de tiempo, valores bajos son precisos pero muy costos
    # N es el total de pasos que se dan, determina la duración de la simulación
    t, p1, p2 = orbital_trajectory.calculate(X, m1, m2, h=5000e-3, N=50000)
    # Anima la simulación
    pl.plot_animation(t, p1, p2, N=10)


if __name__ == "__main__":
    main()
