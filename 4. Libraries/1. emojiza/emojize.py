# Importar la función emojize del módulo emoji
from emoji import emojize

# Definir la función principal del programa
def main():
    # Solicitar al usuario que ingrese un texto en inglés
    english_text = input("Ingrese un texto: ")
    
    # Utilizar la función emojize para convertir el texto en emoji, utilizando alias
    emojized_text = emojize(english_text, language="alias")
    
    # Imprimir el resultado
    print("Resultado:", emojized_text)

# Verificar si el archivo se está ejecutando como un programa independiente
if __name__ == "__main__":
    # Llamar a la función principal
    main()
