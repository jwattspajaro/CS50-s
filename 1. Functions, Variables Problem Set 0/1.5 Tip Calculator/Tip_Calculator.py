# Calculadora de propinas
# Y ahora mi calculadora de propinas Wizard.***
# Morty Seinfeld
# En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un restaurante, g
# eneralmente una cantidad igual al 15% o más del costo de su comida. Sin embargo, no se preocupe, 
# ¡hemos escrito una calculadora de propinas para usted, a continuación!
# * Bueno, hemos escrito la mayor parte de una calculadora de propinas para ti. Desafortunadamente, no tuvimos tiempo de implementar dos funciones:

# * dollars_to_float, que debería aceptar un str como entrada (formateado como `$##.##, donde cada uno #es un dígito decimal), 
# eliminar el inicial $y` devolver la cantidad como float. Por ejemplo, dado $50.00como entrada, debería devolver 50.0.
# percent_to_float, que debería aceptar un strcomo entrada (formateado como ##%, donde cada uno #es un dígito decimal), eliminar el final %y devolver el porcentaje como un float. Por ejemplo, dado 15%como entrada, debería devolver 0.15.
# Suponga que el usuario ingresará valores en los formatos esperados.

# * Sugerencias
# Recuerde que inputdevuelve un str, según https://docs.python.org/3/library/functions.html#input .
# Recuerde que floatpuede convertir a stra float, según https://docs.python.org/3/library/functions.html#float .
# Recuerde que a strviene con bastantes métodos, según https://docs.python.org/3/library/stdtypes.html#string-methods .

def main():
    # Lee el valor de la comida y lo convierte a un número decimal de punto flotante
    dollars = dollars_to_float(input("¿Cuánto costó la comida? "))

    # Lee el porcentaje de propina deseado y lo convierte a un número decimal de punto flotante
    percent = percent_to_float(input("¿Qué porcentaje desea dejar de propina? "))

    # Calcula el monto de la propina y lo almacena en la variable tip
    tip = dollars * percent

    # Imprime el monto de la propina en la salida estándar
    print(f"Deja ${tip:.2f}")

    # La sintaxis de las f-strings en Python 3 permite incluir expresiones dentro de cadenas de texto utilizando llaves {}. 
    # En este caso, la variable tip se incluye en la cadena de texto con {tip:.2f}, 
    # que significa que se imprimirá la variable tip con dos decimales de precisión después del punto decimal.

    # La letra f al principio de la cadena de texto indica que se trata de una f-string y que cualquier expresión dentro de llaves {} 
    # debe ser evaluada y convertida a una cadena de texto antes de imprimir.

def dollars_to_float(d):
    # Convierte la cadena de texto en un número decimal de punto flotante
    return float(d)  # Retorna el valor convertido


def percent_to_float(p):
    # Elimina el símbolo de porcentaje y convierte la cadena de texto en un número decimal de punto flotante
    return float(p.strip('%')) / 100  
    
    # Retorna el valor convertido
    #La función strip() es una función de cadena en Python que se utiliza para eliminar caracteres especificados 
    # del principio y el final de una cadena. En este caso, p.strip('%') elimina el símbolo de porcentaje
    # al final de la cadena p y devuelve una nueva cadena sin el porcentaje.


main()  # Ejecuta la función principal
