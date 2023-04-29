# Función para verificar si la entrada es "42" o "fortytwo"
def is_deep_answer(input_str):
    # Limpie la entrada eliminando espacios y guiones y convirtiéndola a minúsculas
    cleaned_input = input_str.strip().lower().replace(" ", "").replace("-", "")
    
    # Aquí se están utilizando varios métodos de cadena para "limpiar" la entrada del usuario. 
    # Esto se hace para asegurarse de que la entrada sea consistente y no contenga caracteres innecesarios 
    # o espacios en blanco que puedan afectar la verificación.

    #strip(): elimina cualquier espacio en blanco al principio y al final de la cadena input_str.
    #lower(): convierte toda la cadena a minúsculas, lo que permite hacer comparaciones de forma insensible a mayúsculas y minúsculas.
    #replace(" ", ""): elimina todos los espacios en blanco de la cadena.
    #replace("-", ""): elimina todos los guiones de la cadena.
    #En resumen, esta línea de código limpia la entrada del usuario eliminando espacios en blanco y guiones, 
    # convirtiéndola a minúsculas y almacenando la cadena resultante en la variable cleaned_input.
    
    # Verifique si la entrada limpia es igual a "42" o "fortytwo"
    if cleaned_input == "42" or cleaned_input == "fortytwo":

    #
        # Devuelve verdadero si la entrada es igual a "42" o "fortytwo"
        return True
    # Devuelve falso si la entrada no es igual a "42" o "fortytwo"
    return False

# Función principal que pide al usuario una entrada
def main():
    user_input = input("Ingrese un número o una cadena: ")
    # Llama a la función is_deep_answer con la entrada del usuario
    if is_deep_answer(user_input):
        print("Yes")
    else:
        print("No")

# Verifica si el archivo se está ejecutando directamente
if __name__ == "__main__":
    # Llama a la función main solo si el archivo se está ejecutando directamente
    main()
