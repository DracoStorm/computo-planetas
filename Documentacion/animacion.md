# Animacion de Planetas

Este programa desmonta un GIF en sus fotogramas individuales y luego puede rescalar cada fotograma o superponerlos en una imagen principal para crear una animación.
![gif animacion](https://qph.cf2.quoracdn.net/main-qimg-1a46bb25e24f6512cb49446282378c1a)

## Archivos Python

### `desmontar_gif.py`
![gif marte](https://i.gifer.com/origin/5a/5ac8cc0602227834db71a655fb593ce0_w200.gif)

Este archivo contiene la función `desmontar_gif(archivo_gif)` que descompone un GIF en sus fotogramas individuales y los guarda como imágenes PNG en una carpeta específica.

#### Función `desmontar_gif(archivo_gif)`

Esta función toma como entrada el nombre de un archivo GIF y descompone el GIF en sus fotogramas individuales. Luego, guarda cada fotograma como un archivo PNG en una carpeta dedicada.

- **Parámetros**:
  - `archivo_gif`: Nombre del archivo GIF a desmontar.
- **Excepciones**:
  - Genera una excepción si la ruta del archivo o el destino no son encontrados.
- **Valores de Retorno**:
  - No retorna ningún valor, pero guarda los fotogramas desmontados como archivos PNG en una carpeta específica.

```
def desmontar_gif(archivo_gif):
    """
        Desmonta el gif en cada frame que lo contiene y lo deposita en la carpta RUTA_FOTOGRAMAS.

            Parameters
            ----------
                arhivo_gif : string
                    Nombre de un archivo dentro de RUTA_GIF.

            Exceptions
            ----------
                Si la ruta del archivo o destino no es encontrada.
    """

    # Verfifica si el directorio "fotogramas" existe, si no lo crea.
    if (not os.path.isdir(RUTA_FOTOGRAMAS)):
        os.mkdir(RUTA_FOTOGRAMAS)

    # Verfifica si el directorio "animation/fotogramas/archivo_gif" existe, si no lo crea.
    # De esta manera existe una carpeta por cada gif.
    RUTA_FOTOGRAMAS_GIF = RUTA_FOTOGRAMAS + archivo_gif + r"/"
    if (not os.path.isdir(RUTA_FOTOGRAMAS_GIF)):
        os.mkdir(RUTA_FOTOGRAMAS_GIF)

    gif = Image.open(RUTA_GIF + archivo_gif + ".gif")

    try:
        # Extrae todos los fotogramas del GIF
        fotogramas = [f.convert("RGBA") for f in ImageSequence.Iterator(gif)]

        # Guarda cada fotograma como una imagen separada
        for i, fotograma in enumerate(fotogramas):
            archivo_png = RUTA_FOTOGRAMAS_GIF + f"fotograma_{i}.png"
            fotograma.save(archivo_png, "PNG")

        print(
            f"Se han desmontado correctamente {len(fotogramas)} fotogramas del gif {archivo_gif} en la carpeta {RUTA_FOTOGRAMAS_GIF}.")
    except Exception as e:
        print(f"Error al desmontar el GIF: {e}")


# Desmontar el GIF
desmontar_gif("marte")
```
### `Rescalar.py`

Este archivo rescala las imágenes PNG desmontadas del GIF a un nuevo tamaño.
```
# Definir el nuevo tamaño (en píxeles)
nuevo_tamaño = (50, 50)  # Cambia estos valores según tus necesidades

# Iterar sobre cada archivo en la carpeta
for archivo in os.listdir(carpeta_imagenes):
    if archivo.endswith(".png"):  # Solo procesar archivos PNG
        # Ruta completa de la imagen
        ruta_imagen = os.path.join(carpeta_imagenes, archivo)

        # Abrir la imagen
        imagen = Image.open(ruta_imagen)

        # Rescalar la imagen
        imagen_rescalada = imagen.resize(nuevo_tamaño)

        # Ruta para guardar la imagen rescalada (sobrescribe la imagen original)
        ruta_guardar = ruta_imagen

        # Guardar la imagen rescalada (sobrescribe la imagen original)
        imagen_rescalada.save(ruta_guardar)

        print("Imagen rescalada guardada exitosamente en:", ruta_guardar)
```

#### Procedimiento de Rescalado

- Itera sobre cada archivo PNG en la carpeta de imágenes.
- Abre cada imagen, la redimensiona al nuevo tamaño especificado y la guarda, sobrescribiendo la imagen original.
- Imprime la ruta donde se guarda la imagen redimensionada.

### `Imagen.py`

En este archivo se superponen los fotogramas rescalados de un GIF en una imagen principal para crear una animación.
```
sx = 630 
sy = 473
rx = 1
ry = 1
fx = sy / rx
fy = sy / ry

cx = 0.5
cy = 0.5
px = cx * fx
px = int(np.round(px))  # Convertir a entero
py = cy * fy
py = int(np.round(py))  # Convertir a entero

a = np.zeros((sx, sy))

# Abre la imagen principal
imagen_principal = Image.open(r"simulation\astro_physics\fondo.jpg")

# Lista para almacenar los frames superpuestos
frames_superpuestos = []

# Itera sobre los frames del 0 al 9
for i in range(10):
    # Abre la imagen del frame actual
    ruta_frame = fr"animation\frames\marte\frame_{i}.png"
    imagen_superpuesta = Image.open(ruta_frame)

    # Superpone la imagen sobre la imagen principal
    imagen_resultante = imagen_principal.copy()
    imagen_resultante.paste(imagen_superpuesta, (px, py), imagen_superpuesta)
    
    # Agrega la imagen superpuesta a la lista de frames
    frames_superpuestos.append(np.array(imagen_resultante))

    # Cierra la imagen del frame actual
    imagen_superpuesta.close()

# Guarda los frames superpuestos como un GIF animado
imageio.mimsave("animacion.gif", frames_superpuestos, duration=1)  # Duración de 1 segundo entre cada frame

# Cierra la imagen principal
imagen_principal.close()
```

#### Procedimiento de Superposición

- Abre la imagen principal donde se superpondrán los fotogramas.
- Itera sobre los fotogramas rescalados del GIF.
- Superpone cada fotograma en la posición específica dentro de la imagen principal.
- Agrega cada fotograma superpuesto a una lista.
- Guarda la lista de fotogramas superpuestos como un GIF animado con una duración especificada entre cada fotograma.

## Detalles de Funcionamiento

El programa funciona de la siguiente manera:

1. El archivo `desmontar_gif.py` descompone un GIF en sus fotogramas individuales utilizando la función `desmontar_gif(archivo_gif)`.
2. El archivo `Rescalar.py` recorre los fotogramas desmontados del GIF y los redimensiona a un nuevo tamaño especificado.
3. El archivo `Imagen.py` superpone los fotogramas rescalados del GIF en una imagen principal para crear una animación. Luego guarda los fotogramas superpuestos como un GIF animado.
