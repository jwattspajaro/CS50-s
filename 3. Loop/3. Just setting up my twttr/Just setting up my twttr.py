# Función para eliminar las vocales de un texto
def remove_vowels(text):
    # Define las vocales en una cadena de caracteres
    vowels = "AEIOUaeiou"
    # Crea una lista de caracteres que no sean vocales
    result = [char for char in text if char not in vowels]
    # Devuelve el texto sin vocales como una cadena
    return ''.join(result)

# Si el script se ejecuta directamente (no importado como módulo)
if __name__ == "__main__":
    # Solicita al usuario que ingrese un texto
    input_text = input("Ingresa el texto: ")
    # Elimina las vocales del texto ingresado usando la función remove_vowels
    output_text = remove_vowels(input_text)
    # Imprime el texto sin vocales
    print(output_text)

