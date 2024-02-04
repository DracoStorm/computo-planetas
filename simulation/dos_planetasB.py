import numpy as np
import matplotlib.pyplot as plt

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


# Condiciones iniciales
x1, y1, xp1, yp1 = 0.3817, 0.1538, 5e-06, -5e-06
x2, y2, xp2, yp2 = 0.14466, 0.12304, -5e-06, 5e-06

X = np.array([x1, y1, x2, y2, xp1, yp1, xp2, yp2])

h = 1000e-3  # Paso de integración
N = 50000    # Iteraciones
m1, m2 = 5, 5

t = np.arange(0, N*h, h)

p1 = np.zeros((N, 2))
p2 = np.zeros((N, 2))

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

pause_time = 1e-9
# Graficar resultados
for k in range(0, N, 100):
    plt.clf()
    plt.plot(p1[:, 0], p1[:, 1], 'k', p2[:, 0], p2[:, 1], 'b',
             p1[k, 0], p1[k, 1], 'ko', p2[k, 0], p2[k, 1], 'bo')
    plt.grid(True)
    plt.xlabel('Eje $x$', fontsize=19)
    plt.ylabel('Eje $y$', fontsize=19)
    plt.title('Dos planetas ODE', fontsize=16)
    plt.pause(pause_time)

plt.show()