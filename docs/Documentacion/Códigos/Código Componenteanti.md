# Código Componenteanti

Este código implementa un cliente que se conecta a un servidor, envía una imagen y recibe una imagen procesada a través de un socket. 



## Librerías

*   [socket](../librerias/Librería_Socket.md), Proporciona acceso a la comunicación en red.
*   [PIL](../librerias/Librería_PIL.md), Agrega soporte para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes.
*   [io](../librerias/Librería_io.md), Provee facilidades para manejar diferentes tipos de entrada/salida.

## Funciones

1.  Función `cargar_imagen`:

    Carga una imagen desde una ruta especificada.

2.  Función `convertir_imagen_a_bytes`:

    Recibe una imagen. Convierte la imagen recibida a bytes. La envía a través de un socket.

3. Función `main`:

    Organiza todo el proceso para conectar con el servidor, enviar una imagen y recibirla tras ser procesada.



### *Código*

[*componenteanti.py*](../../../server/comp_threads/componenteanti.py)