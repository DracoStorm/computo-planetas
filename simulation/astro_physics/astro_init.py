import numpy as np


def init():
    # Condiciones iniciales
    x1, y1, xp1, yp1 = 0.3817, 0.1538, 5e-06, -5e-06
    x2, y2, xp2, yp2 = 0.14466, 0.12304, -5e-06, 5e-06

    X = np.array([x1, y1, x2, y2, xp1, yp1, xp2, yp2])

    return X
