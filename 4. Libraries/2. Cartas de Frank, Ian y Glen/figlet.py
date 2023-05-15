# Importar los módulos necesarios
import sys
import random
from pyfiglet import Figlet, FigletFont

# Definir la función principal del programa
def main():
    # Obtener el número de argumentos de la línea de comandos
    argc = len(sys.argv)

    # Verificar el número de argumentos de la línea de comandos
    if argc != 1 and argc != 3:
        print("Invalid usage")
        sys.exit(1)

    # Verificar si se proporcionó un nombre de fuente de forma explícita
    if argc == 3:
        # Verificar si el argumento es "-f" o "--font"
        if sys.argv[1] not in ("-f", "--font"):
            print("Invalid usage")
            sys.exit(1)
        
        # Obtener el nombre de la fuente especificada
        font_name = sys.argv[2]

        # Verificar si el nombre de la fuente es válido
        if font_name not in FigletFont.getFonts():
            print("Invalid usage")
            sys.exit(1)
    else:
        # Si no se proporcionó un nombre de fuente, elegir uno aleatoriamente
        font_name = random.choice(FigletFont.getFonts())

    # Solicitar al usuario que ingrese una cadena de texto
    text = input("Ingrese un texto: ")

    # Mostrar el texto en la fuente deseada
    figlet = Figlet(font=font_name)
    print(figlet.renderText(text))

# Verificar si el archivo se está ejecutando como un programa independiente
if __name__ == "__main__":
    # Llamar a la función principal
    main()
