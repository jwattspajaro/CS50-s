# Define la función principal del programa
def main():
    # Pide al usuario que ingrese el nombre del archivo
    filename = input("Por favor, ingrese el nombre del archivo: ")

    # Elimina espacios en blanco al principio y al final del nombre del archivo y convierte a minúsculas
    filename = filename.strip().lower()

    # Obtiene el tipo de medio del archivo
    media_type = get_media_type(filename)

    # Imprime el tipo de medio del archivo
    print(media_type)


# Define la función que obtiene el tipo de medio del archivo
def get_media_type(filename):
    # Obtiene la extensión del archivo
    extension = filename.split(".")[-1].lower()

    # Define un diccionario de tipos de medio y sus extensiones correspondientes
    media_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }

    # Busca la extensión del archivo en el diccionario de tipos de medio y devuelve el tipo de medio correspondiente
    # Si no se encuentra una coincidencia, devuelve "application/octet-stream" como tipo de medio predeterminado
    return media_types.get(extension, "application/octet-stream")


# Verifica si el archivo se está ejecutando directamente
if __name__ == "__main__":
    # Llama a la función principal solo si el archivo se está ejecutando directamente
    main()
