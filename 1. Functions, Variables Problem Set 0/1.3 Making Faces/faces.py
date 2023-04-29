# Haciendo caras
# Antes de que existieran los emoji, existían los emoticonos , 
# en los que el texto como :)era una cara feliz y 
# el texto como :(era una cara triste. ¡Hoy en día, los programas tienden a convertir los emoticonos en emoji automáticamente!

# En un archivo llamado faces.py, 
# implemente una función llamada convertque acepte a str
# como entrada y devuelva esa misma entrada con cualquier :)
# conversión a 🙂(también conocida como cara ligeramente sonriente ) 
# y cualquier :(conversión a 🙁(también conocida como cara ligeramente fruncida ). 
# El resto del texto debe devolverse sin cambios.

# Luego, en ese mismo archivo, implemente una función 
# llamada mainque solicite al usuario una entrada, 
# llame converta esa entrada e imprima el resultado.  
# Le invitamos, pero no es obligatorio, 
# a solicitar al usuario de forma explícita, como al pasar uno str
# propio como argumento a input. Asegúrese de llamar mainal final de su archivo.

# Sugerencias
# Recuerde que inputdevuelve un str, según 
# docs.python.org/3/library/functions.html#input .
# Recuerde que a strviene con bastantes métodos, 
# según docs.python.org/3/library/stdtypes.html#string-methods .
# Un emoji es en realidad solo un carácter, 
# por lo que puede citarlo como cualquier str, a la . 
# Y puede copiar y pegar el emoji de esta página en su propio código según sea necesario."😐"

# Define la función convert
def convert(cadena):
    # Reemplaza los emoticonos :) con 🙂 y :( con 🙁
    cadena = cadena.replace(":)", "🙂").replace(":(", "🙁")
    # Devuelve la cadena convertida
    return cadena

# Define la función main
def main():
    # Pide al usuario que introduzca una cadena
    cadena = input("Introduce una cadena: ")
    # Llama a la función convert y almacena el resultado en una variable
    resultado = convert(cadena)
    # Imprime el resultado
    print(resultado)

# Llama a la función main al final del archivo
if __name__ == "__main__":
    main()

