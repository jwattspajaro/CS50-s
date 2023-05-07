
# Función para convertir un nombre de variable en CamelCase a snake_case
def camel_to_snake(name):
    # Inicializa una lista vacía para almacenar el nombre en snake_case
    snake_name = []
    # Itera a través de cada caracter en el nombre de la variable en CamelCase
    for char in name:
        # Si el caracter es mayúscula, agrega un guion bajo y el caracter en minúscula
        if char.isupper():
            snake_name.append('_')
            snake_name.append(char.lower())
        # Si el caracter es minúscula, lo agrega directamente a la lista
        else:
            snake_name.append(char)
    # Devuelve el nombre en snake_case como una cadena
    return ''.join(snake_name)

# Si el script se ejecuta directamente (no importado como módulo)
if __name__ == "__main__":
    # Solicita al usuario que ingrese un nombre de variable en CamelCase
    camel_name = input("Introduce el nombre de la variable en CamelCase: ")
    # Convierte el nombre de CamelCase a snake_case usando la función camel_to_snake
    snake_name = camel_to_snake(camel_name)
    # Imprime el nombre convertido en snake_case
    print(snake_name)
