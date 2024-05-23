# Código Gravity_Force

Aquí definimos una función "calculate()" que calcula la posicion y velocidad de los astros.



## Librerías

*   [numpy](../librerias/Librería_Numpy.md), Es una biblioteca con una gran colección de funciones matemáticas de alto nivel para operar con ellas.



##  Funciones

1.   Función `calculate(X, m1, m2)`:

Creamos un arreglo "X" con los datos de los astros. Usamos la constante gravitacional "G". Creamos un arreglo "XP" para almacenar las derivadas de los datos de los astros. Calculamos la distancia "L" entre los astros. Se calcula la aceleracion con las fórmulas de la segunda ley de Newton y la ley de gravitación universal.
Retornamos el arreglo "XP" que contiene las posiciones y velocidades de los astros.



### *Código*

[*gravity_force.py*](../../../components/compute_traj/astro_physics/gravity_force.py)