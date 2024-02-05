import numpy
import plot_animation as pl
from astro_physics import orbital_trajectory
from astro_physics import astro_init


def main():
    m1, m2 = 5, 5
    h = 5000e-3  # Paso de integración
    N = 50000    # Iteraciones

    X = astro_init.init()
    t, p1, p2 = orbital_trajectory.calculate(X, m1, m2, h, N)
    pl.plot_animation(t, p1, p2, N)


if __name__ == "__main__":
    main()
