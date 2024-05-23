# Código Compute_Traj

En este código somos un cliente y nos conectamos a un servidor para recibir coordenadas.



## Librerías

*   [socket](../librerias/Librería_Socket.md), Actúa como un enlace de comunicación entre un servidor y un cliente.
*   [threading](../librerias/Librería_Thread.md), Permite que un programa ejecute múltiples operaciones simultáneamente en el mismo espacio de proceso.
*   [network](../../../network/exceptions.py), Nuestro propio módulo.



## Funciones

1.  Función `main`:

    Esta función consta de iteraciones. En cada una intenta recibir un mensaje de coordenadas del servidor. Cierra el socket si sucede alguna excepción y envía el mensaje de error al servidor. Si la recepción es exitosa, imprime las coordenadas recibidas y las actualiza. Después de todas las iteraciones, cierra el socket y avisa al servidor.



### *Código*

[*compute_traj*](../../../server/comp_threads/compute_traj.py)
