import os
import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        print("Uso: python shirt.py input_image.jpg output_image.jpg")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]
    shirt_image_path = "shirt.png"

    # Obtener la extensión de los archivos de entrada y salida
    input_ext = os.path.splitext(input_image_path)[1].lower()
    output_ext = os.path.splitext(output_image_path)[1].lower()

    # Comprobar las extensiones de los archivos de entrada y salida
    if input_ext != output_ext or input_ext not in ['.jpg', '.jpeg', '.png']:
        print("Error: Las extensiones de los archivos de entrada y salida deben ser .jpg, .jpeg o .png y deben coincidir.")
        sys.exit(1)

    try:
        input_image = Image.open(input_image_path)
    except FileNotFoundError:
        print("Error: El archivo de entrada no existe.")
        sys.exit(1)

    # Abrir la imagen de la camiseta
    shirt_image = Image.open(shirt_image_path)
    shirt_size = shirt_image.size

    # Recortar la imagen de entrada para que coincida con el tamaño de la camiseta
    cropped_input_image = ImageOps.fit(input_image, shirt_size)

    # Pegar la imagen de la camiseta en la imagen de entrada recortada
    cropped_input_image.paste(shirt_image, (0, 0), shirt_image)

    # Guardar la imagen resultante
    cropped_input_image.save(output_image_path)

if __name__ == "__main__":
    main()
