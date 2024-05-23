# Código Frames

En este código somos un cliente que se conecta a un servidor. El cliente permite enviar mensajes o archivos al servidor basado en la opción seleccionada por el usuario.



## Librerías

*   [socket](../librerias/Librería_Socket.md), Actúa como un enlace de comunicación entre un servidor y un cliente.
*   [network](../../../network/constants.py), Nuestro propio módulo.



## Funciones

1.  Función `main`:
   
    Define la dirección IP y el puerto del servidor. Crea un socket para la comunicación con el servidor. Conecta el socket al servidor. Entra en un bucle infinito para permitir al usuario enviar mensajes o archivos al servidor. <br>
    Opción 1: Envía un mensaje al servidor. <br>
    Opción 2: Envía un archivo al servidor. <br>
    Opción 'q': Sale del programa. <br>
    Cualquier otra opción no es válida, y esto se le avisa al usuario.



### *Código*

[*frames.py*](../../../server/comp_threads/frames.py)