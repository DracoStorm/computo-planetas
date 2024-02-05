from astro_physics import gravity_force
import numpy as np


def calculate(X, m1, m2, h, N):
    t = np.arange(0, N * h, h)

    p1 = np.zeros((N, 2))
    p2 = np.zeros((N, 2))

    for k in range(N):
        K1 = gravity_force.calculate(X, m1, m2)
        K2 = gravity_force.calculate(X + 0.5 * h * K1, m1, m2)
        K3 = gravity_force.calculate(X + 0.5 * h * K2, m1, m2)
        K4 = gravity_force.calculate(X + 1.0 * h * K3, m1, m2)

        X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)

        p1[k, 0] = X[0]
        p1[k, 1] = X[1]

        p2[k, 0] = X[2]
        p2[k, 1] = X[3]

    return t, p1, p2
