import numpy as np
import matplotlib.pyplot as plt

# Condiciones iniciales
x1, y1, xp1, yp1 = 0.1, 0.1, 5e-06, -5e-06
x2, y2, xp2, yp2 = 0, 0, 5e-06, 0

X = np.array([x1, y1, x2, y2, xp1, yp1, xp2, yp2])

h = 1000e-3  # Paso de integración
N = 50000    # Iteraciones
m1, m2 = 1, 1

t = np.arange(0, N*h, h)

p1 = np.zeros((N, 2))
p2 = np.zeros((N, 2))


def dos_planetas(X, m1, m2):
    # ODE dos planetas
    XP = np.zeros(8)
    G = 6.672e-11  # constante gravitacional

    XP[0:4] = X[4:8]

    # Calculate the distance between the two planets
    L = np.sqrt((X[2] - X[0])**2 + (X[3] - X[1])**2) + 1e-9

    # Update the derivative values
    XP[4] = (G * m2 * (X[2] - X[0])) / (L**3)
    XP[5] = (G * m2 * (X[3] - X[1])) / (L**3)
    XP[6] = (G * m1 * (X[0] - X[2])) / (L**3)
    XP[7] = (G * m1 * (X[1] - X[3])) / (L**3)

    return XP


for k in range(N):
    K1 = dos_planetas(X, m1, m2)
    K2 = dos_planetas(X + 0.5 * h * K1, m1, m2)
    K3 = dos_planetas(X + 0.5 * h * K2, m1, m2)
    K4 = dos_planetas(X + 1.0 * h * K3, m1, m2)

    X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)

    p1[k, 0] = X[0]
    p1[k, 1] = X[1]

    p2[k, 0] = X[2]
    p2[k, 1] = X[3]
plt.plot(p1[:, 0], p1[:, 1], 'k', p2[:, 0], p2[:, 1], 'b',
             p1[k, 0], p1[k, 1], 'ko', p2[k, 0], p2[k, 1], 'bo')

# Graficar resultados
def update():
    
plt.grid(True)
plt.xlabel('Eje $x$', fontsize=14)
plt.ylabel('Eje $y$', fontsize=14)
plt.title('Dos planetas ODE', fontsize=16)
plt.show()
