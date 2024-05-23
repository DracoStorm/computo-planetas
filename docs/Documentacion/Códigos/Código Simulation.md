# Código Simulation

Este código coordina la obtención de condiciones iniciales, el cálculo de trayectorias y la visualización estas. La simulación se ejecuta en un bucle principal que sigue estos pasos para simular y visualizar el movimiento de planetas tomando en cuenta la gravedad.



##  Funciones

1.   Función `main()`:

Se llama a la función astro_init.init() para obtener las condiciones iniciales necesarias para la simulación. Se utiliza la función orbital_trajectory.calculate() para calcular la trayectoria dadas las condiciones iniciales, un intervalo de tiempo y el número total de pasos. Se utiliza la función plot_animation() para animar la simulación de la trayectoria orbital.



### *Código*

[*simulation.py*](../../../components/compute_traj/simulation.py)