from PIL import Image, ImageFilter


def antialiasing(file: str) -> Image:
    # Abrir la imagen original
    imagen_original = Image.open(file)

    # Aplicar el filtro gaussiano
    imagen_suavizada = imagen_original.filter(ImageFilter.GaussianBlur(
        radius=2))  # Puedes ajustar el radio según tus necesidades

    return imagen_suavizada


def main():
    # Ruta de la imagen que deseas suavizar
    # Cambia esto a la ruta de tu imagen
    ruta_imagen = "components/antialiasing/"

    # Aplicar antialiasing a la imagen
    imagen_suavizada = antialiasing(ruta_imagen)

    # Guardar la imagen suavizada
    nombre_imagen_suavizada = "mi_imagen_suavizada.jpg"
    imagen_suavizada.save(nombre_imagen_suavizada)
    print(f"Imagen suavizada guardada como {nombre_imagen_suavizada}")


if __name__ == "__main__":
    main()
