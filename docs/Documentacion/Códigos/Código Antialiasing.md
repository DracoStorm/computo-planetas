# Código "Antialiasing"

En este código creamos un servidor que nos permitirá procesar imágenes usando filtros de suavizado.



## Librerías

*   [socket](../librerias/Librería_Socket.md), Permite la comunicación entre el servidor y el cliente.
*   [PIL.Image y PIL.ImageFilter](../librerias/Librería_PIL.md), Nos aportan herramientas para manipular imágenes.
*   [io.BytesIO](../librerias/Librería_io.md), Permite trabajar con datos binarios, para manejar la conversión entre bytes y objetos de imagen.



##  Funciones

1.   Función `cargar_imagen_desde_bytes(data_bytes)`:

Tomamos datos en forma de bytes y los convertimos en una imagen PIL.

2.  Función `aplicar_antialiasing(imagen, radio=2)`:
    
Tomamos una imagen PIL y aplicamos el efecto de antialiasing,   
(ImageFilter.GaussianBlur(radius=radio)).
Aquí, "radio" determina la intensidad del suavizado.

3.  Función `procesar_imagen(data_bytes)`:    

Cargamos una imagen desde los bytes recibidos, suavizamos la imagen cargada, la convertimos de nuevo a bytes con formato JPEG, y devolvemos los bytes de la imagen suavizada.

4.  Función `main()`:   

Configuramos la dirección IP y el número de puerto donde el servidor escuchará conexiones entrantes. Creamos un socket y lo enlazamos. Dentro de un bucle el servidor acepta conexiones entrantes. Recibimos datos. Procesamos la imagen recibida para suavizarla. Enviamos la imagen suavizada de vuelta al cliente. Cerramos la conexión.



### *Código*

[*antialiasing.py*](../../../components/antialiasing/antialiasing.py)

