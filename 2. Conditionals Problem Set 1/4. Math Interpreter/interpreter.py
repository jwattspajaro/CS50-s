# Define la función principal del programa
def main():
    # Pide al usuario que ingrese una expresión aritmética
    expression = input("Ingrese una expresión aritmética (x y z): ")

    # Divide la expresión en tres partes utilizando el espacio como separador
    x, y, z = expression.split(" ")

    # Convierte las partes x y z en enteros
    x = int(x)
    z = int(z)

    # Evalúa la operación indicada por el operador y y asigna el resultado a la variable result
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        if z == 0:
            # Imprime un mensaje de error si se intenta dividir por cero y finaliza la función
            print("Error: División por cero.")
            return
        result = x / z
    else:
        # Imprime un mensaje de error si se ingresa un operador inválido y finaliza la función
        print("Error: Operación inválida.")
        return

    # Imprime el resultado de la operación en la consola
    print(f"Resultado: {result:.1f}")


# Verifica si el archivo se está ejecutando directamente
if __name__ == "__main__":
    # Llama a la función principal solo si el archivo se está ejecutando directamente
    main()
# How to Test
# Here’s how to test your code manually:
# Run your program with python interpreter.py. Type 1 + 1 and press Enter. Your program should output:
# 2.0 
# Run your program with python interpreter.py. Type 2 - 3 and press Enter. Your program should output:
# -1.0
# Run your program with python interpreter.py. Type 2 * 2 and press Enter. Your program should output
# 4.0
# Run your program with python interpreter.py. Type 50 / 5 and press Enter. Your program should output
# 10.0