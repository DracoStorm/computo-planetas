# Simulación Orbital

Este programa simula la trayectoria orbital de dos cuerpos celestes utilizando el método de 4to orden de Runge-Kutta para resolver ecuaciones diferenciales ordinarias (ODEs). La simulación es visualizada mediante una animación.

![gif orbita dos planetas](https://upload.wikimedia.org/wikipedia/commons/0/0e/Orbit5.gif)

## Archivos Python Utiliazados

### `simulation.py`

Este archivo contiene la función principal `main()`, que inicializa las condiciones iniciales, calcula la trayectoria orbital y luego anima la simulación.

```
def main():
    # Obtiene las condiciones iniciales
    X, m1, m2 = astro_init.init()
    # Calcula la trayectoria con las condiciones iniciales
    # h es el valor del intervalo de tiempo, valores bajos son precisos pero muy costos
    # N es el total de pasos que se dan, determina la duración de la simulación
    t, p1, p2 = orbital_trajectory.calculate(X, m1, m2, h=5000e-3, N=50000)
    # Anima la simulación
    pl.plot_animation(t, p1, p2, N=50000)


if __name__ == "__main__":
    main()
```

### `orbital_trajectory.py`

Contiene la función `calculate()` que realiza el cálculo de la trayectoria orbital utilizando el método de Runge-Kutta de 4to orden.
```
def calculate(X: [float], m1: int, m2: int, h: float, N: float):

    # Calcula el tiempo total de la simulación y guarda el intervalo del tiempo
    t = np.arange(0, N * h, h)

    # Inicializa los arrays para las coordenadas
    astro1_p = np.zeros((N, 2))
    astro2_p = np.zeros((N, 2))

    # Resuelve las ODEs utilizando las aproximaciones del método de 4to orden de Runge-Kutta
    for k in range(N):
        K1 = gravity_force.calculate(X, m1, m2)
        K2 = gravity_force.calculate(X + 0.5 * h * K1, m1, m2)
        K3 = gravity_force.calculate(X + 0.5 * h * K2, m1, m2)
        K4 = gravity_force.calculate(X + 1.0 * h * K3, m1, m2)

        # Formula de actualización
        X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)

        # Asignación de los valores calculados
        astro1_p[k, 0] = X[0]
        astro1_p[k, 1] = X[1]

        astro2_p[k, 0] = X[2]
        astro2_p[k, 1] = X[3]

    return t, astro1_p, astro2_p
```

### `astro_init.py`

Define la función `init()` que proporciona las condiciones iniciales para los astros en la simulación.
```
def init():
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
```

### `plot_animation.py`

Este archivo contiene funciones para crear y actualizar la animación de la trayectoria orbital.
```
def update_plot(frame, p1, p2, line1, line2, scatter1, scatter2):
    line1.set_data(p1[:frame, 0], p1[:frame, 1])
    line2.set_data(p2[:frame, 0], p2[:frame, 1])
    scatter1.set_offsets(p1[frame, :])
    scatter2.set_offsets(p2[frame, :])
    return line1, line2, scatter1, scatter2


def plot_animation(t, p1, p2, N):
    fig, ax = plt.subplots()
    line1, = ax.plot(p1[0], p2[0], 'k', label='trajectory_planet_1')
    line2, = ax.plot(p1[0], p2[0], 'b', label='trajectory_planet_2')
    scatter1 = ax.scatter(p1[0], p2[0], c='k', marker='o', label='planet_1')
    scatter2 = ax.scatter(p1[0], p2[0], c='b', marker='o', label='planet_2')

    ax.grid(True)
    ax.set(xlim=[0.1, 0.4], ylim=[0.1, 0.2],
           xlabel='Distance [x]', ylabel='Distance [y]')
    ax.legend()
    ani = FuncAnimation(fig=fig, func=update_plot, frames=N, fargs=(
        p1, p2, line1, line2, scatter1, scatter2), interval=30, blit=True)

    plt.show()

```

### `gravity_force.py`

Define la función `calculate()` que calcula la fuerza gravitacional entre los dos astros.
```
def calculate(X: [float], m1: int, m2: int):
    # Constante Gravitacional
    G = 6.672e-11

    # XP significa 'X Prime' una notación común para el estado derivado del vector 'X'
    XP = np.zeros(8)

    # Inicializa los valores de las velocidades derivadas
    XP[0:4] = X[4:8]

    # Calcula la distancia entre los dos astros
    # La suma del último término es un valor de estabilización numérica
    # Previene la división de valores extremadamente pequeños y cero
    L = np.sqrt((X[2] - X[0])**2 + (X[3] - X[1])**2) + 1e-9

    # Calcula la aceleración de los astros en x,y con las formulas derivadas de la segunda ley de Newton
    XP[4] = (G * m2 * (X[2] - X[0])) / (L**3)
    XP[5] = (G * m2 * (X[3] - X[1])) / (L**3)
    XP[6] = (G * m1 * (X[0] - X[2])) / (L**3)
    XP[7] = (G * m1 * (X[1] - X[3])) / (L**3)

    return XP
```

## Detalles de Funcionamiento

El programa funciona de la siguiente manera:

1. Se inicializan las condiciones iniciales de los astros utilizando la función `init()` del archivo `astro_init.py`.
2. Se calcula la trayectoria orbital utilizando la función `calculate()` del archivo `orbital_trajectory.py`, que implementa el método de Runge-Kutta de 4to orden.
3. Se anima la trayectoria orbital utilizando la función `plot_animation()` del archivo `plot_animation.py`.
4. La función `calculate()` del archivo `gravity_force.py` es utilizada para calcular la fuerza gravitacional entre los astros en cada paso de la simulación.

## Parámetros y Retornos

Cada archivo contiene funciones con parámetros específicos y valores de retorno.

- `orbital_trajectory.calculate(X, m1, m2, h, N)`: Calcula la trayectoria orbital.
  - `X`: Arreglo con las posiciones y velocidades de los astros.
  - `m1`: Masa del primer astro.
  - `m2`: Masa del segundo astro.
  - `h`: Intervalo de tiempo entre lapsos.
  - `N`: Número total de pasos que definen la duración de la simulación.
  - Retorna `t`, `astro1_p`, y `astro2_p`, que representan los puntos de tiempo de la simulación, y las posiciones x,y de cada astro en cada punto de tiempo, respectivamente.

- `astro_init.init()`: Crea las condiciones iniciales para la simulación de los astros.
  - Retorna `X`, un arreglo de los valores de las posiciones y velocidades del par de astros, `astro1_m`, y `astro2_m`, que representan las masas de los astros.

- `plot_animation.plot_animation(t, p1, p2, N)`: Crea y muestra la animación de la trayectoria orbital.
  - `t`: Puntos de tiempo de la simulación.
  - `p1`: Posición x,y del astro 1.
  - `p2`: Posición x,y del astro 2.
  - `N`: Número total de pasos de la simulación.

- `gravity_force.calculate(X, m1, m2)`: Calcula la atracción gravitacional de dos cuerpos.
  - `X`: Arreglo con las posiciones y velocidades de los astros.
  - `m1`: Masa del primer astro.
  - `m2`: Masa del segundo astro.
  - Retorna `XP`, un arreglo con las posiciones y velocidades de los astros después de ser derivados.
