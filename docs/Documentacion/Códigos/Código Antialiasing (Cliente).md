# Código "Antialiasing" (Cliente)

En este código creamos un cliente que se conecta a un servidor a través de sockets para enviar mensajes y/o archivos. Mandamos imágenes para realizar un efecto de suavizado.



## Librerías

*   [socket](../librerias/Librería_Socket.md), Permite la comunicación entre el servidor y el cliente.
*   [PIL](../librerias/Librería_PIL.md), Nos aportan herramientas para manipular imágenes.
*   [os](../librerias/Librería_OS.md), Proporciona una interfaz para interactuar con el sistema operativo en el que se ejecuta el programa.
*   [constants](../../../network/constants.py) y [network.functions](../../../network/functions.py), Constantes y también funciones de red hechas por nosotros.



##  Funciones

1.  Función `antialiasing(file: str) -> Image`:

Tomamos la ruta de un archivo. Abrimos la imagen. Aplicamos el filtro para realizar antialiasing en la imagen.
Devolvemos la imagen resultante.

2.  Función `main() -> None`:

Definimos la IP y puerto del servidor. Creamos un socket de cliente. Conectamos con el servidor.

3.  Bucle `while True`:

Solicitamos al usuario que seleccione una de estas opciones:

"1", Enviar un mensaje: Envía un mensaje al servidor.

"2", Enviar un archivo: Solicita al usuario la ruta del archivo a enviar. Verifica que la ruta es válida.
Si el archivo es una imagen aplica antialiasing. Sobrescribe el archivo original con la versión resultante. Envia el archivo al servidor.

"Q", Salir: Rompe el bucle para salir del programa. 
Para cualquier otra entrada, imprime un mensaje de error.



### *Código*

[*initialising_component.py*](../../../components/antialiasing/initialising_component.py)