

import re  # Importamos la biblioteca de expresiones regulares

def main():
    # Imprimimos el resultado de la función 'validate' para la dirección IPv4 ingresada por el usuario
    print(validate(input("Dirección IPv4: ")))

def validate(ip):
    # Definimos la expresión regular para validar direcciones IPv4 en notación decimal con puntos
    regex = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"

    # Buscamos si la dirección IP ingresada coincide con la expresión regular
    match = re.search(r"^" + regex + "\." + regex + "\." + regex + "\." + regex + "$", ip)

    # Si se encuentra una coincidencia, devuelve True; de lo contrario, devuelve False
    if match:
        return True
    else:
        return False
    
# El código importa el módulo re, que proporciona soporte para expresiones regulares. Define dos funciones: principal y validar.
# La función principal solicita al usuario que ingrese una dirección IPv4 y luego llama a la función de validación con la dirección ingresada como argumento.
# Luego se imprime el resultado de la función de validación.
# La función de validación toma una dirección IPv4 como entrada y usa una expresión regular para validarla.
# La expresión regular se almacena en la variable regex y representa el patrón para una dirección IPv4 válida
