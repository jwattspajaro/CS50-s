def main():
    """
    Esta función es la función principal del programa.
    Solicita al usuario que ingrese un saludo, llama a la función value() para obtener el valor del saludo
    y luego imprime el valor obtenido.
    """
    greeting = input("Ingresa un saludo: ")
    amount = value(greeting)
    print(f"Valor del saludo: {amount}")

def value(greeting):
    """
    Esta función recibe un saludo y devuelve un valor numérico asociado al mismo.
    
    Parámetros:
        - greeting: El saludo del cual se desea obtener el valor.
        
    Retorna:
        - Un número que representa el valor asociado al saludo.
    """
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    """
    Punto de entrada del programa.
    Llama a la función main() para iniciar la ejecución del programa.
    """
    main()

# Pruebas unitarias
import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello, how are you?") == 0
    assert value("hElLo") == 0

def test_value_h():
    assert value("hi") == 20
    assert value("Hooray!") == 20
    assert value("Howdy!") == 20

def test_value_other():
    assert value("What's up?") == 100
    assert value("Greetings!") == 100
    assert value("Good day!") == 100
