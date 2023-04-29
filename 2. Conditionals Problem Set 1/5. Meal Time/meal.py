# Función principal que lee la hora del usuario
def main():
    # Leer la hora del usuario en formato de 24 horas
    time = input("Enter the time (24-hour format): ")
    # Convertir la hora a un número de punto flotante
    hours_float = convert(time)

    # Verificar si la hora está dentro del intervalo para el desayuno
    if 7 <= hours_float <= 8:
        print("breakfast time")
    # Verificar si la hora está dentro del intervalo para el almuerzo
    elif 12 <= hours_float <= 13:
        print("lunch time")
    # Verificar si la hora está dentro del intervalo para la cena
    elif 18 <= hours_float <= 19:
        print("dinner time")
    # Si la hora no es de comida, no se imprime nada
    else:
        # No es hora de comer, por lo que no hay salida
        pass

# Función que convierte una hora en formato de 24 horas a un número de punto flotante
def convert(time):
    # Dividir la hora en horas y minutos
    hours, minutes = time.split(":")
    # Convertir horas y minutos a números de punto flotante y calcular el número total de horas
    hours_float = int(hours) + int(minutes) / 60
    # Devolver el número total de horas como punto flotante
    return hours_float

# Verifica si el archivo se está ejecutando directamente
if __name__ == "__main__":
    # Llama a la función main solo si el archivo se está ejecutando directamente
    main()

# ow to Test
# Here’s how to test your code manually:

# Run your program with python meal.py. Type 7:00 and press Enter. Your program should output:
# breakfast time   
# Run your program with python meal.py. Type 7:30 and press Enter. Your program should output:
# breakfast time
# Run your program with python meal.py. Type 12:42 and press Enter. Your program should output
# lunch time
# Run your program with python meal.py. Type 18:32 and press Enter. Your program should output
# dinner time
#Run your program with python meal.py. Type 11:11 and press Enter. Your program should output nothing
