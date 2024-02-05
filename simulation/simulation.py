import numpy
import plot_animation as pl
from astro_physics import orbital_trajectory
from astro_physics import astro_init


def main():
    X, m1, m2 = astro_init.init()
    t, p1, p2 = orbital_trajectory.calculate(X, m1, m2, h=5000e-3, N=50000)
    pl.plot_animation(t, p1, p2, N)


if __name__ == "__main__":
    main()
