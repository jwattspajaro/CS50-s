import random

# Definir la función principal del programa
def main():
    # Obtener el nivel de dificultad del usuario
    level = get_level()

    # Inicializar la puntuación
    score = 0

    # Realizar 10 preguntas
    for _ in range(10):
        # Generar dos números aleatorios
        x = generate_integer(level)
        y = generate_integer(level)

        # Calcular la respuesta correcta
        correct_answer = x + y

        # Mostrar la pregunta al usuario
        print(f"{x} + {y} =", end=" ")

        # Realizar hasta 3 intentos
        attempts = 3
        while attempts > 0:
            try:
                # Leer la respuesta del usuario
                answer = int(input())
                if answer == correct_answer:
                    # Si la respuesta es correcta, incrementar la puntuación y salir del bucle
                    score += 1
                    break
                else:
                    # Si la respuesta es incorrecta, reducir los intentos y mostrar un mensaje de error
                    attempts -= 1
                    print("EEE", end=" ")
            except ValueError:
                # Si se produce un error al convertir la entrada a entero, reducir los intentos y mostrar un mensaje de error
                attempts -= 1
                print("EEE", end=" ")

        if attempts == 0:
            # Si se agotan los intentos, mostrar la respuesta correcta
            print(correct_answer)

    # Mostrar la puntuación final
    print(f"Puntuación: {score}")

# Obtener el nivel de dificultad del usuario
def get_level():
    while True:
        try:
            level = int(input("Nivel: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

# Generar un número entero aleatorio según el nivel de dificultad
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

# Verificar si el archivo se está ejecutando como un programa independiente
if __name__ == "__main__":
    # Llamar a la función principal
    main()
