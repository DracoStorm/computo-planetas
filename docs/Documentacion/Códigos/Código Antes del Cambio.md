# Código Antes del Cambio

Este código simula el movimiento de dos planetas mediante una fórmula de constante gravitacional.



## Librerías

*   [numpy](../librerias/Librería_Numpy.md), Es una librería de Python especializada en el cálculo numérico y el análisis de datos.
*   [matplotlib.pyplot](../librerias/Librería_MatPlotLib.md), Permite crear y personalizar los tipos de gráficos más comunes.



##  Funciones

1.  Función `dos_planetas(X, m1, m2)`:

Calculamos las derivadas de las posiciones y velocidades de los planetas basadas en las leyes de la gravitación universal de Newton.

2.  Función `simulate()`:

Definimos las condiciones iniciales de los planetas. Establecemos otros parámetros tales como la masa de los planetas. Devolvemos las trayectorias de los planetas como coordenadas.

3.  Función `plot_animation(p1, p2, N)`:

Creamos una animación que muestra la trayectoria de los planetas. Generamos una animación en la que se muestran las trayectorias de los planetas.

4.  `Función main()`:

Llamamos a las otras funciones. Ejecutamos la simulación y muestra la animación de los planetas.



### *Código*

[*Antes del cambio.py*](../../../components/compute_traj/astro_physics/Antes%20del%20cambio.py)
