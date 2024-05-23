# Código Component

En este código nos conectamos a un servidor utilizando sockets, realizamos simulaciones de trayectoria orbital de dos planetas y enviamos los resultados al servidor a través de una conexión de red.



## Librerías

*   [numpy](../librerias/Librería_Numpy.md), Útil para realizar cálculos lógicos y matemáticos.
*   [socket](../librerias/Librería_Socket.md), Permite la comunicación entre el servidor y el cliente.



##  Funciones

1.   Función `main()`:

Importamos diversos módulos incluyendo manejo de excepciones, funciones de red, simulación orbital, inicialización astronómica, y constantes de red. Configuramos la conexión. Definimos las condiciones iniciales. Ejecutamos un bucle donde se calculan las nuevas posiciones de los planetas utilizando la función orbital_trajectory.calculate(). Enviamos los datos al servidor.

Se intenta recibir el estado del servidor. Se verifica el estado recibido del servidor. Si el estado es igual a SHUTDOWN_IDENTIFIER, se cierra la conexión con el servidor y se sale del bucle. Si el estado no es igual a OK_IDENTIFIER, se levanta una excepción BadNetType.



### *Código*

[*component.py*](../../../components/compute_traj/component.py)