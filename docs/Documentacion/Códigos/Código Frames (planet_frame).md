# Código Frames (planet_frame)

Desmonta un GIF en frames, los redimensiona , y los recorta en forma de elipse, de forma que el planeta se el remanente.



## Librerías

*   [os](../librerias/Librería_OS.md), Proporciona una interfaz para interactuar con el sistema operativo en el que se ejecuta el programa.
*   [PIL](../librerias/Librería_PIL.md), Permite la edición de imágenes directamente desde Python.



## Funciones

1.  Función `unmount_gif`:

    Esta función desmonta un GIF en frames individuales y los guarda como archivos PNG.

2.  Función `re_scale`:

    Esta función toma una imagen y lo redimensiona a un nuevo tamaño especificado.

3.  Función `cut_elipse`:

    Esta función recorta una imagen en forma circular.



### *Código*

[*frames.py*](../../../components/planet_frame/frames.py)