# Función principal para validar una placa de vehículo
def main():
    # Solicita al usuario que ingrese la placa
    plate = input("Plate: ")
    # Comprueba si la placa es válida o no utilizando la función is_valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Función para determinar si una placa de vehículo es válida
def is_valid(s):
    # Comprueba si la longitud de la placa es correcta
    if len(s) < 2 or len(s) > 6:
        return False

    # Comprueba si los dos primeros caracteres son letras
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Comprueba si los caracteres restantes son alfanuméricos
    if not s[2:].isalnum():
        return False

    # Comprueba si el último caracter es una letra después de un dígito
    if any(c.isdigit() for c in s[2:-1]) and s[-1].isalpha():
        return False

    # Comprueba si hay un 0 después de dos letras
    if '0' in s[2:]:
        first_number = s[2:].find('0')
        if first_number != -1 and s[:first_number + 2].isalpha():
            return False

    # Comprueba si hay una letra después de un dígito en la parte central
    for i in range(2, len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False

    # Si pasa todas las condiciones, la placa es válida
    return True

# Si el script se ejecuta directamente (no importado como módulo)
if __name__ == "__main__":
    # Llama a la función principal para iniciar la validación de la placa
    main()
