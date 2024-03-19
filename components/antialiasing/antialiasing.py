from PIL import Image, ImageFilter
import os


def antialising(file: str) -> Image:
    # Abrir la imagen original
    file = Image.open(file)

    # Aplicar el filtro gaussiano
    alias_file = file.filter(ImageFilter.GaussianBlur(
        radius=2))  # Puedes ajustar el radio según tus necesidades

    return alias_file
