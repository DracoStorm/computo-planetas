import numpy as np
import matplotlib.pyplot as plt

def dos_planetas(X, m1, m2):
    G = 6.672e-11
    
    XP = np.zeros(8)
    XP[0:4] = X[4:8]
    
    L = np.sqrt((X[2] - X[0])**2 + (X[3] - X[1])**2) + 1e-9
    
    XP[4] = (G * m2 * (X[2] - X[0])) / (L**3)
    XP[5] = (G * m2 * (X[3] - X[1])) / (L**3)
    XP[6] = (G * m1 * (X[0] - X[2])) / (L**3)
    XP[7] = (G * m1 * (X[1] - X[3])) / (L**3)
    
    return XP

def simulate():
    x1, y1, xp1, yp1 = 0.4050323158600528, 0.1757461028157972, 5e-06, -5e-06
    x2, y2, xp2, yp2 = 0.12132768413994373, 0.7383538971841953, -5e-06, 5e-06

    X = np.array([x1, y1, x2, y2, xp1, yp1, xp2, yp2])
    h = 1000e-3
    N = 50000
    m1, m2 = 4.9, 4.9

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

    return p1, p2

def plot_animation(p1, p2, N):
    pause_time = 1e-9
    for k in range(0, N, 100):
        plt.clf()
        plt.plot(p1[:, 0], p1[:, 1], 'k', p2[:, 0], p2[:, 1], 'b',
                 p1[k, 0], p1[k, 1], 'ko', p2[k, 0], p2[k, 1], 'bo')
        plt.grid(True)
        plt.xlabel('Eje $x$', fontsize=19)
        plt.ylabel('Eje $y$', fontsize=19)
        plt.title('Dos planetas ODE', fontsize=16)
        plt.pause(pause_time)
        ultima_posicion_planeta1 = p1[k, :]
        ultima_posicion_planeta2 = p2[k, :]

        print("Última posición del planeta 1:", ultima_posicion_planeta1)
        print("Última posición del planeta 2:", ultima_posicion_planeta2)
    plt.show()

def main():
    p1, p2 = simulate()
    plot_animation(p1, p2, N=50000)

if __name__ == "__main__":
    main()
