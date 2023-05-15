def remove_vowels(text):
    """
    Esta función recibe un texto y elimina todas las vocales (mayúsculas y minúsculas) del mismo.
    
    Parámetros:
        - text: El texto del cual se eliminarán las vocales.
    
    Retorna:
        - Un nuevo string que es el resultado de eliminar las vocales del texto original.
    """
    vowels = "AEIOUaeiou"
    result = [char for char in text if char not in vowels]
    return ''.join(result)

if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Solicita al usuario que ingrese un texto, llama a la función remove_vowels() para eliminar las vocales
    y luego imprime el resultado.
    """
    input_text = input("Ingresa el texto: ")
    output_text = remove_vowels(input_text)
    print(output_text)
