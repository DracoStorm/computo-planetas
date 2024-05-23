# Código Frames

En este código generamos series de imágenes para posteriormente crear un video que muestre la rotación de un planeta. 

## Librerías

*   [numpy](../librerias/Librería_Numpy.md), Útil para realizar cálculos lógicos y matemáticos.
*   [cv2](../librerias/Librería_cv2.md), Se utiliza para el procesamiento de imágenes y vídeo.
*   [PIL](../librerias/Librería_PIL.md), Agrega soporte para abrir, manipular y guardar muchos formatos de archivo de imagen diferentes.


## Funciones

1.  Función `gen_frame`:

Aquí generamos frames. Tomamos una imagen que funcionará como fondo, además de una imagen del planeta en cuestión. La función superpone ambas imágenes.

2.  Función `generar_imagenes_superpuestas`

En esta función creamos una serie de imágenes. Generamos imágenes con cada fase de rotación del planeta.

3.  Función `generar_video`:

Procedemos a hacer un video a partir de los frames generados en anteriores funciones.

4.  Función `main`:

En está función coordinamos todo el proceso anteriormente explicado.



### *Código*

[*frames.py*](../../../components/gen_frame/frames.py)