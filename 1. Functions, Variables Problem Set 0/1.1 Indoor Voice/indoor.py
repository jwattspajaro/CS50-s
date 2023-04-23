def indoor_voice():
    # Solicita al usuario que ingrese una cadena
    user_input = input("Por favor ingrese una cadena: ")
    # Convierte la cadena ingresada a minúsculas
    lowercase_input = user_input.lower()
    # Imprime la cadena en minúsculas
    print(lowercase_input)

# Verifica si el archivo se está ejecutando como un programa principal
if __name__ == '__main__':
    # Llamada a la función indoor_voice
    indoor_voice()
