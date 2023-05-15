# Importar el módulo random
import random

# Definir la función principal del programa
def main():
    # Solicitar un nivel válido al usuario
    while True:
        try:
            level = int(input("Nivel: "))
            if level > 0:
                break
        except ValueError:
            pass

    # Generar un número aleatorio entre 1 y el nivel
    target = random.randint(1, level)

    # Continuar solicitando adivinanzas hasta que se adivine el número correcto
    while True:
        try:
            guess = int(input("Adivina: "))
            if guess < 1:
                continue

            if guess < target:
                print("Demasiado pequeño!")
            elif guess > target:
                print("Demasiado grande!")
            else:
                print("¡Exacto!")
                break
        except ValueError:
            pass

# Verificar si el archivo se está ejecutando como un programa independiente
if __name__ == "__main__":
    # Llamar a la función principal
    main()
