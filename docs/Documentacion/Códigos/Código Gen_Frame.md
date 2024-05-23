# Código Gen_Frame

Este código nos sirve para envíar un frame a través de un socket de cliente en un bucle y utiliza un sistema de barreras y bloqueos para la sincronización.



## Librerías

*   [socket](../librerias/Librería_Socket.md), Actúa como un enlace de comunicación entre un servidor y un cliente.
*   [threading](../librerias/Librería_Thread.md), Permite que un programa ejecute múltiples operaciones simultáneamente en el mismo espacio de proceso.
*   [network](../../../network/functions.py), Nuestro propio modulo con todos los componentes que necesitamos.
*   [PIL](../librerias/Librería_PIL.md), Agrega soporte para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes.



## Funciones

1.  Función `main`:

    La imagen a enviar es cargada y convertida a bytes. La imagen es enviada en cada iteración. Manejamos varios tipos de errores en los cuales se imprime un mensaje de error, se cierra el socket del cliente y se aborta la barrera (barrera de sincronización para coordinar múltiples hilos). Se verifica el estado después de enviar la imagen y se asegura de que se recibió una confirmación de éxito antes de continuar.La iteración se detiene si se ha alcanzado el número máximo de iteraciones.



### *Código*

[*gen_frame.py*](../../../server/comp_threads/gen_frame.py)