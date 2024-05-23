# Código Orbital_Trajectory

En este código definimos la función "calculate()" que utiliza el método de Runge-Kutta de cuarto orden para resolver ecuaciones diferenciales ordinarias que modelan el movimiento de dos astros bajo la influencia de la gravedad.



## Librerías

*   [numpy](../librerias/Librería_Numpy.md), Es una biblioteca con una gran colección de funciones matemáticas de alto nivel para operar con ellas.



##  Funciones

*   Función `Función calculate(X, m1, m2, h)`:

Creamos un arreglo "X" que contiene las posiciones y velocidades de los astros. Importamos la función "calculate" desde el módulo [gravity_force](). Se utilizan las aproximaciones del método de RK4 para resolver las ODEs. Las nuevas posiciones y velocidades se calculan utilizando la fórmula de actualización de RK4:
X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)
Como retorno hay un nuevo arreglo "X" que contiene las nuevas posiciones y velocidades de los astros después de avanzar un intervalo de tiempo h utilizando RK4.



### *Código*

[*orbital_trajectory.py*](../../../components/compute_traj/astro_physics/orbital_trajectory.py)
