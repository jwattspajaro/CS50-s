import sys  # Importa el módulo sys para manejar los argumentos de la línea de comandos
import os  # Importa el módulo os para verificar la existencia del archivo

def main():
    # Verifica si se proporciona exactamente un argumento en la línea de comandos
    if len(sys.argv) != 2:
        print("Faltan argumentos en la línea de comandos")
        sys.exit(1)

    file_path = sys.argv[1]  # Guarda el nombre del archivo proporcionado como argumento

    # Verifica si el archivo tiene una extensión .py
    if not file_path.endswith(".py"):
        print("No es un archivo de Python")
        sys.exit(1)

    # Verifica si el archivo existe
    if not os.path.exists(file_path):
        print("El archivo no existe")
        sys.exit(1)

    # Cuenta las líneas de código en el archivo, excluyendo comentarios y líneas en blanco
    with open(file_path, 'r') as file:  # Abre el archivo en modo lectura
        lines_of_code = 0  # Inicializa el contador de líneas de código
        for line in file:  # Itera sobre cada línea del archivo
            stripped_line = line.lstrip()  # Elimina los espacios en blanco iniciales de la línea
            # Verifica si la línea no es un comentario, no está en blanco y no está vacía
            if not stripped_line.startswith("#") and not stripped_line.isspace() and stripped_line != "":
                lines_of_code += 1  # Incrementa el contador de líneas de código

    # Imprime el número de líneas de código
    print(lines_of_code)

if __name__ == "__main__":
    main()  # Ejecuta la función main
